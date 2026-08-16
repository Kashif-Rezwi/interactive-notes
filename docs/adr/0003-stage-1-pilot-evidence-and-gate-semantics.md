# ADR-0003: Define Stage 1 pilot evidence and gate semantics

**Status:** Proposed<br>
**Date:** 2026-08-04<br>
**Owner:** Repository maintainer / Human Accountable Owner<br>
**Decision scope:** Stage 1 run and evaluation evidence, pilot closure, and score precision<br>
**Supersedes / superseded by:** None — except the `/100` weighted-score formula clause in the Decision section below, which is superseded by [ADR-0007](0007-gate-arithmetic-and-record-status-hygiene.md) (normalized formula `Σ(score × weight) / Σweights`; all other semantics here unchanged)

## Context and problem

ADR-0002 permits a solo operator to perform separately documented Creator and Reviewer passes for a private pilot, but the existing run and evaluation templates do not record that limitation or distinguish a completed private pilot from a public learner release. The numeric gate requires 3.5 while the rubric describes only whole-number levels, which prevents reproducible gate calculations.

## Decision

For the bounded Stage 1 trial, run and evaluation records must declare work classification, operating scope, review independence, public-release eligibility, and disposition. A non-independent result is ineligible for public release regardless of score and may close only as `private-pilot-complete`, `revise`, `hold`, or `reject`. `released` remains reserved for a public learner release that satisfies all evaluation gates.

Dimension scores use only 0.5-point increments from 0 to 4. Calculate the weighted aggregate as `sum(dimension score × dimension weight) / 100`; compare the unrounded result to gates and display it to two decimal places.

## Decision drivers

- Preserve the separation-of-duties boundary when a solo maintainer performs a manual pilot.
- Make release eligibility evident from records rather than narrative inference.
- Make Stage 1 gate results reproducible before calibration data exists.

## Considered options

| Option | Benefits | Costs/risks | Decision |
| --- | --- | --- | --- |
| Free-text pilot and reviewer limitations | Lowest template change | Not auditable or consistently queryable | Rejected |
| Whole-number scores with an implicit 3.5 threshold | Simple rubric labels | Makes the hard gate ambiguous | Rejected |
| Controlled pilot fields and 0.5-point scores | Clear evidence and gate calculations | Adds small manual-recording overhead | Selected for trial |

## Consequences and controls

- `private-pilot-complete` is not a release, public learner-release claim, or benchmark result.
- A public release candidate needs independent Reviewer evidence, calibration completion, and Human Accountable Owner approval in addition to numeric gates.
- An unassessed dimension blocks a release decision; simulation-only examples may use non-record values such as `Not assessed` only when clearly marked as non-evidence.

## Evidence and validation

Use a simulated private-pilot walkthrough to verify the record fields. Validate the model during three private pilots under the calibration commitment. This ADR may become `Accepted` only after the required review evidence is recorded.

## Rollback or migration plan

If pilot evidence shows the fields or score precision are unsuitable, create a superseding ADR and retain all prior run/evaluation semantics in historical records.

## Review trigger/date

Review after three completed private pilots, before public learner release, or by 2026-11-04.
