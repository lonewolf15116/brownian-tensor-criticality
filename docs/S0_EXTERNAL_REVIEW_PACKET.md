# S0 External Mathematical Review Packet — Brownian Tensor Criticality

**Status:** Owner-requested sharing preparation. Draft PR #1 unmerged. S0 not accepted. No numerical experiments, no G1 authorization, no confirmed original discovery.

## Review sequence
**Round 1 (blind to our solutions):** Read only sections 'Definitions' and 'Independent tasks' below. Produce independent calculations and a signed/attributed report. **Round 2:** Open the linked solution files and perform adversarial review. Reviewer should distinguish their own derivation from checking ours. Public GitHub history means blindness cannot be guaranteed.

## Definitions (Round 1)
- Symmetric order-four tensors T in Sym^4(R^4), quartic f_T(x)=T[x,x,x,x] on S^3, x~ -x.
- Z-eigenpairs satisfy T x^3=lambda x, ||x||=1, lambda=f_T(x).
- Tangent P=I-xx^T; H=P(3T[x,x,.,.]-lambda I)P restricted to x-perp.
- Test family f_mu=x1^4+mu*x1^3*x2+2*x1^2*x2^2+x1*x2^3.
- Tensor Brownian model dT=sigma sum_{a=1}^{35} E_a dW_a, with Frobenius-orthonormal basis and independent standard Brownian coordinates.

## Independent tasks (Round 1)
R1. Reconstruct nonzero tensor entries and multiplicities; verify Z-eigenpair at mu=0,x=e1 and H spectrum.
R2. In t=x2/x1 chart, derive exact stationary equation and prove or refute a generic fold. Check other tangent directions and projective sign.
R3. Determine correct local inverse branches, domains, and stopping times. Distinguish exit at fold from exit at artificial chart boundary.
R4. Derive the stopped Ito equation for t_s when mu_s=mu0+2sigma W_s. Check coefficients, smoothness, endpoint behavior, and hitting-time distributions; determine whether the one-sided reflection formula is a branch lifetime law.
R5. Verify Frobenius basis normalization and the variance rate of the x1^3*x2 coefficient. Distinguish exact linear coefficient noise from nonlinear fold coordinate noise.
R6. Prove or refute smooth local eigenvector selection for a regular eigenpair in the full 35D model; derive its Ito equation and specify tensor-space stopping conditions.
R7. Assess whether the explicit fold extends to a codimension-one local discriminant sheet in full tensor space; assess a positive-probability Brownian hitting argument. Identify missing hypotheses or proof gaps, particularly whether a branch remains available up to crossing.
R8. Search prior literature for theorems subsuming the claimed mathematics; report precise theorem/page/DOI and whether any novelty remains.

## Solution and evidence files (Round 2 only)
- [Initial fold candidate](../math/S0_EXPLICIT_FOLD_CANDIDATE.md)
- [First analytic audit](../math/S0_FOLD_ANALYTIC_AUDIT.md)
- [Brownian fold projection](../math/S0_BROWNIAN_FOLD_PROJECTION.md)
- [Second verification](../math/S0_SECOND_VERIFICATION.md)
- [Restricted stochastic theorem draft](../math/S0_RESTRICTED_STOCHASTIC_FOLD_THEOREM_DRAFT.md)
- [Stopping and 35D scrutiny](../math/S0_STOPPING_TIME_AND_FULL_TENSOR_SCRUTINY.md)
- [Final proof-obligation audit](../math/S0_FINAL_PROOF_OBLIGATION_AUDIT.md)
- [Working singularity taxonomy](../math/S0_SINGULARITY_CLASSIFICATION.md)
- [S0 exit dossier](S0_EXIT_DOSSIER.md)
- [Literature register](LITERATURE_REGISTER.md)
- [Claims ledger](CLAIMS_LEDGER.md)
- [Decision log](DECISION_LOG.md)

## Critical warnings
1. No exact 35-dimensional first-singularity or branch-death distribution has been proved.
2. The one-dimensional coefficient hitting-zero CDF is not the lifetime CDF for a branch stopped at a chart boundary.
3. Exiting an arbitrary chart does not imply singularity or branch termination.
4. Local singular-sheet existence and full 35D positive-probability hitting have proof sketches; request full parameter-dependent Lyapunov-Schmidt and support-theorem details.
5. The reviewer should challenge references and novelty claims; this is not a published theorem or externally reproduced result.

## Report template
Reviewer identifier, date, relevant expertise, independence/conflicts, methods used; table R1–R8 with PASS/FAIL/INDETERMINATE and exact calculations/citations; major errors; minor errors; missing assumptions; literature overlaps; final recommendation (accept S0 / revise S0 / insufficient evidence). Explicitly state whether calculations were derived without seeing the solution files. Review does not itself authorize experiments or G1.
