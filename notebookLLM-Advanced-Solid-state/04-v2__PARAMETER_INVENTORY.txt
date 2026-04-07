# Parameter Inventory — V2

Every choice in the dependency graph, classified by subtype. This is the complete inventory of the theory-construction parameter space.

## Parameter Subtypes

| Subtype | Meaning |
|---------|---------|
| axiom | Foundational choice with no prior constraints within the framework |
| structural | Choice of mathematical/physical structure; options constrained by upstream parameters |
| kinematic | Choice about the arena (dimension, signature, topology) |
| dynamical | Choice about equations of motion or interaction rules |
| boundary | Choice about initial/final conditions or propagator prescription; independent of dynamics |
| convention | Choice affecting description but not physics |

## Dependency Types

| Type | Meaning |
|------|---------|
| logical | Y cannot be formulated without X |
| conventional | Y is standardly built on X but alternatives exist |
| contingent | Y uses X's output only under conditions X doesn't guarantee |

---

## Layer 0: Logic

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P001 | Law of excluded middle | axiom | on (CL) | off (IL) | CL/IL |
| P002 | Explosion principle | axiom | on (CL) | off (paraconsistent) | CL |
| P003 | Underlying logic for FOL | axiom | classical (CL) | intuitionistic (IL) | FOL |
| P004 | Sort structure | structural | single-sorted | many-sorted | FOL |
| P005 | Quantification order | structural | first-order | second-order, higher-order | FOL |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D001 | CL → FOL | conventional | FOL can be built on IL |

## Layer 1: Foundations

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P006 | Axiom of choice | axiom | included (ZFC) | excluded (ZF) | ZFC |
| P007 | Continuum hypothesis | axiom | independent | assumed/denied | ZFC |
| P008 | Foundation axiom | axiom | included | excluded (non-well-founded sets) | ZFC |
| P009 | Univalence axiom | axiom | off | on (HoTT) | TT |
| P010 | Impredicativity | structural | varies | varies | TT |
| P011 | Universe levels | structural | cumulative | non-cumulative | TT |
| P012 | Category size | structural | large allowed | small only | CAT |
| P013 | Enrichment base | structural | Set | Ab, Top, Cat | CAT |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D002 | CL → ZFC | logical | ZFC is formulated in classical FOL |
| D003 | FOL → ZFC | logical | ZFC axioms are first-order sentences |
| D004 | IL → TT | conventional | Type theories with classical logic exist |
| D005 | ZFC → CAT | conventional | Cat can be founded on TT, NBG, ETCS |

## Layer 2: Core Algebra

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P014 | Group commutativity | structural | unrestricted | abelian only | GRP |
| P015 | Group finiteness | structural | unrestricted | finite only | GRP |
| P016 | Ring commutativity | structural | unrestricted | commutative only | RING |
| P017 | Field characteristic | structural | 0 (for physics) | prime p | RING |
| P018 | Base field | structural | R and C | finite fields, p-adic | LA |
| P019 | Vector space dimension | structural | unrestricted | finite, countable | LA |
| P020 | Inner product signature | kinematic | unrestricted at this layer | positive-definite, indefinite, degenerate | LA |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D006 | ZFC → GRP | conventional | Group theory needs a foundational substrate; ZFC is standard |
| D007 | GRP → RING | logical | Rings are abelian groups with multiplication |
| D008 | RING → LA | logical | Vector spaces are modules over fields |

## Layer 3: Topology and Analysis

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P021 | Separation axioms | structural | Hausdorff (T2) | T0, T1, T3, T4 | TOP |
| P022 | Compactness conditions | structural | paracompact (for manifolds) | compact, locally compact | TOP |
| P023 | Completeness of R | axiom | Dedekind complete | constructive reals | REAL |
| P024 | Measure | structural | Lebesgue | Borel, Hausdorff | REAL |
| P025 | Riemann surface structure | structural | varies | varies | CMPLX |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D009 | ZFC → TOP | conventional | Topology can be developed constructively |
| D010 | ZFC → REAL | logical | Dedekind construction requires powersets |
| D011 | TOP → REAL | logical | Metric topology is foundational |
| D012 | REAL → CMPLX | logical | C is constructed from R |

