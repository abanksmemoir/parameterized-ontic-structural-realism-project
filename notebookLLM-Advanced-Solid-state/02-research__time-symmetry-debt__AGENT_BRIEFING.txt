# Agent Briefing: Parameterized Ontic Structural Realism Project

**Date:** 2026-04-05
**Written by:** Claude session that built V2 of the dependency graph
**For:** Any Claude instance picking up work on this project

---

## What this project is

Natural philosophy. Mike Abramson (Occidental Advisors) is building a structural dependency graph of the Standard Model of particle physics — from logical axioms (Layer 0) to the specific particle content and coupling constants (Layer 9). Every node declares its parameters, dependencies, and provisions. Every choice is explicit. Nothing reaches around its interface.

The project originated from a concrete question in experimental physics: the Wheeler-Feynman absorber theory predicts that under specific conditions (small antenna, incomplete absorption), advanced electromagnetic waves — signals traveling backward in time — should be detectable. There is a contested but non-trivial experimental record (Niknejadi-Madey-Kowalczyk 2015 in Phys Rev D; Bajlo's 500-run replication 2016-2017). The dependency graph is infrastructure for navigating the theoretical commitments that bear on this and related questions.

The philosophical stance: "Real" is an honorific for structural regions that do nontrivial empirical work. The Platonism is instrumental. The graph should be legible, technically pristine, and well-formed — useful as a consequence of being correct, not engineered toward a specific use case.

## What exists

The GitHub repo is `abanksmemoir/parameterized-ontic-structural-realism-project` (private). The local working directory is `C:\Users\micha\deep-research\time-symmetry-debt\`.

### V1 (in the GitHub repo root)
- `sm_dependency_graph.md` — Original 10-layer, 30-node graph spec
- `sm_dependency_graph.json` — Machine-readable version
- `README.md` — Project overview

### Time-Symmetry Debt Research (in `deep-research/time-symmetry-debt/`)
- `RESEARCH_BRIEFS.md` — Five research questions about the "time-symmetry debt" (the fact that the retarded propagator is chosen by hand in every gauge sector but structurally justified only in U(1) electromagnetism)
- `reports/agent-1-report.md` — Non-abelian absorber condition: no one has formulated one. Four mathematical obstacles (self-interaction, confinement, Gribov, topology), all temperature-dependent.
- `reports/agent-2-report.md` — Cosmological propagator selection: Yurova-Yurov-Yurov (2023) derives retarded propagator from Hubble expansion for free fields. Doesn't extend to interactions or gauge fields.
- `reports/agent-3-report.md` — CP violation and the propagator: CP/T violation presupposes the iε prescription and cannot explain it. Definitively ruled out as a candidate mechanism.
- `reports/agent-4-report.md` — Inheritance through coupling: the shared vacuum state means iε is a single global choice. Five reinforcing transmission mechanisms identified.
- `reports/agent-5-report.md` — Gravitational absorber condition: Hoyle-Narlikar formulated one but it fails (universe is transparent to gravity). Penrose WCH offers an alternative.
- `reports/synthesis.md` — Cross-cutting synthesis. The debt is one problem, not five. Three-tier architecture: cosmological boundary condition → vacuum state → sector-specific mechanisms.

### V2 (in `deep-research/time-symmetry-debt/v2/`)
- `V2_NOTE.md` — **Read this first.** Why v2 exists, terminology definitions (parameter subtypes, dependency types), decision log (D1-D7), open questions (OQ1-OQ5).
- `sm_dependency_graph_v2.md` — Refactored graph. Primary document. All 30 nodes with typed parameters, audited dependencies, temporal notes, contingent provisions, deep-research flags.
- `sm_dependency_graph_v2.json` — Machine-readable version derived from the markdown.
- `PARAMETER_INVENTORY.md` — Flat inventory of all 79 parameters and 57 dependencies. Temporal structure chain. Underspecified parameters. New parameters added in v2.
- All v1 research reports copied for reference.

## Key decisions you need to know

1. **Everything is a parameter.** Every choice — from logic to the CKM phase — is a parameter subtyped as axiom, structural, kinematic, dynamical, boundary, or convention. No special status for "presuppositions." Dependencies between nodes are typed as logical, conventional, or contingent.

2. **The iε prescription (P057) is the most consequential hidden parameter.** It determines the causal structure of the entire Standard Model. It was invisible in v1. It's a boundary parameter at QFT (Layer 8). Its physical justification is sector-dependent and incomplete. The time-symmetry research covers this in detail.

3. **The vacuum state (P078) and Gribov region (P079) are also hidden parameters** added in v2. Both take values that practice assumes without derivation. Both are flagged for deep research.

4. **Time enters the graph in a chain:** metric signature (P036, Layer 5) → Wick rotation (P047, Layer 6) → iε sign (P057, Layer 8) → CKM phase (P074, Layer 9). Only P057 breaks time-reversal symmetry. P074's T violation is observable only in the presence of P057. These three temporal parameters (P036, P047, P057) may not be independent — flagged for deep research (OQ5).

5. **The theory contains the consequences of time symmetry.** The underlying dynamics (Yang-Mills equations) are time-symmetric at every gauge sector. The retarded propagator assumed by higher layers is contingent on boundary conditions (absorber condition, cosmological expansion) that may fail locally. This is where the experimental program (NMK, Bajlo) connects: it probes regimes where the absorber condition doesn't fully hold.

6. **The graph does not extend to cosmology.** The iε prescription's justification lives in cosmological boundary conditions that are outside the graph's scope. Rather than adding a cosmological layer, the graph annotates every temporal node with this observation.

7. **"Structural" needs disambiguation.** Many things are labeled structural. Some have derivations (anomaly cancellation constrains fermion content). Some don't (why 3 generations?). The subtype label doesn't distinguish these. OQ4 flags this.

## What needs to happen next

- **Review the V2 note with Mike.** That's the immediate next step. He'll want to go through the decisions and open questions.
- **Push to GitHub.** The v2 materials need to be committed and pushed to the repo. Use the `github-access` skill (PAT may need refreshing — it failed in this session).
- **Deep research on OQ2 (vacuum state), OQ3 (Gribov), OQ5 (temporal parameter entanglement).** Same methodology as the time-symmetry debt investigation — parallel agent teams surveying the literature.
- **Simulation environment.** Mike's original motivation includes building a computational sandbox for testing NMK/Bajlo predictions under different absorber geometries and boundary conditions. The dependency graph provides the theoretical map; the simulation environment is a separate workstream.
- **V2 refactor may have further iterations.** Mike's feedback on the V2 note will likely surface more issues. The pattern is consistent: register the variable, note what value practice assumes, flag the justification gap, don't pretend it's resolved.

## How Mike works

- He corrects framing precisely. If you paraphrase something back with your own spin, he'll catch it.
- He wants the graph to be correct and legible, not engineered toward a specific use. Don't optimize for a use case — optimize for honesty.
- "Everything is a parameter" is the governing principle. Don't create special categories when a subtype will do.
- When something is underspecified, say so. Don't resolve it in the graph — flag it for research.
- He's a natural philosopher. Treat the work accordingly.

## File you should always read first

`deep-research/time-symmetry-debt/v2/V2_NOTE.md` — it has the current state of all terminology, decisions, and open questions.
