# Learning OS Agent Operating Manual

This file is the entry point for any AI coding agent working in Learning OS. Treat the repository as executable architecture: documents are operational constraints, not optional background reading.

## Mandatory reading order

1. `README.md`
2. `docs/00-foundation/charter.md`, `principles.md`, and `glossary.md`
3. `docs/02-system/repository-map.md` and `system-blueprint.md`
4. The relevant workflow, agent role card, standard, template, and ADRs
5. For any lesson generation or revision: `docs/01-product/lesson-standard.md` and `docs/03-workflows/lesson-generation-workflow.md` (ADR-0004)

## Operating rules

- Do not introduce implementation code before the roadmap phase and ADR gate permit it.
- Preserve source artifacts. Never alter input material, historical records, or accepted memory without an explicit, traceable supersession.
- Work from an issue, request, or documented hypothesis. State the outcome, evidence, open assumptions, and next handoff.
- Treat every generation as a run: it must have input identity, model and prompt identity, evaluation evidence, reflection, and memory disposition.
- Do not promote a prompt, rubric, agent contract, or lesson from draft to approved without its required evaluation and human-review status.
- Prefer a small, composable document change over duplicate or broad guidance. Link rather than copy.
- Raise uncertainty when a decision changes user trust, educational truthfulness, data rights, accessibility, security, cost, or public API shape.

## Change protocol

1. Locate the applicable acceptance criteria and existing decision records.
2. Create or update the smallest authoritative document.
3. Update cross-links, version history, and affected templates where necessary.
4. Add an ADR for a durable, hard-to-reverse architectural choice.
5. Record how the change will be evaluated and what memory should be captured.
6. Request the review defined by `docs/10-governance/review-policy.md`.

## Boundaries

The operating manual defines future behavior; it does not execute it. Markdown examples illustrate contracts in plain language and must not become premature pseudo-implementations. The `content/` tree may retain owner-authorized historical learning artifacts under the content-package convention, with their rights and governance status made explicit. Do not add application implementation, newly generated lesson output outside the governed workflow, private learner data, credentials, vendor dumps, or source content without documented authorization or a recorded no-redistribution restriction.

## Completion checklist

- [ ] Intent, scope, and non-goals are explicit.
- [ ] Evidence and traceability are linked.
- [ ] Applicable quality, accessibility, privacy, and pedagogy concerns are addressed.
- [ ] Decision, prompt, evaluation, run, and memory impacts are recorded or explicitly marked not applicable.
- [ ] The change is readable by an agent with no outside context.
