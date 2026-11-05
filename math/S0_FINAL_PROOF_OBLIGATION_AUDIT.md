# S0 final proof-obligation audit: regular selection, stopping and singular-set hitting

Status: internal mathematical audit, NOT independent external reproduction; no numerical execution or G1 advancement. 2026-11-02.

## 1. Local branch selection theorem
Define F(T,x)=P_x(Tx^3) on Sym^4(R4) x S3. Fix (T0,x0) with F=0 and tangent H invertible. In a smooth local chart on S3 around x0, the implicit function theorem yields neighborhoods U of T0 and V of x0 and a unique smooth x=X(T) in V solving F(T,x)=0 for T in U. Restrict to a hemisphere fixing x~-x. This proves local uniqueness only, not uniqueness among all eigenvectors or globally along arbitrary tensor paths. The derivative in ambient tangent form is DX(T)[E]=-H^{-1}P_x(Ex^3), with tangent vectors identified consistently. Smoothness holds only on an open regularity domain and may fail approaching H-singularity.

## 2. Stopping domain
Choose a relatively compact open tensor neighborhood U0 whose closure lies in the implicit-function neighborhood U, and start T0 in U0. For continuous adapted T_s=T0+sigma B_s, tau_U0=inf{s>=0:T_s notin U0} is a stopping time. On s<tau_U0, X(T_s) is adapted continuous and satisfies the Ito formula with the full 35D Hessian term. Exit from U0 is merely a certificate that the chosen chart is no longer guaranteed; it does not prove eigenvector branch death, singularity, or nonexistence of continuation. An intrinsic first-singularity stopping time requires a carefully specified continued branch and hitting of det H=0; it is not defined globally by this local theorem.

## 3. Hitting the singular set in full 35D
The discriminant D={T: exists x in RP3 with F(T,x)=0 and det H(T,x)=0} is an algebraic/semialgebraic exceptional set (subject to elimination/real constraints). An explicit corank-one fold with a nonzero unfolding derivative demonstrates a smooth codimension-one local discriminant sheet near the example: in suitable local tensor coordinates a smooth scalar fold-control function a(T) has a(T*)=0 and Da(T*) !=0. Because Frobenius-isotropic Brownian motion has nonzero variance in the normal direction, this sheet is locally accessible with positive probability from appropriate nearby starting tensors, before exiting a suitably chosen neighborhood. This is a local accessibility statement, not almost-sure finite-time hitting, a universal hitting distribution, or a global statement for every initial tensor.

For a rigorous proof of positive-probability local hitting, choose nearby initial T with a(T)<0, choose a continuous finite-time deterministic tensor path crossing the smooth sheet transversely inside the chart, and use full support of nondegenerate Brownian motion in continuous-path topology: an open tube around that path has positive probability; by continuity/sign change a(T_s) crosses zero. The path can be chosen to begin at the specified nearby initial T, and the tube small enough to stay inside the chart. This is a proof sketch requiring explicit establishment of the smooth discriminant sheet via Lyapunov-Schmidt reduction and of the corresponding branch behavior on the approach side. It does not imply the same probability for arbitrary starting tensors.

Brownian paths are not differentiable: do not assert pathwise transverse derivative at the hitting time. 'Nonzero normal diffusion' is the correct local nondegeneracy statement. Crossing the sheet can destroy the chosen local fold pair, but may leave other eigenvectors elsewhere; first H-singularity and branch death remain different concepts.

## 4. Remaining proof obligations
(A) Write the parameter-dependent Lyapunov-Schmidt reduction for all 35 coefficients and prove the local discriminant sheet is smooth near the explicit fold; the one-parameter transverse direction supplies the needed derivative but full reduction is not yet written.
(B) Formalize measurable branch continuation across overlapping charts and its maximal regular stopping time, including possible monodromy/reselection.
(C) Prove local positive-probability hitting with precise time and neighborhood assumptions; no exact 35D law currently.
(D) Independent external check and theorem-level prior-art audit remain outstanding.

## Disposition
Regular-branch implicit function theorem and local stopping-time formulation: supported. Full 35D discriminant-hitting: conditional local argument/proof sketch, NOT established global theorem. S0 remains under internal scrutiny and unaccepted. Confirmed novel discoveries: zero. No permission to enter G1, run experiments, release reproduction package, or merge PR #1.
