# Brownian Tensor Criticality

**Research status (2 November 2026): S0 / Gate 0 OPEN.** This repository studies local singularities and angular diffusion of continuously tracked real Z-eigenvectors of Brownian-evolving symmetric fourth-order tensors in four dimensions.

> Research-stage documentation, not a validated novelty claim or a completed manuscript. All reviews described here are AI-assisted mathematical reviews, not external human peer review.

## Mathematical setting

Let (V=\\operatorname{Sym}^4(\\mathbb R^4)), with its ordered-index Frobenius inner product, and let (T_s=T_0+\\sigma B_s), where (B_s) is standard Brownian motion in the 35-dimensional space (V). A normalized real Z-eigenpair satisfies
[
T x^3=\\lambda x,\\qquad \\|x\\|=1,\\qquad x\\sim-x.
]
At a regular eigenpair, define the tangent linearization
[
H=P_x(3T[x,x,\\cdot,\\cdot]-\\lambda I)P_x\\big|_{x^\\perp},\\qquad P_x=I-xx^\\top.
]

## Established local results

- **Explicit local fold:** A concrete quartic family exhibits a corank-one Z-eigenpair and a two-branch local fold. The local counting statement is restricted to a fixed projective-chart neighborhood.
- **Local 35D discriminant:** Parameter-dependent Lyapunov–Schmidt reduction constructs a smooth codimension-one fold sheet **near the reference tensor** (T_*). This is not a global characterization of the tensor eigendiscriminant.
- **Brownian accessibility:** For sufficiently nearby starting tensors on the two-branch side, full-rank isotropic tensor Brownian motion has positive probability of hitting the local fold sheet before leaving a prescribed neighborhood and by each fixed finite horizon (h>0). This does not imply almost-sure hitting, a uniform small-time bound, or a hitting-time law.
- **Exact tangent covariance:** On a regular, continuously tracked branch before stopping,
[
Q_x=\\frac{\\sigma^2}{4}H^{-2}.
]
The factor (1/4) comes from the Frobenius normalization of the symmetrized order-four tensor forcing.
- **Minimum-gap sufficiency:** With (\\gamma=\\min_i|\\eta_i(H)|),
[
\\|Q_x\\|_{\\mathrm{op}}=\\frac{\\sigma^2}{4\\gamma^2}.
]
The minimum gap determines worst-direction instantaneous variance, **not** total variance or the full diffusion matrix. Explicit realizable symmetric-tensor counterexamples establish those insufficiency results.
- **Ambient Itô drift:** The sphere constraint gives (x^\\top b=-\\tfrac12\\operatorname{tr}Q_x); the minimum gap does not determine the full ambient drift-included SDE.

**Still open:** Whether the minimum gap determines the **intrinsic tangential drift** (P_xb). The ambient sphere-constraint argument alone does not settle it.

## Restricted fold algebra

For the explicit family, the stationary-fold parameterization is
[
\\phi(t)=\\frac{-3t^2+4t^3+t^4}{1-3t^2}
=-3t^2+4t^3-8t^4+12t^5+O(t^6).
]
An earlier source displayed an incorrect (+10t^4) coefficient. The exact source/commit provenance and document synchronization remain pending; no unverified repository correction is claimed here.

## Prior art and novelty

Relevant comparisons include tensor eigendiscriminants (Abo–Seigal–Sturmfels), generic tensor eigenvalue counts (Cartwright–Sturmfels), tensor eigenvalue perturbation (Che–Qi–Wei), additive Hermitian matrix eigenvector diffusion and eigenvector moment flow (including Bourgade–Yau), Brownian hypersurface hitting (Thompson), and stochastic saddle-node escape (Herbert–Bouchet). These concern **different observables and driving processes**; in particular, multiplicative Wishart/ellipsoid matrix diffusions must not be substituted for the additive Hermitian eigenvector SDE.

The local fold uses established bifurcation machinery. The covariance formula is an exact tensor-specific computation, but **independent novelty and publication significance are not established**. Precise theorem-level comparisons, including the additive Hermitian eigenvector SDE and Che–Qi–Wei Theorem 3.2, remain unfinished.

## Current stage and restrictions

- **Local fold theorem:** favorably assessed in AI-assisted mathematical review; committed-text provenance/recheck remains to be reconciled.
- **Exact covariance and worst-direction gap formula:** PASS.
- **Total variance/full covariance and ambient drift sufficiency:** FAIL, with explicit counterexamples and sphere-constraint argument.
- **Intrinsic tangential drift:** OPEN.
- **Prior-art verification and Gate 0 owner sign-off:** OPEN.
- **Novel discoveries confirmed:** none.

**Not authorized:** G1, numerical experiments, Rust implementation, PR merge, manuscript submission, or novelty claims. Changes to this README do not alter the research gates.

## Research documents

- [Gate 0 charter](docs/GATE_0.md)
- [Local 35D fold and Brownian accessibility theorem](math/S0_35D_LOCAL_FOLD_LS_AND_HITTING_THEOREM.md)
- [Restricted stochastic fold draft](math/S0_RESTRICTED_STOCHASTIC_FOLD_THEOREM_DRAFT.md)
- [S0 formal acceptance checklist](docs/S0_FORMAL_ACCEPTANCE_CHECKLIST.md)
- [S0 correction register](docs/S0_AUDIT_CORRECTION_REGISTER.md)
- [S0 exit dossier](docs/S0_EXIT_DOSSIER.md)
