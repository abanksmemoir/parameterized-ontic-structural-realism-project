# V2 Note: Why This Refactor and What Changed

## Why V2

V1 of the Standard Model dependency graph was built on 2026-04-05 as a first pass. It established the 10-layer, 30-node structure from logical axioms to the Standard Model Lagrangian. The five-agent time-symmetry debt investigation, completed the same day, exposed several problems:

1. **The iε prescription — the choice of retarded propagator — is not represented anywhere in v1.** This is the most consequential undeclared assumption in the graph. It enters silently at the quantization layer and determines the causal structure of everything built on top of it. A graph whose thesis is "no smuggled commitments" cannot leave this out.

2. **The term "parametric" is doing too much work.** V1 uses it to cover axiom choices (CL vs IL), structural selections (gauge group), conventions (renormalization scheme), and boundary conditions (not represented at all). These are different kinds of choices with different downstream consequences. They need to be distinguished.

3. **"Presupposes" conflates logical necessity with conventional coupling.** Some v1 presuppositions are genuine entailments (you cannot formulate Lie algebras without a vector space structure). Others are conventional choices of substrate (FOL is built on CL in v1, but could be built on IL). The graph treats both the same way. This hides theory-construction parameters behind an appearance of logical necessity.

4. **Time is underspecified.** Temporal structure enters the graph at multiple points — metric signature, Wick rotation, iε prescription, CP violation — but v1 doesn't track this chain or acknowledge that the number system used to parameterize time is itself a parameter at each stage.

5. **The graph has no way to represent contingent provisions.** Some nodes provide outputs that depend on conditions not guaranteed by the node's own structure. The absorber condition is the prototype: the retarded propagator is provided contingent on the universe being a sufficient absorber, which is a cosmological fact, not a consequence of the QFT formalism. V1 can't express this.

---

## Terminology

### Everything is a parameter

Every choice in the graph — from the selection of a deductive system at Layer 0 to the CKM phase at Layer 9 — is a parameter: a choice among alternatives that can be contemplated and gamed out from common, logically prior, commitments. The graph is a map of the joint parameter space of possible theories built from shared structural roots.

### Parameter subtypes

Each parameter is assigned one of the following subtypes:

- **axiom**: A foundational choice with no prior constraints within the framework. Multiple internally consistent alternatives exist. Nothing upstream forces the choice. *Examples: classical vs. intuitionistic logic; ZFC vs. type theory.*

- **structural**: A choice of mathematical or physical structure. The space of available options is determined by upstream parameter settings. *Examples: gauge group; representation assignments; number of fermion generations.*

- **kinematic**: A choice about the arena — dimension, signature, topology — in which the theory is formulated. *Examples: spacetime dimension; metric signature (−,+,+,+) vs. (+,+,+,+); manifold topology.*

- **dynamical**: A choice about equations of motion or interaction rules. *Examples: Lagrangian density; coupling constants; Yukawa matrices.*

- **boundary**: A choice about initial/final conditions or propagator prescription, logically independent of the dynamics. The dynamics are time-symmetric; the boundary condition breaks that symmetry. *Examples: iε sign; absorber condition; Penrose's Weyl curvature hypothesis; cosmological initial state.*

- **convention**: A choice that affects the description but not the physics. Can be changed without altering any observable. *Examples: renormalization scheme; gauge-fixing condition; coordinate system; units.*

### Dependency types

Edges between nodes (formerly all called "presupposes") are classified as:

- **logical**: Y cannot be formulated without X. This is not a choice — it is entailed by what Y is. *Example: Lie algebras require a vector space structure (LA).*

- **conventional**: Y is standardly built on X, but alternatives exist in the space of possible theories. This is a disguised parameter. *Example: FOL is conventionally built on CL, but intuitionistic FOL exists.*

- **contingent**: Y uses an output of X, but only under conditions that X does not internally guarantee. *Example: QFT uses the retarded propagator, contingent on boundary conditions that are not part of the QFT formalism itself.*

### Provisions

