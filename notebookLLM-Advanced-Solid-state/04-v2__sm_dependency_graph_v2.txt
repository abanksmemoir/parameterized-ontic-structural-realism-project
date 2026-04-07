# Standard Model Structural Dependency Graph — V2

**Project:** Parameterized Ontic Structural Realism
**Version:** 2.0.0
**Date:** 2026-04-05
**Changes from V1:** See V2_NOTE.md

## Thesis

The Standard Model of particle physics is a structural configuration that can be decomposed into a dependency graph where each node declares its parameters, its dependencies, and its provisions. The graph runs from logical axioms (Layer 0) to the specific particle content and coupling constants (Layer 9). Every layer is a functor: parameters in, structural consequences out. Composition is explicit. Nothing reaches around its interface.

Everything that is a choice is a parameter. Parameters are subtyped (axiom, structural, kinematic, dynamical, boundary, convention). Dependencies between nodes are typed (logical, conventional, contingent). Provisions note contingencies where applicable.

"Real" is an honorific bestowed on regions of the lattice of well-formed hypotheticals that do nontrivial empirical work. The Platonism is instrumental — it provides navigational medium without ontological commitment to any particular corner.

---

## Layer 0: Logic

The choice of deductive system. Everything downstream inherits these commitments.

### CL — Classical Logic

- **Parameters:**
  - Law of excluded middle (axiom): on. Alternative: off → intuitionistic logic.
  - Explosion principle (axiom): on. Alternative: off → paraconsistent logic.
- **Dependencies:** none (root node)
- **Provides:** proof by contradiction, De Morgan duality, Boolean algebra, bivalent truth values
- **Temporal note:** none. Logic is atemporal.

### IL — Intuitionistic Logic

- **Parameters:**
  - Law of excluded middle (axiom): off.
  - Explosion principle (axiom): on.
- **Dependencies:** none (root node)
- **Provides:** constructive existence proofs, Curry-Howard correspondence, BHK interpretation
- **Temporal note:** none.

### FOL — First-Order Quantification

- **Parameters:**
  - Underlying logic (axiom): CL. Alternative: IL (intuitionistic FOL exists and is well-studied).
  - Sort structure (structural): single-sorted. Alternative: many-sorted.
  - Order (structural): first-order. Alternatives: second-order, higher-order.
- **Dependencies:**
  - CL — conventional. FOL is standardly built on classical logic. Intuitionistic FOL is an alternative.
- **Provides:** quantified statements, model theory, completeness theorem (Godel), compactness theorem
- **Temporal note:** none.

---

## Layer 1: Foundations

Set-theoretic or type-theoretic substrate. Determines what mathematical objects you can construct.

### ZFC — ZFC Set Theory

- **Parameters:**
  - Axiom of choice (axiom): included. Alternative: excluded → ZF.
  - Continuum hypothesis (axiom): independent (neither provable nor refutable from ZFC).
  - Foundation axiom (axiom): included. Alternative: excluded → non-well-founded sets (Aczel).
- **Dependencies:**
  - CL — logical. ZFC is formulated in classical first-order logic.
  - FOL — logical. ZFC axioms are first-order sentences.
- **Provides:** infinite sets, powersets, well-ordering, Cartesian products, transfinite induction
- **Temporal note:** none. Set theory is atemporal. (The well-ordering theorem provides a total order on any set, which is a faint structural echo of sequentiality but carries no temporal interpretation.)

### TT — Type Theory

- **Parameters:**
  - Univalence (axiom): off. Alternative: on → HoTT.
  - Impredicativity (structural): varies by system.
  - Universe levels (structural): cumulative hierarchy.
- **Dependencies:**
  - IL — conventional. Martin-Lof type theory is natively intuitionistic. Type theories with classical logic exist (Lean 4 has classical axioms available).
- **Provides:** dependent types, inductive types, universe hierarchy, propositions-as-types
- **Temporal note:** none.

### CAT — Category Theory

- **Parameters:**
  - Size (structural): allows large categories. Alternative: restrict to small categories.
  - Enrichment base (structural): Set. Alternatives: Ab, Top, Cat (2-categories).
- **Dependencies:**
  - ZFC — conventional. Category theory can be founded on type theory, NBG set theory, or its own axioms (ETCS, ETCC).
- **Provides:** functors, natural transformations, limits/colimits, adjunctions, Yoneda lemma
- **Temporal note:** none.

---

