---
name: generate-lesson
description: >
  Autonomously generate a governed interactive HTML lesson from source notes.
  Executes the full P0–P6 lesson-generation workflow with self-correction,
  browser verification, record authoring, and knowledge-system updates. User
  provides only the source file and an optional trigger prompt.
---

# Autonomous Lesson Generation Orchestrator

This skill guides an AI agent to execute the governed **P0–P6 lesson-generation workflow** autonomously in a single session. It enforces all repository governance standards ([docs/01-product/lesson-standard.md](../../../docs/01-product/lesson-standard.md), [docs/01-product/depth-calibration-contract.md](../../../docs/01-product/depth-calibration-contract.md), [docs/03-workflows/lesson-generation-workflow.md](../../../docs/03-workflows/lesson-generation-workflow.md), [ADR-0009](../../../docs/adr/0009-forced-adversarial-re-examination-gate.md), [ADR-0010](../../../docs/adr/0010-rendered-output-verification.md), [ADR-0011](../../../docs/adr/0011-benchmark-definition-and-artifact-change-protocol.md), [ADR-0012](../../../docs/adr/0012-autonomous-pipeline-orchestration.md)).

---

## Operating Invariants & Constraints

1. **Zero-Touch Execution:** The user provides only a source note (any format: `.ipynb`, `.md`, `.txt`, `.pdf`, etc.) and a trigger prompt (e.g. "create interactive notes for this"). The agent proceeds through P0 to P6 without requesting intermediate user approvals.
2. **Private Pilot Output:** All autonomous outputs are designated `private-pilot-complete` under Stage 1/2 non-independent review rules ([ADR-0003](../../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md)).
3. **Budget-Bounded Self-Correction:** The self-correction loop during P5 (six audits + adversarial gate) is capped at a maximum of **2 revision cycles** (`revision_cycles <= 2`). If defects persist after 2 cycles, halt and escalate with a clear diagnostic.
4. **No Silent Drops:** Any concept, widget, or technique specified in the Learning Plan (LP) or Experience Specification (XS) must appear in the candidate at full depth. If something cannot be built, mark it explicitly as an intentional omission with rationale in the records.
5. **Traceability:** Every intermediate record (SRC, CM, LP, XS, RUN, EVAL) must be written to `records/` using the corresponding template in `templates/`.

---

## Autonomous Lifecycle (P0 – P6)

```text
[P0 Intake & Package Setup] ──► [P1 Concept Model (CM)] ──► [P2 Learning Plan (LP)]
             │                                                          │
             ▼                                                          ▼
  [P4 HTML Candidate Build] ◄── [P3 Experience Spec (XS)] ◄─────────────┘
             │
             ▼
  [P5 Audits 1–6 + Adversarial Gate] ──(Defects? Max 2 cycles)──► [Self-Correction Loop]
             │
             ▼ (Passed)
  [P6 Evaluation, Closure & Compounding Updates] ──► [Summary Report to User]
```

---

## Phase-by-Phase Execution Instructions

### Phase 0: Intake and Package Setup (P0)

1. **Source Identification & Hash:**
   - Locate the target source file from the user's prompt.
   - Compute its SHA-256 hash using Python or shell.
2. **Package Structure:**
   - If the source is not already inside `content/<course-slug>/<module-slug>/sources/`, determine appropriate `<course-slug>` and `<module-slug>` and place/link the file per [content-package-convention.md](../../../docs/02-system/content-package-convention.md).
3. **Sequential ID Allocation:**
   - Scan `records/sources/`, `records/concepts/`, `records/plans/`, `records/specifications/`, `records/runs/`, `records/evaluations/` to identify the next sequential IDs:
     - `SRC-YYYY-NNNN`
     - `CM-YYYY-NNNN`
     - `LP-YYYY-NNNN`
     - `XS-YYYY-NNNN`
     - `RUN-YYYYMMDD-NNNN`
     - `CAN-YYYY-NNNN`
     - `EVAL-YYYY-NNNN`
4. **Source Record Authoring:**
   - Create `records/sources/src-YYYY-NNNN-<slug>.md` using [templates/run/generation-run.md](../../../templates/run/generation-run.md) source manifest format, recording the source title, file path, and SHA-256 hash.
5. **Initialize Run Ledger:**
   - Create `records/runs/run-YYYYMMDD-NNNN-<slug>.md` from [templates/run/generation-run.md](../../../templates/run/generation-run.md) in status `Generating`.

---

### Phase 1: Source Understanding (CM Authoring)

1. **Content Inventory:**
   - Read the entire source document.
   - Catalog all topics, formulas, definitions, examples, implicit instructor assumptions, underexplained points, and missing-but-necessary prerequisite concepts.
