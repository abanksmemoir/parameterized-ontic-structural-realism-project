"""Tests for graph module."""

import pytest
from posr.graph import (
    build_from_json,
    resolve_parametric_choices,
    validate_consistency,
    compare_structures,
    find_deepest_chain,
)
from posr.schema import Node, TheoryGraph, TheoryGraphMeta
from datetime import datetime
import json
import os


class TestBuildFromJson:
    """Test building a graph from JSON."""

    def test_build_from_sm_json(self):
        """Test that we can build the SM graph from the JSON file."""
        json_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "sm_dependency_graph.json",
        )

        if not os.path.exists(json_path):
            pytest.skip(f"sm_dependency_graph.json not found at {json_path}")

        graph = build_from_json(json_path)

        assert graph.meta.name is not None
        assert len(graph.nodes) > 0
        # Check for key SM nodes
        key_nodes = ["CL", "FOL", "ZFC", "GRP", "SM_G", "SM_F"]
        for node_id in key_nodes:
            assert node_id in graph.nodes, f"Expected node {node_id} not found"


class TestResolveParametricChoices:
    """Test parametric choice resolution."""

    def test_resolve_choices(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        from posr.schema import ParametricSlot

        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="SM gauge group",
            description="",
            parametric_slots=[
                ParametricSlot(
                    name="gauge_group",
                    description="Gauge group",
                    slot_type="architectural",
                    known_options=["SU(3)xSU(2)xU(1)", "SU(5)"],
                    default="SU(3)xSU(2)xU(1)",
                ),
            ],
        )
        graph.add_node(node)

        choices = {
            "SM_G": {"gauge_group": "SU(3)xSU(2)xU(1)"},
        }

        theory_file = resolve_parametric_choices(graph, choices)

        assert theory_file.theory_graph.nodes["SM_G"].resolved_values[
            "gauge_group"
        ] == "SU(3)xSU(2)xU(1)"


class TestValidateConsistency:
    """Test graph validation."""

    def test_validate_valid_graph(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        graph.add_node(
            Node(id="A", structural_type="logic", label="A", description="")
        )
        graph.add_node(
            Node(
                id="B",
                structural_type="logic",
                label="B",
                description="",
                presupposes=["A"],
            )
        )
        graph.validate()

        errors = validate_consistency(graph)
        assert len(errors) == 0

    def test_validate_missing_presupposes(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        graph.add_node(
            Node(id="A", structural_type="logic", label="A", description="")
        )
        graph.add_node(
            Node(
                id="B",
                structural_type="logic",
                label="B",
                description="",
                presupposes=["MISSING"],
            )
        )

        errors = validate_consistency(graph)
        assert len(errors) > 0
        assert any("MISSING" in e for e in errors)


class TestCompareStructures:
    """Test cross-theory comparison."""

    def test_compare_identical_graphs(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph1 = TheoryGraph(meta)
        graph2 = TheoryGraph(meta)

        node = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(node)
        graph2.add_node(node)

        result = compare_structures(graph1, graph2)

        assert "A" in result["shared_nodes"]
        assert len(result["graph1_only"]) == 0
        assert len(result["graph2_only"]) == 0

    def test_compare_with_fork(self):
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

        from posr.schema import ParametricSlot

        # Shared node
        shared_node = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(shared_node)
        graph2.add_node(shared_node)

        # Same node but different resolved values
        fork_node1 = Node(
            id="B",
            structural_type="logic",
            label="B",
            description="",
            presupposes=["A"],
            resolved_values={"param": "value1"},
        )
        fork_node2 = Node(
            id="B",
            structural_type="logic",
            label="B",
            description="",
            presupposes=["A"],
            resolved_values={"param": "value2"},
        )

        graph1.add_node(fork_node1)
        graph2.add_node(fork_node2)

        result = compare_structures(graph1, graph2)

        assert "A" in result["shared_nodes"]
        assert "B" in result["shared_nodes"]
        assert "B" in result["fork_points"]


class TestFindDeepestChain:
    """Test finding the deepest dependency chain."""

    def test_deepest_chain(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        # Create a linear chain: A -> B -> C
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(
            Node(
                id="B",
                structural_type="logic",
                label="B",
                description="",
                presupposes=["A"],
            )
        )
        graph.add_node(
            Node(
                id="C",
                structural_type="logic",
                label="C",
                description="",
                presupposes=["B"],
            )
        )
        graph.validate()

        chain = find_deepest_chain(graph)
        assert len(chain) == 3
        assert chain[0] == "A"
        assert chain[-1] == "C"
