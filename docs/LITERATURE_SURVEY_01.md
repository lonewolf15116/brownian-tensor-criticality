# Literature survey 01 — primary-source screening (2026-11-02)

Status: initial screening, not exhaustive. Distinguish stationary distributions, dynamical computation, and time-correlated Brownian tensor eigenvector paths. No novelty claim.

| Source | Verified scope | Relationship to H3/H4 | Follow-up |
|---|---|---|---|
| Benson & Gleich (2019), Computing Tensor Z-Eigenvectors with Dynamical Systems, DOI 10.1137/18M1229584 | Dynamical system numerically converging to tensor Z-eigenvectors | Does not by itself establish Brownian tensor-coefficient eigenvector flow | Inspect full method and Jacobian |
| Fasino & Tudisco (2020), Ergodicity Coefficients for Higher-Order Stochastic Processes, DOI 10.1137/19M1285214 | Sensitivity bounds and uniqueness for nonnegative stochastic tensors | Important perturbation prior art; different tensor class | Compare bound assumptions |
| Sasakura (2023), Real eigenvector distributions of random tensors with backgrounds and random deviations, DOI 10.1093/ptep/ptad138 | Static random tensor eigenvector distributions and spiked thresholds | Restricts claims about random-tensor thresholds | Compare covariance conventions |
| Sasakura (2026), Joint Distributions of Eigenvectors of Symmetric Random Tensors, DOI 10.1093/ptep/ptag143 | Joint distributions, large-dimension asymptotics and a geometry-dependent universality result | Direct obstacle to generic 'tensor eigenvector universality' claims; not automatically continuous-time Brownian flow | Read theorem and model assumptions |
| Herbert & Bouchet (2017), Predictability of escape for a stochastic saddle-node bifurcation, DOI 10.1103/PhysRevE.96.030201 | Stochastic escape near fold and competing regimes | Generic fold criticality is prior art | Compare stochastic forcing placement |
| Bergeot, Berglund & Zogheib (2026), The dynamic saddle-node bifurcation with noise on the slow variable, DOI 10.1088/1361-6544/ae7ec0 | Fold with noise in slow control variable; asymptotic moment corrections | Closest conceptual normal-form comparison | Read exact scaling assumptions |

## Important distinctions
- A tensor termed *stochastic* can be a nonnegative transition-probability tensor, not a tensor whose coefficients evolve as Brownian motions.
- Static Gaussian ensemble joint distributions are not the same observable as time-dependent overlap of a tracked eigenvector branch; nevertheless Gaussian marginals and correlations may connect them.
- Brownian coefficient perturbations and stochastic gradient dynamics on the sphere are different processes.
- At singular tangent Hessian, inverse-Hessian perturbation formulas fail. Branch selection and stopping at fold must be specified.
- Symmetric fourth-order eigenvectors have x ~ -x sign equivalence for directional overlap.

## Candidate gap, NOT verified
A theorem-level characterization of local diffusion and critical scaling of *continuously tracked* normalized Z-eigenvectors under a specified Brownian process on Sym^4(R^4), especially the insufficiency of scalar-gap predictors under anisotropic noise. Existing implicit-function arguments may already imply the regular-case formula, so novelty must come from a genuinely new critical result or characterization.

## Next audit tasks
1. Extract exact theorems and assumptions from the six papers above.
2. Search stochastic implicit function theorems, random critical-point continuation, p-spin landscape dynamics, and tensor perturbation results.
3. Build a theorem-level overlap matrix and explicit counterexample plan before any experiment.

## Sources
- https://epubs.siam.org/doi/abs/10.1137/18M1229584
- https://epubs.siam.org/doi/10.1137/19M1285214
- https://academic.oup.com/ptep/article/2023/12/123A01/7424130
- https://doi.org/10.1093/ptep/ptag143
- https://doi.org/10.1103/PhysRevE.96.030201
- https://doi.org/10.1088/1361-6544/ae7ec0
