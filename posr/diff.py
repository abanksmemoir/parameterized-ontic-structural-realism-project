"""
Cross-theory structural comparison.

Identifies shared subgraphs, fork points, and theory-specific branches
between different theory-graphs (e.g., SM vs GR).

Design intent:
    The primary application is comparing theory-files to make structural
    relationships precise and visible. When you diff SM and GR, the system
    should show you exactly which nodes they share (logic through manifolds),
    exactly where they fork (connection type: internal gauge bundle vs tangent
    bundle), and exactly what each branch adds that the other doesn't.

    This is not just a code utility — it's the project's main analytical
    instrument. The claim that SM and GR "reduplicate" connection/curvature
    machinery on different bundles, and that unification proposals amount to
    collapsing that reduplication into shared ancestry, is a claim the diff
    operation makes testable.

    Contemplated extensions:
    - Overlay mode: given two theory-files, produce a merged visualization
      showing shared subgraph, fork point, and divergent branches
    - Unification testing: given a proposed unification theory-file, verify
      that SM and GR are both derivable as parametric specializations of it
    - Lattice navigation: given a collection of theory-files, compute the
      full lattice structure (which theories are parametric neighbors, which
      share the most upstream structure, etc.)
"""

from typing import Dict, List, Set, Any, Optional, Tuple
from .schema import TheoryGraph, Node
from dataclasses import dataclass


@dataclass
class StructuralDiff:
    """Result of comparing two theory graphs."""

    name1: str
    """Name of first theory."""

    name2: str
    """Name of second theory."""

    shared_nodes: Set[str]
    """Node IDs in both theories."""

    theory1_only: Set[str]
    """Node IDs only in theory 1."""

    theory2_only: Set[str]
    """Node IDs only in theory 2."""

    fork_points: Dict[str, Tuple[Dict[str, Any], Dict[str, Any]]]
    """Nodes where resolved values differ: {node_id: (values1, values2)}"""

    shared_depth: int
    """Topological depth of shared subgraph."""

    fork_depth: int
    """Topological depth at which fork occurs."""

    def summary(self) -> str:
        """Human-readable summary of the structural difference."""
        lines = [
            f"Structural Comparison: {self.name1} vs {self.name2}",
            "",
            f"Shared structure: {len(self.shared_nodes)} nodes",
            f"  {self.name1}-only: {len(self.theory1_only)} nodes",
            f"  {self.name2}-only: {len(self.theory2_only)} nodes",
            f"  Fork points (parametric differences): {len(self.fork_points)} nodes",
            "",
            f"Shared depth: {self.shared_depth}",
            f"Fork occurs at depth: {self.fork_depth}",
        ]

        if self.fork_points:
            lines.append("")
            lines.append("Fork points:")
            for node_id, (vals1, vals2) in self.fork_points.items():
                lines.append(f"  {node_id}:")
                lines.append(f"    {self.name1}: {vals1}")
                lines.append(f"    {self.name2}: {vals2}")

        return "\n".join(lines)


def compute_structural_diff(graph1: TheoryGraph, graph2: TheoryGraph) -> StructuralDiff:
    """Compute the structural difference between two theories.

    Args:
        graph1: First TheoryGraph.
        graph2: Second TheoryGraph.

    Returns:
        StructuralDiff object.
    """
    all_ids_1 = set(graph1.nodes.keys())
    all_ids_2 = set(graph2.nodes.keys())

    shared_ids = all_ids_1 & all_ids_2
    theory1_only = all_ids_1 - all_ids_2
    theory2_only = all_ids_2 - all_ids_1

    # Find fork points: nodes where resolved values differ
    fork_points: Dict[str, Tuple[Dict[str, Any], Dict[str, Any]]] = {}
    for node_id in shared_ids:
        node1 = graph1.nodes[node_id]
        node2 = graph2.nodes[node_id]
        if node1.resolved_values != node2.resolved_values:
            fork_points[node_id] = (node1.resolved_values, node2.resolved_values)

    # Compute depth of shared subgraph by looking at topological distances
    shared_depth = 0
    if shared_ids:
        # Build the subgraph induced by shared nodes
        shared_graph = graph1.shared_subgraph(graph2)
        try:
            topo = shared_graph.topological_sort()
            shared_depth = len(topo)
        except ValueError:
            shared_depth = 0

    # Find fork depth: the shallowest node where a fork occurs
    fork_depth = float("inf")
    if fork_points:
        for node_id in fork_points.keys():
            # Count distance from a root node (presupposes nothing)
            depth = _compute_depth(graph1, node_id)
            fork_depth = min(fork_depth, depth)
    if fork_depth == float("inf"):
        fork_depth = 0

    return StructuralDiff(
        name1=graph1.meta.name,
        name2=graph2.meta.name,
        shared_nodes=shared_ids,
        theory1_only=theory1_only,
        theory2_only=theory2_only,
        fork_points=fork_points,
        shared_depth=shared_depth,
        fork_depth=int(fork_depth),
    )


