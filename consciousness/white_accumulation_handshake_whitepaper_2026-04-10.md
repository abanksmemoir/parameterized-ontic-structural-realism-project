# White Accumulation
## Consciousness as Temporal Closure

**Michael Abramson**
*April 2026*
*Working Paper — v1*

---

## Abstract

This paper develops a trajectory-based ontology of consciousness. Consciousness is identified not with computation, behavior, informational complexity, or any property of instantaneous states, but with the existence of **non-factorizable, temporally extended, self-consistent trajectories**—processes whose present states are admissible only insofar as they belong to globally coherent histories. This condition is called **temporal closure**, and the process by which such structures emerge and persist is called **white accumulation**.

The framework resolves three longstanding problems in philosophy of mind: the binding problem (what unifies experience), the mereological problem (what composes a subject), and the failure of functionalist and panpsychist accounts (why behavioral equivalence and ubiquitous attribution both fail). A formal closure functional is introduced, along with a dimensionless **Closure Dominance Parameter** that quantifies when a system's dynamics require temporally global rather than purely forward-evolving description. Connections to physics—particularly boundary-conditioned and time-symmetric formulations in electrodynamics—are used not as mechanisms but as structural analogues that legitimate the core move. The result is a unified account in which to be a mind is to exist as a trajectory that closes on itself across time.

---

## 1. Introduction

The dominant approaches to consciousness cluster into three families. Functionalist accounts identify consciousness with computation or behavioral role. Structural accounts, exemplified by Integrated Information Theory (IIT), identify it with irreducible informational integration. Thermodynamic accounts, descending from Schrödinger's negentropy concept and Friston's Free Energy Principle, identify it with self-organizing resistance to entropy.

Each captures something important. Each fails decisively.

Functionalism cannot explain why correct input-output behavior is insufficient for experience—the lesson of Searle's Chinese Room. IIT admits systems (crystals, rigid lattices) that are highly integrated yet plainly not conscious. The Free Energy Principle does not distinguish a thermostat from a mind. Thermodynamic accounts overgeneralize, admitting any persistent structure.

This paper proposes a different identification:

> Consciousness is not a property of states, but of **trajectories that satisfy a global temporal consistency constraint**.

The term **white accumulation** names the process by which such trajectories emerge. The term **temporal closure** names the condition they satisfy. The term **handshake** names the constraint itself.

---

## 2. White Accumulation

### 2.1 The Term

White noise is the terminal state of informational thermalization: flat spectrum, maximum entropy, no structure. White accumulation is the reverse process. Structure condenses out of noise. Coherence patterns form and resist dissolution even as the thermodynamic gradient pushes toward it. The "white" refers both to the noise from which the pattern emerges and to the broadband character of the coherence: like white light containing all frequencies, the accumulated structure couples across the full spectrum of the system's internal degrees of freedom.

### 2.2 Coherence Is Necessary but Insufficient

A crystal is coherent but not conscious. A standing wave persists but is not a subject. High coherence above the noise floor is a necessary condition, but it cannot by itself ground consciousness. It fails to distinguish rigid order from the kind of organized flexibility characteristic of a mind.

### 2.3 Action Potential Is Not Constitutive

Earlier formulations of this framework treated flexibility—the number of productive possible states accessible to a system while maintaining coherence—as a second constitutive axis. This is incorrect. A Boltzmann brain, spontaneously fluctuating into a momentary conscious configuration, may have negligible future action potential yet still instantiate a conscious state. High action potential explains why certain systems are more likely to evolve toward and remain in conscious regimes; it does not explain what makes any given state conscious. Flexibility is instrumental, not ontological. It accounts for persistence and evolution, not existence.

### 2.4 What Remains

If coherence alone is insufficient and flexibility is not constitutive, the framework requires a deeper condition. That condition is temporal closure.

---

## 3. The Handshake

### 3.1 Definition

