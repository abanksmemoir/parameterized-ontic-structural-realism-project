"""
Registry of known node types and their parametric options.

This module provides pre-configured node templates and options for
common structural concepts in physics and mathematics.
"""

from typing import Dict, List, Optional
from .schema import Node, ParametricSlot


# Standard structural type categories
STRUCTURAL_TYPES = {
    "logic": "Deductive system and proof structure",
    "foundation": "Set-theoretic or type-theoretic substrate",
    "algebraic_structure": "Groups, rings, fields, algebras",
    "geometric_structure": "Manifolds, bundles, topology",
    "analytic_structure": "Analysis, measure theory, functional spaces",
    "dynamical_principle": "Lagrangian, Hamiltonian, equations of motion",
    "quantization": "Path integral, operator algebras, Hilbert spaces",
    "physical_theory": "Specific physical theories (SM, GR, etc.)",
}


# Known parametric options for common structural concepts
PARAMETRIC_OPTIONS = {
    "logic_choice": {
        "options": ["classical", "intuitionistic", "paraconsistent", "linear"],
        "default": "classical",
    },
    "foundation_choice": {
        "options": ["ZFC", "ZF", "type_theory", "category_theory"],
        "default": "ZFC",
    },
    "gauge_group": {
        "options": ["SU(3)xSU(2)xU(1)", "SU(5)", "SO(10)", "E(6)", "E(8)"],
        "default": "SU(3)xSU(2)xU(1)",
    },
    "num_generations": {
        "options": ["1", "2", "3", "4"],
        "default": "3",
    },
    "time_asymmetry": {
        "options": ["retarded", "advanced", "wheeler_feynman", "symmetric"],
        "default": "retarded",
    },
    "metric_signature": {
        "options": ["(+,-,-,-)", "(-,+,+,+)", "euclidean"],
        "default": "(+,-,-,-)",
    },
}


