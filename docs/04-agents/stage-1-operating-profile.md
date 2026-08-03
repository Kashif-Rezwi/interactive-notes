# Stage 1 operating profile

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Validation and promotion trigger:** Three completed private pilots plus the review evidence required by the review policy.

Stage 1 uses five composite roles for bounded manual private pilots. This profile operationalizes proposed [ADR-0002](../adr/0002-stage-1-role-activation-profile.md); it does not remove or weaken the 18-role reference catalog.

## Active profiles

| Profile | Role card | Reference roles represented | Primary boundary |
| --- | --- | --- | --- |
| Coordinator | [Coordinator](roles/coordinator.md) | Orchestrator; Documentation Manager | Does not classify rights, generate candidates, review its own candidate, or release work |
| Steward | [Steward](roles/steward.md) | Source Steward; Logger; Memory Manager; Release Steward | Does not create or score the candidate it audits |
| Creator | [Creator](roles/creator.md) | Parser; Concept Extractor; Teacher; Curriculum Planner; Visualization Planner; Experience/Interaction Planner; Generator | Cannot be the sole reviewer or release authority for its candidate |
| Reviewer | [Reviewer](roles/reviewer.md) | Domain/Math Reviewer; Accessibility Reviewer; Reviewer; Evaluator | Does not alter candidates or waive policy gates |
| Human Accountable Owner | [Human Accountable Owner](roles/human-accountable-owner.md) | Human Accountable Owner | Owns rights, risk acceptance, and public-release decisions |

## Mapping and activation rule

Every reference role is represented exactly once in the table above. A pilot may use a single person in more than one profile only when each pass is separately recorded. Any Creator-to-Reviewer pass by the same person is `non-independent`, and the resulting candidate may be held, revised, rejected, or marked `private-pilot-complete`, but never marked publicly `released`. The controlled record fields are defined by proposed [ADR-0003](../adr/0003-stage-1-pilot-evidence-and-gate-semantics.md).

Split a composite role when three pilots show recurring defects, handoff confusion, avoidable rework, specialist disagreement, or a material risk that the composite cannot control. See ADR-0002 for the review trigger.