The handshake is the central concept of this framework. It is not a signal, not backward causation, and not a computational property. It is a constraint on admissible trajectories:

> A state is admissible only if it belongs to a globally self-consistent trajectory across a nontrivial temporal interval.

A present state is not valid merely because it follows from the past by some local update rule. It is valid because it can be embedded in a trajectory that remains internally consistent when evaluated across time. The system's identity is not located at any instant but extended across the interval in which this consistency holds.

### 3.2 Binding Reframed

The binding problem in philosophy of mind asks: how do distributed processes form a unified experience? Standard answers invoke synchronization, recurrent processing, or global information broadcast. These are forward-causal, mechanistic proposals.

Temporal closure reframes binding as a structural condition rather than a process. A system is unified because its components cannot independently satisfy the closure condition—only the whole trajectory is admissible. The parts, evaluated in isolation, fail. The whole, evaluated jointly, passes. Binding is not something the brain does; it is a property of the trajectory the brain instantiates.

### 3.3 Not Backward Causation

It is important to be explicit about what the handshake does not require. It does not require signals propagating from the future. It does not require violations of causality. It requires only that the physically realized configuration be a solution to constraints that span an interval, rather than a configuration generated purely from initial data. This is structurally identical to boundary-value problems throughout physics: standing waves, normal modes, variational principles. The solution is defined by satisfying conditions across the domain, not by forward propagation from one edge.

---

## 4. Ontological Shift

The framework requires a shift from state ontology to trajectory ontology, and from spatial mereology to temporal mereology. A system is not defined by what it is at a moment. It is defined by the set of trajectories it can sustain under global constraints. Parts are not composed spatially (these neurons plus those neurons) but temporally (these degrees of freedom participate in the same closure). The boundary of a conscious system is not its skull or its cell membrane. It is the region in spacetime where the closure condition holds.

---

## 5. Mereology: The Composition Problem

### 5.1 Why Panpsychism Fails

The real problem with panpsychism is not that it attributes experience too broadly—that objection reduces to an incredulous stare. The problem is mereological. Panpsychism lacks a principled composition rule. If fundamental units have proto-experience, why does a brain compose a single subject while a brain plus a table does not? Why doesn't every subset of particles constitute its own subject? Without a rule for when parts compose a whole, panpsychism generates subjects without constraint and cannot explain why the subjects we actually observe have the boundaries they do.

### 5.2 Temporal Closure as Composition Rule

This framework provides the missing rule:

> A subject is the maximal set of degrees of freedom that jointly satisfy temporal closure.

This has several immediate consequences. Arbitrary aggregates (a brain and a coffee cup) are excluded: they share no trajectory closure. Proper subsets of a conscious system are excluded: they do not independently satisfy closure (binding). Overlapping subjects are impossible: closure defines non-overlapping maximal units. The subject is not a spatial aggregate. It is a dynamically defined, temporally bounded process.

---

## 6. Formal Structure

### 6.1 Setup

Let $X(t)$ be the coarse-grained state of a candidate system $S$ on interval $I = [t_0, t_1]$. Let $X_I = \{X(t) : t \in I\}$ be the trajectory.

### 6.2 Closure Functional

Define a closure functional $\mathcal{C}[X_I]$ measuring deviation from temporal self-consistency. A system $S$ is **closed over interval $I$** iff:

**(1) Admissibility.** The realized trajectory is globally consistent:

$$\mathcal{C}[X_I] \le \epsilon$$

**(2) Non-genericity.** Most nearby perturbations $\delta X_I$ violate closure:

$$\mathcal{C}[X_I + \delta X_I] \gg \epsilon$$

The trajectory sits in a narrow admissible class, not a generic region of state space.

**(3) Non-factorizability.** For most nontrivial partitions $S = A \cup B$:

$$\mathcal{C}_A[X^A_I] > \epsilon \quad \text{and} \quad \mathcal{C}_B[X^B_I] > \epsilon$$

