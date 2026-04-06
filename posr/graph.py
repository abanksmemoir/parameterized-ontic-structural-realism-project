"""
Graph operations: build, traverse, validate, and propagate changes (V2).

Handles both V2 JSON format (typed parameters, typed dependencies) and
legacy V1 format (string presupposes, parametric descriptions).

Design intent (plug-and-play):
    The core operation is: take a resolved TheoryFile, change one parametric
    choice, and produce a new TheoryFile. resolve_parametric_choices() handles
    the "make choices" step; propagate_change() identifies which downstream
    nodes are affected. Together they support the plug-and-play workflow:

        load theory → toggle parameter → propagate → save as new file

    propagate_change() now tracks dependency type: a change at a node
    connected via a contingent dependency may or may not propagate depending
    on whether the contingent condition holds.
"""

from typing import Dict, List, Set, Optional, Any, Callable
from .schema import (
    TheoryGraph, TheoryGraphMeta, Node, Parameter, Dependency,
    TheoryFile, ForkPoint, PARAMETER_SUBTYPES, DEPENDENCY_TYPES,
)
from datetime import datetime


def build_from_json(json_path_or_data) -> TheoryGraph:
    """Build a TheoryGraph from JSON (handles both V1 and V2 formats).

    V2 format: nodes have 'parameters' (typed) and 'dependencies' (typed).
    V1 format: nodes have 'parametric' (strings) and 'presupposes' (string list).

    Args:
        json_path_or_data: Either a file path string or a dict of JSON data.

    Returns:
        A TheoryGraph object.
    """
    import json as json_module

    if isinstance(json_path_or_data, str):
        with open(json_path_or_data, 'r') as f:
            json_data = json_module.load(f)
    else:
        json_data = json_path_or_data

    meta_data = json_data.get("meta", {})
    version = meta_data.get("version", "1.0.0")

    meta = TheoryGraphMeta(
        name=meta_data.get("project", meta_data.get("name", "Unknown")),
        description=meta_data.get("description", ""),
        version=version,
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
        6: "analytic_structure",   # Functional analysis
        7: "dynamical_principle",
        8: "quantization",
        9: "physical_theory",
    }

    for layer in json_data.get("layers", []):
        layer_idx = layer.get("index", 0)
        structural_type = layer_type_map.get(layer_idx, "unknown")

        for node_data in layer.get("nodes", []):
            node_id = node_data["id"]

            # Parse dependencies (V2: typed objects; V1: string list)
            dependencies = []
            if "dependencies" in node_data:
                for dep_data in node_data["dependencies"]:
                    if isinstance(dep_data, dict):
                        dependencies.append(Dependency.from_dict(dep_data))
                    elif isinstance(dep_data, str):
                        dependencies.append(
                            Dependency(on=dep_data, dependency_type="logical")
                        )
            elif "presupposes" in node_data:
                for dep_id in node_data["presupposes"]:
                    dependencies.append(
                        Dependency(on=dep_id, dependency_type="logical")
                    )

            # Parse parameters (V2: typed objects; V1: description strings)
            parameters = []
            if "parameters" in node_data:
                for param_data in node_data["parameters"]:
                    if isinstance(param_data, dict) and "type" in param_data:
                        parameters.append(Parameter.from_dict(param_data))
                    elif isinstance(param_data, str):
                        parameters.append(_parse_legacy_parametric(
                            param_data, len(parameters), node_id
                        ))
            elif "parametric" in node_data:
                for i, desc in enumerate(node_data["parametric"]):
                    parameters.append(_parse_legacy_parametric(desc, i, node_id))

            node = Node(
                id=node_id,
                structural_type=structural_type,
                label=node_data["label"],
                description=node_data.get("description", ""),
                dependencies=dependencies,
                provides=node_data.get("provides", []),
                parameters=parameters,
                temporal_note=node_data.get("temporal_note"),
                contingent_provisions=node_data.get("contingent_provisions", []),
            )
            graph.add_node(node)

    graph.validate()
    return graph


