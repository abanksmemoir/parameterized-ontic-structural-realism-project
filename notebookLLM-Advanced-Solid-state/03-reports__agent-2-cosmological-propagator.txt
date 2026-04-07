# Agent 2 Report: Cosmological Selection of the Retarded Propagator

## Central Question

Can the cosmological expansion of the universe provide a universal mechanism for selecting the retarded propagator across all gauge sectors — not just electromagnetism (U(1)) but also the weak (SU(2)) and strong (SU(3)) interactions?

---

## Executive Summary

The literature contains one direct attempt to derive the retarded propagator from cosmological expansion for quantum fields generally — the Yurova-Yurov-Yurov (2023) paper in *Universe*. This paper succeeds in showing that the Hubble expansion generates a small imaginary contribution to the effective mass of any quantum field propagating in FLRW spacetime, which shifts the Green's function poles into the lower half of the complex frequency plane, thereby mathematically selecting the retarded propagator via contour integration. However, the derivation applies only to **free fields** and does not address interactions, renormalization, confinement, or the specific complications of massive gauge bosons. Outside this paper, the literature on cosmological propagator selection is dominated by the electromagnetic case (Wheeler-Feynman absorber theory and its extensions), with no systematic treatment of the non-abelian sectors. The question therefore remains substantially open: the mechanism is suggestive and mathematically clean for free fields, but its extension to the full interacting Standard Model is undemonstrated.

---

## 1. The Wheeler-Feynman Absorber Theory and Its Cosmological Extensions

### 1.1 The Original Theory (1945)

Wheeler and Feynman showed that classical electrodynamics can be formulated with time-symmetric (half-retarded plus half-advanced) interactions between charged particles, with no independent electromagnetic field [4]. The observed dominance of retarded radiation emerges as a consequence of the **absorber condition**: the universe must contain a sufficient density of future absorbers to produce the interference pattern that cancels the advanced component. The key result is:

> F_ret = (1/2)(F_ret + F_adv) + (1/2)(F_ret - F_adv)

where the second term is contributed by the response of the absorber medium.

### 1.2 Hogarth (1962): Cosmological Absorber Condition

Hogarth examined the Wheeler-Feynman absorber condition in various Friedmann cosmological models [5]. His critical finding was that **none of the commonly acceptable model universes seems to provide boundary conditions appropriate to a unique fully retarded solution**. In expanding universes, the dilution of matter means that photons emitted now may escape to infinity without being fully absorbed. This creates a fundamental tension: the absorber condition that works in a static universe becomes problematic in an expanding one.

### 1.3 Hoyle and Narlikar (1963-1995)

Hoyle and Narlikar developed a comprehensive action-at-a-distance formulation of electrodynamics (and later gravity) in which the cosmological boundary conditions directly determine the arrow of electromagnetic time. Their framework — published across multiple works from 1963 to 1995 — showed that when the theory is placed in cosmological context, the alignment of three arrows of time (thermodynamic, electrodynamic, and cosmological) can be explained by the structure of the universe itself. Crucially, their approach **eliminates field divergences** that plague conventional QFT, but the mechanism operates specifically for electromagnetic interactions mediated by massless photons [3].

### 1.4 Cramer (1983): Generalized Absorber Theory

John Cramer extended the Wheeler-Feynman approach in a pivotal 1983 paper. He considered an open expanding universe with a Big Bang singularity at T = 0 and showed that a **four-vector reflection boundary condition at the singularity** leads to the observed dominance of retarded radiation. Cramer's key insight was that the Big Bang singularity exists only in the past time direction, not in the future direction — this fundamental asymmetry of an open universe accounts for the electromagnetic direction of time.

Critically, Cramer noted that this mechanism also applies to the **"weak" arrow of time associated with neutrino emission**. This is one of the few explicit statements in the literature extending the absorber-type argument beyond pure electromagnetism to the weak sector, though the treatment remained qualitative rather than deriving propagators from first principles.

### 1.5 Davies (1972) and Cosmological Horizons

Paul Davies examined the absorber theory in the context of cosmological horizons. In an open expanding universe, the cosmological event horizon acts as a kind of absorber boundary. The asymmetry between the past boundary (Big Bang singularity) and the future boundary (cosmological horizon or continued expansion) provides the fundamental time-asymmetry that selects retarded over advanced solutions. However, Davies' analysis was restricted to electromagnetic radiation.

---

## 2. The Yurova-Yurov-Yurov Paper (2023): The Central Result

