#!/usr/bin/env python
"""
Demonstration of POSR core API (V2): building graphs, making parametric choices,
and comparing theories (SM vs GR).

V2 features demonstrated:
  - Typed parameters (axiom/structural/kinematic/dynamical/boundary/convention)
  - Typed dependencies (logical/conventional/contingent)
  - Temporal structure chain
  - Boundary parameters and contingent provisions
  - Cross-theory comparison with dependency-type awareness
"""

from posr.templates import sm, gr
from posr.graph import resolve_parametric_choices, validate_consistency
from posr.diff import (
    compute_structural_diff, identify_fork_path,
    dependency_type_summary, parameter_type_summary,
)
import json


def demo_sm_graph():
    """Load and inspect the Standard Model graph."""
    print("=" * 70)
    print("DEMO 1: Standard Model Theory Graph (V2)")
    print("=" * 70)

    graph = sm.build()

    print(f"\nTheory: {graph.meta.name}")
    print(f"Version: {graph.meta.version}")
    print(f"Total nodes: {len(graph.nodes)}")

    # Show topological order
    topo = graph.topological_sort()
    print(f"\nTopological order (first 10 nodes):")
    for i, node_id in enumerate(topo[:10], 1):
        node = graph.nodes[node_id]
        print(f"  {i}. {node_id}: {node.label}")

    # Show key nodes with typed dependencies
    print(f"\nKey dependencies (V2: typed):")
    for node_id in ["ZFC", "QFT", "SM_G"]:
        if node_id in graph.nodes:
            node = graph.nodes[node_id]
            print(f"  {node_id} ({node.label})")
            for dep in node.dependencies:
                print(f"    → {dep.on} [{dep.dependency_type}]"
                      + (f" — {dep.note}" if dep.note else ""))

    # Show parameter type breakdown
    param_counts = parameter_type_summary(graph)
    print(f"\nParameter type breakdown:")
    for ptype, count in sorted(param_counts.items()):
        if count > 0:
            print(f"  {ptype}: {count}")

    # Show dependency type breakdown
    dep_counts = dependency_type_summary(graph)
    print(f"\nDependency type breakdown:")
    for dtype, count in sorted(dep_counts.items()):
        if count > 0:
            print(f"  {dtype}: {count}")

    # Show temporal chain
    temporal_nodes = graph.temporal_chain()
    print(f"\nTemporal structure chain ({len(temporal_nodes)} nodes):")
    for node_id in temporal_nodes:
        node = graph.nodes[node_id]
        note_preview = node.temporal_note[:80] + "..." if len(node.temporal_note) > 80 else node.temporal_note
        print(f"  {node_id}: {note_preview}")

    # Show boundary parameters (the most consequential hidden assumptions)
    boundary = graph.boundary_parameters()
    print(f"\nBoundary parameters ({len(boundary)}):")
    for node_id, param in boundary:
        print(f"  {node_id}/{param.id}: {param.name} = {param.value}")
        if param.note:
            print(f"    Note: {param.note[:80]}...")

    # Validate the graph
    errors = validate_consistency(graph)
    print(f"\nGraph validation: {'PASSED' if not errors else 'FAILED'}")

    return graph


def demo_gr_graph():
    """Build the General Relativity graph."""
    print("\n" + "=" * 70)
    print("DEMO 2: General Relativity Theory Graph (V2)")
    print("=" * 70)

    graph = gr.build()

    print(f"\nTheory: {graph.meta.name}")
    print(f"Total nodes: {len(graph.nodes)}")

    # Show GR-specific nodes
    gr_specific = ["METRIC", "LEVI_CIVITA", "RIEMANN", "EINSTEIN_EQ", "STRESS_ENERGY", "GR_CAUSALITY"]
    print(f"\nGR-specific nodes:")
    for node_id in gr_specific:
        if node_id in graph.nodes:
            node = graph.nodes[node_id]
            print(f"  {node_id}: {node.label}")
            if node.temporal_note:
                print(f"    Temporal: {node.temporal_note[:70]}...")

    errors = validate_consistency(graph)
    print(f"\nGraph validation: {'PASSED' if not errors else 'FAILED'}")

    return graph


def demo_parametric_choices(sm_graph):
    """Make parametric choices and create a theory-file."""
    print("\n" + "=" * 70)
    print("DEMO 3: Parametric Choices & Theory-File Generation")
    print("=" * 70)

    # V2 choices using parameter names from the V2 graph
    choices = {
        "CL": {
            "Law of excluded middle": "on",
            "Explosion principle": "on",
        },
        "ZFC": {
            "Axiom of choice": "included",
            "Foundation axiom": "included",
        },
        "SM_G": {
            "Gauge group": "SU(3)xSU(2)xU(1)_Y",
        },
        "SM_F": {
            "Number of generations": "3",
        },
        "QFT": {
            "iε sign": "+iε",
            "Vacuum state": "Poincare-invariant |Omega>",
        },
    }

    print(f"\nMaking parametric choices:")
    for node_id, params in choices.items():
        print(f"  {node_id}:")
        for param_name, value in params.items():
            print(f"    {param_name} = {value}")

    theory_file = resolve_parametric_choices(sm_graph, choices)

    print(f"\nTheory-File generated:")
    print(f"  Slug: {theory_file.human_slug}")
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

    # Show shared foundational nodes
    print(f"\nShared foundational nodes:")
    for node_id in sorted(diff.shared_nodes):
        print(f"  {node_id}")

    # Find fork path
    fork_path = identify_fork_path(sm_graph, gr_graph)
    if fork_path:
        print(f"\nFork path to parametric divergence:")
        print(f"  {' -> '.join(fork_path[:5])}")

    return diff


def main():
    """Run all demonstrations."""
    print("\n")
    print("=" * 70)
    print("  POSR Core API Demonstration (V2)")
    print("  Parameterized Ontic Structural Realism")
    print("=" * 70)

    try:
        sm_graph = demo_sm_graph()
        gr_graph = demo_gr_graph()
        sm_theory_file = demo_parametric_choices(sm_graph)
        diff = demo_sm_vs_gr_comparison(sm_graph, gr_graph)

        print("\n" + "=" * 70)
        print("DEMO Complete")
        print("=" * 70)
        print(f"\nKey results:")
        print(f"  Standard Model: {len(sm_graph.nodes)} nodes")
        print(f"  General Relativity: {len(gr_graph.nodes)} nodes")
        print(f"  Shared structure: {len(diff.shared_nodes)} nodes")
        print(f"  SM-specific: {len(diff.theory1_only)} nodes")
        print(f"  GR-specific: {len(diff.theory2_only)} nodes")
        print(f"\nV2 capabilities demonstrated:")
        print(f"  - Typed parameters (axiom/structural/kinematic/dynamical/boundary/convention)")
        print(f"  - Typed dependencies (logical/conventional/contingent)")
        print(f"  - Temporal structure chain")
        print(f"  - Boundary parameters (iε, vacuum state)")
        print(f"  - Contingent provisions")
        print(f"  - Cross-theory comparison with SM vs GR")

    except Exception as e:
        print(f"\nError during demonstration: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
