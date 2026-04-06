# Agent Briefing — POSR Project

**Last updated:** 2026-04-06
**Updated by:** Claude session that completed the V2 Python package rewrite
**Repository:** https://github.com/abanksmemoir/parameterized-ontic-structural-realism-project

---

## What this project is

A software system that decomposes physical theories into structural dependency graphs where every presupposition is declared, every parametric choice is explicit, and theories are saved as individual "theory-files" in a flat directory. The system models a lattice of theories, not a single theory.

The philosophical stance is **Parameterized Ontic Structural Realism (POSR):** "real" is an honorific for whatever structural configuration bears an identity relationship to the actual world. The graph is natural philosophy — correct first, useful as a consequence.

**Mike Abramson** runs this project through Occidental Advisors LLC. He is not a physicist by training — he came to this through the Wheeler-Feynman absorber theory and the NMK/Bajlo experimental program (testing advanced electromagnetic wave detection). The project exists because he needed a map of what the Standard Model actually presupposes, and found that no such map existed with the rigor he required.

---

## What exists right now

### Python Package (`posr/`) — V2, current

The package was rewritten to V2 on 2026-04-06. **69 tests passing.** All files reflect the V2 schema.

| Module | What it does |
|--------|-------------|
| `posr/schema.py` | Core types: `Parameter` (typed: axiom/structural/kinematic/dynamical/boundary/convention), `Dependency` (typed: logical/conventional/contingent), `Node` (with temporal_note, contingent_provisions), `TheoryGraph`, `TheoryFile`, `ForkPoint`. Backward compat: `ParametricSlot` alias, `node.presupposes` property. |
| `posr/graph.py` | `build_from_json()` handles both V1 and V2 JSON. `resolve_parametric_choices()`, `propagate_change()` (can skip contingent deps), `validate_consistency()` (checks parameter/dependency types), `compare_structures()`, `find_deepest_chain()`. |
| `posr/diff.py` | `StructuralDiff`, `compute_structural_diff()`, `extract_shared_subgraph()`, `identify_fork_path()`, `extract_theory_branch()`, `parametric_signature()`. New V2: `dependency_type_summary()`, `parameter_type_summary()`. |
| `posr/registry.py` | V2 parameter subtypes, dependency types, expanded `PARAMETRIC_OPTIONS` (includes iε sign, vacuum state, Wick rotation, gauge fixing, renormalization scheme). Node templates for CL, FOL, ZFC, QFT. |
| `posr/templates/sm.py` | Loads from `deep-research/time-symmetry-debt/v2/sm_dependency_graph_v2.json`. 30 nodes, 79 parameters, 57 typed dependencies. Falls back to V1 JSON if V2 not found. |
| `posr/templates/gr.py` | 18 nodes, all V2 typed. Shares 12 nodes with SM. Fork at METRIC/LEVI_CIVITA (tangent bundle) vs CONN (internal gauge bundle). |
| `tests/` | 69 tests across test_schema.py, test_graph.py, test_diff.py, test_templates.py. Covers V2 parameter types, dependency types, temporal chain, boundary parameters, contingent provisions, cross-theory comparison, backward compat. |
| `demo.py` | Full V2 demo: temporal chain, boundary parameters, dependency/parameter type breakdowns, SM vs GR comparison. |

### V2 Graph Specification (`deep-research/time-symmetry-debt/v2/`)

This is the authoritative source. The Python package loads from this.

- `V2_NOTE.md` — **Start here.** Decisions D1-D7, open questions OQ1-OQ5, terminology.
- `sm_dependency_graph_v2.md` / `.json` — 30-node graph, 79 parameters, 57 typed dependencies.
- `PARAMETER_INVENTORY.md` — Flat inventory of all 79 parameters and 57 dependencies. Includes "underspecified parameters" and "temporal structure" tables.
- `creating-agent-notes/` — Institutional knowledge from the agent that created V2:
  - `origin_story.md` — Mike's NMK/Bajlo passage (only record of this text)
  - `methodological_lessons.md` — 6 lessons from Mike's corrections
  - `where_the_leverage_is.md` — Prioritized research directions
  - `what_compaction_will_lose.md` — Perishable knowledge

### Time-Symmetry Debt Research (`deep-research/time-symmetry-debt/`)

Five parallel research agents surveyed the academic literature. Key finding: the retarded propagator (iε prescription) is chosen by hand in every gauge sector, structurally justified only in U(1) via Wheeler-Feynman. The debt is one problem, not five — the vacuum state is the fulcrum.

- `reports/agent-1-report.md` through `agent-5-report.md`
- `reports/synthesis.md`
- `RESEARCH_BRIEFS.md`, `ORCHESTRATION_PROMPT.md`

### Other documents

