# S0 restricted stochastic fold — revised theorem (2026-11-02)

**Status:** revised after user-provided Manus AI audit. Restricted one-coefficient theorem only; no G1 authorization, no full 35D lifetime theorem.

## Definitions and exact algebra
For the ordered-index contraction f_T(x)=sum_{ijkl}T_ijkl x_i x_j x_k x_l, take f_mu(x)=x1^4+mu*x1^3*x2+2*x1²*x2²+x1*x2³. At mu=0,x=e1, lambda=1 and H on x-perp (basis e2,e3,e4) equals diag(0,-1,-1); H is one quarter of the spherical Riemannian Hessian. With x=(1,t,0,0)/sqrt(1+t²), g=(1+mu*t+2t²+t³)/(1+t²)² and

g_t=[mu*(1-3t²)+3t²-4t³-t⁴]/(1+t²)³.

**The +3t² term is mandatory.** Thus phi(t)=(-3t²+4t³+t⁴)/(1-3t²)=-3t²+4t³+10t⁴+O(t⁵). For small mu<0, there are two local branches; for mu>0, none. The fold is quadratic, not cubic-leading.

## Stopped inverse theorem
Fix sigma>0 and delta>0 sufficiently small so phi'<0 on (0,delta), phi'>0 on (-delta,0), phi(t)<0 for nonzero |t|<=delta, and 1-3delta²>0. For either sign epsilon in {+,-}, set I_+=(0,delta), I_-=(-delta,0), L_epsilon=phi(epsilon*delta)<0 and J_epsilon=(L_epsilon,0). Let mu0 in J_epsilon, W standard BM on a usual filtered probability space, mu_s=mu0+2sigma W_s, tau0=inf{s>=0:mu_s=0}, tauL=inf{s>=0:mu_s=L_epsilon}, rho=tau0 wedge tauL. All are stopping times; tau0 and tauL are individually finite almost surely for one-dimensional driftless BM, and rho is finite almost surely. Let psi_epsilon=(phi|I_epsilon)^(-1). For s<rho, t_s=psi_epsilon(mu_s) is adapted, continuous and a semimartingale locally. For each compact subinterval J' of J_epsilon, stop at its exit before applying Ito; then

dt_s = [2sigma/phi'(t_s)]dW_s - [2sigma² phi''(t_s)/(phi'(t_s))³]ds, s<rho,

in the local/stopped sense. Coefficients diverge approaching t=0, and no Ito decomposition through rho is asserted. On tau0<tauL, t_s tends to 0; on tauL<tau0, it tends to epsilon*delta. The latter is an artificial local cutoff, not singularity or global branch death.

## Hitting probabilities and scope
P(tau0<=s)=2[1-Phi(|mu0|/(2sigma sqrt(s)))], s>0; f_tau0(s)=|mu0|/(2sigma sqrt(2pi s³))*exp[-mu0²/(8sigma²s)]. These are for **unrestricted scalar coefficient first hitting of zero**, not for the killed interval lifetime rho. P(tau0<tauL)=(mu0-L_epsilon)/(-L_epsilon). Exact time-resolved two-sided exit requires separate calculation. No transfer of these formulas to full 35D tensor branch survival.

The 1112 Frobenius-unit orbit has four entries 1/2 and quartic polynomial 2x1³x2. Therefore dmu=2sigma dW_1112 and d[mu]=4sigma²ds for the **raw polynomial coefficient**, not for a nonlinear 35D fold-control coordinate.

## Remaining
Independent check of full local continuation; 35D parameter-dependent Lyapunov-Schmidt proof; first-singularity definition; theorem-level novelty audit. S0 remains REVISE, not accepted.
