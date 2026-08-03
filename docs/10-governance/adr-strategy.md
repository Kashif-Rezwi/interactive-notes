# ADR Strategy

## When to write an ADR

Create an Architecture Decision Record for a significant, durable, or hard-to-reverse choice: system boundary, data ownership, storage/retention policy, model/provider strategy, framework commitment, public interface, quality gate, agent authority, security control, or replacement of a core workflow.

Do not create ADRs for routine edits, reversible experiments, or implementation details that have no cross-team consequence. Capture those in change records or experiments instead.

## Rules

- ADRs are numbered sequentially and stored in `docs/adr/`.
- Accepted ADRs are immutable except for corrections that do not change the decision. Change the decision with a new ADR that supersedes the old one.
- Each ADR states context, decision, alternatives, consequences, evidence, risks, owner, status, and review trigger.
- An ADR is not approved by an agent alone when it changes policy, public behavior, sensitive data handling, or an implementation commitment.

See [the ADR directory](../adr/README.md) and [template](../../templates/adr/adr.md).
