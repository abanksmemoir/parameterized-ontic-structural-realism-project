# POSR Operating Manual

**Parameterized Ontic Structural Realism**
Version 0.1.0 | April 2026

---

## Part I: What This Is

### The one-sentence version

Software that decomposes physical theories into dependency graphs where every structural presupposition is declared, every parametric choice is explicit, and every well-formed alternative has standing as a legitimate structure in the lattice.

### The problem it solves

Modern theoretical physics rests on a stack of mathematical dependencies that nobody has ever made fully explicit in one place. The Standard Model presupposes gauge theory, which presupposes connection theory and representation theory, which presuppose Lie algebras, which presuppose group theory and linear algebra, which presuppose set theory (or type theory), which presupposes a choice of logic. General Relativity shares most of that stack but forks at a specific, locatable point: the connection lives on the tangent bundle of spacetime rather than on an internal gauge bundle.

Every physics software package handles one or two layers of this stack. Lean and Coq handle logic and foundations. GAP handles group theory. LieART handles Lie algebra representations. FeynRules and SARAH handle gauge theory and Lagrangians. Lattice QCD codes handle simulation. None of them provide the connective tissue: the explicit mapping of what presupposes what, from axiom choice all the way up to particle content and coupling constants, with every dependency declared and every convention exposed.

This project provides that connective tissue.

### What we built (v0.1.0)

A Python API core that implements the structural dependency graph as a first-class object. The system has four components:

**1. A theory-agnostic graph schema.** A `Node` represents any structural concept (a logic, a set theory, a group, a manifold, a gauge theory, a particle). Each node declares what it presupposes (which other nodes must be present below it), what it provides (what capabilities it makes available to nodes above it), and what is parametric (which choices are swappable without breaking the interface). The schema is not specific to the Standard Model or any other theory. It works for any physical theory that can be decomposed into structural dependencies.

**2. Two populated theory-graphs.** The Standard Model graph has 30 nodes across 10 layers, from classical logic at the bottom to Yukawa couplings and flavor mixing at the top. The General Relativity graph has 18 nodes, sharing 12 foundational nodes with the Standard Model and forking at the connection/curvature layer where SM goes to internal gauge bundles and GR goes to the tangent bundle.

**3. A theory-file system.** The unit of output is a "theory-file" — a self-contained JSON document recording a complete, well-formed physical theory as the totality of its parametric choices. Each theory-file gets a human-readable slug (for navigation) plus a cryptographic fingerprint (for machine deduplication). The system produces a flat directory of theory-files, each one a distinct path through the parametric lattice.

**4. Cross-theory structural comparison.** Given two theory-graphs, the system identifies the shared subgraph, the fork points, and the theory-specific branches. This is the project's main analytical instrument. The claim that SM and GR "reduplicate" connection/curvature machinery on different bundles — and that unification proposals amount to collapsing that reduplication into shared ancestry — is a claim this operation makes precise and testable.

---

## Part II: The Philosophical Frame

### Position in the literature

This project executes a program that three lines of published work in philosophy of physics have argued for but never carried out.

Kerry McKenzie asked whether being a quark just *is* occupying a slot in the fundamental representation of SU(3). She is the most granular philosopher working on ontic structural realism (OSR) and the Standard Model specifically. Her limitation: she worries that coupling constants, mixing angles, and the mass hierarchy resist purely structural explanation — that group theory underdetermines the ontology. This project's framework dissolves that worry rather than answering it.

Steven French's *The Structure of the World* (2014) is the most comprehensive published attempt at full OSR metaphysics engaging the Standard Model. He draws on permutation invariance and gauge symmetry but stays at the level of general arguments rather than producing the actual structural mapping.

Ladyman and Ross's *Every Thing Must Go* (2007) set the programmatic agenda for OSR but operates at the level of quantum mechanics in general rather than the specific architecture of the Standard Model.

What none of them produced: a formal object that says, here is the Standard Model as a purely structural ontology, here is exactly what "electron" means in that ontology, here is what makes three generations three rather than four, here is the structural content of CP violation. That is what this project builds.

### How this project's realism differs from standard OSR

The philosophical stance is not standard ontic structural realism as found in French, Ladyman, or McKenzie. It departs in specific ways that are load-bearing for the architecture:

**Genuine realism.** "Real" in the ontic sense is whatever concatenation of parameterized, well-formed primitives bears an identity relationship to the world we live in. This is not a deflationary or epistemic claim. There is a definite structure, and science is in the business of honing in on a formal recapitulation of it. The Standard Model theory-file is distinguished in the lattice because it is the one whose parametric choices match actuality — not because it is the only well-formed structure, but because it is the one that bears the identity relationship to the world.

