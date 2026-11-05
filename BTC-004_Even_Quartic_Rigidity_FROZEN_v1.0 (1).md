# BTC-004 — Frozen Internal Proof Record

**Record ID:** BTC-004-EQR-001  
**Version:** 1.0  
**Frozen date:** 2026-11-03  
**Status:** INTERNAL ANALYTICAL PROOF VERIFIED; independent external review outstanding; novelty not established.  
**Scope:** Real ternary quartics even in each coordinate, with 13 distinct real Morse critical points on real projective space.  
**Change control:** Do not alter this file in place. Any correction must issue a new version with an explicit change log and checksum.  
**Research stage:** BTC-004 Gate 0 OPEN. Global ledger: 8/21 triples realized; 13 globally unresolved; 0 confirmed novel discoveries.

## Proposition: Thirteen-point rigidity for even ternary quartics

Let

\[
f(x,y,z)=d_1x^4+d_2y^4+d_3z^4+a x^2y^2+b x^2z^2+c y^2z^2,
\]

where the six coefficients are arbitrary real numbers. Define

\[
F_f([x:y:z])=\frac{f(x,y,z)}{(x^2+y^2+z^2)^2}
\]

on \(\mathbb{RP}^2\). Suppose that \(F_f\) is Morse and has 13 distinct real critical points. Write \(m_i\) for the number of its critical points of Morse index \(i\), \(i\in\{0,1,2\}\). Then

\[
\boxed{(m_0,m_1,m_2)\in\{(4,6,3),(3,6,4)\}.}
\]

Both possibilities occur in this family. In particular, the other four arithmetically possible 13-real-index triples \((1,6,6),(2,6,5),(5,6,2),(6,6,1)\) are impossible within this even-power family. This is NOT a theorem about arbitrary ternary quartics.

## Proof

### 1. Squared-coordinate reduction and support accounting

On the unit sphere set \(u=x^2,v=y^2,w=z^2\). Then \(u,v,w\ge0\), \(u+v+w=1\), and the restricted function becomes the quadratic

\[
Q(u,v,w)=d_1u^2+d_2v^2+d_3w^2+auv+buw+cvw.
\]

For a projective point with exactly \(k\) nonzero coordinates, the same strictly positive squared-coordinate tuple gives \(2^{k-1}\) distinct projective sign choices. The vertices of the simplex always give three critical points. Each open edge has at most one stationary squared-coordinate point (unless its restriction is constant), producing two projective critical points. The simplex interior has at most one stationary point if its Hessian is nonsingular, producing four projective critical points.

Because \(F_f\) is Morse, it cannot have a constant restricted edge or a degenerate interior stationary point. Therefore the maximum number of real critical points is \(3+3\cdot2+4=13\). Equality forces the following strictly interior support conditions: each of the three edge stationary points lies between its endpoints, and the unique interior stationary point has \(u_*,v_*,w_*>0\). In particular, the three edge curvatures are nonzero and the interior quadratic Hessian is nonsingular.

### 2. General edge identity with all six coefficients

For the \(xy\)-edge use affine coordinates \(t=u\), \(n=w\), \(v=1-t-n\), so the edge is \(n=0\). The constant Hessian is

\[
K=\begin{pmatrix}\kappa&h\\h&\ell\end{pmatrix},\qquad
\kappa=2(d_1+d_2-a),\quad
h=2d_2-a+b-c,\quad
\ell=2(d_2+d_3-c).
\]

Let \((t_*,n_*)\) be the interior stationary point, where \(n_*>0\). For quadratic \(Q\),

\[
\begin{pmatrix}Q_t\\Q_n\end{pmatrix}
=K\begin{pmatrix}t-t_*\\n-n_*\end{pmatrix}.
\]

At the unique stationary point \((t_e,0)\) of the edge restriction, \(Q_t=0\), whence

\[
t_e-t_*=(h/\kappa)n_*.
\]

It follows exactly that

\[
\boxed{Q_n(t_e,0)=-\frac{\det K}{\kappa}n_*}.\tag{E}
\]

The same identity holds at each other edge with the corresponding affine coordinates and curvature. No assumption of equal pure quartic coefficients or vanishing mixed coefficients was used.

The Hessian of \(F_f\) at an edge projective point has two signs: the sign of the along-edge curvature \(\kappa\), and the sign of the inward derivative \(Q_n(t_e,0)\). Indeed, the simplex tangential coordinate is a local smooth coordinate on an open edge; the missing homogeneous coordinate enters quadratically, yielding a positive multiple of \(Q_n\) as the transverse second derivative. Equation (E) therefore gives

\[
\operatorname{sgn}(\text{transverse})=-\operatorname{sgn}(\det K)\operatorname{sgn}(\kappa).
\]

At a vertex, the Hessian sign in a direction toward a neighboring edge is the sign of the **inward** derivative of that edge restriction, not the derivative in a fixed global edge orientation. If the edge restriction has nonzero curvature \(\kappa\) and a unique critical parameter \(t_e\in(0,1)\), its inward derivatives at both endpoints have sign \(-\operatorname{sgn}(\kappa)\). The corresponding projective Hessian eigenvalue is a positive multiple of that inward derivative. Thus each vertex has Morse index equal to the number of its two adjacent edge curvatures that are positive.

