# BTC-004 — Real Eigenpoints of Ternary Quartics

**Research archive | Working reconstruction | 5 November 2026**

> **Gate 0 OPEN.** 19/21 reported Morse triples; 0/13 direct witnesses independently certified; 0 confirmed novel discoveries. The missing triples are (6,6,1) and (1,6,6). This repository does **not** claim a complete classification or established novelty.

## Mathematical problem

For a real homogeneous ternary quartic (h), study the Morse critical points of
[
Phi([x:y:z])=h(x,y,z)/(x^2+y^2+z^2)^2
]
on (mathbb{RP}^2). A Morse triple ((m_0,m_1,m_2)) counts minima, saddles, and maxima, satisfying (m_0-m_1+m_2=1). The projective eigenpoint equations are (xh_y-yh_x=xh_z-zh_x=yh_z-zh_y=0). A zero-dimensional ternary-quartic eigenscheme has length 13 by the determinantal degree formula; this does not automatically imply 13 distinct real eigenpoints.

## Research state

- **Working inventory:** 19/21 candidate realizations, including 13 direct, two Maccioni-derived, and four scaling-derived triples.
- **Unresolved:** (6,6,1); its negation yields (1,6,6).
- **Closest direct certificate:** (h=x^4+y^4-z^4-18x^2y^2+12xyz^2), reported triple (2,5,4); six nonzero real fibre lifts and transverse infinity/Hessian checks remain.
- **Track A:** follow the complex conjugate eigenpoint pair from a known (5,5,1) anchor into a possible (6,6,1) chamber; no landing has been established.
- **Novelty:** even-family rigidity is flagged as potentially subsumed by earlier ESS/replicator-dynamics literature; primary-source verification outstanding.

## Archive policy

Frozen proofs and manuscript versions are historical artifacts, **not** to be silently rewritten. Audit corrections and subsequent results belong in versioned ledgers and separate files. Do not label a reported numerical computation as an independently reproducible certificate without the corresponding executable artifact and rerun.

See [Master Evidence Ledger v1.0](docs/BTC-004_Master_Evidence_Ledger_v1.0.md) for witnesses, evidence tiers, correction log, open tasks, and gate criteria.

## Reproducibility and limitations

The original frozen documents, manuscripts, PDFs, audit scripts, and reviewer dossiers may reside outside this initial GitHub branch and must be uploaded byte-for-byte with hashes before this is described as a complete archive. No new discovery, independent certification, or repository-wide reproducibility is claimed.

## Status

**Private working research. External review deferred by owner until final stage.**