What a node makes available to downstream nodes. Unchanged from v1 in concept, but v2 adds contingency annotations where a provision depends on conditions external to the node.

---

## Decision Log

Every structural choice made in the v2 refactor is documented here.

### D1: Node structure retained from v1

The 10-layer, 30-node structure is preserved. The layers and nodes represent real structural strata in the construction of the Standard Model. What changes is the annotation of each node (parameter subtypes, dependency audit, time notes), not the topology.

**Rationale:** The node structure is sound. The problems are in the metadata, not the skeleton.

### D2: "Presupposes" split into dependency types

Every v1 `presupposes` entry was audited. Each is now classified as logical, conventional, or contingent. Where a dependency turned out to be a disguised parameter, this is noted.

**Audit results (summary — full details in the graph spec):**

| Node | V1 Presupposes | V2 Classification | Notes |
|------|---------------|-------------------|-------|
| FOL | CL | conventional | Could be built on IL; choice of underlying logic is a parameter |
| ZFC | CL, FOL | logical (CL), logical (FOL) | ZFC is defined within classical first-order logic |
| TT | IL | conventional | Martin-Lof TT uses IL, but type theories exist with classical logic |
| CAT | ZFC | conventional | Category theory can be founded on TT or its own axioms |
| GRP | ZFC | conventional | Group theory requires some foundational substrate; ZFC is the standard choice |
| RING | GRP | logical | Rings are defined in terms of groups (additive group) |
| LA | RING | logical | Vector spaces are modules over fields, which are rings |
| TOP | ZFC | conventional | Point-set topology requires a set theory; ZFC is conventional |
| REAL | ZFC, TOP | logical (ZFC), logical (TOP) | Completeness of R requires set theory; metric topology is essential |
| CMPLX | REAL | logical | C is constructed from R |
| LIE | GRP, TOP, REAL | logical (all) | Lie groups are topological groups with smooth structure |
| LIEA | LIE, LA | conventional (LIE), logical (LA) | Lie algebras can be defined purely algebraically without Lie groups; historically motivated by them |
| REP | LIEA, LA | logical (both) | Representations are homomorphisms into GL(V); require both algebra and linear structure |
| MAN | TOP, REAL, LA | logical (all) | Manifolds require topology, real analysis (charts), and linear algebra (tangent spaces) |
| FB | MAN, GRP | logical (both) | Fiber bundles require a base manifold and a structure group |
| CONN | FB, LIEA | logical (both) | Connections are Lie-algebra-valued 1-forms on fiber bundles |
| HILB | LA, REAL, TOP | logical (all) | Hilbert spaces are complete inner product spaces |
| OA | HILB, RING | logical (both) | Operator algebras are algebras of operators on Hilbert spaces |
| PATH | HILB, MAN, REAL | logical (HILB, REAL), conventional (MAN) | Path integrals require a Hilbert space and analysis; manifold structure is one way to specify the configuration space |
| LAG | MAN, REAL | logical (both) | Lagrangian mechanics requires smooth manifolds and calculus of variations |
| GAUGE | CONN, LAG, REP | logical (all) | Gauge theory is connection geometry + Lagrangian dynamics + matter representations |
| QFT | GAUGE, HILB, PATH | conventional (GAUGE), logical (HILB), conventional (PATH) | QFT requires Hilbert space but can be formulated without gauge theory (scalar QFT) and without path integrals (canonical quantization) |
| RENORM | QFT, CMPLX | logical (both) | Renormalization requires QFT and complex analysis (dimensional regularization, analytic continuation) |
| ANOM | QFT, REP, CONN | logical (all) | Anomaly cancellation requires representation theory, topology (index theorems), and the QFT framework |
| SM_G | GAUGE, ANOM, RENORM | logical (all) | The SM gauge group requires gauge theory, anomaly freedom, and renormalizability |
| SM_F | SM_G, REP, ANOM | logical (all) | Fermion content requires gauge representations and anomaly cancellation |
| SM_H | SM_G, LAG | logical (both) | Higgs mechanism requires the gauge structure and a Lagrangian |
| SM_Y | SM_F, SM_H | logical (both) | Yukawa couplings require fermion fields and the Higgs field |

