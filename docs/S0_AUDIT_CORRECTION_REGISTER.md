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

## Second-review wording refinement (2026-11-02)
- The inverse branch is continuous on [0,rho) and admits a finite one-sided limit at rho; no regular inverse is asserted at the fold or artificial boundary.
- Describe its stochastic differential as an **exact pre-stopping Itô equation**, valid for s<rho under compact localization, rather than an unqualified 'exact stopped SDE'.
- S0 remains revised, not accepted; G1, numerical experiments and PR merge remain blocked.

## 2026-11-02 proof-only 35D local theorem draft
A full parameter-dependent Lyapunov–Schmidt **local proof draft** now exists at `math/S0_35D_LOCAL_FOLD_LS_AND_HITTING_THEOREM.md` (commit `4bfd2686`). It eliminates the two transverse chart coordinates by IFT, defines a smooth fold-control a(T), proves a local codimension-one sheet and two local regular roots on a<0, constructs adapted local branch selections and stopping times, and gives a positive-probability Brownian tube argument for reaching local H-degeneracy from suitable nearby starts. **This has not yet undergone independent line-by-line verification.** It is not a global branch continuation, branch-death distribution, almost-sure hitting theorem, or novelty result. S0 acceptance and G1 remain blocked pending independent proof scrutiny and owner decision.

## 2026-11-02 external follow-up review and correction
Reviewer found local LS core sound but requested six refinements. The 35D theorem draft was updated at commit `c203279` to restrict root counting to a fixed chart window, use one degenerate critical point at the fold, require an interior sign-changing path for the Brownian tube, specify a finite-horizon positive margin and boundary distance, define tau_Sigma only before chart exit, and distinguish q_tt(0,T*)=6 from uniform positivity nearby. This is a revised proof draft **awaiting independent recheck**, not formal S0 acceptance. No G1, experiments, PR merge or novelty claims.

## Final proof-precision pass (2026-11-02)
Follow-up reviewer judged the local theorem mathematically sound subject to six precision changes. Commit `8d544ad` adds chart Hessian identity D²_y g=4J^T H J at critical points; Schur complement q_t=A-BM^{-1}B^T; compact closed-set K={a=0}∩closure(U0) and tau_K; ordered ball/start/crossing-path quantifiers; convergence of both branches to one corank-one eigenpair; and qualitative probability scope. Also records q_tt(0,T_mu)=6-12mu (reviewer's statement that it is 6 for every mu was incorrect). **Corrected text has not been independently rechecked. S0 not formally accepted, G1/experiments/merge blocked, novelty unconfirmed.**

## Reviewer arithmetic correction and scope (2026-11-02)
The follow-up reviewer explicitly retracted their claim that q_tt(0,T_mu)=6 for every mu. Direct differentiation gives **q_tt(0,T_mu)=6-12mu**. This was a reviewer arithmetic error, **not an error in the original proof**, which used only q_tt(0,T*)=6. On the restricted line, mu<1/2 is necessary and sufficient for positivity at t=0; |mu|<1/2 is a convenient sufficient symmetric restriction, and |mu|<=1/4 gives q_tt>=3 at t=0. Continuity and further neighborhood shrinking handle t!=0 and the other 34 directions. This clarifies the positivity justification without altering the local theorem. The latest proof text still awaits independent recheck; S0 not formally accepted.

## Internal cross-consistency audit (2026-11-02)
After the eight text-presence checks, a new quantifier inconsistency was found: the theorem required closure(U0) subset B(T*,2delta) but suggested U0=B(T*,2delta). Commit `c7e9b85` fixes this by using U0=B(T*,3delta/2) for starts in B(T*,delta), choosing T_cross in B(T*,delta/2) on the a>0 side, and giving the explicit straight-line path gamma(s)=(1-s/h)T_init+(s/h)T_cross. This is an internal consistency correction, **not independent verification**. S0 acceptance remains pending an external recheck of the latest text and owner authorization. No G1, simulations, merge or novelty claim.

## 2026-11-02 owner-supplied final reviewer PASS and proof-only corrections
Owner supplied a four-page *S0 Final Corrected-Text Verification* assessing the local theorem as **PASS with minor textual/hypothesis corrections**, not an overall Gate 0 acceptance or novelty endorsement. The theorem was revised in commit `39d6450` to make the fixed local window, two-to-one coalescence, full-rank Brownian covariance, finite-horizon ordered quantifiers, strict interior stopping event, and qualitative probability dependence explicit. The reviewer also required preserving the distinction between local eigenpair count and global eigenpair count. Reviewer arithmetic correction q_tt(0,T_mu)=6-12mu remains a reviewer error, not a defect in the base proof. The sign-off checklist is `docs/S0_FORMAL_ACCEPTANCE_CHECKLIST.md` (commit `ec6b30f`). **Latest commit not independently rechecked.** Historical OPEN entries above describe earlier stages; local LS/hitting proof obligations are now *written and favorably reviewed*, but global continuation/hitting laws remain OPEN. Critically, `docs/GATE_0.md` still has open prior-art and single-gap-sufficiency exit criteria. Therefore **overall S0/Gate 0 is not accepted**. No G1, simulations, merge, submission or novelty claims authorized.
