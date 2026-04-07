# Project Briefing: Parameterized Ontic Structural Realism

**Origin session:** 2026-04-05
**Repo:** https://github.com/abanksmemoir/parameterized-ontic-structural-realism-project
**Local:** `C:\Users\micha\OneDrive\Desktop\parameterized ontic structural realism project`

---

## What this project is

Software that implements the Standard Model's structural dependency graph from logical axioms up, parameterized and docile at every layer. The novel contribution is the connective tissue — the explicit mapping of what presupposes what, all the way from axiom choice to particle content. Nobody in philosophy of physics or mathematical physics has produced this synthesis. The pieces exist; the assembly doesn't.

---

## The philosophical stance

Mike's epistemological framework is not standard ontic structural realism (OSR) as found in French, Ladyman, or McKenzie. It departs from the published literature in specific ways that are load-bearing for the project:

### 1. Genuine realism

"Real" in the ontic sense is whatever concatenation of parameterized, well-formed primitives bears an identity relationship to the world we live in. This is a genuine realist commitment — there is a definite structure, and science is in the business of honing in on a formal recapitulation of it.

### 2. The instrumental lattice

Even realists in this sense are interested in a broader class of theories. Approximations of the target structure earn their keep by supporting counterintuitive, nontrivial inferences and providing frameworks for engineering and world-navigation via their intelligibility more generally. The lattice of well-formed hypotheticals is the navigational space within which you converge on the ontic target — not a substitute for it.

### 3. No brute contingency

OSR philosophers like McKenzie worry that the Standard Model's specific parameters (coupling constants, mixing angles, generation count) are "non-structural contingencies" that resist structural explanation. Mike's response: this smuggles in a non-structural substrate that selects which structures get instantiated, which is exactly what OSR is supposed to eliminate. The actual world is a structural configuration, full stop. "Why this structure?" either bottoms out in further structure or the question is malformed.

### 4. Instrumental Platonism

The lattice is animated by a covert methodological Platonism, but this is a meta-theory Mike uses rather than commits to as an ontological posit. The Platonism provides navigational medium without collapsing the ontology into any particular corner.

### 5. No side-picking on modality

The project doesn't need to choose between Tegmark's mathematical universe (all consistent structures exist) and structural necessitarianism (only one self-consistent totality). That choice is downstream from axiom selection, which is itself parametric. The lattice doesn't have a top node.

### 6. "Geometry" is already structure

To say something "is geometry" is underdetermined — there are many geometries downstream from different axiom sets. To BE geometry is to be a kind of structure downstream from a choice of axioms. This dissolves the Calabi-Yau selection problem: the topology is part of the total structural fact, not something chosen from a landscape by an external principle.

---

## Why this matters for the software

These aren't philosophical decorations. They are architectural requirements:

- The system cannot hardcode any mathematical convention as if it were structurally primitive. Every presupposition must be declared and parameterized.
- The system cannot treat the Standard Model's specific content as arbitrary — it's the distinguished point in the parametric space, the configuration that bears an identity relationship to actuality. But the system must also model the surrounding lattice of well-formed alternatives.
- The system cannot assume a single foundational framework (ZFC, type theory, category theory) as privileged. Foundations are a parameter.

---

## Architectural decisions

### Docility

Each layer must be docile: a black box only in the sense that it has a clean interface, but it cannot smuggle in commitments that aren't declared in its parameters. No ambient assumptions, no hidden imports from mathematical context that aren't explicitly wired in.

### Functorial composition

Each layer is a functor: axioms in, structural consequences out. Composition is explicit. Swap the logic at the bottom and the consequences should propagate upward — the gauge theory layer should ripple without crashing or silently absorbing the change into hardcoded assumptions.

### Dependency graph, not pipeline

The system is a DAG, not a linear stack. You need to be able to pull on any node and see what moves. Cross-layer dependencies matter (e.g., connections depend on both fiber bundles from geometry and Lie algebras from algebra — this is where geometry and algebra merge).

### Segregation of Python logic from graph logic

The graph is the ontological object. Python is the construction tool. The two must be cleanly separated: Python builds, traverses, and manipulates the graph, but the graph's structural content does not inherit Python's implicit commitments (classical logic, ZFC-ish set theory, sequential evaluation). If the same graph were rebuilt in Haskell or Lean, the graph should be identical — the implementation language is interchangeable; the graph is not.