- `OPERATING_MANUAL.md` — Six-part master manual (philosophy, architecture, operations)
- `PROJECT_BRIEFING.md` — Canonical project briefing
- `SUPPLEMENTARY_BRIEFING.md` — Prior art, tooling, cross-theory comparison, time symmetry
- `IMPLEMENTATION_NOTES.md` — Technical notes with theory-nesting design section
- `state_of_project_4_6_26.md` — Project status and roadmap (written before V2 package update)

---

## V2 schema — what you need to know

### Parameter subtypes
Every parameter has one of six subtypes:
- **axiom** — Foundational choice with no prior constraints (e.g., LEM, Axiom of Choice)
- **structural** — Mathematical/physical structure, constrained by upstream (e.g., gauge group, Lie algebra type)
- **kinematic** — Arena choice (dimension, metric signature, topology)
- **dynamical** — Equations of motion or interaction rules (e.g., coupling constants, Yukawa matrices)
- **boundary** — Initial/final conditions, propagator prescription (e.g., **iε sign**, vacuum state, Wick rotation)
- **convention** — Affects description not physics (e.g., gauge fixing, renormalization scheme)

The old V1 distinction "architectural" vs "runtime" is gone. Use the six subtypes.

### Dependency types
Every dependency edge has one of three types:
- **logical** — Y cannot be formulated without X (48 in SM graph)
- **conventional** — Y is standardly built on X but alternatives exist — this is a disguised parameter (9 in SM graph)
- **contingent** — Y uses X's output only under conditions X does not guarantee (rare, important)

### Temporal structure chain
The V2 graph tracks where temporal structure enters. The chain: metric signature (P036, MAN) → Wick rotation (P047, PATH) → iε sign (P057, QFT) → CKM phase (P074, SM_Y). Prior to P036, the graph is time-agnostic.

### Contingent provisions
Some nodes have `contingent_provisions` — outputs that depend on conditions the node doesn't internally guarantee. QFT's causal propagator depends on iε (P057). SM_Y's observable CP violation requires iε to set the causal arrow before the CKM phase can produce interference effects.

### Three most consequential hidden parameters (boundary type)
1. **P047 — Wick rotation** (PATH node): `t → -iτ`. Transforms temporal structure.
2. **P057 — iε sign** (QFT node): `+iε`. Determines causal structure. Universal across gauge sectors. Physical justification sector-dependent and incomplete. **The most important hidden parameter in the graph.**
3. **P078 — Vacuum state** (QFT node): Poincaré-invariant `|Ω⟩`. No derivation of why. Entangled with P057.

---

## Key architectural principles

1. **Everything is a parameter.** If the alternative is well-formed, it's a parameter regardless of whether physics instantiates only one value.
2. **Register, do not resolve.** When something is underspecified, note what practice assumes and flag the gap.
3. **The graph is the language, Python is the interpreter.** Graph logic must not inherit Python's implicit commitments (segregation principle).
4. **Fork discipline.** Different parametric choices = different theory-graphs sharing a subgraph, not variants within one graph.
5. **Direction of justification matters.** Place things based on their preconditions, not their consequences.
6. **Time symmetry is pushed upward with contingent containment.** The underlying dynamics are time-symmetric. The retarded character is contingent on external conditions.

---

## What Mike expects from you

- **Read the V2 spec before touching the graph.** Start with `V2_NOTE.md`, then the parameter inventory, then the JSON.
- **Do not optimize for a use case.** Correctness generates usefulness.
- **Do not smooth over gaps.** If something is underspecified, say so. Mike values intellectual honesty about what is and isn't known.
- **No frontend yet.** The Python API is the primary interface. Design notes for a future frontend are in IMPLEMENTATION_NOTES.md.
- **Commit and push when work is done.** GitHub repo is `abanksmemoir/parameterized-ontic-structural-realism-project` (private). Auth token is at `OneDrive/Desktop/Claude Helps Mike/claude's token.txt`. Use the `github-access` skill to set up.

---

## Next steps (prioritized)

### Near-term research

1. **OQ2 — Vacuum state justification.** Is the Poincaré-invariant vacuum derivable from anything, or is it an independent boundary condition? What happens to vacuum selection in curved spacetime? Does the absorber condition, if it selects the retarded propagator, also select the vacuum?

2. **OQ3 — Gribov ambiguity.** What justifies restricting to the first Gribov horizon? Does the choice affect observables? Currently P079 in the GAUGE node.

3. **OQ5 — Temporal parameter entanglement.** Are P036 (metric signature), P047 (Wick rotation), and P057 (iε sign) independent parameters or three aspects of a single choice? Visser (2022) on complex metric deformation is a lead.

