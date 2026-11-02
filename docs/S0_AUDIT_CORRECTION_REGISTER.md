# S0 independent-audit correction register (2026-11-02)

Source: owner-provided Independent Mathematical Audit of Brownian Tensor Criticality (Manus AI, 2026-11-02). User explicitly approved 'Revise S0'.

| Issue | Decision | Evidence / remaining work |
|---|---|---|
| Missing +3t² in stationary equation | VALID mathematical defect if present; source occurrence NOT LOCATED in inspected core branch files | Correct canonical G=mu(1-3t²)+3t²-4t³-t⁴; inspect remaining paths/commit history before claiming specific correction |
| Wrong branch side | Correct side mu<0 | Verified phi=-3t²+O(t³); no wrong sign located in inspected core files |
| Tensor contraction convention | Clarified | Ordered-index sum; T1112=mu/4 |
| H versus spherical Hessian | Clarified | H restricted to x-perp; Riemannian Hessian=4H |
| Restricted Ito endpoint | Strengthened | Compact localization, rho=tau0 wedge tauL, no continuation through fold |
| Scalar coefficient hitting vs branch lifetime | Clarified | Reflection formula for tau0, two-sided exit for rho |
| Frobenius noise | Confirmed | 1112 unit orbit -> coefficient 2sigma, bracket 4sigma² |
| 35D Ito and stopping | Proof obligation | Choose precompact U0 inside IFT domain; D²X bounded there; full Hessian term structural |
| 35D Lyapunov-Schmidt | OPEN | Need kernel/cokernel, transverse inverse, quadratic/unfolding coefficients, local discriminant sheet |
| 35D hitting and continuation | OPEN | Need path support, normal nondegeneracy, branch availability, intrinsic first-singularity stopping |
| Literature/novelty | OPEN | Prior art includes Cartwright–Sturmfels, Qi, Lim, Hu, Che–Qi–Wei, classical fold and Brownian exit; no novelty claim |
| Missing dossier raw URL | Unresolved access/path | File exists at docs/S0_EXIT_DOSSIER.md in this branch via GitHub connector; raw URL failure needs separate diagnosis |

**Gate:** S0 not accepted; G1, experiments and PR merge blocked. Reviewer report is evidence of critique, not independently authenticated reproduction.
