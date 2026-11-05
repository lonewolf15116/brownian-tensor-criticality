# BTC-004 Master Evidence Ledger v1.0
**Date:** 2026-11-05  
**Status:** Working reconstruction; not independently certified  
**Gate:** OPEN | 19/21 working | 0/13 direct certified | 0 confirmed novel discoveries  
**Change control:** Frozen BTC-004-EQR-001 v1.0, scaling proof v3, and manuscript v0.3 are referenced, not modified. Amendments require v1.1 with change log.

## A. Working realizations

| ID | Triple | Witness / derivation | Evidence status |
|---|---|---|---|
| 1 | (1,1,1) | x⁴+y⁴+z⁴+4r²(x²+2y²+3z²), r²=x²+y²+z² | Argument, hand-checked |
| 2 | (1,2,2) | x⁴+y⁴−z⁴ | Argument, hand-checked |
| 3 | (2,2,1) | Negation of #2 | Inherited |
| 4 | (1,3,3) | −y⁴−3z⁴−3x²y²+3x²z²−5y²z² | Partial; corrected arithmetic; HIGH priority |
| 5 | (3,3,1) | Negation of #4 | Inherited; parent partial |
| 6 | (2,3,2) | (y²−z²)(y²+z²−3r²/2) | Argument, hand-checked |
| 7 | (2,4,3) | x⁴+y⁴+z⁴+t x²y², t<−2 | Argument, hand-checked |
| 8 | (3,4,2) | Negation of #7 | Inherited |
| 9 | (3,5,3) | y⁴−z⁴−2x²y²+2x²z² | Argument; intermediate correction |
| 10 | (4,6,3) | x⁴+y⁴+z⁴ | Argument, hand-checked |
| 11 | (3,6,4) | Negation of #10 | Inherited |
| 12 | (2,5,4) | x⁴+y⁴−z⁴−18x²y²+12xyz² | SymPy computation reported; standalone certificate pending |
| 13 | (4,5,2) | (x²+5y²−3z²)²+4(z²−x²−y²)² | Argument, hand-checked |
| 14 | (1,4,4) | Maccioni polynomial M below | Two same-author implementations; independent reproduction pending |
| 15 | (4,4,1) | −M | Inherited |
| 16 | (5,6,2) | Scaling F_{s,0} | Executable symbolic audit 5/5; analytic Reviews 6–7 pending |
| 17 | (2,6,5) | −F_{s,0} | Inherited |
| 18 | (5,5,1) | Scaling F_{s,1} | Executable symbolic audit 5/5; analytic Reviews 6–7 pending |
| 19 | (1,5,5) | −F_{s,1} | Inherited |

M = −21x⁴+1350x³z−17220x²z²+1000xy²z−136060xz³−y⁴−45000y²z²−13051z⁴.

Scaling seed q(X,Y)=3X⁴−5X²Y²+5Y⁴+20X²Y−32Y³+X²+2Y²; q_σ(X,Y)=q(X+σY,Y), σ∈{0,1}; F_{s,σ}=s⁴H₄,σ+s³zH₃,σ+s²z²H₂,σ. Existence asserted for sufficiently large s, without explicit finite bound. Four scaling triples include negations. Executable audit checks algebraic premises, not all analytic conclusions.

**Evidence terminology:** Argument = prose and hand-checks; Computational = output or script, specify whether packaged; Certified = standalone reproducible evidence independently rerun. None certified.

## B. Frozen even-family result

Even quartics f=d₁x⁴+d₂y⁴+d₃z⁴+ax²y²+bx²z²+cy²z²: frozen v1.0 internally claims 13-real configurations only (4,6,3) and (3,6,4). The ESS/Zeeman–Bomze/Vickers–Cannings/Palagi–Bomze subsumption chain is **reported, bibliographic primary-source verification pending**. Do not assert novelty. Potential residual contributions: nine-real exclusion of (1,4,4)/(4,4,1), explicit gallery, edge-normal identity.

## C. Missing target and Track A

(6,6,1) and (1,6,6) remain unresolved; negation exchanges them. A 13-real simple witness would exhaust a zero-dimensional eigenscheme of length 13. Neither construction nor impossibility proof exists.

