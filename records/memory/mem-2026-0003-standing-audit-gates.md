# MEM-2026-0003: Structural checks cannot see a lesson's two most damaging defect classes — audit dependency order and behavior explicitly

**Status:** Supported
**Curator:** Repository maintainer (solo Stage 1 operator)
**Created / review date:** 2026-08-10
**Scope:** Evaluation of any generated interactive lesson in Learning OS
**Tags:** evaluation, quality-gate, dependency-audit, behavioral-simulation, workflow
**Evidence records:** [RUN-20260810-0001](../runs/run-20260810-0001-linear-algebra-foundations-v4.md) §Revision 1, [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md) §Revision 1, [MEM-2026-0001](mem-2026-0001-prediction-gated-reveals.md), [MEM-2026-0002](mem-2026-0002-assessment-beyond-recognition.md)
**Supersedes / conflicts-with:** none

## Lesson

The pre-audit v4 build passed the entire standing verification suite (syntax, structure, zero-dependency, recomputation, load-level smoke test) while still containing three Major defects: (R1) a dependency-rule breach — matrix products used in Unit 6 before being defined; (R2) dead calibration UI — confidence logic wired only into the radio grading path; (R3) a quadrant-sensitive canvas drawing bug. None was visible to structural checks. They surfaced only through (a) a read-in-order dependency audit and (b) handler-level behavioral simulation of the actual learner flows.

## Why this is believed

- Direct evidence: R1–R3 were found post-verification by adversarial audit and confirmed repaired by re-running the extended suite (21/21 handler simulations pass).
- Mechanism: syntax/structure/recomputation verify *statics*; dependency order and interactive behavior are *dynamic/sequential* properties that require reading as a learner or firing events as a user.

## Recommended action

1. Both audits are codified as mandatory gates in the [lesson-generation workflow](../../docs/03-workflows/lesson-generation-workflow.md) P5 (audits 3 and 5) and the [QA checklist](../../library/rubrics/lesson-qa-checklist.md).
2. Every future lesson evaluation must cite evidence for both gates; "load-only smoke test passed" is insufficient.
3. When a reusable harness is built (Stage 2), the behavioral-simulation cases from RUN-20260810-0001 Revision 1 are the seed test set.

## Counterexamples and limitations

- Handler simulation under a hand-rolled DOM stub approximates browser behavior (selector scoping, event semantics); it catches logic defects, not rendering fidelity. A real-browser pass remains a distinct check.
- The dependency audit is manual and judgment-based; inter-rater consistency is unmeasured at Stage 1.

## Retrieval guidance

Consult at evaluation time for every learner-facing artifact, and when designing the Stage 2 evaluation harness.

## Privacy, rights, and retention classification

No personal data; retain as a standing quality gate until superseded by harness-level automation evidence.
