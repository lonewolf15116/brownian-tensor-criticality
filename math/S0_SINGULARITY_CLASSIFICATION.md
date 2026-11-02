# S0 singularity taxonomy — working mathematical definitions

Let V=Sym^4(R^4), x in S^3, and F(T,x)=P_x(Tx^3), P_x=I-xx^T. A normalized Z-eigenpair has F=0 and lambda=T[x^4]. The derivative with respect to x, expressed in tangent coordinates, is H=P_x(3T[x,x,.,.]-lambda I)P_x restricted to x-perp. A *regular eigenpair* has det(H) != 0. A *singular eigenpair* has det(H)=0. The first singularity time of a locally tracked branch is a candidate stopping time; it is NOT automatically a branch-death time.

Working classes (not exhaustive): (A) corank-one singularity, with one-dimensional kernel; (B) corank-one higher-order degeneracy, when reduced quadratic coefficient vanishes; (C) corank-two/three singularity with interacting soft modes. Additional distinctions: transverse versus tangent parameter forcing, persistent symmetry-enforced degeneracy, branch crossing, and eigenpair reselection.

At a corank-one point, choose tangent kernel unit v, cokernel unit w (for symmetric H, w=v). Lyapunov-Schmidt reduction of F(T0+mu E,x(u,mu))=0 yields scalar g(u,mu)=A mu + B u^2 + higher order terms, provided complement derivative is invertible. Generic fold sufficient conditions: A=<w,D_T F[E]> !=0 and B=(1/2)<w,D_x^2 F[v,v]> !=0 in a consistent local chart, with complement corrections accounted for in the reduced derivative. These are hypotheses to check in explicit tensor examples, not yet a complete classification theorem.

Brownian forcing: dT=sigma sum F_k dW^k on an orthonormal Frobenius basis. The projected forcing along the fold normal is random. A one-dimensional reduced control Brownian motion is only a local approximation after fixing chart, covariance and stopping domain; no global fold SDE is asserted.

Proof obligations: verify coordinate independence of conditions; construct a genuine tensor fold with A,B nonzero; distinguish H-singularity from branch termination; assess symmetry x~-x; verify transversality and codimension; compare existing tensor eigendiscriminant and stochastic-fold results.
