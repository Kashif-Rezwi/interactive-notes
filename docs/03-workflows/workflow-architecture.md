# Workflow Architecture

## Operating flow

The reference-role names below describe the target architecture. Manual Stage 1 pilots use the five composites in the [Stage 1 operating profile](../04-agents/stage-1-operating-profile.md), which preserves the same control boundaries.

| Stage | Accountable role | Required input | Required output | Exit condition |
| --- | --- | --- | --- | --- |
| 0. Intake and authorization | Orchestrator + Source Steward | Request and source package | Intake decision | Scope, authorization, risk, and owner are known |
| 1. Source understanding | Parser + Domain Reviewer | Authorized source | Extraction evidence and concept model | Claims are anchored; gaps are declared |
| 2. Learning design | Teacher + Curriculum Planner | Concept model | Learning plan and assessment plan | Outcomes and prerequisites are measurable |
| 3. Experience design | Visualization + Accessibility planners | Learning plan | Experience specification | Interaction is purposeful and alternatives are defined |
| 4. Generation | Generator | Approved plan/specification and prompt set | Candidate artifact and run record | Candidate is complete enough to evaluate |
| 5. Review | Review specialists | Candidate, sources, rubrics | Evaluation reports and defect list | Evidence supports all scores and blockers are classified; public release requires independent review |
| 6. Improvement loop | Orchestrator + Generator | Defect list and reflection | Revised candidate/run | Targeted defects have a verified response |
| 7. Release judgment | Release steward + humans | Candidate, evaluations, lineage | Release or hold decision | Gate criteria and accountability are satisfied |
| 8. Learning capture | Logger + Memory Manager | Completed run and decision | Run ledger, experiment result, memory disposition | Reusable lessons are curated or rejected explicitly |

## Two-speed work

**Exploration** permits fast, isolated prototypes. It requires source rights, a hypothesis, and a record, but cannot modify approved prompts, memory, benchmarks, or release policy.

**Production** consumes approved inputs, writes full lineage, runs required evaluations, and passes release gates. Artifacts must never move from exploration to production by copy/paste; they are formally promoted with their evidence.

## Autonomous execution mode (ADR-0012)

The workflow stages (0–8) and the specialized lesson lifecycle (P0–P6) may be executed autonomously by an AI agent following the governed skill document ([.agents/skills/generate-lesson/SKILL.md](../../.agents/skills/generate-lesson/SKILL.md)) and orchestration card ([prm-orchestrator-autonomous@0.1.0](../../library/prompts/prm-orchestrator-autonomous@0.1.0.md)).

Autonomous execution preserves every boundary from manual execution: identical planning records (CM, LP, XS), identical QA audits (Audits 1–6), the mandatory adversarial gate ([ADR-0009](../adr/0009-forced-adversarial-re-examination-gate.md)), and full in-repo persistence ([ADR-0010](../adr/0010-rendered-output-verification.md), [ADR-0011](../adr/0011-benchmark-definition-and-artifact-change-protocol.md)). Self-correction is budget-bounded to a maximum of 2 revision cycles before escalating to human review. Output status is `private-pilot-complete` under non-independent review rules ([ADR-0003](../adr/0003-stage-1-pilot-evidence-and-gate-semantics.md)).

## Work intake triage

Every request receives a scope classification:

| Class | Typical change | Required control |
| --- | --- | --- |
| Clarification | Terminology or link correction | Peer review |
| Reversible experiment | Prompt or design hypothesis | Experiment record and isolated results |
| Quality-impacting change | Rubric, workflow, or prompt behavior | Evaluation comparison and specialist review |
| Durable architecture | Data model, system boundary, governance, provider commitment | ADR, alternatives, human approval |
| High-risk content | Sensitive, regulated, high-stakes, or restricted content | Domain and policy escalation before generation |

## Separation of duties

The role that generates a candidate cannot be its sole factual, educational, accessibility, or release reviewer. The orchestrator coordinates work but cannot silently overrule a specialist. Any override is a decision record with rationale and accountable human approver.

For a solo-operator pilot, Creator and Reviewer passes must be separately recorded as non-independent. That limitation sets public-release eligibility to `ineligible` and blocks a public `released` decision; only `private-pilot-complete`, hold, revise, or reject is permitted. [ADR-0003](../adr/0003-stage-1-pilot-evidence-and-gate-semantics.md) defines the controlled record fields and score precision.