## Layer 4: Lie Theory

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P026 | Lie group compactness | structural | both compact and noncompact | compact only, noncompact only | LIE |
| P027 | Lie group connectedness | structural | identity component | full group | LIE |
| P028 | Simple vs. semisimple | structural | unrestricted | simple only | LIE |
| P029 | Lie algebra rank | structural | varies by application | any non-negative integer | LIEA |
| P030 | Lie algebra type | structural | A, B, C, D for physics | E, F, G (exceptional) | LIEA |
| P031 | Real form | structural | compact for internal symmetries | split, other | LIEA |
| P032 | Representation dimension | structural | varies | any positive integer | REP |
| P033 | Highest weight | structural | varies | any dominant integral weight | REP |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D013 | GRP → LIE | logical | Lie groups are groups |
| D014 | TOP → LIE | logical | Lie groups are topological spaces |
| D015 | REAL → LIE | logical | Smooth structure requires R |
| D016 | LIE → LIEA | conventional | Lie algebras can be defined purely algebraically |
| D017 | LA → LIEA | logical | Lie algebras are vector spaces with bracket |
| D018 | LIEA → REP | logical | Representations are Lie algebra homomorphisms |
| D019 | LA → REP | logical | Target space is a vector space |

## Layer 5: Differential Geometry

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P034 | Spacetime dimension | kinematic | 4 | 2, 3, 5, ..., 10, 11, 26 | MAN |
| P035 | Orientability | kinematic | orientable | non-orientable | MAN |
| P036 | **Metric signature** | **kinematic** | **(−,+,+,+) Lorentzian** | **(+,+,+,+) Euclidean; (−,−,+,...) ultrahyperbolic; degenerate** | **MAN** |
| P037 | Structure group | structural | U(1), SU(2), SU(3), Spin(1,3) | any Lie group | FB |
| P038 | Fiber type | structural | principal, vector, associated | spinor, tensor | FB |
| P039 | Bundle topology (characteristic classes) | structural | trivial for most local physics | nontrivial (monopoles, instantons) | FB |
| P040 | Gauge orbit representative | convention | Lorenz gauge, Coulomb gauge, etc. | any gauge-fixing condition | CONN |
| P041 | Curvature constraints | structural | Yang-Mills (extremal) | flat, self-dual, anti-self-dual | CONN |

**P036 is the first parameter where temporal structure enters the graph.** The choice of one negative eigenvalue in the metric distinguishes a "timelike" direction from three "spacelike" directions. At this layer the distinction is geometric only — no preferred direction along the timelike dimension.

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D020 | TOP → MAN | logical | Manifolds are topological spaces |
| D021 | REAL → MAN | logical | Charts map to R^n |
| D022 | LA → MAN | logical | Tangent spaces are vector spaces |
| D023 | MAN → FB | logical | Bundles need a base manifold |
| D024 | GRP → FB | logical | Principal bundles need a structure group |
| D025 | FB → CONN | logical | Connections live on bundles |
| D026 | LIEA → CONN | logical | Connections are Lie-algebra-valued forms |

## Layer 6: Functional Analysis and Quantization

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P042 | Hilbert space separability | structural | separable | non-separable | HILB |
| P043 | Hilbert space dimension | structural | infinite (QFT) | finite (quantum info) | HILB |
| P044 | Operator algebra type | structural | Type I (standard) | Type II, Type III (AQFT) | OA |
| P045 | Factor structure | structural | factors | general von Neumann algebras | OA |
| P046 | Path integral measure | structural | Gaussian (free fields) | non-perturbative (open problem) | PATH |
| P047 | **Wick rotation** | **boundary** | **t → −iτ (standard)** | **no rotation (stay Lorentzian)** | **PATH** |

**P047 is the second major temporal parameter.** Wick rotation transforms temporal structure: in Euclidean signature, all four dimensions are equivalent and there is no distinction between "forward" and "backward" in the Euclideanized time direction. The Osterwalder-Schrader reconstruction theorem recovers the Lorentzian time-ordered structure upon continuation back.

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D027 | LA → HILB | logical | Hilbert spaces are inner product spaces |
| D028 | REAL → HILB | logical | Completeness requires analysis |
| D029 | TOP → HILB | logical | Norm topology |
| D030 | HILB → OA | logical | Operators act on Hilbert spaces |
| D031 | RING → OA | logical | Operator algebras are rings |
| D032 | HILB → PATH | logical | Path integral computes Hilbert space amplitudes |
| D033 | MAN → PATH | conventional | Configuration space can be non-manifold (lattice, etc.) |
| D034 | REAL → PATH | logical | Integration theory required |

