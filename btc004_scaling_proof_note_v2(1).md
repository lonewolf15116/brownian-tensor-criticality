# BTC-004: Scaled homogenization of an affine quartic — standalone proof note

**Status:** Revised qualitative existence proof (internal draft; not externally reviewed).  
**Scope:** Four Morse-index triples `(5,6,2)`, `(2,6,5)`, `(5,5,1)`, `(1,5,5)`.  
**No claimed novelty.** The note establishes existence for all sufficiently large real `s`; it does not provide a numerical threshold or a fixed integer-coefficient quartic witness.

## Statement

Define the affine polynomial

\[
q(X,Y)=3X^4-5X^2Y^2+5Y^4+20X^2Y-32Y^3+X^2+2Y^2.
\]

For \(\sigma\in\{0,1\}\), let \(q_\sigma(X,Y)=q(X+\sigma Y,Y)\), and write \(q_\sigma=H_{4,\sigma}+H_{3,\sigma}+H_{2,\sigma}\) as a sum of homogeneous components. **In this theorem the binary leading forms \(H_{4,0}\) and \(H_{4,1}\) are positive definite on \(\mathbb R^2\setminus\{0\}\); this is an explicit hypothesis used in the index classification below.** For \(s>0\) define the homogeneous ternary quartic

\[
F_{s,\sigma}(x,y,z)=s^4 H_{4,\sigma}(x,y)+s^3 z H_{3,\sigma}(x,y)+s^2z^2 H_{2,\sigma}(x,y).
\]

Regard it as a function on \(\mathbb{RP}^2\) via \(F_{s,\sigma}(x,y,z)/(x^2+y^2+z^2)^2\). **Theorem.** For every sufficiently large \(s\), all projective critical points are isolated and nondegenerate. Their real Morse triples are

\[
\sigma=0:\ (m_0,m_1,m_2)=(5,6,2),\qquad
\sigma=1:\ (m_0,m_1,m_2)=(5,5,1).
\]

Their negatives realize the reflected triples `(2,6,5)` and `(1,5,5)`.

## Proof

### I. Nine affine Morse critical points

\[
q_X=2X(6X^2-5Y^2+20Y+1),
\quad q_Y=4Y(5Y^2-24Y+1)+X^2(20-10Y).
\]

For \(X=0\), the solutions are

\[
(0,0),\quad \left(0,\frac{12\pm\sqrt{139}}5\right).
\]

For \(X\ne0\), substitute \(X^2=(5Y^2-20Y-1)/6\) in \(q_Y=0\). The resulting polynomial (up to a nonzero scalar) factors as

\[
35Y^3-138Y^2-183Y-10=35\left(Y+\frac2{35}\right)(Y-5)(Y+1).
\]

All six solutions from its three roots are real:

\[
(\pm2,-1),\quad(\pm2,5),\quad
\left(\pm\sqrt{\frac{13}{490}},-\frac2{35}\right).
\]

By direct Hessian evaluation: `(0,0)` is a minimum; `(±2,-1)` and `(±2,5)` are minima (Hessian determinants respectively `6336`, `33984`, with `q_XX=96`); both nonzero axial critical points are saddles; and the last pair are saddles with determinant `-303732/8575`. Thus there are **five minima and four saddles**, all nondegenerate. The two cubic partial derivatives have nine distinct complex intersections and hence, by Bézout, these are all critical points of \(q\) over \(\mathbb C\).

The shear \((X,Y)\mapsto(X+\sigma Y,Y)\) is invertible and preserves the count and Morse indices of these affine critical points.

### II. Persistence near the projective pole

Set \(\varepsilon=1/s\) and divide the homogeneous polynomial by its positive scalar \(s^4\):

\[
p_{\varepsilon,\sigma}(x,y,z)
=H_{4,\sigma}(x,y)+\varepsilon zH_{3,\sigma}(x,y)
+\varepsilon^2 z^2H_{2,\sigma}(x,y).
\]

In the projective chart \(z=1\), introduce \(x=\varepsilon X\), \(y=\varepsilon Y\). Then the normalized potential equals

\[
\varepsilon^4\frac{q_\sigma(X,Y)}{(1+\varepsilon^2(X^2+Y^2))^2}.
\]