### 2.1 Paper Details

- **Title:** "The Cosmological Arrow of Time and the Retarded Potentials"
- **Authors:** Alla A. Yurova, Artyom Yurov, Valerian A. Yurov (Immanuel Kant Baltic Federal University, Kaliningrad)
- **Published:** *Universe* 9(1), 30 (2023); arXiv:2301.07508
- **Keywords:** arrow of time, Klein-Gordon equation, Dirac equation, Schrödinger equation, retarded potentials, Hubble parameter

### 2.2 The Mathematical Mechanism

The paper proceeds through a hierarchy of field equations: Klein-Gordon → Dirac → Schrödinger/Pauli, working in a homogeneous and isotropic Friedmann geometry with scale factor a(t).

**Step 1: Klein-Gordon equation in Friedmann spacetime.**

The standard KGE φ̈ - c²Δφ + (mc²/ℏ)²φ = 0 becomes, in the expanding universe:

> φ̈ + 3(ȧ/a)φ̇ - (c²/a²)Δφ + M²φ = 0

where M² = (3H/2)² + (mc²/ℏ)². The friction term 3Hφ̇ is the Hubble damping that breaks time-reversal symmetry at the level of solutions (not of the underlying dynamics, since H → -H under time reversal exchanges expansion with contraction).

**Step 2: Modified Dirac equation.**

Taking the "square root" following the standard Dirac procedure yields a modified Dirac equation in expanding spacetime:

> iℏ(∂/∂t + 3H/2)Ψ = -iℏc Σ_k α_k ∂_k Ψ + mc²βΨ

**Step 3: Non-relativistic limit and the key result.**

In the non-relativistic limit, the Schrödinger equation acquires a modified kinetic term:

> iℏ(∂ψ/∂t) = -ℏ²/(2m + iλ) Δψ

where **λ = 3ℏH/(2c²)** is a tiny imaginary contribution to the effective mass arising from cosmological expansion.

**Step 4: Green's function analysis.**

The Fourier-space Green's function for this modified Schrödinger equation is:

> G₀(p,ω) = 1/(ℏω - 2mp²/(4m² + λ²) + iλp²/(4m² + λ²))

The term iλp²/(4m² + λ²) in the denominator places the pole at ω = -iε in the **lower complex half-plane** (since λ > 0 for H > 0, i.e., an expanding universe). By the residue theorem, contour integration for t' > t picks up this pole and yields:

> G(x' - x) = 0 for t' < t

This is precisely the **retarded boundary condition**. The full retarded Green's function is:

> G(x'-x) = -(i/ℏ^{5/2}) [(3iℏH + 4mc²)/(8iπc²(t'-t))]^{3/2} × θ(t'-t) × exp[(im/ℏ - 3H/(4c²))|r'-r|²/(2(t'-t))]

**Step 5: Contracting universe reversal.**

Under t → -t, we get H → -H, so λ → -λ, which moves the pole to the upper half-plane and selects the **advanced** propagator. This confirms the Gold hypothesis: in a contracting universe, the advanced propagator would be selected instead.

### 2.3 Scope and Limitations

**What the paper covers:**
- Scalar fields (Klein-Gordon equation) with arbitrary mass m
- Spinor fields (Dirac equation) 
- Non-relativistic limit (Schrödinger/Pauli equation)
- Both massive and massless cases (the mechanism works for any m, with the Hubble contribution being additive)

**What the paper does NOT cover:**
1. **Interacting fields.** The derivation is for free fields only. No interaction Hamiltonians (electromagnetic coupling, Yukawa coupling, gauge interactions) are included.
2. **Gauge fields themselves.** The paper treats matter fields (scalar, spinor) propagating in FLRW spacetime, not the gauge field propagators (photon, gluon, W/Z). The propagator of the gauge field itself in FLRW spacetime is not derived.
3. **Renormalization.** There is no discussion of whether the mechanism survives loop corrections or renormalization.
4. **Confinement.** No treatment of the infrared behavior of QCD or the non-perturbative effects that confine gluons.
5. **Non-abelian self-interactions.** The nonlinear self-coupling of gluons (which has no electromagnetic analog) is not addressed.
6. **The Feynman propagator vs. the retarded propagator.** The paper derives the retarded Green's function. In QFT, the relevant object for scattering calculations is the Feynman propagator (with its specific iε prescription), not the retarded propagator. The relationship between the cosmological selection of the retarded propagator and the Feynman iε prescription is not discussed.

### 2.4 Numerical Magnitude

The parameter λ = 3ℏH/(2c²) ≈ 2.42 × 10⁻⁶⁵ g, which is approximately 37 orders of magnitude smaller than the electron mass. This means the effect is utterly negligible for any local experiment — it manifests only through the global boundary condition it imposes on the Green's function pole structure, not through any measurable local correction.

### 2.5 Assessment of Robustness

The mathematical argument is clean and correct for what it proves: in an FLRW spacetime with H > 0, free quantum fields acquire a complex effective mass that shifts Green's function poles into the lower half-plane, selecting retarded propagation. The key assumptions are:

1. **Homogeneous and isotropic spacetime** (Friedmann geometry)
2. **Constant Hubble parameter** (valid as an approximation because cosmological timescales >> quantum mechanical timescales)
3. **Free fields** (no interactions)
4. **Synchronous reference frame** (cosmic time)

The constant-H assumption is well-justified for the purpose of propagator selection, since the mechanism requires only that H > 0, not that H take any particular value. The homogeneity and isotropy assumptions are likewise appropriate for a cosmological-scale argument.

---

## 3. The Gap: Extension to Non-Abelian Gauge Sectors

### 3.1 The Weak Sector (SU(2))

**The mass problem.** The W and Z bosons have masses of approximately 80 and 91 GeV respectively. Their Compton wavelength is ~10⁻¹⁸ m — far smaller than any cosmological scale. The Wheeler-Feynman absorber mechanism, which relies on radiation propagating to cosmological distances, cannot operate in its standard form for these massive particles.

**However**, the Yurova-Yurov mechanism is different from the Wheeler-Feynman mechanism. It does not require the field to propagate to cosmological distances. It operates through the modification of the field equation by the Hubble friction term, which shifts the Green's function pole regardless of the particle's mass. Since their derivation includes the mass term explicitly (M² = (3H/2)² + (mc²/ℏ)²), the mathematical mechanism **formally applies to massive fields**, including the W and Z bosons.

**But** this formal applicability comes with a caveat: the W and Z bosons are unstable (lifetimes ~10⁻²⁵ s) and are always produced in interactions. The free-field Green's function is not directly observable for these particles. The question is whether the pole-shifting mechanism survives when the full self-energy corrections and finite width of these particles are included.

**The electroweak epoch argument.** Before electroweak symmetry breaking (T > 159.5 GeV, t < 10⁻¹² s after the Big Bang), the W and Z bosons were massless. In this epoch, all electroweak gauge bosons behaved like photons — massless, long-range, propagating to cosmological distances. The Wheeler-Feynman absorber condition could in principle operate for the entire electroweak sector during this phase. If the retarded boundary condition was established during this early epoch, it would persist through electroweak symmetry breaking, since the boundary condition is a global property of the solution space, not a local property that changes when particles acquire mass. **This argument, while plausible, does not appear to have been made explicitly in the published literature.**

### 3.2 The Strong Sector (SU(3))

**The confinement problem.** Gluons are massless but confined — they do not propagate as free particles beyond hadronic scales (~10⁻¹⁵ m). The Wheeler-Feynman absorber mechanism, which requires radiation to reach cosmological absorbers, cannot operate for gluons in the present universe.

**The quark-gluon plasma argument.** Before the QCD phase transition (T > ~170 MeV, t < ~10⁻⁵ s after the Big Bang), quarks and gluons existed in a deconfined quark-gluon plasma. In this phase, gluons propagated freely (up to thermal screening effects). The absorber-type mechanism could in principle have operated during this epoch. Again, if the retarded boundary condition was established during the deconfined phase, it would persist through confinement.

**The non-abelian self-interaction problem.** Unlike photons, gluons carry color charge and interact with each other. The Yang-Mills equations are nonlinear: the superposition principle does not hold. This means the standard Green's function analysis (which relies on linearity) does not straightforwardly apply. Retarded solutions of the Yang-Mills equations have been studied — degrees of freedom can be rearranged to give dressed quarks and Yang-Mills radiation governed by an Abraham-Lorentz-Dirac type equation — but the connection between these retarded solutions and cosmological boundary conditions has not been established.

**The Yurova-Yurov mechanism for gluon fields.** The Hubble friction term 3Hφ̇ in the Klein-Gordon equation is generic — it arises from the FLRW metric for any field. For the linearized gluon field equations (valid in the perturbative regime, i.e., at high energies or short distances where asymptotic freedom holds), the same pole-shifting mechanism should apply. But in the infrared/confining regime, where perturbation theory breaks down, the argument has no obvious extension.

### 3.3 Summary of the Gap

| Sector | Wheeler-Feynman type mechanism | Yurova-Yurov type mechanism | Status |
|--------|-------------------------------|----------------------------|--------|
| U(1) EM | Works (photons are massless, long-range) | Works (free scalar/spinor in FLRW) | Structurally justified |
| SU(2) Weak | Does not work now (massive W, Z); may work before EWSB | Works formally for free massive fields | Gap: interactions, finite width, renormalization |
| SU(3) Strong | Does not work now (confinement); may work in QGP phase | Works formally for linearized/perturbative regime | Gap: nonlinear YM, confinement, non-perturbative QCD |

---

## 4. Other Approaches to Cosmological Time-Asymmetry

### 4.1 Penrose's Weyl Curvature Hypothesis (1979)

Penrose proposed that the Weyl curvature tensor was zero (or very small) at the Big Bang and grows with time, providing a gravitational measure of entropy increase. This hypothesis addresses the thermodynamic arrow of time through the initial conditions of spacetime geometry. However, **Penrose does not address propagator selection specifically**. The Weyl curvature hypothesis constrains the gravitational degrees of freedom at the initial singularity but does not derive the retarded propagator for matter or gauge fields.

Recent work (e.g., power-law inflation satisfying the WCH) has shown that inflationary cosmology is compatible with the Weyl curvature hypothesis, and quantum backreaction effects at the Planck scale can enforce near-zero Weyl curvature at the bounce/singularity.

### 4.2 Carroll and Chen: Spontaneous Inflation (2004)

Sean Carroll and Jennifer Chen proposed that de Sitter space is unstable to spontaneous inflation, creating an arrow of time that is statistical rather than fundamental. In their model, the universe is time-symmetric on ultra-large scales, with entropy increasing in both temporal directions from a minimum-entropy state. This addresses the thermodynamic Past Hypothesis without positing a special initial condition.

**Relevance to propagator selection:** Carroll's framework explains the thermodynamic arrow of time but does not address the selection of retarded vs. advanced propagators at the level of QFT. It provides a cosmological context in which the retarded propagator might be selected (since entropy increases in both time directions, observers in each branch would see a retarded propagator in their "forward" direction), but this connection is not made explicit.

### 4.3 The Gold Universe Hypothesis (1962)

Thomas Gold proposed that the thermodynamic arrow of time is caused by cosmological expansion, and that in a recollapsing universe the arrow would reverse. This directly implies that in the collapsing phase, the advanced propagator would be selected instead of the retarded one.

**Hawking's engagement:** Hawking initially endorsed Gold's hypothesis in 1985 ("Arrow of time in cosmology," Phys. Rev. D 32, 2489), arguing from the no-boundary proposal that entropy would decrease in the recollapsing phase. He retracted this shortly after, acknowledging that Don Page had shown individual WKB components of the wave function need not be CPT invariant, and that entropy would continue to increase during contraction.

The Yurova-Yurov result provides mathematical support for Gold's hypothesis in a limited sense: H > 0 gives retarded propagation, H < 0 gives advanced propagation. But this is for free fields in FLRW spacetime, not for the full thermodynamic argument Gold intended.

### 4.4 Huw Price: Time-Symmetry and Radiation (1996)

Huw Price, in *Time's Arrow and Archimedes' Point*, argued that the asymmetry of radiation is not fundamental but requires a cosmological explanation. He advocated for Gold's time-symmetric universe and criticized the Wheeler-Feynman absorber theory for containing a "misleading concept of temporal asymmetry of radiation." Price's position is that we should not treat the retarded propagator as a fundamental law but as a cosmological boundary condition, favoring Gold's hypothesis. He does not, however, provide a mathematical derivation of propagator selection from cosmological data.

### 4.5 Schulman: Opposite Arrows of Time

Lawrence Schulman explored toy models with two weakly-coupled systems having opposite thermodynamic arrows of time, realized through two-time boundary conditions. His work (including the book *Time's Arrows and Quantum Measurement*, 1997) addresses the conceptual possibility of coexisting arrows without deriving propagator selection from cosmology.

### 4.6 Castagnino and Lombardi: Global Geometrical Arrow (2003-2009)

Mario Castagnino and Olimpia Lombardi proposed that the arrow of time is an intrinsic geometrical feature of spacetime, manifested globally as the time-asymmetry of the universe and locally as time-asymmetric energy flow via the energy-momentum tensor. Their approach reframes the arrow of time as non-entropic and geometric. They note that the energy-momentum tensor "supplies the basis for deducing the time-asymmetry of quantum field theory, posed as an axiom in this theory." This comes closest to addressing propagator selection: they identify that the time-asymmetry of QFT (including the retarded/advanced distinction) follows from the global geometrical asymmetry, but they do not provide an explicit derivation of propagator pole positions from cosmological data.

### 4.7 Hartle: Arrows of Time in Quantum Cosmology (2020)

James Hartle showed that arrows of time emerge in a quantum universe with time-neutral dynamics but time-asymmetric initial and final conditions. Using the decoherent histories framework, he demonstrated that requiring decoherence of history sets yields time asymmetry even when the fundamental dynamics are time-symmetric. The work uses a "final state of maximum indifference" (proportional to the unit density matrix) to maintain causality. This addresses the emergence of macroscopic time-asymmetry but does not specifically derive the retarded propagator or the Feynman iε prescription from boundary conditions.

### 4.8 Nayeri: Inflationary Branch Decoherence (2026)

Ali Nayeri's recent paper (arXiv:2602.21263) computes the reduced density matrix for long-wavelength curvature perturbations and shows that expanding branches decohere within ~0.5 e-folds, acquiring robust classical records while contracting branches do not. This provides a dynamical mechanism for selecting expanding cosmological histories as classical. The implication for propagator selection is indirect: if only expanding branches are classical, then the retarded propagator (selected by H > 0 per Yurova-Yurov) is the one that operates in any classically realized cosmological history.

### 4.9 Visser: The iε Prescription as Complex Metric Deformation (2022)

Matt Visser showed that Feynman's iε prescription for QFT propagators has a natural reinterpretation as a slight complex deformation of the Minkowski spacetime metric. This geometric reinterpretation extends to curved spacetime QFT and fluctuating geometries. While this does not derive the iε prescription from cosmology, it provides a geometric framework in which the prescription could potentially be connected to the spacetime metric itself — and hence to cosmological properties. This remains unexplored.

### 4.10 Wald and the Hadamard Condition

Robert Wald and collaborators established that in curved spacetime, the Hadamard condition on the two-point function of a quantum field is equivalent to the Feynman propagator being a distinguished parametrix. The Hadamard condition ensures finite renormalized stress-energy tensors and is considered the correct physical condition on quantum states in curved spacetime. In stationary spacetimes with bifurcate Killing horizons, this uniquely determines the vacuum state. However, in general FLRW spacetimes without timelike Killing vectors, **there is no unique vacuum state**, and hence no unique propagator selection from the Hadamard condition alone. Additional input — such as the Bunch-Davies vacuum in de Sitter space — is required.

---

## 5. The Feynman Propagator vs. the Retarded Propagator

An important conceptual issue, inadequately addressed in the literature, is the distinction between the **retarded propagator** and the **Feynman propagator**. The Yurova-Yurov paper derives selection of the retarded Green's function. But in QFT, scattering amplitudes are computed using the Feynman propagator, which has a different pole structure:

- **Retarded propagator:** both poles in the lower half-plane (propagation only forward in time)
- **Feynman propagator:** positive-frequency pole in the lower half-plane, negative-frequency pole in the upper half-plane (particles propagate forward, antiparticles backward — equivalently, positive energy forward and negative energy backward, per the Stueckelberg-Feynman interpretation)

The Feynman iε prescription is:

> G_F(p) = 1/(p² - m² + iε)

This encodes time-ordering, not strict retardation. The cosmological mechanism described by Yurova-Yurov shifts **all** poles to the lower half-plane (selecting retardation), not just the positive-frequency pole (which would select the Feynman prescription). The relationship between these two prescriptions in cosmological context is an unresolved issue.

One possible resolution: the retarded propagator and the Feynman propagator differ by the homogeneous solution (the Pauli-Jordan commutator function). If cosmological expansion selects retarded boundary conditions, and the Feynman propagator is then constructed from the retarded propagator by the standard relation G_F = G_ret - (1/2)G_PJ (with appropriate vacuum state specification), then the cosmological selection of the retarded propagator would indirectly constrain the Feynman propagator. But this has not been worked out.

---

## 6. The Schwinger-Keldysh (In-In) Formalism

In cosmological QFT, the appropriate formalism is not the in-out S-matrix but the **Schwinger-Keldysh (in-in or closed-time-path) formalism**, which uses a doubled contour in the complex time plane. This formalism naturally incorporates retarded, advanced, and Keldysh (statistical) propagators. The time-ordering on the forward branch gives the Feynman propagator; the anti-time-ordering on the backward branch gives the anti-Feynman propagator; and the cross terms give retarded and advanced propagators.

In cosmological applications (e.g., primordial perturbation theory), the in-in formalism is the standard tool. The arrow of time enters through the **initial state** (typically the Bunch-Davies vacuum at early times). The retarded propagator emerges naturally as a causal Green's function in this formalism, while the Feynman propagator enters through the in-out amplitude. The cosmological boundary condition (specifying the initial vacuum state) effectively selects the propagator structure.

This suggests that the proper framework for understanding cosmological propagator selection is the in-in formalism rather than the in-out S-matrix, and that the selection is encoded in the choice of initial state (which is a boundary condition set by cosmological initial conditions).

---

## 7. The Early Universe Argument: A Proposed Synthesis

The following argument, which I construct from the various pieces in the literature, has not been stated explicitly in any single paper but represents the strongest case that can be assembled:

1. **Before electroweak symmetry breaking** (T > 160 GeV, t < 10⁻¹² s): All gauge bosons — photons, W, Z, and gluons — were massless. All forces were long-range. The universe was in a hot, dense state expanding rapidly (H extremely large).

2. **Before the QCD phase transition** (T > 170 MeV, t < 10⁻⁵ s): Quarks and gluons were deconfined in a quark-gluon plasma. Gluons propagated freely.

3. **The Yurova-Yurov mechanism** applies to any field in FLRW spacetime: the Hubble friction term shifts Green's function poles to select retarded propagation. During the early universe, when all gauge bosons were effectively massless and long-range, this mechanism (and the Wheeler-Feynman-type absorber condition) could operate across all gauge sectors simultaneously.

4. **The boundary condition, once set, persists.** The retarded boundary condition is a property of the solution space, not of the field equations. Once established in the early universe (when all sectors were amenable to the cosmological mechanism), it does not "un-set" when particles acquire mass or become confined. The boundary condition is inherited by the low-energy effective theory.

5. **Therefore**, cosmological expansion can provide a universal mechanism for selecting the retarded propagator across all gauge sectors, provided the selection was established during the early universe when all sectors had the appropriate properties (massless, deconfined, long-range).

**Critical weakness of this argument:** Step 4 — that boundary conditions established in the early universe persist through phase transitions — is assumed rather than proven. The electroweak and QCD phase transitions involve nonperturbative reorganization of the vacuum. Whether a boundary condition on the Green's function pole structure survives such transitions is a nontrivial question that has not been addressed.

---

## 8. Key Papers and Authors

### Papers Directly Addressing Cosmological Propagator Selection

1. **Yurova, Yurov, and Yurov (2023)** — "The Cosmological Arrow of Time and the Retarded Potentials," *Universe* 9(1), 30. [arXiv:2301.07508] — **The key paper.** Derives retarded Green's function from Hubble expansion for free KG, Dirac, and Schrödinger fields.

2. **Wheeler and Feynman (1945)** — "Interaction with the Absorber as the Mechanism of Radiation," *Rev. Mod. Phys.* 17, 157. — Original absorber theory for electrodynamics.

3. **Hogarth (1962)** — "Cosmological Considerations of the Absorber Theory of Radiation," *Proc. R. Soc. Lond. A* 267, 365. — Shows difficulties of absorber condition in expanding FRW models.

4. **Cramer (1983)** — "The Arrow of Electromagnetic Time and the Generalized Absorber Theory," *Found. Phys.* 13, 887. — Extends absorber theory to open expanding universes; mentions weak interaction arrow.

5. **Hoyle and Narlikar (1963-1995)** — Series of papers on action-at-a-distance electrodynamics and cosmology. Book: *Action at a Distance in Physics and Cosmology* (1974); review in *Rev. Mod. Phys.* 67, 113 (1995).

### Papers on Cosmological Arrow of Time (Relevant Context)

6. **Gold (1962)** — "The Arrow of Time," *Am. J. Phys.* 30, 403. — Proposes cosmological origin of time's arrow.

7. **Hawking (1985)** — "Arrow of Time in Cosmology," *Phys. Rev. D* 32, 2489. — Proposes (later retracts) entropy reversal in recollapsing universe.

8. **Penrose (1979)** — "Singularities and Time-Asymmetry" in *General Relativity: An Einstein Centenary Survey*. — Weyl curvature hypothesis.

9. **Carroll and Chen (2004)** — "Spontaneous Inflation and the Origin of the Arrow of Time," arXiv:hep-th/0410270. — Time-symmetric cosmology with spontaneous inflation.

10. **Hartle (2020)** — "Arrows of Time and Initial and Final Conditions in the Quantum Mechanics of Closed Systems," arXiv:2002.07093. — Decoherent histories approach to arrows of time.

11. **Price (1996)** — *Time's Arrow and Archimedes' Point*, Oxford University Press. — Philosophical analysis of time-asymmetry.

12. **Castagnino and Lombardi (2003-2009)** — "The Global Arrow of Time as a Geometrical Property of the Universe," *Found. Phys.* 33, 877 (2003); "The global non-entropic arrow of time," *Synthese* 169, 1 (2009).

### Papers on Propagators in Curved Spacetime

13. **Visser (2022)** — "Feynman's iε prescription, almost real spacetimes, and acceptable complex spacetimes," *JHEP* 2022, 129. [arXiv:2111.14016] — Geometric reinterpretation of iε.

14. **Wald (1994)** — *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press. — Hadamard condition and propagator uniqueness.

15. **Nayeri (2026)** — "The Cosmological Arrow of Time from Inflationary Branch Decoherence," arXiv:2602.21263. — Decoherence selects expanding branches.

### Papers on Propagators in de Sitter Space

16. **Various authors (2013-2025)** — Work on propagators in de Sitter space shows that there is no unique vacuum state in the absence of a global timelike Killing vector, leading to propagator ambiguity that must be resolved by additional physical input (typically the Bunch-Davies condition).

---

## 9. What Remains Open

1. **Extension to interacting fields.** The Yurova-Yurov mechanism works for free fields. Whether the Hubble-induced pole shift survives self-energy corrections, vertex corrections, and renormalization in interacting QFT is completely unknown.

2. **Extension to gauge field propagators.** The paper treats matter fields (scalar, spinor) in FLRW spacetime. The propagators of the gauge fields themselves (gluon propagator, W/Z propagator) in FLRW spacetime have not been shown to acquire the retarded boundary condition through this mechanism.

3. **The Feynman iε vs. retarded Green's function distinction.** The cosmological mechanism selects the retarded propagator, but QFT uses the Feynman propagator. The precise relationship — and whether cosmological selection of the retarded propagator implies the Feynman iε prescription — needs to be established.

4. **Persistence through phase transitions.** Whether the retarded boundary condition, if established in the early universe when all gauge bosons were massless and deconfined, survives through the electroweak and QCD phase transitions is unproven.

5. **Non-perturbative QCD.** The behavior of the gluon propagator in the infrared (confining) regime is governed by non-perturbative physics. Whether the cosmological pole-shifting mechanism has any bearing on the confined gluon propagator is unknown.

6. **The absorber condition for non-abelian fields.** No paper in the literature formulates the Wheeler-Feynman absorber condition for SU(2) or SU(3) gauge fields. The self-interaction of non-abelian gauge bosons fundamentally complicates the absorber picture.

7. **Experimental or observational tests.** The Hubble correction λ ≈ 10⁻⁶⁵ g is far too small to measure directly. The Partridge experiment (1973) attempted to test for advanced radiation effects but was later ruled out as a valid test of the absorber theory.

---

## 10. Conclusion

**Can the cosmological expansion of the universe provide a universal mechanism for selecting the retarded propagator across all gauge sectors?**

**The short answer is: partially yes for free fields, but the full answer for interacting non-abelian gauge theories remains open.**

The Yurova-Yurov-Yurov (2023) paper provides a mathematically clean demonstration that the Hubble expansion generates an imaginary mass contribution that shifts Green's function poles to select retarded propagation for any free quantum field (scalar, spinor, of any mass) in FLRW spacetime. This is genuinely gauge-sector-independent at the level of free field propagation: the mechanism works identically for the equations governing any spin, any mass, and any gauge group, because the Hubble friction term is a universal feature of field equations in expanding spacetime.

However, the mechanism has not been extended to:
- Interacting fields or gauge field self-energies
- The non-linear self-interactions of non-abelian gauge fields  
- The non-perturbative confining regime of QCD
- The Feynman propagator (as opposed to the retarded propagator)

The strongest available argument for universality is the **early universe synthesis** outlined in Section 7: during the earliest cosmological epoch, all gauge bosons were massless, all were deconfined, and the Hubble parameter was maximal. Both the Yurova-Yurov pole-shifting mechanism and the Wheeler-Feynman absorber condition could operate across all gauge sectors simultaneously. If the boundary condition set during this epoch persists through subsequent phase transitions, then cosmological expansion does provide a universal mechanism. But the persistence of boundary conditions through phase transitions is an assumption, not a theorem.

This represents a significant **structural gap** in the foundations of quantum field theory: the retarded propagator is assumed in every gauge sector, but only the electromagnetic sector has a cosmological justification (through the Wheeler-Feynman absorber theory), and only free fields of arbitrary type have a mathematical derivation of propagator selection from expansion (through Yurova-Yurov). The non-abelian interacting gauge sectors remain without a structural account of why the retarded propagator is chosen.

---

## References

[1] Penrose, R. (1979). "Singularities and Time-Asymmetry." In *General Relativity: An Einstein Centenary Survey*, eds. S.W. Hawking and W. Israel.

[2] Hawking, S.W. (1988). *A Brief History of Time*.

[3] Hoyle, F. and Narlikar, J.V. (1964). "Time Symmetric Electrodynamics and the Arrow of Time." *Proc. R. Soc. Lond. A* 277, 1.

[4] Wheeler, J.A. and Feynman, R.P. (1945). "Interaction with the Absorber as the Mechanism of Radiation." *Rev. Mod. Phys.* 17, 157.

[5] Hogarth, J.E. (1962). "Cosmological Considerations of the Absorber Theory of Radiation." *Proc. R. Soc. Lond. A* 267, 365.

[6] Gold, T. (1962). "The Arrow of Time." *Am. J. Phys.* 30, 403.

[7] Cramer, J.G. (1983). "The Arrow of Electromagnetic Time and the Generalized Absorber Theory." *Found. Phys.* 13, 887.

[8] Yurova, A.A., Yurov, A., and Yurov, V.A. (2023). "The Cosmological Arrow of Time and the Retarded Potentials." *Universe* 9(1), 30.

[9] Carroll, S.M. and Chen, J. (2004). "Spontaneous Inflation and the Origin of the Arrow of Time." arXiv:hep-th/0410270.

[10] Hartle, J.B. (2020). "Arrows of Time and Initial and Final Conditions in the Quantum Mechanics of Closed Systems." arXiv:2002.07093.

[11] Price, H. (1996). *Time's Arrow and Archimedes' Point*. Oxford University Press.

[12] Castagnino, M. and Lombardi, O. (2009). "The Global Non-Entropic Arrow of Time: From Global Geometrical Asymmetry to Local Energy Flow." *Synthese* 169, 1.

[13] Visser, M. (2022). "Feynman's iε prescription, almost real spacetimes, and acceptable complex spacetimes." *JHEP* 2022, 129.

[14] Wald, R.M. (1994). *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*. University of Chicago Press.

[15] Schulman, L.S. (1997). *Time's Arrows and Quantum Measurement*. Cambridge University Press.

[16] Hawking, S.W. (1985). "Arrow of Time in Cosmology." *Phys. Rev. D* 32, 2489.

[17] Page, D.N. (1985). "Will Entropy Decrease if the Universe Recollapses?" *Phys. Rev. D* 32, 2496.

[18] Nayeri, A. (2026). "The Cosmological Arrow of Time from Inflationary Branch Decoherence." arXiv:2602.21263.

[19] Hoyle, F. and Narlikar, J.V. (1995). "Cosmology and Action at a Distance Electrodynamics." *Rev. Mod. Phys.* 67, 113.

[20] Calzetta, E. and Hu, B.L. (1987). "Closed Time Path Functional Formalism in Curved Space-Time." *Phys. Rev. D* 35, 495.

[21] Zeh, H.D. (2007). *The Physical Basis of the Direction of Time*. 5th ed. Springer.

[22] Castagnino, M., Lombardi, O., and Lara, L. (2003). "The Global Arrow of Time as a Geometrical Property of the Universe." *Found. Phys.* 33, 877.

[23] Davies, P.C.W. (1972). "Is the Universe Transparent or Opaque?" *J. Phys. A* 5, 1722.

[24] Partridge, R.B. (1973). "Absorber Theory of Radiation and the Future of the Universe." *Nature* 244, 263.
