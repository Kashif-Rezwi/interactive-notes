# Logging Architecture

## Principle

Every generation, evaluation, revision, decision, and memory disposition produces structured, append-only evidence. Future tooling may serialize this evidence, but the required semantics begin here.

## Event families

| Event | Minimum fields |
| --- | --- |
| Intake | request ID, purpose, requester authority, source IDs, risk classification, scope decision |
| Source handling | source ID/version, rights status, extraction method/version, failures, citation anchors |
| Planning | concept/plan/spec IDs, owner, assumptions, acceptance criteria, approvals |
| Generation | run ID, parent run, model/config identity, prompt-card versions/digests, inputs, time, cost, candidate IDs, warnings/errors |
| Evaluation | candidate/rubric IDs, evaluator identity/type, operating scope, review independence, public-release eligibility, scores, evidence, confidence, defects, disagreement |
| Revision | triggering defect, root-cause hypothesis, changed variables, regression checks, score delta |
| Decision | decision ID, alternatives, evidence, approver, rationale, residual risk, review date |
| Memory | proposed lesson, disposition, confidence, provenance, expiry/review date |
| Release | gate results, accountable owner, artifact version, disposition, eligibility, known limitations, rollback/revision path |

## Run ledger

Each run has one immutable ledger that links all events in chronological order. It must let a reviewer reconstruct: which source and rights basis were used; what was asked; which prompt/model/configuration produced each candidate; how it was evaluated; why it changed; who approved release; and which lesson entered memory.

## Operational metrics

Track throughput, stage latency, cost, failed-run rate, retry count, score distribution, score delta, critical-defect rate, evaluator agreement, prompt/model comparison, provenance completeness, and memory promotion/reversal rate. Segment by source type, artifact family, risk class, model, prompt bundle, and workflow version. Metrics diagnose the system; do not use them as undisputed educational proof.

## Privacy and access

Classify events before storage. Minimize content capture, redact sensitive data, restrict raw prompts/outputs when necessary, and record access/export actions. Logs must support deletion/retention obligations while retaining a non-sensitive audit statement that an action occurred.
