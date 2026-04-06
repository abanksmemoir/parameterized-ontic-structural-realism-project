# Synthesis: The Time-Symmetry Debt Across the Standard Model

## Overview

This document synthesizes findings from five parallel research investigations into the "time-symmetry debt" — the fact that every gauge sector of the Standard Model uses the retarded propagator (encoded via the Feynman iε prescription), but only one sector (U(1) electromagnetism) has a structural account of why. Each investigation surveyed the academic literature on a specific face of this problem. The synthesis identifies which sectors have resolved their time-symmetry debt, whether the five faces are independent or connected, the most promising leads, and the specific papers the POSR structural graph needs to incorporate.

---

## 1. Sector-by-Sector Status of Time-Symmetry Accounts

### U(1) Electromagnetism — RESOLVED (via absorber condition)

The Wheeler-Feynman absorber theory (1945, 1949) provides a complete structural account. The underlying dynamics (Maxwell's equations) are time-symmetric. The retarded propagator is selected by a cosmological boundary condition: the universe contains sufficient future absorbers to cancel advanced radiation. This has been extended to quantum electrodynamics by Davies (1971-72), and connected to cosmological expansion by Cramer (1983) and Yurova-Yurov-Yurov (2023). The electromagnetic sector is the benchmark against which all other sectors are measured.

**Status: Debt discharged.**

### Gravity (linearized GR) — PARTIALLY ADDRESSED (competing mechanisms, none complete)

Gravity is the sector that most naturally *should* admit an absorber condition: the graviton is massless, gravity is long-range, and the linearized Einstein equations are time-symmetric. Three candidate mechanisms exist:

1. **Hoyle-Narlikar gravitational absorber theory** (1964-1974): The most complete attempt, using a direct-particle-interaction framework with half-retarded/half-advanced propagation. However, it faces a seemingly fatal obstacle: the universe is nearly *transparent* to gravitational radiation (interaction cross-section ~10⁻⁶⁵ cm²), making future absorption physically impossible. Hawking (1965) showed it diverges in expanding universes, though cosmic acceleration may partially resolve this.

2. **Penrose's Weyl curvature hypothesis** (1979): Proposes a *past* boundary condition (vanishing Weyl tensor at the Big Bang) rather than a future-absorber mechanism. This avoids the transparency problem but shifts the explanatory mechanism from future absorption to initial conditions. The connection to retarded gravitational wave dominance has not been rigorously established.

3. **Cosmological expansion** (Gold-Wheeler-Yurova et al.): The Hubble friction term selects retarded propagation for free fields in FLRW spacetime. Applicable in principle to gravity but not worked out for the full nonlinear theory.

Blanchet and Damour (1993) rigorously demonstrated that the time-asymmetry of gravitational radiation enters through boundary conditions (retarded propagator choice), not through the dynamics — confirming that the debt exists and is structural.

**Status: Debt acknowledged; three partial accounts exist; none is complete. The transparency paradox (the sector best suited for an absorber mechanism is where it fails) is the sharpest version of the time-symmetry debt.**

### SU(2) Weak — UNADDRESSED (no structural account; CP violation is irrelevant)

No absorber-type mechanism has been proposed for the weak sector. The W and Z bosons are massive (~80-91 GeV) with range ~10⁻¹⁸ m, precluding propagation to cosmological absorbers. Agent 3's investigation definitively establishes that:

- **CP violation cannot substitute for the absorber condition.** Dynamical T violation from the CKM matrix phase *presupposes* the iε prescription — observable CP-violating effects require interference between weak phases (CKM) and strong phases (from the propagator's causal structure). CP violation is downstream of the propagator choice; it cannot explain it.
- CP violation operates at the level of the Lagrangian (dynamics), not boundary conditions. The absorber condition is a boundary condition.
- The weak sector's T violation and the propagator's time-asymmetry are "logically distinct but physically entangled" — related only in that the former presupposes the latter.

**Status: Debt fully outstanding. The most prominent candidate explanation (CP/T violation) is ruled out as structurally irrelevant.**

### SU(3) Strong — UNADDRESSED (compounded by confinement, self-interaction, and Gribov ambiguity)

No absorber condition has been proposed for QCD. The obstacles are the most severe of any sector:

1. **Gluon self-interaction and nonlinearity** prevent construction of a Fokker-type direct-action functional (the foundation of Wheeler-Feynman theory). The gluon field has independent degrees of freedom that cannot be eliminated.
2. **Color confinement** prevents gluons from propagating beyond ~1 fm, precluding cosmological-scale absorption.
3. **The Gribov ambiguity** may obstruct the construction of unique retarded and advanced Green's functions in a gauge-invariant way.
4. **Topological vacuum structure** (θ-vacua, instantons) introduces additional subtleties in time-reversal symmetry with no EM analog.

The strong sector has θ ≈ 0 (strong CP problem), meaning it is T-invariant at the dynamical level. This makes the propagator selection the *only* source of time-asymmetry in QCD — a "purer" version of the debt than in the weak sector.

**Status: Debt fully outstanding with the most severe mathematical obstacles.**

---

## 2. Are the Five Faces Independent or Connected?

**They are deeply connected.** The five investigations converge on a unified picture with three layers:

### Layer 1: The Global Constraint (Agent 4)

The strongest finding across all five reports is that **the Standard Model has a single vacuum state, and the Feynman iε prescription is a single global choice, not an independent choice per gauge sector.** This follows from:

- The **Wightman axioms**: a unique Poincaré-invariant vacuum and the spectral condition (energy positivity) together determine the propagator for all fields simultaneously.
- The **Osterwalder-Schrader theorem**: Euclidean path integrals automatically encode the Feynman iε for all fields; analytic continuation to Minkowski space yields a uniform prescription.
- **Unitarity**: mixed propagator prescriptions (e.g., retarded for photons, symmetric for gluons) would violate unitarity in any Feynman diagram containing quark loops with both electromagnetic and strong vertices.
- **Shared matter fields**: quarks carry charges under all three gauge groups. A single quark propagator connects to both photon and gluon vertices with the same iε. There is no consistent way to give the quark a different causal structure depending on which gauge boson it couples to.

**Implication:** The time-symmetry debt is not five independent problems — it is one problem with one answer that must apply to all sectors simultaneously. If any mechanism justifies the retarded propagator in one sector, it automatically justifies it in all sectors (via vacuum uniqueness), provided the mechanism is connected to the vacuum state.

### Layer 2: The Early Universe Epoch (Agents 1, 2, 4)

All three reports on non-electromagnetic sectors converge on the same observation: **the obstacles to extending the absorber condition to non-abelian sectors are temperature-dependent and vanish in the early universe.**

- Above the **electroweak symmetry-breaking scale** (~246 GeV, ~10⁻¹² s after Big Bang): all four electroweak gauge bosons were massless and long-range. The absorber condition could operate for the entire SU(2)×U(1) sector.
- Above the **QCD deconfinement transition** (~170 MeV, ~10⁻⁵ s after Big Bang): gluons were deconfined and propagated freely. The confinement obstacle vanished.
- During both epochs, the universe was in **thermal equilibrium**, and the **KMS condition** enforced uniform propagator structure across all sectors.

The "early universe synthesis" (independently constructed by Agents 2 and 4) is the most promising unified mechanism: during the earliest epoch, all gauge bosons were massless, deconfined, and long-range, so both absorber-type and cosmological-expansion mechanisms could select the retarded propagator universally. The retarded boundary condition, once established, would persist through subsequent phase transitions.

**Critical gap:** Whether boundary conditions on propagator pole structure actually survive phase transitions (electroweak symmetry breaking, QCD confinement) is **assumed, not proven.** This is the single most important open question identified by the research.

### Layer 3: The Asymmetry of Explanatory Mechanisms (Agents 3, 5)

The two faces that seem most "different" — CP violation (Agent 3) and gravitational absorption (Agent 5) — are both connected to the core problem but in asymmetric ways:

- **CP violation is downstream.** It presupposes the propagator choice and cannot explain it. This rules out one intuitively appealing candidate and clarifies the logical structure: boundary conditions come first, dynamical T violation is built on top of them.
- **Gravity faces a transparency paradox.** The sector best suited for an absorber mechanism (massless, long-range) is precisely where it fails, because the universe is transparent to gravitational radiation. This forces gravity toward a *past* boundary condition (Penrose's WCH) rather than a future-absorber mechanism, suggesting that past and future boundary conditions may both be needed to close the full account.

---

## 3. Most Promising Leads for Resolving Open Questions

### Lead 1: Prove boundary condition persistence through phase transitions
**Priority: Highest.** The early universe synthesis is the strongest available argument for universal propagator selection, but it rests on the unproven assumption that the retarded boundary condition survives the electroweak and QCD phase transitions. A proof (or disproof) would either close the debt or reveal it as deeper than currently understood.

### Lead 2: Extend Yurova-Yurov to interacting and gauge fields
The Yurova-Yurov-Yurov (2023) mechanism (Hubble friction shifts Green's function poles) is clean and gauge-sector-independent for free fields. Extending it to:
- Gauge field propagators (not just matter fields)
- Interacting fields with self-energy corrections
- The non-perturbative confining regime of QCD
would either establish or falsify cosmological expansion as a universal selection mechanism.

### Lead 3: The Schwinger-Keldysh formalism as implicit absorber theory
The SK (closed-time-path) formalism uses both forward and backward time contours, naturally yields retarded propagators, and applies to non-abelian gauge theories. No one has interpreted its backward contour as encoding the response of future absorbers. This is a concrete, unexplored research direction that could bridge the Wheeler-Feynman tradition and modern non-equilibrium QFT.

### Lead 4: Formalize the shared-vacuum unitarity argument
Agent 4 constructs an argument that mixed propagator prescriptions across gauge sectors would violate unitarity (via quark loops with both EM and QCD vertices). This argument has **never been explicitly made in the literature** despite following directly from standard QFT principles. Formalizing it would constitute a proof that propagator selection is a single global problem.

### Lead 5: Connect Penrose's WCH to retarded gravitational radiation
The Weyl curvature hypothesis imposes a past boundary condition on the gravitational field. Whether this mathematically implies dominance of retarded gravitational waves has never been rigorously demonstrated. Proving this connection would add gravity as a second sector (alongside EM) where the debt is structurally discharged — via a past rather than future boundary condition.

### Lead 6: Classical time-symmetric Yang-Mills solutions
No one has constructed the half-retarded + half-advanced solution for the Yang-Mills equations with sources. This is the non-abelian analog of the *first step* in the Wheeler-Feynman program (done for EM in 1945). Even if the full absorber program can't be carried out for non-abelian fields, knowing the structure of time-symmetric Yang-Mills solutions would clarify what's at stake.

---

## 4. Papers and Results for the POSR Structural Graph

The following papers and results should be incorporated as nodes, edges, or annotations in the project's structural graph of time-symmetry across gauge sectors:

### Foundational Framework
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Wheeler & Feynman (1945, 1949) | Absorber condition for U(1) — structural selection of retarded propagator | Root node: the benchmark mechanism |
| Donoghue & Menezes (2019, 2020) | Arrow of causality from iε prescription; the sign choice is conventional, not derived | Formalizes the debt: iε is undeclared assumption in every sector |
| Streater & Wightman (1964); Haag (1996) | Wightman axioms: single vacuum determines all propagators | Constraint node: propagator selection is a global, not per-sector, property |

### Cosmological Mechanisms
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Yurova, Yurov & Yurov (2023) | Hubble expansion selects retarded propagator for free fields of any mass/spin | Best available sector-agnostic mechanism (but free fields only) |
| Cramer (1983) | Boundary condition at Big Bang singularity produces retarded radiation; mentions weak sector | Earliest extension of absorber logic beyond pure EM |
| Castagnino & Lombardi (2003-2009) | Global geometrical arrow of time as non-entropic spacetime property | Alternative framework: time-asymmetry as geometric, not thermodynamic |

### Non-Abelian Sector
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Kosyakov (1994-2007) | Exact retarded solutions for classical SU(N) Yang-Mills | Only classical non-abelian retarded solutions in literature; no advanced solutions exist |
| Fischer et al. (2024/2025) | Causal structure of quark propagator via spectral Dyson-Schwinger | QCD's own dynamics enforce standard causal propagator structure |
| Buzzegoli (2025) | KMS conditions for all gauge sectors including ghosts | Thermal equilibrium enforces uniform propagator structure universally |

### CP Violation and T Violation
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Donoghue & Menezes (2020) [§ on CP] | Observable CP violation requires interference of weak phases with iε-derived strong phases | Proves CP violation presupposes propagator choice — eliminates a candidate explanation |
| Carroll (2010, 2012) | T violation is not the arrow of time | Conceptual clarification: dynamical T violation ≠ propagator time-asymmetry |

### Gravitational Sector
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Hoyle & Narlikar (1964-1974) | Gravitational absorber theory (direct-particle-interaction) | Most complete gravitational attempt; fails due to transparency |
| Blanchet & Damour (1993) | Time-asymmetry of gravitational radiation is structural (from boundary conditions) | Confirms the debt exists for gravity specifically |
| Penrose (1979) | Weyl curvature hypothesis: past boundary condition on gravitational field | Alternative to future-absorber: past boundary selects retarded radiation |
| Duda (2025) | First experimental test proposal (LIGO data) for retarded vs. advanced gravitational waves | Only proposed empirical test of the gravitational time-symmetry assumption |
| Dyson (2012); Rothman & Boughn (2006) | Universe is transparent to gravitational radiation | Establishes why the absorber mechanism fails for gravity |

### Cross-Sector Transmission
| Paper | Contribution | Graph Role |
|-------|-------------|------------|
| Osterwalder & Schrader (1973) | Euclidean path integral automatically encodes Feynman iε for all fields | Formal mechanism for uniform propagator selection |
| Epstein & Glaser (1973); Grigore (2000s) | Causal perturbation theory: time-ordering axioms apply uniformly to all sectors | Causality axioms are sector-agnostic |
| Visser (2022) | iε prescription as complex metric deformation of Minkowski spacetime | Geometric reinterpretation connecting propagator to spacetime itself |
| Hartle & Hawking (1983) | No-boundary proposal: Euclidean path integral defines the wave function of the universe | If correct, propagator choice is uniform across all sectors by construction |
| Nayeri (2026) | Inflationary branch decoherence: expanding branches become classical within ~0.5 e-folds | Dynamical mechanism selecting expanding (retarded) cosmological histories |

---

## 5. The Architecture of the Debt

The five investigations reveal a three-tier structure:

```
TIER 1 — COSMOLOGICAL BOUNDARY CONDITION
  Penrose WCH / Hartle-Hawking no-boundary / expanding universe
  ↓ (sets initial conditions for all of spacetime)

TIER 2 — VACUUM STATE + SPECTRAL CONDITION
  Single vacuum |Ω⟩ for the full Standard Model
  Wightman axioms → unique Feynman propagator for all fields
  ↓ (uniform iε prescription across all gauge sectors)

TIER 3 — SECTOR-SPECIFIC MECHANISMS
  U(1) EM:  Wheeler-Feynman absorber condition  ✓ RESOLVED
  Gravity:  Hoyle-Narlikar / Penrose WCH        ~ PARTIAL
  SU(2):   (nothing)                             ✗ OPEN
  SU(3):   (nothing)                             ✗ OPEN
```

The key insight is that Tier 2 already guarantees uniformity — if the propagator is justified anywhere, it's justified everywhere, because there is only one vacuum. The real question is at Tier 1: **what cosmological boundary condition selects the vacuum state that yields the Feynman propagator rather than its time-reverse?**

The Wheeler-Feynman absorber condition provides a Tier 3 answer for electromagnetism that is physically satisfying but sector-specific. What is needed is either:

(a) **A Tier 1 answer** that works for all sectors simultaneously (cosmological expansion, Penrose WCH, or Hartle-Hawking), or

(b) **A Tier 2 proof** that the vacuum structure of the Standard Model, combined with any one sector's structural account, necessarily implies the same account for all sectors (via the shared-vacuum/unitarity argument).

Path (b) is closer to being achieved: the pieces exist in the literature but have never been assembled into a single argument.

---

## 6. Conclusion

The time-symmetry debt is real, significant, and largely unrecognized. The retarded propagator is the most silently-imposed assumption in the Standard Model — selected identically in every gauge sector but structurally justified only in electromagnetism. The five faces of the problem are not independent: they are projections of a single question about the cosmological boundary condition and vacuum state of the universe.

The most important finding is negative: **CP violation cannot help.** The most important finding is positive: **the shared vacuum state means the debt, if paid in any sector, is paid in all.** The most important open question is: **do boundary conditions on propagator pole structure survive phase transitions?**

The POSR project should register the time-symmetry debt as a structural feature of the Standard Model that connects cosmology, QFT foundations, and the gauge structure of particle physics. The absorber condition is not merely a curiosity of classical electrodynamics — it is the only existing structural answer to a question that every gauge sector faces.