## Layer 2: Core Algebra

Basic algebraic structures.

### GRP — Group Theory

- **Parameters:**
  - Commutativity (structural): unrestricted (includes non-abelian). Can restrict to abelian.
  - Finiteness (structural): unrestricted. Can restrict to finite groups.
- **Dependencies:**
  - ZFC — conventional. Group theory requires some foundational substrate for the set-with-operations definition. ZFC is standard; alternatives exist.
- **Provides:** subgroups, quotient groups, homomorphisms, group actions, Sylow theorems, classification of finite simple groups
- **Temporal note:** none.

### RING — Rings and Fields

- **Parameters:**
  - Commutativity (structural): unrestricted. Can restrict to commutative rings.
  - Characteristic (structural): unrestricted. Fields have characteristic 0 or prime p.
- **Dependencies:**
  - GRP — logical. A ring is an abelian group under addition with a second associative operation. The group structure is definitionally required.
- **Provides:** ideals, quotient rings, field extensions, polynomial rings, algebraic closure
- **Temporal note:** none.

### LA — Linear Algebra

- **Parameters:**
  - Base field (structural): unrestricted. Physics uses R and C. Alternatives: finite fields, p-adic fields.
  - Dimension (structural): unrestricted. Physics uses finite and countably infinite.
  - Inner product signature (kinematic): unrestricted. Physics uses (−,+,+,+) for spacetime, (+,+,+,+) for Euclidean, positive-definite for Hilbert spaces.
- **Dependencies:**
  - RING — logical. Vector spaces are modules over fields. Fields are commutative division rings.
- **Provides:** bases, dual spaces, tensor products, inner products, determinants, eigenvalues
- **Temporal note:** Inner product signature is the first parameter in the graph that will eventually distinguish time from space, but at this layer it carries no temporal interpretation. It is a parameter of the bilinear form, nothing more.

---

## Layer 3: Topology and Analysis

Continuity, convergence, completeness.

### TOP — Point-Set Topology

- **Parameters:**
  - Separation axioms (structural): T0 through T4. Physics typically uses Hausdorff (T2).
  - Compactness conditions (structural): varies. Paracompactness required for manifold theory.
- **Dependencies:**
  - ZFC — conventional. Topology can be developed in constructive settings or type theory, but point-set topology as standardly practiced uses ZFC.
- **Provides:** continuous maps, compactness, connectedness, quotient spaces, covering spaces
- **Temporal note:** none.

### REAL — Real Analysis

- **Parameters:**
  - Completeness (axiom): included (Dedekind completeness). Alternative: constructive reals (Bishop).
  - Measure (structural): Lebesgue. Alternatives: Borel, Hausdorff.
- **Dependencies:**
  - ZFC — logical. The Dedekind construction of R requires powersets. Completeness is a set-theoretic property.
  - TOP — logical. Metric topology on R is foundational.
- **Provides:** Lebesgue measure, L^p spaces, distribution theory (Schwartz), Fourier analysis
- **Temporal note:** R provides the continuum that will parameterize both space and time. At this layer, R is a complete ordered field — no temporal interpretation.

### CMPLX — Complex Analysis

- **Parameters:**
  - Riemann surface structure (structural): varies by application.
- **Dependencies:**
  - REAL — logical. C = R + iR. Complex analysis presupposes real analysis.
- **Provides:** analytic continuation, residue calculus, conformal maps, Cauchy integral formula
- **Temporal note:** The complex plane will later be the arena for pole structure in propagators. Analytic continuation (the Wick rotation) and contour integration (the iε prescription) both live here. But at this layer, C is a mathematical structure with no physical interpretation.

---

## Layer 4: Lie Theory

Continuous symmetry groups, their infinitesimal structure, and how they act on vector spaces.

### LIE — Lie Groups

- **Parameters:**
  - Compactness (structural): physics uses compact groups for internal symmetries (SU(N), SO(N)) and noncompact for spacetime (Lorentz group SO(1,3)).
  - Connectedness (structural): physics uses connected components (identity component).
  - Simple vs. semisimple (structural): the Standard Model gauge group is a product of simple and abelian factors.
- **Dependencies:**
  - GRP — logical. Lie groups are groups.
  - TOP — logical. Lie groups are topological spaces (with smooth structure).
  - REAL — logical. Smooth structure requires real analysis.
