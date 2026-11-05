# BTC-004 manuscript v0.3 — change and review log

**Date:** 2026-11-03  
**Author:** Mahesh Reddy Pagadala  
**Draft status:** Working manuscript, not submitted; novelty unverified; human peer review outstanding.  
**Reference:** Frozen BTC-004-EQR-001 v1.0 (unchanged).

## Changes from v0.2

1. Clarified Lemma 4 vertex-index rule: each vertex has two incident edges **in total**, not necessarily two positive-curvature edges. An edge contributes one negative Hessian direction iff its curvature is positive.
2. Added explicit projective-chart calculation near a vertex: on an adjacent edge, `s(Y)=Y^2/(1+Y^2)` and `d²/dY²[φ(s(Y))]` at zero equals `2φ′(0)`. This establishes the inward-derivative sign transfer directly.
3. Explained Cartwright–Sturmfels' generic complex count as `((d−1)^n−1)/(d−2)=(3³−1)/2=13`, which can also be written `1+3+9`. Distinguished this geometric-series count from the **different** real support count `3+6+4` for the 13-real even family.
4. Slightly clarified the literature comparison's targeted, non-exhaustive character. No claim of novelty was added.
5. Kept the draft at four pages through minor layout adjustments (20 mm margins and reduced paragraph spacing).

## Disposition of latest referee-style assessment

- Mathematical proof and witness: no mathematical amendment requested.
- Two Lemma 4 presentation ambiguities: addressed.
- The 1+3+9 citation/explanation: addressed.
- Contrast between complex algebraic count and support-based count: addressed.
- Novelty and human peer review: still unresolved.

## Limitations and next gates

**Not authorized for external claims of confirmed novelty or peer review.** Existing comparisons include Maccioni, Basso–Tu, Kozhasov, Michel–Zhilinskii, Vassiliev and selected Combe/Arnold materials from prior BTC-004 work. These are targeted checks, not exhaustive classical-literature clearance; some claims in the earlier audit are based on abstracts or selected full text rather than all possible sources.

The earlier broad BTC-004 ledger remains **8/21 realized; 13 globally unresolved; 0 confirmed novel discoveries; Gate 0 OPEN**. No numerical experiments, GitHub changes or external submissions were performed for v0.3.

## Frozen integrity

BTC-004-EQR-001 v1.0 SHA-256 (unchanged):
`7e90d980a3b574d0a91d0dc7328138ac5af50ed85c4d1abd1bfdb6b7dad2d20f`
