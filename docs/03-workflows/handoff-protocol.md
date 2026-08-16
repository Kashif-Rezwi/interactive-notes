# Handoff Protocol

## Handoff packet

Every role-to-role transfer includes:

1. **Objective:** the learner or system outcome being pursued.
2. **Scope and status:** what is included, excluded, decided, and unresolved.
3. **Input manifest:** stable IDs, versions, authorization/classification, and source of truth.
4. **Output manifest:** produced IDs, summaries, quality status, and known limits.
5. **Acceptance criteria:** conditions the recipient must verify or preserve.
6. **Evidence:** citations, evaluation report links, test/inspection results, and confidence.
7. **Risks and dependencies:** blockers, assumptions, escalation needs, and deadlines/budgets.
8. **Requested action:** the next accountable decision or transformation.

## Communication rules

- State facts, inferences, and proposals separately.
- Quote stable IDs and versions, not ambiguous filenames or “latest” artifacts.
- The recipient acknowledges accepted, rejected, or incomplete handoffs; silence is not acceptance.
- A recipient may return a handoff with a concrete deficiency list instead of guessing.
- Source facts retain evidence anchors through every handoff; summaries do not replace provenance.

## Escalation

Escalate to a human owner before proceeding when rights are unclear; sensitive learner data is implicated; a factual claim has material impact and weak evidence; a release gate is overridden; budget is exceeded; or agent roles disagree materially. Log the question, alternatives, evidence, decision owner, and deadline.
