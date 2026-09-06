# EVAL-2026-0012: Matrix decompositions and applications v2 (from-scratch rebuild)

**Candidate ID/version:** CAN-2026-0011, [matrix-decompositions-applications-v2.html](../../content/aiml-4/module-02-math-statistics-for-ml/generated/matrix-decompositions-applications-v2.html), SHA-256 `6c7e50951ce318c97272e7788439a2e7cce6c2b774f99df640786ef8ce28ae01`, 136,143 bytes  
**Rubric version:** Stage 1 evaluation framework (operational anchors, WF-007) + lesson standard §10.6–10.8  
**Evaluator role/identity:** Repository maintainer, Reviewer profile  
**Evaluation mode:** script-assisted, browser-assisted, non-independent  
**Operating scope:** Stage 1 private pilot  
**Review independence:** non-independent  
**Reviewer relationship or limitation:** same operator generated and evaluated; no screen-reader specialist pass; no second evaluator  
**Public-release eligibility:** ineligible  
**Confidence:** medium  
**Recommendation:** private-pilot-complete  
**Iterations reviewed:** builds = 1 (final hash above); revision cycles = 0; in-generation corrections = 2 (both re-verified, see RUN-20260906-0002)

## Scope and evidence inspected

Source notebook (40 markdown cells, SHA re-verified), CM-2026-0009 / LP-2026-0010 / XS-2026-0010, the candidate HTML, `verify-candidate.py` strict output (0 failures), Node math-core harness output (21/21 vs independent Python), live browser session evidence (console, 320/640/1024px screenshots, interaction and adversarial traces), and the run ledger.

### Coverage matrix (all 40 source cells)

| Cells | Source content | Disposition | Lesson location |
|---|---|---|---|
| 1–2 | Title, agenda | transcribed → orientation | U0 (loop, labels, concept map) |
| 3–5 | Eigenvectors/eigenvalues, Av=λv | included-expanded | U1 Learn + EQ-001 |
| 6 | diag(2,3) example; ML intuition (PCA, spectral, dynamics, covariance) | included-expanded | U1 worked example; Connect |
| 7–8 | Geometric interpretation; invariant subspaces; expansion rates | included-expanded | U1 geometric reading |
| 9–10 | Spectrum; spectral naming; characteristic equation (duplicated line = artifact) | included-expanded; duplication dispositioned | U1 spectrum + EQ-002 |
| 11–12 | Diagonalization A=PDP⁻¹; why useful; A¹⁰⁰ | included-expanded + constructed example | U2 + EQ-003/004 |
| 13–14 | Matrix powers via Dⁿ | included-expanded | U2 + W2 + L2 |
| 15 | Diagonalizability condition (multiplicity phrasing bridged) | included-expanded + EXTENSION panel | U2 |
| 16 | ML insight (transformations, covariance, stability, NN dynamics) | included | U2 Connect |
| 17–19 | SVD works for all matrices; A=UΣVᵀ | included-expanded | U3 + EQ-005 |
| 20 | Three-stage geometric interpretation | included-expanded (live canvas) | U3 + W3 |
| 21 | Singular value meaning; "likely noise" softened; four powers of SVD | included-expanded (softened per CM) | U3; U5 measurement |
| 22 | σ=√λ(AᵀA) (typo dispositioned); AI/ML + CV + NLP + recommender + LLM applications | included-expanded | U3 + EQ-006 + L3 |
| 23–24 | ML applications table | included (mechanism-anchored, bridged) | U3 Connect table |
| 25 | PCA goal | included-expanded | U4 Learn |
| 26 | Covariance (1/n)XᵀX | included-expanded | U4 + EQ-007 |
| 27 | PCA computes covariance eigenvectors; PCA=SVD on centered data | included-expanded (payoff section) | U4 + EQ-008 |
| 28–29 | Core PCA insight; ordering | included | U4 |
| 30 | PCA workflow (5 steps) | included | U4 workflow |
| 31 | PCA applications (CV/NLP/finance/bioinformatics) | included (bridged) | U4 Connect |
| 32 | MOST IMPORTANT CONNECTION (PCA=SVD) | included-expanded | U4 payoff + synthesis |
| 33–34 | Low-rank approximation; why powerful; error claim | included-expanded + constructed matrix | U5 + EQ-009/010/011 + W5 |
| 35–36 | Real-world applications; R≈UVᵀ ("4R" typo corrected, tagged); image compression; NLP/LoRA | included-expanded | U5 Connect |
| 37–38 | Deep ML insight; low-rank/latent reliance | included | U5 DEEP DIVE |
| 39–40 | Latent spaces; deepest idea | included-expanded | U5 latent close + synthesis |
## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
|---|---:|---|---|---|---|
| Educational quality | 3.5 | Orientation unit; 5-unit anatomy; 3 gates; 5 ladders; 2 explain items; 7-item confidence-calibrated mastery with routing; reveal arcs paid off | None material | — | medium |
| Factual/mathematical accuracy | 3.5 | Node/Python cross-check 21/21 at 1e-6; every readout computed live; "likely noise" and typo dispositions | None observed | — | medium-high |
| Source grounding | 3.5 | 40/40 cells dispositioned (matrix above); constructed additions tagged | None | — | medium |
| Interactivity and agency | 3.5 | 7 sliders across 5 widgets (4 canvas), goal strips, live readouts, commitment-gated unlock, self-verifying invariants | None material | — | medium-high |
| Accessibility and inclusion | 3.5 | Native controls, aria-live, canvas text equivalents + legends, 16.5px at all widths, reduced-motion, print CSS, focus-visible | No screen-reader specialist pass | Specialist review before any public release | medium |
| Visual clarity | 3.5 | Pinned tokens, frosted nav + dots, labeled canvases, σ bar chart, live-rendered evidence at 3 breakpoints | None post-fix | — | medium |
| User experience | 3.5 | Orientation, map + revisit, persistent dots/review list with spacing invitation and reset, storage fallback note | None material | — | medium |
| Completeness | 3.5 | All v1 gaps closed (numeric SVD, persistence, confidence calibration); glossary 34×6 fields; formula manifest 11/11 | None | — | medium |
| Readability | 3.5 | Short blocks; per-symbol keys; direct definitions; mechanism-before-application | None material | — | medium-high |
| Technical feasibility/performance intent | 3.5 | 136KB single file; 0 external requests; 4/4 resize listeners; strict verifier clean; 320px overflow found and fixed in-generation | None post-fix | — | medium |

## Weighted result and gate check

Weighted score: **3.50 / 4.00** (all dimensions 3.5 under the Stage 1 default weights summing to 100). All hard-gate dimensions ≥ 3.5; no score 0–1; no unresolved critical defect; complete lineage. Gate satisfied for **private-pilot-complete**. Public release is ineligible: review is non-independent, no specialist accessibility pass, and Stage 1 policy conditions (calibration review, Human Accountable Owner approval) are not met.

## Disagreement or uncertainty

Judgment-based qualities (lede aptness, signature-visual aesthetics, density balance) were assessed by a single non-independent evaluator; those axes are provisional. Both in-generation corrections were caught before evaluation and re-verified.

## Non-negotiable blockers

None for private-pilot scope. The candidate must not be described as a public release, benchmark result, or efficacy claim.

## Reviewer sign-off

Disposition: **private-pilot-complete** — supersedes CAN-2026-0010 (v1, EVAL-2026-0011 weighted 3.45) as the Class 2 reference candidate. Future work: independent review and a screen-reader specialist pass before any public release; run one more governed lesson to confirm the reveal-arc durability observation before memory promotion.
