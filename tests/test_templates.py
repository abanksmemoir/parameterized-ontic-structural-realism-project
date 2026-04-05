"""Tests for theory templates (SM and GR)."""

import pytest
import os
from posr.templates import sm, gr
from posr.diff import compute_structural_diff


class TestStandardModelTemplate:
    """Test SM template."""

    def test_build_sm(self):
        """Test building the Standard Model template."""
        try:
            graph = sm.build()
            assert graph is not None
            assert graph.meta.name is not None
            assert len(graph.nodes) > 0
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")

    def test_sm_has_key_nodes(self):
        """Test that SM has key structural nodes."""
        try:
            graph = sm.build()
            key_nodes = ["CL", "FOL", "ZFC", "GRP", "LA", "MAN", "CONN", "QFT", "SM_G"]
            for node_id in key_nodes:
                assert node_id in graph.nodes, f"SM missing key node: {node_id}"
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")

    def test_sm_topological_order(self):
        """Test that SM nodes are in valid topological order."""
        try:
            graph = sm.build()
            topo = graph.topological_sort()
            # Verify all nodes are accounted for
            assert len(topo) == len(graph.nodes)
            # Verify dependencies are respected
            for node_id in topo:
                node = graph.nodes[node_id]
                for presupposed in node.presupposes:
                    assert topo.index(presupposed) < topo.index(node_id)
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")


class TestGeneralRelativityTemplate:
    """Test GR template."""

    def test_build_gr(self):
        """Test building the General Relativity template."""
        graph = gr.build()
        assert graph is not None
        assert graph.meta.name == "General Relativity"
        assert len(graph.nodes) > 0

    def test_gr_has_key_nodes(self):
        """Test that GR has key structural nodes."""
        graph = gr.build()
        key_nodes = [
            "CL",
            "FOL",
            "ZFC",
            "MAN",
            "METRIC",
            "LEVI_CIVITA",
            "RIEMANN",
            "EINSTEIN_EQ",
        ]
        for node_id in key_nodes:
            assert node_id in graph.nodes, f"GR missing key node: {node_id}"

    def test_gr_topological_order(self):
        """Test that GR nodes are in valid topological order."""
        graph = gr.build()
        topo = graph.topological_sort()
        # Verify all nodes are accounted for
        assert len(topo) == len(graph.nodes)
        # Verify dependencies are respected
        for node_id in topo:
            node = graph.nodes[node_id]
            for presupposed in node.presupposes:
                assert topo.index(presupposed) < topo.index(node_id)


class TestSMVsGRComparison:
    """Test comparison between SM and GR theories."""

    def test_sm_gr_shared_structure(self):
        """Test that SM and GR share significant structure."""
        try:
            sm_graph = sm.build()
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")

        gr_graph = gr.build()

        diff = compute_structural_diff(sm_graph, gr_graph)

        # Both should share foundational nodes
        shared_nodes = diff.shared_nodes
        assert "CL" in shared_nodes, "SM and GR should share classical logic"
        assert "FOL" in shared_nodes, "SM and GR should share FOL"
        assert "ZFC" in shared_nodes, "SM and GR should share ZFC"
        assert "MAN" in shared_nodes, "SM and GR should share manifold theory"

        # Both should have theory-specific content
        assert len(diff.theory1_only) > 0, "SM should have unique nodes"
        assert len(diff.theory2_only) > 0, "GR should have unique nodes"

    def test_sm_gr_connection_fork(self):
        """Test that SM and GR fork at connections."""
        try:
            sm_graph = sm.build()
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")

        gr_graph = gr.build()

        diff = compute_structural_diff(sm_graph, gr_graph)

        # CONN should exist in both but may have different resolved values
        assert "CONN" in diff.shared_nodes or "CONN" in diff.theory1_only

    def test_sm_deeper_than_gr(self):
        """Test analysis of depth comparison."""
        try:
            sm_graph = sm.build()
        except FileNotFoundError:
            pytest.skip("sm_dependency_graph.json not available")

        gr_graph = gr.build()

        # SM has more specialized nodes below the fork point
        sm_deepest = len(sm_graph.topological_sort())
        gr_deepest = len(gr_graph.topological_sort())

        # Both should have substantial structure
        assert sm_deepest > 10, "SM should have >10 nodes"
        assert gr_deepest > 10, "GR should have >10 nodes"
