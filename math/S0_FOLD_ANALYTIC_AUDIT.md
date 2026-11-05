# S0 independent analytic audit: explicit fold (2026-11-02)

Status: independent manual algebraic re-derivation and literature comparison; NOT independent human review, computer algebra, or numerical execution. Gate 0 only.

## Candidate
f_mu(x)=x1^4+mu*x1^3*x2+2*x1^2*x2^2+x1*x2^3, x in S^3. Coefficients define a fully symmetric order-four tensor by dividing each monomial coefficient by its permutation multiplicity: T1111=1, T1112=mu/4, T1122=2/6=1/3, T1222=1/4; other components zero.

At mu=0, x=e1: T x^3=e1, lambda=1. Tangent H=P(3T[e1,e1,.,.]-I)P has diagonal (0,-1,-1) in basis e2,e3,e4. The zero eigenvalue is simple. For mu !=0, e1 is generally not an eigenvector, as expected in an unfolding.

## Exact reduced equation
In the local chart x=(cos theta,sin theta,0,0), t=tan theta, f_mu=(1+mu*t+2*t^2+t^3)/(1+t^2)^2. Its t derivative is

G(t,mu)=[mu+3*t^2-3*mu*t^2-4*t^3-t^4]/(1+t^2)^3.

Thus G(0,0)=0, G_t(0,0)=0, G_mu(0,0)=1, and G_tt(0,0)=6. These are standard generic fold conditions for the reduced stationary equation. The implicit function theorem gives a unique local parameter curve mu=phi(t) with phi(0)=phi'(0)=0, phi''(0)=-6; hence mu=-3*t^2+O(t^3). Consequently sufficiently small negative mu has two nearby simple stationary solutions, positive mu has none, and mu=0 has a double stationary root.

## No omitted transverse branches near e1
The polynomial has no x3,x4 dependence. At a normalized eigenpair near (mu,x)=(0,e1), lambda=f_mu(x) remains near 1. For j=3,4, the eigen-equation reads 0=lambda*x_j, forcing x3=x4=0. Hence the local reduction is exact for all nearby eigenpairs, not just a convenient invariant slice.

## Projective convention and limitations
Because order four is even, x and -x represent the same eigenvector direction and the same eigenvalue. Near e1 the chart x1>0 fixes the sign; antipodal solutions are not counted twice. The fold is a local birth/death of nearby real eigenvector directions under deterministic parameter mu, not proof of global disappearance of eigenvectors or any Brownian lifetime law. Singularity det(H)=0 need not imply branch death in general.

## Prior art comparison
- Hannes Uecker, *Numerical Continuation and Bifurcation in Nonlinear PDEs*, Chapter 2, DOI 10.1137/1.9781611976618.ch2: Lyapunov-Schmidt reduction and local folds. Our local fold is an instance of standard theory, not a new normal form.
- Yuri Kuznetsov, *Elements of Applied Bifurcation Theory*: standard fold conditions via left/right nullvectors, quadratic nonlinearity and parameter transversality. https://www.ma.imperial.ac.uk/~dturaev/kuznetsov.pdf
- Shenglong Hu, *Nondegeneracy of eigenvectors and singular vector tuples of tensors*, arXiv:2104.05900: generic tensor Z-eigenvectors are nondegenerate; our singular example is a special parameter configuration, consistent with this result.
- Shenglong Hu and Liqun Qi, *The E-eigenvectors of tensors*, DOI 10.1080/03081087.2013.828721: algebraic discriminant/eigenvector geometry; further theorem-level comparison remains open.

## Disposition
S0-A fold construction: internally analytically verified (explicit exact formula and transverse argument). External independent verification pending. S0 singularity taxonomy and stochastic claims remain open. No novelty claim; no Rust compilation or numerical work authorized or performed.
