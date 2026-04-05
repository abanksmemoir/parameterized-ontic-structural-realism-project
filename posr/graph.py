"""
Graph operations: build, traverse, validate, and propagate changes.

This module provides higher-level operations on theory graphs beyond
the basic topological sort and ancestor/descendant queries.

Design intent (plug-and-play):
    The core operation is: take a resolved TheoryFile, change one parametric
    choice, and produce a new TheoryFile. resolve_parametric_choices() handles
    the "make choices" step; propagate_change() identifies which downstream
    nodes are affected. Together they support the plug-and-play workflow:

        load theory → toggle parameter → propagate → save as new file

    Currently propagate_change() only identifies affected nodes — it does not
    recompute their content. When external tools are wired in (GAP for group
    theory, FeynRules for Lagrangians, etc.), propagation will trigger actual
    recomputation at each affected node via its tool binding. For now, it
    serves as the structural skeleton for that future capability.

    The key invariant: changing a parametric choice at node N should never
    silently leave a downstream node unchanged if that node's structural
    content depends on the changed provision. The system should either
    recompute or flag as stale. This is the "functorial composition"
    requirement from the project briefing.
"""

from typing import Dict, List, Set, Optional, Any, Callable
from .schema import TheoryGraph, Node, ParametricSlot, TheoryFile, ForkPoint
from datetime import datetime


def build_from_json(json_path_or_data) -> TheoryGraph:
    """Build a TheoryGraph from the old JSON format (sm_dependency_graph.json).

    The old format has nodes organized by layers. This function flattens
    and converts to the new schema, inferring structural_type from context.

    Args:
        json_path_or_data: Either a file path string or a dict of JSON data.

    Returns:
        A TheoryGraph object.
    """
    import json as json_module
    from .schema import TheoryGraphMeta

    # Handle both file path and dict input
    if isinstance(json_path_or_data, str):
        with open(json_path_or_data, 'r') as f:
            json_data = json_module.load(f)
    else:
        json_data = json_path_or_data

    meta_data = json_data.get("meta", {})
    meta = TheoryGraphMeta(
        name=meta_data.get("project", "Unknown"),
        description=meta_data.get("description", ""),
        version=meta_data.get("version", "0.1.0"),
        date=meta_data.get("date", datetime.utcnow().isoformat()),
    )

    graph = TheoryGraph(meta)

    # Map layer index to structural type
    layer_type_map = {
        0: "logic",
        1: "foundation",
        2: "algebraic_structure",
        3: "analytic_structure",
        4: "algebraic_structure",  # Lie theory
        5: "geometric_structure",
        6: "analytic_structure",  # Functional analysis
        7: "dynamical_principle",
        8: "quantization",
        9: "physical_theory",
    }

    for layer in json_data.get("layers", []):
        layer_idx = layer.get("index", 0)
        structural_type = layer_type_map.get(layer_idx, "unknown")

        for node_data in layer.get("nodes", []):
            # Convert parametric descriptions to ParametricSlot objects
            parametric_slots = []
            for param_desc in node_data.get("parametric", []):
                # Parse the description to extract name and default if present
                # Example: "LEM can be dropped → intuitionistic"
                parts = param_desc.split("→")
                name = parts[0].strip().split()[-1].lower() if parts else "param"
                slot_type = "architectural" if "drop" in param_desc or "change" in param_desc.lower() else "runtime"

                parametric_slots.append(
                    ParametricSlot(
                        name=name,
                        description=param_desc,
                        slot_type=slot_type,
                        known_options=None,
                        default=None,
                    )
                )

            node = Node(
                id=node_data["id"],
                structural_type=structural_type,
                label=node_data["label"],
                description=node_data["description"],
                presupposes=node_data.get("presupposes", []),
                provides=node_data.get("provides", []),
                parametric_slots=parametric_slots,
            )
            graph.add_node(node)

    graph.validate()
    return graph


def resolve_parametric_choices(
    graph: TheoryGraph,
    choices: Dict[str, Dict[str, Any]],
) -> TheoryFile:
    """Create a TheoryFile by resolving parametric choices at each node.

    Args:
        graph: The base TheoryGraph.
        choices: Dict of {node_id: {slot_name: chosen_value, ...}}

    Returns:
        A TheoryFile with all resolved values and provenance.
    """
    # Create a deep copy of the graph
    import copy

    new_graph = copy.deepcopy(graph)

    fork_provenance = []

    for node_id, choice_dict in choices.items():
        if node_id not in new_graph.nodes:
            raise KeyError(f"Node {node_id} not found in graph.")

        node = new_graph.nodes[node_id]
        node.resolved_values = choice_dict

        # Record fork point provenance
        alternatives = {}
        for slot_name, chosen_value in choice_dict.items():
            # Find the slot definition
            slot = next((s for s in node.parametric_slots if s.name == slot_name), None)
            if slot and slot.known_options:
                alternatives[slot_name] = [o for o in slot.known_options if o != chosen_value]
            else:
                alternatives[slot_name] = []

        if alternatives:
            fork_provenance.append(
                ForkPoint(
                    node_id=node_id,
                    chosen=choice_dict,
                    alternatives=alternatives,
                )
            )

    return TheoryFile(
        theory_graph=new_graph,
        fork_provenance=fork_provenance,
    )