def node_template(node_id: str) -> Optional[Node]:
    """Retrieve a pre-configured node template by ID.

    Returns None if the template is not registered.
    """
    templates = {
        "CL": Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="Law of excluded middle, double negation elimination, material conditional.",
            presupposes=[],
            provides=["proof_by_contradiction", "de_morgan_duality", "boolean_algebra"],
            parametric_slots=[
                ParametricSlot(
                    name="LEM",
                    description="Law of excluded middle",
                    slot_type="architectural",
                    default="true",
                ),
                ParametricSlot(
                    name="explosion",
                    description="Principle of explosion (ex falso quodlibet)",
                    slot_type="architectural",
                    default="true",
                ),
            ],
        ),
        "ZFC": Node(
            id="ZFC",
            structural_type="foundation",
            label="ZFC set theory",
            description="Zermelo-Fraenkel with Choice.",
            presupposes=["CL", "FOL"],
            provides=["infinite_sets", "powersets", "well_ordering", "cartesian_products"],
            parametric_slots=[
                ParametricSlot(
                    name="axiom_of_choice",
                    description="Axiom of Choice",
                    slot_type="architectural",
                    known_options=["true", "false"],
                    default="true",
                ),
                ParametricSlot(
                    name="foundation",
                    description="Axiom of Foundation",
                    slot_type="architectural",
                    known_options=["true", "false"],
                    default="true",
                ),
            ],
        ),
        "FOL": Node(
            id="FOL",
            structural_type="logic",
            label="First-order logic",
            description="Universal and existential quantification over individuals.",
            presupposes=["CL"],
            provides=["quantified_statements", "model_theory"],
            parametric_slots=[
                ParametricSlot(
                    name="sorts",
                    description="Single or many-sorted",
                    slot_type="architectural",
                    known_options=["single", "many"],
                    default="single",
                ),
            ],
        ),
        "GRP": Node(
            id="GRP",
            structural_type="algebraic_structure",
            label="Group theory",
            description="Sets with associative binary operation, identity, inverses.",
            presupposes=["ZFC"],
            provides=["subgroups", "quotient_groups", "homomorphisms", "group_actions"],
            parametric_slots=[
                ParametricSlot(
                    name="commutativity",
                    description="Abelian vs non-abelian",
                    slot_type="architectural",
                    known_options=["abelian", "non_abelian"],
                    default="non_abelian",
                ),
            ],
        ),
        "LA": Node(
            id="LA",
            structural_type="algebraic_structure",
            label="Linear algebra",
            description="Vector spaces over fields.",
            presupposes=["RING"],
            provides=["bases", "dual_spaces", "tensor_products", "inner_products"],
            parametric_slots=[
                ParametricSlot(
                    name="base_field",
                    description="Base field (R, C, or other)",
                    slot_type="runtime",
                    known_options=["R", "C"],
                    default="C",
                ),
                ParametricSlot(
                    name="inner_product_signature",
                    description="Signature of inner product if defined",
                    slot_type="runtime",
                    default="euclidean",
                ),
            ],
        ),
        "MAN": Node(
            id="MAN",
            structural_type="geometric_structure",
            label="Smooth manifolds",
            description="Locally Euclidean spaces with smooth transition maps.",
            presupposes=["TOP", "REAL", "LA"],
            provides=["tangent_bundles", "differential_forms", "de_rham_cohomology"],
            parametric_slots=[
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
        ),
        "CONN": Node(
            id="CONN",
            structural_type="geometric_structure",
            label="Connections & curvature",
            description="Parallel transport on fiber bundles.",
            presupposes=["FB", "LIEA"],
            provides=["covariant_derivative", "holonomy", "characteristic_classes"],
            parametric_slots=[
                ParametricSlot(
                    name="bundle_type",
                    description="Which bundle the connection lives on (principal, tangent, internal gauge)",
                    slot_type="architectural",
                    known_options=["principal", "tangent", "internal_gauge"],
                    default="principal",
                ),
                ParametricSlot(
                    name="torsion",
                    description="Presence of torsion",
                    slot_type="architectural",
                    known_options=["present", "absent"],
                    default="absent",
                ),
            ],
        ),
        "QFT": Node(
            id="QFT",
            structural_type="quantization",
            label="Field quantization",
            description="Promote fields to operator-valued distributions.",
            presupposes=["GAUGE", "HILB", "PATH"],
            provides=["feynman_diagrams", "s_matrix", "vacuum_state", "particle_interpretation"],
            parametric_slots=[
                ParametricSlot(
                    name="time_asymmetry",
                    description="Time symmetry choice (retarded, advanced, or symmetric)",
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
        ),
        "SM_G": Node(
            id="SM_G",
            structural_type="physical_theory",
            label="Standard Model gauge group",
            description="The gauge group SU(3)×SU(2)×U(1).",
            presupposes=["GAUGE", "ANOM", "RENORM"],
            provides=["strong_interaction", "weak_interaction", "electromagnetic_interaction"],
            parametric_slots=[
                ParametricSlot(
                    name="gauge_group",
                    description="Specific gauge group structure",
                    slot_type="architectural",
                    known_options=["SU(3)xSU(2)xU(1)", "SU(5)", "SO(10)", "E(6)"],
                    default="SU(3)xSU(2)xU(1)",
                ),
                ParametricSlot(
                    name="g3",
                    description="Strong coupling constant",
                    slot_type="runtime",
                    default="1.221",
                ),
                ParametricSlot(
                    name="g2",
                    description="Weak coupling constant",
                    slot_type="runtime",
                    default="0.652",
                ),
                ParametricSlot(
                    name="g1",
                    description="Hypercharge coupling constant",
                    slot_type="runtime",
                    default="0.357",
                ),
            ],
        ),
        "SM_F": Node(
            id="SM_F",
            structural_type="physical_theory",
            label="Fermion content",
            description="Quark and lepton fields in specific representations.",
            presupposes=["SM_G", "REP", "ANOM"],
            provides=["quark_fields", "lepton_fields", "anomaly_constraints"],
            parametric_slots=[
                ParametricSlot(
                    name="num_generations",
                    description="Number of fermion generations",
                    slot_type="architectural",
                    known_options=["1", "2", "3", "4"],
                    default="3",
                ),
            ],
        ),
    }

    return templates.get(node_id)


def get_parametric_options(parameter_name: str) -> Dict[str, any]:
    """Get known options for a parametric slot by name.

    Returns a dict with 'options' (list) and 'default' keys.
    """
    return PARAMETRIC_OPTIONS.get(parameter_name, {})
