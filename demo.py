#!/usr/bin/env python
"""
Demonstration of POSR core API: building graphs, making parametric choices,
and comparing theories (SM vs GR).
"""

from posr.templates import sm, gr
from posr.graph import resolve_parametric_choices, validate_consistency
from posr.diff import compute_structural_diff, identify_fork_path
import json


def demo_sm_graph():
    """Load and inspect the Standard Model graph."""
    print("=" * 70)
    print("DEMO 1: Standard Model Theory Graph")
    print("=" * 70)

    graph = sm.build()

    print(f"\nTheory: {graph.meta.name}")
    print(f"Description: {graph.meta.description}")
    print(f"Version: {graph.meta.version}")
    print(f"Total nodes: {len(graph.nodes)}")

    # Show topological order
    topo = graph.topological_sort()
    print(f"\nTopological order (first 10 nodes):")
    for i, node_id in enumerate(topo[:10], 1):
        node = graph.nodes[node_id]
        print(f"  {i}. {node_id}: {node.label}")

    # Show key nodes and their presupposes
    print(f"\nKey dependencies:")
    for node_id in ["ZFC", "MAN", "CONN", "QFT", "SM_G", "ANOM"]:
        if node_id in graph.nodes:
            node = graph.nodes[node_id]
            print(f"  {node_id} ({node.label})")
            print(f"    Presupposes: {node.presupposes}")
            print(f"    Provides: {node.provides}")

    # Validate the graph
    errors = validate_consistency(graph)
    print(f"\nGraph validation: {'PASSED' if not errors else 'FAILED'}")
    if errors:
        for error in errors:
            print(f"  ERROR: {error}")

    return graph


def demo_gr_graph():
    """Build the General Relativity graph."""
    print("\n" + "=" * 70)
    print("DEMO 2: General Relativity Theory Graph")
    print("=" * 70)

    graph = gr.build()

    print(f"\nTheory: {graph.meta.name}")
    print(f"Description: {graph.meta.description}")
    print(f"Total nodes: {len(graph.nodes)}")

    # Show GR-specific nodes
    gr_specific = ["METRIC", "LEVI_CIVITA", "RIEMANN", "EINSTEIN_EQ", "STRESS_ENERGY"]
    print(f"\nGR-specific nodes:")
    for node_id in gr_specific:
        if node_id in graph.nodes:
            node = graph.nodes[node_id]
            print(f"  {node_id}: {node.label}")

    # Validate
    errors = validate_consistency(graph)
    print(f"\nGraph validation: {'PASSED' if not errors else 'FAILED'}")

    return graph


def demo_parametric_choices(sm_graph):
    """Make parametric choices and create a theory-file."""
    print("\n" + "=" * 70)
    print("DEMO 3: Parametric Choices & Theory-File Generation")
    print("=" * 70)

    # Define parametric choices for the Standard Model
    choices = {
        "CL": {
            "LEM": "true",
            "explosion": "true",
        },
        "ZFC": {
            "axiom_of_choice": "true",
            "foundation": "true",
        },
        "SM_G": {
            "gauge_group": "SU(3)xSU(2)xU(1)",
            "g3": "1.221",
            "g2": "0.652",
            "g1": "0.357",
        },
        "SM_F": {
            "num_generations": "3",
        },
    }

    print(f"\nMaking parametric choices:")
    for node_id, params in choices.items():
        print(f"  {node_id}:")
        for param_name, value in params.items():
            print(f"    {param_name} = {value}")

    # Resolve choices
    theory_file = resolve_parametric_choices(sm_graph, choices)

    print(f"\nTheory-File generated:")
    print(f"  Name: {theory_file.theory_graph.meta.name}")
    print(f"  Human slug: {theory_file.human_slug}")
    print(f"  Fingerprint: {theory_file.parametric_fingerprint}")
    print(f"  Filename: {theory_file.filename()}")

    return theory_file


def demo_sm_vs_gr_comparison(sm_graph, gr_graph):
    """Compare Standard Model and General Relativity graphs."""
    print("\n" + "=" * 70)
    print("DEMO 4: Cross-Theory Comparison (SM vs GR)")
    print("=" * 70)

    diff = compute_structural_diff(sm_graph, gr_graph)

    print(f"\n{diff.summary()}")

    # Show shared structure
    print(f"\nShared foundational nodes:")
    shared_foundations = ["CL", "FOL", "ZFC", "GRP", "LA", "TOP", "MAN"]
    for node_id in shared_foundations:
        if node_id in diff.shared_nodes:
            print(f"  ✓ {node_id}")

    # Show theory-specific branches
    print(f"\nStandard Model-specific nodes:")
    sm_specific = ["SM_G", "SM_F", "SM_H", "SM_Y", "ANOM"]
    for node_id in sm_specific:
        if node_id in diff.theory1_only:
            print(f"  • {node_id}")

    print(f"\nGeneral Relativity-specific nodes:")
    gr_specific = ["METRIC", "LEVI_CIVITA", "RIEMANN", "EINSTEIN_EQ"]
    for node_id in gr_specific:
        if node_id in diff.theory2_only:
            print(f"  • {node_id}")

    # Find fork path
    fork_path = identify_fork_path(sm_graph, gr_graph)
    if fork_path:
        print(f"\nFork path from common ancestor to parametric divergence:")
        print(f"  {' → '.join(fork_path[:5])}")
        if len(fork_path) > 5:
            print(f"  ... ({len(fork_path)} nodes total)")

    return diff


def main():
    """Run all demonstrations."""
    print("\n")
    print("█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  POSR Core API Demonstration".center(68) + "█")
    print("█" + "  Parameterized Ontic Structural Realism".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)

    try:
        # Build SM and GR graphs
        sm_graph = demo_sm_graph()
        gr_graph = demo_gr_graph()

        # Make parametric choices
        sm_theory_file = demo_parametric_choices(sm_graph)

        # Compare theories
        diff = demo_sm_vs_gr_comparison(sm_graph, gr_graph)

        print("\n" + "=" * 70)
        print("DEMO Complete")
        print("=" * 70)
        print("\nKey takeaways:")
        print(f"  • Standard Model has {len(sm_graph.nodes)} nodes")
        print(f"  • General Relativity has {len(gr_graph.nodes)} nodes")
        print(f"  • Shared structure: {len(diff.shared_nodes)} nodes")
        print(f"  • SM-specific: {len(diff.theory1_only)} nodes")
        print(f"  • GR-specific: {len(diff.theory2_only)} nodes")
        print("\nThe POSR system successfully models:")
        print("  ✓ Theory graphs as DAGs with parametric choices")
        print("  ✓ Cross-theory comparison and fork point identification")
        print("  ✓ Theory-file generation with provenance tracking")
        print("  ✓ Shared subgraph extraction and dependency analysis")

    except Exception as e:
        print(f"\nError during demonstration: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