- **Provides:** exponential map, adjoint representation, compact form classification, Haar measure, one-parameter subgroups
- **Temporal note:** One-parameter subgroups of the Lorentz group generate time translations and boosts. This is where continuous time evolution becomes representable — but no specific physical interpretation is imposed at this layer.

### LIEA — Lie Algebras

- **Parameters:**
  - Rank (structural): determines the dimension of the Cartan subalgebra.
  - Type (structural): Cartan classification A, B, C, D, E, F, G.
  - Real form (structural): compact vs. split vs. other real forms.
- **Dependencies:**
  - LIE — conventional. Lie algebras are historically and motivationally derived from Lie groups (as the tangent space at identity). But Lie algebras can be defined purely algebraically without reference to Lie groups. The dependency is conventional, not logical.
  - LA — logical. Lie algebras are vector spaces with a bracket operation. Linear algebra is definitionally required.
- **Provides:** root systems, Dynkin diagrams, Cartan subalgebras, Killing form, Casimir operators, structure constants
- **Temporal note:** none at this layer.

### REP — Representation Theory

- **Parameters:**
  - Representation dimension (structural): varies. Physics uses specific representations (fundamental, adjoint, trivial, etc.).
  - Highest weight (structural): labels irreducible representations of semisimple Lie algebras.
- **Dependencies:**
  - LIEA — logical. Representations are homomorphisms from Lie algebras to gl(V).
  - LA — logical. The target space V is a vector space.
- **Provides:** irreducible representations, characters, Clebsch-Gordan decomposition, weight diagrams, Schur's lemma, tensor product decomposition
- **Temporal note:** none.

---

## Layer 5: Differential Geometry

Manifolds, bundles, connections.

### MAN — Smooth Manifolds

- **Parameters:**
  - Dimension (kinematic): 4 in standard physics. Alternatives: any positive integer; also studied for 2, 3, 10, 11, 26.
  - Orientability (kinematic): orientable in standard physics. Alternative: non-orientable.
  - Metric signature (kinematic): (−,+,+,+) Lorentzian in standard physics. Alternatives: (+,+,+,+) Euclidean; (−,−,+,+) ultrahyperbolic; degenerate (Newton-Cartan).
- **Dependencies:**
  - TOP — logical. Manifolds are topological spaces with smooth atlas.
  - REAL — logical. Charts map to R^n; smooth structure requires real analysis.
  - LA — logical. Tangent spaces are vector spaces.
- **Provides:** tangent/cotangent bundles, differential forms, de Rham cohomology, Riemannian/Lorentzian geometry, geodesics, curvature tensors
- **Temporal note:** **First formal appearance of temporal structure.** The metric signature parameter is where time is distinguished from space. The choice (−,+,+,+) declares that one dimension has opposite sign under the inner product. This dimension is interpreted as time. At this layer, the distinction is purely geometric — there is no preferred direction along the time dimension. The metric is invariant under t → −t. The number system parameterizing this dimension is R (inherited from REAL). Whether it should be R, or a half-line R+, or a circle, or something else is a kinematic parameter that is typically left implicit.

### FB — Fiber Bundles

- **Parameters:**
  - Structure group (structural): varies. Physics uses U(1), SU(2), SU(3), SO(1,3), Spin(1,3).
  - Fiber type (structural): varies (vector bundle, principal bundle, associated bundle).
  - Topology / characteristic classes (structural): Chern classes, Pontryagin classes. Determines global structure (monopoles, instantons).
- **Dependencies:**
  - MAN — logical. A fiber bundle requires a base manifold.
  - GRP — logical. A principal bundle requires a structure group.
- **Provides:** sections, bundle maps, associated bundles, transition functions, clutching construction
- **Temporal note:** none directly. But if the base manifold has Lorentzian signature, the bundle inherits a distinction between timelike and spacelike directions in the base.

### CONN — Connections and Curvature

- **Parameters:**
  - Connection choice / gauge orbit (convention): within a gauge equivalence class, the specific connection is a convention (gauge choice). The gauge orbit is physical; the representative is not.
  - Curvature constraints (structural): flat, self-dual, anti-self-dual, Yang-Mills (extremal of the Yang-Mills functional).
- **Dependencies:**
  - FB — logical. A connection is defined on a fiber bundle.
  - LIEA — logical. A connection is a Lie-algebra-valued 1-form.
