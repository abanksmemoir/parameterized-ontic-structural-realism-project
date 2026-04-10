# White Accumulation — Simulation Specification

## Purpose
Build a minimal numerical sandbox for testing the core formal claim:

> A closure-dominated system is one whose present state is better understood as part of a globally self-consistent trajectory than as the output of purely forward local evolution.

This spec is intentionally minimal. It is not a brain simulation. It is a tractable testbed for:
- temporal closure
- non-factorizability
- closure dominance
- identity / branching behavior in trajectory space

---

## 1. Scope

### In scope
- Low-dimensional toy systems
- Discrete-time and continuous-time versions
- Comparison between:
  - retarded-only models
  - closure-aware models
- Synthetic perturbation experiments
- Binding / composition tests on coupled subsystems
- Branching and identity-distance tests

### Out of scope
- Real neuroscience
- Real EM advanced-wave modeling
- Phenomenology
- Semantic content
- Full agent behavior

---

## 2. Core Design Principles

1. The system must support both:
   - purely forward evolution
   - globally constrained trajectory selection

2. Closure must be parameterized explicitly.

3. The sandbox must produce observables that let us compare:
   - explanatory adequacy of retarded-only description
   - explanatory adequacy of closure-aware description

4. The sandbox must include nontrivial counterexamples:
   - noise
n- rigid order
- over-constrained synchrony
- weak coupling

5. All metrics should be defined over intervals, not single states.

---

## 3. Phase 1 — Minimal Scalar Toy

### 3.1 State space
Discrete time, scalar state:

- times: t = 0, 1, ..., T
- state: x_t in R

### 3.2 Retarded-only dynamics
Base local dynamics:

x_{t+1} = f(x_t)

Initial test families:
- linear: f(x) = a x
- nonlinear saturating: f(x) = a x - b x^3
- chaotic/logistic-like: f(x) = r x (1 - x)

### 3.3 Closure-aware objective
For a full trajectory X = (x_0, ..., x_T), define:

C[X] = sum_{t=0}^{T-1} alpha * ||x_{t+1} - f(x_t)||^2
      + sum_{t=1}^{T-1} gamma * ||x_t - G_t(X)||^2

Where:
- first term = local forward consistency
- second term = temporal closure constraint
- G_t(X) = global consistency operator

### 3.4 Initial global consistency operators
Implement at least three:

#### Operator A — midpoint smoothing
G_t(X) = 0.5 * (x_{t-1} + x_{t+1})

Interpretation:
- middle state should fit its temporal neighborhood symmetrically

#### Operator B — interval anchor consistency
G_t(X) = w1(t) * x_0 + w2(t) * x_T
with weights interpolating across the interval

Interpretation:
- state must fit endpoint-conditioned trajectory

#### Operator C — learned global projector
G_t(X) = projection of x_t onto a low-dimensional trajectory family inferred from the whole X

Interpretation:
- first crude stand-in for “admissible manifold”

### 3.5 Control parameter
Closure strength:
- gamma >= 0

Regimes:
- gamma = 0: open / retarded-only
- small gamma: weak closure
- large gamma: closure-dominated

---

## 4. Phase 2 — Continuous-Time Form

### 4.1 State
Trajectory X(t), t in [0, T]

### 4.2 Objective
C[X] = integral_0^T [
  alpha * ||dX/dt - F(X)||^2
  + gamma * ||X(t) - Pi[X](t)||^2
] dt

Where:
- F(X) = local dynamics
- Pi[X](t) = global consistency map acting on full trajectory

### 4.3 Numerical method
Represent X(t) on a grid.
Use:
- gradient descent on trajectory space
- or variational optimization with autodiff

Compare to direct forward integration of F.

---

## 5. Phase 3 — Binding / Non-Factorizability

### 5.1 Coupled system
State:
- X_t = (u_t, v_t)

Local dynamics:
- u_{t+1} = f_u(u_t, v_t)
- v_{t+1} = f_v(v_t, u_t)

Closure objective:
C[X] = C_u + C_v + eta * sum_t ||u_t - H(v_t)||^2

Where eta controls coupling / binding pressure.

### 5.2 Required experiments
For each parameter setting:
- optimize full system
- optimize u-subsystem alone
- optimize v-subsystem alone

### 5.3 Binding criterion
Binding is present when:
- C[u,v] is low
- C[u] and C[v] alone are high

Derived metric:
N = 1 - C[u,v] / min(C[u], C[v])

Normalize to [0,1] if needed.

Interpretation:
- low N: decomposable
- high N: non-factorizable

---

## 6. Phase 4 — Mereology / Maximal Closed Set

### 6.1 Add third weakly coupled component
State:
- X_t = (u_t, v_t, w_t)

Design w_t so that:
- sometimes it improves closure
- sometimes it degrades closure

### 6.2 Goal
Test whether the optimal subject-like set is:
- {u,v}
- {u,v,w}
- {u}
- etc.

### 6.3 Maximality criterion
For candidate subset S:
- compute C_S[X^S]
- compute N_S
- define score:

Score(S) = -C_S + lambda1 * N_S - lambda2 * Degeneracy(S)

Choose maximal subset by score.

This is the first computational version of temporal mereology.

---

## 7. Phase 5 — Identity, Branching, and Distance Between Minds

### 7.1 Trajectories
Let T1 and T2 be two optimized trajectories.

### 7.2 Subject-unification functional
Define:

d_mind(T1, T2) = min over T* [ C[T*] + distortion(T1, T2 -> T*) ]

