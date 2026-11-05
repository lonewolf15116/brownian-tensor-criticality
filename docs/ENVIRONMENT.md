# Rust-first environment plan — not executed

Decision (2026-11-02): Rust is the proposed primary numerical language, pending owner review of this draft PR. Windows / PowerShell, stable rustc and cargo; no WSL, GPU or Python requirement.

Candidate dependencies (versions to be pinned only at implementation authorization): nalgebra for small tangent matrices, ndarray or a custom 35-coefficient symmetric-tensor representation, rand + rand_distr for Gaussian increments, serde/serde_json for manifests, thiserror for explicit errors. Confirm crate-version compatibility before locking.

Architecture: separate exact mathematical definitions, deterministic algebraic kernels, Brownian path generation, eigenpair continuation, diagnostics and output provenance. Fully symmetric order-four dimension-four tensors have 35 independent coefficients; choose orthonormal Sym^4 basis and explicitly specify covariance before sampling.

Planned checks: contraction/permutation symmetry, Z-eigenpair residual, tangent-Hessian projection, sign-invariant overlap, fixed-seed repeatability, finite-difference checks, convergence and branch-loss handling.

No Cargo project initialized, dependencies installed, code compiled, or numerical validation executed. Gate 0 remains documentation-only.