**No brute contingency.** Standard OSR philosophers worry that the Standard Model's specific parameters (coupling constants, mixing angles, generation count) are "non-structural contingencies" that resist structural explanation. This project's response: that worry smuggles in a non-structural substrate that "selects" which structures get instantiated, which is exactly what OSR is supposed to eliminate. The actual world is a structural configuration, full stop. "Why this structure?" either bottoms out in further structure or the question is malformed. The software treats these parameters as structural coordinates, not brute contingencies.

**Instrumental Platonism.** The lattice of well-formed hypotheticals is animated by a covert methodological Platonism — all consistent structures have standing. But this Platonism is instrumental: a navigational medium, not an ontological commitment to the existence of every structure in the lattice. The Platonism provides the space within which you converge on the ontic target. It does not collapse the ontology into any particular corner.

**No side-picking on modality.** The project does not choose between Tegmark's mathematical universe hypothesis (all consistent structures exist) and structural necessitarianism (only one self-consistent totality). That choice is downstream from axiom selection, which is itself parametric. The lattice does not have a top node. The software is neutral on this question by design.

**"Geometry" is already structure.** To say something "is geometry" is underdetermined — there are many geometries downstream from different axiom sets. To BE geometry is to be a kind of structure downstream from a choice of axioms. This dissolves the Calabi-Yau selection problem: the topology is part of the total structural fact, not something chosen from a landscape by an external principle. The software makes this concrete by representing geometric structures as nodes with parametric slots, not as privileged primitives.

### Why this matters for the software's architecture

These are not philosophical decorations. They are the constraints that shaped every design decision:

The system cannot hardcode any mathematical convention as if it were structurally primitive. Everything — including classical logic, ZFC set theory, the real number field — is a parametric choice at a specific node. The system must be able to receive a different logic, a different foundation, and propagate the consequences.

The system cannot treat the Standard Model's specific content as arbitrary, nor as uniquely necessary. It is the distinguished point in a parametric space. The system must model both the point and the surrounding space.

The system cannot assume a single foundational framework as privileged. Foundations are a parameter. The v0.1 graph includes both ZFC and type theory as alternative Layer 1 choices; the consequences of choosing one over the other propagate upward through the entire graph.

---

## Part III: How It Works

### The dependency graph

The graph is a directed acyclic graph (DAG). Edges point from presuppositions to dependents: classical logic is presupposed by first-order logic, which is presupposed by ZFC, which is presupposed by group theory, and so on up to the Standard Model.

The current Standard Model graph has 30 nodes across 10 layers:

| Layer | Name | Nodes | What it contributes |
|-------|------|-------|-------------------|
| 0 | Logic | CL, IL, FOL | Deductive system, quantification |
| 1 | Foundations | ZFC, TT, CAT | Set theory or type theory, categories |
| 2 | Core Algebra | GRP, RING, LA | Groups, rings, fields, vector spaces |
| 3 | Topology and Analysis | TOP, REAL, CMPLX | Continuity, measure, analytic functions |
| 4 | Lie Theory | LIE, LIEA, REP | Continuous symmetry, infinitesimal structure, representations |
| 5 | Differential Geometry | MAN, FB, CONN | Manifolds, bundles, connections |
| 6 | Functional Analysis | HILB, OA, PATH | Hilbert spaces, operator algebras, path integral |
| 7 | Classical Field Theory | LAG, GAUGE | Lagrangian dynamics, gauge theory |
| 8 | Quantum Field Theory | QFT, RENORM, ANOM | Quantized fields, renormalization, anomaly cancellation |
| 9 | Standard Model | SM_G, SM_F, SM_H, SM_Y | Gauge group, fermion content, Higgs, Yukawa |

The deepest dependency chain runs 12 links: CL to FOL to ZFC to GRP to LIE to LIEA to REP to CONN to GAUGE to QFT to ANOM to SM_F. Every link is a point where a different parametric choice would produce a different theory.

The most structurally constrained node is ANOM (anomaly cancellation). It takes representation theory and topology as input and outputs hard constraints on which particle content is even consistent. The Standard Model's specific fermion content is not arbitrary — it is one of a small number of anomaly-free configurations. This is the structural realist's strongest card.

### Nodes and parametric slots

Each node has three interfaces:

**Presupposes** — the nodes that must be present below it. ZFC presupposes classical logic and first-order logic. The Lie algebras node presupposes Lie groups and linear algebra. Anomaly cancellation presupposes QFT, representation theory, and connections. These are hard dependencies: remove a presupposed node and the dependent node is structurally unsupported.