Where T* must embed both trajectories over chosen intervals.

### 7.3 Test cases
#### Case A — same system, adjacent intervals
Expect low distance.

#### Case B — same system after gradual parameter drift
Expect moderate distance.

#### Case C — duplicated trajectory with branching futures
Expect distance near zero at split point, then rapid rise.

#### Case D — unrelated systems
Expect large distance.

### 7.4 Outputs
- distance curves over time
- branch penalty curves
- continuity threshold candidates

---

## 8. Closure Dominance Parameter

### 8.1 Retarded-only fit error
Given observed or optimized trajectory X:

E_R(X) = min over local models F sum_t ||x_{t+1} - F(x_t)||^2

### 8.2 Closure-aware fit error
E_RC(X) = min over F, G [
  sum_t alpha * ||x_{t+1} - F(x_t)||^2
  + sum_t gamma * ||x_t - G_t(X)||^2
]

### 8.3 Parameter
Omega_closure(X) = 1 - E_RC(X) / (E_R(X) + eps)

Interpretation:
- near 0: retarded-only description sufficient
- near 1: closure-aware description materially superior

### 8.4 Mind-likeness score
M(X) = Omega_closure(X) * N(X)

Interpretation:
- high closure dominance + high non-factorizability = candidate conscious-like regime

---

## 9. Failure Modes to Simulate Explicitly

### 9.1 Noise
Generate random trajectories.
Expected:
- low closure dominance
- low non-factorizability

### 9.2 Rigid periodic systems
Examples:
- constant signal
- perfectly periodic oscillator
Expected:
- apparent persistence
- low nontriviality
- likely degenerate closure

### 9.3 Over-constrained synchrony
Coupled units with extremely strong eta.
Expected:
- high coherence
- collapse of admissible trajectory richness
- seizure analogue

### 9.4 Weak coupling
Set eta ~ 0.
Expected:
- no binding
- no maximal closed whole

### 9.5 Edge regime
Tune parameters to find narrow band where:
- closure dominance high
- non-factorizability high
- degeneracy not too high

This is the target region.

---

## 10. Degeneracy Penalty

Need an explicit term to exclude trivial closure.

Candidate degeneracy measures:
- variance of admissible trajectories under perturbation too low
- Lyapunov-like responsiveness too low
- complexity of optimized trajectory too low
- rank / dimension of trajectory manifold too low

Initial proxy:
Degeneracy(X) = exp(-k * trajectory_variance(X))

Or more robustly:
Degeneracy(X) high when perturbations leave trajectory unchanged in a trivial way.

---

## 11. Numerical Workflow

### 11.1 For each system family
1. Choose parameters
2. Generate initial trajectory guess
3. Optimize closure-aware objective
4. Fit best retarded-only model
5. Compute:
   - C[X]
   - E_R
   - E_RC
   - Omega_closure
   - N
   - M
   - Degeneracy
6. Perturb trajectory and repeat
7. Sweep across parameters

### 11.2 Parameter sweeps
Sweep:
- gamma (closure strength)
- eta (coupling / binding)
- nonlinearity parameters
- noise level
- dissipation parameters

Goal:
map regions of:
- no closure
- trivial closure
- closure-dominated nontrivial regimes

---

## 12. Visualization Requirements

Generate:
- trajectory plots
- heatmaps of Omega_closure across parameter space
- heatmaps of N across parameter space
- combined M score maps
- branching distance plots
- degeneracy maps

Most important figure:
> phase diagram showing target band where closure is high, binding is high, and degeneracy is low

---

## 13. Success Criteria

The sandbox is successful if it demonstrates all of the following:

1. There exist regimes where closure-aware models substantially outperform retarded-only models.
2. There exist regimes where whole systems satisfy closure and parts do not.
3. There exist regimes where trivial coherence is distinguishable from nontrivial closure.
4. Identity/branching cases can be represented by the unification functional.
5. A narrow parameter band emerges between under-constrained and over-constrained regimes.

---

## 14. Minimal Implementation Stack

Suggested stack:
- Python
- NumPy
- SciPy
- JAX or PyTorch for autodiff and trajectory optimization
- Matplotlib for plots

Project modules:
- dynamics.py
- closure_objectives.py
- optimize.py
- metrics.py
- experiments.py
- plots.py

---

## 15. Immediate Build Order

### Milestone 1
Implement scalar discrete-time toy.
Deliverables:
- optimizer
- trajectory plots
- Omega_closure curve vs gamma

### Milestone 2
Implement 2-variable binding system.
Deliverables:
- N metric
- phase plots over gamma x eta

### Milestone 3
Add degeneracy penalties and classify failure modes.
Deliverables:
- phase diagram with target band

### Milestone 4
Add branching / identity distance experiments.
Deliverables:
- d_mind curves for same / branch / unrelated systems

### Milestone 5
Write interpretation memo linking results back to white accumulation.

---

## 16. Questions for the Next Agent

1. What is the best simple choice of global operator G_t(X) or Pi[X] that makes closure nontrivial but computable?
2. Can the closure functional be rewritten in a more elegant variational form?
3. What is the best normalized non-factorizability score?
4. How should degeneracy be penalized so crystals and seizures are excluded cleanly?
5. Does the subject-unification functional behave metric-like, or should it remain a pre-metric / cost functional?
6. What is the narrowest toy that already shows branching identity behavior?

---

## 17. One-Sentence Goal

Build the smallest numerical system in which the present state is better explained as part of a globally self-consistent trajectory than as the output of past-directed propagation alone.

