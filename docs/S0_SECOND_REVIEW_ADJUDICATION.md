# S0 second reviewer critique — adjudication

Date 2026-11-02. User-supplied reviewer report; independence not externally verified. S0 remains unaccepted.

## Alleged derivative/sign error — REJECT
For N=1+mu*t+2t²+t³, g=N/(1+t²)², derivative denominator is 4t(1+t²). Thus dg/dt=[(mu+4t+3t²)(1+t²)-4tN]/(1+t²)³ = [mu+3t²-3mu*t²-4t³-t⁴]/(1+t²)³. The report used 2tN instead of 4tN. The original G and phi=(-3t²+4t³+t⁴)/(1-3t²) are correct. No change to these formulas.

## Alleged stochastic normalization error — WITHDRAWN BY REVIEWER'S OWN CALCULATION
The 1112 orbit has 4 entries, a unit Frobenius tensor has entries 1/2, giving polynomial coefficient 2. Thus the coefficient mu has volatility 2sigma and bracket 4sigma² ds. Both coefficient hitting CDF and density supplied in packet are correct. Explain this chain explicitly.

## Accepted clarifications
- H is restricted to x-perp, not invertibility of ambient projected 4x4 matrix.
- Choose relatively compact U0 with closure inside IFT domain U to ensure bounded DX and D²X for stopped Ito.
- LS reduction must explicitly invert the transverse block and prove it stays invertible locally; transverse eigenvalues -1,-1 at base point imply local persistence.
- Local discriminant sheet and normal nondegeneracy must be proved before a positive-probability hitting theorem; tensor-space discriminant hit is not automatically global branch death.
- Distinguish standard deterministic fold, standard Brownian first passage, tensor perturbation prior art from any genuinely novel stochastic result.

## Verified literature leads
Abo, Seigal, Sturmfels, Eigenconfigurations of Tensors, arXiv:1505.05729 (2015), published Contemporary Mathematics 685 (2017), DOI 10.1090/conm/685. Scope and precise eigendiscriminant statements require theorem-level checking.
Che, Qi, Wei, Perturbation bounds of tensor eigenvalue and singular value problems with even order, Linear and Multilinear Algebra 64(4), 622–652 (2016), DOI 10.1080/03081087.2015.1074153.

## Gate disposition
REVISE S0, no G1, no numerical work, no PR merge. External reviewer feedback is not equivalent to verified independent reproduction.
