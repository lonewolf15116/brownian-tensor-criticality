# S0 reviewer feedback triage — 2026-11-02

Status: owner-supplied reviewer analysis, not independently authenticated external reproduction. Reviewer reports inability to access solution files and an independent Round 1 reconstruction. No S0 acceptance or G1 authorization.

## Supported
R1 tensor multiplicities, tangent spectrum: PASS.
R2 local fold, transverse nondegeneracy: PASS. The reviewer's second-order branch coefficient **2/3 is correct**, not an error: let z=sqrt(-mu/3), t_±=±z+(2/3)z^2+O(z^3). Verify by substitution into mu+3t²-4t³+O(t4,mu*t²)=0.
R5 Frobenius noise coefficient: PASS.
R6 regular eigenvector IFT: PASS locally, with chart and stopping.
R7 codim-one local sheet/hitting: proof incomplete; no 35D lifetime law.

## Nuanced corrections
R3: the rational pole t=±1/sqrt(3) is outside the chosen sufficiently small local interval; it is not a defect in the local proof. Local cutoff delta is in t, not necessarily in mu. At mu=0 the local fold pair coalesces; an arbitrary chart exit is not branch death.
R4: the reflection formula in our draft was explicitly for coefficient tau0, not for t being Brownian, and the draft explicitly warned tau0 need not equal stopped-chart lifetime. The reviewer correctly emphasizes this distinction but its conditional FAIL is not evidence that our actual draft made that claim.
The reviewer's claim 'h smooth on (-infinity,0)' is too broad; only a sufficiently small negative interval is proved.
Reviewer's eigendiscriminant degree formula and literature attributions require primary-source checking before reuse.

## Revision tasks
1. Full parameter-dependent Lyapunov-Schmidt reduction in 35 tensor coordinates, with chart-specific fold parameter and branch availability.
2. Precisely define first H-singularity, fold collision, and chart exit as distinct stopping notions.
3. State stopped Ito theorem with localization away from endpoints; distinguish coefficient hitting law from killed-interval exit law.
4. Rigorous local positive-probability hitting argument for smooth discriminant sheet, with conditions on initial tensor, time horizon and branch continuation.
5. Independent verification provenance: review is user-provided and self-described independent; reviewer identity, methods and answer-file access not independently confirmed. Record as external feedback, not completed independent reproduction.

## Gate
REVISE S0; draft PR unmerged; no experiments, no G1, no novelty claim.