This means the graph needs its own internal logic — its own declared inference rules, its own composition semantics — and Python serves as the runtime that executes those rules. Python is the interpreter, not the language. The parameterization occurs as a kind of projection from the programming language: the graph is something we construct with Python, and the construction process is where the segregation discipline lives.

### Constructor injection, no ambient reach

Every layer is a class that receives its entire structural substrate as constructor arguments. The logic layer hands the algebra layer its permitted inference rules. The algebra layer hands the gauge theory layer its group-theoretic toolkit. Nothing reaches around its interface to grab something from a layer it shouldn't know about.

---

## The dependency graph (v0.1.0)

Ten layers, ~30 nodes. See `sm_dependency_graph.json` for the machine-readable graph and `sm_dependency_graph.md` for the annotated reference.

**Layers:** Logic → Foundations → Core algebra → Topology & analysis → Lie theory → Differential geometry → Functional analysis & quantization → Classical field theory → Quantum field theory → Standard Model

**Key structural observations:**

- **Deepest chain:** Classical logic → FOL → ZFC → Groups → Lie groups → Lie algebras → Representations → Connections → Gauge theory → QFT → Anomaly cancellation → SM fermion content (12 links, each a parametric swap point)
- **Most constrained node:** Anomaly cancellation — takes representation theory and topology as input, outputs hard constraints on consistent particle content. The structural realist's strongest card.
- **Fattest parametric nodes:** All at the Standard Model layer — generation count, coupling constants, gauge group choice. These are the coordinates in structural space, not brute contingencies.
- **Critical merge point:** Connections & curvature (Layer 5) — where fiber bundle geometry and Lie algebra meet. The connection on a principal bundle IS a Lie-algebra-valued 1-form. This is the node where the KK holonomy framework lives.

---

## Existing tools that do partial work

| Layer | Tools | What they cover |
|-------|-------|----------------|
| Logic/Foundations | Lean (mathlib), Coq, Isabelle | Formalized mathematics with explicit axiom dependencies |
| Algebra | GAP, LieART | Computational group theory, Lie algebra representations |
| Gauge/Physics | FeynRules, SARAH | Lagrangian from gauge group + particle content → Feynman rules, RGE, anomaly conditions |
| Simulation | Lattice QCD (MILC), lattice gauge theory | Parameterized gauge group, representation content, couplings |

The novel contribution is the connective tissue between these — the explicit structural dependency mapping that none of them provide.

---

## What to avoid

1. **Don't collapse into a textbook.** This is not "implement the Standard Model in Python." It's "implement the Standard Model's structural dependency graph such that every presupposition is declared and swappable." The distinction is everything.

2. **Don't treat any layer as foundationally privileged.** ZFC is not "the right foundation" — it's one parametric choice. The system must be able to receive a different foundation and propagate consequences.

3. **Don't hardcode mathematicians' conventions.** When implementing SU(3), most code presupposes compactness, Lie group theory, manifold structure without declaring it. This system must make all of that parametric.

4. **Don't let Python's logic leak into the graph's logic.** Python constructs the graph; it doesn't infect it. The graph has its own declared inference rules and composition semantics. Python is the interpreter, not the language. If a structural relationship in the graph only holds because of how Python evaluates expressions, that's a bug.

5. **Don't get seduced by completeness.** The v0.1 graph has ~30 nodes. Each could be deepened with internal sub-dependencies. Build the skeleton first, deepen iteratively.

6. **Don't ask Mike to code.** Mike directs, never codes. Claude implements everything. Mike evaluates output, not code. Protect his flow state — but do not take shortcuts that will "make Mike happy locally" in ways that undermine the core objectives of parameterization and faithfulness to the technically rigorous subject matter. Mike engages with this material epistemically and metaphysically but not at the level of technical granularity. If you need to explain something to him, do so. We cannot afford mistakes. If Mike "does not get it," abstract to a higher level while maintaining the correct relationship to the underlying technicalities until it's clear.

---

## Next steps (from founding session)

1. Deepen each node with internal sub-dependencies
2. Map existing software packages to each node
3. Design the Python class architecture: each layer as a class receiving its substrate as constructor arguments
4. Identify which "parametric" annotations are runtime parameters vs. architectural choices
5. ~~Initialize the GitHub repo with the graph files and this briefing~~ ✓
