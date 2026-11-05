# BTC-004 — Response to AI-Assisted Referee Audit

**Date:** 2026-11-03  
**Status:** Internal audit-response note; **not** a human peer-review report or originality certificate.  
**Documents compared:** `BTC-004_Independent_Referee_Audit.pdf` (five pages), `BTC-004_Independent_Reviewer_Dossier.docx`, and frozen `BTC-004_Even_Quartic_Rigidity_FROZEN_v1.0.md`.  
**Change control:** Frozen v1.0 is unchanged. No repository changes were made.

## Executive disposition

The AI-assisted referee's overall decision was **REVISE**, not unconditional acceptance. It accepted the support count, exact edge identity, index transfer (with a convention clarification), and witnesses. Its principal criticism was that the indefinite-Hessian case did not explicitly rule out all three edge curvatures having the same sign using the Morse–Euler relation.

**That particular criticism does not apply to the actual documents compared.** The submitted reviewer dossier, section 4, paragraph 41, explicitly states that three positive edge curvatures would give six minima, four saddles and three maxima, so the alternating sum is **5**, contradicting **χ(RP²)=1**, and that the all-negative pattern likewise violates Euler. The frozen proof v1.0, section 3(c), contains the same explicit argument and equation **6−4+3=5**. Thus the requested Euler repair was already present. The AI report appears to have overlooked it; do not treat its “REVISE” as evidence of a new, unresolved mathematical counterexample.

## Comment-by-comment response

1. **Support count — accepted.** Three vertices + three pairs of edge points + four interior sign lifts give 13. The strict-support conditions and nondegenerate-Hessian implications are stated in frozen v1.0 section 1.
2. **Edge-normal identity — accepted.** In the `xy` chart `(t,n)=(u,w)`, `κ=2(d1+d2−a)`, `h=2d2−a+b−c`, and `ℓ=2(d2+d3−c)`. At an interior stationary point `(t*,n*)`, with `n*>0`, the exact relation is `Q_n(t_e,0)=−det(K)n*/κ`. This is explicitly derived in v1.0 section 2.
3. **Index convention — minor editorial clarification.** State explicitly that Morse index means the number of **negative** eigenvalues of the constrained Hessian. Frozen v1.0 already uses the conventional index meanings (0=min, 1=saddle, 2=max), but a future separately versioned revision may spell this out.
4. **Indefinite-case exhaustion — already addressed.** The complete Euler contradiction is present in both the submitted DOCX and frozen v1.0. The sign patterns remaining are one-positive/two-negative and two-positive/one-negative, giving `(3,6,4)` and `(4,6,3)` respectively.
5. **Boundary/rank loss — largely addressed.** Frozen v1.0 section 5 states that `κ=0` yields no isolated edge stationary point or a non-Morse continuum; `det(K)=0` excludes a nondegenerate full-support critical point; collisions with a vertex or edge force a zero Hessian direction. A future v1.1 could add local coordinate formulas purely for referee readability.
6. **Attainment — accepted.** `2x⁴+y⁴+z⁴` gives `(4,6,3)` and its negative gives `(3,6,4)`.
7. **Novelty — unresolved.** The checked references do not constitute comprehensive literature clearance. No claim of a newly discovered theorem or completed external human review is justified.

## Decision with no human reviewer available

**Continue internal research without treating the human-review gate as passed.** It is appropriate to label the proposition *internally proved / AI-assisted checked / external review outstanding* and to prepare a clearly labeled preprint draft or continue adjacent research. An owner decision to proceed under these limits is a **risk-acceptance decision**, not independent mathematical verification.

Suggested next technical assurance: independently reproduce the theorem by a second exact argument (e.g., critical-point index counts from the simplex's edge derivatives and Euler characteristic), check the proof's boundary cases algebraically, and maintain an explicit prior-art search log. Any future change to the frozen mathematics requires a new version; the v1.0 file and checksum remain unchanged.

**BTC-004 ledger:** 8/21 globally realized triples; 13 unresolved; zero confirmed novel discoveries; Gate 0 OPEN.
