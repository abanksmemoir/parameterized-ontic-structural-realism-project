"""
General Relativity template: a GR theory graph showing where it shares structure
with the Standard Model and where it forks.

Key insight: GR and SM share much structure up to the connection/curvature layer.
They fork at whether the connection lives on a tangent bundle (GR) or internal
gauge bundle (SM).
"""

from datetime import datetime
from ..schema import (
    TheoryGraph,
    TheoryGraphMeta,
    Node,
    ParametricSlot,
)


def build() -> TheoryGraph:
    """Build the General Relativity theory graph.

    GR shares with SM:
      - Classical logic (CL)
      - First-order logic (FOL)
      - ZFC set theory
      - Group theory
      - Linear algebra
      - Topology
      - Real analysis
      - Lie groups and algebras
      - Smooth manifolds
      - Fiber bundles
      - Connection theory (on a different bundle)

    GR-specific:
      - Levi-Civita connection (metric-compatible, torsion-free)
      - Riemann curvature tensor
      - Einstein field equations
      - Stress-energy tensor coupling
      - Diffeomorphism invariance (gauge symmetry)
      - Topological considerations (global structure, causality)

    Fork point: CONN (Connections & Curvature)
      - SM instantiates connections on internal gauge bundles
      - GR instantiates connections on the tangent bundle of spacetime

    Returns:
        A fully configured TheoryGraph for General Relativity.
    """
    meta = TheoryGraphMeta(
        name="General Relativity",
        description="Gravitational theory as geometry of spacetime curvature",
        version="0.1.0",
        date=datetime.utcnow().isoformat(),
    )

    graph = TheoryGraph(meta)

    # Shared nodes (same as SM up to CONN)
    shared_nodes = [
        # Logic layer
        Node(
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
            ],
        ),
        Node(
            id="FOL",
            structural_type="logic",
            label="First-order logic",
            description="Universal and existential quantification over individuals.",
            presupposes=["CL"],
            provides=["quantified_statements", "model_theory"],
            parametric_slots=[],
        ),
        # Foundations layer
        Node(
            id="ZFC",
            structural_type="foundation",
            label="ZFC set theory",
            description="Zermelo-Fraenkel with Choice.",
            presupposes=["CL", "FOL"],
            provides=["infinite_sets", "powersets", "well_ordering"],
            parametric_slots=[
                ParametricSlot(
                    name="axiom_of_choice",
                    description="Axiom of Choice",
                    slot_type="architectural",
                    known_options=["true", "false"],
                    default="true",
                ),
            ],
        ),
        # Algebra layer
        Node(
            id="GRP",
            structural_type="algebraic_structure",
            label="Group theory",
            description="Sets with associative binary operation, identity, inverses.",
            presupposes=["ZFC"],
            provides=["subgroups", "quotient_groups", "homomorphisms"],
            parametric_slots=[],
        ),
        Node(
            id="RING",
            structural_type="algebraic_structure",
            label="Rings & fields",
            description="Groups with additional multiplicative structure.",
            presupposes=["GRP"],
            provides=["ideals", "field_extensions"],
            parametric_slots=[],
        ),
        Node(
            id="LA",
            structural_type="algebraic_structure",
            label="Linear algebra",
            description="Vector spaces over fields.",
            presupposes=["RING"],
            provides=["bases", "dual_spaces", "tensor_products"],
            parametric_slots=[],
        ),
        # Topology & analysis layer
        Node(
            id="TOP",
            structural_type="analytic_structure",
            label="Point-set topology",
            description="Open sets, continuity, compactness.",
            presupposes=["ZFC"],
            provides=["continuous_maps", "compactness", "hausdorff_separation"],
            parametric_slots=[],
        ),
        Node(
            id="REAL",
            structural_type="analytic_structure",
            label="Real analysis",
            description="Completeness of R, limits, measure theory.",
            presupposes=["ZFC", "TOP"],
            provides=["lebesgue_measure", "lp_spaces"],
            parametric_slots=[],
        ),
        # Lie theory layer
        Node(
            id="LIE",
            structural_type="algebraic_structure",
            label="Lie groups",
            description="Smooth manifolds with compatible group structure.",
            presupposes=["GRP", "TOP", "REAL"],
            provides=["exponential_map", "adjoint_representation"],
            parametric_slots=[],
        ),
        Node(
            id="LIEA",
            structural_type="algebraic_structure",
            label="Lie algebras",
            description="Tangent space at identity of a Lie group.",
            presupposes=["LIE", "LA"],
            provides=["root_systems", "cartan_subalgebras"],
            parametric_slots=[],
        ),
        # Differential geometry layer
        Node(
            id="MAN",
            structural_type="geometric_structure",
            label="Smooth manifolds",
            description="Locally Euclidean spaces with smooth transition maps.",
            presupposes=["TOP", "REAL", "LA"],
            provides=["tangent_bundles", "differential_forms", "de_rham_cohomology"],
            parametric_slots=[
                ParametricSlot(
                    name="dimension",
                    description="Manifold dimension (spacetime: 4)",
                    slot_type="runtime",
                    default="4",
                ),
                ParametricSlot(
                    name="metric_signature",
                    description="Metric signature",
                    slot_type="runtime",
                    known_options=["(+,-,-,-)", "(-,+,+,+)", "euclidean"],
                    default="(+,-,-,-)",
                ),
            ],
        ),
        Node(
            id="FB",
            structural_type="geometric_structure",
            label="Fiber bundles",
            description="Spaces locally product but globally twisted.",
            presupposes=["MAN", "GRP"],
            provides=["sections", "bundle_maps", "associated_bundles"],
            parametric_slots=[],
        ),
        # GR-specific layer starts here
        Node(
            id="METRIC",
            structural_type="geometric_structure",
            label="Riemannian/pseudo-Riemannian geometry",
            description="Metric tensor on manifolds. Defines distances and angles.",
            presupposes=["MAN", "LA"],
            provides=["induced_topology", "geodesics", "volume_form"],
            parametric_slots=[
                ParametricSlot(
                    name="signature",
                    description="Euclidean (+,+,+,+), Lorentzian (+,-,-,-), or other",
                    slot_type="architectural",
                    known_options=["euclidean", "lorentzian", "split"],
                    default="lorentzian",
                ),
            ],
        ),
        Node(
            id="LEVI_CIVITA",
            structural_type="geometric_structure",
            label="Levi-Civita connection",
            description="Unique metric-compatible, torsion-free connection on (pseudo-)Riemannian manifold.",
            presupposes=["METRIC", "FB", "LIEA"],
            provides=["parallel_transport", "geodesic_deviation"],
            parametric_slots=[
                ParametricSlot(
                    name="connection_type",
                    description="Metric-compatible and torsion-free by definition on tangent bundle",
                    slot_type="architectural",
                    default="metric_compatible_torsion_free",
                ),
            ],
        ),
        Node(
            id="RIEMANN",
            structural_type="geometric_structure",
            label="Riemann curvature",
            description="Curvature tensor measuring non-commutativity of covariant derivatives.",
            presupposes=["LEVI_CIVITA"],
            provides=["ricci_tensor", "scalar_curvature", "curvature_forms"],
            parametric_slots=[],
        ),
        Node(
            id="EINSTEIN_EQ",
            structural_type="dynamical_principle",
            label="Einstein field equations",
            description="Relate curvature to matter/energy via Ricci tensor and Einstein tensor.",
            presupposes=["RIEMANN"],
            provides=["gravitational_dynamics", "solution_space"],
            parametric_slots=[
                ParametricSlot(
                    name="cosmological_constant",
                    description="Presence of cosmological constant term",
                    slot_type="architectural",
                    known_options=["present", "absent"],
                    default="present",
                ),
                ParametricSlot(
                    name="lambda_value",
                    description="Cosmological constant value (if present)",
                    slot_type="runtime",
                    default="small_positive",
                ),
            ],
        ),
        Node(
            id="STRESS_ENERGY",
            structural_type="physical_theory",
            label="Stress-energy coupling",
            description="Matter couples to gravity via stress-energy tensor. Energy-momentum conservation.",
            presupposes=["EINSTEIN_EQ"],
            provides=["matter_coupling", "energy_momentum_conservation"],
            parametric_slots=[],
        ),
        Node(
            id="GR_CAUSALITY",
            structural_type="physical_theory",
            label="Causal structure & global topology",
            description="Global structure of spacetime: causality conditions, topology, boundary conditions.",
            presupposes=["METRIC", "STRESS_ENERGY"],
            provides=["light_cones", "causality_constraints", "topological_structure"],
            parametric_slots=[
                ParametricSlot(
                    name="global_hyperbolicity",
                    description="Spacetime is globally hyperbolic",
                    slot_type="architectural",
                    known_options=["true", "false"],
                    default="true",
                ),
                ParametricSlot(
                    name="time_orientation",
                    description="Time-orientation (time-orientable or not)",
                    slot_type="architectural",
                    known_options=["oriented", "non_oriented"],
                    default="oriented",
                ),
            ],
        ),
    ]

    for node in shared_nodes:
        graph.add_node(node)

    graph.validate()
    return graph
