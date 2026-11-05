# S0 formal acceptance checklist — owner decision pending

Date: 2026-11-02. Prepared from the owner's submitted four-page *S0 Final Corrected-Text Verification* and the reviewed repository files. This document is **not** owner acceptance, a G1 authorization, a PR-merge instruction, or a novelty claim.

## A. Local theorem verification
- [x] Explicit symmetric tensor contraction and base corank-one Hessian recorded.
- [x] Correct stationary polynomial G and local two-root orientation recorded.
- [x] Full 35-parameter transverse IFT, fold-control a(T), and smooth local discriminant proof written.
- [x] Chart-Hessian identity and Schur complement recorded.
- [x] Fixed local chart window; exactly two regular roots for a<0, one coalesced corank-one root at a=0, none *locally* for a>0.
- [x] Full-rank Frobenius-isotropic Brownian model, compact closed-set stopping time, strict tau_K<tau_U event, finite h, positive path-to-boundary distance.
- [x] Theorem statement quantifiers and qualitative dependence stated; no unjustified asymptotic hitting-probability claim.
- [x] Reviewer arithmetic correction q_tt(0,T_mu)=6-12mu identified as reviewer error, not proof error.
- [x] Favorable owner-provided external mathematical review: PASS with minor text/hypothesis corrections.
- [ ] Independent recheck of **latest** revised theorem commit 39d6450 and reconciliation with final reviewer packet.

## B. Project-wide Gate 0 exit criteria (docs/GATE_0.md)
- [ ] 1. Nearest prior art verified with precise theorem-level comparisons. **OPEN**.
- [x] 2. Symmetric tensor Brownian covariance/normalization specified for local result.
- [x] 3. Local branch continuation distinguished from re-selection and x~-x sign convention.
- [ ] 4. Single-minimum-absolute-Hessian-gap sufficiency question derived or refuted under explicit assumptions. **OPEN; local fold theorem alone does not answer it.**
- [ ] 5. Counterexamples, unresolved issues and explicit owner exit decision recorded. **PARTIAL; decision absent**.

## C. Dossier/register integrity
- [x] Local theorem and reviewer correction traceable by branch and file.
- [ ] Full consistency review of older 'OPEN' and 'not independently verified' historical statements against current status; retain history without presenting stale claims as current.
- [ ] Resolve or explicitly defer audit's alleged missing +3t² source location.
- [ ] Check separate restricted-theorem Taylor expansion for any residual coefficient typo.

## D. Decision and restrictions
- [ ] Owner explicitly accepts the **local theorem** as an S0 mathematical deliverable.
- [ ] Owner explicitly decides whether overall **S0/Gate 0** is accepted, deferred, or remains open against B criteria.
- [ ] Separate explicit authorization before G1, numerical experiments, Rust implementation, manuscript submission, or PR merge.

**Current disposition:** local theorem favorable PASS pending latest-text recheck; **overall S0/Gate 0 remains OPEN**, and G1, experiments, merge, submission and novelty claims remain blocked. The local theorem is not a new mechanism or a demonstrated publication contribution.
