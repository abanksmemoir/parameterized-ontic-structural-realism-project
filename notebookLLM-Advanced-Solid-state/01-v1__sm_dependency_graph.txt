# Standard Model Structural Dependency Graph

**Project:** Parameterized Ontic Structural Realism  
**Version:** 0.1.0  
**Date:** 2026-04-05

## Thesis

The Standard Model of particle physics is a structural configuration that can be decomposed into a dependency graph where each node declares its presuppositions, its outputs, and its parametric degrees of freedom. The graph runs from the choice of logical axioms at the bottom to the specific particle content and coupling constants at the top. Every layer is a functor: axioms in, structural consequences out. Composition is explicit. Nothing reaches around its interface.

The philosophical commitment: "real" is an honorific bestowed on regions of the lattice of well-formed hypotheticals that do nontrivial empirical work. The Platonism is instrumental — it provides navigational medium without ontological commitment to any particular corner. The software that implements this graph should be docile at every layer: no smuggled commitments, no ambient assumptions, no hidden imports.

---

## Layer 0: Logic

The choice of deductive system. Everything downstream inherits these commitments.

### CL — Classical logic
- **Presupposes:** ∅ (axiom choice)
- **Provides:** Proof by contradiction, De Morgan duality, Boolean algebra
- **Parametric:** LEM can be dropped → intuitionistic; explosion can be dropped → paraconsistent

### IL — Intuitionistic logic
- **Presupposes:** ∅ (axiom choice)
- **Provides:** Constructive existence proofs, Curry-Howard correspondence
- **Parametric:** Can add LEM back selectively; decidability of specific propositions

### FOL — First-order quantification
- **Presupposes:** CL
- **Provides:** Quantified statements, model theory basics
- **Parametric:** Choice of logic (classical vs intuitionistic); sorts (single vs many-sorted)

---

## Layer 1: Foundations

Set-theoretic or type-theoretic substrate. Determines what mathematical objects you can construct.

### ZFC — ZFC set theory
- **Presupposes:** CL, FOL
- **Provides:** Infinite sets, powersets, well-ordering, Cartesian products
- **Parametric:** Axiom of Choice (drop → ZF); continuum hypothesis (independent); foundation (drop → non-well-founded sets)

### TT — Type theory
- **Presupposes:** IL
- **Provides:** Dependent types, inductive types, universe hierarchy
- **Parametric:** Univalence axiom (add → HoTT); impredicativity; universe levels

### CAT — Category theory
- **Presupposes:** ZFC
- **Provides:** Functors, natural transformations, limits/colimits, adjunctions
- **Parametric:** Size (small vs large categories); enrichment base

---

## Layer 2: Core algebra

Basic algebraic structures. Groups encode symmetry; rings and fields provide arithmetic; linear algebra provides the representation medium.

### GRP — Group theory
- **Presupposes:** ZFC
- **Provides:** Subgroups, quotient groups, homomorphisms, group actions
- **Parametric:** Commutativity (abelian vs non-abelian); finiteness

### RING — Rings & fields
- **Presupposes:** GRP
- **Provides:** Ideals, field extensions, characteristic
- **Parametric:** Commutativity; characteristic (0 vs p)

### LA — Linear algebra
- **Presupposes:** RING
- **Provides:** Bases, dual spaces, tensor products, inner products
- **Parametric:** Dimension; base field (R vs C); inner product signature

---

## Layer 3: Topology & analysis

Continuity, convergence, completeness. The substrate for geometric and analytic reasoning.

### TOP — Point-set topology
- **Presupposes:** ZFC
- **Provides:** Continuous maps, compactness, Hausdorff separation, quotient spaces
- **Parametric:** Separation axioms (T0–T4); compactness conditions

### REAL — Real analysis
- **Presupposes:** ZFC, TOP
- **Provides:** Lebesgue measure, L^p spaces, distribution theory
- **Parametric:** Completeness (drop → constructive analysis); measure (Lebesgue vs other)

### CMPLX — Complex analysis
- **Presupposes:** REAL
- **Provides:** Analytic continuation, residue calculus, conformal maps
- **Parametric:** Riemann surface structure

---

## Layer 4: Lie theory

Continuous symmetry groups, their infinitesimal structure, and how they act on vector spaces.

### LIE — Lie groups
- **Presupposes:** GRP, TOP, REAL
- **Provides:** Exponential map, adjoint representation, compact form classification
- **Parametric:** Compactness; connectedness; simple vs semisimple

### LIEA — Lie algebras
- **Presupposes:** LIE, LA
- **Provides:** Root systems, Dynkin diagrams, Cartan subalgebras, Killing form
- **Parametric:** Rank; type (A,B,C,D,E,F,G); real form

### REP — Representation theory
- **Presupposes:** LIEA, LA
- **Provides:** Irreducible representations, characters, Clebsch-Gordan decomposition, weight diagrams
- **Parametric:** Representation dimension; highest weight

---

## Layer 5: Differential geometry

Manifolds, bundles, connections. The geometric language in which gauge fields live.

### MAN — Smooth manifolds
- **Presupposes:** TOP, REAL, LA
- **Provides:** Tangent/cotangent bundles, differential forms, de Rham cohomology
- **Parametric:** Dimension; orientability; metric signature

### FB — Fiber bundles
- **Presupposes:** MAN, GRP
- **Provides:** Sections, bundle maps, associated bundles, transition functions
- **Parametric:** Structure group; fiber type; topology (Chern classes)