- **Provides:** covariant derivative, parallel transport, holonomy, curvature 2-form, Chern-Simons forms, characteristic classes, Bianchi identity
- **Temporal note:** none directly. But the curvature 2-form on a Lorentzian base manifold decomposes into electric and magnetic parts, introducing a time-dependent decomposition.

---

## Layer 6: Functional Analysis and Quantization

Infinite-dimensional spaces, operator theory, and the bridge from classical to quantum.

### HILB — Hilbert Spaces

- **Parameters:**
  - Separability (structural): separable in standard physics (countable orthonormal basis). Alternative: non-separable.
  - Dimension (structural): infinite-dimensional in QFT. Finite-dimensional in quantum information.
- **Dependencies:**
  - LA — logical. Hilbert spaces are inner product spaces (linear algebra).
  - REAL — logical. Completeness requires real analysis (Cauchy sequences).
  - TOP — logical. The norm topology is essential.
- **Provides:** orthonormal bases, spectral theorem, tensor product spaces, trace class operators, Stone's theorem (one-parameter unitary groups ↔ self-adjoint generators)
- **Temporal note:** Stone's theorem connects one-parameter unitary groups to self-adjoint operators (Hamiltonians). This is the structural basis for time evolution in quantum mechanics: the Hamiltonian generates unitary time evolution via U(t) = exp(−iHt). Time here is parameterized by R (from REAL) and the evolution is unitary — time-reversal is an antiunitary operation, not forbidden by the Hilbert space structure.

### OA — Operator Algebras

- **Parameters:**
  - Type classification (structural): Type I, II_1, II_∞, III. Physics mostly uses Type I (bounded operators on Hilbert space) and Type III (local algebras in AQFT).
  - Factor structure (structural): factors (trivial center) vs. general von Neumann algebras.
- **Dependencies:**
  - HILB — logical. Operator algebras are algebras of operators on Hilbert spaces (or abstract C*-algebras represented on them via GNS).
  - RING — logical. Operator algebras are rings with additional structure (involution, norm).
- **Provides:** GNS construction, states as positive linear functionals, superselection sectors, KMS states (thermal equilibrium), modular theory (Tomita-Takesaki)
- **Temporal note:** The KMS condition characterizes thermal equilibrium states and encodes a relationship between time evolution and temperature: analytic continuation of the time parameter by iβ (inverse temperature). Tomita-Takesaki modular theory generates a "modular flow" that, in certain states, coincides with physical time evolution. These are structural connections between time and thermodynamics at the algebraic level.

### PATH — Path Integral

- **Parameters:**
  - Measure (convention/structural): not rigorously defined in general. Defined for Gaussian (free field) cases. Status of non-perturbative measure is an open problem.
  - Wick rotation (boundary): t → −iτ. Analytic continuation from Lorentzian to Euclidean signature. This is a transformation of temporal structure. The Euclidean path integral is better defined (positive-definite action) but the physical theory lives in Lorentzian signature. The rotation is invertible.
- **Dependencies:**
  - HILB — logical. The path integral computes matrix elements of the time evolution operator, which lives on a Hilbert space.
  - MAN — conventional. The path integral sums over field configurations on a manifold. But the configuration space could be specified differently (lattice, discrete, etc.).
  - REAL — logical. Integration theory (Lebesgue or otherwise) is required.
- **Provides:** propagators, partition functions, correlation functions, saddle-point / WKB approximation, instanton contributions
- **Temporal note:** **Second major temporal commitment.** The Wick rotation is a boundary parameter that transforms temporal structure. In Euclidean signature, "time" becomes a spatial dimension — the path integral treats all four dimensions symmetrically. The rotation back to Lorentzian signature reintroduces the time/space distinction. The path integral weight exp(iS) vs. exp(−S_E) encodes the phase structure that distinguishes propagation from diffusion. The Wick rotation is invertible, but the Euclidean theory does not distinguish "forward" from "backward" in the Euclideanized time direction — the Osterwalder-Schrader reflection positivity condition reconstructs this distinction upon continuation back to Lorentzian signature.

---

## Layer 7: Classical Field Theory

Lagrangian dynamics on spacetime. Gauge theory as geometry of connections.

### LAG — Lagrangian / Variational

- **Parameters:**
  - Lagrangian density (dynamical): the specific functional form. This is the core dynamical content of any field theory.
  - Spacetime signature (kinematic): inherited from MAN. Determines whether the action is real-valued (Lorentzian) or positive-definite (Euclidean).
