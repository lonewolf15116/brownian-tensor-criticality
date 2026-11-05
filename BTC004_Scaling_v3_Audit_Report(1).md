# BTC-004 — Gate A independent-derivation audit of scaling proof v3

**Audit date:** 4 November 2026  
**Source note:** `BTC004_Scaling_Proof_v3.md`  
**Source SHA-256:** `8c051b53bcabc3b6f911d4c1018c545d47d7a00eb029f2017ce22073a3cf0450`  
**Method:** Independently reconstructed the calculations from the stated affine polynomial. Exact symbolic assertions were executed with SymPy 1.14.0 in `BTC004_Scaling_v3_Independent_Audit.py`. The local analytic arguments were reviewed separately, not computer-certified. This is **not** external peer review or a second independent CAS.

## Decision

**Internal mathematical audit: PASS**, subject to standard local holomorphic conservation-of-number and implicit-function theorems. No counterexample or unclosed mathematical gap was identified in v3. The four **existence** claims are supported:

- `sigma=0`: `(5 minima, 6 saddles, 2 maxima)`.
- `sigma=1`: `(5 minima, 5 saddles, 1 maximum)`.
- Reversing the sign gives `(2,6,5)` and `(1,5,5)`, respectively.

**External independent review: OPEN.** **Publication novelty: unverified.** No explicit finite lower bound on `s` is supplied or needed for the qualitative theorem.

## 1. Affine critical-point audit — PASS (exact algebra)

Starting from

\[
q(X,Y)=3X^4-5X^2Y^2+5Y^4+20X^2Y-32Y^3+X^2+2Y^2,
\]

the independently differentiated equations are

\[
q_X=2X(6X^2-5Y^2+20Y+1),\qquad
q_Y=4Y(5Y^2-24Y+1)+X^2(20-10Y).
\]

At `X=0`, the three roots are `Y=0` and `Y=(12 ± sqrt(139))/5`.
At `X != 0`, the first equation yields `X²=(5Y²−20Y−1)/6`; substitution into `q_Y` gives **exactly**

\[
q_Y\big|_{X^2=(5Y^2-20Y-1)/6}
=\frac{(Y-5)(Y+1)(35Y+2)}3.
\]

Hence the other six points are `(±2,-1)`, `(±2,5)` and `(±sqrt(13/490),-2/35)`. All nine are real and distinct. Exact Hessian-sign assertions confirm:

| Point family | Count | Type | Additional exact check |
|---|---:|---|---|
| `(0,0)` | 1 | Minimum | Hessian diagonal `(2,4)` |
| `(±2,-1)` | 2 | Minimum | `det = 6336`, `q_XX = 96` |
| `(±2,5)` | 2 | Minimum | `det = 33984`, `q_XX = 96` |
| `(0,(12±sqrt(139))/5)` | 2 | Saddle | `det < 0` at both |
| `(±sqrt(13/490),-2/35)` | 2 | Saddle | `det = -303732/8575` |

The quartic's two cubic gradient equations have no common projective point at infinity because the partial derivatives of the leading binary quartic have no common linear factor. Thus these nine points exhaust the complex affine critical-point set.

## 2. Angular/equatorial audit — PASS (exact algebra)

For `sigma in {0,1}`, the leading form is

\[
H_{4,\sigma}(x,y)=3(x+\sigma y)^4-5(x+\sigma y)^2y^2+5y^4.
\]

The binary form is positive definite: with `u=x+sigma*y`, `v=y`, positivity follows from `3w²-5w+5` (discriminant `-35`) at `w=(u/v)²`, and the trivial `v=0` case. Both shears are invertible.

For `t=x/y`, set

\[
E_\sigma(t)=(1+t^2)\partial_t H_{4,\sigma}(t,1)-4tH_{4,\sigma}(t,1).
\]

- **sigma 0:** `E_0 = 2t(11t²−15)`. Three simple finite roots, `t=0, ±sqrt(15/11)`, and one further simple projective root `[1:0]` in the reciprocal chart. Angular values `A` at `[1:0], [0:1], [±sqrt(15/11):1]` are `3,5,35/52,35/52` respectively. The corresponding angular second derivatives have signs `−,−,+,+` (actual values `−22,−30,330/13,330/13`). The transverse second derivative `−4A` is always negative. Therefore the equatorial Morse contribution is **`(0,2,2)`**.
- **sigma 1:** `E_1 = −2(6t⁴+7t³−15t²−7t−1)`. The inner quartic has discriminant `−2,482,700`, four simple complex roots, and exactly **two real** roots by an exact Sturm count (one in `(-3,-2)` and the other in `(1,2)`). On a circle, two simple real angular stationary points must consist of one maximum and one minimum. Since `H4>0`, their projective contribution is **`(0,1,1)`**.

Exact resultants certify that the complex angular polynomials have no roots with `t²+1=0` (isotropic points of the denominator) and no roots where `H4(t,1)=0`. The sigma-0 root at infinity is also non-isotropic and has `H4(1,0)=3`.

## 3. Local completeness audit — PASS (theorem-level review)

