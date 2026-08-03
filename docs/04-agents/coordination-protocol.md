# Multi-Agent Coordination Protocol

## Coordination model

The Orchestrator maintains a visible work graph. Nodes are versioned artifacts or decisions; edges are transformations, reviews, or dependencies. Each active node has exactly one accountable owner, although many roles may contribute evidence.

## Communication protocol

Agents communicate through the handoff packet, not unstructured conclusion-only messages. Every message declares its type: `request`, `handoff`, `review`, `decision-needed`, `blocker`, `reflection`, or `status`. Future tooling may serialize these types, but their meaning is defined here.

## Consensus and disagreement

- Independent evaluators may disagree; preserve both reports and calculate neither a hidden average nor a silent winner.
- The Orchestrator requests adjudication when disagreement affects a gate, confidence is low, or the difference exceeds one rubric level on a release-critical dimension.
- Domain truth, accessibility, rights, and learner-safety issues require the relevant specialist or human owner; general reviewers cannot waive them.
- A final decision identifies accepted evidence, rejected evidence, residual risk, and accountable owner.

## Health signals

Track handoff rejection rate, unresolved blocker age, iteration count, score delta per revision, evaluator agreement, recurrence of memory-tagged failures, and percentage of releases with complete lineage. These measure coordination quality, not individual agent worth.