Restricted-family obstructions reported: positive-definite leading H₄ scaling; threefold symmetry; X-even sign-changing leading H₄. These are not general obstructions. Metric orbit-equivalence is about attainable Morse triples, not literal equality of metric and GL₃ orbits.

**Anchor:** H(x,y,z)=3x⁴−5x²y²+5y⁴+20x²yz−32y³z+x²z²+2y²z². Under x=u+v, y=v, metric M₁₀₀=[[10⁻⁴,−10⁻⁴,0],[-10⁻⁴,2·10⁻⁴,0],[0,0,1]] becomes diag(10⁻⁴,10⁻⁴,1). Transformed quartic:
3u⁴+12u³v+13u²v²+2uv³+3v⁴+20u²vz+40uv²z−12v³z+u²z²+2uvz²+3v²z².

**Track A:** Search M(A,B)=diag(A,B,1) in these transformed coordinates. Generalized equations ∂uH̃=λAu, ∂vH̃=λBv, ∂zH̃=λz. Track conjugate pair projectively; seek real landing with P=Q=det(J(P,Q))=0; classify neighboring chambers and verify all 13 projective points. Prior reported diagonal sample counts 11,11,9,11,11 are *resultant real-root counts only*, not proof that a narrow 13-real interval is absent. Anchor pair coordinates were reported numerically, not independently reproduced here. 2D sensitivity/continuation pending.

**Track B:** 17-variable semialgebraic feasibility, on hold. No search expansion or repository changes to frozen artifacts.

## D. Audit correction log

- Mixed Hessian coefficient corrected to h=2d₂−a+b−c.
- Nine-point Case A k=0 maps (3,4,2), k=3 maps (2,4,3).
- Even witness vertex Lagrange multiplier corrected from f(p) to 2f(p).
- Reported determinant corrected to 1,734,000, not 1,725,000.
- Maccioni Δ(84) corrected to 1,924,133, not 1,676,133.
- Metric family reaches same Morse triples as GL₃ orbit, not literally same orbit.
- Claimed (1,2,1) equatorial split withdrawn.
- Boundary-maximum conjecture withdrawn; singular metric issue.
- Semialgebraic dimension corrected 16→17; positive dimension does not imply real feasibility.
- At y=0 for odd witness: Gx=4x(x²+1), Gy=12x(x²+1); gcd x(x²+1), only real root x=0.
- Odd witness symmetric under x↔y.
- Linear gcd requirement withdrawn; criterion is exactly one *real* common root per real eliminant y.
- Scheme length 13 follows from determinantal/Porteous degree under zero-dimensionality, not bare semicontinuity.
- Odd witness resultant degree in x corrected to 3.
- Isotropic complex artifacts must be saturated out or use full E_ij eigenpoint ideal.
- Distinct-point count and scheme length are different; reducedness requires proof.
- Four simple roots of E₁₂ on z=0 do not by themselves certify transverse projective Hessian nondegeneracy.
- Sparse diagonal sampling does not exclude thin unobserved chambers.

## E. Verification requirements

**R2-A (Morse triple):** For h_odd, with d=1+x²+y² and Gx=d h_x−4xh, Gy=d h_y−4yh, each real eliminant y_i must lift to exactly one distinct real common x, d>0, nondegenerate Hessian and correct index. y=0 done; six nonzero real y_i pending exact lifts. Infinity E₁₂ restricted has four real roots [1:0:0], [0:1:0], [1:1:0], [1:−1:0]; transverse projective/Hessian verification pending.

**R2-B (optional):** 13 distinct simple complex projective eigenpoints: saturated affine points + infinity, reducedness.

**R2-C:** Affine finiteness, full infinity finiteness, and determinantal length 13; document hypotheses and exact proof. No semicontinuity shortcut.

## F. Governance

Gate 0 OPEN; 19/21 working; 0/13 direct independently certified; 0 novel discoveries confirmed. External human review deferred by owner until final stage. Do not modify frozen files, silently upgrade evidence tiers, or publish novelty claims without prior-art verification. Next artifact: standalone exact certificate for #12, while bounded Track A proceeds separately.