**Key findings from the audit:**
- 7 dependencies (out of ~50) are conventional rather than logical. These represent disguised theory-construction parameters.
- The most significant is QFT → GAUGE: the Standard Model uses gauge theory, but QFT as a framework does not require it. This dependency is a structural parameter (the choice to build the theory on gauge symmetry).
- QFT → PATH is also conventional: canonical quantization is an alternative.
- At Layers 0-1 (logic and foundations), most dependencies are conventional — reflecting the fact that the foundational substrate is a genuine theory-construction choice.

### D3: iε prescription added as explicit boundary parameter

Added to the QFT node as a boundary parameter with two values: +iε (standard, selects Feynman propagator / retarded causal structure) and −iε (time-reversed). The contingent dependency on cosmological boundary conditions is noted. This parameter was invisible in v1.

**Rationale:** The time-symmetry research establishes that the iε prescription (a) is the most consequential undeclared assumption in the Standard Model, (b) is a genuine parameter with a well-defined alternative, (c) has a physical justification in only one gauge sector (U(1), via the absorber condition), and (d) propagates causally to every node above QFT.

### D4: Time audit conducted

Every node was examined for where temporal structure enters or acquires new commitments. Findings are recorded as `temporal_note` entries in the graph spec. The chain is:

1. **REAL (Layer 3)**: Provides the continuum (R) that will parameterize time. No temporal interpretation yet.
2. **MAN (Layer 5)**: Metric signature is a kinematic parameter. The choice (−,+,+,+) vs. (+,+,+,+) is where time is first formally distinguished from space. The number system used (R for Lorentzian, imaginary time for Euclidean) is a parameter.
3. **PATH (Layer 6)**: Wick rotation (t → −iτ) is listed as a parameter. This is an analytic continuation that transforms temporal structure. The measure over paths inherits the temporal direction from the signature.
4. **QFT (Layer 8)**: The iε prescription enters here. This is where time acquires a *preferred direction* — positive-energy states propagate forward, negative-energy states backward. Prior to this, temporal structure was symmetric (Lorentzian signature distinguishes time from space but doesn't privilege a direction).
5. **SM_Y (Layer 9)**: The CKM complex phase introduces dynamical T violation — certain processes distinguish past from future. But the time-symmetry research (Agent 3) establishes that this presupposes the iε prescription: observable CP violation requires interference with iε-derived strong phases.

**Key finding:** Time's directionality first enters at QFT (Layer 8) via the iε prescription. Everything below Layer 8 is time-symmetric (the dynamics admit both retarded and advanced solutions). Everything above Layer 8 inherits the direction. The physical justification for the choice sits outside the graph as currently constructed — in cosmological boundary conditions (absorber condition, Hubble expansion, Penrose WCH) that have no node.

**Decision:** The iε prescription is registered as a boundary parameter at QFT. The cosmological justification is noted but not given its own node, because the graph covers the Standard Model's mathematical structure, not cosmology. The graph is honest about where it receives this input from outside its scope.

### D5: Contingent provisions annotated

Three nodes have provisions that depend on conditions not guaranteed internally:

1. **QFT**: Provides "causal propagator structure" contingent on the iε boundary parameter being set. If the iε sign is treated as genuinely open (which the time-symmetric formulation does), the causal structure is not determined by QFT alone.

2. **GAUGE**: The Yang-Mills equations are time-symmetric. The provision of "field equations with causal solutions" depends on the propagator prescription imposed at the QFT level. GAUGE alone provides both retarded and advanced solutions equally.

3. **SM_Y**: CP violation is a provision, but its observability is contingent on the iε prescription (Agent 3 finding). Without the pre-existing causal arrow, the CKM phase produces no observable CP asymmetry.

### D6: Absorber condition noted as external input

The Wheeler-Feynman absorber condition is a physical argument from outside the graph's scope (cosmology, not SM structure) that provides a justification for the iε boundary parameter in the U(1) sector. It is noted as an external input, not a node. The time-symmetry research findings (Agents 1-5) on the status of this justification across gauge sectors are summarized in a note on the QFT node.

### D7: Markdown is the primary document

The markdown graph spec (sm_dependency_graph_v2.md) is the primary document. The JSON (sm_dependency_graph_v2.json) is derived from it. Where they conflict, the markdown is authoritative. V1 had both as co-equal, which created ambiguity.

---

## Open Questions and Deep Research Flags

These are not resolved by the v2 refactor. The graph handles each by noting the parameter, recording what value practice assumes, and flagging the justification gap. The pattern is consistent: register the variable, don't pretend the assumed value is derived.

### OQ1: Cosmological context and time symmetry

The graph does not extend to cosmology. The iε prescription's physical justification lives in cosmological boundary conditions (absorber condition, Hubble expansion, Penrose WCH) that are outside the graph's scope. Rather than adding a cosmological layer, the graph annotates every node where temporal structure appears with the following observation: the theory contains the consequences of time symmetry via these boundary conditions, and we should be mindful of what that implies for its predictions. Specifically: wherever the graph assumes the retarded propagator, the underlying dynamics are time-symmetric, and the retarded character is contingent on external conditions. If those conditions fail locally, the theory's predictions change. This is noted in the temporal commentary at QFT (P057), GAUGE, and SM_Y.

**Status:** Handled via annotation, not architectural extension. May revisit.

### OQ2: Vacuum state as a hidden parameter

The choice of vacuum state is a theory-construction parameter that the Standard Model silently consumes. Practice assumes the vacuum is the unique Poincaré-invariant state |Ω⟩ determined by the Wightman axioms and spectral condition. This is registered as a variable. Why it takes that value and not another (e.g., Bunch-Davies in curved spacetime, a squeezed state, a thermal state, a state with different iε) is not derived from within the SM framework. 

**Action:** Add vacuum state as a boundary parameter at QFT (P078). Note that practice assumes the Poincaré-invariant vacuum. Flag for deep research: is there a principled reason the vacuum takes this value, or is it an independent boundary condition?

### OQ3: Gribov ambiguity

In non-abelian gauge theory (SU(2), SU(3)), the gauge-fixing procedure does not yield unique gauge-field configurations. Gribov copies exist — physically equivalent configurations that satisfy the same gauge condition but are related by large gauge transformations. The choice of Gribov region (typically the first Gribov horizon) is a parameter that practice assumes a specific value for.

**Action:** Add Gribov region choice as a parameter at CONN/GAUGE for non-abelian theories (P079). Note that practice restricts to the first Gribov horizon (or the fundamental modular region). Flag for deep research: what is the justification? Does the choice affect physical observables? What are the consequences of alternative choices?

### OQ4: Number of fermion generations — subtype disambiguation

The number of generations (P066) is listed as structural. "Structural" needs to be flagged as potentially in need of disambiguation. Many things are structural. The value 3 is one well-formed way of elaborating the logically prior elements (anomaly cancellation works per generation, so any N is consistent). There may be a deeper reason (CP violation requires N ≥ 3; anthropic considerations; a GUT or string-theoretic derivation), but no such derivation exists. 

**Action:** Keep as structural. Add a flag noting that this parameter takes a value (3) for which no derivation exists, and that the counterfactual (N ≠ 3) is well-formed and should be contemplated. Flag for deep research.

### OQ5: Entanglement of temporal parameters (P036, P047, P057)

The metric signature at MAN (P036), the Wick rotation at PATH (P047), and the iε sign at QFT (P057) all concern temporal structure and may not be independent parameters. The Wick rotation transforms the Lorentzian signature to Euclidean. The iε prescription is related to the Wick rotation via contour integration in the complex time plane. Whether these are three independent choices or three aspects of a single choice is not fully understood.

**Action:** Note the potential entanglement in the temporal structure chain. Flag for deep research. Handle with care — this is a case where assuming independence may be wrong, but asserting dependence without proof would be worse.
