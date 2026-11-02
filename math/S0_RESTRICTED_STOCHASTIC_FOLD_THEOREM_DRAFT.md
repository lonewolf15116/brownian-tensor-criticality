# S0 restricted stochastic fold: theorem and proof draft

Status: author-derived, not independent reproduction, not novelty claim. Documentation/proof only; no numerical execution.

Define N(t,m)=m(1-3t^2)+3t^2-4t^3-t^4 and phi(t)=(-3t^2+4t^3+t^4)/(1-3t^2). For sufficiently small delta>0, phi is strictly increasing on (-delta,0) and strictly decreasing on (0,delta), with phi(0)=0 and phi(t)<0 for 0<|t|<delta. Define branch domains I_+= (0,delta), I_-=(-delta,0), and J_±=phi(I_±)=(phi(±delta),0) (endpoints may differ).

Let m_s=m0+2 sigma W_s with sigma>0 and m0 in J_±. Let t_s=psi_±(m_s), where psi_± is the inverse of phi on I_±, stopped at rho=inf{s>=0:m_s not in J_±}. Then t_s is adapted and continuous up to rho, and for s<rho Ito gives
 dt_s = [2 sigma/phi'(t_s)] dW_s - [2 sigma^2 phi''(t_s)/(phi'(t_s))^3] ds.
This is an exact stopped SDE for the restricted ONE-COEFFICIENT tensor family. Proof: inverse-function theorem, psi'=1/phi', psi''=-phi''/(phi')^3, Ito formula with (dm)^2=4 sigma^2 ds.

Let tau0=inf{s:m_s=0}. The unrestricted coefficient hitting-time CDF is P(tau0<=s)=2[1-Phi(|m0|/(2 sigma sqrt(s)))], s>0, by reflection principle; density |m0|/(2 sigma sqrt(2 pi s^3))*exp[-m0^2/(8 sigma^2 s)]. IMPORTANT: rho may occur earlier at the opposite boundary phi(±delta). Therefore tau0 is NOT in general the lifetime of the locally stopped eigenvector branch. The exact event of fold-reaching before chart exit is {tau0<tauL}, where L=phi(±delta)<m0<0; its probability is (m0-L)/(0-L), by harmonicity/gambler's ruin. No unqualified identification of tau0 with branch death is permitted.

The 35-dimensional Frobenius-isotropic tensor Brownian process is not confined to this one-coefficient family. This theorem does not describe its exact fold-coordinate process or full branch survival law.

Source: standard Brownian reflection principle and first passage, Cambridge University Press Brownian Motion chapter https://doi.org/10.1017/CBO9781139087698.003 . Related but distinct slow-fast dynamics: Bergeot, Berglund, Zogheib, Nonlinearity 39 075004 (2026), https://doi.org/10.1088/1361-6544/ae7ec0 .

Proof obligations remaining: choose explicit delta bounds if needed; external independent check of inverse branches, stopping conventions, and finite-interval hitting probability; theorem-level novelty audit.
