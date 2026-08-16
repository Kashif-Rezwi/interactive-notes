# ADR-0010: Adopt rendered-output verification in the lesson evaluation workflow

**Status:** Accepted  
**Date:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Lesson generation workflow (P5 verification audits and evaluation criteria)  
**Supersedes / superseded by:** none

## Context and problem

The comprehensive audit ([comprehensive-workflow-and-benchmark-audit.md](../audit/comprehensive-workflow-and-benchmark-audit.md) WF-006, §14 Unknown #4) identified that every technical verification check in the pipeline's history has operated on source text, static regex/scans, or handler-level DOM/canvas stubs. No governed run has ever recorded browser-rendered evidence for any candidate (v1–v6), including the benchmark.

As a consequence, the pipeline could not detect or exclude rendered-behavior defects:
- Visual clipping, layout overflow, or canvas scaling distortions at responsive breakpoints.
- Runtime JavaScript errors triggered only during live browser execution.
- Sub-breakpoint font degradation (e.g. V4's 15.5px font at ≤640px vs the standard's 16px hard floor).
- Live browser event issues with touch/keyboard interactions and print-media rendering.

Without a rendered-output verification step, the verification ceiling is handler-level logic, leaving learner-visible execution unverified.

## Decision

1. **Adopt Audit 6 (Rendered-Output Verification):** Add a mandatory browser-based rendered verification pass to Phase P5 of the lesson generation workflow.
2. **Required rendered verification criteria:**
   - *Console log audit:* Zero JavaScript console errors and unhandled exceptions on initial page load and throughout all interaction sequences.
   - *Responsive rendering verification:* Visual verification and screenshot capture at standard responsive breakpoints: mobile (≥320px), tablet/phablet (640px), and desktop (1024px+). Confirm that body font size maintains ≥16px at all breakpoints per [lesson-standard.md](../01-product/lesson-standard.md) §10.
   - *Interaction trace verification:* Live browser exercise of all interactive widgets, prediction gates, faded ladders, mastery assessment items, and local storage reset controls.
   - *Canvas extrema visuals:* Driving every manipulable parameter to boundary values in a rendered browser to visually confirm that coordinates, grids, labels, and vectors remain within the canvas boundary and autoscale cleanly.
   - *Print and reduced-motion verification:* Confirming that `@media print` renders each interactive widget's default-state note cleanly, and that `prefers-reduced-motion: reduce` prevents uninitiated animations.
3. **Benchmark baseline measurement:** The active benchmark (BMK-2026-0001) is included in the rendered verification pass to establish the first measured rendered baseline in repository history.
4. **Evidence attachment:** Rendered evidence (browser version, console logs, breakpoint screenshots, trace checklists) must be attached to the evaluation record (EVAL) and summarized in the run ledger (RUN).

## Decision drivers

- Principle 9 (measurable and contestable quality) and Principle 1 (learner trust).
- Audit finding WF-006: eliminating the gap between handler simulation and real-browser rendering.
- V4 defect history: R3 (quadrant angle bug) and R14 (portrait canvas sizing) were rendered-layout defects that bypassed static checks.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Continue handler-level simulation only | Zero tooling / fast execution | Blind to visual clipping, runtime errors, responsive layout breaks | Rejected |
| B. Full automated end-to-end headless browser test suite | Automated CI execution | Requires heavy testing framework and runtime dependencies deferred to Stage 2 | Rejected for Stage 1 |
| C. Protocol-based browser verification with recorded evidence (chosen) | Zero external repo dependencies; captures real browser screenshots and console traces; matches Stage 1 manual pilot profile | Requires manual or environment-assisted browser execution during P5 | Selected |

## Consequences

- Positive: Guarantees that what the learner sees in a real browser has been visually verified and evidenced with screenshots and console captures.
- Operational: Updates `docs/03-workflows/lesson-generation-workflow.md`, `library/rubrics/lesson-qa-checklist.md`, and evaluation templates.
- Rubric impact: Evaluation framework dimension scores for Visual clarity, User experience, and Technical feasibility now require rendered evidence for scores ≥3.0.
- Reversibility: Fully reversible by superseding this ADR.

## Evidence and validation

- Validated on BMK-2026-0001 (V4 baseline) and candidate evaluations in subsequent governed runs.
- Formal validation occurs on the next governed generation run with attached rendered evidence.

## Rollback or migration plan

Supersede this ADR and restore P5 to five audits in the workflow documentation.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-14 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: this ADR, audit finding WF-006, and corresponding checklist additions. Decision: accept. Limitation: non-independent self-review recorded per policy.

## Review trigger/date

Review at the Stage 1 calibration review (three completed pilots) or 2026-11-04, whichever comes first.