### CONN — Connections & curvature
- **Presupposes:** FB, LIEA
- **Provides:** Covariant derivative, holonomy, Chern-Simons forms, characteristic classes
- **Parametric:** Connection choice (gauge orbit); curvature constraints (flat, self-dual, etc.)

---

## Layer 6: Functional analysis & quantization

Infinite-dimensional spaces, operator theory, and the path integral. The bridge from classical to quantum.

### HILB — Hilbert spaces
- **Presupposes:** LA, REAL, TOP
- **Provides:** Orthonormal bases, spectral theorem, tensor product spaces, trace class operators
- **Parametric:** Separability; dimension (finite vs infinite)

### OA — Operator algebras
- **Presupposes:** HILB, RING
- **Provides:** GNS construction, states as functionals, superselection sectors
- **Parametric:** Type (I, II, III); factor structure

### PATH — Path integral
- **Presupposes:** HILB, MAN, REAL
- **Provides:** Propagators, partition functions, saddle-point / WKB approximation
- **Parametric:** Measure (not rigorously defined in general); Wick rotation

---

## Layer 7: Classical field theory

Lagrangian dynamics on spacetime. Gauge theory as geometry of connections.

### LAG — Lagrangian / variational
- **Presupposes:** MAN, REAL
- **Provides:** Equations of motion, conserved currents, symplectic structure
- **Parametric:** Lagrangian density; spacetime signature

### GAUGE — Gauge theory (classical)
- **Presupposes:** CONN, LAG, REP
- **Provides:** Gauge transformations, field strength tensor, minimal coupling, covariant derivatives on matter fields
- **Parametric:** Gauge group G; matter representations; coupling constants

---

## Layer 8: Quantum field theory

Quantized fields, renormalization, anomaly structure. The framework that constrains which classical field theories survive quantization.

### QFT — Field quantization
- **Presupposes:** GAUGE, HILB, PATH
- **Provides:** Feynman diagrams, S-matrix, vacuum state, particle interpretation
- **Parametric:** Regularization scheme; operator ordering

### RENORM — Renormalization
- **Presupposes:** QFT, CMPLX
- **Provides:** Running couplings, beta functions, anomalous dimensions, effective field theory
- **Parametric:** Renormalization scheme (MS-bar, etc.); scale μ; counterterm structure

### ANOM — Anomaly cancellation
- **Presupposes:** QFT, REP, CONN
- **Provides:** Anomaly-free representations, index theorems, topological constraints on spectrum
- **Parametric:** Fermion content must satisfy trace conditions

---

## Layer 9: Standard Model

The specific structural configuration that matches observation.

### SM_G — SU(3)×SU(2)×U(1)
- **Presupposes:** GAUGE, ANOM, RENORM
- **Provides:** Strong, weak, hypercharge interactions; gauge boson content (8+3+1)
- **Parametric:** The group itself (why not SU(5)? SO(10)?); coupling constants g₃, g₂, g₁

### SM_F — Three fermion generations
- **Presupposes:** SM_G, REP, ANOM
- **Provides:** Quark and lepton fields; anomaly cancellation (per generation)
- **Parametric:** Number of generations (why 3?); representation assignments

### SM_H — Higgs mechanism / SSB
- **Presupposes:** SM_G, LAG
- **Provides:** W±, Z masses; photon as massless residual; fermion mass terms (via Yukawa); Higgs boson
- **Parametric:** Higgs potential parameters (μ², λ); vev v ≈ 246 GeV

### SM_Y — Yukawa & mixing
- **Presupposes:** SM_F, SM_H
- **Provides:** Fermion masses; flavor-changing currents; CP violation
- **Parametric:** Yukawa coupling matrices; CKM angles + phase; PMNS angles + phases; neutrino mass mechanism

---

## Structural observations

**Deepest dependency chain:** CL → FOL → ZFC → GRP → LIE → LIEA → REP → CONN → GAUGE → QFT → ANOM → SM_F (12 links). Every link is a point where a different parametric choice propagates upward.

**Most constrained node:** ANOM (anomaly cancellation). Takes representation theory and topology as input, outputs hard constraints on which particle content is consistent. This is the structural realist's strongest card — the Standard Model's particle content is not arbitrary but is one of a small number of anomaly-free configurations.

**Fattest parametric nodes:** All at Layer 9. "Why 3 generations?", "Why these coupling constants?", "Why SU(3)×SU(2)×U(1)?" — these are the questions that look like brute contingency from a conventional perspective but are reframed in the lattice approach as structural coordinates.

**Cross-layer dependencies to watch:** CONN depends on both FB (geometry) and LIEA (algebra). This is the node where geometry and algebra merge — the connection on a fiber bundle *is* a Lie-algebra-valued 1-form. The KK holonomy framework makes this merger the fundamental ontological fact.

---

## Next steps

1. Deepen each node with internal sub-dependencies (e.g., GRP → normal subgroups → quotient construction → first isomorphism theorem)
2. Map existing software packages to each node (Lean mathlib, GAP, LieART, FeynRules, SARAH, lattice QCD)
3. Design the Python class architecture: each layer as a class receiving its substrate as constructor arguments
4. Identify which "parametric" annotations correspond to actual runtime parameters vs. architectural choices (swap at build time vs. runtime)
