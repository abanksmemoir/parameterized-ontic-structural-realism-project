"""
Standard Model template: converts sm_dependency_graph.json to the new schema
and enriches it with parametric information.
"""

import json
from typing import Dict, Any
from datetime import datetime
from ..schema import (
    TheoryGraph,
    TheoryGraphMeta,
    Node,
    ParametricSlot,
)


def load_from_json(json_path: str) -> TheoryGraph:
    """Load the SM dependency graph from the original JSON file.

    Converts the old format to the new schema, enriching nodes with
    structural_type and formalized parametric_slots.

    Args:
        json_path: Path to sm_dependency_graph.json

    Returns:
        A TheoryGraph representing the Standard Model.
    """
    with open(json_path, "r") as f:
        data = json.load(f)

    meta_data = data.get("meta", {})
    meta = TheoryGraphMeta(
        name=meta_data.get("project", "Standard Model"),
        description=meta_data.get("description", ""),
        version=meta_data.get("version", "0.1.0"),
        date=meta_data.get("date", datetime.utcnow().isoformat()),
    )

    graph = TheoryGraph(meta)

    # Map layer index to structural type
    layer_type_map = {
        0: "logic",
        1: "foundation",
        2: "algebraic_structure",
        3: "analytic_structure",
        4: "algebraic_structure",
        5: "geometric_structure",
        6: "analytic_structure",
        7: "dynamical_principle",
        8: "quantization",
        9: "physical_theory",
    }

    for layer in data.get("layers", []):
        layer_idx = layer.get("index", 0)
        structural_type = layer_type_map.get(layer_idx, "unknown")

        for node_data in layer.get("nodes", []):
            node_id = node_data["id"]

            # Convert parametric descriptions to ParametricSlot objects
            parametric_slots = _parse_parametric_descriptions(
                node_id, node_data.get("parametric", [])
            )

            node = Node(
                id=node_id,
                structural_type=structural_type,
                label=node_data["label"],
                description=node_data["description"],
                presupposes=node_data.get("presupposes", []),
                provides=node_data.get("provides", []),
                parametric_slots=parametric_slots,
            )
            graph.add_node(node)

    graph.validate()
    return graph