**Provides** — what this node makes available to nodes above it. Group theory provides subgroups, quotient groups, homomorphisms, and group actions. Connections provide covariant derivatives, holonomy, and characteristic classes. These are the capabilities that higher nodes can presuppose.

**Parametric slots** — the choices that can be made at this node. Each slot has a name, a description, a type (architectural or runtime), known options (if enumerable), and optionally a default value. Architectural parameters change the graph structure (dropping the law of excluded middle removes access to proof by contradiction throughout the entire graph). Runtime parameters change values within a fixed structure (the strong coupling constant g3 = 1.221 could be different without altering which nodes are present).

### Two kinds of parametric choice

**Architectural choices** alter what is structurally available downstream. Dropping the axiom of choice from ZFC changes which theorems are provable in every node above. Choosing intuitionistic logic instead of classical logic removes proof by contradiction from the entire graph. Choosing SU(5) instead of SU(3)xSU(2)xU(1) changes the gauge boson content and the anomaly constraints. These are swap-at-build-time decisions that produce a structurally different theory.

**Runtime choices** alter numerical values within a fixed structure. The strong coupling constant, the Weinberg angle, the Higgs vacuum expectation value. The nodes and their dependencies remain the same; the quantitative content changes. These are adjust-at-runtime decisions within an already-built theory.

The distinction matters because architectural choices can propagate: changing the logic at Layer 0 may invalidate nodes at Layer 8. Runtime choices do not propagate structurally — they change output values but not the graph topology.

### Theory-files

A theory-file is a saved, resolved theory-graph: all parametric choices have been made, every slot has a value, and the result is serialized as a self-contained JSON document. The theory-file is the project's primary artifact.

Each theory-file has:

A **metadata header** with the theory's name, description, version, creation date, and provenance (which theory it was forked from, if any).

A **choices section** recording every parametric decision: which logic, which foundation, which gauge group, which coupling constants, which propagator convention.

A **full node graph** with all 30 (or 18, for GR) nodes, their dependencies, their provisions, and their resolved parametric values.

A **provenance record** listing every fork point: which node, what was chosen, and what alternatives were available.

A **fingerprint** — the first 8 hex characters of a SHA256 hash computed over all resolved parametric values in topological order. Two theory-files with the same fingerprint are structurally identical.

A **human-readable slug** derived from the major structural choices: theory family, logic, foundation, gauge group, generation count. The slug is for human navigation; the fingerprint is for machine deduplication.

The **filename** combines both: `SM-CL_ZFC_SU321-3gen-b7a2f3c1.json`. Short enough for NotebookLM to use as a source title. Informative enough to identify at a glance.

### Cross-theory comparison

Given two theory-graphs, the system computes:

**Shared subgraph** — the nodes present in both theories with compatible presupposes relations. For SM and GR, this is 12 nodes: everything from classical logic through smooth manifolds and fiber bundles.

**Theory-specific branches** — nodes present in only one theory. SM has 18 specific nodes (gauge theory through Yukawa mixing). GR has 6 specific nodes (metric through stress-energy coupling).

**Fork points** — nodes present in both theories where parametric choices differ. The critical fork point for SM vs GR is at the connection/curvature level: SM instantiates connections on internal gauge bundles (structure group SU(3)xSU(2)xU(1)); GR instantiates connections on the tangent bundle (structure group Lorentz group or GL(4,R)).

**Fork depth** — how deep in the graph the fork occurs. A shallow fork means the theories diverge early and share little structure. A deep fork means they share a lot. SM and GR share structure through 12 nodes before forking — a substantial shared foundation.

The fork point is precisely where unification theories live. Any unification scheme amounts to a proposal for a shared parent node at or below the fork — a structure from which both the internal gauge bundle and the tangent bundle descend as special cases. Kaluza-Klein does this by embedding the gauge fiber in extra spatial dimensions. String theory does it differently. The graph makes these proposals structurally comparable.

### The SM/GR composite as reduplication

The current situation in physics is not a clean fork. It is a reduplication. Both the Standard Model and General Relativity instantiate the same formal concepts — connections, curvature, gauge-like symmetry — but on different bundles, at different nodes. Working physicists carry both theories around and context-switch between them depending on whether the task is particle physics or cosmology. The graph makes this reduplication precise and visible: *this* connection in the SM branch and *that* connection in the GR branch are both downstream instantiations of the same parent concept, parameterized differently. Unification would resolve this by collapsing the reduplication back into a single ancestry.

### The Wheeler-Feynman time symmetry constraint

