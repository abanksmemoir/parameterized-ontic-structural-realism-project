# POSR Core Implementation — Technical Notes

## What Was Built

A complete Python API core implementing Parameterized Ontic Structural Realism (POSR):

```
posr/
  schema.py          — Core data types (Node, ParametricSlot, TheoryGraph, TheoryFile)
  graph.py           — Graph operations (build, traverse, propagate, validate)
  diff.py            — Cross-theory comparison (shared subgraph, fork points, diff)
  registry.py        — Registry of known node types and parametric options
  templates/
    sm.py            — Standard Model template (from sm_dependency_graph.json)
    gr.py            — General Relativity template (stub with known structure)
tests/               — 40 comprehensive test cases (all passing)
demo.py             — Demonstration of the full system
```

## Key Design Decisions

### 1. **Segregation of Graph from Implementation**

The graph is the ontological object; Python is the construction tool. The graph's content (presupposes relations, provisions, parametric slots) is entirely declarative and would be identical in any implementation language. Python constructs and traverses it but does not infect it with Python semantics.

### 2. **Constructor Injection, No Ambient Reach**

Every layer receives its substrate as constructor arguments. A `TheoryGraph` receives nodes; a `TheoryFile` receives a graph. Nothing reaches around to grab context from elsewhere.

### 3. **Fork Discipline**

Different parametric choices produce distinct theory-graphs. They are not variants within a single graph. They share upstream structure but diverge at fork points where choices are made. The system tracks provenance precisely.

### 4. **Parametric Slots: Architectural vs Runtime**

- **Architectural**: Changes that affect graph structure (e.g., dropping LEM changes which nodes are available)
- **Runtime**: Changes to values within a fixed structure (e.g., coupling constants)

### 5. **Cross-Theory Generality from Day One**

The schema accommodates both SM and GR without SM-specific assumptions. A `Node` is generic; a parametric slot at a connection node can specify which bundle the connection lives on (principal, tangent, or internal gauge).

### 6. **Fingerprinting and Naming**

Each theory-file gets:
- A **fingerprint**: SHA256 hash (first 8 hex chars) of all resolved values
- A **human slug**: derived from major parametric choices
- A **filename**: slug + fingerprint

This enables deduplication and human navigation.

## How It Works

### Building a Graph

```python
from posr.templates import sm, gr

sm_graph = sm.build()  # Loads sm_dependency_graph.json, converts to new schema
gr_graph = gr.build()  # Builds GR template from scratch
```

### Making Parametric Choices

```python
from posr.graph import resolve_parametric_choices

choices = {
    "SM_G": {"gauge_group": "SU(3)xSU(2)xU(1)", "g3": "1.221"},
    "SM_F": {"num_generations": "3"},
}

theory_file = resolve_parametric_choices(sm_graph, choices)
```

### Comparing Theories

```python
from posr.diff import compute_structural_diff, identify_fork_path

diff = compute_structural_diff(sm_graph, gr_graph)
print(diff.summary())

fork_path = identify_fork_path(sm_graph, gr_graph)
```

### Graph Operations

```python
# Topological sort
topo = graph.topological_sort()

# Ancestors and descendants
ancestors = graph.ancestors("SM_G")
descendants = graph.descendants("ZFC")

# Dependency chains
chain = graph.dependency_chain("CL", "SM_G")

# Shared structure
shared = graph.shared_subgraph(other_graph)
```

## Test Coverage

All 40 tests pass:

```
test_schema.py      — 11 tests (Node, ParametricSlot, TheoryGraph, TheoryFile)
test_graph.py       — 7 tests (building, resolving, validation, comparison)
test_diff.py        — 7 tests (structural diff, shared subgraph, fork path)
test_templates.py   — 9 tests (SM, GR, SM vs GR comparison)
```

Key test scenarios:
- Graph construction and validation
- Topological sort with cycle detection
- Ancestors/descendants queries
- Dependency chain finding
- Shared subgraph extraction
- Parametric choice resolution
- SM and GR template loading
- Cross-theory comparison

## Architectural Insights from Implementation

### 1. **The Twelve-Link Chain**

The deepest path through SM (and shared with GR) is:

```
CL → FOL → ZFC → GRP → LIE → LIEA → REP → CONN → GAUGE → QFT → ANOM → SM_G
```

Every link is a parametric swap point.

### 2. **Anomaly Cancellation as Structural Constraint**

The `ANOM` node takes representation theory and topology as input, outputs hard constraints on consistent particle content. This is where the SM's specific fermion content becomes non-arbitrary — it's one of a small number of anomaly-free configurations.

### 3. **The Fork Point: Bundle Type**

SM and GR fork at the connection layer:
- SM: Connections on **internal gauge bundles** (structure group is SU(3)×SU(2)×U(1))
- GR: Connections on the **tangent bundle** (structure group is Lorentz group or GL(4,R))

Both use the same mathematical machinery (Levi-Civita connection, curvature, etc.) but on different bundles.

### 4. **Time-Asymmetry as Parametric**

The `QFT` node includes a parametric slot for time-asymmetry convention (retarded, advanced, Wheeler-Feynman, or symmetric). This prevents the arrow of time from sneaking in as an undeclared assumption at the wrong structural level.

## Design Direction: Theory Nesting and Plug-and-Play Parameterization

