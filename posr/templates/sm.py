"""
Standard Model template (V2): loads from sm_dependency_graph_v2.json.

The V2 JSON is the authoritative machine-readable graph with:
  - 30 nodes, 79 typed parameters, 57 typed dependencies
  - Parameter subtypes: axiom, structural, kinematic, dynamical, boundary, convention
  - Dependency types: logical, conventional, contingent
  - Temporal notes and contingent provisions
  - iε prescription (P057), vacuum state (P078), Gribov region (P079) as explicit parameters
"""

import os
from ..graph import build_from_json
from ..schema import TheoryGraph


def build() -> TheoryGraph:
    """Build the Standard Model theory graph from V2 JSON.

    Returns:
        A fully configured TheoryGraph for the Standard Model.
    """
    module_dir = os.path.dirname(__file__)

    # V2 JSON is the authoritative source
    v2_path = os.path.join(
        module_dir, "..", "..",
        "deep-research", "time-symmetry-debt", "v2",
        "sm_dependency_graph_v2.json",
    )

    if os.path.exists(v2_path):
        return build_from_json(v2_path)

    # Fallback to V1 if V2 not found (should not happen in normal use)
    v1_path = os.path.join(module_dir, "..", "..", "sm_dependency_graph.json")
    if os.path.exists(v1_path):
        return build_from_json(v1_path)

    raise FileNotFoundError(
        "Neither sm_dependency_graph_v2.json nor sm_dependency_graph.json found. "
        f"Searched: {v2_path}, {v1_path}"
    )