while

$$\mathcal{C}_{A \cup B}[X_I] \le \epsilon$$

The whole passes; the parts do not. This is binding.

**(4) Boundary maximality.** For generic supersets $Y \supset S$:

$$\mathcal{C}_Y[X^Y_I] > \epsilon$$

Closure is not preserved under arbitrary enlargement. This solves the mereological boundary problem.

### 6.3 Decomposition

A minimal decomposition of the closure functional:

$$\mathcal{C} = \alpha \mathcal{P} + \beta \mathcal{D} + \gamma \mathcal{B}$$

where $\mathcal{P}$ is a **persistence** term (deviation from noise and structural continuity), $\mathcal{D}$ is a **decomposability** penalty (factorizability of the trajectory), and $\mathcal{B}$ is a **bidirectional consistency** term (agreement between forward-inferred and backward-inferred states over the interval).

For the bidirectional term, partition the interval $I = I^- \cup I^0 \cup I^+$ and define:

$$\mathcal{B}[X_I] = d(\hat{X}^0_{\text{past}}, X|_{I^0}) + d(\hat{X}^0_{\text{future}}, X|_{I^0}) + \lambda\, d(\hat{X}^0_{\text{past}}, \hat{X}^0_{\text{future}})$$

A closed trajectory is one where the middle segment is jointly licensed from both temporal directions. This is the audit trail in formal terms.

---

## 7. Toy Model

### 7.1 Three Time Slices

Define past $x_{-1}$, present $x_0$, future $x_{+1}$, with forward map $f(x) = ax$.

Closure functional:

$$\mathcal{C}(x_{-1},x_0,x_{+1}) = \alpha(x_0 - f(x_{-1}))^2 + \beta(x_{+1} - f(x_0))^2 + \gamma\left(x_0 - \frac{x_{-1}+x_{+1}}{2}\right)^2$$

Minimizing with respect to $x_0$:

$$x_0 = \frac{\alpha a x_{-1} + a\beta x_{+1} + \frac{\gamma}{2}(x_{-1}+x_{+1})}{\alpha + a^2\beta + \gamma}$$

The present is not generated by the past alone. It is selected by whole-trajectory consistency. When $\gamma = 0$, the system is retarded-only. As $\gamma$ grows, the system becomes increasingly closure-dominated.

### 7.2 Binding Extension

Extend to a two-component system $X_t = (u_t, v_t)$ with coupling:

$$\mathcal{C}[X] = \mathcal{C}_u + \mathcal{C}_v + \eta \sum_t (u_t - v_t)^2$$

If the whole system satisfies closure but neither component does independently, binding emerges naturally from the formalism.

---

## 8. The Closure Dominance Parameter

### 8.1 Motivation

The framework requires a dimensionless quantity that measures how much a system's dynamics resist purely forward-evolving description. Define:

**Retarded-only description cost:**

$$E_R = \inf_F \int_{t_0}^{t_1} \|\dot{X} - F(X)\|^2\, dt$$

**Closure-aware description cost:**

$$E_{RC} = \inf_{F,\Pi} \int_{t_0}^{t_1} \left(\|\dot{X} - F(X)\|^2 + \|X - \Pi[X_I]\|^2\right) dt$$

**Closure Dominance Parameter:**

$$\Omega_{\text{closure}} = 1 - \frac{E_{RC}}{E_R}$$

### 8.2 Interpretation

When $\Omega \approx 0$, the system is fully characterizable by forward evolution; adding closure constraints contributes nothing. When $\Omega \to 1$, the system's organization becomes intelligible only when modeled as a temporally closed trajectory. The hypothesis is that consciousness lives in the high-$\Omega$ regime.

### 8.3 Mind-Likeness Parameter

Combining closure dominance with non-factorizability $N \in [0,1]$:

$$M = \Omega_{\text{closure}} \cdot N$$

