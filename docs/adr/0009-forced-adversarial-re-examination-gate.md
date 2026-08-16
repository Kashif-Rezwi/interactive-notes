# ADR-0009: Adopt the forced adversarial re-examination gate

**Status:** Accepted  
**Date:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Lesson generation workflow (P5/P6 gates and quality-loop state transitions)  
**Supersedes / superseded by:** none

## Context and problem

The audit findings ([comprehensive-workflow-and-benchmark-audit.md](../audit/comprehensive-workflow-and-benchmark-audit.md) WF-003) revealed a critical process gap: benchmark candidate V4 reached reference quality only after *Revision 1*, an owner-requested post-evaluation adversarial audit (scripted structural audit + two isolated adversarial sub-audits + handler-level simulation) that found 3 Major and 11 Minor/nit defects (R1–R15) *after* the artifact had already passed the entire standing verification suite (MEM-2026-0003).

In contrast, V5 (RUN-20260813-0001) and V6 (RUN-20260813-0002) both closed with `revision cycles = 0` because passing P5 audits allowed immediate progression to closure without any adversarial pressure. In V5, this allowed severe defects (hollow gates, recognition-only assessment in two units, linear-strip concept map, unbounded canvas inputs, dangling forward promises) to pass as a "compliant minimum."

Without a forced adversarial gate, the pipeline's stopping condition cannot distinguish "nothing left to find" from "our instruments cannot see it."

## Decision

1. **Mandatory adversarial re-examination gate:** A passing first build may not auto-close a governed run. Every candidate that passes the standing P5 verification audits must undergo a recorded adversarial re-examination before the run transitions from `evaluating` to `reflecting` in the quality loop.
2. **Methodological independence:** The adversarial pass must use methods independent of the initial P5 checks:
   - *Read-in-order dependency re-pass:* A fresh-perspective verification of the taught-so-far set without relying on P5 Audit 3 notes.
   - *Handler-level behavioral simulation of edge cases:* Testing gate commitment refusal/unlock under all branches, quiz grading boundary values, confident-miss routing on radio AND numeric items, and reset from corrupted/divergent states.
   - *Canvas-extrema forcing:* Driving all manipulables to boundary extremes and degenerate values (zero vectors, collinear points, parallel vectors, large numbers) to verify visual bounding and autoscale behavior.
   - *Honesty and provenance scan:* Scanning for unsupported claims, stale or dangling forward promises, uncredited external materials, and missing layer badges or provenance tags.
3. **Evidence bar:** The re-examination must record: (a) methods executed, (b) elements covered, and (c) findings with severity. A clean pass with documented evidence is a valid outcome; an evidence-free pass is a gate failure.
4. **Defect routing:** If defects surface, the run routes to `revising` per the quality loop's retry policy ("fix the plan, not the symptom") with an incremented revision cycle counter per [ADR-0006](0006-record-iteration-accounting.md).

## Decision drivers

- Principle 7 (explicit contracts) and Principle 9 (measurable and contestable quality).
- Audit finding WF-003 and root-cause analyses RC-1 and RC-2: V4's benchmark quality was fundamentally caused by its adversarial revision cycle.
- V4 defect history: R1 (matrix product dependency breach at lesson climax), R2 (dead confidence routing on numeric items), and R3 (quadrant-sensitive angle-arc bug) were all invisible to static syntax and recomputation checks.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Keep optional revision (status quo) | Low operator effort | Demonstrated failure (V5 collapse shipped uncaught with 0 revision cycles) | Rejected |
| B. Mandate fixed revision cycles (e.g. always ≥1 revision) | Forces re-generation | Wasteful churn when an artifact is genuinely defect-free; creates artificial edits | Rejected |
| C. Mandatory adversarial re-examination gate with documented evidence (chosen) | Forces independent scrutiny; permits clean exit if genuinely defect-free with evidence; catches dynamic/behavioral defects | Additional review time before run closure | Selected |

## Consequences

- Positive: Prevents compliant-minimum escapes from silently passing to closure; formalizes the exact practice that created the V4 benchmark.
- Operational: Adds an explicit step to P5/P6 transition in `docs/03-workflows/lesson-generation-workflow.md`, `docs/03-workflows/quality-loop.md`, and `library/rubrics/lesson-qa-checklist.md`.
- Lineage: Run ledgers explicitly record adversarial re-examination evidence and findings.
- Reversibility: Fully reversible by superseding this ADR.

## Evidence and validation

- **Negative validation test (V5):** Walking the V5 record (RUN-20260813-0001) through the adversarial gate intercepts findings F-1 through F-7 (hollow gates, recognition-only checks, dangling promises, unbounded canvases) and prevents closure as `private-pilot-complete` on the initial build.
- **Positive validation test (V4):** The gate's specific methods directly cover and intercept the entire V4 Revision 1 defect set (R1–R15).
- Formal validation occurs on the next governed generation run.

## Rollback or migration plan

Supersede this ADR; update `lesson-generation-workflow.md`, `quality-loop.md`, and `lesson-qa-checklist.md` to remove the mandatory gate requirement.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-14 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: this ADR, audit findings WF-003/RC-1/RC-2, and corresponding workflow/checklist changes. Decision: accept. Limitation: non-independent self-review recorded per policy.

## Review trigger/date

Review at the Stage 1 calibration review (three completed pilots) or 2026-11-04, whichever comes first.
