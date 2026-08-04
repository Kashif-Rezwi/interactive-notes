# ADR-0002: Activate five composite roles for Stage 1 pilots

**Status:** Proposed<br>
**Date:** 2026-08-04<br>
**Owner:** Repository maintainer / Human Accountable Owner<br>
**Decision scope:** Role activation and separation-of-duties controls for manual Stage 1 pilots<br>
**Supersedes / superseded by:** None

## Context and problem

The reference catalog defines 18 specialized roles, but no governed run has yet validated that all should operate separately. Stage 1 is a manual pilot phase. Activating all 18 roles would create process overhead before there is evidence that the additional boundaries reduce risk.

## Decision

Stage 1 proposes five experimental composite profiles: Coordinator, Steward, Creator, Reviewer, and Human Accountable Owner. The 18-role catalog remains the reference architecture and is not deleted. Each reference role maps to exactly one active profile.

## Decision drivers

- Keep manual pilots usable by a solo maintainer.
- Preserve the most important separation: creation, review, and accountable release judgment.
- Gather evidence before splitting composites into specialized operational roles.
- Follow the principle that complexity must be earned.

## Considered options

| Option | Benefits | Costs/risks | Decision |
| --- | --- | --- | --- |
| Activate all 18 roles | Maximum specialization on paper | High coordination cost with no operational evidence | Rejected for Stage 1 |
| Activate four profiles | Lowest overhead | Merges source/release stewardship into coordination | Rejected |
| Activate five profiles | Keeps stewardship visible while remaining manageable | Some specialist checks are composite | Selected |

## Consequences and controls

- A Creator cannot be the sole Reviewer or release authority for the same candidate.
- A solo operator may conduct distinct Creator and Reviewer passes only for a private pilot and must mark the review `non-independent`.
- A non-independent pilot cannot receive a public `released` decision.
- Public learner release requires an independent Reviewer and Human Accountable Owner approval.
- Reassess the profile after three completed private pilots or when a composite boundary causes a material defect, recurring rework, or review conflict.

## Evidence and validation

The [Stage 1 operating profile](../04-agents/stage-1-operating-profile.md) maps all 18 reference roles and supplies five role cards. Future private-pilot records will test handoff quality, reviewer independence, iteration cost, and recurring defects. This ADR may become `Accepted` only after the review evidence required by the review policy is recorded.

## Rollback or migration plan

Split a composite into one or more reference roles when evidence meets the activation criteria. Record the change in a superseding ADR only if it changes durable authority or release controls.

## Review trigger/date

Review after three completed private pilots, before any public learner release, or by 2026-11-04.