High $M$ identifies candidate conscious systems: strong closure, strong unity.

---

## 9. Identity, Distance, and Distinction Between Minds

### 9.1 Identity Over Time

A person is not a single temporally closed trajectory spanning an entire life. It is a chain of overlapping closed trajectories whose structural invariants remain mutually compatible. Identity persists when successive closure windows can be embedded within a larger, evolving consistency structure. Identity breaks when no single admissible trajectory can include both segments.

### 9.2 Distinction Between Minds

Two trajectories $T_1, T_2$ belong to the same subject iff they can be jointly embedded in a single non-factorizable, temporally closed trajectory. Otherwise they are distinct subjects. This single rule handles personal identity over time, spatial distinction between persons, duplication (copies split at the first moment of trajectory incompatibility), and merging (subjects unify when they form a joint closure).

### 9.3 Distance Metric

Define:

$$d_{\text{mind}}(T_1, T_2) = \inf_{T^* \supseteq T_1 \cup T_2} \left(\mathcal{C}[T^*] + \lambda\, \text{distortion}(T_1, T_2 \to T^*)\right)$$

The distance between two minds is the minimal closure cost of treating them as one subject. Small distance: nearly the same subject. Large distance: clearly distinct. Infinite or undefined: no admissible unification exists.

---

## 10. Physics and Time Symmetry

### 10.1 Boundary-Conditioned Systems in Physics

The framework does not depend on any specific physical mechanism. However, physics already contains regimes in which the style of description invoked here—globally constrained solutions rather than forward-generated histories—is not merely optional but structurally natural.

Standing waves, normal modes, variational principles, and eigenvalue problems all define solutions by satisfaction of constraints across an interval rather than by forward propagation from one edge. In these cases, no one objects to the "bidirectional" character of the description. The solution is boundary-conditioned. That is orthodox physics.

### 10.2 Wheeler–Feynman and Free-Electron Lasers

Wheeler–Feynman absorber theory treats radiation fields as fundamentally time-symmetric, with advanced and retarded components entering on equal footing, and apparent time-asymmetry arising from absorber boundary conditions rather than from any intrinsic asymmetry in the underlying equations.

This is not merely an interpretive curiosity. In certain highly coherent, weak-absorption regimes—notably the radiation of coherently oscillating electrons in free-electron lasers (FELs)—conventional retarded-only electrodynamics encounters difficulties. Niknejadi, Madey, and Kowalczyk (2015, *Physical Review D*) found it necessary to revive the Wheeler–Feynman assumption of equal advanced and retarded amplitudes to resolve discrepancies in the coherent radiation problem. They also proposed experimental detection of advanced effects by reducing absorber coupling (antenna length reduced to 1/10–1/20 of emitted wavelength).

The relevance to this framework is not that the brain is an FEL. It is that physics already admits regimes in which retarded-only descriptions are not merely cumbersome but structurally inadequate. If such regimes exist, it is legitimate to ask whether other complex systems—particularly those characterized by dense nonlinear coupling, massive recurrence, and extreme sensitivity to boundary conditions—might also belong to the same descriptive class.

### 10.3 The Strong Structural Claim

The claim is not that advanced electromagnetic signals propagate in neural tissue. It is stronger and more general:

> In a sufficiently complex, nonlinear, recursively coupled system, a purely forward-evolution description is not just inconvenient—it is structurally inadequate as a generalizable explanatory framework.

Such systems cannot be cleanly decomposed into forward-propagating causal steps. Their admissible trajectories are defined by global consistency, not local generation. The advanced Green's function, in this context, is not a literal signal but the mathematical signature that the system belongs to a class whose dynamics are inherently boundary-conditioned.

