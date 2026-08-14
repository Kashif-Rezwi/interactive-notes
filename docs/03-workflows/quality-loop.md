# Loop Engineering: Quality Loop

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Validation and promotion trigger:** Three completed private pilots plus the review evidence required by the review policy.

The loop is an evidence-driven control system, not repeated generation. It seeks the smallest verified change that resolves an observed defect while protecting already-passing dimensions.

## State machine

| State | Entry condition | Action | Transition |
| --- | --- | --- | --- |
| `planned` | Approved objective and acceptance criteria exist | Select source, plan, prompts, rubric, budget | `generating` or `blocked` |
| `generating` | Inputs are version-pinned | Create one candidate and run record | `evaluating` or `failed` |
| `evaluating` | Candidate is renderable/reviewable | Execute standing audits (P5 Audits 1–6, including rendered verification per ADR-0010); execute mandatory adversarial re-examination (ADR-0009); score rubric | `reflecting`, `revising`, `validated`, or `blocked` |
| `reflecting` | Evaluation and adversarial re-examination are recorded with evidence | Diagnose root cause; propose a minimal revision hypothesis or closure rationale | `revising`, `pilot-complete`, or `stopped` |
| `revising` | Hypothesis and target scores are declared | Change only the implicated plan, prompt, spec, or candidate | `generating` with parent-run link |
| `validated` | Public-release gates pass after independent review and calibration | Perform release validation and lineage audit | `released` or `blocked` |
| `released` | Accountable release decision accepted | Curate lessons and close run | `done` |
| `pilot-complete` | A private pilot has evaluation, reflection, a `private-pilot-complete` disposition, public-release eligibility `ineligible`, and clean adversarial re-examination evidence | Preserve limitations, curate lessons, and close without release | `done` |
| `stopped` | Further iteration lacks value or authority | Capture reason and learning | `done` |
| `failed` / `blocked` | Technical, evidence, policy, or authority issue | Preserve evidence; route to owner | `planned`, `stopped`, or `done` |

No transition skips evaluation, rendered verification, or adversarial re-examination after a material candidate change. A revision must name the parent run, observed defect, root-cause hypothesis, expected score movement, and regression checks. A candidate that passes standing audits transitions to `reflecting` only after documented adversarial re-examination evidence is recorded (clean pass with evidence or defects diagnosed).

## Evaluation and scoring

Use the reusable rubric in `docs/06-evaluation/`. Each dimension receives a 0–4 score, evidence, confidence, and blocker flag. The aggregate is a weighted release signal, not a substitute for hard gates.

**Gate authority:** [the evaluation framework](../06-evaluation/evaluation-framework.md#provisional-stage-1-gate-rules) defines the sole authoritative numeric release gates, score precision, and their provisional status. Domains may raise thresholds in a benchmark charter. A non-independent pilot cannot receive a public `released` decision.

## Retry policy

1. Classify the failure: source gap, plan defect, experience defect, prompt defect, model limitation, evaluator disagreement, or policy/technical blocker.
2. Apply the narrowest remedy at the earliest responsible stage; do not patch downstream symptoms when the plan is wrong.
3. Re-run only the necessary dependent stages, preserving prior artifacts and input versions.
4. Change one primary variable per experiment. Multiple changes require an explicit comparative experiment design.
5. Run targeted regression checks for dimensions previously passing.

## Budgets and stopping conditions

Set run-level ceilings before generation: maximum iterations, wall time, model spend, reviewer effort, and acceptable risk. Stop and escalate when any is reached.

Stop successfully with `released` only when public-release gates pass and expected benefit from another iteration is below the declared improvement threshold. Close a sufficiently evaluated non-independent private pilot only as `private-pilot-complete`. Stop without release when the source cannot substantiate needed claims, quality cannot reach the minimum under budget, reviewers have unresolved material disagreement, authorization is missing, or the artifact would create unacceptable learner risk.

Never continue merely because an agent can generate another variation. A score plateau across two targeted revisions triggers root-cause review or human escalation.

## Mandatory learning update

At closure, the Logger creates the run ledger. The Memory Manager evaluates each proposed lesson: promote if it is reusable, evidenced, scoped, and non-duplicative; otherwise retain it only in the run reflection. A closed run without an explicit memory disposition is incomplete.
