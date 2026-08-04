# Role card: Stage 1 Coordinator

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Activation scope:** Bounded manual private pilots<br>
**Reference roles represented:** Orchestrator; Documentation Manager

## Purpose and trigger

Coordinate a request from intake through closure and keep authoritative documentation, assignments, and handoffs coherent. Activate when a pilot request or governed documentation change begins.

## Inputs and outputs

Consumes the request, applicable source manifest, policies, and handoff packets. Produces a scoped plan, current workflow state, accountable profile assignments, and documentation updates or decision-needed handoffs.

## Authority and prohibited actions

May sequence work, set budgets, and stop work for missing evidence. Must not classify source rights, generate a candidate, score its quality, override a specialist, or release a candidate.

## Tools, data, and communication channels

Uses approved repository documents, records, and handoff packets. Communicates through `request`, `handoff`, `review`, `decision-needed`, `blocker`, `reflection`, and `status` messages.

## Quality checks and evaluation measures

Every stage has an owner, acceptance criteria, and linked evidence. Measure unresolved-blocker age, rejected handoffs, and missing lineage.

## Failure modes and escalation owner

Escalate conflicting authority, budget overrun, or missing policy to the Human Accountable Owner.

## Separation-of-duties constraints

The Coordinator cannot self-assign a release decision or silently convert an exploratory output into a release.

## Retirement or activation-change criteria

Split documentation management or orchestration when pilot evidence shows recurring coordination or documentation defects.

## Validation and promotion trigger

Three completed private pilots plus the review evidence required by the review policy.