The brain is a highly nonlinear electrochemical system dominated by recursive feedback loops and near-field electromagnetic effects. In such a system, the Wheeler–Feynman paradigm does not appear as an exotic add-on or a philosophical preference. It appears in the formalism of the time evolution itself—because the system's dynamics are too tightly coupled, too recursively entangled across scales, for the retarded-only description to remain natural or complete. The appearance of time-symmetric structure in the formalism is a sign that the handshake is operative: the system's boundary conditions are not merely initial conditions propagating forward, but global consistency constraints spanning the trajectory. Those constraints are exactly what defeat the binding problem. The parts of the system cohere because they jointly satisfy a trajectory-level consistency condition whose natural mathematical expression requires both temporal directions. The handshake provides the boundary conditions. The boundary conditions bind the system.

---

## 11. Neural Closure Regimes

### 11.1 Physical Requirements

If neural systems exhibit elevated closure dominance, the relevant substrate is likely **near-field dominated, highly recursive electrochemical interactions**. Near-field interactions are where coupling is strongest, most geometry-sensitive, and least reducible to clean propagating modes. The brain is not a purely electrical system; it is an electrochemical excitable medium with mutually constraining layers: membrane potentials, synaptic transmission, ion gradients, dendritic integration, glial modulation, local field potentials, and metabolic boundary conditions.

These processes operate across multiple timescales and are recursively coupled: voltage changes alter chemical gradients, chemical states alter excitability, excitability alters future voltage dynamics. The result is continuous self-conditioning across time—a necessary condition for closure dominance.

### 11.2 Expected Signatures

If neural closure dominance is real, observable signatures would include: extreme sensitivity to mesoscale boundary conditions beyond what feedforward models predict; multi-timescale coordination without collapse into rigid global synchrony; reduced predictability of present states from past-local variables alone, with improved intelligibility when extended temporal constraints are included; and strong vulnerability of consciousness to disruptions of recursive coupling (anesthesia, hypothermia, ischemia).

---

## 12. Failure Modes and Counterexamples

A theory of consciousness is only as strong as its ability to explain why most structured systems are *not* conscious.

**Weakly coupled systems** (diffusion, simple circuits): no closure, because trajectory selection is weak. $\Omega \approx 0$.

**Pure noise**: no structure to constrain. Closure is undefined.

**Rigid order** (crystals, static fields): closure is satisfied trivially, because the admissible trajectory space has collapsed to a degenerate subset. There is no meaningful distinction between possible and actual trajectories. This is not consciousness; it is death by over-constraint.

**Pathological synchrony** (seizures): high coherence, strong coupling, but extreme reduction of dynamical dimensionality. The system collapses into a degenerate attractor. This resembles rigid order more than genuine closure.

**Deep sleep and anesthesia**: persistent neural activity and structured oscillations, but long-range temporal integration collapses. Recursive coupling weakens. The system becomes locally consistent but globally unconstrained. Closure is lost through under-constraining.

**Transient coherent events**: brief bursts of structured activity may exhibit local coherence but lack the temporal thickness required for closure. Closure must persist across a nontrivial interval.

**Large language models**: local coherence, high generative flexibility, zero intrinsic closure. They simulate trajectories without instantiating temporally closed ones. They borrow structure from pre-compressed training data rather than maintaining it under real constraint.

These cases define the regime precisely. Consciousness occupies a narrow band between under-constrained systems (noise, anesthesia, weak coupling) and over-constrained systems (crystals, seizures, rigid order). It exists only where constraint is strong enough to enforce global consistency but flexible enough to preserve nontrivial structure.

---

## 13. Implications

### 13.1 Against Functionalism

Functionalism identifies consciousness with computation or causal role. The Chinese Room and Chinese Nation arguments demonstrate that correct input-output behavior does not guarantee the existence of a unified subject. In this framework, such systems fail because they are externally scaffolded symbol relays—they lack intrinsic temporal closure. Computation is neither necessary nor sufficient for closure.

### 13.2 Against Panpsychism