def propagate_change(
    graph: TheoryGraph,
    node_id: str,
    changed_provisions: List[str],
    callback: Optional[Callable[[str, List[str]], None]] = None,
) -> Set[str]:
    """Propagate a change at a node upward through the graph.

    When a node's structural content changes (e.g., from classical logic to
    intuitionistic), this function identifies all dependent nodes that might
    be affected.

    Args:
        graph: The TheoryGraph.
        node_id: The node where the change occurred.
        changed_provisions: List of provisions that changed.
        callback: Optional callback(affected_node_id, changed_provisions) for each affected node.

    Returns:
        Set of all affected node IDs (including node_id itself).
    """
    affected = {node_id}
    queue = [node_id]

    while queue:
        current = queue.pop(0)
        # Find all nodes that depend on this one
        for other_id, other_node in graph.nodes.items():
            if current in other_node.presupposes and other_id not in affected:
                affected.add(other_id)
                queue.append(other_id)
                if callback:
                    callback(other_id, changed_provisions)

    return affected


def validate_consistency(graph: TheoryGraph) -> List[str]:
    """Check a graph for structural inconsistencies.

    Returns:
        List of error messages (empty if valid).
    """
    errors = []

    # Check for cycles
    try:
        graph.topological_sort()
    except ValueError as e:
        errors.append(str(e))

    # Check that all presupposes are satisfied
    all_ids = set(graph.nodes.keys())
    for node_id, node in graph.nodes.items():
        for presupposed in node.presupposes:
            if presupposed not in all_ids:
                errors.append(
                    f"Node {node_id} presupposes {presupposed}, which is not in the graph."
                )

    return errors


def compare_structures(
    graph1: TheoryGraph,
    graph2: TheoryGraph,
) -> Dict[str, Any]:
    """Compare two theory graphs and identify shared structure and fork points.

    Args:
        graph1: First theory graph.
        graph2: Second theory graph.

    Returns:
        A dict with keys:
          - 'shared_nodes': Set of node IDs in both graphs
          - 'shared_graph': TheoryGraph of shared nodes
          - 'graph1_only': Set of node IDs only in graph1
          - 'graph2_only': Set of node IDs only in graph2
          - 'fork_points': List of node IDs where parametric choices differ
    """
    all_ids_1 = set(graph1.nodes.keys())
    all_ids_2 = set(graph2.nodes.keys())

    shared_ids = all_ids_1 & all_ids_2
    graph1_only = all_ids_1 - all_ids_2
    graph2_only = all_ids_2 - all_ids_1

    # Find fork points: nodes in both graphs with different resolved values
    fork_points = []
    for node_id in shared_ids:
        node1 = graph1.nodes[node_id]
        node2 = graph2.nodes[node_id]
        if node1.resolved_values != node2.resolved_values:
            fork_points.append(node_id)

    # Extract shared subgraph
    shared_graph = graph1.shared_subgraph(graph2)

    return {
        "shared_nodes": shared_ids,
        "shared_graph": shared_graph,
        "graph1_only": graph1_only,
        "graph2_only": graph2_only,
        "fork_points": fork_points,
    }


def find_deepest_chain(graph: TheoryGraph) -> List[str]:
    """Find the longest path through the graph (most constrained chain).

    This is the deepest dependency chain — every link is a potential
    parametric swap point.

    Returns:
        List of node IDs from a root (no presupposes) to a deepest leaf.
    """
    topo_order = graph.topological_sort()
    root_nodes = [nid for nid in topo_order if not graph.nodes[nid].presupposes]

    def dfs(node_id: str, visited: Set[str]) -> List[str]:
        visited.add(node_id)
        node = graph.nodes[node_id]

        # Find dependents
        dependents = [
            other_id
            for other_id in graph.nodes
            if node_id in graph.nodes[other_id].presupposes
        ]

        if not dependents:
            return [node_id]

        longest = []
        for dep in dependents:
            if dep not in visited:
                path = dfs(dep, visited)
                if len(path) + 1 > len(longest):
                    longest = [node_id] + path

        visited.remove(node_id)
        return longest

    all_chains = []
    for root in root_nodes:
        chain = dfs(root, set())
        all_chains.append(chain)

    return max(all_chains, key=len) if all_chains else []
