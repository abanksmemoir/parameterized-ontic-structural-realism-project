"""Tests for schema module (V2)."""

import pytest
from posr.schema import (
    Node,
    Parameter,
    Dependency,
    TheoryGraph,
    TheoryGraphMeta,
    TheoryFile,
    ForkPoint,
    PARAMETER_SUBTYPES,
    DEPENDENCY_TYPES,
)
from datetime import datetime


class TestParameter:
    """Test Parameter class (replaces ParametricSlot)."""

    def test_create_parameter(self):
        param = Parameter(
            id="P001",
            name="Law of excluded middle",
            parameter_type="axiom",
            value="on",
            alternatives=["off (intuitionistic)"],
        )
        assert param.id == "P001"
        assert param.parameter_type == "axiom"
        assert param.value == "on"

    def test_parameter_type_validation(self):
        with pytest.raises(ValueError, match="Invalid parameter_type"):
            Parameter(
                id="bad",
                name="bad",
                parameter_type="nonexistent_type",
            )

    def test_all_parameter_subtypes_valid(self):
        for subtype in PARAMETER_SUBTYPES:
            param = Parameter(id="test", name="test", parameter_type=subtype)
            assert param.parameter_type == subtype

    def test_parameter_serialization(self):
        param = Parameter(
            id="P006",
            name="Axiom of choice",
            parameter_type="axiom",
            value="included",
            alternatives=["excluded (ZF)"],
            note="Foundational choice",
        )
        d = param.to_dict()
        assert d["id"] == "P006"
        assert d["type"] == "axiom"
        assert d["note"] == "Foundational choice"

        param2 = Parameter.from_dict(d)
        assert param2.id == param.id
        assert param2.parameter_type == param.parameter_type
        assert param2.note == param.note


class TestDependency:
    """Test Dependency class."""

    def test_create_dependency(self):
        dep = Dependency(
            on="CL",
            dependency_type="logical",
            note="ZFC is formulated in classical logic",
        )
        assert dep.on == "CL"
        assert dep.dependency_type == "logical"

    def test_dependency_type_validation(self):
        with pytest.raises(ValueError, match="Invalid dependency_type"):
            Dependency(on="X", dependency_type="invalid")

    def test_all_dependency_types_valid(self):
        for dep_type in DEPENDENCY_TYPES:
            dep = Dependency(on="X", dependency_type=dep_type)
            assert dep.dependency_type == dep_type

    def test_dependency_serialization(self):
        dep = Dependency(
            on="CL",
            dependency_type="conventional",
            note="FOL can be built on IL",
        )
        d = dep.to_dict()
        assert d["on"] == "CL"
        assert d["type"] == "conventional"

        dep2 = Dependency.from_dict(d)
        assert dep2.on == dep.on
        assert dep2.dependency_type == dep.dependency_type


