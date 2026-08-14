# ADR-0012: Authorize bounded autonomous pipeline orchestration

**Status:** Accepted  
**Date:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Stage 2 workflow automation, agent skill architecture, verification tooling  
**Supersedes / superseded by:** none

## Context and problem

The Learning OS roadmap ([docs/11-roadmap/roadmap.md](../11-roadmap/roadmap.md)) designates Stage 1 as manual governed pilots and Stage 2 as reproducible workflow automation. Through four completed end-to-end pilots (V1–V3 cross-model exploration, V4 governed benchmark, V5 regeneration test, V6 comparison run), the quality loop, evaluation rubrics, depth calibration contract, and adversarial audit gates have stabilized.

However, operating the full P0–P6 lesson-generation workflow manually requires extensive operator coordination across multiple discrete handoffs (intake, concept modeling, learning plan, experience spec, generation prompt assembly, six QA audits, adversarial re-examination, evaluation scoring, run closure, memory curation). This manual friction limits throughput and increases the risk of ad-hoc omissions.

A "zero-touch" autonomous generation pipeline—where an operator provides only a source note and a trigger prompt, with the agent autonomously executing P0 through P6 and self-correcting—requires explicit architectural authorization to ensure governance invariants, human accountability, and bounded failure containment are maintained.

## Decision

1. **Authorize bounded autonomous orchestration.** An AI agent may execute P0 through P6 of the lesson-generation workflow autonomously within a single execution session, provided all governing contracts (source intake, CM, LP, XS, RUN, EVAL, QA checklist, adversarial gate, persistence checklist) are authored and verified in-repo.
2. **Skill-as-orchestrator architecture.** The orchestration logic is implemented as a versioned agent Skill (`.agents/skills/generate-lesson/SKILL.md`) following the Antigravity skill conventions, supported by an orchestration prompt card ([library/prompts/prm-orchestrator-autonomous@0.1.0.md](../../library/prompts/prm-orchestrator-autonomous@0.1.0.md)). The skill contains no runtime application code; it provides structured, sequential operational instructions directly to the agent.
3. **Extend repository verification tooling.** Authorize `scripts/verify-candidate.py` as read-only, offline, zero-dependency repository tooling under the same precedent established by [ADR-0008](0008-repository-checker-tooling.md). It verifies mechanical HTML invariants (well-formedness, duplicate IDs, zero external dependencies, provenance header, standard colophon, data-attribute wiring, glossary structure, and element metrics).
4. **Enforce a self-correction budget.** Autonomous repair loops during P5 (six audits and adversarial re-examination) are capped at a maximum of 2 revision cycles per run (`revision_cycles <= 2`). If defects persist after 2 cycles, the pipeline must halt, persist a diagnostic report, and escalate to the human owner.
5. **Preserve human accountability and release boundaries.** All autonomous outputs are designated `private-pilot-complete` under the Stage 1/2 non-independent review rule ([ADR-0003](0003-stage-1-pilot-evidence-and-gate-semantics.md)). Public release remains an exclusive human decision. The orchestrator cannot silently overrule rubrics, waive policy gates, or modify approved prompt cards, benchmark definitions, or release policies.

## Decision drivers

- **Principle 3 (Plan before generation)** and **Principle 7 (Explicit contracts):** The autonomous orchestrator must produce every intermediate record (CM, LP, XS) before generating code, ensuring full auditability.
- **Principle 4 (Evaluate before retrying):** Self-correction must target observed checklist and adversarial defects, never unguided variation.
- **Principle 12 (Earn complexity):** Implementing orchestration via agent instructions (Skills) and lightweight read-only scripts avoids premature commitments to workflow engines, backend daemons, or heavy dependencies.
- **Invariant 3 (Human accountability):** Human retains authority over release decisions and escalation triggers.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Continue manual stage-by-stage execution | Zero new tooling | High operator time (4+ hours per lesson); prone to missed steps | Rejected as sole operating mode; preserved as manual fallback |
| B. External CI/CD / containerized workflow engine | Rigid determinism | Heavy external dependency, premature framework commitment, violates charter non-goals | Rejected |
| C. Skill-as-orchestrator with read-only verification tooling (chosen) | Zero runtime dependencies; native agent discovery; fully auditable; preserves all governance contracts | Relies on LLM reasoning discipline; requires self-correction budget cap | Selected |

## Consequences

- **Positive:** Enables end-to-end lesson generation from raw notes with a single prompt; enforces consistent execution of all six audits, the adversarial gate, and in-repo persistence.
- **Operational:** Introduces `.agents/skills/generate-lesson/` to the repository map; adds `scripts/verify-candidate.py` as companion maintenance tooling.
- **Safety / Containment:** Bounded revision cycles prevent runaway token consumption or infinite repair loops.
- **Reversibility:** Fully reversible. The skill and script can be removed without affecting underlying governance standards or existing candidate lineage.

## Evidence and validation

- **Tooling precedent:** [ADR-0008](0008-repository-checker-tooling.md) established the validity of zero-dependency Python verification scripts for repository governance.
- **Workflow maturity:** The six-audit suite and adversarial gate ([ADR-0009](0009-forced-adversarial-re-examination-gate.md), [ADR-0010](0010-rendered-output-verification.md)) provide clear, programmatic pass/fail criteria that an agent can evaluate autonomously.
- **Validation:** Exercised via candidate verification against historical candidates (`linear-algebra-foundations-v6.html`) and execution of autonomous generation runs under `EXP-2026-0002`.

## Rollback or migration plan

Supersede this ADR, remove `.agents/skills/generate-lesson/` and `scripts/verify-candidate.py`, and revert to manual pilot coordination per [docs/04-agents/stage-1-operating-profile.md](../04-agents/stage-1-operating-profile.md).

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-14 under the Stage 1/Stage 2 transitional governance path. Inspected: ADR text, Skill specification, verification script requirements, and self-correction bounds. Decision: accept. Limitation: non-independent self-review recorded per review policy.

## Review trigger/date

Review upon completion of three autonomous generation runs, upon major prompt architecture revision, or by 2026-11-04, whichever comes first.
