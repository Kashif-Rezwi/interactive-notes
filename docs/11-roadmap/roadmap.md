# Capability Roadmap

## Stage 0 — Documentation foundation (complete)

**Goal:** establish a complete, agent-readable operating manual.

**Deliverables:** charter, system/workflow/agent architecture, prompt/evaluation/memory/logging strategy, standards, templates, ADR system, playbooks, risks, and open questions.

**Exit gate:** a new agent can independently identify authoritative documents and inherited metadata; create a traceable simulated walkthrough without mistaking it for evidence; explain all release-critical controls; find a source-identity record; and apply the five-profile Stage 1 operating model. Numeric gate authority must be centralized in the evaluation framework. No product code is required.

## Stage 1 — Manual governed pilots (substantially complete, transitioning to Stage 2)

**Goal:** execute the quality loop manually for a small, curated benchmark corpus under the five-profile operating model.

**Deliverables:** populated records, calibration examples, initial prompt cards, benchmark charter, curated memory, and retrospective updates.

**Exit gate:** at least several end-to-end runs are reproducible from records; reviewers agree on rubric interpretation; quality improvements are evidenced rather than anecdotal. Stage 1 remains open in parallel for calibration across additional course domains while Stage 2 automation proceeds.

## Stage 2 — Reproducible workflow automation (in progress)

**Goal:** automate record capture and bounded orchestration without changing the conceptual contracts.

**Deliverables:** machine-readable schemas derived from approved artifact contracts, version-pinned runners, lineage capture, evaluation harness, candidate verification tooling (`scripts/verify-candidate.py`), discoverable agent skills (`.agents/skills/generate-lesson/SKILL.md`), orchestration prompt cards (`prm-orchestrator-autonomous@0.1.0`), and protected record storage. Authorized by [ADR-0012](../adr/0012-autonomous-pipeline-orchestration.md).

**Exit gate:** repeated automated runs recreate equivalent evidence; failure handling and data controls pass review; manual fallback remains possible.

## Stage 3 — Developer tooling and internal studio

**Goal:** make the governed workflow usable by engineers, educators, and reviewers.

**Deliverables:** intake tools, review surfaces, prompt/benchmark registry, workflow visibility, memory retrieval, and operational dashboards.

**Exit gate:** operators can conduct a full lifecycle without undocumented tribal knowledge; role permissions and auditability are verified.

## Stage 4 — Learner artifact platform

**Goal:** implement and validate a limited set of learner-facing artifact families.

**Deliverables:** rendering/runtime architecture, accessibility baseline, analytics consent design, release process, and artifact quality monitoring.

**Exit gate:** released artifacts meet quality gates in real user testing and have correction/rollback mechanisms.

## Stage 5 — Production AI platform

**Goal:** scale multi-tenant, reliable, cost-aware generation and learning operations.

**Deliverables:** tenancy/data governance, model routing, security/compliance controls, service reliability, and experimentation.

**Exit gate:** production SLOs, governance, and incident practice are proven under real workloads.

## Stage 6 — Ecosystem and research stewardship

**Goal:** become a flagship learning infrastructure with transparent benchmarks, extensions, and research partnerships.

**Deliverables:** extension contracts, benchmarks, reproducible research reports, governance council, and long-term archival policy.

**Exit gate:** ecosystem growth does not weaken provenance, accessibility, or accountable decision-making.
