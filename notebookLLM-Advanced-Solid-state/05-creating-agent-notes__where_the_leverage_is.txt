# Where the Leverage Is

**My assessment, from full context, of what research and work would most move the POSR project forward. This is speculative but informed by having read all five agent reports in full, built the parameter inventory, and had Mike correct my understanding of the project's goals.**

---

## Highest leverage: OQ5 — Are P036, P047, and P057 independent?

The metric signature (Lorentzian vs. Euclidean), the Wick rotation (t → −iτ), and the iε prescription (+iε vs. −iε) are three parameters that all concern temporal structure. They're listed as independent in the inventory. I suspect they aren't.

Here's why this matters: if they're three aspects of a single choice, then the "time enters at Layer 5" story is wrong — time's directionality enters once, not in stages, and the apparent multi-layer chain is an artifact of how we've decomposed the theory. If they're genuinely independent, then there are theories where you set the signature to Lorentzian but the iε to −iε, and you should be able to game out the consequences. Either answer is illuminating. But the dependency structure between them isn't understood, and getting it wrong corrupts the graph at a fundamental level.

**What research would help:** A careful mathematical analysis of whether the Wick rotation is *derivable* from the iε prescription (or vice versa), or whether they're logically independent choices that happen to be made consistently. Visser (2022) on the iε as complex metric deformation is a lead — it connects the propagator prescription to the spacetime metric, which is exactly the bridge between P036 and P057.

## Second highest: OQ2 — Vacuum state justification

The vacuum state (P078) is entangled with the iε prescription (P057). In the Wightman framework, specifying the vacuum determines the propagator and vice versa. But the Wightman axioms assume flat spacetime. In curved spacetime, there is no unique vacuum (no global timelike Killing vector → no preferred positive-frequency decomposition). The Bunch-Davies vacuum in de Sitter space is a conventional choice, not a derived one.

This matters because the absorber condition is a cosmological argument, and cosmology requires curved spacetime. The bridge between "the absorber condition selects the retarded propagator in an expanding universe" and "the Standard Model uses the Feynman propagator in flat spacetime" passes through the vacuum state. If the vacuum state's justification doesn't survive the bridge, the absorber condition's reach is limited.

**What research would help:** A systematic survey of vacuum state selection in curved spacetime QFT. Focus on: (1) Is the Bunch-Davies vacuum derivable from anything, or is it a boundary condition? (2) What is the precise relationship between the vacuum state in cosmological spacetime and the Poincaré-invariant vacuum in the flat-spacetime limit? (3) Does the absorber condition, if it selects the retarded propagator cosmologically, also select the vacuum state?

## Third: The simulation environment

The dependency graph maps the theory. The simulation environment tests the theory's predictions under different parameter settings. Specifically: what happens to electromagnetic radiation when the absorber condition is locally violated (small antenna, specific geometry, atmospheric absorption profiles)?

The NMK paper (2015) gives specific quantitative predictions. Bajlo's data (2016-2017) provides 500 runs of observational data with specific signal characteristics (amplitude vs. antenna length, amplitude vs. distance, amplitude vs. angle, galactic-center modulation). A simulation environment that can:
- Model the Wheeler-Feynman time-symmetric radiation field for a pulsed transmitter
- Model the absorber condition as a function of antenna geometry and atmospheric absorption
- Predict signal amplitude at a downstream detector as a function of these variables
- Compare predictions against Bajlo's reported data

...would either reproduce Bajlo's results (supporting NMK) or fail to (identifying where the theory or the experiment went wrong). This is computational work, not theoretical — it requires implementing the equations, not discovering new ones.

**What would help:** An agent or team that reads the NMK paper carefully, implements the half-retarded-plus-half-advanced field equations, models the absorber condition for finite-geometry antenna configurations, and produces testable predictions. Python with NumPy/SciPy would be sufficient. The equations are classical EM — no quantum field theory needed.

## Fourth: The Schwinger-Keldysh bridge (from Agent 1)

The Schwinger-Keldysh (closed-time-path) formalism uses both forward and backward time contours, naturally yields retarded propagators, and applies to non-abelian gauge theories. Nobody has interpreted its backward contour as encoding the response of future absorbers in the Wheeler-Feynman sense. This is a concrete, unexplored research direction.

If someone can show that the SK formalism *is* an implicit absorber theory — that the backward contour plays the role of the future absorber response — then the non-abelian sectors (SU(2), SU(3)) already have an absorber mechanism built into their standard computational framework. The time-symmetry debt would be discharged not by extending Wheeler-Feynman to non-abelian fields, but by recognizing that the standard formalism already does it.

**What would help:** A deep research survey focused specifically on the question: "Is the Schwinger-Keldysh backward time contour structurally equivalent to the Wheeler-Feynman absorber response?" This requires reading the SK formalism literature with the absorber question explicitly in mind, which nobody has done.

## Fifth: Boundary condition persistence through phase transitions

The "early universe synthesis" — the most promising resolution of the time-symmetry debt across all sectors — assumes that the retarded boundary condition, established when all gauge bosons were massless and deconfined, persists through the electroweak and QCD phase transitions. This is assumed, not proven. If it's wrong, the entire cross-sector argument collapses.

**What would help:** Literature survey on whether propagator boundary conditions are preserved through phase transitions. This is a technical question in thermal field theory and might have a known answer that just hasn't been connected to the absorber question.

---

## What I would de-prioritize

- **Extending the graph to cosmology (OQ1).** Mike decided against this and I agree. The graph covers SM structure. Cosmological context enters as annotation, not architecture. Don't reopen this unless Mike does.
- **The Gribov ambiguity (OQ3).** Important for QCD but probably not load-bearing for the time-symmetry question. The Gribov problem affects gauge-fixing, not boundary conditions. Flag it, research it eventually, but it's not where the leverage is.
- **Disambiguating "structural" (OQ4).** This is a terminology issue that matters for graph cleanliness but doesn't block any research. Handle it when the graph gets its next major revision.