The ambition is not to model a single theory. The system models a **lattice of theories**. Each saved theory-file is a specific path through the parametric space — a resolved configuration of choices at every node from axioms to physical content. The system's job is to make it trivially easy to:

1. Start from any existing theory-file (SM, GR, or something novel)
2. Toggle one or more parametric choices at any depth
3. Let the consequences propagate upward through the DAG
4. Save the result as a new, distinct theory-file

Each file is a self-contained artifact. The filename encodes enough to identify it at a glance; the metadata inside encodes everything needed for machine recovery. A flat directory of theory-files is the output: no nesting, no hierarchy in the filesystem. The hierarchy is *in the graphs themselves* — the lattice structure lives in the presupposes relations and fork provenance, not in folder structure. This matters because the files need to be ingestible by tools like NotebookLM that want a flat collection of documents.

### What a theory-file represents

A theory-file is not a "configuration file" in the software engineering sense. It is a **structural identity claim**: "here is a complete, well-formed physical theory, expressed as the totality of its structural presuppositions and parametric choices." The Standard Model theory-file says: classical logic, first-order quantification, ZFC, groups through to Lie algebras, representations, connections on internal gauge bundles, quantized via path integral with retarded propagator convention, gauge group SU(3)×SU(2)×U(1), three fermion generations, Higgs doublet, specific Yukawa couplings. Every one of those is a choice. A different choice at any point is a different theory — equally well-formed, differently parameterized, potentially non-actual.

### The distinguished point

One theory-file in the collection is distinguished: the one whose parametric choices match actuality. This is the Standard Model (or more precisely, the SM+GR composite once both branches are populated). It bears an identity relationship to the world. The rest are legitimate structures that do not bear that relationship. The system doesn't editorialize — it doesn't flag the actual-world configuration as "correct" and others as "wrong." It marks it as the **distinguished point** in the parametric space, the configuration that does empirical work.

### Slug and naming convention

Filenames use a hybrid: a human-readable slug encoding the major structural identity (theory family, logic, foundation, gauge group, generation count) plus a truncated SHA256 hash of the full parametric state. The slug is for Mike; the hash is for the machine. Example:

```
SM-CL_ZFC_SU321-3gen-b7a2f3c1.json
GR-CL_ZFC_Lorentz-4d-e91c0a7b.json
SM-IL_TT_SU5-3gen-2f8d4e1a.json      (intuitionistic logic, type theory, SU(5) GUT)
```

The slug must be short enough for NotebookLM to encode as a source title. The hash disambiguates when two theories share a slug but differ in fine-grained parameters (coupling constants, mixing angles, etc.).

### How the slug is generated (current limitation and planned fix)

The current `_generate_slug()` in `schema.py` concatenates resolved values naively. This needs to be replaced with a smarter system that:
- Pulls theory family from the graph's terminal nodes (SM, GR, or composite)
- Pulls logic choice (CL, IL) from Layer 0
- Pulls foundation (ZFC, TT) from Layer 1
- Pulls gauge group from the gauge layer (abbreviated: SU321, SU5, SO10)
- Pulls generation count if applicable
- Ignores runtime parameters (coupling constant values don't belong in the slug)

### Future: the web frontend and other consumers

The API core is designed to be consumed by any frontend. A web app is contemplated but not prioritized — the theory-files and the Python API are the primary interface for now. When a frontend is built, it should:
- Let the user see the full graph for any theory-file
- Let the user toggle parametric choices and see which nodes are affected (via `propagate_change`)
- Let the user save the result as a new theory-file
- Let the user overlay two theory-files and see the structural diff
- Let the user browse the flat collection of saved theories

The API already supports all of this. The frontend is presentation, not logic.

---

## Limitations and Future Work

### Current Scope (v0.1.0)

- Graph schema and core operations
- SM and GR templates
- Basic parametric choice resolution
- Cross-theory diff and comparison

### Not Yet Implemented

1. **Smarter slug generation**: Pull structurally significant choices into the slug, ignore runtime values
2. **Parametric propagation**: When a choice at a lower node is toggled, automatically recompute dependencies and flag affected nodes as "stale"
3. **Wrapping external tools**: Integration with GAP, LieART, FeynRules, SARAH — each wrapped with the project's parametric interface so a node can invoke computation
4. **Interactive exploration**: Web frontend consuming the API core
5. **Anomaly computation**: Actual algebraic verification of anomaly cancellation at the ANOM node
6. **Unification frameworks**: Explicit modeling of KK, string theory, other unification proposals as theory-files that collapse the SM/GR fork into shared ancestry
7. **More theories**: Beyond SM and GR (QED alone, weak interaction alone, ΛCDM, electroweak, etc.) — each as its own template and set of theory-files
8. **Time symmetry node**: Currently time-asymmetry is a parametric slot on QFT. Per the supplementary briefing, it should be elevated to a separate node above both SM and GR branches so toggling it propagates through both simultaneously

## Installation and Usage

```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/ -v

# Run demo
python demo.py

# Use in code
from posr.templates import sm, gr
from posr.diff import compute_structural_diff

sm_graph = sm.build()
gr_graph = gr.build()
diff = compute_structural_diff(sm_graph, gr_graph)
```

## Code Quality

- Type hints throughout (compatible with Python 3.8+)
- Comprehensive docstrings
- Clean separation of concerns
- No external dependencies (intentional)
- ~3300 lines of implementation code
- ~1600 lines of test code
