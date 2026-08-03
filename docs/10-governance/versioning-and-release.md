# Versioning and Release Strategy

## Versioned surfaces

Version independently: source packages, concept models, plans/specifications, prompts, rubrics, agent contracts, playbooks, benchmarks, workflow definitions, artifacts, and the repository release. A run pins all consumed versions.

## Semantic versions

Use `major.minor.patch` where consumers need compatibility guarantees:

- **Major:** incompatible contract, policy, or meaning change.
- **Minor:** backward-compatible capability or approved guidance addition.
- **Patch:** correction that preserves contract and intended behavior.

Records retain immutable IDs and revisions; documents use Git history plus visible status/changelog where impact is material. Never relabel a prior version to hide changed behavior.

## Release classes

| Class | Examples | Minimum approval |
| --- | --- | --- |
| Documentation release | Clarified standard or navigation | Documentation Manager + peer review |
| Operational release | Prompt, rubric, playbook, agent role change | Owner, evaluator evidence, affected specialists |
| Artifact release | Learner-facing lesson/asset | Required reviewers + release steward + human owner |
| Architecture release | New durable boundary, data policy, vendor commitment | ADR + human architecture approval |

## Release packet

A release contains scope, linked changes, version impacts, benchmark/evaluation evidence, accessibility/factual/risk status, known limitations, migration notes, rollback or correction plan, release owner, and follow-up review date. A release is a decision, not a merge event.