### Pole at ε=0: length 9

For `p_ε=H4+ε z H3+ε² z² H2`, in chart `z=1` the eigenpoint equations may be chosen as

\[
(p_\varepsilon)_x-x(p_\varepsilon)_z=0,\qquad
(p_\varepsilon)_y-y(p_\varepsilon)_z=0.
\]

At `ε=0` they reduce to `(∂_x H4,∂_y H4)`. They are homogeneous cubics with no common complex projective zero, hence define an isolated complete intersection at `(x,y)=(0,0)` of local intersection multiplicity **`3·3=9`**.

For `x=εX, y=εY`, the normalized real potential is (up to a positive `ε⁴` multiplier)

\[
\frac{q_\sigma(X,Y)}{(1+\varepsilon^2(X^2+Y^2))^2}.
\]

It converges to `q_sigma` in `C²` on compact sets. Real implicit-function theorem supplies exactly nine *distinct and simple* branches, with original indices `(5,4,0)`, exhausting local multiplicity nine.

### Equator at ε=0: four length-one points

At each finite projective angular root `t0`, use chart `y=1` with coordinates `(t=x/y,w=z/y)`. On the non-isotropic patch, the complexified normalized limiting function is

\[
V_0(t,w)=\frac{h(t)}{(1+t^2+w^2)^2},\qquad h(t)=H_4(t,1).
\]

At `w=0`,

\[
V_{0,t}=\frac{E(t)}{(1+t^2)^3},\quad
V_{0,ww}=-\frac{4h(t)}{(1+t^2)^3},\quad
V_{0,tw}=0.
\]

At an angular root `t0` (where `E(t0)=0`),

\[
\boxed{\det D^2 V_0(t_0,0)
=-\frac{4h(t_0)E'(t_0)}{(1+t_0^2)^6}\ne0.}
\]

This directly verifies the complex local Jacobian condition: `E' != 0`, `h != 0` and `1+t² != 0` have all been separately checked. The remaining `[1:0]` root for sigma 0 uses the reciprocal chart `x=1` and has the same property. Each point therefore has multiplicity one and a unique holomorphic branch.

### No other limiting or perturbed points

At `ε=0`, the eigenpoint condition gives `λ z=0` because the homogeneous form is `z`-independent. If `z != 0`, then `λ=0`, and the cubic partial derivatives force `x=y=0` (the pole). If `z=0`, the eigenpoint equation is precisely the degree-four binary angular equation. Thus the limiting complex projective eigenscheme has *exactly five support points*, pole plus four equatorial points, and no positive-dimensional part.

Take disjoint small neighborhoods around these five points. Local holomorphic conservation-of-intersection-multiplicity under perturbation preserves the multiplicity sum within each neighborhood (nine and four copies of one), because the limiting equations have isolated zeros and remain nonzero on neighborhood boundaries. Stoll's multivariable Rouché theorem is a direct reference for this step. All near-pole and equatorial branches found above already use those multiplicities. If any other eigenpoint appeared along `ε_n→0`, projective compactness would force a subsequence limit at a *sixth* limiting zero outside the neighborhoods, which is impossible. Thus the construction yields exactly thirteen complex projective eigenpoints for small nonzero ε; the number of real ones depends on sigma as stated.

## 4. Limits of this audit

1. **Software verification:** The attached script rederives exact finite algebraic premises in SymPy, independently of the Maccioni verifier. It is not a second CAS, a formal proof assistant, or an external human referee.
2. **Analytic verification:** I audited the conditions for real/complex IFT, complex local intersection multiplicity, Stoll's conservation theorem, and compactness. Those steps are mathematical arguments rather than unit tests. The internal audit found no remaining gap.
3. **Existence versus witness:** `s` is known to be sufficiently large, without explicit numeric threshold. This is sufficient for existence; no finite-`s` exact integer certificate is claimed.
4. **Novelty:** Nothing here establishes originality of the scaled-homogenization method or a publishable discovery. The external review and novelty gates remain separate.

## 5. References checked

- Wilhelm Stoll, *The Multiplicity of a Holomorphic Map*, Inventiones Mathematicae **2** (1966), 15–58; Theorem 2.7 (multivariable Rouché). https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0002/00000023?_format=xml
- William Fulton, *Intersection Theory*, 2nd ed., §10.2 (Conservation of Number). https://djvu.online/file/Pl4avuZzLcI6I
- Dustin Cartwright and Bernd Sturmfels, *The Number of Eigenvalues of a Tensor*, Linear Algebra and its Applications **438** (2013), 942–952, as background for the generic count only, not as a replacement for the local argument. https://www.sciencedirect.com/science/article/pii/S0024379511004629

**BTC-004 ledger after this internal audit:** original 13 previously audited; two Maccioni supported by exact-rational verifier executed by another party, not external second CAS; four scaling configurations now have an independently derived algebra check and separate detailed analytic review, not independent outside certification; two remaining `(6,6,1)/(1,6,6)` unresolved; Gate 0 OPEN, zero confirmed novel discoveries.