def _parse_parametric_descriptions(node_id: str, parametric_descs: list) -> list:
    """Parse parametric descriptions from old JSON format into ParametricSlot objects.

    Examples of old format descriptions:
      - "LEM can be dropped → intuitionistic"
      - "Axiom of Choice (drop → ZF)"
      - "Why 3 generations? Why these coupling constants?"

    This function extracts the key parametric information and creates slots.
    """
    slots = []

    # Node-specific slot definitions
    node_slot_defs = {
        "CL": [
            ParametricSlot(
                name="LEM",
                description="Law of excluded middle (can drop → intuitionistic)",
                slot_type="architectural",
                known_options=["true", "false"],
                default="true",
            ),
            ParametricSlot(
                name="explosion",
                description="Principle of explosion (can drop → paraconsistent)",
                slot_type="architectural",
                known_options=["true", "false"],
                default="true",
            ),
        ],
        "ZFC": [
            ParametricSlot(
                name="axiom_of_choice",
                description="Axiom of Choice (can drop → ZF)",
                slot_type="architectural",
                known_options=["true", "false"],
                default="true",
            ),
            ParametricSlot(
                name="foundation",
                description="Axiom of Foundation (can drop → non-well-founded sets)",
                slot_type="architectural",
                known_options=["true", "false"],
                default="true",
            ),
            ParametricSlot(
                name="continuum_hypothesis",
                description="Continuum hypothesis (independent of ZFC)",
                slot_type="architectural",
                known_options=["true", "false", "independent"],
                default="independent",
            ),
        ],
        "FOL": [
            ParametricSlot(
                name="logic_base",
                description="Classical or intuitionistic logic",
                slot_type="architectural",
                known_options=["classical", "intuitionistic"],
                default="classical",
            ),
            ParametricSlot(
                name="sorts",
                description="Single or many-sorted FOL",
                slot_type="architectural",
                known_options=["single", "many"],
                default="single",
            ),
        ],
        "LIE": [
            ParametricSlot(
                name="compactness",
                description="Compact or non-compact Lie group",
                slot_type="architectural",
                known_options=["compact", "non_compact"],
                default="compact",
            ),
            ParametricSlot(
                name="connectedness",
                description="Connected or disconnected",
                slot_type="architectural",
                known_options=["connected", "disconnected"],
                default="connected",
            ),
        ],
        "LIEA": [
            ParametricSlot(
                name="type",
                description="Lie algebra type (A,B,C,D,E,F,G)",
                slot_type="architectural",
                known_options=["A", "B", "C", "D", "E", "F", "G"],
                default=None,
            ),
            ParametricSlot(
                name="rank",
                description="Rank of the algebra",
                slot_type="runtime",
                default=None,
            ),
        ],
        "MAN": [
            ParametricSlot(
                name="dimension",
                description="Manifold dimension",
                slot_type="runtime",
                default="4",
            ),
            ParametricSlot(
                name="orientability",
                description="Orientable or non-orientable",
                slot_type="architectural",
                known_options=["orientable", "non_orientable"],
                default="orientable",
            ),
            ParametricSlot(
                name="metric_signature",
                description="Metric signature if metric present",
                slot_type="runtime",
                known_options=["(+,-,-,-)", "(-,+,+,+)", "euclidean"],
                default="(+,-,-,-)",
            ),
        ],
        "CONN": [
            ParametricSlot(
                name="bundle_type",
                description="Principal, tangent, or internal gauge bundle",
                slot_type="architectural",
                known_options=["principal", "tangent", "internal_gauge"],
                default="principal",
            ),
            ParametricSlot(
                name="torsion",
                description="Torsion-free or with torsion",
                slot_type="architectural",
                known_options=["torsion_free", "with_torsion"],
                default="torsion_free",
            ),
        ],
        "QFT": [
            ParametricSlot(
                name="time_asymmetry",
                description="Time asymmetry convention (retarded, advanced, symmetric)",
                slot_type="architectural",
                known_options=["retarded", "advanced", "wheeler_feynman", "symmetric"],
                default="retarded",
            ),
            ParametricSlot(
                name="regularization",
                description="UV regularization scheme",
                slot_type="runtime",
                known_options=["dimensional", "cutoff", "zeta"],
                default="dimensional",
            ),
        ],
        "SM_G": [
            ParametricSlot(
                name="gauge_group",
                description="Gauge group structure (why SU(3)×SU(2)×U(1) and not SU(5)?)",
                slot_type="architectural",
                known_options=["SU(3)xSU(2)xU(1)", "SU(5)", "SO(10)", "E(6)", "E(8)"],
                default="SU(3)xSU(2)xU(1)",
            ),
            ParametricSlot(
                name="g3",
                description="Strong coupling constant at MZ scale",
                slot_type="runtime",
                default="1.221",
            ),
            ParametricSlot(
                name="g2",
                description="Weak coupling constant at MZ scale",
                slot_type="runtime",
                default="0.652",
            ),
            ParametricSlot(
                name="g1",
                description="Hypercharge coupling constant at MZ scale",
                slot_type="runtime",
                default="0.357",
            ),
        ],
        "SM_F": [
            ParametricSlot(
                name="num_generations",
                description="Number of fermion generations (why 3?)",
                slot_type="architectural",
                known_options=["1", "2", "3", "4"],
                default="3",
            ),
        ],
        "SM_H": [
            ParametricSlot(
                name="higgs_potential_type",
                description="Higgs potential structure",
                slot_type="architectural",
                known_options=["mexican_hat", "other"],
                default="mexican_hat",
            ),
            ParametricSlot(
                name="vev",
                description="Higgs vacuum expectation value",
                slot_type="runtime",
                default="246.22",
            ),
            ParametricSlot(
                name="lambda",
                description="Higgs self-coupling constant",
                slot_type="runtime",
                default="0.129",
            ),
        ],
        "SM_Y": [
            ParametricSlot(
                name="ckm_parameterization",
                description="CKM matrix parameterization",
                slot_type="runtime",
                default="standard",
            ),
            ParametricSlot(
                name="neutrino_mass_mechanism",
                description="Neutrino mass generation mechanism",
                slot_type="architectural",
                known_options=["dirac", "majorana", "see_saw"],
                default="dirac",
            ),
        ],
    }

    # Return predefined slots if available
    if node_id in node_slot_defs:
        return node_slot_defs[node_id]

    # Fallback: create generic slots from descriptions
    for i, desc in enumerate(parametric_descs):
        slot_type = "architectural" if "drop" in desc or "change" in desc.lower() else "runtime"
        slots.append(
            ParametricSlot(
                name=f"param_{i}",
                description=desc,
                slot_type=slot_type,
                known_options=None,
                default=None,
            )
        )

    return slots


def build() -> TheoryGraph:
    """Build the Standard Model theory graph from JSON.

    This is the high-level entry point that loads and constructs the SM graph.

    Returns:
        A fully configured TheoryGraph for the Standard Model.
    """
    import os

    # Try to find the JSON file relative to this module
    module_dir = os.path.dirname(__file__)
    json_path = os.path.join(module_dir, "..", "..", "sm_dependency_graph.json")

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"sm_dependency_graph.json not found at {json_path}")

    return load_from_json(json_path)