4. **Schwinger-Keldysh bridge.** The SK (closed-time-path) formalism uses both forward and backward time contours and naturally yields retarded propagators. Does the backward contour function as an implicit absorber mechanism for non-abelian sectors? Nobody has asked this.

5. **Boundary condition persistence through phase transitions.** The retarded boundary condition, established when all gauge bosons were massless and deconfined, is assumed to persist through the electroweak (~160 GeV) and QCD (~170 MeV) transitions. This is assumed, not proven.

### Near-term engineering

6. **GR template update.** The GR template is handcoded with 18 nodes. It should ideally load from its own V2 JSON file (like SM does), with full parameter inventories and temporal notes. Consider creating `gr_dependency_graph_v2.json`.

7. **Slug generation improvement.** `_generate_slug()` in TheoryFile is naive — it concatenates the first few resolved values. Should pull theory family, logic, foundation, gauge group, generation count into the slug while ignoring convention/runtime parameters.

8. **Theory-file I/O round-trip tests.** Save a TheoryFile, reload it, verify identity. Not currently tested.

9. **Propagation with recomputation hooks.** `propagate_change()` currently only identifies affected nodes. When external tools are wired in (GAP for group theory, FeynRules for Lagrangians), it should trigger actual recomputation. The callback mechanism exists but is untested with real tools.

### Medium-term

10. **Simulation environment.** Computational sandbox for the NMK/Bajlo experimental program — modeling time-symmetric radiation fields, absorber conditions, antenna configurations. The equations are classical EM. The dependency graph provides the theoretical map.

11. **Frontend (contemplated, not urgent).** Web UI for navigating the theory lattice, toggling parameters, visualizing the DAG. Design notes in IMPLEMENTATION_NOTES.md.

---

## Repository structure

```
parameterized-ontic-structural-realism-project/
├── AGENT_BRIEFING.md              ← YOU ARE HERE
├── OPERATING_MANUAL.md            ← design philosophy & operations
├── PROJECT_BRIEFING.md            ← canonical project context
├── SUPPLEMENTARY_BRIEFING.md      ← prior art, cross-theory, time symmetry
├── IMPLEMENTATION_NOTES.md        ← technical notes, theory-nesting design
├── state_of_project_4_6_26.md     ← project status (pre-V2 package update)
├── README.md
├── sm_dependency_graph.md / .json ← V1 graph (kept for reference)
├── pyproject.toml
├── demo.py                        ← V2 demo (run this to see everything)
├── posr/                          ← Python package (V2, 69 tests)
│   ├── __init__.py               ← v2.0.0
│   ├── schema.py                 ← Parameter, Dependency, Node, TheoryGraph, TheoryFile
│   ├── graph.py                  ← build_from_json (V1+V2), resolve, propagate, validate
│   ├── diff.py                   ← structural diff, type summaries
│   ├── registry.py               ← V2 types, templates, options
│   └── templates/
│       ├── sm.py                 ← loads from V2 JSON (30 nodes)
│       └── gr.py                 ← hardcoded V2 (18 nodes)
├── tests/
│   ├── test_schema.py            ← 24 tests
│   ├── test_graph.py             ← 16 tests
│   ├── test_diff.py              ← 11 tests
│   └── test_templates.py         ← 18 tests
└── deep-research/
    └── time-symmetry-debt/
        ├── RESEARCH_BRIEFS.md
        ├── ORCHESTRATION_PROMPT.md
        ├── reports/               ← 5 agent reports + synthesis
        └── v2/                    ← AUTHORITATIVE GRAPH SPEC
            ├── V2_NOTE.md        ← START HERE
            ├── sm_dependency_graph_v2.md / .json
            ├── PARAMETER_INVENTORY.md
            └── creating-agent-notes/
```

---

## Session history

| Date | Session | What happened |
|------|---------|--------------|
| 2026-04-05 | Time-symmetry debt research | 5 parallel agents surveyed literature. V2 refactor created. Agent briefing written. Creating-agent notes saved. |
| 2026-04-06 | V2 Python package rewrite | Set up GitHub repo from desktop files. Built V1 Python package. Read V2 spec. Rewrote entire package to V2: schema.py (Parameter, Dependency types), graph.py (V2 JSON loader), templates (SM from V2 JSON, GR rewritten), registry (V2 types), diff.py (type summaries), all tests (69 passing), demo. Committed and pushed. |

---

## GitHub access

- **Repo:** `abanksmemoir/parameterized-ontic-structural-realism-project` (private)
- **Token:** `/sessions/eager-affectionate-fermi/mnt/micha/OneDrive/Desktop/Claude Helps Mike/claude's token.txt`
- **Setup:** Run `bash /path/to/.claude/skills/github-access/scripts/setup.sh`
- After setup, `git` and `curl` API calls work. No `gh` CLI in the sandbox — use `curl` with the token for API calls.
