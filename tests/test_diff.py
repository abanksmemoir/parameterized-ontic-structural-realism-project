"""Tests for cross-theory comparison (diff module, V2)."""

import pytest
from posr.diff import (
    compute_structural_diff,
    extract_shared_subgraph,
    identify_fork_path,
    extract_theory_branch,
    parametric_signature,
    dependency_type_summary,
    parameter_type_summary,
    StructuralDiff,
)
from posr.schema import Node, Dependency, Parameter, TheoryGraph, TheoryGraphMeta
from datetime import datetime


def _make_meta(name="Theory"):
    return TheoryGraphMeta(name=name, description="", version="2.0.0",
                          date=datetime.utcnow().isoformat())


class TestComputeStructuralDiff:
    """Test structural diff computation."""

    def test_diff_identical_graphs(self):
        graph1 = TheoryGraph(_make_meta())
        graph2 = TheoryGraph(_make_meta())
        node = Node(id="A", structural_type="logic", label="A", description="")
        graph1.add_node(node)
        graph2.add_node(node)
        diff = compute_structural_diff(graph1, graph2)
        assert "A" in diff.shared_nodes
        assert len(diff.theory1_only) == 0
        assert len(diff.fork_points) == 0

    def test_diff_disjoint_graphs(self):
        graph1 = TheoryGraph(_make_meta("T1"))
        graph2 = TheoryGraph(_make_meta("T2"))
        graph1.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph2.add_node(Node(id="B", structural_type="logic", label="B", description=""))
        diff = compute_structural_diff(graph1, graph2)
        assert len(diff.shared_nodes) == 0
        assert "A" in diff.theory1_only
        assert "B" in diff.theory2_only

    def test_diff_with_parametric_fork(self):
        graph1 = TheoryGraph(_make_meta())
        graph2 = TheoryGraph(_make_meta())

        node1 = Node(id="SM_G", structural_type="physical_theory", label="Gauge",
                     description="", resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"})
        node2 = Node(id="SM_G", structural_type="physical_theory", label="Gauge",
                     description="", resolved_values={"gauge_group": "SU(5)"})
        graph1.add_node(node1)
        graph2.add_node(node2)

        diff = compute_structural_diff(graph1, graph2)
        assert "SM_G" in diff.fork_points
        assert diff.fork_points["SM_G"][0]["gauge_group"] == "SU(3)xSU(2)xU(1)"
        assert diff.fork_points["SM_G"][1]["gauge_group"] == "SU(5)"


class TestExtractSharedSubgraph:
    """Test shared subgraph extraction."""

    def test_extract_shared(self):
        graph1 = TheoryGraph(_make_meta("T1"))
        graph2 = TheoryGraph(_make_meta("T2"))

        graph1.add_node(Node(id="S1", structural_type="logic", label="S1", description=""))
        graph1.add_node(Node(id="S2", structural_type="logic", label="S2", description="",
                            dependencies=[Dependency(on="S1", dependency_type="logical")]))
        graph2.add_node(Node(id="S1", structural_type="logic", label="S1", description=""))
        graph2.add_node(Node(id="S2", structural_type="logic", label="S2", description="",
                            dependencies=[Dependency(on="S1", dependency_type="logical")]))

        graph1.add_node(Node(id="T1_ONLY", structural_type="logic", label="T1", description="",
                            dependencies=[Dependency(on="S2", dependency_type="logical")]))
        graph2.add_node(Node(id="T2_ONLY", structural_type="logic", label="T2", description="",
                            dependencies=[Dependency(on="S2", dependency_type="logical")]))

        graph1.validate()
        graph2.validate()

        shared = extract_shared_subgraph(graph1, graph2)
        assert "S1" in shared.nodes
        assert "S2" in shared.nodes
        assert "T1_ONLY" not in shared.nodes


class TestIdentifyForkPath:
    """Test fork path identification."""

    def test_identify_fork_path(self):
        graph1 = TheoryGraph(_make_meta("T1"))
        graph2 = TheoryGraph(_make_meta("T2"))

        graph1.add_node(Node(id="ROOT", structural_type="logic", label="Root", description=""))
        graph2.add_node(Node(id="ROOT", structural_type="logic", label="Root", description=""))

        graph1.add_node(Node(id="FORK", structural_type="logic", label="Fork", description="",
                            dependencies=[Dependency(on="ROOT", dependency_type="logical")],
                            resolved_values={"param": "value1"}))
        graph2.add_node(Node(id="FORK", structural_type="logic", label="Fork", description="",
                            dependencies=[Dependency(on="ROOT", dependency_type="logical")],
                            resolved_values={"param": "value2"}))

        graph1.validate()
        graph2.validate()

        fork_path = identify_fork_path(graph1, graph2)
        assert fork_path is not None
        assert "ROOT" in fork_path
        assert "FORK" in fork_path


class TestExtractTheoryBranch:
    """Test theory branch extraction."""

    def test_extract_branch(self):
        graph = TheoryGraph(_make_meta())
        graph.add_node(Node(id="ROOT", structural_type="logic", label="Root", description=""))
        graph.add_node(Node(id="B1", structural_type="logic", label="B1", description="",
                           dependencies=[Dependency(on="ROOT", dependency_type="logical")]))
        graph.add_node(Node(id="B2", structural_type="logic", label="B2", description="",
                           dependencies=[Dependency(on="B1", dependency_type="logical")]))
        graph.add_node(Node(id="OTHER", structural_type="logic", label="Other", description="",
                           dependencies=[Dependency(on="ROOT", dependency_type="logical")]))
        graph.validate()

        branch = extract_theory_branch(graph, "B1")
        assert "B1" in branch.nodes
        assert "B2" in branch.nodes
        assert "OTHER" not in branch.nodes


class TestParametricSignature:
    """Test parametric signature extraction."""

    def test_signature(self):
        graph = TheoryGraph(_make_meta())
        graph.add_node(Node(id="N1", structural_type="logic", label="N1", description="",
                           resolved_values={"param1": "value1"}))
        graph.add_node(Node(id="N2", structural_type="logic", label="N2", description="",
                           resolved_values={"param2": "v2", "param3": "v3"}))
        graph.add_node(Node(id="N3", structural_type="logic", label="N3", description=""))

        sig = parametric_signature(graph)
        assert "N1" in sig
        assert "N2" in sig
        assert "N3" not in sig
        assert "param1" in sig["N1"]


class TestDependencyTypeSummary:
    """Test V2 dependency type counting."""

    def test_dependency_type_summary(self):
        graph = TheoryGraph(_make_meta())
        graph.add_node(Node(id="CL", structural_type="logic", label="CL", description=""))
        graph.add_node(Node(id="FOL", structural_type="logic", label="FOL", description="",
                           dependencies=[Dependency(on="CL", dependency_type="conventional")]))
        graph.add_node(Node(id="ZFC", structural_type="foundation", label="ZFC", description="",
                           dependencies=[
                               Dependency(on="CL", dependency_type="logical"),
                               Dependency(on="FOL", dependency_type="logical"),
                           ]))
        counts = dependency_type_summary(graph)
        assert counts["logical"] == 2
        assert counts["conventional"] == 1
        assert counts["contingent"] == 0


class TestParameterTypeSummary:
    """Test V2 parameter type counting."""

    def test_parameter_type_summary(self):
        graph = TheoryGraph(_make_meta())
        graph.add_node(Node(
            id="QFT", structural_type="quantization", label="QFT", description="",
            parameters=[
                Parameter(id="P054", name="Reg", parameter_type="convention"),
                Parameter(id="P057", name="iε", parameter_type="boundary"),
                Parameter(id="P078", name="Vacuum", parameter_type="boundary"),
            ],
        ))
        graph.add_node(Node(
            id="CL", structural_type="logic", label="CL", description="",
            parameters=[
                Parameter(id="P001", name="LEM", parameter_type="axiom"),
            ],
        ))
        counts = parameter_type_summary(graph)
        assert counts["boundary"] == 2
        assert counts["convention"] == 1
        assert counts["axiom"] == 1