Panpsychism's failure is mereological. This framework resolves it via temporal composition: only systems that jointly satisfy closure compose a subject. This avoids overgeneration, defines clear boundaries, and eliminates arbitrary aggregation without denying that consciousness might be realized in substrates very different from biological tissue.

### 13.3 Artificial Intelligence

Current AI systems are not conscious under this framework. They lack persistent trajectories, intrinsic temporal closure, and self-maintaining constraint structures. For an artificial system to cross the threshold, it would require persistent endogenous state, strong recursive coupling, multiscale constraint propagation, non-factorizable dynamics, and closure-dominated trajectory selection—a continuously operating, self-constraining dynamical system, not a stateless predictor.

### 13.4 Death and Revival

Death is the loss of the system's ability to sustain temporally closed trajectories. When recursive coupling collapses, admissible trajectories dissolve, and the system returns to the space of unconstrained dynamics. Revival (including from cryopreservation) succeeds as continuation of the same subject only if the post-revival system can sustain a trajectory continuous with the pre-interruption closure structure. Otherwise, it is a new subject.

### 13.5 Duplication

At the moment of perfect duplication, two systems share identical trajectories. Immediately after, their futures diverge. Under this framework, they become distinct subjects at the first point of trajectory incompatibility. Identity does not branch—it splits.

### 13.6 Personal Identity

Personal identity is not absolute. It is structural, graded, and trajectory-based. A person persists not because some substance endures, but because successive closure windows remain mutually embeddable within a larger evolving consistency structure. Identity is continuity of closure.

---

## 14. Philosophical Orientation

White accumulation is realist about structure and agnostic about substance. It does not claim that consciousness is "made of" information or "made of" physics. It claims that the pattern—the persistent, non-factorizable, temporally closed trajectory—is what matters, and that this pattern can in principle be identified, measured, and compared across substrates without resolving the hard problem in either the materialist or the panpsychist direction.

In this respect, the framework shares the orientation of ontic structural realism: what is real is the structure, and the structure can be parameterized and compared without commitment to what "underlies" it. White accumulation is structural realism applied to consciousness—the claim that the conscious system is a structural invariant (a closed trajectory in spacetime) rather than a substance, a function, or a computation.

---

## 15. Conclusion

The central claim of this paper can be stated in its strongest form:

Consciousness is not a feature of matter, computation, or structure alone. It is a feature of systems that exist as temporally closed trajectories—processes that sustain their own consistency across time. Binding is not a mechanism but a property of such trajectories: the parts cannot independently satisfy closure; only the whole can. Identity is not sameness but continuity of closure. The boundary of a subject is not spatial but defined by where closure holds and where it drops away. Everything else—intelligence, memory, flexibility, embodiment—is secondary to this condition.

To be a mind is to be a trajectory that closes.

---

*The concept is Mike's. The formalization is collaborative. The errors are the assistant's.*

---

## References

- Cramer, J. G. (1986). The Transactional Interpretation of Quantum Mechanics. *Reviews of Modern Physics*, 58(3), 647–687.
- Friston, K. J. (2010). The Free-Energy Principle: A Unified Brain Theory? *Nature Reviews Neuroscience*, 11, 127–138.
- Ho, M.-W. (1998). *The Rainbow and the Worm: The Physics of Organisms*. World Scientific.
- Niknejadi, P., Madey, J. M. J., & Kowalczyk, J. M. (2015). Radiation by a time-symmetric source. *Physical Review D*, 91(9), 096006.
- Schrödinger, E. (1944). *What Is Life?* Cambridge University Press.
- Searle, J. (1980). Minds, Brains, and Programs. *Behavioral and Brain Sciences*, 3(3), 417–424.
- Tononi, G. (2004). An Information Integration Theory of Consciousness. *BMC Neuroscience*, 5, 42.
- Wheeler, J. A., & Feynman, R. P. (1945). Interaction with the Absorber as the Mechanism of Radiation. *Reviews of Modern Physics*, 17(2–3), 157–181.
