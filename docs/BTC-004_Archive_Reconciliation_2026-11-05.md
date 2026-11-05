# BTC-004 Archive Reconciliation Note v1.0

Date: 2026-11-05
Status: Additive archival note; not independent mathematical certification or novelty clearance.

## Preservation
This note does not alter frozen proof v1.0, manuscripts, historic logs, audit reports, scripts, or the original checksum manifest. Dated documents retain their historical state.

## Ledger reconciliation
The 8/21 realized and 13 unresolved statements in November 3–4 documents are historical snapshots. The November 5 working inventory is **19/21**, comprising 13 previously supported direct entries, two Maccioni-derived entries (1,4,4) and (4,4,1), and four scaling-derived entries (5,6,2), (2,6,5), (5,5,1), (1,5,5). The missing triples remain (6,6,1) and (1,6,6). These are **working realizations, not 19 independently certified witnesses**. Under the strict audit standard, 0/13 direct witnesses are fully independently certified. Gate 0 OPEN; zero confirmed novel discoveries.

## Euler objection
The referee's claim that the indefinite-case exclusion merely invokes Euler vaguely does not apply to frozen proof v1.0 section 3(c). Its exact text states:

> All three edge curvatures cannot be positive. That would give six edge minima, four interior saddles and three axis maxima, contradicting the Morse Euler relation \(m_0-m_1+m_2=\chi(\mathbb{RP}^2)=1\), since \(6-4+3=5\). All three cannot be negative either, by the same argument (three axis minima, four saddles, six edge maxima). Consequently the edge-curvature signs are mixed.

This rebuts that specific criticism, not every other referee concern. A future separately versioned manuscript can reorder the paragraph for clarity.

## v0.1 formula (5) erratum
The v0.1 expression has incorrect mixed terms aw+bw+cw. The intended expression is
\[Q(u,v,w)=d_1u^2+d_2v^2+d_3w^2+auv+buw+cvw.\]
The v0.2/v0.3 TeX sources were reported to have the corrected formula. The source v0.1 remains unmodified. The reported loss of the v in cvw in extracted v0.2/v0.3 PDF text and repeated 1 characters on page 2 require visual PDF verification before external distribution; these are not yet established rendering defects.

## Scaling v3 provenance
The uploaded v3 audit report cites source BTC004_Scaling_Proof_v3.md and SHA-256 8c051b53bcabc3b6f911d4c1018c545d47d7a00eb029f2017ce22073a3cf0450. Neither the uploaded file list nor the original SHA256SUMS.txt contains this named source. Existing scaling_proof_note and scaling_proof_note_v2 files have different recorded hashes. **Do not substitute them for the cited source without byte-level verification.** Recover and hash the actual v3 proof, then add a supplemental manifest or issue a dated citation correction.

Preserve the audit distinction: PASS 1–5 are executable algebraic checks; REVIEW 6–7 are analytic review, not executable certification. Missing source provenance does not by itself refute the algebraic checks.

## Integrity and follow-up
GitHub lists byte-identical blob pairs for frozen v1.0, v0.1 PDF, and reviewer dossier. This is Git blob identity, not independent SHA-256 verification. The original SHA256SUMS manifest records frozen v1.0 SHA-256 7e90d980a3b574d0a91d0dc7328138ac5af50ed85c4d1abd1bfdb6b7dad2d20f, but all archived files have not been freshly checked against their SHA-256 entries here.

| Task | Status |
|---|---|
| Reconcile 8/21 historical versus 19/21 working | Documented |
| Quote frozen Euler argument | Documented |
| Record v0.1 formula correction | Documented |
| Inspect rendered PDFs | OPEN |
| Recover/hash-match v3 proof source | OPEN |
| Verify full SHA-256 manifest | OPEN |
| Independent witness certification and novelty assessment | OPEN |

**Research status unchanged:** 19/21 working; 0/13 direct fully independently certified; Gate 0 OPEN; zero confirmed novel discoveries.