- **Dependencies:**
  - MAN — logical. The Lagrangian is integrated over a manifold.
  - REAL — logical. The calculus of variations requires analysis.
- **Provides:** Euler-Lagrange equations of motion, conserved currents (Noether's theorem), symplectic structure on the space of solutions, energy-momentum tensor
- **Temporal note:** The Euler-Lagrange equations derived from a Lagrangian with Lorentzian signature are hyperbolic PDEs — they have a well-posed initial value formulation (Cauchy problem). This is where the distinction between initial data (on a spacelike surface) and time evolution (off that surface) becomes dynamically meaningful. The equations are time-symmetric: if φ(t,x) is a solution, so is φ(−t,x) (for T-invariant Lagrangians). The choice of which solution to use is not made here.

### GAUGE — Gauge Theory (Classical)

- **Parameters:**
  - Gauge group G (structural): the choice of Lie group for the principal bundle. Standard Model uses SU(3) × SU(2) × U(1). Alternatives: any compact Lie group; GUT groups SU(5), SO(10), E_6, E_8; the trivial group (no gauge symmetry).
  - Matter representations (structural): which representations of G the matter fields transform in.
  - Coupling constants (dynamical): the strengths of gauge interactions. These run with energy scale (see RENORM).
  - Gauge-fixing condition (convention): Lorenz gauge, Coulomb gauge, axial gauge, etc. Physical observables are gauge-invariant.
  - **Gribov region (structural — non-abelian only):** for non-abelian gauge groups (SU(2), SU(3)), gauge-fixing does not yield unique configurations. Gribov copies exist — physically equivalent configurations satisfying the same gauge condition, related by large gauge transformations. Practice restricts to the first Gribov horizon or the fundamental modular region. This is a parameter that takes a value; the justification for the standard choice is incomplete. Whether the choice affects physical observables (especially non-perturbative ones like confinement) is an active research question. Absent for abelian theories (U(1) has no Gribov copies). **Flagged for deep research.** See OQ3 in V2_NOTE.md.
- **Dependencies:**
  - CONN — logical. Gauge fields are connections on principal bundles.
  - LAG — logical. The Yang-Mills action is a Lagrangian functional of the connection.
  - REP — logical. Matter fields are sections of associated bundles in representations of G.
- **Provides:** gauge transformations, field strength tensor F_μν, minimal coupling (covariant derivative on matter fields), Yang-Mills equations, Bianchi identity, classical solutions (monopoles, instantons, vortices)
- **Temporal note:** **The Yang-Mills equations are time-symmetric for any gauge group.** Both retarded and advanced solutions are equally valid. The choice of boundary condition (retarded vs. advanced vs. time-symmetric) is not made at this layer — it is a parameter that belongs to the quantized theory or to cosmological boundary conditions. This is the structural root of the time-symmetry debt: the classical dynamics do not select a preferred temporal direction. The selection is deferred to QFT (Layer 8) where it enters via the iε prescription. **The theory at this layer contains the full consequences of time symmetry.** Higher layers assume the retarded propagator and build predictions on it. If the boundary conditions that select the retarded solution fail locally (e.g., in regimes where the absorber condition is not satisfied), the predictions of the higher layers change. The graph should be read with awareness that the retarded character assumed above this layer is contingent, not structural.

---

## Layer 8: Quantum Field Theory

Quantized fields, renormalization, anomaly structure.

### QFT — Field Quantization

- **Parameters:**
  - Regularization scheme (convention): dimensional regularization, Pauli-Villars, lattice, zeta function. Physical results are scheme-independent.
  - Operator ordering (convention): normal ordering, Weyl ordering. Affects finite renormalization counterterms.
  - Quantization method (structural): path integral (via PATH) or canonical (via HILB directly). These are believed to be equivalent but the equivalence is not proven in all cases.
  - **Vacuum state (boundary):** the Poincaré-invariant vacuum |Ω⟩ determined by the Wightman axioms and spectral condition. Practice assumes this value universally. Why the vacuum takes this value and not another (thermal state, squeezed state, Bunch-Davies in curved spacetime, a state with different analytic structure) is not derived from within the SM framework. The vacuum state is entangled with the iε prescription — the unique vacuum determines the Feynman propagator and vice versa. **Flagged for deep research:** is there a principled reason the vacuum takes this value, or is it an independent boundary condition received from cosmology? See OQ2 in V2_NOTE.md.
  - **iε sign (boundary):** +iε (standard) or −iε. This is the most consequential parameter in the Standard Model that is not visible in the Lagrangian. +iε selects the Feynman propagator: positive-frequency modes propagate forward in time, negative-frequency modes backward. −iε selects the time-reversed propagator. Both choices produce internally consistent, causal theories — with opposite causal arrows. The standard choice +iε is universal across all gauge sectors (enforced by the unique vacuum state and unitarity). Its physical justification varies by sector:
    - U(1) EM: justified by the Wheeler-Feynman absorber condition (cosmological boundary condition).
    - Gravity: partially justified (Penrose WCH, Hoyle-Narlikar; obstructed by gravitational transparency).
    - SU(2) weak: no sector-specific justification. May inherit from U(1) via electroweak unification above 246 GeV.
    - SU(3) strong: no sector-specific justification. Obstructed by confinement, self-interaction, and Gribov ambiguity.
    - Cross-sector: the shared vacuum state (Wightman axioms, spectral condition) enforces a single iε sign for all sectors simultaneously. Mixed prescriptions violate unitarity. See time-symmetry debt research (synthesis.md) for full analysis.
- **Dependencies:**
  - GAUGE — conventional. QFT can be formulated for non-gauge theories (scalar field theory, Yukawa theory). The Standard Model's use of gauge theory is a structural parameter, not a requirement of QFT.
  - HILB — logical. The state space of QFT is a Hilbert space (Fock space or otherwise).
  - PATH — conventional. The path integral is one quantization method. Canonical quantization is an alternative.
- **Provides:** Feynman diagrams, S-matrix, vacuum state |Ω⟩, particle interpretation (Fock space), propagators (contingent on iε — see below), crossing symmetry, spin-statistics theorem, CPT theorem
- **Contingent provisions:**
  - The causal propagator structure (Feynman propagator, retarded/advanced Green's functions, time-ordered products) depends on the iε boundary parameter. This is not determined by the QFT framework alone.
  - The vacuum state |Ω⟩ is unique (cluster property, Wightman axioms) given the iε prescription. Without it, the vacuum is underdetermined.
- **Temporal note:** **This is where time acquires a preferred direction.** The iε prescription breaks the time-reversal symmetry of the classical field equations. Prior to this layer, the dynamics are time-symmetric. After this layer, positive-energy states propagate forward and the causal arrow is fixed. The CPT theorem (proved at this layer) guarantees that the combined operation CPT is a symmetry even though C, P, and T individually need not be. The iε prescription's physical justification comes from outside the QFT framework — from cosmological boundary conditions (absorber condition, Hubble expansion). The graph is honest about receiving this input from outside its scope.

### RENORM — Renormalization

- **Parameters:**
  - Renormalization scheme (convention): MS-bar, on-shell, momentum subtraction. Physical observables are scheme-independent.
  - Renormalization scale μ (convention): the energy scale at which couplings are defined. Physical observables are μ-independent (by the renormalization group equation).
  - Counterterm structure (convention): determined by the scheme.
- **Dependencies:**
  - QFT — logical. Renormalization addresses divergences in QFT calculations.
  - CMPLX — logical. Dimensional regularization requires analytic continuation in the spacetime dimension (d → 4 − ε), which lives in C.
- **Provides:** running couplings, beta functions, anomalous dimensions, effective field theory framework, asymptotic freedom/safety, Landau poles
- **Temporal note:** The beta functions and running couplings are time-reversal invariant — they depend on the energy scale, not on the direction of time. Renormalization does not introduce new temporal structure beyond what QFT provides.

### ANOM — Anomaly Cancellation

- **Parameters:**
  - Fermion content (structural — constrained): not freely choosable. The fermion representations must satisfy Tr[T_a {T_b, T_c}] = 0 for all gauge generators. This is a constraint on the joint parameter space of SM_G and SM_F, enforced at this layer. The constraint is topological (index theorem) and algebraic (trace condition).
- **Dependencies:**
  - QFT — logical. Anomalies are quantum effects (one-loop exact).
  - REP — logical. The anomaly conditions involve traces over representation matrices.
  - CONN — logical. Anomalies are related to characteristic classes (index theorem, Atiyah-Singer).
- **Provides:** anomaly-free representations, index theorems, topological constraints on the fermion spectrum, 't Hooft anomaly matching
- **Temporal note:** Anomaly cancellation is time-reversal invariant. The constraints it imposes on the fermion spectrum do not depend on the direction of time.

---

## Layer 9: Standard Model

The specific structural configuration that matches observation.

### SM_G — SU(3) × SU(2) × U(1)

- **Parameters:**
  - Gauge group (structural): SU(3) × SU(2) × U(1)_Y. Alternatives: SU(5), SO(10), E_6, E_8 × E_8 (GUT/string embeddings); the trivial group (no gauge symmetry); any product of simple and abelian compact Lie groups.
  - Coupling constants at a reference scale (dynamical): g_3 (strong), g_2 (weak), g_1 (hypercharge). These are three independent parameters. Their values at the Z mass are measured. Whether they unify at a GUT scale is a structural question (they approximately do, for SUSY-SU(5)).
- **Dependencies:**
  - GAUGE — logical. The SM is a gauge theory.
  - ANOM — logical. The gauge group must admit anomaly-free fermion representations.
  - RENORM — logical. The theory must be renormalizable (or at least an effective field theory with controlled divergences).
- **Provides:** strong interaction (SU(3) color), weak interaction (SU(2) isospin), hypercharge interaction (U(1)_Y); gauge boson content: 8 gluons + W+, W−, W3 + B (before SSB) → 8 gluons + W+, W− + Z + γ (after SSB)
- **Temporal note:** The gauge group is time-reversal invariant. SU(3) × SU(2) × U(1) does not inherently distinguish past from future.

### SM_F — Three Fermion Generations

- **Parameters:**
  - Number of generations (structural): 3. Alternatives: any positive integer. Anomaly cancellation works per generation, so any N is consistent. Why N = 3 has no known structural derivation. (CP violation in the CKM matrix requires N ≥ 3, but this is a downstream consequence, not a justification.) The value 3 is one well-formed way of elaborating the logically prior elements; the counterfactuals (N = 1, 2, 4, ...) are equally well-formed. "Structural" may need disambiguation here — this is a parameter, not a derived quantity, but the subtype label doesn't distinguish between parameters with known derivations and those without. **Flagged for deep research.** See OQ4 in V2_NOTE.md.
  - Representation assignments (structural): per generation, the fermion fields transform as specific representations of SU(3) × SU(2) × U(1)_Y. These are tightly constrained by anomaly cancellation. The standard assignments (Q_L = (3,2,1/6), u_R = (3,1,2/3), d_R = (3,1,−1/3), L_L = (1,2,−1/2), e_R = (1,1,−1)) are one of a small number of anomaly-free configurations.
- **Dependencies:**
  - SM_G — logical. Fermion representations are defined relative to the gauge group.
  - REP — logical. The representation theory machinery is required.
  - ANOM — logical. Anomaly cancellation constrains the fermion content.
- **Provides:** quark fields (6 flavors × 3 colors × 2 chiralities), lepton fields (6 flavors × 2 chiralities), anomaly cancellation within each generation
- **Temporal note:** Fermion fields are Dirac or Weyl spinors. Under time reversal T, a Dirac spinor transforms nontrivially (T is antiunitary and involves complex conjugation of the spinor components). But the fermion content itself doesn't introduce temporal asymmetry — T invariance is a property of the Lagrangian, not the field content.

### SM_H — Higgs Mechanism / SSB

- **Parameters:**
  - Higgs potential parameters (dynamical): μ² (mass parameter, negative for SSB) and λ (quartic coupling, positive for stability). These determine the Higgs boson mass m_H = √(2λ)v and the vacuum expectation value v = √(−μ²/λ) ≈ 246 GeV.
  - Higgs representation (structural): complex scalar doublet (1,2,1/2) under SU(3) × SU(2) × U(1)_Y. Alternatives: triplet, singlet, multiple doublets (2HDM), composite (technicolor).
  - vev (dynamical): v ≈ 246 GeV. Sets the electroweak scale.
- **Dependencies:**
  - SM_G — logical. SSB requires a gauge symmetry to break.
  - LAG — logical. The Higgs potential is a Lagrangian.
- **Provides:** W± and Z boson masses (M_W = gv/2, M_Z = M_W/cos θ_W), photon as massless residual of SSB, Goldstone bosons (eaten by W±, Z), Higgs boson, fermion mass terms (via Yukawa coupling to the Higgs)
- **Temporal note:** The Higgs potential is time-reversal invariant. SSB itself does not break T. The electroweak phase transition (the cosmological event where the Higgs vev "turned on") is a thermal/cosmological event — it happened at a specific time in the universe's history but the Lagrangian is still T-symmetric.

### SM_Y — Yukawa Couplings and Mixing

- **Parameters:**
  - Yukawa coupling matrices (dynamical): 3 × 3 complex matrices Y_u, Y_d, Y_e (up-type quarks, down-type quarks, charged leptons). These contain far more parameters than are physical — most are absorbed by field redefinitions.
  - CKM matrix (dynamical): 3 angles + 1 complex phase (for 3 generations). The phase δ is the source of CP violation in the quark sector. For 2 generations, no phase exists and CP is conserved.
  - PMNS matrix (dynamical): 3 angles + 1 Dirac phase + (possibly) 2 Majorana phases. CP violation in the lepton sector is under experimental investigation (DUNE, Hyper-Kamiokande).
  - Neutrino mass mechanism (structural): unknown. Dirac masses (like other fermions), Majorana masses (lepton number violation), seesaw mechanism (Type I, II, III), or radiative generation. This is an open structural question.
- **Dependencies:**
  - SM_F — logical. Yukawa couplings couple fermion fields to the Higgs.
  - SM_H — logical. The Higgs vev converts Yukawa couplings into mass terms.
- **Provides:** fermion masses (hierarchical: m_t ≈ 173 GeV down to m_ν < 0.1 eV), flavor-changing charged currents (CKM), CP violation (CKM phase), neutrino oscillations (PMNS)
- **Contingent provisions:**
  - CP violation is a dynamical T violation: certain processes proceed at different rates under time reversal. But its observability is contingent on the iε prescription at QFT (Layer 8). Observable CP asymmetries arise from interference between weak phases (CKM) and strong phases (absorptive parts of loop diagrams, which trace back to iε). Without the pre-existing causal arrow from iε, CP violation produces no observable rate asymmetries. See Agent 3 report for the full argument (Donoghue-Menezes framework).
- **Temporal note:** **Dynamical T violation enters here** via the CKM complex phase. This is the only place in the Standard Model where the Lagrangian itself distinguishes past from future. But per the Agent 3 analysis, this dynamical T violation presupposes the kinematic time-asymmetry from the iε prescription (Layer 8). The logical order is: iε (boundary) → causal arrow → observable CP violation (dynamical). Not the reverse.

---

## Structural Observations (Updated for V2)

**Deepest dependency chain:** CL → FOL → ZFC → GRP → LIE → LIEA → REP → CONN → GAUGE → QFT → ANOM → SM_F (12 links). Unchanged from v1.

**Most constrained node:** ANOM. Takes representation theory and topology as input, outputs hard constraints on fermion content. The Standard Model's particle spectrum is one of a small number of anomaly-free configurations. This remains the structural realist's strongest card.

**Most consequential hidden parameter (new in v2):** The iε sign at QFT. It determines the causal structure of the entire theory, is invisible in the Lagrangian, is universal across all gauge sectors, and has a physical justification in only one sector (U(1) electromagnetism, via the absorber condition). Every node above QFT inherits this choice silently.

**Temporal structure chain (new in v2):**
1. MAN: time distinguished from space (metric signature parameter)
2. PATH: time analytically continued (Wick rotation parameter)
3. QFT: time given a preferred direction (iε boundary parameter)
4. SM_Y: certain processes distinguish past from future (CKM phase, presupposes iε)

Each step adds temporal commitment on top of the prior. The chain is: geometric distinction → analytic transformation → causal direction → dynamical asymmetry. Only the last is visible in the Lagrangian.

**Cross-layer dependencies to watch (updated):**
- CONN depends on FB (geometry) and LIEA (algebra) — unchanged.
- QFT depends on boundary conditions from outside the graph — new. The iε prescription connects QFT to cosmology (absorber condition, Hubble expansion, Penrose WCH) through a dependency the graph cannot currently represent internally.

**Fattest parametric nodes:** Layer 9, unchanged. "Why 3 generations?", "Why these coupling constants?", "Why SU(3) × SU(2) × U(1)?" remain structural coordinates with no known derivation.

**Conventional dependencies identified in v2 audit (new):** FOL→CL, TT→IL, CAT→ZFC, GRP→ZFC, TOP→ZFC, LIEA→LIE, QFT→GAUGE, QFT→PATH, PATH→MAN. These are disguised theory-construction parameters: choices of substrate that could be made differently.