2. **Concept Model (CM):**
   - Author `records/concepts/cm-YYYY-NNNN-<slug>.md` following [templates/concept/concept-model.md](../../../templates/concept/concept-model.md).
   - Ensure every claim is atomic and anchored to source cells/pages.
   - Include the prerequisite dependency graph, examples, non-examples, and a table of specific beginner misconceptions.
3. **Depth-Calibration Conformance Check:**
   - Verify all items in the CM conformance checklist ([docs/01-product/depth-calibration-contract.md](../../../docs/01-product/depth-calibration-contract.md)).
   - Status: `Reviewed`.

---

### Phase 2: Learning Design (LP Authoring)

1. **Sequence & Pedagogy:**
   - Author `records/plans/lp-YYYY-NNNN-<slug>.md` following [templates/learning/learning-plan.md](../../../templates/learning/learning-plan.md).
   - Organize units by logical conceptual dependency (explain-before-use), NOT source presentation order.
   - Include measurable learning outcomes, additional-knowledge triage (must/should/could/do-not-add), and assessment strategy.
2. **Depth-Pass Table (Mandatory per WF-002 / MEM-2026-0004):**
   - Fill the depth pass table:
     - Per-unit lede (1 sentence explaining intuition & purpose)
     - Signature visual design
     - Reveal arcs (setup unit $\to$ payoff unit)
     - Misconception-alert callouts
     - 1 faded ladder (worked $\to$ completion $\to$ independent) per computational skill
     - Placement of $\ge 2$ explain-in-own-words items
3. **Benchmark Context:**
   - Cite [records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md](../../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) as calibration exemplar.
4. **LP Conformance Check:**
   - Verify all items in the LP conformance checklist.
   - Status: `Reviewed`.

---

### Phase 3: Experience Design (XS Authoring)

1. **Interactive Experience Specification:**
   - Author `records/specifications/xs-YYYY-NNNN-<slug>.md` following [templates/lesson/lesson-specification.md](../../../templates/lesson/lesson-specification.md).
   - Map every unit to canonical anatomy: Learn $\to$ Predict $\to$ Explore $\to$ Practice $\to$ Check $\to$ Connect.
   - Select interaction patterns from [library/patterns/lesson-patterns.md](../../../library/patterns/lesson-patterns.md).
2. **Concrete Variable & Geometry Declarations:**
   - Explicitly declare all manipulable variables, input bounds, autoscaling rules, and text equivalents for every canvas widget.
   - Specify high-fidelity prediction gates (hiding manipulable until commitment; option-specific feedback).
   - Detail the 6-field glossary term list and concept-map branching structure.
3. **XS Conformance Check:**
   - Verify the XS conformance checklist.
   - Status: `Approved`.

---

### Phase 4: Candidate HTML Generation

1. **Prompt Assembly & Candidate Authoring:**
   - Generate the single-file HTML lesson implementing [library/prompts/prm-generator-lesson-standard@0.4.0.md](../../../library/prompts/prm-generator-lesson-standard@0.4.0.md).
   - Embed the governed provenance comment at the very top (Line 1):
     `<!-- candidate: CAN-YYYY-NNNN | model: <ModelName> | date: YYYY-MM-DD | run: RUN-YYYYMMDD-NNNN | source: SRC-YYYY-NNNN | prompt card: prm-generator-lesson-standard@0.4.0 digest <digest> | inputs: CM-YYYY-NNNN / LP-YYYY-NNNN / XS-YYYY-NNNN -->`
   - Include standard colophon (`<footer class="colophon">`) with AI-honesty statement.
   - Save candidate to `content/<course-slug>/<module-slug>/generated/<note-slug>-v<N>.html`.
2. **Full Prompt Snapshot Persistence (WF-001 / WF-015):**
   - Save the fully rendered prompt text into the appendix of `records/runs/run-YYYYMMDD-NNNN-<slug>.md`.
3. **Mechanical Verification:**
   - Run: `python3 scripts/verify-candidate.py content/<course-slug>/<module-slug>/generated/<note-slug>-v<N>.html`
   - If mechanical check fails, fix immediately (counted as in-generation correction per ADR-0006).

---

### Phase 5: Six Audits & Adversarial Gate

Execute all six audits per [library/rubrics/lesson-qa-checklist.md](../../../library/rubrics/lesson-qa-checklist.md):