class TestNode:
    """Test Node class (V2)."""

    def test_create_simple_node(self):
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="Law of excluded middle",
            dependencies=[],
            provides=["boolean_algebra"],
        )
        assert node.id == "CL"
        assert node.structural_type == "logic"
        assert len(node.dependencies) == 0

    def test_node_with_typed_parameters(self):
        params = [
            Parameter(id="P001", name="LEM", parameter_type="axiom", value="on"),
        ]
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="",
            parameters=params,
        )
        assert len(node.parameters) == 1
        assert node.parameters[0].parameter_type == "axiom"

    def test_node_with_typed_dependencies(self):
        deps = [
            Dependency(on="CL", dependency_type="conventional", note="Can use IL"),
        ]
        node = Node(
            id="FOL",
            structural_type="logic",
            label="FOL",
            description="",
            dependencies=deps,
        )
        assert len(node.dependencies) == 1
        assert node.dependencies[0].dependency_type == "conventional"

    def test_presupposes_backward_compat(self):
        """Test that presupposes property returns dependency IDs."""
        deps = [
            Dependency(on="CL", dependency_type="logical"),
            Dependency(on="FOL", dependency_type="logical"),
        ]
        node = Node(id="ZFC", structural_type="foundation", label="ZFC",
                    description="", dependencies=deps)
        assert node.presupposes == ["CL", "FOL"]

    def test_node_temporal_note(self):
        node = Node(
            id="MAN",
            structural_type="geometric_structure",
            label="Smooth manifolds",
            description="",
            temporal_note="First formal appearance of temporal structure.",
        )
        assert node.temporal_note is not None

    def test_node_contingent_provisions(self):
        node = Node(
            id="QFT",
            structural_type="quantization",
            label="QFT",
            description="",
            contingent_provisions=["Causal propagator depends on iε."],
        )
        assert len(node.contingent_provisions) == 1

    def test_dependency_filtering(self):
        deps = [
            Dependency(on="GAUGE", dependency_type="conventional"),
            Dependency(on="HILB", dependency_type="logical"),
            Dependency(on="PATH", dependency_type="conventional"),
        ]
        node = Node(id="QFT", structural_type="quantization", label="QFT",
                    description="", dependencies=deps)
        logical_deps = node.dependencies_by_type("logical")
        conv_deps = node.dependencies_by_type("conventional")
        assert len(logical_deps) == 1
        assert len(conv_deps) == 2

    def test_parameter_filtering(self):
        params = [
            Parameter(id="P054", name="Regularization", parameter_type="convention"),
            Parameter(id="P057", name="iε sign", parameter_type="boundary"),
            Parameter(id="P078", name="Vacuum state", parameter_type="boundary"),
        ]
        node = Node(id="QFT", structural_type="quantization", label="QFT",
                    description="", parameters=params)
        boundary_params = node.parameters_by_type("boundary")
        conv_params = node.parameters_by_type("convention")
        assert len(boundary_params) == 2
        assert len(conv_params) == 1

    def test_node_serialization(self):
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="CL",
            dependencies=[
                Dependency(on="X", dependency_type="logical"),
            ],
            provides=["boolean_algebra"],
            parameters=[
                Parameter(id="P001", name="LEM", parameter_type="axiom", value="on"),
            ],
            temporal_note="No temporal structure.",
        )
        d = node.to_dict()
        node2 = Node.from_dict(d)
        assert node2.id == node.id
        assert node2.label == node.label
        assert len(node2.dependencies) == 1
        assert node2.dependencies[0].dependency_type == "logical"
        assert len(node2.parameters) == 1
        assert node2.parameters[0].parameter_type == "axiom"
        assert node2.temporal_note == "No temporal structure."

    def test_node_resolved_values(self):
        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="SM gauge group",
            description="",
            resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"},
        )
        assert node.resolved_values["gauge_group"] == "SU(3)xSU(2)xU(1)"


