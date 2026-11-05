# M0-A/B: Explicit tensors and Brownian covariance (documentation-only)

Status: analytic draft; independent verification pending. No numerical experiments executed.

## Tensor construction
Let f(x)=T[x,x,x,x]=a*x1^4+sum_{j=2}^4 b_j*x1^2*xj^2. Fully symmetric entries: T1111=a and all six permutations of T11jj=b_j/6. At x=e1, T x^3=a e1 and lambda=a. The tangent linearization H=P(3T[x,x,.,.]-lambda I)P restricted to x-perp has diagonal entries h_j=b_j/2-a. This H equals one quarter of the Riemannian Hessian of f on the unit sphere.

With a=1, tensor A b=(2.2,4,4) gives H_A=diag(0.1,1,1); tensor B b=(2.2,2.2,4) gives H_B=diag(0.1,0.1,1). Both are realizable symmetric fourth-order tensors with the same minimum absolute tangent gap 0.1.

## Brownian normalization
Take an orthonormal Frobenius basis {F_k}_{k=1}^{35} of Sym^4(R^4), and dT_t=sigma sum_k F_k dW_t^k for independent standard Brownian motions. At e1, projected increment P(dT e1^3) has tangent coordinate j equal to (sigma/2)dW_{111j}, because the normalized symmetric basis element for index multiset (1,1,1,j) has four entries 1/2. Therefore projected covariance per unit time is sigma^2 Q with Q=I_3/4.

At a regular eigenpair, the linear response is dx=-H^{-1}P(dT x^3) at leading martingale order, with drift terms omitted. Local sign-invariant squared angular displacement rate is sigma^2 tr(H^{-1}QH^{-T}). A: sigma^2*(100+1+1)/4=25.5 sigma^2. B: sigma^2*(100+100+1)/4=50.25 sigma^2.

## Scope and caveats
- This is a local stopped-process coefficient away from det(H)=0, not a globally defined eigenvector SDE.
- The full tensor Brownian process is rotationally invariant under the stated Frobenius covariance; other covariance choices change Q.
- A and B have different curvature multiplicities, not a claim about critical universality.
- The statement is an elementary counterexample to scalar-gap determination, not a confirmed novel theorem.
- Requires independent coefficient audit, comparison with existing perturbation theory, and owner gate decision.

## Prior-art pointers (screened, not exhaustive)
- Z-eigenpair conventions and objective derivatives: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280493/
- Gaussian symmetric tensor covariance conventions: https://www.mathnet.ru/links/3a7439fcab3b40ef0727053c00fb3ef0/sigma2256.pdf
