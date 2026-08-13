# RUN-20260804-0001: Stage 1 private pilot — linear algebra foundations candidate

**Status:** Pilot complete<br>
**Parent run:** None<br>
**Owner:** Repository maintainer (solo Stage 1 operator; Coordinator, Creator, Reviewer, and Human Accountable Owner passes recorded separately)<br>
**Objective:** Run one bounded Stage 1 private pilot for AIML-4 Module 2 from SRC-2026-0001: produce a source-grounded concept model, learning plan, experience specification, and one new interactive-notes candidate, with linked evaluation evidence.<br>
**Budget:** 1 generation iteration plus in-generation corrections; 1 non-independent review pass; no external model spend beyond the operator's agent session; no learner contact<br>
**Classification:** exploratory<br>
**Operating scope:** Stage 1 private pilot<br>
**Review-independence summary:** non-independent<br>
**Public-release eligibility:** ineligible

## Input manifest

| Input | Identity | Version/pin |
| --- | --- | --- |
| Source package | [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md) | Notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` |
| Concept model | [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) | Created in this run, 2026-08-04 |
| Learning plan | [LP-2026-0001](../plans/lp-2026-0001-linear-algebra-foundations.md) | Created in this run, 2026-08-04 |
| Experience specification | [XS-2026-0001](../specifications/xs-2026-0001-linear-algebra-foundations-v2.md) | Created in this run, 2026-08-04 |
| Prompt bundle | None | **Limitation:** no approved prompt cards exist in `library/prompts/`; generation was driven by the operator's instruction and repository templates. Prompt identity is therefore weak and recorded here as a pilot finding. |
| Model/configuration | AI coding agent operated through the LM Studio Bionic desktop harness | Exact model identifier and parameters are not exposed to the operator; recorded as unknown rather than inferred |
| Rubric | [Evaluation framework](../../docs/06-evaluation/evaluation-framework.md) | Provisional Stage 1 defaults (Experimental; review by 2026-11-04) |
| Workflow | [Quality loop](../../docs/03-workflows/quality-loop.md) | Experimental; Stage 1 five-profile model per [ADR-0002](../../docs/adr/0002-stage-1-role-activation-profile.md) and record fields per [ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md) |
| Benchmarks | None | No benchmark suite exists; none used or claimed |

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-04 (IST) | CAN-2026-0001 | Agent via LM Studio Bionic; model ID not exposed | None (no prompt cards; see input-manifest limitation) | Single operator session | None |
| 2026-08-04 (IST) | CAN-2026-0001 (in-generation correction) | Same | None | Same session | Two self-caught defects fixed before evaluation: source examples mislabeled as constructed; widgets lacked reset controls required by XS-2026-0001 |

Candidate: [`linear-algebra-foundations-v2.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v2.html), SHA-256 `81bdd4bcf260bfb97d74f7da60b2709a95d5d1cae97d1f2180ebdda1bee49aad`, 49,066 bytes, zero external runtime dependencies. The filename is operator-assigned; the stable identity is CAN-2026-0001 (the naming standard's prohibition on "v2" as identity is satisfied by the CAN identifier, not the filename).

## Evaluation and defects

Full scorecard: [EVAL-2026-0001](../evaluations/eval-2026-0001-linear-algebra-foundations-v2.md). Weighted aggregate 3.37 (diagnostic only). No critical defects. Minor defects: no mastery gating; preset-bounded vector entry. One release-relevant major limitation: accessibility not verified by an independent specialist or screen reader. Verification evidence: JS syntax check passed; all seven widgets executed under a DOM/canvas stub with correct readouts; widget math independently recomputed (least squares slope 0.7 / intercept 0.3 / SSE 0.3; projection e·y ≈ 0; AB ≠ BA); zero external references found.

## Reflection and root-cause hypothesis

The five-profile Stage 1 model is operable end-to-end by a solo operator, and the records in this run are sufficient to reconstruct the lineage without outside context. Two process findings: (1) the absence of versioned prompt cards weakens prompt identity — future pilots should draft at least experimental prompt cards in `records/` before generation; (2) both in-generation defects were specification-conformance slips caught by re-reading XS-2026-0001, suggesting a pre-generation spec checklist would have prevented them. The non-independent review caps confidence, and no learner evidence exists; nothing in this run supports a public-release, benchmark, or efficacy claim.

## Revision history and regression checks

One in-generation correction set (see generation events); no post-evaluation revision was needed because the evaluation found no critical or pilot-blocking major defects. Regression checks after correction: JS syntax re-check and full widget stub re-run passed; source-notebook and historical `index.html` hashes re-verified unchanged.

## Decision and approvers

**Disposition:** private-pilot-complete<br>
**Decision scope:** private pilot<br>
**Approvers and limitations:** Approved for pilot closure by the Human Accountable Owner (the same solo operator) on 2026-08-04. Under ADR-0002/ADR-0003 a non-independent pilot may close only as `private-pilot-complete`, `revise`, `hold`, or `reject`; this disposition is not a public learner release, not a benchmark result, and not a learning-efficacy claim. Public-release eligibility remains `ineligible` regardless of the 3.37 diagnostic aggregate.

## Memory disposition

No memory item is promoted. Candidate lessons — (a) create experimental prompt cards before generation to restore prompt identity; (b) use a specification-conformance checklist before evaluating; (c) reset controls and dual visual+numeric readouts are a reusable widget pattern — are retained here only. Rationale: this is the first private pilot; the calibration commitment requires three completed pilots before patterns are promoted, and these observations are not yet independently evidenced.

## Lineage audit

- Source notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` — verified unchanged after the run.
- Historical [`linear-algebra-foundations-v1.html` (formerly `index.html`)](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v1.html) SHA-256 `687bccda2b71b8fd50b84a1198b194697598de6fa6c54e992c71ccdf5122fee1` — verified unchanged after the run; it remains a historical artifact, not a governed release.
- Chain: SRC-2026-0001 → CM-2026-0001 → LP-2026-0001 → XS-2026-0001 → CAN-2026-0001 → EVAL-2026-0001 → this run. All links resolve within this repository.