def _compute_depth(graph: TheoryGraph, node_id: str) -> int:
    """Compute topological depth of a node (distance from roots).

    A root node (no presupposes) has depth 0.
    A node with depth depends on the maximum depth of its presupposes + 1.
    """
    memo = {}

    def dfs(nid: str) -> int:
        if nid in memo:
            return memo[nid]

        node = graph.nodes[nid]
        if not node.presupposes:
            result = 0
        else:
            result = 1 + max(dfs(p) for p in node.presupposes)

        memo[nid] = result
        return result

    return dfs(node_id)


def extract_shared_subgraph(
    graph1: TheoryGraph, graph2: TheoryGraph
) -> TheoryGraph:
    """Extract the largest common subgraph shared by both theories.

    Only includes nodes that appear in both and have compatible presupposes.

    Returns:
        A new TheoryGraph containing only shared nodes.
    """
    return graph1.shared_subgraph(graph2)


def identify_fork_path(
    graph1: TheoryGraph, graph2: TheoryGraph
) -> Optional[List[str]]:
    """Identify the path from a shared root to the first fork point.

    The fork path is the sequence of nodes from a common ancestor
    to the first node where parametric choices diverge.

    Args:
        graph1, graph2: TheoryGraphs to compare.

    Returns:
        A list of node IDs forming the path, or None if no path exists.
    """
    diff = compute_structural_diff(graph1, graph2)

    if not diff.fork_points:
        return None

    # Find a root node (in both graphs, no presupposes)
    all_roots = [
        nid
        for nid in diff.shared_nodes
        if not graph1.nodes[nid].presupposes
    ]

    if not all_roots:
        return None

    root = all_roots[0]

    # BFS from root to find path to any fork point
    from collections import deque

    queue = deque([(root, [root])])
    visited = {root}

    while queue:
        current, path = queue.popleft()

        if current in diff.fork_points:
            return path

        # Expand to dependents
        for node_id in graph1.nodes:
            if (
                current in graph1.nodes[node_id].presupposes
                and node_id in diff.shared_nodes
                and node_id not in visited
            ):
                visited.add(node_id)
                queue.append((node_id, path + [node_id]))

    return None


def extract_theory_branch(
    graph: TheoryGraph, from_node_id: str
) -> TheoryGraph:
    """Extract a subgraph rooted at a given node (downward to descendants).

    Args:
        graph: TheoryGraph to extract from.
        from_node_id: Starting node ID.

    Returns:
        A new TheoryGraph containing from_node_id and all its descendants.
    """
    if from_node_id not in graph.nodes:
        raise KeyError(f"Node {from_node_id} not found.")

    # BFS to collect all descendants
    descendants = {from_node_id}
    queue = [from_node_id]

    while queue:
        current = queue.pop(0)
        for other_id, other_node in graph.nodes.items():
            if current in other_node.presupposes and other_id not in descendants:
                descendants.add(other_id)
                queue.append(other_id)

    # Build new graph with these nodes
    # Adjust presupposes to only include those in the branch
    new_graph = type(graph)(graph.meta)
    for node_id in descendants:
        node = graph.nodes[node_id]
        presupposes_in_branch = [
            p for p in node.presupposes if p in descendants
        ]
        new_node = Node(
            id=node.id,
            structural_type=node.structural_type,
            label=node.label,
            description=node.description,
            presupposes=presupposes_in_branch,
            provides=node.provides,
            parametric_slots=node.parametric_slots,
            resolved_values=node.resolved_values,
        )
        new_graph.add_node(new_node)

    try:
        new_graph.validate()
    except ValueError:
        # If validation fails, try adding root presupposes back
        for node_id in descendants:
            node = graph.nodes[node_id]
            new_graph.nodes[node_id].presupposes = [
                p for p in node.presupposes if p not in descendants
            ] + new_graph.nodes[node_id].presupposes

    return new_graph


def parametric_signature(graph: TheoryGraph) -> Dict[str, Set[str]]:
    """Extract all parametric choices in a theory graph.

    Returns:
        A dict {node_id: {slot_name1, slot_name2, ...}} of all parametric
        decisions in the graph (nodes with resolved_values).
    """
    signature = {}
    for node_id, node in graph.nodes.items():
        if node.resolved_values:
            signature[node_id] = set(node.resolved_values.keys())
    return signature
