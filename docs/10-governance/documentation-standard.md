# Documentation Standard

## Required shape

Every authoritative document begins with a clear title and answers, as applicable: purpose, owner, status, audience, scope, non-goals, inputs/dependencies, decisions/constraints, procedure or contract, acceptance criteria, evidence/links, change history, and review date. Keep the content proportional; a glossary entry does not need an operations manual.

## Writing rules

- Write for an intelligent reader or agent with no unstated context.
- Use normative language intentionally: **must** for non-negotiable requirements, **should** for strong defaults, **may** for options.
- Define terms once in the glossary and link to their source of truth.
- Prefer short, atomic sections and tables for repeated contracts. Link rather than duplicate.
- Separate observed fact, interpretation, hypothesis, and decision.
- Cite source material and record uncertainty. Do not turn a model output into evidence by restating it.
- State boundaries and failure modes, not only ideal paths.

## Authority and lifecycle

| Status | Meaning |
| --- | --- |
| Draft | Proposal; not operationally binding |
| Experimental | Bounded trial; use only within stated scope |
| Approved | Current standard; agents should follow it |
| Deprecated | Still traceable; do not start new work with it |
| Superseded | Replaced by a linked authority |
| Archived | Historical evidence; not current guidance |

Documents with durable operational impact need an owner and review date. New documents link to related ADRs, templates, policies, and records. The Documentation Manager performs link, terminology, duplication, and status checks before approval.
