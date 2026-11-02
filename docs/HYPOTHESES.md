# Hypothesis register — provisional

**H3 (first priority):** A scalar minimum absolute tangent-Hessian eigenvalue generally does not determine short-time angular diffusion; the full inverse-Hessian/noise covariance contraction matters.

**H1:** Narrow instability windows can be missed by coarse parameter scans. This is a testable possibility, not an observed result.

**H2:** Abrupt eigenvector changes may result from eigenpair re-selection rather than discontinuity of a tracked branch.

**H4:** A critical scaling limit may hold within a restricted class of generic degeneracies after suitable normalization; universality is not assumed.

## Baseline mathematics
For T in Sym^4(R^4), a normalized Z-eigenpair satisfies T x^3 = lambda x, ||x||=1. With P=I-xx^T, define the tangent linearization H = P(3T[x,x,.,.] - lambda I)P restricted to x-perp. For invertible H, first-order response to tensor perturbation dT is dx = -H^{-1}P(dT x^3). A Brownian perturbation with projected covariance Q suggests local squared angular displacement rate sigma^2 tr(H^{-1}Q H^{-T}) under specified conventions.

This is a local perturbative prediction, not a new theorem. At singular H, the formula is inapplicable. Finite time branch loss and stopping rules require separate treatment.
