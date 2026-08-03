# Learning OS

Learning OS is the documentation-first operating system for a future AI-native platform that turns technical source material into rigorous, beautiful, interactive learning experiences.

This repository is deliberately **not the application**. It is the durable source of truth that tells humans and AI coding agents what to build, why it matters, how work is performed, how quality is measured, and how lessons learned become reusable knowledge. No production implementation belongs here until the foundation documents explicitly authorize it.

## Start here

1. Read [the charter](docs/00-foundation/charter.md), [principles](docs/00-foundation/principles.md), and [glossary](docs/00-foundation/glossary.md).
2. Read [the repository map](docs/02-system/repository-map.md) and [system blueprint](docs/02-system/system-blueprint.md).
3. Follow [the agent protocol](docs/04-agents/coordination-protocol.md) and the role card relevant to your work.
4. Use the [quality loop](docs/03-workflows/quality-loop.md) for every generation or design decision.
5. Record decisions, evaluations, run evidence, and reusable lessons using [templates](templates/README.md).

## Repository contract

- Documentation precedes implementation; a proposed code change needs a linked decision, contract, and acceptance criteria.
- AI agents are first-class contributors, but high-impact decisions remain reviewable by humans.
- Claims, scores, outputs, and decisions must be traceable to their evidence.
- The `AIML-4/` directory is pre-existing reference material. It is not part of this operating manual and must not be silently rewritten.
- This foundation contains no application code, web pages, APIs, CLI commands, or runtime configuration.

## Navigation

| Need | Read |
| --- | --- |
| Product intent and limits | [Product brief](docs/01-product/product-brief.md) |
| Future system boundaries and data lineage | [System blueprint](docs/02-system/system-blueprint.md) |
| End-to-end quality process | [Workflow architecture](docs/03-workflows/workflow-architecture.md) |
| Agent roles and handoffs | [Agent catalog](docs/04-agents/agent-catalog.md) |
| Prompt lifecycle | [Prompt architecture](docs/05-prompts/prompt-architecture.md) |
| Scoring and benchmarks | [Evaluation framework](docs/06-evaluation/evaluation-framework.md) |
| Long-term learning | [Memory architecture](docs/07-memory/memory-architecture.md) |
| Run provenance and observability | [Logging architecture](docs/08-observability/logging-architecture.md) |
| Repeatable operations | [Playbooks](docs/09-operations/playbooks.md) |
| Standards and releases | [Governance](docs/10-governance/README.md) |
| Risks, questions, and staged evolution | [Roadmap](docs/11-roadmap/README.md) |

## Maturity path

The repository progresses through explicit gates: documentation foundation, manually operated workflow, reproducible automation, developer tooling, product implementation, and platform governance. The authoritative sequence is in [the roadmap](docs/11-roadmap/roadmap.md).

## Contributions

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before changing this repository. A contribution is complete only when its documentation, decision record, evaluation impact, and knowledge capture are complete.
