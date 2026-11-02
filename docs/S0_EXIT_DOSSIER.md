# S0 exit dossier — ready for owner review, not approval of G1

Date: 2026-11-02. Scope: documentation and mathematical proofs only. No Rust, numerical runs, or PR merge.

## Completed internal mathematical checks
- Tensor quartic coefficients and tangent-Hessian conventions checked for regular examples.
- Explicit corank-one singular Z-eigenpair constructed with H eigenvalues (0,-1,-1).
- Exact reduced fold equation and generic nondegeneracy derivatives established; local transverse eigenvector equations exclude extra branches near e1.
- Frobenius-isotropic 35-dimensional tensor Brownian noise projected onto the fold-normal coordinate: variance rate 4*sigma^2 for the quartic coefficient mu.

## Literature overlap
Hu, *Nondegeneracy of eigenvectors and singular vector tuples of tensors*, arXiv:2104.05900 (published Science China Mathematics 2022, DOI 10.1007/s11425-020-1863-5): generic nondegeneracy of tensor Z-eigenvectors. https://arxiv.org/abs/2104.05900
Bergeot, Berglund & Zogheib, *The dynamic saddle-node bifurcation with noise on the slow variable*, Nonlinearity 39 (2026) 075004, DOI 10.1088/1361-6544/ae7ec0: stochastic fold with noise on slow variable, not automatically the same as a static-constraint branch selected from Brownian tensor coefficients. https://doi.org/10.1088/1361-6544/ae7ec0
Hu & Qi, *The E-eigenvectors of tensors*, https://arxiv.org/abs/1303.2840: algebraic eigenvector and discriminant geometry. The theorem-level comparison is not exhaustive.

## Unresolved / blocked
- External independent verification of algebra and complete theorem-level novelty audit.
- Rigorous stochastic continuation, measurable branch selection, and exact first-singularity stopping time.
- Curved discriminant geometry, non-transverse Brownian paths, multiple-mode and higher-order singularities.
- Exact survival distributions and critical scaling; no discovery established.

## S0 disposition
Documentation package assembled for owner review. **S0 not formally closed**; owner must decide accept/revise. G1 remains BLOCKED. PR #1 remains draft/unmerged. Confirmed novel discoveries: 0.
