# Operational Playbooks

Until automation exists, these playbooks are performed manually with the same records future automation must produce.

| Playbook | Trigger | Primary owner (reference role) | Stage 1 profile (ADR-0002) | Required exit evidence |
| --- | --- | --- | --- | --- |
| Start a new course or learning unit | Authorized source and learning need | Orchestrator | Coordinator | Intake, source package, concept model, learning plan, risk classification |
| Import a notebook or technical source | New source material | Source Steward + Parser | Steward + Creator (extraction) | Source manifest, extraction evidence, anchored claims, known gaps |
| Generate a new lesson | Approved plan/specification | Generator | Creator | Candidate, complete run ledger, independent evaluation |
| Improve an existing lesson | Defect or hypothesis | Orchestrator | Coordinator | Baseline, root-cause hypothesis, targeted revision, regression evidence |
| Improve a visualization | Learner confusion or visual defect | Visualization Planner | Creator | Representation diagnosis, accessibility alternatives, revised scorecard |
| Revise a prompt | Recurrent failure or measured opportunity | Prompt owner | Coordinator, with Reviewer evidence | Versioned card, test set comparison, migration/rollback decision |
| Benchmark models/workflows | Procurement, change proposal, or scheduled review | Evaluation owner | Reviewer | Frozen protocol, comparable runs, adjudicated report, decision |
| Curate memory | Completed run or recurring lesson | Memory Manager | Steward | Promotion/rejection record, confidence, scope, expiry |
| Release an artifact or policy | Gates pass | Release Steward + human owner | Steward + Human Accountable Owner | Gate checklist, lineage audit, known limitations, decision |
| Respond to an incident | Material quality/trust/policy event | Accountable owner | Human Accountable Owner | Containment, impact analysis, corrective action, follow-up record |

Owners are named as reference roles; at Stage 1 each maps to exactly one composite profile per the [Stage 1 operating profile](../04-agents/stage-1-operating-profile.md).

## Playbook standard

Each playbook must state: purpose; trigger; owner and approvers; prerequisites; input and output manifests; numbered procedure; decision points; quality checks; evidence to log; time/cost budget; failure modes; escalation; exit criteria; and retrospective questions. Start from `templates/playbook/playbook.md`.

## High-value procedure: improve an existing lesson

1. Preserve the released baseline and identify the learner-impacting defect with evaluation evidence.
2. Trace the defect to source understanding, plan, specification, prompt, model behavior, or implementation (once implementation exists).
3. Declare one primary revision hypothesis, expected score movement, and regression dimensions.
4. Produce a child run; do not overwrite the baseline.
5. Re-evaluate using the same rubric and, where possible, blinded comparison.
6. Release, hold, or reject based on gates—not aesthetic preference alone.
7. Capture a scoped lesson in memory and update the playbook if the process itself changed.
