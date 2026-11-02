# S0 scrutiny: stopped inverse branches and 35D distinction

Status: internal proof scrutiny; no experiments, external reproduction, G1 approval, or merge.

## Restricted model and stopping
Let phi(t)=(-3t^2+4t^3+t^4)/(1-3t^2). Choose delta>0 sufficiently small so 1-3delta^2>0, phi'<0 on (0,delta), phi'>0 on (-delta,0), and phi(t)<0 for nonzero |t|<=delta. For positive branch let L=phi(delta)<m0<0. Define m_s=m0+2sigma W_s, tau_0=inf{s:m_s=0}, tau_L=inf{s:m_s=L}, rho=tau_0 wedge tau_L. Brownian paths continuous, so rho is a stopping time and is almost surely finite. For s<rho, t_s=psi(m_s) is uniquely defined in (0,delta), continuous and adapted. It is not defined as a regular inverse at the fold endpoint. At rho, t_s has a continuous endpoint limit: t->0 on tau_0, t->delta on tau_L. The endpoint t=0 is singular; delta is an artificial chart boundary, not branch death.

Reflection principle: P(tau_0<=s)=2[1-Phi(|m0|/(2sigma sqrt(s)))] for unrestricted Brownian coefficient, but P(rho<=s, m_rho=0) is a *two-sided exit* probability, not this CDF. P(tau_0<tau_L)=(m0-L)/(0-L). An exact time-dependent fold-exit distribution requires killed-interval Brownian transition or spectral expansion; do not substitute the one-sided reflection formula. The hitting-time density for tau_0 is |m0|/(2sigma sqrt(2pi*s^3))*exp(-m0^2/(8sigma^2*s)).

## Exact inverse branch Ito calculation
For s<rho, psi'=1/phi'(t), psi''=-phi''(t)/(phi'(t))^3. Ito: dt=[2sigma/phi'(t)]dW - [2sigma^2 phi''(t)/(phi'(t))^3]ds. Coefficients are smooth on compact subsets of (0,delta), but diverge as t->0. Do not claim a classical global SDE solution through the fold. For negative branch use (-delta,0) and L=phi(-delta); analogous formulas apply. Starting m0=0 is excluded from regular inverse theorem.

## Full 35D model: implicit regular-branch SDE
Let T_s=T_0+sigma sum_{a=1}^{35} E_a W_s^a with E_a Frobenius orthonormal. Let a local smooth regular Z-eigenvector selection x=X(T) in a fixed projective chart (exists by implicit function theorem while H invertible). Let U be an open tensor neighborhood on which X is defined and smooth, and tau_U=inf{s:T_s notin U}. Then, for s<tau_U,
 dx_s=sigma sum_a D X(T_s)[E_a] dW_s^a +(sigma^2/2)sum_a D^2 X(T_s)[E_a,E_a]ds,
with D X(T)[E]=-H^{-1}P(E x^3) in tangent coordinates. The second derivative includes the manifold/chart curvature and the dependence of H, P, x on T; it is not generally zero. A fixed sign convention is required; x and -x are equivalent in projective space. The full process is not confined to the one-coefficient line, and its singular set is curved in general. Therefore mu_s=m0+2sigma W_s and the restricted hitting law do NOT describe full 35D fold lifetime.

## Precise noise statement at base point
The basis orbit (1112) has four equal entries 1/2; its polynomial coefficient is 2. Consequently the linear functional extracting x1^3*x2 has Brownian bracket 4sigma^2 ds, exactly. It is only a first-order fold-normal coordinate at the base tensor, not an exact stochastic coordinate of the discriminant for all times. Other tensor noise components also perturb the branch and Hessian, and may produce drift after nonlinear coordinate changes.

## Review outcome
No inconsistency in the local inverse-branch Ito formula. Material correction to interpretation: one-sided first-passage CDF cannot be called the local branch-lifetime law, and exit at delta is not branch death. Full 35D regular-branch Ito equation is available implicitly, but no exact singular crossing/first-hit law or stochastic critical scaling is proved. S0 remains under scrutiny and unaccepted. Independent external reproduction remains absent.
