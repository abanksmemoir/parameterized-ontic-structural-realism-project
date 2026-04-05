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

## Limitations and Future Work

### Current Scope (v0.1.0)

- Graph schema and core operations
- SM and GR templates
- Basic parametric choice resolution
- Cross-theory diff and comparison

### Not Yet Implemented

1. **Parametric propagation**: When a choice at a lower node is toggled, automatically recompute dependencies
2. **Wrapping external tools**: Integration with GAP, LieART, FeynRules, SARAH
3. **Interactive exploration**: UI/web interface for navigating the lattice
4. **Anomaly computation**: Actual algebraic verification of anomaly cancellation
5. **Unification frameworks**: Explicit modeling of KK, string theory, other unification proposals
6. **More theories**: Beyond SM and GR (QED, Weak interaction alone, ΛCDM, etc.)

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
