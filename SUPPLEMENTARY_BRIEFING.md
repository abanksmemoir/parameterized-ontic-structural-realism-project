# Supplementary Briefing: Context, Tooling, and Design Constraints

This document supplements `PROJECT_BRIEFING.md` with material the agent needs to make good decisions. Read the briefing first; this fills in the gaps.

---

## 1. Prior Art and Why It's Insufficient

Three lines of published work are relevant. All three argue for the program this project executes. None of them execute it.

**Kerry McKenzie** — the most granular philosopher on OSR and the Standard Model specifically. Her contribution: asking whether being a quark just *is* occupying a slot in the fundamental representation of SU(3). Her limitation: she worries that group theory underdetermines the ontology — that coupling constants, mixing angles, and the mass hierarchy resist purely structural explanation. This worry is symptomatic of the mistake the briefing identifies: smuggling in a non-structural substrate that "selects" which structures get instantiated. The project's framework dissolves her objection rather than answering it.

**Steven French** — *The Structure of the World* (2014). Most comprehensive published attempt at full OSR metaphysics engaging the Standard Model. Draws on permutation invariance (quantum particles lack transcendental individuality, so structure does all the ontological work) and extends into gauge symmetry. Limitation: stays at the level of general arguments rather than producing the actual structural mapping.

**Ladyman and Ross** — *Every Thing Must Go* (2007). Set the programmatic agenda for OSR. Limitation: operates at the level of quantum mechanics in general rather than the specific architecture of the SM.

**What none of them did:** Produce a document or formal object that says: here is the Standard Model as a purely structural ontology, here is exactly what "electron" means in that ontology, here is what makes three generations three rather than four, here is the structural content of CP violation. That is this project.

**What none of them engaged with:** What happens when the gauge structure itself is geometrized à la Kaluza-Klein. If SU(3)×SU(2)×U(1) is fiber bundle geometry over a base manifold, then the "ontic structure" isn't abstract algebra — it's literal geometric topology. That's a stronger structural realism than any of the above contemplate.

---

## 2. Existing Tooling Inventory

The project doesn't build from scratch. Existing tools handle individual layers. The novel contribution is the connective tissue — the dependency graph that links them with explicit parametric interfaces.

**Logic/foundations layer:**
- Lean 4 + mathlib: enormous coverage of algebra, topology, group theory with explicit axiom dependencies. You can inspect which axioms any theorem depends on.
- Coq, Isabelle: alternative proof assistants with different foundational commitments (useful for the cross-medium diffing the project envisions).

**Algebra/group theory layer:**
- GAP: computational group theory — can enumerate group structures algorithmically.
- LieART: Lie algebra representations — can compute representation content, branching rules, tensor products.

**Gauge theory / physics layer:**
- FeynRules: define a Lagrangian by specifying gauge group and particle content, derive Feynman rules automatically.
- SARAH: similar to FeynRules but also derives RGE running and anomaly conditions.
- MILC collaboration codes: open-source lattice gauge theory, parameterizes gauge group, representation content, coupling constants.

The agent should survey these before writing any code. The first implementation task is determining which of these can be wrapped with the project's parametric interface pattern and which need to be reimplemented.

---

## 3. Key Structural Insights That Guide Implementation

**The twelve-link dependency chain.** The deepest path through the SM dependency graph runs:

classical logic → first-order logic → ZFC → groups → Lie groups → Lie algebras → representations → connections → gauge theory → QFT → anomaly cancellation → Standard Model fermion content

Every link is a point where a different parametric choice propagates upward. This chain is the implementation spine.

**Anomaly cancellation is the most structurally constrained node.** It takes representation theory and topology as input and outputs hard constraints on which particle content is even consistent. This node does the most work for the structural realist's case, because it shows the SM's specific content isn't arbitrary — it's one of a small number of anomaly-free configurations. Invest implementation effort here early.

**The "fattest" parametric nodes are at the SM layer.** Why 3 generations? Why these coupling constants? Why SU(3)×SU(2)×U(1) and not SU(5)? These look like brute contingency from a conventional perspective. The project's framework reframes them as structural coordinates — the system explores only the region of the lattice that is inferentially productive given the data.

---

## 4. Primary Design Constraint: Cross-Theory Comparison

**The first target application is comparing the structural graph of the Standard Model to General Relativity.**

This means the graph schema cannot be SM-specific. It must be general enough that GR's structural dependencies express in the same vocabulary. The comparison then becomes a graph operation.

**GR's dependency structure includes (non-exhaustively):**
- Differentiable manifold structure
- Metric tensor / pseudo-Riemannian geometry
- Diffeomorphism invariance (the gauge symmetry of GR)
- Equivalence principle (multiple formulations with different structural content)
- Levi-Civita connection / spin connection
- Curvature (Riemann tensor and its contractions)
- Einstein field equations
- Stress-energy coupling
- Topological considerations (global structure, causality conditions)

**Where SM and GR share structure:** Both depend on differential geometry and fiber bundles up to a specific depth. They share: manifold structure, connection theory, curvature, fiber bundle architecture.