1. **Audit 1: Coverage Audit** — Map every CM inventory item to lesson section + disposition.
2. **Audit 2: Mathematical Audit** — Scripted / independent recomputation of all values, formulas, and keys.
3. **Audit 3: Dependency Order Audit** — Read-in-order sweep with taught-so-far set.
4. **Audit 4: Pedagogical & Depth Audit** — Check all 11 depth-calibration criteria (ledes, ladders, constructed-response checks, glossary 6-field shape, branched concept map, etc.).
5. **Audit 5: Technical & Behavioral Audit** — Duplicate IDs, contrast, keyboard handling, offline state reset.
6. **Audit 6: Rendered-Output Verification ([ADR-0010](../../../docs/adr/0010-rendered-output-verification.md))** —
   - If browser capability is active (`browser_subagent`):
     - Open `file://<absolute-path-to-candidate.html>`.
     - Confirm 0 console errors.
     - Capture screenshots at $\ge 320\text{px}$, $640\text{px}$, $1024\text{px}$ (confirm font $\ge 16\text{px}$).
     - Execute live interaction traces (widgets, gates, ladders, mastery scoring).
   - If browser is unavailable (degraded mode):
     - Execute rigorous handler-level simulation and record degraded mode note in EVAL (scores capped at 2.5 on Visual/UX/Technical).

**Adversarial Re-Examination Gate ([ADR-0009](../../../docs/adr/0009-forced-adversarial-re-examination-gate.md)):**
- Conduct an adversarial pass independent of initial audit notes:
  - Read-in-order fresh perspective sweep.
  - Handler-level edge cases: gate commitment bypass, grading boundaries, confident-miss routing, reset from corrupted localStorage.
  - Canvas-extrema forcing: zero vectors, collinear vectors, extreme slider values.
  - Honesty / provenance scan: check for unsupported claims or dangling forward promises.

**Self-Correction Logic:**
- If defects are found (Major/Critical):
  - Increment `revision_cycles`.
  - If `revision_cycles > 2`: **HALT**, record diagnostic, and escalate to human.
  - If `revision_cycles <= 2`:
    - If Audits 1–3 fail $\to$ revise CM/LP/XS upstream, then regenerate.
    - If Audits 4–6 / Adversarial fail $\to$ perform targeted code revision.
    - Re-run verification suite and re-audit.

---

### Phase 6: Evaluation, Closure, and Compounding Updates

1. **Score Candidate:**
   - Complete scorecard in `records/evaluations/eval-YYYY-NNNN-<slug>.md` using [templates/evaluation/evaluation-report.md](../../../templates/evaluation/evaluation-report.md) and the 10 weighted dimensions in [docs/06-evaluation/evaluation-framework.md](../../../docs/06-evaluation/evaluation-framework.md).
   - Record `Independence: non-independent` and `Release eligibility: private-pilot-complete`.
2. **Close Run Record:**
   - Update `records/runs/run-YYYYMMDD-NNNN-<slug>.md` status to `Pilot complete` with full iteration accounting (ADR-0006).
   - Record retrospective reflections, forward-looking risk notes (WF-013), and memory disposition.
3. **Update Module README:**
   - Update `content/<course-slug>/<module-slug>/README.md` to link the new reference candidate.
4. **Repository Hygiene Verification:**
   - Run `python3 scripts/check-repo.py`. Must exit 0 with 0 failures.
5. **Persistence Checklist (WF-015):**
   - Verify prompt snapshot, audit evidence, adversarial traces, and evaluation scorecards are stored in-repo.

---

## Final User Summary Format

Upon completing P6, provide a clean, concise summary to the user:

```markdown
# Lesson Generation Complete: [Lesson Title]

- **Candidate:** `content/<course-slug>/<module-slug>/generated/<note-slug>-v<N>.html`
- **Evaluation Score:** [Weighted Score] / 4.0 (Private Pilot Complete)
- **Iteration Accounting:** [N] generation iterations, [N] in-generation corrections, [N] revision cycles
- **Audits & Verification:**
  - verify-candidate.py: PASSED (0 failures)
  - Six QA Audits: PASSED
  - Adversarial Gate (ADR-0009): PASSED
  - Rendered Verification (ADR-0010): PASSED
  - Repository Checker (check-repo.py): PASSED (0 failures)

### Key Records Produced
- Source Record: `records/sources/src-YYYY-NNNN-<slug>.md`
- Concept Model: `records/concepts/cm-YYYY-NNNN-<slug>.md`
- Learning Plan: `records/plans/lp-YYYY-NNNN-<slug>.md`
- Experience Spec: `records/specifications/xs-YYYY-NNNN-<slug>.md`
- Run Ledger: `records/runs/run-YYYYMMDD-NNNN-<slug>.md`
- Evaluation Report: `records/evaluations/eval-YYYY-NNNN-<slug>.md`
```
