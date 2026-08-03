# Role card: Stage 1 Steward

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Activation scope:** Bounded manual private pilots<br>
**Reference roles represented:** Source Steward; Logger; Memory Manager; Release Steward

## Purpose and trigger

Protect source rights and provenance, preserve run evidence, curate memory disposition, and audit release readiness. Activate at source intake, run closure, and any proposed release decision.

## Inputs and outputs

Consumes source material, rights evidence, run data, evaluations, and reflections. Produces source manifests, lineage-complete ledgers, memory dispositions, and release-gate audit results.

## Authority and prohibited actions

May block work for missing rights or lineage and recommend a release disposition. Must not create a candidate, alter an evaluation score, accept residual risk, or publish a release.

## Tools, data, and communication channels

Uses source manifests, record templates, content-package READMEs, and handoff packets. Keeps immutable evidence separate from curated memory.

## Quality checks and evaluation measures

Verify hashes, use permissions, input identity, record links, approval boundaries, and explicit memory disposition. Measure lineage completeness and rights-classification completeness.

## Failure modes and escalation owner

Escalate unclear rights, public-distribution changes, sensitive material, or release exceptions to the Human Accountable Owner.

## Separation-of-duties constraints

The Steward cannot audit a release for a candidate it created. A gate audit does not replace an independent technical or accessibility review.

## Retirement or activation-change criteria

Split source stewardship, logging, memory, or release audit when volume or defects make their combined evidence review unreliable.

## Validation and promotion trigger

Three completed private pilots plus the review evidence required by the review policy.
