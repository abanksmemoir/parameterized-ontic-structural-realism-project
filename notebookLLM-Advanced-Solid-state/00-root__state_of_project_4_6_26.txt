# State of Project — April 6, 2026

## What this is

A structural dependency graph of the Standard Model of particle physics — 10 layers, 30 nodes, from logical axioms (Layer 0) to the SM Lagrangian (Layer 9). Every choice is an explicit parameter. Every dependency is typed. Nothing is smuggled.

The philosophical stance is Parameterized Ontic Structural Realism: "real" is an honorific for structural regions that do nontrivial empirical work. The graph is natural philosophy — correct first, useful as a consequence.

## What exists

### V1 (repo root)
The original graph, built 2026-04-05. Functional but has blind spots exposed by the time-symmetry research:
- `sm_dependency_graph.md` / `.json` — 30-node graph
- `posr/` — Python package (graph, schema, diff, registry, templates)
- `tests/` — test suite
- `demo.py`, `pyproject.toml` — runnable demo

### Time-Symmetry Debt Research (`deep-research/time-symmetry-debt/`)
Five parallel research agents surveyed the academic literature on a single question: the retarded propagator (iε prescription) is chosen by hand in every gauge sector of the SM, but it is structurally justified only in U(1) electromagnetism via the Wheeler-Feynman absorber condition. What about the rest?

**Findings:**
- **No absorber condition exists for non-abelian gauge fields** (SU(2), SU(3)). Four mathematical obstacles, all temperature-dependent — they vanish in the early universe.
- **CP violation presupposes the iε prescription**, not the other way around. Ruled out as a candidate mechanism for selecting the causal arrow. (Donoghue-Menezes 2019, 2020.)
- **The shared vacuum state means iε is one global choice**, not a per-sector decision. The Wightman axioms enforce this via the spectral condition.
- **Cosmological expansion selects the retarded propagator for free fields** (Yurova-Yurov-Yurov 2023). Does not extend to interacting or gauge fields.
- **The gravitational absorber condition fails** — the universe is transparent to gravitational radiation. Penrose's Weyl curvature hypothesis offers an alternative that works in the opposite temporal direction.
- **The debt is one problem, not five.** The vacuum state is the fulcrum. Three-tier architecture: cosmological boundary condition -> vacuum state -> sector-specific mechanisms.

Reports: `reports/agent-1-report.md` through `agent-5-report.md`, plus `synthesis.md`.

### V2 Refactor (`deep-research/time-symmetry-debt/v2/`)
The current, authoritative version of the graph. Key changes from v1:

- **Every parameter is typed** (axiom, structural, kinematic, dynamical, boundary, convention)
- **Every dependency is audited** — 46 logical, 11 conventional (disguised parameters)
- **iε prescription (P057)** added as an explicit boundary parameter at QFT — the most consequential hidden assumption in v1
- **Vacuum state (P078)** and **Gribov region (P079)** added as hidden parameters flagged for deep research
- **Temporal structure chain** traced: metric signature -> Wick rotation -> iε sign -> CKM phase
- **Contingent provisions** annotated — where the graph's outputs depend on conditions it does not guarantee

Files:
- `V2_NOTE.md` — **Start here.** Rationale, terminology, decision log, open questions.
- `sm_dependency_graph_v2.md` / `.json` — The graph (79 parameters, 57 dependencies)
- `PARAMETER_INVENTORY.md` — Flat inventory with underspecified parameters table
- `creating-agent-notes/` — Institutional knowledge from the creating agent (origin story, lessons, leverage points, perishable knowledge)

### Agent Briefing
`AGENT_BRIEFING.md` — Onboarding document for future Claude sessions. Covers project goals, what exists, key decisions, what Mike expects, and what needs to happen next.

## Where we are going

### Near-term

1. **Deep research on three open questions:**
   - **OQ2 — Vacuum state justification.** Is the Poincare-invariant vacuum derivable from anything, or is it an independent boundary condition? What happens to vacuum selection in curved spacetime? Does the absorber condition, if it selects the retarded propagator, also select the vacuum?
   - **OQ3 — Gribov ambiguity.** What justifies restricting to the first Gribov horizon? Does the choice affect observables?
   - **OQ5 — Temporal parameter entanglement.** Are the metric signature (P036), Wick rotation (P047), and iε sign (P057) independent parameters or three aspects of a single choice? Visser (2022) on complex metric deformation is a lead.

2. **Schwinger-Keldysh bridge.** The SK (closed-time-path) formalism uses both forward and backward time contours and naturally yields retarded propagators. Nobody has asked whether the backward contour is structurally equivalent to the Wheeler-Feynman absorber response. If it is, the non-abelian sectors already have an implicit absorber mechanism in their standard computational framework.

3. **Boundary condition persistence through phase transitions.** The early-universe synthesis argument assumes the retarded boundary condition, established when all gauge bosons were massless and deconfined, persists through the electroweak (~160 GeV) and QCD (~170 MeV) phase transitions. This is assumed, not proven. If it is wrong, the cross-sector argument collapses.

### Medium-term

4. **Simulation environment.** The project's experimental origin is the NMK (Niknejadi-Madey-Kowalczyk 2015) prediction and Bajlo's contested replication: under specific absorber geometries (small antenna, incomplete absorption), advanced electromagnetic waves should be detectable. A computational sandbox — modeling time-symmetric radiation fields, absorber conditions, antenna configurations, atmospheric parameters — would let us design better experiments without needing a lab. The equations are classical EM. The dependency graph provides the theoretical map; the simulation tests its predictions.

5. **V1 Python package update.** The `posr/` package implements v1 of the graph. It needs to be updated to reflect v2's typed parameters, audited dependencies, and new nodes (P057, P078, P079). The schema, templates, and tests all need revision.

### Governing principles

- Everything is a parameter. If the alternative is well-formed, it is a parameter regardless of whether the physical universe instantiates only one value.
- Register, do not resolve. When something is underspecified, note what practice assumes and flag the gap. Do not pretend assumed values are derived.
- The graph is a map. Make it accurate. Do not optimize for a use case — let correctness generate usefulness.
- Direction of justification matters. Place things based on their preconditions, not their consequences.
- Time symmetry is pushed upward with contingent containment. The underlying dynamics are time-symmetric. The retarded character is contingent on external conditions that may fail locally.

## Repository structure

```
parameterized-ontic-structural-realism-project/
|-- state_of_project_4_6_26.md          <-- you are here
|-- README.md                            <-- project overview
|-- sm_dependency_graph.md / .json       <-- v1 graph
|-- posr/                                <-- Python package (v1)
|-- tests/                               <-- test suite (v1)
|-- demo.py, pyproject.toml              <-- runnable demo
|-- OPERATING_MANUAL.md                  <-- design philosophy
|-- PROJECT_BRIEFING.md                  <-- project context
|-- SUPPLEMENTARY_BRIEFING.md
|-- IMPLEMENTATION_NOTES.md
+-- deep-research/
    +-- time-symmetry-debt/
        |-- AGENT_BRIEFING.md            <-- onboarding for future agents
        |-- RESEARCH_BRIEFS.md           <-- research task definitions
        |-- ORCHESTRATION_PROMPT.md
        |-- reports/                     <-- 5 agent reports + synthesis
        +-- v2/                          <-- CURRENT VERSION
            |-- V2_NOTE.md              <-- start here
            |-- sm_dependency_graph_v2.md / .json
            |-- PARAMETER_INVENTORY.md
            +-- creating-agent-notes/    <-- institutional knowledge
```
