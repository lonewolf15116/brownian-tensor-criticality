# S0 second verification — owner pre-acceptance audit (2026-11-02)

Scope: exact symbolic differentiation of restricted quartic using SymPy (not numerical simulation), independent rereading of committed documents, and source-level bibliography check. No Rust or stochastic execution; PR stays draft.

1. f_mu(t)=(1+mu*t+2*t^2+t^3)/(1+t^2)^2. Computer-algebra derivative factored to (-3*mu*t^2+mu-t^4-4*t^3+3*t^2)/(1+t^2)^3, exactly matching the recorded numerator.
2. At mu=0,e1, T1111=1, T1122=1/3; H22=3*(1/3)-1=0, H33=H44=-1. T1112=mu/4 and T1222=1/4 are consistent with polynomial multiplicities.
3. G_mu(0,0)=1, G_t(0,0)=0, G_tt(0,0)=6: local fold. With lambda near 1, eigenpair equations in x3,x4 force those coordinates zero.
4. In a Frobenius-orthonormal tensor basis, the 1112 orbit has four entries of size 1/2, yielding quartic coefficient 2*sigma*dW and bracket rate 4*sigma^2. This is exact for that linear coefficient; it is NOT an exact Brownian SDE for the nonlinear fold location in the full 35-dimensional space.
5. Checked original sources: Hu arXiv:2104.05900 reports generic tensor Z-eigenvector nondegeneracy; Bergeot, Berglund & Zogheib, Nonlinearity 39 (2026) 075004, DOI 10.1088/1361-6544/ae7ec0, treats noise on the slow variable of a slow-fast saddle-node system. Their theorem-level relationship to our stopped algebraic branch remains to be analyzed.

Audit outcome: NO algebraic discrepancy found in the explicit fold or linear noise normalization. Important wording constraint: 'independently rechecked with symbolic differentiation' does not mean independent researcher reproduction. No claim of stochastic lifetime law or original discovery. S0 dossier remains ready for owner review but unaccepted; G1 blocked.
