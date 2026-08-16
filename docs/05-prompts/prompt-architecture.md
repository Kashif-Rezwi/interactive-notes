# Prompt Architecture

## Prompt stack

| Layer | Purpose | Stable across runs? | Owner |
| --- | --- | --- | --- |
| System policy | Safety, truthfulness, privacy, formatting, escalation | High | Governance owner |
| Role prompt | Agent purpose, boundaries, tools, handoff behavior | Medium | Agent owner |
| Task prompt | Specific transformation objective and context | Low | Orchestrator/task owner |
| Evidence context | Source excerpts, concept model, plan, constraints | Per run | Source/plan owner |
| Evaluation prompt | Rubric interpretation and evidence requirements | Medium | Evaluation owner |
| Reflection prompt | Root-cause analysis and learning capture | Medium | Quality/memory owner |
| Revision prompt | Bounded defect correction and regression preservation | Per loop | Orchestrator |

Compose prompts from named, version-pinned cards; do not rely on invisible copy/paste history. Rendered prompt content is recorded as a digest plus controlled-access snapshot in every generation run.

## Prompt-card requirements

Each card declares purpose, owner, status, layer, compatible agent roles, required inputs, output contract, hard constraints, uncertainty behavior, examples, anti-examples, evaluation set, known failure modes, change log, and deprecation/replacement path. See the template.

## Prompt quality rules

- Ask for a structured, reviewable output that names evidence and uncertainty.
- Distinguish source-grounded content from creative teaching choices.
- State prohibited shortcuts: fabricated citations, hidden assumptions, claim laundering through summaries, and untraceable external knowledge.
- Keep role behavior separate from task-specific material to enable targeted testing.
- Version every material semantic change, including rubric interpretation or output-format changes.

## Prompt persistence rule (WF-001, WF-015)

Every generation run must record its fully rendered prompt content in-repo: a controlled-access snapshot (the complete, un-redacted text sent to the model) plus its SHA-256 digest in the run ledger or a linked appendix. A digest-only reference to out-of-band material (session logs, operator scratchpads, unpersisted briefs) is a persistence failure — the prompt is a primary input to the artifact, and an unrecoverable prompt breaks reproducible lineage.

This rule addresses the V4 benchmark gap (WF-001): the V4 generation instruction (owner's 30-section brief, digest `f1a43cbf21cf`) exists in-repo only as a condensed snapshot. An authoritative reconstruction from surviving records is maintained in [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) per [ADR-0011](../adr/0011-benchmark-definition-and-artifact-change-protocol.md).

## Prompt evolution loop

Observe failures → cluster by cause → formulate a testable change hypothesis → run on frozen representative cases → compare quality, cost, latency, safety, and regressions → approve, revise, or reject → record the lesson. A prompt update without a comparison is an experiment, not an improvement.