**Where they fork:** SM uses the connection on an *internal* fiber bundle (gauge fields — the structure group is SU(3)×SU(2)×U(1), the fiber is not spacetime). GR uses the connection on the *tangent bundle* (the fiber is spacetime's own tangent space, structure group is the Lorentz group or GL(4,R)).

**The fork point is precise and locatable in the graph.** This is the node where unification theories live. Any unification scheme amounts to a proposal for a shared parent node at or below the fork — a structure from which both the internal gauge bundle and the tangent bundle descend as special cases. Kaluza-Klein does this by embedding the gauge fiber in extra spatial dimensions. String theory does it differently. The graph makes these proposals structurally comparable.

**What this means for the schema:**
- Nodes must be typed generally enough to accommodate both gauge field theory and gravitational geometry.
- The "presupposes" relation must be able to express shared ancestry (both SM and GR presuppose connection theory, but they instantiate it differently).
- The parametric interface at each node must include a slot for *which bundle* the connection lives on — this is the structural variable that distinguishes SM from GR.
- The graph must support overlay/diff operations: given two theory-graphs over the same schema, identify shared subgraph, fork points, and theory-specific branches.

**Design the schema for this from day one.** Do not build an SM-specific graph and retrofit it for GR later. The comparison is the application; the generality is not optional.

**The SM+GR composite is not a clean fork — it is a reduplication.** Both branches instantiate the same formal concepts — connections, curvature, gauge-like symmetry — but on different bundles, at different nodes. The working physicist carries both around and context-switches between them depending on whether the task at hand is particle physics or cosmology. The graph's job is to make this reduplication precise and visible: *this* connection in the SM branch and *that* connection in the GR branch are both downstream instantiations of the same parent concept, parameterized differently. The current two-branch composite is not a well-formed single structure — it duplicates machinery for the same phenomena, and practitioners project whichever branch they need onto the world at any given moment. This is the structural diagnosis of why the present situation is confused, and it is what unification would actually resolve: collapsing the reduplication back into a single ancestry.

---

## 5. Lattice Ontology and Fork Discipline

**All well-formed structures exist in the lattice.** The graph schema represents a space in which every consistent parameterization has standing — including ones that seem ad hoc or arbitrary from a physical perspective. An alternative gauge group, an extra generation of fermions, a different compactification — these are all well-formed graphs. They get their due as legitimate structures. The lattice does not editorialize about which structures are "natural."

**But structures that share upstream ancestry must be clearly represented as forks, not competitors.** When two graphs share logically prior structure — the same foundational axioms, the same group theory, the same connection formalism — and then parameterize differently at some node, the schema must represent this as a fork from a common ancestor. The two branches coexist as distinct well-formed structures that happen to share a subgraph. They do not mutually compete. A structure parameterized with SU(5) and a structure parameterized with SU(3)×SU(2)×U(1) are both legitimate forks from the same parent node in the representation/gauge layer — one matches the data, the other doesn't, but they are segregated graphs, not rival answers jostling within a single graph.

**Why this matters:** Without this discipline, the agent may inadvertently treat different parameterizations as if they occupy the same graph and need to be adjudicated against each other. They don't. Each fork is its own graph. The distinguished point (the actual world's structure) is a specific path through the lattice. Other paths are real as structures but do not bear the identity relationship to the actual world. The graph schema must make fork provenance explicit at every node where a parametric choice creates a branch.

---

## 6. Time Symmetry Constraint (Wheeler-Feynman)

**The graph must handle time in a non-arbitrary way.**

The Wheeler-Feynman absorber theory establishes that the fundamental electrodynamics is time-symmetric — both retarded and advanced solutions are real. The observed arrow of time is not a property of the dynamics. It emerges from the absorber condition: a cosmological boundary condition (sufficient future absorbers) that selects the retarded-dominated solution we observe. The time asymmetry is a *boundary condition fact*, not a *dynamical law fact*.

**The problem with conventional implementations:** Most physics software bakes the arrow of time into the propagator choice — retarded Green's function by default. This means the time asymmetry is an undeclared parametric commitment hiding inside the QFT node. It enters silently, at the wrong structural level, as a computational convenience.

**What the graph must do instead:**
- The QFT node must be time-symmetric in its base formulation.
- The time asymmetry must enter at a separate, explicit node that declares its dependency on cosmological/absorber boundary structure.
- The propagator choice (retarded, advanced, or Wheeler-Feynman half-retarded/half-advanced) must be a declared parameter, not a hardcoded default.

**Critical downstream consequence for GR:** The time-asymmetric convention doesn't just affect the SM branch. It propagates into GR's branch as well, imparting rigidity that looks structural but is actually inherited from the conventional choice. Specifically: GR's causal structure, the distinction between past and future light cones, global hyperbolicity conditions, and the framing of the Cauchy initial value problem all carry assumptions about time directionality. Some of this may be genuine structural content of the geometry. Some of it may be rigidity imported from the same undeclared time-asymmetric convention that infects the SM's propagator.

**The graph must be able to distinguish these.** The time-symmetry/asymmetry node must sit at the correct depth — above both SM and GR — so that toggling it propagates changes through both branches simultaneously. This is how the project reveals which features of each theory are genuinely structural and which are artifacts of a shared smuggled assumption.

**Implication for the cross-theory comparison:** Some apparent structural differences between SM and GR may dissolve when the time-asymmetric convention is made parametric and stripped out. The fork point between the two theories may be shallower than it appears in conventional formulations. The graph must be able to show this — it is one of the project's potentially novel contributions.

---

## 7. Sequencing

1. Finalize graph schema with cross-theory generality baked in.
2. Populate SM dependency graph using the existing JSON as a starting point, enriching nodes with parametric interfaces.
3. Populate GR dependency graph in the same schema.
4. Implement graph comparison operations (shared subgraph extraction, fork point identification, structural diff).
5. Begin wrapping existing tooling (GAP, LieART, FeynRules, etc.) with the project's parametric interface pattern.
6. Connect the wrapped tools to graph nodes so that parametric changes at a node trigger recomputation downstream.