def _parse_legacy_parametric(desc: str, index: int, node_id: str) -> Parameter:
    """Parse a V1 parametric description string into a Parameter."""
    parts = desc.split("→")
    name = parts[0].strip().split()[-1].lower() if parts else f"param_{index}"

    return Parameter(
        id=f"P_{node_id}_{index}",
        name=name,
        parameter_type="structural",  # best guess for legacy
        value=None,
        alternatives=None,
        note=f"Legacy: {desc}",
    )


def resolve_parametric_choices(
    graph: TheoryGraph,
    choices: Dict[str, Dict[str, Any]],
) -> TheoryFile:
    """Create a TheoryFile by resolving parametric choices at each node.

    Args:
        graph: The base TheoryGraph.
        choices: Dict of {node_id: {param_name_or_id: chosen_value, ...}}

    Returns:
        A TheoryFile with all resolved values and provenance.
    """
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
        for param_key, chosen_value in choice_dict.items():
            param = next(
                (p for p in node.parameters
                 if p.id == param_key or p.name == param_key),
                None
            )
            if param and param.alternatives:
                alternatives[param_key] = [
                    a for a in param.alternatives if a != chosen_value
                ]
            else:
                alternatives[param_key] = []

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
    skip_contingent: bool = False,
) -> Set[str]:
    """Propagate a change at a node upward through the graph.

    Args:
        graph: The TheoryGraph.
        node_id: The node where the change occurred.
        changed_provisions: List of provisions that changed.
        callback: Optional callback(affected_node_id, changed_provisions).
        skip_contingent: If True, don't propagate through contingent dependencies.

    Returns:
        Set of all affected node IDs (including node_id itself).
    """
    affected = {node_id}
    queue = [node_id]

    while queue:
        current = queue.pop(0)
        for other_id, other_node in graph.nodes.items():
            if other_id in affected:
                continue
            for dep in other_node.dependencies:
                if dep.on == current:
                    if skip_contingent and dep.dependency_type == "contingent":
                        continue
                    affected.add(other_id)
                    queue.append(other_id)
                    if callback:
                        callback(other_id, changed_provisions)
                    break

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

    # Check that all dependencies are satisfied
    all_ids = set(graph.nodes.keys())
    for node_id, node in graph.nodes.items():
        for dep in node.dependencies:
            if dep.on not in all_ids:
                errors.append(
                    f"Node {node_id} depends on {dep.on}, which is not in the graph."
                )

    # V2 checks: validate parameter types
    for node_id, node in graph.nodes.items():
        for param in node.parameters:
            if param.parameter_type not in PARAMETER_SUBTYPES:
                errors.append(
                    f"Node {node_id}, parameter {param.id}: "
                    f"invalid type '{param.parameter_type}'"
                )
        for dep in node.dependencies:
            if dep.dependency_type not in DEPENDENCY_TYPES:
                errors.append(
                    f"Node {node_id}, dependency on {dep.on}: "
                    f"invalid type '{dep.dependency_type}'"
                )

    return errors


def compare_structures(
    graph1: TheoryGraph,
    graph2: TheoryGraph,
) -> Dict[str, Any]:
    """Compare two theory graphs and identify shared structure and fork points."""
    all_ids_1 = set(graph1.nodes.keys())
    all_ids_2 = set(graph2.nodes.keys())

    shared_ids = all_ids_1 & all_ids_2
    graph1_only = all_ids_1 - all_ids_2
    graph2_only = all_ids_2 - all_ids_1

    fork_points = []
    for node_id in shared_ids:
        node1 = graph1.nodes[node_id]
        node2 = graph2.nodes[node_id]
        if node1.resolved_values != node2.resolved_values:
            fork_points.append(node_id)

    shared_graph = graph1.shared_subgraph(graph2)

    return {
        "shared_nodes": shared_ids,
        "shared_graph": shared_graph,
        "graph1_only": graph1_only,
        "graph2_only": graph2_only,
        "fork_points": fork_points,
    }


def find_deepest_chain(graph: TheoryGraph) -> List[str]:
    """Find the longest path through the graph (most constrained chain)."""
    topo_order = graph.topological_sort()
    root_nodes = [nid for nid in topo_order if not graph.nodes[nid].dependencies]

    def dfs(node_id: str, visited: Set[str]) -> List[str]:
        visited.add(node_id)

        dependents = [
            other_id
            for other_id in graph.nodes
            if node_id in graph.nodes[other_id].dependency_ids()
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
