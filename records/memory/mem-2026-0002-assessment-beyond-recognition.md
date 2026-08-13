# MEM-2026-0002: Recognition-only assessment is the dominant defect class in generated lessons

**Status:** Supported
**Curator:** Repository maintainer (solo Stage 1 operator)
**Created / review date:** 2026-08-10
**Scope:** All Learning OS lesson generation and evaluation
**Tags:** assessment, retrieval-practice, evaluation-rubric, quality-gate
**Evidence records:** [RUN-20260810-0001](../runs/run-20260810-0001-linear-algebra-foundations-v4.md), [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md), [EVAL-2026-0001](../evaluations/eval-2026-0001-linear-algebra-foundations-v2.md)
**Supersedes / conflicts-with:** none

## Lesson

All three AIML-4 Module 2 variants (v1 historical, v2, v3 — different authors/models) independently converged on the same defect: assessments composed entirely of recognition-format items (MCQ/matching), or none at all. Three isolated audits diagnosed the identical gap. Recognition lets a learner "complete" a lesson while unable to compute, explain, or transfer — precisely the owner's stated failure mode with the original course.

## Why this is believed

- Convergent evidence across three independent generations: the defect is systematic, not idiosyncratic — expect it by default in future generations.
- Literature: retrieval practice / testing effect is high-utility (Dunlosky et al. 2013); ICAP predicts constructive > active engagement; fluency illusions (Bjork) explain why recognition *feels* like learning.
- v4 repair: every unit check includes ≥1 constructed response (numeric entry or explain-in-words with model-answer reveal); the mastery check interleaves units and adds reasoning/transfer/error-identification items plus confidence tags.

## Recommended action

1. Add to every lesson specification: "each unit check includes at least one constructed-response item; the final assessment interleaves units and includes at least one transfer item and one error-identification item; mastery items must not repeat worked examples."
2. Add to the evaluation rubric's educational-quality dimension an explicit check: "assessment requires retrieval/computation/explanation, not recognition only."
3. Add to the standing verification suite: a structural scan that flags a lesson whose assessments are 100% radio/select inputs.

## Counterexamples and limitations

- Constructed-response grading is shallow (numeric tolerance, self-graded explanations); it verifies effort and exact numerics, not free-text correctness. Acceptable at Stage 1; revisit if an NLP grader is ever introduced.
- Confidence tags add clicks; v4 restricts them to the mastery check only.

## Retrieval guidance

Consult at specification time and at evaluation time for every learner-facing lesson. This item should be re-reviewed after the first real learner pilot.

## Privacy and retention

No personal data; retain as a standing quality gate until superseded.