### 3. Interior-index and case classification

The four full-support projective critical points all share the signature of the constant simplex Hessian \(K\), because squared coordinates give a local diffeomorphism on each full-support sign chamber.

**Case (a): \(K\) positive definite.** Every edge curvature is positive. Equation (E) makes the six edge points saddles; the axes are three maxima; and the four full-support points are minima. Hence \((m_0,m_1,m_2)=(4,6,3)\).

**Case (b): \(K\) negative definite.** Every edge curvature is negative. All six edge points are saddles; all three axes are minima; and the four full-support points are maxima. Hence \((m_0,m_1,m_2)=(3,6,4)\).

**Case (c): \(\det K<0\).** The four full-support points are saddles. Equation (E) makes every edge point an extremum: two minima for each positive edge curvature and two maxima for each negative edge curvature. The three vertex indices follow from the signs of their incident edge curvatures.

All three edge curvatures cannot be positive. That would give six edge minima, four interior saddles and three axis maxima, contradicting the Morse Euler relation \(m_0-m_1+m_2=\chi(\mathbb{RP}^2)=1\), since \(6-4+3=5\). All three cannot be negative either, by the same argument (three axis minima, four saddles, six edge maxima). Consequently the edge-curvature signs are mixed.

If one is positive and two are negative, the three axes contribute one minimum and two saddles; the edges contribute two minima and four maxima; and the interior contributes four saddles. The triple is \((3,6,4)\). If two are positive and one is negative, the axes contribute one maximum and two saddles; the edges contribute four minima and two maxima; and the interior four saddles. The triple is \((4,6,3)\).

These are all nonsingular Hessian possibilities. This proves the stated inclusion. \(\square\)

### 4. Attainment

For example \(f_+(x,y,z)=2x^4+y^4+z^4\) has three axis maxima, six edge saddles and four interior minima, hence \((4,6,3)\). Its negative \(f_-=-f_+\) interchanges minima and maxima, giving \((3,6,4)\). All 13 points in these examples are distinct and Morse.

### 5. Explicit degenerate-boundary exclusions

- If the restricted quadratic has edge curvature \(\kappa=0\), its restriction to that edge is either nonconstant linear, yielding no open-edge critical point, or constant, yielding a continuous critical set along that projective coordinate line. Neither admits exactly 13 distinct Morse critical points.
- If \(\det K=0\), an interior stationary point, if present, has degenerate Hessian (the squared-coordinate map is a local diffeomorphism in the interior). If absent, four full-support points cannot occur. Either way the 13-point Morse hypothesis fails.
- If an edge stationary point meets an endpoint, it is no longer an open-edge critical point distinct from a vertex; the corresponding vertex has a zero Hessian direction. Similarly, an interior stationary point on an edge fails to provide four distinct full-support points and has a zero transverse Hessian direction.

### 6. Interpretation and scope

The two allowed triples each arise by two mechanisms:

1. With definite interior Hessian: all six saddles lie on open edges.
2. With indefinite interior Hessian: four saddles are full-support and two lie at vertices; no edge saddles occur.

This is a **family-level obstruction** for quartics even in all three coordinates in an orthonormal frame. It does **not** establish that any globally unresolved triple is impossible for general real ternary quartics. It implies that a quartic realizing one of the four excluded extreme triples cannot have a representation involving only even powers in any orthonormal coordinate frame.

## Verification and release gates

- [x] Correct the mixed Hessian coefficient to \(h=2d_2-a+b-c\).
- [x] Give the exact edge identity for arbitrary six coefficients.
- [x] State strictly interior edge parameter \(t_e\in(0,1)\).
- [x] Specify inward derivatives at vertices.
- [x] Treat definite and indefinite Hessian cases.
- [x] Exclude boundary/degenerate cases under the hypotheses.
- [x] Provide witnesses for both allowed triples.
- [ ] Independent external human mathematical audit.
- [ ] Thorough prior-art novelty audit.
- [ ] Publication readiness decision.

**Research readiness:** provisional, not a peer-review assessment.  
**Novelty claim:** NONE.  
**External review:** NOT COMPLETED.  
**No repository mutations, numerical experiments, or new computational evidence are represented by this record.**

## Preliminary prior-art pointers (not an exhaustive novelty review)

- Mauro Maccioni, *The number of real eigenvectors of a real polynomial*, arXiv:1606.04737 (studies real eigenvector counts).
- Joao Marcos Vensi Basso and Loring W. Tu, *Basis-Free Analysis of Singular Tuples and Eigenpairs of Tensors*, arXiv:2012.07313 (Morse-theoretic framework).

## Freeze metadata

This file is frozen as version 1.0. SHA-256 checksum is supplied separately in the companion `.sha256` file; any revised mathematics must be released under a new version rather than silently overwriting this record.
