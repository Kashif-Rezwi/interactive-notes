# Reusable Evaluation Framework

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Validation and promotion trigger:** Recorded calibration review after three completed private pilots, plus the review evidence required by the review policy.

## Evaluation principles

- Judge the learner-facing result, not just whether a model complied with a prompt.
- Require evidence for every score, especially a high score.
- Combine automated checks, specialist review, and human judgment according to risk.
- Separate source fidelity from pedagogical effectiveness; both matter.
- Report uncertainty and evaluator disagreement instead of manufacturing precision.
- Score verified artifact evidence, not review independence. Independence is captured by the controlled review-independence field and enforced through the release conditions; deducting it inside a dimension score double-counts the limitation and makes dimension trends across pilots unreadable.

## Four-point rubric

| Score | Meaning |
| --- | --- |
| 4 — exemplary | Meets the intent with clear evidence; no material defect; transferable pattern worth reusing. |
| 3 — release-ready | Meets the minimum with minor, non-blocking improvements identified. |
| 2 — incomplete | Partially meets intent; material revision is needed before release. |
| 1 — deficient | Fails the dimension or introduces material learner/operational risk. |
| 0 — unsafe/unusable | Cannot be responsibly used or evaluated; blocks release. |

Each dimension uses only 0.5-point increments from 0 through 4. The level labels describe the whole-number anchors; a half point represents evidenced performance between adjacent anchors. Do not round dimension scores.

## Default dimensions

The weights below are **provisional Stage 1 defaults**. They are a decision aid for manual pilots, not empirical claims or permission to relax policy controls.

| Dimension | What is evaluated | Default weight | Hard gate? |
| --- | --- | ---: | --- |
| Educational quality | Outcome alignment, explanation, scaffolding, feedback, transfer | 18% | Yes |
| Factual/mathematical accuracy | Claims, calculations, definitions, assumptions, citations | 18% | Yes |
| Source grounding | Coverage, traceable evidence, correct attribution, uncertainty | 10% | Yes |
| Interactivity and agency | Meaningful learner action, causal feedback, recovery | 10% | No |
| Accessibility and inclusion | Equivalent paths, alternatives, readability, cognitive support | 14% | Yes |
| Visual clarity | Accurate encodings, hierarchy, labels, representation choice | 8% | No |
| User experience | Orientation, flow, feedback, error prevention, learner control | 8% | No |
| Completeness | Required content, interactions, assessments, metadata, edge cases | 6% | No |
| Readability | Audience fit, precision, terminology, scanability | 4% | No |
| Technical feasibility/performance intent | Reasonable complexity, graceful degradation, responsiveness plan | 4% | No |
| **Total** |  | **100%** |  |

**Weight-integrity rule:** the dimension weights must always sum to exactly 100; a weight edit that breaks the sum is a defect in the gate definition, not a stylistic choice ([ADR-0007](../adr/0007-gate-arithmetic-and-record-status-hygiene.md)).

Domains may add dimensions—for example, ML relevance/reproducibility for machine-learning lessons—but must document weights, calibration, and backward-comparison impact in a benchmark charter.

### Stage 1 dimension anchors (diagnostic)

The whole-point rubric anchors are generic by design, which let two materially different candidates score identically (CAN-2026-0003 and CAN-2026-0004 both weighted 3.59; MEM-2026-0004). For lesson candidates, score against the reference implementation's verified traits so that teaching depth — not just compliance — moves the score. CAN-2026-0003 (`linear-algebra-foundations-v4.html`) is the calibration exemplar; CAN-2026-0004 (v5) is the compliant-minimum contrast.

