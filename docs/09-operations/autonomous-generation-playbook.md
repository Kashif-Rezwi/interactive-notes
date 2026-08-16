# Playbook: Autonomous Lesson Generation

**Status:** Approved  
**Owner:** Repository maintainer (Coordinator / Creator / Reviewer composite)  
**Trigger:** User provides a source note document and requests interactive note creation.  
**Last exercised:** 2026-08-14 (Initial playbook release under ADR-0012)  
**Related policies/ADRs:** [ADR-0004](../adr/0004-lesson-standard-adoption.md), [ADR-0006](../adr/0006-record-iteration-accounting.md), [ADR-0009](../adr/0009-forced-adversarial-re-examination-gate.md), [ADR-0010](../adr/0010-rendered-output-verification.md), [ADR-0011](../adr/0011-benchmark-definition-and-artifact-change-protocol.md), [ADR-0012](../adr/0012-autonomous-pipeline-orchestration.md)

## Purpose, scope, and non-goals

- **Purpose:** Provide an end-to-end operational procedure for an AI agent to execute the complete lesson generation workflow autonomously with zero intermediate human touches.
- **Scope:** Covers P0 Intake through P6 Closure, including planning records, HTML candidate build, mechanical checking, six QA audits, adversarial gate, rendered browser verification, self-correction, and evaluation.
- **Non-goals:** Public release authorization (outputs remain `private-pilot-complete`); runtime infrastructure development; model gateway deployment.

## Roles and approval authority

- **Coordinator:** Coordinates P0 intake, allocates sequential IDs, creates run ledger, manages lifecycle.
- **Creator (Parser, Teacher, Planner, Generator):** Authors CM, LP, XS records; generates candidate HTML.
- **Reviewer:** Conducts Six Audits, Adversarial Re-examination, and completes EVAL scorecard.
- **Human Accountable Owner:** Retains authority over public release and unresolvable escalation cases.

## Preconditions and inputs

- An authorized source file exists (e.g. `.ipynb`, `.md`, `.txt`, `.pdf`).
- Repository environment is clean (`python3 scripts/check-repo.py` exits 0).
- Discoverable agent skill is loaded (`.agents/skills/generate-lesson/SKILL.md`).

## Procedure

1. **Intake & Hashing (P0):**
   - Calculate SHA-256 hash of the input source.
   - Allocate sequential IDs (`SRC`, `CM`, `LP`, `XS`, `RUN`, `CAN`, `EVAL`).
   - Create `records/sources/src-...` and `records/runs/run-...` (Status: `Generating`).
2. **Concept Modeling (P1):**
   - Ingest source; extract atomic claims, prerequisites, misconceptions, and dispositions.
   - Author `records/concepts/cm-...` and verify CM conformance checklist.
3. **Learning Design (P2):**
   - Author `records/plans/lp-...` ordering concepts by pedagogy (explain-before-use).
   - Complete the mandatory depth-pass table (ledes, visuals, reveal arcs, callouts, ladders, explain items).
   - Verify LP conformance checklist.
4. **Experience Specification (P3):**
   - Author `records/specifications/xs-...` detailing widget variables, bounds, gates, and glossary shape.
   - Verify XS conformance checklist.
5. **Candidate Generation & Mechanical Check (P4):**
   - Generate candidate HTML using `prm-generator-lesson-standard@0.4.0` with full provenance header and standard colophon.
   - Store full prompt snapshot in RUN appendix.
   - Execute `python3 scripts/verify-candidate.py content/<course>/<module>/generated/<note-slug>-v<N>.html`.
6. **Six Audits & Adversarial Gate (P5):**
   - Execute Audits 1–5 per `library/rubrics/lesson-qa-checklist.md`.
   - Execute Audit 6 (Rendered-output verification via browser tools or recorded degraded mode).
   - Execute Mandatory Adversarial Re-Examination Gate ([ADR-0009](../adr/0009-forced-adversarial-re-examination-gate.md)).
   - If defects found: trigger self-correction loop (max 2 revision cycles).
7. **Evaluation & Closure (P6):**
   - Score the 10 rubric dimensions in `records/evaluations/eval-...`.
   - Close `records/runs/run-...` (Status: `Pilot complete`).
   - Update module README reference table.
   - Execute `python3 scripts/check-repo.py` to confirm repository hygiene (0 errors).
   - Deliver final summary walkthrough to user.

## Decision points and quality checks

- **CM/LP/XS Conformance Check:** Non-conformance halts progression before generation.
- **Candidate Mechanical Check:** `verify-candidate.py` must exit 0 before proceeding to audits.
- **Adversarial Gate:** Discovered defects must route to `revising` with incremented `revision_cycles`.
- **Repo Hygiene Check:** `check-repo.py` must exit 0 at closure.

## Evidence and records to create

- Source Record (`records/sources/src-...`)
- Concept Model (`records/concepts/cm-...`)
- Learning Plan (`records/plans/lp-...`)
- Experience Spec (`records/specifications/xs-...`)
- Candidate HTML (`content/.../generated/<note-slug>-v<N>.html`)
- Run Ledger (`records/runs/run-...`)
- Evaluation Report (`records/evaluations/eval-...`)

## Budget, failure modes, and escalation

- **Self-Correction Budget:** Maximum 2 revision cycles. If defects persist after 2 cycles, halt run, record status `Needs Human Review`, and present diagnostic.
- **Token Budget:** If source document exceeds ~50 concepts, split into multiple class packages under the module.
- **Degraded Browser Mode:** If browser automation tools are unavailable, perform handler-level simulation, document limitation in EVAL, and cap Visual/UX/Technical scores at 2.5 per framework rules.

## Exit criteria and retrospective questions

- **Exit criteria:** Candidate and all 6 records written to disk; `verify-candidate.py` exits 0; `check-repo.py` exits 0; EVAL scorecard completed; user presented with summary.
- **Retrospective questions:**
  1. Did the candidate require any manual interventions?
  2. Were any unexpected defect classes intercepted by the adversarial gate?
  3. Did prompt snapshot and full audit traces persist in-repo without session leakage?