The positive scalar \(\varepsilon^4\) does not affect stationary points or their indices. The remaining expression, together with its first two derivatives, converges locally uniformly to \(q_\sigma\) as \(\varepsilon\to0\). Since each of its nine critical points is Morse, the real implicit function theorem produces **nine distinct real Morse branches** near \([0:0:1]\), preserving indices `(5,4,0)`.

### III. Equatorial branches and Hessian indices

On the unit sphere let

\[
x=\sqrt{1-z^2}\cos\theta,\quad
 y=\sqrt{1-z^2}\sin\theta.
\]

Write \(A(\theta)=H_{4,\sigma}(\cos\theta,\sin\theta)\), \(B(\theta)=H_{3,\sigma}(\cos\theta,\sin\theta)\), and \(C(\theta)=H_{2,\sigma}(\cos\theta,\sin\theta)\). The normalized potential (restricted to the sphere) is exactly

\[
\Phi_\varepsilon(\theta,z)
=(1-z^2)^2 A(\theta)+\varepsilon z(1-z^2)^{3/2}B(\theta)
+\varepsilon^2 z^2(1-z^2)C(\theta).
\]

At a limiting equatorial point satisfying \(A'(\theta_0)=0\), its Hessian is

\[
D^2\Phi_0(\theta_0,0)=
\begin{pmatrix}A''(\theta_0)&0\\0&-4A(\theta_0)\end{pmatrix}.
\]

For both shears, the binary leading form
\[
H_{4,\sigma}=3(x+\sigma y)^4-5(x+\sigma y)^2y^2+5y^4
\]
is strictly positive on the real unit circle. Indeed, putting \(u=x+\sigma y\), \(v=y\), one has \(3u^4-5u^2v^2+5v^4>0\) for \((u,v)
e(0,0)\): if \(v
e0\), the quadratic \(3(u/v)^4-5(u/v)^2+5\) in \((u/v)^2\) has negative discriminant \(-35\) and positive leading coefficient; the case \(v=0\) is immediate. Each shear is invertible, so this proves positive definiteness for both \(\sigma=0,1\).

Consequently \(-4A(	heta_0)<0\), and every simple real angular maximum lifts to a projective maximum, while every simple real angular minimum lifts to a projective saddle.

**Scope of the method.** The implicit-function construction does **not** require global positive definiteness of \(H_4\): locally it requires \(A(	heta_0)
e0\) and \(A''(	heta_0)
e0\). A sign-changing leading form can also be treated at its nondegenerate, nonzero-valued angular critical points, with Morse index determined by the signs of \(A''\) and \(-4A\). Positive definiteness is needed here to obtain the *particular* index contributions \((0,2,2)\) and \((0,1,1)\), not for the existence mechanism itself. If \(A=0\) or \(A''=0\) at a limiting critical point, this simple Hessian/IFT argument is insufficient.

The ordinary implicit function theorem applies whenever \(A''(\theta_0)\ne0\). An equatorial branch need **not** lie exactly at \(z=0\) for positive \(\varepsilon\). In fact

\[
z_\varepsilon=\frac{\varepsilon B(\theta_0)}{4A(\theta_0)}+O(\varepsilon^2).
\]

In affine coordinate \(t=x/y\), angular critical directions are the roots of

\[
(1+t^2)\frac{d}{dt}H_{4,\sigma}(t,1)-4tH_{4,\sigma}(t,1)=0,
\]

with \([1:0]\) checked separately when the degree drops.

* For \(\sigma=0\), this equation is \(2t(11t^2-15)=0\); together with \([1:0]\), there are four simple real angular points, two minima and two maxima. Their projective contribution is `(0,2,2)`.
* For \(\sigma=1\), the equation is \(-2(6t^4+7t^3-15t^2-7t-1)=0\). The quartic factor has discriminant \(-2,482,700<0\), hence exactly two simple real roots and one nonreal conjugate pair. The two real critical points are one angular minimum and one angular maximum, contributing `(0,1,1)`.

### IV. Completeness: conservation of local eigenpoint multiplicity

All complex projective eigenpoints are zeros of the polynomial eigenvector equations
\[
\nabla p_{\varepsilon,\sigma}(x,y,z)\wedge(x,y,z)=0.
\]
The following conservation argument is **local** and does not infer flatness of an arbitrary family merely from a generic tensor-eigenpoint count.

**Lemma (local conservation of number).** Consider a holomorphic family of two polynomial equations on a complex surface. If the common zero set at parameter \(0\) consists of finitely many isolated points, choose disjoint sufficiently small neighborhoods of these points, with no common zeros on their boundaries. For all sufficiently small parameter values, the sum of local intersection multiplicities inside each neighborhood equals the local intersection multiplicity at parameter \(0\). This is the standard conservation-of-number property for isolated complete-intersection zeros. Since \(\mathbb{CP}^2\) is compact, if these neighborhoods contain **all** zeros of the limiting system, no additional zeros can occur elsewhere for sufficiently small parameters: otherwise a sequence of such extra zeros would have a limiting zero outside the neighborhoods.

We apply the lemma to the projective eigenpoint equations using local coordinates and two independent components of the cross product near each limiting point.

**Pole.** At \(\varepsilon=0\), the homogeneous form is \(H_{4,\sigma}(x,y)\), independent of \(z\). In the chart \(z=1\), the eigenpoint equations reduce to \((H_{4,\sigma})_x=(H_{4,\sigma})_y=0\). Because the binary quartic is square-free over \(\mathbb C\), these homogeneous cubics have no common nonzero zero in \(\mathbb C^2\). They form a regular sequence and their intersection at the origin has local multiplicity \(3\cdot3=9\). The nine distinct simple complex branches supplied by Part II (in fact all real) exhaust this local multiplicity.

**Equator.** Away from the pole, the \(z\)-component of \(\nabla H_{4,\sigma}\) vanishes, so the projective eigenvector equations imply \(z=0\): for \(z\ne0\) the eigenvalue parameter would be zero, forcing the binary gradient to vanish, contrary to square-freeness. On \(z=0\) the equation is the binary angular eigenpoint equation from Part III. It has exactly four simple roots over \(\mathbb C\) for each \(\sigma\); there are no additional limiting projective eigenpoints. The corresponding points are non-isotropic (their \(x^2+y^2\ne0\)); for example \(H_{4,0}(i,1)=13\), \(H_{4,1}(i,1)=-7-10i\), and the conjugate evaluations are nonzero, so \(t=\pm i\) cannot satisfy the angular equation. The two-dimensional limiting Hessian is nonsingular at each equatorial root because \(A\ne0\) and the angular root is simple. The complex implicit function theorem therefore gives one distinct simple branch at each equatorial point.

The limiting eigenpoint scheme has nine local zeros counted with multiplicity at the pole and four simple zeros on the equator. For sufficiently small \(\varepsilon\), these are exhausted by the nine pole branches and four equatorial branches. Local conservation of number plus compactness excludes any further eigenpoints. This also agrees with the standard total complex eigenpoint count \(1+3+9=13\), but the completeness argument does not assume that this generic count alone automatically applies to the degenerate \(\varepsilon=0\) form.

For \(\sigma=0\), all four equatorial branches are real. For \(\sigma=1\), exactly two are real and the remaining conjugate pair stays nonreal under sufficiently small real perturbations.

Combining the nine affine branches with the real equatorial contributions gives

\[
\sigma=0:\quad (5,4,0)+(0,2,2)=(5,6,2),
\]

\[
\sigma=1:\quad (5,4,0)+(0,1,1)=(5,5,1).
\]

Negating the form interchanges indices zero and two. **QED.**

## Audit boundary

- This is a **qualitative existence proof**. It does not identify an explicit finite value of \(s\), and no such value is required for the stated theorem.
- The completeness proof uses local intersection multiplicity plus conservation of number for isolated holomorphic zeros, with the standard complex eigenpoint count \(13\) only as a consistency check. A referee should review the local algebra, conservation lemma, and isotropic-direction exclusion.
- The two-variable IFT also applies to some sign-changing leading forms; positive definiteness is a hypothesis of this **specific index claim**, not a general requirement of scaled homogenization. No external independent mathematician or second CAS has reviewed this note. It should not be described as independently certified or a new theorem relative to existing literature.