| Dimension | 3 (release-ready) looks like | 4 (exemplary) also has |
| --- | --- | --- |
| Educational quality | Full unit anatomy; constructed response per unit; misconception-keyed distractors | A worked numeric example before every widget; visible misconception-alert callouts; explain-in-own-words items; reveal arcs that pay off where promised |
| Interactivity and agency | Every unit offers goal-directed manipulation | Every explorer manipulates a learner variable (no demo badged as Explore); gates hide the manipulable and differentiate feedback by choice; a signature visual anchors each central concept |
| Visual clarity | Standard tokens, hierarchy, correct encodings | Color legends on multi-entity canvases; true fraction/radical markup; per-symbol key lines; bounded or autoscaling canvases (nothing renders off-canvas) |
| Completeness | All §1.1 elements present | Glossary covers every used term in six fields; concept map is a branched dependency graph; mastery sized at ≈ units + 2 |

These anchors are diagnostic guidance for Stage 1 scoring consistency only; they change no weight, gate, or eligibility rule.

## Provisional Stage 1 gate rules

This is the sole authoritative numeric release-gate definition. Calculate the weighted score as `sum(dimension score × dimension weight) / sum(dimension weights)` — the weights are required to sum to exactly 100, so this equals division by 100 today and remains correct if weights are ever redistributed ([ADR-0007](../adr/0007-gate-arithmetic-and-record-status-hygiene.md)); compare the unrounded result to the gate and display it to two decimal places. Default learner release requires: all hard-gate dimensions at least 3.5; all other dimensions at least 3; weighted score at least 3.5; no score of 0–1; no unassessed dimension; no unresolved critical defect; source status approved; complete lineage; independent review; calibration completion; and Human Accountable Owner approval. A rubric score does not waive legal, privacy, safety, or human-release policy.

Manual pilots may use these thresholds diagnostically. A non-independent pilot cannot receive a public `released` decision regardless of score.

## Calibration commitment

Before changing the weights or thresholds, or permitting a public learner release, complete a recorded calibration review of three manual pilot candidates across at least two source packages. If only one source package exists, use three materially distinct candidates and record the limited evidence. Compare dimension-level agreement, gate outcomes, defects, and learner-risk trade-offs; preserve the review as an evaluation or benchmark record. Any weight edit must preserve a total of exactly 100 and is verified arithmetically before adoption ([ADR-0007](../adr/0007-gate-arithmetic-and-record-status-hygiene.md)).

## Evaluation report content

For every dimension: score, evidence, evaluator confidence, defects, severity, recommended remedy, and whether the remedy affects another dimension. Report the weighted score, gate result, evaluation rubric version, candidate/version IDs, evaluator identities/types, operating scope, review independence, public-release eligibility, disagreement, and recommended disposition: release, private-pilot-complete, revise, hold, or reject.

## Defect severity

- **Critical:** false or harmful material claim, unavailable equivalent access, rights/privacy violation, or broken core learner task. Blocks release.
- **Major:** prevents a stated outcome or creates likely learner misunderstanding. Requires revision.
- **Minor:** reduces quality but does not invalidate the stated outcome. May be scheduled.
- **Observation:** opportunity without sufficient evidence to count as a defect.

## Change history

| Date | Change |
| --- | --- |
| 2026-08-13 | Added the Stage 1 dimension anchors (diagnostic) after the CAN-2026-0003/0004 comparison showed identical weighted scores for materially different teaching depth (MEM-2026-0004); no weight, gate, or eligibility rule changed. |
| 2026-08-13 | Corrected the weight table (Technical feasibility/performance intent 2% → 4%; the stated 100% total was previously 98 in fact) and normalized the gate formula to divide by the sum of the weights, per [ADR-0007](../adr/0007-gate-arithmetic-and-record-status-hygiene.md). Historical aggregates are corrected by dated retrospective appendices on EVAL-2026-0001 (3.37 → 3.45) and EVAL-2026-0002 (3.51 → 3.59); no gate outcome, disposition, or eligibility changed. |
| 2026-08-13 | Clarified scoring semantics: dimension scores record verified artifact evidence; review independence is enforced through its dedicated field and the release conditions, not deducted inside dimension scores. Historical note: the EVAL-2026-0001/0002 accessibility scores (3.0) embed an independence deduction and are not retroactively re-scored; future evaluations apply the split. |
