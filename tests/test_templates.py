"""Tests for theory templates (SM and GR, V2)."""

import pytest
import os
from posr.templates import sm, gr
from posr.diff import compute_structural_diff, dependency_type_summary, parameter_type_summary


class TestStandardModelTemplate:
    """Test SM template (V2)."""

    def test_build_sm(self):
        """Test building the Standard Model template."""
        try:
            graph = sm.build()
            assert graph is not None
            assert graph.meta.name is not None
            assert len(graph.nodes) > 0
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_has_key_nodes(self):
        """Test that SM has key structural nodes."""
        try:
            graph = sm.build()
            key_nodes = ["CL", "FOL", "ZFC", "GRP", "LA", "MAN", "CONN", "QFT", "SM_G"]
            for node_id in key_nodes:
                assert node_id in graph.nodes, f"SM missing key node: {node_id}"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_has_v2_nodes(self):
        """Test that SM has V2-specific nodes (IL, TT, CAT)."""
        try:
            graph = sm.build()
            v2_nodes = ["IL", "TT", "CAT"]
            for node_id in v2_nodes:
                assert node_id in graph.nodes, f"SM missing V2 node: {node_id}"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_topological_order(self):
        """Test that SM nodes are in valid topological order."""
        try:
            graph = sm.build()
            topo = graph.topological_sort()
            assert len(topo) == len(graph.nodes)
            for node_id in topo:
                node = graph.nodes[node_id]
                for dep_id in node.dependency_ids():
                    assert topo.index(dep_id) < topo.index(node_id)
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_typed_dependencies(self):
        """Test that SM has typed dependencies (not plain strings)."""
        try:
            graph = sm.build()
            counts = dependency_type_summary(graph)
            # V2 has both logical and conventional dependencies
            assert counts["logical"] > 0, "SM should have logical dependencies"
            assert counts["conventional"] > 0, "SM should have conventional dependencies"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_typed_parameters(self):
        """Test that SM has typed parameters across multiple subtypes."""
        try:
            graph = sm.build()
            counts = parameter_type_summary(graph)
            assert counts["axiom"] > 0, "SM should have axiom parameters"
            assert counts["structural"] > 0, "SM should have structural parameters"
            assert counts["boundary"] > 0, "SM should have boundary parameters (iε, vacuum)"
            assert counts["convention"] > 0, "SM should have convention parameters"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_iepsilon_parameter(self):
        """Test that iε is explicit in the QFT node."""
        try:
            graph = sm.build()
            qft = graph.nodes["QFT"]
            boundary_params = qft.parameters_by_type("boundary")
            ie_params = [p for p in boundary_params if "iε" in p.name or "iepsilon" in p.name.lower()]
            assert len(ie_params) >= 1, "QFT should have iε as explicit boundary parameter"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_temporal_chain(self):
        """Test that SM has temporal notes at expected locations."""
        try:
            graph = sm.build()
            temporal_nodes = graph.temporal_chain()
            # Should include at least MAN, PATH, QFT, SM_Y (from V2 temporal audit)
            assert len(temporal_nodes) >= 3, "SM should have >=3 nodes with temporal notes"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

    def test_sm_contingent_provisions(self):
        """Test that QFT and GAUGE have contingent provisions."""
        try:
            graph = sm.build()
            qft = graph.nodes["QFT"]
            assert len(qft.contingent_provisions) > 0, "QFT should have contingent provisions"
            gauge = graph.nodes["GAUGE"]
            assert len(gauge.contingent_provisions) > 0, "GAUGE should have contingent provisions"
        except FileNotFoundError:
            pytest.skip("SM JSON not available")


class TestGeneralRelativityTemplate:
    """Test GR template (V2)."""

    def test_build_gr(self):
        graph = gr.build()
        assert graph is not None
        assert graph.meta.name == "General Relativity"
        assert len(graph.nodes) > 0

    def test_gr_has_key_nodes(self):
        graph = gr.build()
        key_nodes = ["CL", "FOL", "ZFC", "MAN", "METRIC", "LEVI_CIVITA",
                     "RIEMANN", "EINSTEIN_EQ"]
        for node_id in key_nodes:
            assert node_id in graph.nodes, f"GR missing key node: {node_id}"

    def test_gr_topological_order(self):
        graph = gr.build()
        topo = graph.topological_sort()
        assert len(topo) == len(graph.nodes)
        for node_id in topo:
            node = graph.nodes[node_id]
            for dep_id in node.dependency_ids():
                assert topo.index(dep_id) < topo.index(node_id)

    def test_gr_typed_dependencies(self):
        """Test that GR has typed dependencies."""
        graph = gr.build()
        counts = dependency_type_summary(graph)
        assert counts["logical"] > 0
        assert counts["conventional"] > 0


class TestSMVsGRComparison:
    """Test comparison between SM and GR theories."""

    def test_sm_gr_shared_structure(self):
        try:
            sm_graph = sm.build()
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

        gr_graph = gr.build()
        diff = compute_structural_diff(sm_graph, gr_graph)

        shared = diff.shared_nodes
        assert "CL" in shared, "SM and GR should share classical logic"
        assert "FOL" in shared, "SM and GR should share FOL"
        assert "ZFC" in shared, "SM and GR should share ZFC"
        assert "MAN" in shared, "SM and GR should share manifold theory"

        assert len(diff.theory1_only) > 0, "SM should have unique nodes"
        assert len(diff.theory2_only) > 0, "GR should have unique nodes"

    def test_sm_gr_both_substantial(self):
        try:
            sm_graph = sm.build()
        except FileNotFoundError:
            pytest.skip("SM JSON not available")

        gr_graph = gr.build()
        assert len(sm_graph.topological_sort()) > 10
        assert len(gr_graph.topological_sort()) > 10
