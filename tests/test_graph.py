"""Tests for graph module (V2)."""

import pytest
from posr.graph import (
    build_from_json,
    resolve_parametric_choices,
    validate_consistency,
    compare_structures,
    find_deepest_chain,
)
from posr.schema import Node, Parameter, Dependency, TheoryGraph, TheoryGraphMeta
from datetime import datetime
import json
import os


class TestBuildFromJson:
    """Test building a graph from JSON."""

    def test_build_from_v2_json(self):
        """Test that we can build the SM graph from V2 JSON."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)
        assert graph.meta.name is not None
        assert len(graph.nodes) > 0

        # Check for key SM nodes including V2 additions
        key_nodes = ["CL", "FOL", "ZFC", "GRP", "SM_G", "SM_F", "QFT"]
        for node_id in key_nodes:
            assert node_id in graph.nodes, f"Expected node {node_id} not found"

    def test_v2_typed_parameters(self):
        """Test that V2 parameters are typed correctly."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)

        # CL should have axiom-type parameters
        cl_node = graph.nodes["CL"]
        assert len(cl_node.parameters) > 0
        assert cl_node.parameters[0].parameter_type == "axiom"

        # QFT should have boundary-type parameters (iε sign)
        qft_node = graph.nodes["QFT"]
        boundary_params = qft_node.parameters_by_type("boundary")
        assert len(boundary_params) >= 1
        ie_param = next((p for p in boundary_params if "iε" in p.name), None)
        assert ie_param is not None, "QFT should have iε parameter"

    def test_v2_typed_dependencies(self):
        """Test that V2 dependencies are typed correctly."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)

        # FOL -> CL is conventional
        fol_node = graph.nodes["FOL"]
        cl_dep = next((d for d in fol_node.dependencies if d.on == "CL"), None)
        assert cl_dep is not None
        assert cl_dep.dependency_type == "conventional"

        # ZFC -> CL is logical
        zfc_node = graph.nodes["ZFC"]
        cl_dep = next((d for d in zfc_node.dependencies if d.on == "CL"), None)
        assert cl_dep is not None
        assert cl_dep.dependency_type == "logical"

    def test_v2_temporal_notes(self):
        """Test that temporal notes are loaded."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)

        # MAN should have a temporal note about metric signature
        man_node = graph.nodes["MAN"]
        assert man_node.temporal_note is not None
        assert "temporal" in man_node.temporal_note.lower() or "signature" in man_node.temporal_note.lower()

        # QFT should have a temporal note about iε
        qft_node = graph.nodes["QFT"]
        assert qft_node.temporal_note is not None

    def test_v2_contingent_provisions(self):
        """Test that contingent provisions are loaded."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)

        # QFT should have contingent provisions
        qft_node = graph.nodes["QFT"]
        assert len(qft_node.contingent_provisions) > 0

        # GAUGE should have contingent provisions
        gauge_node = graph.nodes["GAUGE"]
        assert len(gauge_node.contingent_provisions) > 0

    def test_v2_node_count(self):
        """Test that V2 has the expected number of nodes."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..",
            "deep-research", "time-symmetry-debt", "v2",
            "sm_dependency_graph_v2.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V2 JSON not found")

        graph = build_from_json(json_path)
        # V2 has 30 nodes (same topology as V1, plus IL and TT)
        assert len(graph.nodes) >= 30

    def test_build_from_v1_json(self):
        """Test backward compat: build from V1 JSON."""
        json_path = os.path.join(
            os.path.dirname(__file__), "..", "sm_dependency_graph.json",
        )
        if not os.path.exists(json_path):
            pytest.skip("V1 JSON not found")

        graph = build_from_json(json_path)
        assert len(graph.nodes) > 0
        assert "CL" in graph.nodes


class TestResolveParametricChoices:
    """Test parametric choice resolution."""

    def test_resolve_choices(self):
        meta = TheoryGraphMeta(name="Test", description="", version="2.0.0",
                              date=datetime.utcnow().isoformat())
        graph = TheoryGraph(meta)

        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="SM gauge group",
            description="",
            parameters=[
                Parameter(
                    id="P062", name="Gauge group",
                    parameter_type="structural",
                    value="SU(3)xSU(2)xU(1)",
                    alternatives=["SU(5)", "SO(10)"],
                ),
            ],
        )
        graph.add_node(node)

        choices = {"SM_G": {"Gauge group": "SU(3)xSU(2)xU(1)"}}
        theory_file = resolve_parametric_choices(graph, choices)

        assert theory_file.theory_graph.nodes["SM_G"].resolved_values[
            "Gauge group"
        ] == "SU(3)xSU(2)xU(1)"


class TestValidateConsistency:
    """Test graph validation."""

    def test_validate_valid_graph(self):
        meta = TheoryGraphMeta(name="Test", description="", version="2.0.0",
                              date=datetime.utcnow().isoformat())
        graph = TheoryGraph(meta)
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")]))
        graph.validate()
        errors = validate_consistency(graph)
        assert len(errors) == 0

    def test_validate_missing_dependency(self):
        meta = TheoryGraphMeta(name="Test", description="", version="2.0.0",
                              date=datetime.utcnow().isoformat())
        graph = TheoryGraph(meta)
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="MISSING", dependency_type="logical")]))
        errors = validate_consistency(graph)
        assert len(errors) > 0
        assert any("MISSING" in e for e in errors)


class TestCompareStructures:
    """Test cross-theory comparison."""

    def test_compare_identical_graphs(self):
        meta = TheoryGraphMeta(name="Test", description="", version="2.0.0",
                              date=datetime.utcnow().isoformat())
        graph1 = TheoryGraph(meta)
        graph2 = TheoryGraph(meta)

        node = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(node)
        graph2.add_node(node)

        result = compare_structures(graph1, graph2)
        assert "A" in result["shared_nodes"]
        assert len(result["graph1_only"]) == 0

    def test_compare_with_fork(self):
        meta1 = TheoryGraphMeta(name="T1", description="", version="2.0.0",
                               date=datetime.utcnow().isoformat())
        meta2 = TheoryGraphMeta(name="T2", description="", version="2.0.0",
                               date=datetime.utcnow().isoformat())
        graph1 = TheoryGraph(meta1)
        graph2 = TheoryGraph(meta2)

        shared = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(shared)
        graph2.add_node(shared)

        fork1 = Node(id="B", structural_type="logic", label="B", description="",
                     dependencies=[Dependency(on="A", dependency_type="logical")],
                     resolved_values={"param": "value1"})
        fork2 = Node(id="B", structural_type="logic", label="B", description="",
                     dependencies=[Dependency(on="A", dependency_type="logical")],
                     resolved_values={"param": "value2"})
        graph1.add_node(fork1)
        graph2.add_node(fork2)

        result = compare_structures(graph1, graph2)
        assert "B" in result["fork_points"]


class TestFindDeepestChain:
    """Test finding the deepest dependency chain."""

    def test_deepest_chain(self):
        meta = TheoryGraphMeta(name="Test", description="", version="2.0.0",
                              date=datetime.utcnow().isoformat())
        graph = TheoryGraph(meta)
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")]))
        graph.add_node(Node(id="C", structural_type="logic", label="C", description="",
                           dependencies=[Dependency(on="B", dependency_type="logical")]))
        graph.validate()
        chain = find_deepest_chain(graph)
        assert len(chain) == 3
        assert chain[0] == "A"
        assert chain[-1] == "C"
