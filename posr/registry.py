"""
Registry of known node types, parameter subtypes, and their options (V2).

V2 changes:
  - Parameter subtypes replace the old architectural/runtime distinction
  - Dependency types are registered
  - Node templates use V2 Parameter and Dependency types
"""

from typing import Dict, List, Optional
from .schema import Node, Parameter, Dependency, PARAMETER_SUBTYPES, DEPENDENCY_TYPES


# ──────────────────────────────────────────────────────────────
# Standard structural type categories
# ──────────────────────────────────────────────────────────────

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


# ──────────────────────────────────────────────────────────────
# Parameter subtype descriptions (from V2 ontology)
# ──────────────────────────────────────────────────────────────

PARAMETER_SUBTYPE_DESCRIPTIONS = {
    "axiom": "Foundational choice with no prior constraints within the framework",
    "structural": "Choice of mathematical/physical structure; options constrained by upstream",
    "kinematic": "Choice about the arena (dimension, signature, topology)",
    "dynamical": "Choice about equations of motion or interaction rules",
    "boundary": "Choice about initial/final conditions or propagator prescription; independent of dynamics",
    "convention": "Choice affecting description but not physics",
}


# ──────────────────────────────────────────────────────────────
# Dependency type descriptions (from V2 ontology)
# ──────────────────────────────────────────────────────────────

DEPENDENCY_TYPE_DESCRIPTIONS = {
    "logical": "Y cannot be formulated without X",
    "conventional": "Y is standardly built on X but alternatives exist (disguised parameter)",
    "contingent": "Y uses X's output only under conditions X does not guarantee",
}


# ──────────────────────────────────────────────────────────────
# Known parametric options for common structural concepts
# ──────────────────────────────────────────────────────────────

PARAMETRIC_OPTIONS = {
    "logic_choice": {
        "options": ["classical", "intuitionistic", "paraconsistent", "linear"],
        "default": "classical",
        "parameter_type": "axiom",
    },
    "foundation_choice": {
        "options": ["ZFC", "ZF", "type_theory", "category_theory"],
        "default": "ZFC",
        "parameter_type": "axiom",
    },
    "gauge_group": {
        "options": ["SU(3)xSU(2)xU(1)", "SU(5)", "SO(10)", "E(6)", "E(8)"],
        "default": "SU(3)xSU(2)xU(1)",
        "parameter_type": "structural",
    },
    "num_generations": {
        "options": ["1", "2", "3", "4"],
        "default": "3",
        "parameter_type": "structural",
    },
    "iepsilon_sign": {
        "options": ["+iε", "-iε"],
        "default": "+iε",
        "parameter_type": "boundary",
    },
    "vacuum_state": {
        "options": ["Poincare-invariant", "Bunch-Davies", "thermal", "squeezed"],
        "default": "Poincare-invariant",
        "parameter_type": "boundary",
    },
    "metric_signature": {
        "options": ["(-,+,+,+)", "(+,-,-,-)", "(+,+,+,+)"],
        "default": "(-,+,+,+)",
        "parameter_type": "kinematic",
    },
    "wick_rotation": {
        "options": ["t -> -i*tau", "no rotation (Lorentzian)"],
        "default": "t -> -i*tau",
        "parameter_type": "boundary",
    },
    "renormalization_scheme": {
        "options": ["MS-bar", "on-shell", "MOM"],
        "default": "MS-bar",
        "parameter_type": "convention",
    },
    "gauge_fixing": {
        "options": ["Lorenz", "Coulomb", "axial", "light-cone"],
        "default": "Lorenz",
        "parameter_type": "convention",
    },
}


def node_template(node_id: str) -> Optional[Node]:
    """Retrieve a pre-configured node template by ID (V2 types).

    Returns None if the template is not registered.
    """
    templates = {
        "CL": Node(
            id="CL",
            structural_type="logic",
            label="Classical logic",
            description="Law of excluded middle, double negation elimination, material conditional.",
            dependencies=[],
            provides=["Proof by contradiction", "De Morgan duality", "Boolean algebra"],
            parameters=[
                Parameter(
                    id="P001", name="Law of excluded middle",
                    parameter_type="axiom",
                    value="on", alternatives=["off (intuitionistic)"],
                ),
                Parameter(
                    id="P002", name="Explosion principle",
                    parameter_type="axiom",
                    value="on", alternatives=["off (paraconsistent)"],
                ),
            ],
        ),
        "FOL": Node(
            id="FOL",
            structural_type="logic",
            label="First-order quantification",
            description="Universal and existential quantification over individuals.",
            dependencies=[
                Dependency(on="CL", dependency_type="conventional",
                          note="FOL can be built on IL"),
            ],
            provides=["Quantified statements", "Model theory"],
            parameters=[
                Parameter(
                    id="P003", name="Underlying logic",
                    parameter_type="axiom",
                    value="classical (CL)", alternatives=["intuitionistic (IL)"],
                ),
                Parameter(
                    id="P004", name="Sort structure",
                    parameter_type="structural",
                    value="single-sorted", alternatives=["many-sorted"],
                ),
            ],
        ),
        "ZFC": Node(
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
            provides=["Infinite sets", "Powersets", "Well-ordering", "Cartesian products"],
            parameters=[
                Parameter(
                    id="P006", name="Axiom of choice",
                    parameter_type="axiom",
                    value="included", alternatives=["excluded (ZF)"],
                ),
                Parameter(
                    id="P007", name="Continuum hypothesis",
                    parameter_type="axiom",
                    value="independent", alternatives=["assumed", "denied"],
                ),
                Parameter(
                    id="P008", name="Foundation axiom",
                    parameter_type="axiom",
                    value="included", alternatives=["excluded"],
                ),
            ],
        ),
        "QFT": Node(
            id="QFT",
            structural_type="quantization",
            label="Field quantization",
            description="Promote fields to operator-valued distributions.",
            dependencies=[
                Dependency(on="GAUGE", dependency_type="conventional",
                          note="QFT can exist without gauge theory"),
                Dependency(on="HILB", dependency_type="logical",
                          note="State space"),
                Dependency(on="PATH", dependency_type="conventional",
                          note="Canonical quantization is an alternative"),
            ],
            provides=["Feynman diagrams", "S-matrix", "Vacuum state", "Propagators",
                      "CPT theorem", "Spin-statistics theorem"],
            parameters=[
                Parameter(
                    id="P057", name="iε sign",
                    parameter_type="boundary",
                    value="+iε", alternatives=["-iε"],
                    note="Most consequential hidden parameter. Determines causal structure.",
                ),
                Parameter(
                    id="P078", name="Vacuum state",
                    parameter_type="boundary",
                    value="Poincare-invariant |Omega>",
                    alternatives=["Bunch-Davies", "thermal", "squeezed"],
                    note="Practice assumes this value. No derivation of why.",
                ),
            ],
            temporal_note="THIS IS WHERE TIME ACQUIRES A PREFERRED DIRECTION via iε.",
            contingent_provisions=[
                "Causal propagator structure depends on iε boundary parameter (P057).",
                "Vacuum state uniqueness depends on iε prescription.",
            ],
        ),
    }

    return templates.get(node_id)


def get_parametric_options(parameter_name: str) -> Dict[str, any]:
    """Get known options for a parametric slot by name."""
    return PARAMETRIC_OPTIONS.get(parameter_name, {})