## Layer 7: Classical Field Theory

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P048 | Lagrangian density | dynamical | SM Lagrangian | any Lorentz-invariant local functional | LAG |
| P049 | Spacetime signature (inherited) | kinematic | (−,+,+,+) | from MAN P036 | LAG |
| P050 | Gauge group G | structural | SU(3)×SU(2)×U(1) | any compact Lie group; GUT groups; trivial | GAUGE |
| P051 | Matter representations | structural | SM assignments | any anomaly-free set | GAUGE |
| P052 | Coupling constants | dynamical | g_3, g_2, g_1 at M_Z | any positive real values | GAUGE |
| P053 | Gauge-fixing condition | convention | Lorenz gauge | Coulomb, axial, light-cone, etc. | GAUGE |
| **P079** | **Gribov region** | **structural** | **first Gribov horizon** | **fundamental modular region, other** | **GAUGE (non-abelian only)** |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D035 | MAN → LAG | logical | Integration over manifold |
| D036 | REAL → LAG | logical | Calculus of variations |
| D037 | CONN → GAUGE | logical | Gauge fields are connections |
| D038 | LAG → GAUGE | logical | Yang-Mills action is a Lagrangian |
| D039 | REP → GAUGE | logical | Matter fields are representation sections |

## Layer 8: Quantum Field Theory

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P054 | Regularization scheme | convention | dim. reg. | Pauli-Villars, lattice, zeta | QFT |
| P055 | Operator ordering | convention | normal ordering | Weyl, anti-normal | QFT |
| P056 | Quantization method | structural | path integral | canonical, BRST, stochastic | QFT |
| **P057** | **iε sign** | **boundary** | **+iε** | **−iε** | **QFT** |
| **P078** | **Vacuum state** | **boundary** | **Poincaré-invariant |Ω⟩** | **Bunch-Davies, thermal, squeezed, other** | **QFT** |
| P058 | Renormalization scheme | convention | MS-bar | on-shell, MOM | RENORM |
| P059 | Renormalization scale μ | convention | M_Z ≈ 91.2 GeV | any energy scale | RENORM |
| P060 | Counterterm structure | convention | determined by scheme | — | RENORM |
| P061 | Fermion content (constrained) | structural | SM assignments | any anomaly-free set | ANOM |

**P057 is the most consequential parameter in the graph that was invisible in V1.** It determines the causal structure of the entire theory. It is universal across all gauge sectors. Its physical justification is sector-dependent and incomplete — see the time-symmetry debt research.

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D040 | GAUGE → QFT | conventional | QFT doesn't require gauge theory |
| D041 | HILB → QFT | logical | State space |
| D042 | PATH → QFT | conventional | Canonical quantization is an alternative |
| D043 | QFT → RENORM | logical | Renormalization addresses QFT divergences |
| D044 | CMPLX → RENORM | logical | Dim. reg. uses complex analysis |
| D045 | QFT → ANOM | logical | Anomalies are quantum effects |
| D046 | REP → ANOM | logical | Anomaly conditions involve representation traces |
| D047 | CONN → ANOM | logical | Index theorem connects anomalies to topology |

## Layer 9: Standard Model

| ID | Parameter | Subtype | Standard Value | Alternatives | Node |
|----|-----------|---------|---------------|-------------|------|
| P062 | Gauge group | structural | SU(3)×SU(2)×U(1)_Y | SU(5), SO(10), E_6, E_8×E_8, trivial | SM_G |
| P063 | g_3 (strong coupling) | dynamical | ≈ 1.22 at M_Z | any positive real | SM_G |
| P064 | g_2 (weak coupling) | dynamical | ≈ 0.65 at M_Z | any positive real | SM_G |
| P065 | g_1 (hypercharge coupling) | dynamical | ≈ 0.36 at M_Z | any positive real | SM_G |
| P066 | Number of generations | structural | 3 | any positive integer (anomaly-free per generation) | SM_F |
| P067 | Fermion representation assignments | structural | SM assignments | any anomaly-free set for given G | SM_F |
| P068 | Higgs μ² | dynamical | negative (SSB occurs) | positive (no SSB, all gauge bosons massless) | SM_H |
| P069 | Higgs λ (quartic coupling) | dynamical | ≈ 0.13 | any positive real (stability) | SM_H |
| P070 | Higgs representation | structural | (1,2,1/2) doublet | singlet, triplet, 2HDM, composite | SM_H |
| P071 | vev | dynamical | ≈ 246 GeV | determined by μ² and λ | SM_H |
| P072 | Yukawa matrices (Y_u, Y_d, Y_e) | dynamical | measured values | any complex 3×3 matrices | SM_Y |
| P073 | CKM angles (θ_12, θ_13, θ_23) | dynamical | measured values | any values in [0, π/2] | SM_Y |
| P074 | CKM phase δ | dynamical | ≈ 1.2 rad | any value in [0, 2π); 0 = no CP violation | SM_Y |
| P075 | PMNS angles | dynamical | measured values | any values | SM_Y |
| P076 | PMNS phases | dynamical | under investigation | any values | SM_Y |
| P077 | Neutrino mass mechanism | structural | unknown | Dirac, Majorana, seesaw (I/II/III), radiative | SM_Y |

