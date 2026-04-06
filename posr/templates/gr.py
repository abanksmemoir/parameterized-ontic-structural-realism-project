"""
General Relativity template (V2): typed dependencies and parameters.

Key insight: GR and SM share much structure up to the connection/curvature layer.
They fork at whether the connection lives on a tangent bundle (GR) or internal
gauge bundle (SM).

V2 changes: all dependencies are typed (logical/conventional), parameters have
subtypes (axiom/structural/kinematic/dynamical/boundary/convention), temporal
notes are added where applicable.
"""

from datetime import datetime
from ..schema import (
    TheoryGraph,
    TheoryGraphMeta,
    Node,
    Parameter,
    Dependency,
)


def build() -> TheoryGraph:
    """Build the General Relativity theory graph (V2).

    GR shares with SM:
      - Classical logic (CL), FOL, ZFC, Group theory, Linear algebra,
        Topology, Real analysis, Lie groups/algebras, Smooth manifolds,
        Fiber bundles

    GR-specific:
      - Levi-Civita connection (metric-compatible, torsion-free)
      - Riemann curvature tensor
      - Einstein field equations
      - Stress-energy tensor coupling
      - Causal structure & global topology

    Fork point: CONN (SM) vs METRIC/LEVI_CIVITA (GR)
      - SM instantiates connections on internal gauge bundles
      - GR instantiates connections on the tangent bundle of spacetime
    """
    meta = TheoryGraphMeta(
        name="General Relativity",
        description="Gravitational theory as geometry of spacetime curvature",
        version="2.0.0",
        date=datetime.utcnow().isoformat(),
    )

    graph = TheoryGraph(meta)

    nodes = [
        # ── Layer 0: Logic ──
        Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="Law of excluded middle, double negation elimination, material conditional.",
            dependencies=[],
            provides=["Proof by contradiction", "De Morgan duality", "Boolean algebra"],
            parameters=[
                Parameter(id="P001", name="Law of excluded middle", parameter_type="axiom",
                         value="on", alternatives=["off (intuitionistic)"]),
            ],
        ),
        Node(
            id="FOL",
            structural_type="logic",
            label="First-order logic",
            description="Universal and existential quantification over individuals.",
            dependencies=[
                Dependency(on="CL", dependency_type="conventional",
                          note="FOL can be built on IL"),
            ],
            provides=["Quantified statements", "Model theory"],
            parameters=[],
        ),

        # ── Layer 1: Foundations ──
        Node(
            id="ZFC",
            structural_type="foundation",
            label="ZFC set theory",
            description="Zermelo-Fraenkel with Choice.",
            dependencies=[
                Dependency(on="CL", dependency_type="logical",
                          note="ZFC is formulated in classical logic"),
                Dependency(on="FOL", dependency_type="logical",
                          note="ZFC axioms are first-order sentences"),
            ],
            provides=["Infinite sets", "Powersets", "Well-ordering"],
            parameters=[
                Parameter(id="P006", name="Axiom of choice", parameter_type="axiom",
                         value="included", alternatives=["excluded (ZF)"]),
            ],
        ),

        # ── Layer 2: Core algebra ──
        Node(
            id="GRP",
            structural_type="algebraic_structure",
            label="Group theory",
            description="Sets with associative binary operation, identity, inverses.",
            dependencies=[
                Dependency(on="ZFC", dependency_type="conventional",
                          note="Needs foundational substrate; ZFC is standard"),
            ],
            provides=["Subgroups", "Quotient groups", "Homomorphisms"],
            parameters=[],
        ),
        Node(
            id="RING",
            structural_type="algebraic_structure",
            label="Rings and fields",
            description="Groups with additional multiplicative structure.",
            dependencies=[
                Dependency(on="GRP", dependency_type="logical",
                          note="Rings are abelian groups with multiplication"),
            ],
            provides=["Ideals", "Field extensions"],
            parameters=[],
        ),
        Node(
            id="LA",
            structural_type="algebraic_structure",
            label="Linear algebra",
            description="Vector spaces over fields.",
            dependencies=[
                Dependency(on="RING", dependency_type="logical",
                          note="Vector spaces are modules over fields"),
            ],
            provides=["Bases", "Dual spaces", "Tensor products"],
            parameters=[],
        ),

        # ── Layer 3: Topology & analysis ──
        Node(
            id="TOP",
            structural_type="analytic_structure",
            label="Point-set topology",
            description="Open sets, continuity, compactness.",
            dependencies=[
                Dependency(on="ZFC", dependency_type="conventional",
                          note="Can be developed constructively"),
            ],
            provides=["Continuous maps", "Compactness", "Hausdorff separation"],
            parameters=[],
        ),
        Node(
            id="REAL",
            structural_type="analytic_structure",
            label="Real analysis",
            description="Completeness of R, limits, measure theory.",
            dependencies=[
                Dependency(on="ZFC", dependency_type="logical",
                          note="Dedekind construction requires powersets"),
                Dependency(on="TOP", dependency_type="logical",
                          note="Metric topology is foundational"),
            ],
            provides=["Lebesgue measure", "L^p spaces"],
            parameters=[],
            temporal_note="R provides the continuum that will parameterize time.",
        ),

        # ── Layer 4: Lie theory ──
        Node(
            id="LIE",
            structural_type="algebraic_structure",
            label="Lie groups",
            description="Smooth manifolds with compatible group structure.",
            dependencies=[
                Dependency(on="GRP", dependency_type="logical", note="Lie groups are groups"),
                Dependency(on="TOP", dependency_type="logical", note="Lie groups are topological spaces"),
                Dependency(on="REAL", dependency_type="logical", note="Smooth structure requires R"),
            ],
            provides=["Exponential map", "Adjoint representation"],
            parameters=[],
        ),
        Node(
            id="LIEA",
            structural_type="algebraic_structure",
            label="Lie algebras",
            description="Tangent space at identity of a Lie group.",
            dependencies=[
                Dependency(on="LIE", dependency_type="conventional",
                          note="Lie algebras can be defined purely algebraically"),
                Dependency(on="LA", dependency_type="logical",
                          note="Lie algebras are vector spaces with bracket"),
            ],
            provides=["Root systems", "Cartan subalgebras"],
            parameters=[],
        ),

        # ── Layer 5: Differential geometry ──
        Node(
            id="MAN",
            structural_type="geometric_structure",
            label="Smooth manifolds",
            description="Locally Euclidean spaces with smooth transition maps.",
            dependencies=[
                Dependency(on="TOP", dependency_type="logical", note="Manifolds are topological spaces"),
                Dependency(on="REAL", dependency_type="logical", note="Charts map to R^n"),
                Dependency(on="LA", dependency_type="logical", note="Tangent spaces are vector spaces"),
            ],
            provides=["Tangent/cotangent bundles", "Differential forms", "de Rham cohomology"],
            parameters=[
                Parameter(id="P034", name="Dimension", parameter_type="kinematic",
                         value="4", alternatives=["2", "3", "10", "11"]),
                Parameter(id="P036", name="Metric signature", parameter_type="kinematic",
                         value="(-,+,+,+) Lorentzian", alternatives=["(+,+,+,+) Euclidean"]),
            ],
            temporal_note="Metric signature distinguishes time from space. No preferred direction yet.",
        ),
        Node(
            id="FB",
            structural_type="geometric_structure",
            label="Fiber bundles",
            description="Spaces locally product but globally twisted.",
            dependencies=[
                Dependency(on="MAN", dependency_type="logical", note="Bundles need a base manifold"),
                Dependency(on="GRP", dependency_type="logical", note="Principal bundles need a structure group"),
            ],
            provides=["Sections", "Bundle maps", "Associated bundles"],
            parameters=[],
        ),

        # ── GR-specific layers ──
        Node(
            id="METRIC",
            structural_type="geometric_structure",
            label="Riemannian/pseudo-Riemannian geometry",
            description="Metric tensor on manifolds. Defines distances and angles.",
            dependencies=[
                Dependency(on="MAN", dependency_type="logical",
                          note="Metric is a tensor field on a manifold"),
                Dependency(on="LA", dependency_type="logical",
                          note="Metric is a bilinear form on tangent spaces"),
            ],
            provides=["Induced topology", "Geodesics", "Volume form"],
            parameters=[
                Parameter(id="GR_P001", name="Metric signature", parameter_type="kinematic",
                         value="Lorentzian (-,+,+,+)", alternatives=["Euclidean", "split"]),
            ],
        ),
        Node(
            id="LEVI_CIVITA",
            structural_type="geometric_structure",
            label="Levi-Civita connection",
            description="Unique metric-compatible, torsion-free connection.",
            dependencies=[
                Dependency(on="METRIC", dependency_type="logical",
                          note="Defined by the metric uniquely"),
                Dependency(on="FB", dependency_type="logical",
                          note="Connection on the tangent bundle"),
                Dependency(on="LIEA", dependency_type="logical",
                          note="Connection valued in gl(n,R)"),
            ],
            provides=["Parallel transport", "Geodesic deviation"],
            parameters=[
                Parameter(id="GR_P002", name="Connection type", parameter_type="structural",
                         value="metric-compatible, torsion-free",
                         alternatives=["Einstein-Cartan (with torsion)"]),
            ],
        ),
        Node(
            id="RIEMANN",
            structural_type="geometric_structure",
            label="Riemann curvature",
            description="Curvature tensor measuring non-commutativity of covariant derivatives.",
            dependencies=[
                Dependency(on="LEVI_CIVITA", dependency_type="logical",
                          note="Curvature is defined from a connection"),
            ],
            provides=["Ricci tensor", "Scalar curvature", "Curvature forms"],
            parameters=[],
        ),
        Node(
            id="EINSTEIN_EQ",
            structural_type="dynamical_principle",
            label="Einstein field equations",
            description="Relate curvature to matter/energy via Ricci tensor and Einstein tensor.",
            dependencies=[
                Dependency(on="RIEMANN", dependency_type="logical",
                          note="EFE involve the Ricci tensor and scalar curvature"),
            ],
            provides=["Gravitational dynamics", "Solution space"],
            parameters=[
                Parameter(id="GR_P003", name="Cosmological constant", parameter_type="dynamical",
                         value="present (small positive)", alternatives=["absent", "negative"]),
                Parameter(id="GR_P004", name="Lambda value", parameter_type="dynamical",
                         value="~10^-52 m^-2", alternatives=["any real"]),
            ],
            temporal_note="EFE are time-symmetric (time-reversal invariant). Both retarded and advanced solutions exist.",
        ),
        Node(
            id="STRESS_ENERGY",
            structural_type="physical_theory",
            label="Stress-energy coupling",
            description="Matter couples to gravity via stress-energy tensor.",
            dependencies=[
                Dependency(on="EINSTEIN_EQ", dependency_type="logical",
                          note="RHS of Einstein equations"),
            ],
            provides=["Matter coupling", "Energy-momentum conservation"],
            parameters=[],
        ),
        Node(
            id="GR_CAUSALITY",
            structural_type="physical_theory",
            label="Causal structure & global topology",
            description="Global structure of spacetime: causality conditions, topology, boundary conditions.",
            dependencies=[
                Dependency(on="METRIC", dependency_type="logical",
                          note="Causal structure defined by the metric"),
                Dependency(on="STRESS_ENERGY", dependency_type="logical",
                          note="Matter content affects global structure"),
            ],
            provides=["Light cones", "Causality constraints", "Topological structure"],
            parameters=[
                Parameter(id="GR_P005", name="Global hyperbolicity", parameter_type="kinematic",
                         value="globally hyperbolic", alternatives=["not globally hyperbolic"]),
                Parameter(id="GR_P006", name="Time orientation", parameter_type="kinematic",
                         value="time-orientable", alternatives=["non-orientable"]),
            ],
            temporal_note="This is where GR acquires a preferred temporal direction via boundary conditions (analogous to iε in QFT).",
        ),
    ]

    for node in nodes:
        graph.add_node(node)

    graph.validate()
    return graph