Most physics software bakes the arrow of time into the propagator choice — retarded Green's function by default. This means the time asymmetry is an undeclared parametric commitment hiding inside the QFT node: it enters silently, at the wrong structural level, as a computational convenience.

The Wheeler-Feynman absorber theory establishes that the fundamental electrodynamics is time-symmetric. The observed arrow of time emerges from a cosmological boundary condition, not from the dynamics. The time asymmetry is a boundary condition fact, not a dynamical law fact.

The graph handles this by making the propagator choice (retarded, advanced, Wheeler-Feynman half-retarded/half-advanced, or symmetric) a declared parametric slot at the QFT node. No default is smuggled in. The time-asymmetric convention is exposed as a choice that can be toggled, with consequences that propagate through both SM and GR branches.

This matters for the cross-theory comparison: some apparent structural differences between SM and GR may dissolve when the time-asymmetric convention is made parametric and stripped out. The fork point between the two theories may be shallower than it appears in conventional formulations. The graph is designed to be able to show this.

### Fork discipline and the lattice

All well-formed structures exist in the lattice. A theory parameterized with SU(5) and a theory parameterized with SU(3)xSU(2)xU(1) are both legitimate — they share everything below the gauge group node and diverge above it. One matches the data; the other does not. But they are segregated graphs, not rival answers within a single graph.