| Dependency | From → To | Type | Notes |
|------------|-----------|------|-------|
| D048 | GAUGE → SM_G | logical | SM is a gauge theory |
| D049 | ANOM → SM_G | logical | Anomaly freedom required |
| D050 | RENORM → SM_G | logical | Renormalizability required |
| D051 | SM_G → SM_F | logical | Fermion reps defined relative to G |
| D052 | REP → SM_F | logical | Representation theory machinery |
| D053 | ANOM → SM_F | logical | Anomaly cancellation constrains content |
| D054 | SM_G → SM_H | logical | SSB requires a gauge symmetry |
| D055 | LAG → SM_H | logical | Higgs potential is a Lagrangian |
| D056 | SM_F → SM_Y | logical | Yukawa couplings couple fermions to Higgs |
| D057 | SM_H → SM_Y | logical | vev converts Yukawa couplings to masses |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total parameters | 79 |
| — axiom | 10 |
| — structural | 37 |
| — kinematic | 5 |
| — dynamical | 16 |
| — boundary | 3 |
| — convention | 8 |
| Total dependencies | 57 |
| — logical | 46 |
| — conventional | 11 |
| — contingent | 0 explicit (contingent provisions noted at QFT, GAUGE, SM_Y) |

## Temporal Structure Parameters

The following parameters introduce or transform temporal structure. Listed in order of first appearance:

| ID | Parameter | Node | Layer | What It Does to Time |
|----|-----------|------|-------|---------------------|
| P020 | Inner product signature | LA | 2 | Makes indefinite signature available (no temporal interpretation yet) |
| P036 | Metric signature | MAN | 5 | **Distinguishes time from space** (one negative eigenvalue) |
| P047 | Wick rotation | PATH | 6 | **Transforms temporal structure** (Lorentzian ↔ Euclidean) |
| P057 | **iε sign** | **QFT** | **8** | **Gives time a preferred direction** (breaks t → −t symmetry) |
| P074 | CKM phase δ | SM_Y | 9 | Introduces dynamical T violation (presupposes P057) |

**The chain of temporal commitments is: P036 → P047 → P057 → P074. Each builds on the prior. Only P057 breaks time-reversal symmetry. P074's T violation is observable only in the presence of P057.**

## Underspecified or Open Parameters

| ID | Parameter | Issue |
|----|-----------|-------|
| P046 | Path integral measure | Not rigorously defined for interacting QFT. Open problem. |
| P057 | iε sign | Physical justification incomplete. Sector-dependent. See time-symmetry debt research. Flagged for deep research. |
| P066 | Number of generations | No known derivation. Why 3? Counterfactuals well-formed. Flagged for deep research (OQ4). |
| P068/P069 | Higgs μ², λ | No derivation of values. Hierarchy problem (why is μ² so much smaller than the Planck scale?). |
| P072 | Yukawa matrices | No derivation of the mass hierarchy. 6 orders of magnitude unexplained. |
| P077 | Neutrino mass mechanism | Unknown. Major open question. |
| P078 | Vacuum state | Practice assumes Poincaré-invariant |Ω⟩. No derivation of why this value. Flagged for deep research (OQ2). |
| P079 | Gribov region | Practice restricts to first Gribov horizon. Justification incomplete. Non-abelian only. Flagged for deep research (OQ3). |

## Parameters Not in V1 (Added in V2)

| ID | Parameter | Node | Why It Was Missing |
|----|-----------|------|--------------------|
| P057 | iε sign | QFT | Entered the theory silently as a quantization convention. Not visible in the Lagrangian. Identified by the time-symmetry debt investigation as the most consequential hidden parameter. |
| P047 | Wick rotation (reclassified) | PATH | Listed in v1 under PATH "parametric" but not typed as a boundary parameter or connected to the temporal structure chain. |
| P078 | Vacuum state | QFT | Practice assumes Poincaré-invariant vacuum without declaring it as a parameter. Entangled with P057. |
| P079 | Gribov region | GAUGE | Practice restricts to first Gribov horizon for non-abelian theories without declaring it as a parameter. |
