"""Tests for schema module."""

import pytest
from posr.schema import (
    Node,
    ParametricSlot,
    TheoryGraph,
    TheoryGraphMeta,
    TheoryFile,
    ForkPoint,
)
from datetime import datetime


class TestParametricSlot:
    """Test ParametricSlot class."""

    def test_create_slot(self):
        slot = ParametricSlot(
            name="LEM",
            description="Law of excluded middle",
            slot_type="architectural",
            default="true",
        )
        assert slot.name == "LEM"
        assert slot.slot_type == "architectural"

    def test_slot_serialization(self):
        slot = ParametricSlot(
            name="axiom_of_choice",
            description="Axiom of Choice",
            slot_type="architectural",
            known_options=["true", "false"],
            default="true",
        )
        d = slot.to_dict()
        assert d["name"] == "axiom_of_choice"
        assert d["known_options"] == ["true", "false"]

        slot2 = ParametricSlot.from_dict(d)
        assert slot2.name == slot.name
        assert slot2.default == slot.default


class TestNode:
    """Test Node class."""

    def test_create_simple_node(self):
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="Law of excluded middle",
            presupposes=[],
            provides=["boolean_algebra"],
        )
        assert node.id == "CL"
        assert node.structural_type == "logic"
        assert len(node.presupposes) == 0

    def test_node_with_parametric_slots(self):
        slots = [
            ParametricSlot(
                name="LEM",
                description="LEM",
                slot_type="architectural",
                default="true",
            ),
        ]
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="",
            parametric_slots=slots,
        )
        assert len(node.parametric_slots) == 1
        assert node.parametric_slots[0].name == "LEM"

    def test_node_resolved_values(self):
        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="SM gauge group",
            description="",
            resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"},
        )
        assert node.resolved_values["gauge_group"] == "SU(3)xSU(2)xU(1)"

    def test_node_serialization(self):
        node = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="CL",
            presupposes=[],
            provides=["boolean_algebra"],
        )
        d = node.to_dict()
        node2 = Node.from_dict(d)
        assert node2.id == node.id
        assert node2.label == node.label


class TestTheoryGraph:
    """Test TheoryGraph class."""

    def test_create_empty_graph(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="Test graph",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)
        assert graph.meta.name == "Test"
        assert len(graph.nodes) == 0

    def test_add_nodes(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        node1 = Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="",
        )
        node2 = Node(
            id="FOL",
            structural_type="logic",
            label="FOL",
            description="",
            presupposes=["CL"],
        )

        graph.add_node(node1)
        graph.add_node(node2)
        graph.validate()

        assert len(graph.nodes) == 2
        assert "CL" in graph.nodes
        assert "FOL" in graph.nodes

    def test_topological_sort(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

        # Create a simple DAG: CL -> FOL -> ZFC
        graph.add_node(
            Node(id="CL", structural_type="logic", label="CL", description="")
        )
        graph.add_node(
            Node(
                id="FOL",
                structural_type="logic",
                label="FOL",
                description="",
                presupposes=["CL"],
            )
        )
        graph.add_node(
            Node(
                id="ZFC",
                structural_type="foundation",
                label="ZFC",
                description="",
                presupposes=["CL", "FOL"],
            )
        )
        graph.validate()

        topo = graph.topological_sort()
        assert topo[0] == "CL"
        assert topo.index("CL") < topo.index("FOL")
        assert topo.index("FOL") < topo.index("ZFC")

    def test_ancestors(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

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

        ancestors_of_c = graph.ancestors("C")
        assert "B" in ancestors_of_c
        assert "A" in ancestors_of_c
        assert "C" not in ancestors_of_c

    def test_descendants(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

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

        descendants_of_a = graph.descendants("A")
        assert "B" in descendants_of_a
        assert "C" in descendants_of_a
        assert "A" not in descendants_of_a

    def test_dependency_chain(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)

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

        chain = graph.dependency_chain("A", "C")
        assert chain == ["A", "B", "C"]

    def test_shared_subgraph(self):
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

        # Add shared nodes
        shared_node = Node(
            id="SHARED",
            structural_type="logic",
            label="Shared",
            description="",
        )
        graph1.add_node(shared_node)
        graph2.add_node(shared_node)

        # Add theory-specific nodes
        graph1.add_node(
            Node(
                id="T1_ONLY",
                structural_type="logic",
                label="T1 Only",
                description="",
                presupposes=["SHARED"],
            )
        )
        graph2.add_node(
            Node(
                id="T2_ONLY",
                structural_type="logic",
                label="T2 Only",
                description="",
                presupposes=["SHARED"],
            )
        )

        graph1.validate()
        graph2.validate()

        shared = graph1.shared_subgraph(graph2)
        assert "SHARED" in shared.nodes
        assert "T1_ONLY" not in shared.nodes
        assert "T2_ONLY" not in shared.nodes


class TestTheoryFile:
    """Test TheoryFile class."""

    def test_create_theory_file(self):
        meta = TheoryGraphMeta(
            name="Test Theory",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)
        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="SM gauge group",
            description="",
            resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"},
        )
        graph.add_node(node)

        theory_file = TheoryFile(theory_graph=graph)
        assert theory_file.theory_graph.meta.name == "Test Theory"

    def test_theory_file_fingerprint(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)
        node = Node(
            id="SM_G",
            structural_type="physical_theory",
            label="",
            description="",
            resolved_values={"gauge_group": "SU(3)xSU(2)xU(1)"},
        )
        graph.add_node(node)

        theory_file = TheoryFile(theory_graph=graph)
        fingerprint = theory_file.parametric_fingerprint
        assert len(fingerprint) == 8  # 8 hex chars
        assert all(c in "0123456789abcdef" for c in fingerprint)

    def test_theory_file_filename(self):
        meta = TheoryGraphMeta(
            name="SM",
            description="",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)
        theory_file = TheoryFile(theory_graph=graph)
        filename = theory_file.filename()
        assert filename.endswith(".json")
        assert "-" in filename

    def test_theory_file_serialization(self):
        meta = TheoryGraphMeta(
            name="Test",
            description="Test theory",
            version="0.1.0",
            date=datetime.utcnow().isoformat(),
        )
        graph = TheoryGraph(meta)
        node = Node(
            id="TEST",
            structural_type="logic",
            label="Test",
            description="",
            resolved_values={"param1": "value1"},
        )
        graph.add_node(node)

        theory_file = TheoryFile(theory_graph=graph)
        d = theory_file.to_dict()

        assert d["meta"]["name"] == "Test"
        assert "choices" in d
        assert "TEST" in d["choices"]