The system enforces fork discipline: different parametric choices produce different theory-files that share a subgraph up to the fork point. They do not compete within a single structure. The distinguished point (the actual world's structure) is a specific path through the lattice. Other paths are real as structures but do not bear the identity relationship to the actual world.

This discipline prevents the system from treating different parameterizations as if they occupy the same graph and need to be adjudicated. They do not. Each fork is its own theory. Adjudication happens empirically, outside the graph — the graph provides the structural space within which empirical comparison is meaningful.

---

## Part IV: The Software

### Repository structure

```
posr/
  __init__.py              API entry point, version
  schema.py                Core data types: Node, ParametricSlot,
                           TheoryGraph, TheoryFile, ForkPoint
  graph.py                 Graph operations: build, traverse, validate,
                           resolve choices, propagate changes
  diff.py                  Cross-theory comparison: shared subgraph,
                           fork points, structural diff
  registry.py              Registry of known node types and parametric options
  templates/
    __init__.py
    sm.py                  Standard Model template (30 nodes, 10 layers)
    gr.py                  General Relativity template (18 nodes)

tests/
  test_schema.py           11 tests: Node, ParametricSlot, TheoryGraph, TheoryFile
  test_graph.py            7 tests: building, resolving, validation, comparison
  test_diff.py             7 tests: structural diff, shared subgraph, fork path
  test_templates.py        9 tests: SM, GR, SM vs GR comparison

sm_dependency_graph.json   Original machine-readable graph (v0.1 format)
sm_dependency_graph.md     Annotated human-readable reference
PROJECT_BRIEFING.md        Governing project document
SUPPLEMENTARY_BRIEFING.md  Design constraints and prior art
IMPLEMENTATION_NOTES.md    Technical notes and design decisions
demo.py                    Full system demonstration
pyproject.toml             Package configuration
```

### Installation

```bash
git clone https://github.com/abanksmemoir/parameterized-ontic-structural-realism-project.git
cd parameterized-ontic-structural-realism-project
pip install -e .
```

### Running the tests

```bash
python -m pytest tests/ -v
```

All 40 tests pass. They verify graph construction, topological sorting, ancestor/descendant queries, dependency chain finding, parametric choice resolution, theory-file serialization round-trips, SM and GR template loading, and cross-theory comparison.

### Running the demo

```bash
python demo.py
```

Demonstrates: SM graph loading, GR graph loading, parametric choice resolution, theory-file generation, and SM-vs-GR structural diff with shared subgraph identification.

### Core API usage

Building a theory-graph from a template:

```python
from posr.templates import sm, gr

sm_graph = sm.build()    # 30 nodes
gr_graph = gr.build()    # 18 nodes
```

Making parametric choices and saving a theory-file:

```python
from posr.graph import resolve_parametric_choices

choices = {
    "CL":   {"LEM": "true", "explosion": "true"},
    "ZFC":  {"axiom_of_choice": "true", "foundation": "true"},
    "SM_G": {"gauge_group": "SU(3)xSU(2)xU(1)", "g3": "1.221", "g2": "0.652", "g1": "0.357"},
    "SM_F": {"num_generations": "3"},
    "QFT":  {"time_asymmetry": "retarded", "regularization": "dimensional"},
}

theory_file = resolve_parametric_choices(sm_graph, choices)
saved_path = theory_file.save("/path/to/theory-files/")
```

Comparing two theories:

```python
from posr.diff import compute_structural_diff

diff = compute_structural_diff(sm_graph, gr_graph)
print(diff.summary())
# Shared structure: 12 nodes
# SM-only: 18 nodes
# GR-only: 6 nodes
```

Querying the graph:

```python
# Topological sort (dependencies before dependents)
order = sm_graph.topological_sort()

# Everything that SM_G depends on (transitively)
ancestors = sm_graph.ancestors("SM_G")

# Everything that depends on ZFC (transitively)
descendants = sm_graph.descendants("ZFC")

# Path from classical logic to the Standard Model gauge group
chain = sm_graph.dependency_chain("CL", "SM_G")
```

Extracting a shared subgraph:

```python
shared = sm_graph.shared_subgraph(gr_graph)
# 12 nodes: CL, FOL, ZFC, GRP, RING, LA, TOP, REAL, LIE, LIEA, MAN, FB
```

---

## Part V: What Comes Next

### Immediate priorities

**Smarter slug generation.** The current `_generate_slug()` concatenates resolved values naively. It needs to pull theory family from terminal nodes, logic from Layer 0, foundation from Layer 1, gauge group from the gauge layer (abbreviated), and generation count — while ignoring runtime parameters that do not belong in the filename.

**Time symmetry as a separate node.** Currently time-asymmetry is a parametric slot on the QFT node. Per the project's design constraints, it should be elevated to a separate node sitting above both SM and GR branches so toggling it propagates through both simultaneously.

### Medium-term

**Parametric propagation.** When a choice at a lower node is toggled, automatically flag all downstream nodes as stale and, where tool bindings exist, trigger recomputation. This is the "functorial composition" requirement: swap the logic at the bottom, and the consequences should ripple upward through the entire graph without silently absorbing the change.

**Wrapping external tools.** GAP for group theory, LieART for Lie algebra representations, FeynRules for Lagrangian derivation, SARAH for RGE running and anomaly conditions. Each wrapped with the project's parametric interface so a node can invoke computation when its inputs change.

**Anomaly computation.** Actual algebraic verification of anomaly cancellation at the ANOM node — the most structurally constrained node in the graph and the strongest card in the structural realist's hand.

**More theory-graphs.** QED alone. The electroweak theory alone. LCDM cosmology. Each as its own template and set of theory-files, expressible in the same schema and comparable via the same diff operations.

### Long-term

**Unification testing.** Given a proposed unification theory-file (Kaluza-Klein, a GUT, string-derived models), verify that SM and GR are both derivable as parametric specializations of it. This is the graph-level formulation of "does this unification proposal actually work?"

**Lattice navigation.** Given a collection of theory-files, compute the full lattice structure: which theories are parametric neighbors, which share the most upstream structure, which differ by a single architectural choice. This is the navigational medium the instrumental Platonism provides.

---

## Part VI: Governing Principles

These are the constraints under which all implementation decisions are made. They are not negotiable and they are not aspirational — they are the requirements that shaped what we built and will shape everything we build next.

**Segregation of Python logic from graph logic.** The graph is the ontological object. Python is the construction tool. The two are cleanly separated: Python builds, traverses, and manipulates the graph, but the graph's structural content does not inherit Python's implicit commitments (classical logic, ZFC-ish set theory, sequential evaluation). If the same graph were rebuilt in Haskell or Lean, the graph should be identical. Python is the interpreter, not the language.

**Constructor injection, no ambient reach.** Every layer receives its entire structural substrate as constructor arguments. The logic layer hands the algebra layer its permitted inference rules. The algebra layer hands the gauge theory layer its group-theoretic toolkit. Nothing reaches around its interface to grab something from a layer it should not know about.

**Functorial composition.** Each layer is a functor: axioms in, structural consequences out. Composition is explicit. Swap the logic at the bottom and the consequences should propagate upward. The gauge theory layer should ripple when the logic changes, not silently absorb the change into hardcoded assumptions.

**Docility.** Each layer is a black box only in the sense that it has a clean interface. It cannot smuggle in commitments that are not declared in its parameters. No ambient assumptions, no hidden imports from mathematical context that are not explicitly wired in.

**Fork discipline.** Different parametric choices produce different theory-graphs. They share upstream structure but are distinct entities, not variants jostling within a single structure. Fork provenance is recorded explicitly at every node where a parametric choice creates a branch.

**Cross-theory generality from day one.** The schema accommodates any physical theory, not just the Standard Model. GR, QED, LCDM, GUTs, string-derived models — all expressible in the same vocabulary, all comparable via the same diff operations. This generality is not optional and was not retrofitted; it was a design requirement from the first line of code.