class TestTheoryGraph:
    """Test TheoryGraph class."""

    def _make_meta(self, name="Test"):
        return TheoryGraphMeta(
            name=name, description="", version="2.0.0",
            date=datetime.utcnow().isoformat(),
        )

    def test_create_empty_graph(self):
        graph = TheoryGraph(self._make_meta())
        assert graph.meta.name == "Test"
        assert len(graph.nodes) == 0

    def test_add_nodes(self):
        graph = TheoryGraph(self._make_meta())
        node1 = Node(id="CL", structural_type="logic", label="CL", description="")
        node2 = Node(
            id="FOL", structural_type="logic", label="FOL", description="",
            dependencies=[Dependency(on="CL", dependency_type="conventional")],
        )
        graph.add_node(node1)
        graph.add_node(node2)
        graph.validate()
        assert len(graph.nodes) == 2

    def test_topological_sort(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="CL", structural_type="logic", label="CL", description=""))
        graph.add_node(Node(
            id="FOL", structural_type="logic", label="FOL", description="",
            dependencies=[Dependency(on="CL", dependency_type="conventional")],
        ))
        graph.add_node(Node(
            id="ZFC", structural_type="foundation", label="ZFC", description="",
            dependencies=[
                Dependency(on="CL", dependency_type="logical"),
                Dependency(on="FOL", dependency_type="logical"),
            ],
        ))
        graph.validate()
        topo = graph.topological_sort()
        assert topo[0] == "CL"
        assert topo.index("CL") < topo.index("FOL")
        assert topo.index("FOL") < topo.index("ZFC")

    def test_ancestors(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")]))
        graph.add_node(Node(id="C", structural_type="logic", label="C", description="",
                           dependencies=[Dependency(on="B", dependency_type="logical")]))
        graph.validate()
        assert "B" in graph.ancestors("C")
        assert "A" in graph.ancestors("C")
        assert "C" not in graph.ancestors("C")

    def test_descendants(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")]))
        graph.add_node(Node(id="C", structural_type="logic", label="C", description="",
                           dependencies=[Dependency(on="B", dependency_type="logical")]))
        graph.validate()
        assert "B" in graph.descendants("A")
        assert "C" in graph.descendants("A")
        assert "A" not in graph.descendants("A")

    def test_dependency_chain(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")]))
        graph.add_node(Node(id="C", structural_type="logic", label="C", description="",
                           dependencies=[Dependency(on="B", dependency_type="logical")]))
        graph.validate()
        chain = graph.dependency_chain("A", "C")
        assert chain == ["A", "B", "C"]

    def test_shared_subgraph(self):
        graph1 = TheoryGraph(self._make_meta("Theory1"))
        graph2 = TheoryGraph(self._make_meta("Theory2"))

        shared_node = Node(id="SHARED", structural_type="logic", label="Shared", description="")
        graph1.add_node(shared_node)
        graph2.add_node(shared_node)

        graph1.add_node(Node(id="T1_ONLY", structural_type="logic", label="T1", description="",
                            dependencies=[Dependency(on="SHARED", dependency_type="logical")]))
        graph2.add_node(Node(id="T2_ONLY", structural_type="logic", label="T2", description="",
                            dependencies=[Dependency(on="SHARED", dependency_type="logical")]))

        graph1.validate()
        graph2.validate()

        shared = graph1.shared_subgraph(graph2)
        assert "SHARED" in shared.nodes
        assert "T1_ONLY" not in shared.nodes
        assert "T2_ONLY" not in shared.nodes

    def test_temporal_chain(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="A", structural_type="logic", label="A", description=""))
        graph.add_node(Node(id="B", structural_type="logic", label="B", description="",
                           dependencies=[Dependency(on="A", dependency_type="logical")],
                           temporal_note="Time enters here."))
        graph.add_node(Node(id="C", structural_type="logic", label="C", description="",
                           dependencies=[Dependency(on="B", dependency_type="logical")],
                           temporal_note="Direction added here."))
        graph.validate()
        chain = graph.temporal_chain()
        assert chain == ["B", "C"]

    def test_boundary_parameters(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(
            id="QFT", structural_type="quantization", label="QFT", description="",
            parameters=[
                Parameter(id="P057", name="iε sign", parameter_type="boundary", value="+iε"),
                Parameter(id="P054", name="Regularization", parameter_type="convention"),
            ],
        ))
        boundary = graph.boundary_parameters()
        assert len(boundary) == 1
        assert boundary[0][1].id == "P057"

    def test_conventional_dependencies(self):
        graph = TheoryGraph(self._make_meta())
        graph.add_node(Node(id="CL", structural_type="logic", label="CL", description=""))
        graph.add_node(Node(
            id="FOL", structural_type="logic", label="FOL", description="",
            dependencies=[Dependency(on="CL", dependency_type="conventional")],
        ))
        convs = graph.conventional_dependencies()
        assert len(convs) == 1
        assert convs[0][0] == "FOL"


class TestTheoryFile:
    """Test TheoryFile class."""

    def _make_meta(self, name="Test"):
        return TheoryGraphMeta(
            name=name, description="", version="2.0.0",
            date=datetime.utcnow().isoformat(),
        )

    def test_create_theory_file(self):
        graph = TheoryGraph(self._make_meta("Test Theory"))
        node = Node(id="SM_G", structural_type="physical_theory", label="SM",
                    description="", resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"})
        graph.add_node(node)
        theory_file = TheoryFile(theory_graph=graph)
        assert theory_file.theory_graph.meta.name == "Test Theory"

    def test_theory_file_fingerprint(self):
        graph = TheoryGraph(self._make_meta())
        node = Node(id="SM_G", structural_type="physical_theory", label="", description="",
                    resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"})
        graph.add_node(node)
        theory_file = TheoryFile(theory_graph=graph)
        fp = theory_file.parametric_fingerprint
        assert len(fp) == 8
        assert all(c in "0123456789abcdef" for c in fp)

    def test_theory_file_filename(self):
        graph = TheoryGraph(self._make_meta("SM"))
        theory_file = TheoryFile(theory_graph=graph)
        filename = theory_file.filename()
        assert filename.endswith(".json")
        assert "-" in filename

    def test_theory_file_serialization(self):
        graph = TheoryGraph(self._make_meta())
        node = Node(id="TEST", structural_type="logic", label="Test", description="",
                    resolved_values={"param1": "value1"})
        graph.add_node(node)
        theory_file = TheoryFile(theory_graph=graph)
        d = theory_file.to_dict()
        assert d["meta"]["name"] == "Test"
        assert "choices" in d
        assert "TEST" in d["choices"]
