# Review Policy

## Minimum reviews

| Change | Required review |
| --- | --- |
| Foundation, product, or governance policy | Peer reviewer and human owner |
| System boundary, durable data model, external dependency | ADR review and human architecture owner |
| Agent prompt/role or workflow | Owner, evaluator, and affected specialist |
| Learning artifact | Educational, factual/domain, accessibility, and release review |
| Benchmark/rubric | Evaluation owner plus calibrated reviewers |
| Memory item marked Established | Memory Manager plus evidence reviewer |

## Review quality

A review names the scope inspected, evidence considered, defects by severity, unresolved questions, decision (approve/request changes/hold/reject), and reviewer identity/role. “Looks good” is not sufficient evidence for high-impact work.

## Status accuracy

An `Experimental` document may guide only its stated bounded trial and must name its validation and promotion trigger. An `Approved` document or `Accepted` ADR must link or contain the review evidence required by this policy. If that evidence is not yet recorded, use `Experimental` or `Proposed`; do not imply a completed review. **Stage 1 solo-maintainer path:** where the repository maintainer is both author and Human Accountable Owner, an ADR may be Accepted on a recorded self-review that names the scope inspected, evidence considered, decision, and the independence limitation; the ADR's review trigger/date then schedules its formal re-examination.

## Independence

Reviewers should be independent of generation for release-critical dimensions. When team size makes full independence impossible, record the limitation and compensate with benchmark evidence, delayed review, or human oversight. Do not approve your own exception.
