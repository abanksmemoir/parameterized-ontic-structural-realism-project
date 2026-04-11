## Appendix F: Formal Structure and Equations

### F.1 Notation and Setup

Let:

- \( I = [t_0, t_1] \subset \mathbb{R} \) be a nontrivial time interval  
- \( X(t) \in \mathcal{X} \) be the state of a candidate system  
- \( X_I = \{X(t) : t \in I\} \) be a trajectory  

We assume a coarse-graining has been chosen such that:

- \( X(t) \) represents dynamically relevant macrostates  
- microscopic noise is suppressed  

---

### F.2 Closure Functional

Define a closure functional:

\[
\mathcal{C}[X_I]
\]

which measures deviation from temporal self-consistency.

A system is said to satisfy **temporal closure** over \( I \) if:

\[
\mathcal{C}[X_I] \le \epsilon
\]

for some small threshold \( \epsilon \).

---

### F.3 Discrete-Time Toy Model

Let:

\[
x_{-1}, \quad x_0, \quad x_{+1} \in \mathbb{R}
\]

Define:

\[
\mathcal{C}(x_{-1}, x_0, x_{+1}) =
\alpha (x_0 - f(x_{-1}))^2
+
\beta (x_{+1} - f(x_0))^2
+
\gamma \left(x_0 - \frac{x_{-1} + x_{+1}}{2}\right)^2
\]

Interpretation:

- first term: consistency with past  
- second term: consistency with forward evolution  
- third term: global temporal consistency  

Minimizing with respect to \( x_0 \):

\[
\frac{\partial \mathcal{C}}{\partial x_0} = 0
\]

yields:

\[
x_0 =
\frac{
\alpha a x_{-1}
+
a \beta x_{+1}
+
\frac{\gamma}{2}(x_{-1} + x_{+1})
}{
\alpha + a^2 \beta + \gamma
}
\]

Thus:

> the present is selected by the whole trajectory.

---

### F.4 Continuous-Time Formulation

Define:

\[
\mathcal{C}[X_I] =
\int_{t_0}^{t_1}
\left[
\alpha \|\dot{X}(t) - F(X(t))\|^2
+
\gamma \|X(t) - \Pi[X_I](t)\|^2
\right] dt
\]

Where:

- \( F(X) \): local dynamics (retarded evolution)  
- \( \Pi[X_I](t) \): global consistency operator  

---

### F.5 Closure Condition

A trajectory is admissible if:

\[
\mathcal{C}[X_I] \le \epsilon
\]

and **non-generic** if:

\[
\mathcal{C}[X_I + \delta X_I] \gg \epsilon
\]

for typical perturbations \( \delta X_I \).

---

### F.6 Non-Factorizability (Binding)

Let system decompose as:

\[
X(t) = (X_A(t), X_B(t))
\]

Define:

\[
\mathcal{C}_{A \cup B}[X_I] \le \epsilon
\]

but:

\[
\mathcal{C}_A[X^A_I] \gg \epsilon, \quad
\mathcal{C}_B[X^B_I] \gg \epsilon
\]

Then:

> the system is non-factorizable (bound).

---

### F.7 Temporal Mereology

Define the subject:

\[
S^* = \arg\min_{S}
\mathcal{C}[X^S_I]
\]

subject to:

- non-factorizability  
- maximality  
- non-degeneracy  

---

### F.8 Identity Across Time

Two intervals \( I_1, I_2 \) belong to the same subject iff:

\[
\exists X_{I^*} \supset X_{I_1} \cup X_{I_2}
\quad \text{such that} \quad
\mathcal{C}[X_{I^*}] \le \epsilon
\]

---

### F.9 Distance Between Minds

Define:

\[
d_{\text{mind}}(T_1, T_2)
=
\inf_{T^* \supseteq T_1 \cup T_2}
\left(
\mathcal{C}[T^*]
+
\mathcal{D}(T_1, T_2 \rightarrow T^*)
\right)
\]

Where:

- \( \mathcal{D} \) measures distortion required for unification  

---

### F.10 Closure Dominance Parameter

Define:

\[
E_R =
\inf_{F}
\int \|\dot{X}(t) - F(X(t))\|^2 dt
\]

\[
E_{RC} =
\inf_{F,\Pi}
\int
\left[
\|\dot{X} - F(X)\|^2
+
\|X - \Pi[X_I]\|^2
\right] dt
\]

Then:

\[
\Omega_{\text{closure}} =
1 - \frac{E_{RC}}{E_R + \epsilon}
\]

---

### F.11 Interpretation of \( \Omega_{\text{closure}} \)

- \( \Omega \approx 0 \): retarded-only sufficient  
- \( \Omega \approx 1 \): closure-dominated  

---

### F.12 Non-Factorizability Metric

Define:

\[
N[X_I] =
1 - \frac{\mathcal{C}[X_I]}{\min(\mathcal{C}_A, \mathcal{C}_B)}
\]

Normalized to \( [0,1] \).

---

### F.13 Mind-Likeness Parameter

\[
M[X_I] = \Omega_{\text{closure}} \cdot N[X_I]
\]

---

### F.14 Degeneracy Penalty

Define:

\[
D[X_I] =
\exp(-k \cdot \text{Var}(X_I))
\]

or more generally:

\[
D[X_I] = \text{measure of trivial trajectory space}
\]

---

### F.15 Final Criterion

A system is conscious over interval \( I \) iff:

\[
\mathcal{C}[X_I] \le \epsilon
\quad \land \quad
N[X_I] \approx 1
\quad \land \quad
\Omega_{\text{closure}} \gg 0
\quad \land \quad
D[X_I] \text{ is low}
\]

---

### F.16 Compact Statement

\[
\text{Consciousness} \equiv
\text{non-factorizable temporal closure over an interval}
\]
