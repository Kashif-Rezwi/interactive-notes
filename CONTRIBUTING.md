# Contributing to Learning OS

Learning OS is not currently accepting or merging external contributions. This document defines the standard that will apply when a future licensing and inbound-rights decision authorizes them. Maintainer-controlled changes should make future work more understandable, reproducible, or safer.

## Before proposing a change

- Read `AGENTS.md` and the relevant standards under `docs/10-governance/`.
- Search for an existing decision, term, prompt, rubric, lesson, or record before creating a new one.
- State whether the change is a correction, a proposal, an experiment, a policy, or a supersession.

## Contribution types

| Type | Required evidence |
| --- | --- |
| Documentation clarification | Source links and affected readers |
| Architecture proposal | ADR and alternatives considered |
| Prompt change | Versioned prompt card, test set, evaluation delta |
| Evaluation/rubric change | Calibration examples and scorer impact |
| Memory addition | Provenance, confidence, scope, retention rationale |
| Playbook change | Trigger, owner, exit criteria, and dry-run evidence |

## Distribution boundary

No repository-wide reuse license or inbound contribution grant has been adopted. Do not open or expect acceptance of external pull requests, source material, generated artifacts, or third-party content. Owner-authorized public distribution of a specific package does not grant contributors or readers a general right to reuse it. A future licensing decision will define contribution, maintainer-use, and redistribution terms before this pause is lifted.

## Review expectations

Use the reviewer roles in `docs/04-agents/agent-catalog.md`. Educational, accessibility, privacy, or safety implications need their corresponding reviewer. Durable decisions require an ADR and human approval under the review policy.

## Record hygiene

Records are append-only evidence. Correct an accepted record by adding a linked superseding record; do not erase history. Mark personal, restricted, or unlicensed material as such and keep it outside the public corpus.
