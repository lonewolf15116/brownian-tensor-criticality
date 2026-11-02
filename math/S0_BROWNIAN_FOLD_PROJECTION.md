# S0: Brownian forcing projection at the explicit tensor fold

Status: symbolic derivation, local at T0 and x=e1; no stochastic simulation, no claim of exact global reduction.

Use the Frobenius-orthonormal basis of Sym^4(R^4). The normalized basis tensor F_(1112) has four entries each 1/2, so its quartic polynomial is 2*x1^3*x2. For dT=sigma*sum F_alpha dW_alpha, the coefficient mu of x1^3*x2 receives dmu=2*sigma*dW_(1112). Thus quadratic variation d[mu]=4*sigma^2 dt. Equivalently, the e2 coordinate of P(dT e1^3) is (sigma/2)dW_(1112), and derivative of quartic stationary equation along e2 is four times this, namely 2*sigma*dW_(1112). Other orthonormal basis directions do not contribute to this first-order fold-normal forcing at (T0,e1).

For f_mu=x1^4+mu*x1^3*x2+2*x1^2*x2^2+x1*x2^3, the exact local stationarity numerator is N(t,mu)=mu+3t^2-3mu*t^2-4t^3-t^4. Hence at leading order the local random fold control is mu_t≈mu_0+2*sigma*W_t, and the formal local roots are t≈±sqrt(-mu_t/3) while mu_t<0.

CAUTION: the full 35-dimensional tensor Brownian motion also changes all other coefficients, including fold location and the reduced quadratic term. The displayed 1D process is the linear fold-normal projection at the base tensor, not an exact description of the evolving singular set or a proof of a branch lifetime law. Brownian paths are nowhere differentiable, and nonlinear coordinate changes can generate Ito corrections. Exact stopping and survival laws require G1 authorization and further proof.

Sign convention: x~-x in RP^3; local x1>0 chart fixes representative. A zero tangent determinant marks loss of regularity; continuation or branch death is a separate question.
