# EVAL-2026-0002: Candidate evaluation for CAN-2026-0003 (v4)

**Candidate ID/version:** CAN-2026-0003 · [`linear-algebra-foundations-v4.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v4.html) · SHA-256 `22b4047e7834ce233ff5088ff3d2e603242b8932e321f62004b823d076f445d6`
**Rubric version:** [Evaluation framework](../../docs/06-evaluation/evaluation-framework.md), provisional Stage 1 default dimensions and weights (Experimental; review by 2026-11-04)
**Evaluator role/identity:** Repository maintainer, Reviewer profile (solo Stage 1 operator)
**Evaluation mode:** human, assisted by scripted verification of the artifact's mathematics and structure, and by three isolated per-variant audit passes whose findings fed the redesign
**Operating scope:** Stage 1 private pilot
**Review independence:** non-independent
**Reviewer relationship or limitation:** The same operator performed the Creator pass (plan, specification, generation) and this Reviewer pass under [ADR-0002](../../docs/adr/0002-stage-1-role-activation-profile.md). Self-review limitation, not independent review.
**Public-release eligibility:** ineligible
**Confidence:** medium
**Recommendation:** private-pilot-complete

## Scope and evidence inspected

- The candidate rendered from `file://` with no network access; scripted scans confirmed zero external `src`/`href`/`@import` (the sole `url(#arr)` is an internal SVG marker).
- JavaScript syntax checked (`node --check`); the full script executed under a DOM/canvas stub: all 12 widgets initialize, all default readouts contain independently recomputed values, glossary renders 32 entries, no NaN/undefined in any readout.
- 44 scripted recomputations of every numeric claim, widget default, and answer key (RUN-20260810-0001 §Verification evidence) — all PASS.
- Comparative audits of v1/v2/v3 (three isolated evaluator passes, one rubric, one source map) are the basis for the redesign; their findings and dispositions are summarized in the run reflection and in the owner's brief response.
- Every factual statement traced to [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) claims or to blocks labeled Foundation/Supplemental; constructed examples are labeled.
- Specification conformance checked against [XS-2026-0002](../specifications/xs-2026-0002-linear-algebra-foundations-v4.md); outcome coverage against [LP-2026-0002](../plans/lp-2026-0002-linear-algebra-foundations.md).

## Source-defect disposition (mathematical audit)

| Source/variant defect | v4 disposition |
| --- | --- |
| "Scaler" typo (cell 2) | Corrected |
| Garbled L2 typography (cell 32) | Corrected to √(Σ xᵢ²) with a true vinculum; correction flagged in-text |
| Projection/decomposition formulas as opaque images (cells 38, 42) | Transcribed as annotated formulas + interactive; images not redistributed |
| Linearity proof taught before the dot product (cell 19 vs cell 30) | Re-sequenced to Unit 5, labeled "re-sequenced" |
| xᵀ and wᵀx used before transpose/dot product exist | Transpose taught as a Unit 2 tool; linear model first taught as weighted sum; wᵀx revealed in Unit 5 |
| (AᵀA)⁻¹ with undefined inverse and unstated condition | Foundation bridge box; condition (full column rank) forward-linked and closed in Unit 8 |
| Eigenvectors named but untaught (cell 63) | One-line extension note; matching row labeled Extension |
| v2: determinant used undefined | Avoided: 2D area test, determinant named only in passing |
| v2: outlier renders off-canvas | Repaired: slider-bounded points + data-space window covers y ≤ 10 |
| v3: interview Q2 rotate/shear results swapped | Repaired by construction: AB/BA computed live, never hard-coded |
| v3: aria-live chatter on every slider tick | Repaired: readouts are not live regions; equivalent text via aria-describedby |
| v1: wrong ellipsis in column vector; dropped dimension concept; no offline/mobile/a11y | Repaired: ⋮ notation avoided entirely in favor of explicit components; dimension taught in Unit 3; zero-dep single file, native controls, full keyboard path |

## Pedagogical audit (LP-2026-0002 checklist)

- **Beginner test:** every nontrivial term is either taught before use, bridged at point of need (cos θ, transpose, inverse), or excluded (determinant). PASS by construction; not yet verified with a real beginner.
- **Dependency test:** no concept is used before explanation; the one source violation is repaired and flagged. PASS.
- **Cognitive-load test:** one idea per block; formulas carry symbol keys; optional depth collapsed (proof, extensions). PASS by inspection.
- **Interaction test (ICAP):** every unit requires production — a prediction, a computation, or an explanation — not only consumption. PASS.
- **Practice test:** 4 faded ladders; checks include 12 numeric blanks and 3 explain-in-words; mastery adds reasoning/transfer/error-identification. PASS.
- **Transfer test:** mastery items 5 (embedding search) and 10 (collapse matrix) are new situations, not repeated examples. PASS.
- **ML-relevance test:** every unit closes with a specific ML mechanism (not "used in ML"); the Unit 9 table is the source's own mapping with a "where you saw it" column. PASS.
- **Completeness test:** all seven source parts covered; the full coverage matrix ships with the owner's deliverable summary. PASS.

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality | 3.5 | Unit loop with prediction gates, 4 faded ladders, mixed constructed-response checks, interleaved mastery with confidence calibration; LP outcomes 1–11 all exercised | Minor: no learner has used it; no efficacy evidence exists or is claimed | Learner pilot in a future stage | Medium |
| Factual/mathematical accuracy | 4.0 | 44 recomputations PASS; widget math computed live (never hard-coded), eliminating the v3 contradiction class | None observed | — | High |
| Source grounding | 3.5 | Claim-level traceability; layer/provenance tags separate class content from additions everywhere | Observation: reordering deviates from lecture order by design; each deviation is labeled in-artifact and justified in LP-2026-0002 | — | High |
| Interactivity and agency | 4.0 | 12 widgets, 3 prediction gates, goal-directed tasks, edge-state pedagogy, degenerate-state guards | Minor: sliders discretized at 0.5 steps | Widen if learners request free entry | Medium |
| Accessibility and inclusion | 3.0 | Landmarks, skip link, keyboard-operable native controls, canvas text equivalents, no color-only encoding, reduced-motion, print notes; slider-chatter repair | Major (for release only): no screen-reader or independent accessibility verification; contrast asserted by design intent, not measured | Independent accessibility review before any release consideration | Low |
| Visual clarity | 3.5 | Standard encodings; labeled arrows; dashed leftovers; area squares; calm single-accent system | None observed | — | Medium |
| User experience | 3.5 | Sticky nav with progress dots tied to cleared checks; predictable unit structure; offline use; honest status banner | Minor: 172.7 KB is heavier than v2; still trivial for local use | — | Medium |
| Completeness | 3.5 | All 7 source parts + glossary + concept map + mastery check + review list | None observed | — | Medium |
| Readability | 3.5 | Plain language precedes formalism; every symbol named; consistent terminology with the glossary | None observed | — | Medium |
| Technical feasibility/performance intent | 4.0 | Single file, zero requests, input-driven redraws, DPR-crisp canvases, graceful localStorage degradation | None observed | — | High |

## Weighted result and gate check

Weighted aggregate = (3.5×18 + 4.0×18 + 3.5×10 + 4.0×10 + 3.0×14 + 3.5×8 + 3.5×8 + 3.5×6 + 3.5×4 + 4.0×2) / 100 = 351 / 100 = **3.51**.

Diagnostic gate check (provisional Stage 1 gates, used diagnostically per policy):

- Hard-gate dimensions ≥ 3.5: educational quality 3.5 ✓, accuracy 4.0 ✓, source grounding 3.5 ✓, accessibility 3.0 ✗.
- Other dimensions ≥ 3: all ✓. No score of 0–1 ✓. No unassessed dimension ✓.
- Weighted ≥ 3.5: 3.51 ✓ (diagnostic only).

Independently of any score, the non-independent review makes public release prohibited; public-release eligibility is **ineligible**.

## Disagreement or uncertainty

No second evaluator exists; disagreement is unmeasurable. Highest uncertainty remains accessibility (self-assessed without specialist tooling) and educational quality (no learner evidence; the redesign's assessment-layer hypothesis — retrieval over recognition — is evidence-based from the literature but untested on the target learner).

## Non-negotiable blockers

None for private-pilot closure. For any future public-release consideration: independent review, accessibility specialist verification, calibration completion, and Human Accountable Owner approval are all required and currently absent.

## Revision 1 — post-evaluation adversarial audit (2026-08-10, same cycle, pre-closure)

An owner-requested audit re-examined the candidate after the initial scorecard above. Method: scripted structural audit (answer-key integrity, ARIA/ID/reference wiring), two isolated adversarial sub-audits (content/mathematics; pedagogy, each with full recomputation), and an operator technical audit (WCAG contrast measurement; handler-level runtime simulation under an instrumented DOM stub — 21/21 behaviors verified, including gate commitment semantics, weak-topic record/clear, and confident-numeric-miss routing).

**Findings:** 0 blockers; 3 majors (Unit-6 matrix-product dependency breach; confidence logic covering radios only; angle-arc quadrant bug); 11 minors/nits — all repaired and regression-checked in [RUN-20260810-0001](../runs/run-20260810-0001-linear-algebra-foundations-v4.md) §Revision 1, including the full defect/root-cause/disposition table.

**Post-revision artifact identity:** SHA-256 `b35c622e8d14b15de50f7c077e157d26e2dc8243410c3d21a40b9559d6851590`, 178,020 bytes. (The header of this record names the pre-audit build `22b4047e…f445d6`; both hashes are preserved for provenance. The scorecard above was issued against the pre-revision build; the revision strictly improves the assessed properties.)

**Score movement:** none claimed. Educational quality remains 3.5 (the repair closes a dependency breach and a dead-UI defect — these were defects against the spec, and the scores already reflected the design intent; no learner evidence exists either way). Accessibility remains 3.0, though one evidence upgrade is recorded: contrast is now **measured**, not asserted — all 12 text/background pairs compute to ≥ 4.5:1 (WCAG AA normal text); the remaining gap is the absence of independent screen-reader verification, unchanged. Public-release eligibility remains **ineligible** (non-independent review).

**Audit-process note for future cycles:** the two highest-severity findings (R1, R2) were invisible to the standing verification suite and surfaced only through (a) a read-in-order dependency audit and (b) handler-level behavioral simulation. Both are proposed as standing gates in the run reflection.

## Reviewer sign-off

Reviewed as a Stage 1 non-independent Reviewer pass by the repository maintainer on 2026-08-10. Recommendation: **private-pilot-complete**. This evaluation is not a release decision, not a benchmark result, and not a learning-efficacy claim.

## Appendix — Retrospective iteration accounting (2026-08-11)

Per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md): **Iterations reviewed = 2 builds / 1 revision cycle** — build 1 `22b4047e…f445d6` (scorecard above), revision cycle 1 → build 2 `b35c622e…1590` (Revision 1 section above). Retrospective appendix; the evaluation's original body is unchanged.

## Appendix B — Retrospective gate recomputation (2026-08-13)

Per [ADR-0007](../../docs/adr/0007-gate-arithmetic-and-record-status-hygiene.md): the evaluation-framework weights in force when this scorecard was issued summed to 98 against a stated total of 100, so the `/ 100` formula above deflated the aggregate. Corrected arithmetic under the repaired weight table (Technical feasibility/performance intent 2% → 4%): (3.5×18 + 4.0×18 + 3.5×10 + 4.0×10 + 3.0×14 + 3.5×8 + 3.5×8 + 3.5×6 + 3.5×4 + 4.0×4) / 100 = 359 / 100 = **3.59** (recorded above: 3.51).

Gate outcomes are unchanged: hard-gate dimensions — educational quality 3.5 ✓, accuracy 4.0 ✓, source grounding 3.5 ✓, accessibility 3.0 ✗; other dimensions ≥ 3 ✓; weighted ≥ 3.5: 3.59 ✓ (diagnostic only). The Revision 1 score-movement statement, the disposition (`private-pilot-complete`), and public-release eligibility (`ineligible`, non-independent review) are unchanged. Retrospective appendix; the evaluation's original body, including the 3.51 figure, is unchanged and remains the historical computation.

## Appendix C — Coverage matrix (retrospective, 2026-08-13)

Lesson standard §3 and QA-checklist Audit 1 require the coverage matrix to ship with the evaluation record; the pedagogical-audit section above references it as shipping with the owner's deliverable summary, which is outside this repository. This appendix reconstructs and preserves it from [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) claim anchors and the [XS-2026-0002](../specifications/xs-2026-0002-linear-algebra-foundations-v4.md) content-and-evidence map, and is now the matrix's canonical location. Dispositions follow standard §3 (included-as-taught / included-expanded / transcribed-from-opaque-format / added-foundation / added-extension / excluded-with-reason). No source item was dropped silently.

| Source item (SRC-2026-0001 cells) | v4 location | Disposition |
| --- | --- | --- |
| Agenda and course framing (cell 2, incl. "Scaler" typo) | Unit 1 | Included-as-taught; typo corrected and flagged in-body |
| Scalars, vectors, matrices (cells 3–10) | Unit 1 | Included-as-taught; expanded with the data/arrow dual view of vectors (Foundation) |
| Functions in ML, f: Rⁿ → R (cell 12) | Unit 2 | Included-as-taught |
| Linear model wᵀx + b (cell 13) | Units 2 & 5 | Included-expanded: taught first as a weighted sum (Unit 2); the wᵀx reveal lands after the dot product (Unit 5), per the dependency rule |
| Summation notation (cell 15) | Unit 2 | Included-expanded: summation expander widget; for-loop analogy for code-fluent learners |
| Important notation xᵀ, ‖x‖, Rⁿ (cell 17) | Unit 2 | Included-expanded: transpose pre-taught as a tool so later uses are legal (Foundation) |
| Dot-product linearity proof / interview skill (cell 19) | Unit 5 | Re-sequenced after the dot product (source ordering defect repaired and labeled); collapsed optional depth |
| Vector space, linear combination, span, basis, dimension (cells 20–28) | Unit 3 | Included-as-taught; prediction gate on span collapse; misconception distractors on basis |
| Dot product, orthogonality (cells 29–34 excl. 32) | Unit 5 | Included-expanded: cos θ bridge (Foundation); sign/magnitude-confound misconception handling |
| Norms L1/L2 (cell 32; garbled L2 typography in source) | Unit 4 | Included-as-taught; typography corrected to √(Σ xᵢ²) with a true vinculum, correction flagged in-text |
| Projection, orthogonal decomposition, least squares (cells 35–45; opaque figures in cells 38, 42) | Unit 6 | Transcribed-from-opaque-format (figures not redistributed); (AᵀA)⁻¹ Foundation bridge; invertibility condition forward-linked to Unit 8 |
| Matrix multiplication, matrix-vector product, identity, transpose, symmetric (cells 46–56) | Unit 7 | Included-as-taught; AB ≠ BA computed live, never hard-coded |
| Linear independence, rank (cells 57–61) | Unit 8 | Included-expanded: 2D area test with the determinant named only in passing; multicollinearity mechanism link closes the Unit 6 loop |
| ML connections table incl. eigenvector mention (cells 62–63) | Unit 9 | Included-as-taught with a "where you saw it" column; eigenvectors receive a one-line EXTENSION |
| Determinant procedures, eigendecomposition, SVD, gradient calculus, numerical methods (absent from source) | — | Excluded-with-reason: not taught by the source and beyond the declared learner (CM-2026-0001 scope boundary) |
| Lesson additions with no source anchor: concept map, glossary, faded ladders, prediction gates, mastery check, review list | Units 0–9 | Added-foundation / added-extension; every block carries a layer badge and provenance tag |
