"""Tests for cross-theory comparison (diff module)."""

import pytest
from posr.diff import (
    compute_structural_diff,
    extract_shared_subgraph,
    identify_fork_path,
    extract_theory_branch,
    parametric_signature,
    StructuralDiff,
)
from posr.schema import Node, TheoryGraph, TheoryGraphMeta
from datetime import datetime


class TestComputeStructuralDiff:
    """Test structural diff computation."""

    def test_diff_identical_graphs(self):
        meta = TheoryGraphMeta(
            name="Theory",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph1 = TheoryGraph(meta)
        graph2 = TheoryGraph(meta)

        node = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(node)
        graph2.add_node(node)

        diff = compute_structural_diff(graph1, graph2)

        assert "A" in diff.shared_nodes
        assert len(diff.theory1_only) == 0
        assert len(diff.theory2_only) == 0
        assert len(diff.fork_points) == 0

    def test_diff_disjoint_graphs(self):
        meta1 = TheoryGraphMeta(
            name="Theory1",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        meta2 = TheoryGraphMeta(
            name="Theory2",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph1 = TheoryGraph(meta1)
        graph2 = TheoryGraph(meta2)

        graph1.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph2.add_node(Node(id="B", structural_type="logic", label="B", description=""))

        diff = compute_structural_diff(graph1, graph2)

        assert len(diff.shared_nodes) == 0
        assert "A" in diff.theory1_only
        assert "B" in diff.theory2_only

    def test_diff_with_parametric_fork(self):
        meta = TheoryGraphMeta(
            name="Theory",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph1 = TheoryGraph(meta)
        graph2 = TheoryGraph(meta)

        # Shared node with different resolved values
        node1 = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="Gauge group",
            description="",
            resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"},
        )
        node2 = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="Gauge group",
            description="",
            resolved_values={"gauge_group": "SU(5)"},
        )

        graph1.add_node(node1)
        graph2.add_node(node2)

        diff = compute_structural_diff(graph1, graph2)

        assert "SM_G" in diff.shared_nodes
        assert "SM_G" in diff.fork_points
        fork_vals = diff.fork_points["SM_G"]
        assert fork_vals[0]["gauge_group"] == "SU(3)xSU(2)xU(1)"
        assert fork_vals[1]["gauge_group"] == "SU(5)"


class TestExtractSharedSubgraph:
    """Test shared subgraph extraction."""

    def test_extract_shared(self):
        meta1 = TheoryGraphMeta(
            name="Theory1",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        meta2 = TheoryGraphMeta(
            name="Theory2",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph1 = TheoryGraph(meta1)
        graph2 = TheoryGraph(meta2)

        # Shared nodes
        graph1.add_node(
            Node(id="SHARED1", structural_type="logic", label="S1", description="")
        )
        graph1.add_node(
            Node(
                id="SHARED2",
                structural_type="logic",
                label="S2",
                description="",
                presupposes=["SHARED1"],
            )
        )

        # Same shared nodes in graph2
        graph2.add_node(
            Node(id="SHARED1", structural_type="logic", label="S1", description="")
        )
        graph2.add_node(
            Node(
                id="SHARED2",
                structural_type="logic",
                label="S2",
                description="",
                presupposes=["SHARED1"],
            )
        )

        # Theory-specific nodes
        graph1.add_node(
            Node(
                id="T1_ONLY",
                structural_type="logic",
                label="T1",
                description="",
                presupposes=["SHARED2"],
            )
        )
        graph2.add_node(
            Node(
                id="T2_ONLY",
                structural_type="logic",
                label="T2",
                description="",
                presupposes=["SHARED2"],
            )
        )

        graph1.validate()
        graph2.validate()

        shared = extract_shared_subgraph(graph1, graph2)

        assert "SHARED1" in shared.nodes
        assert "SHARED2" in shared.nodes
        assert "T1_ONLY" not in shared.nodes
        assert "T2_ONLY" not in shared.nodes


class TestIdentifyForkPath:
    """Test fork path identification."""

    def test_identify_fork_path(self):
        meta1 = TheoryGraphMeta(
            name="Theory1",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        meta2 = TheoryGraphMeta(
            name="Theory2",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph1 = TheoryGraph(meta1)
        graph2 = TheoryGraph(meta2)

        # Common root
        graph1.add_node(Node(id="ROOT", structural_type="logic", label="Root", description=""))
        graph2.add_node(Node(id="ROOT", structural_type="logic", label="Root", description=""))

        # Common intermediate
        graph1.add_node(
            Node(
                id="FORK",
                structural_type="logic",
                label="Fork",
                description="",
                presupposes=["ROOT"],
                resolved_values={"param": "value1"},
            )
        )
        graph2.add_node(
            Node(
                id="FORK",
                structural_type="logic",
                label="Fork",
                description="",
                presupposes=["ROOT"],
                resolved_values={"param": "value2"},
            )
        )

        graph1.validate()
        graph2.validate()

        fork_path = identify_fork_path(graph1, graph2)

        assert fork_path is not None
        assert "ROOT" in fork_path
        assert "FORK" in fork_path


class TestExtractTheoryBranch:
    """Test theory branch extraction."""

    def test_extract_branch(self):
        meta = TheoryGraphMeta(
            name="Theory",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph = TheoryGraph(meta)

        graph.add_node(
            Node(id="ROOT", structural_type="logic", label="Root", description="")
        )
        graph.add_node(
            Node(
                id="BRANCH1",
                structural_type="logic",
                label="B1",
                description="",
                presupposes=["ROOT"],
            )
        )
        graph.add_node(
            Node(
                id="BRANCH2",
                structural_type="logic",
                label="B2",
                description="",
                presupposes=["BRANCH1"],
            )
        )
        graph.add_node(
            Node(
                id="OTHER",
                structural_type="logic",
                label="Other",
                description="",
                presupposes=["ROOT"],
            )
        )

        graph.validate()

        branch = extract_theory_branch(graph, "BRANCH1")

        assert "BRANCH1" in branch.nodes
        assert "BRANCH2" in branch.nodes
        assert "OTHER" not in branch.nodes


class TestParametricSignature:
    """Test parametric signature extraction."""

    def test_signature(self):
        meta = TheoryGraphMeta(
            name="Theory",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )

        graph = TheoryGraph(meta)

        graph.add_node(
            Node(
                id="NODE1",
                structural_type="logic",
                label="N1",
                description="",
                resolved_values={"param1": "value1"},
            )
        )
        graph.add_node(
            Node(
                id="NODE2",
                structural_type="logic",
                label="N2",
                description="",
                resolved_values={"param2": "value2", "param3": "value3"},
            )
        )
        graph.add_node(
            Node(
                id="NODE3",
                structural_type="logic",
                label="N3",
                description="",
                # No resolved values
            )
        )

        sig = parametric_signature(graph)

        assert "NODE1" in sig
        assert "NODE2" in sig
        assert "NODE3" not in sig
        assert "param1" in sig["NODE1"]
        assert "param2" in sig["NODE2"]
        assert "param3" in sig["NODE2"]
