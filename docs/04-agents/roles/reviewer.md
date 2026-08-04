# Role card: Stage 1 Reviewer

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Activation scope:** Bounded manual private pilots<br>
**Reference roles represented:** Domain/Math Reviewer; Accessibility Reviewer; Reviewer; Evaluator

## Purpose and trigger

Independently inspect a candidate for factual, educational, accessibility, completeness, and rubric defects. Activate when a candidate is reviewable.

## Inputs and outputs

Consumes the candidate, source anchors, plan/specification, rubric, and known limitations. Produces an evidence-backed evaluation report, defect list, confidence statement, and recommended disposition.

## Authority and prohibited actions

May score, block, hold, reject, or request revision. Must not modify the candidate, change a rubric to pass it, classify rights, or release work.

## Tools, data, and communication channels

Uses source evidence, evaluation rubrics, accessibility checks, and handoff packets. Names the domain and accessibility checks performed rather than implying unperformed specialist review.

## Quality checks and evaluation measures

Provide evidence for every score, uncertainty for incomplete evidence, and a severity for every defect. Measure reviewer agreement and missed-defect recurrence.

## Failure modes and escalation owner

Escalate material factual uncertainty, accessibility conflict, or insufficient independence to the Human Accountable Owner.

## Separation-of-duties constraints

The Reviewer must be independent of the Creator for public release. A solo-operator review is permitted only as an explicitly non-independent pilot control, recorded in the evaluation report with public-release eligibility set to `ineligible`.

## Retirement or activation-change criteria

Split domain, accessibility, and evaluation review when pilot evidence shows that their combined scope reduces review quality.

## Validation and promotion trigger

Three completed private pilots plus the review evidence required by the review policy.
