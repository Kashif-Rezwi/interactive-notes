# EVAL-2026-0001: Candidate evaluation for CAN-2026-0001

**Candidate ID/version:** CAN-2026-0001 · [`linear-algebra-foundations-v2.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v2.html) · SHA-256 `7bbb8d45f093c5ab888081a3b6c0c61a7f3418f3ef64b1c5a1141db5fb540c3e`<br>
**Rubric version:** [Evaluation framework](../../docs/06-evaluation/evaluation-framework.md), provisional Stage 1 default dimensions and weights (Experimental; review by 2026-11-04)<br>
**Evaluator role/identity:** Repository maintainer, Reviewer profile (solo Stage 1 operator)<br>
**Evaluation mode:** human (assisted by scripted verification of the artifact's math and structure)<br>
**Operating scope:** Stage 1 private pilot<br>
**Review independence:** non-independent<br>
**Reviewer relationship or limitation:** The same operator performed the Creator pass (concept model, plan, specification, generation) and this Reviewer pass, as separately recorded passes under [ADR-0002](../../docs/adr/0002-stage-1-role-activation-profile.md). This is a self-review limitation, not an independent review.<br>
**Public-release eligibility:** ineligible<br>
**Confidence:** medium<br>
**Recommendation:** private-pilot-complete

## Scope and evidence inspected

- The candidate file rendered from `file://` with no network access; static inspection confirmed zero external `src`/`href` references.
- JavaScript syntax checked (`node --check`); all seven interactive widgets executed under a DOM/canvas stub and produced populated, correct readouts.
- Widget mathematics independently recomputed outside the artifact: least-squares fit of the constructed points gives slope 0.7, intercept 0.3, SSE 0.3 (artifact agrees: AᵀA = [[55, 15], [15, 5]], Aᵀb = [43, 12]); projection error satisfies e·y ≈ 0; the order demo confirms AB ≠ BA.
- Every factual statement traced to [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) atomic claims, each anchored to SRC-2026-0001 notebook cells; the two embedded source figures (cells 38, 42) appear only as transcribed formulas.
- Specification conformance checked against [XS-2026-0001](../specifications/xs-2026-0001-linear-algebra-foundations-v2.md) and plan outcome coverage against [LP-2026-0001](../plans/lp-2026-0001-linear-algebra-foundations.md).

## Dimension scorecard

| Dimension | Score (0–4) | Evidence | Defects/severity | Recommended remedy | Confidence |
| --- | ---: | --- | --- | --- | --- |
| Educational quality | 3.5 | All 7 sections follow definition → example → interactive → self-check; feedback states the governing rule; optional interview depth (LP outcomes 1–9 all exercised) | Minor: no mastery gating or spaced retrieval (not required by the plan) | Consider in a future revision hypothesis | Medium |
| Factual/mathematical accuracy | 3.5 | Formulas match source cells; widget math verified by external recomputation (see scope) | Minor: source's raw L2-norm typography is ambiguous; standard reading adopted and disclosed in CM-2026-0001 | None for the pilot; flag if the source is ever revised | High |
| Source grounding | 3.5 | Claim-to-cell traceability complete; constructed examples labeled; ML-connection table preserved; figures transcribed, not redistributed | Observation: embedded PNG figures are not viewable in the artifact (deliberate provenance-preserving choice) | None | High |
| Interactivity and agency | 3.5 | 7 widgets with immediate causal feedback, dual visual + numeric channels, and reset controls | Minor: vector entry limited to preset ranges | Widen ranges or add free entry in a revision | Medium |
| Accessibility and inclusion | 3.0 | Landmarks, skip link, aria-live text equivalents for every canvas, keyboard-operable native controls, reduced-motion and print support; color never the sole encoder | Major (for release only): no screen-reader or independent accessibility verification; contrast asserted by design intent, not measured | Independent accessibility review with tooling before any release consideration | Low |
| Visual clarity | 3.5 | Standard vector/grid encodings; labeled arrows; dashed error components; consistent section styling | None observed | — | Medium |
| User experience | 3.5 | Sticky section nav with active-section highlight; linear flow; no attempt penalties; offline use | None observed | — | Medium |
| Completeness | 3.5 | All 7 source parts, 7 interactives, 14 self-check items, status banner, provenance footer | Observation: outcome-coverage matrix lives in LP/XS, not in the artifact | Acceptable for a pilot | Medium |
| Readability | 3.5 | Plain-language restatements beside formal definitions; consistent terminology with the glossary | None observed | — | Medium |
| Technical feasibility/performance intent | 4.0 | Single 49.9 KB file, zero external requests, works from `file://`, redraws only on input | None observed | — | High |

## Weighted result and gate check

Weighted aggregate = (3.5×18 + 3.5×18 + 3.5×10 + 3.5×10 + 3.0×14 + 3.5×8 + 3.5×8 + 3.5×6 + 3.5×4 + 4.0×2) / 100 = 337 / 100 = **3.37**.

Diagnostic gate check (provisional Stage 1 gates, used diagnostically per policy):

- Hard-gate dimensions ≥ 3.5: educational quality 3.5 ✓, accuracy 3.5 ✓, source grounding 3.5 ✓, accessibility 3.0 ✗.
- Other dimensions ≥ 3: all ✓. No score of 0–1 ✓. No unassessed dimension ✓.
- Weighted ≥ 3.5: 3.37 ✗.

The candidate would not meet the numeric public-release gates even diagnostically. Independently of any score, the non-independent review makes public release prohibited; public-release eligibility is **ineligible**.

## Disagreement or uncertainty

No second evaluator exists; disagreement is unmeasurable in this pilot. Highest uncertainty is the accessibility score (self-assessed without specialist tooling) and the educational-quality score (no learner has used the artifact; no efficacy evidence exists or is claimed).

## Non-negotiable blockers

None for private-pilot closure. For any future public-release consideration: independent review, accessibility specialist verification, calibration completion, and Human Accountable Owner approval are all required and currently absent.

## Reviewer sign-off

Reviewed as a Stage 1 non-independent Reviewer pass by the repository maintainer on 2026-08-04. Recommendation: **private-pilot-complete**. This evaluation is not a release decision, not a benchmark result, and not a learning-efficacy claim.

## Appendix — Retrospective gate recomputation (2026-08-13)

Per [ADR-0007](../../docs/adr/0007-gate-arithmetic-and-record-status-hygiene.md): the evaluation-framework weights in force when this scorecard was issued summed to 98 against a stated total of 100, so the `/ 100` formula above deflated the aggregate. Corrected arithmetic under the repaired weight table (Technical feasibility/performance intent 2% → 4%): (3.5×18 + 3.5×18 + 3.5×10 + 3.5×10 + 3.0×14 + 3.5×8 + 3.5×8 + 3.5×6 + 3.5×4 + 4.0×4) / 100 = 345 / 100 = **3.45** (recorded above: 3.37).

Gate outcomes are unchanged: hard-gate dimensions — educational quality 3.5 ✓, accuracy 3.5 ✓, source grounding 3.5 ✓, accessibility 3.0 ✗; other dimensions ≥ 3 ✓; weighted ≥ 3.5: 3.45 ✗ (diagnostic only). The disposition (`private-pilot-complete`) and public-release eligibility (`ineligible`, non-independent review) are unchanged. Retrospective appendix; the evaluation's original body, including the 3.37 figure, is unchanged and remains the historical computation.
