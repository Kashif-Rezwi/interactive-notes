# EXP-2026-0002: Workflow Improvement Reproduction Experiment Plan

**Status:** Planned  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision this informs:** Acceptance validation of Tier 1 and Tier 2 workflow improvements (ADR-0009, ADR-0010, ADR-0011, depth-calibration contract).  
**Budget and end date:** 1 governed generation run on frozen evaluation set; execution target: scheduled following audit-phase close.

---

## Hypothesis

Executing a full generation run on the frozen evaluation set (SRC-2026-0001) under the improved workflow — with [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) in context, the [depth-calibration contract](../../docs/01-product/depth-calibration-contract.md) enforced upstream, [ADR-0010](../../docs/adr/0010-rendered-output-verification.md) Audit 6 rendered verification, [ADR-0009](../../docs/adr/0009-forced-adversarial-re-examination-gate.md) adversarial re-examination, and full in-repo prompt snapshots — will produce a candidate that:
1. Re-verifies all 11 depth-calibration contract targets with documented element evidence.
2. Provides the first browser-rendered visual evidence (screenshots at $\ge 320\text{px}$, console log capture, interaction traces).
3. Intercepts dynamic/behavioral defects via the mandatory adversarial gate.
4. Scores $\ge 3.70$ weighted under operational rubric anchors with full execution evidence.

---

## Baseline and Treatment

- **Baseline A (Benchmark):** V4 (CAN-2026-0003, RUN-20260810-0001, EVAL-2026-0002) — 178 KB, rich depth produced via unpersisted brief + manual Revision 1; no rendered browser evidence.
- **Baseline B (Pre-improvement baseline):** V6 (CAN-2026-0005, RUN-20260813-0002, EVAL-2026-0004) — 170 KB, 3.76 weighted score; 0 revision cycles; no browser-rendered evidence; self-certified audits.
- **Treatment:** New candidate (v7) generated on SRC-2026-0001 through the complete improved workflow (P0–P6) incorporating all findings WF-001 through WF-015.

---

## Variables Held Constant

- **Source:** [SRC-2026-0001](../../records/sources/src-2026-0001-aiml-4-module-02.md) (AIML-4 Module 2, frozen).
- **Prompt Card:** [PRM-generator-lesson-standard@0.4.0.md](../../library/prompts/prm-generator-lesson-standard@0.4.0.md) (recorded as "no card change needed").
- **Operator:** Solo-maintainer operating profile.
- **Primary Variable:** The governed workflow structure (Audit 6 rendered verification + mandatory adversarial re-examination gate + prompt persistence + execution evidence + benchmark in context).

---

## Benchmark/Cases and Evaluation Plan

- Complete intake and confirm benchmark [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) in context.
- Author conforming CM, LP, and XS verified against [depth-calibration-contract.md](../../docs/01-product/depth-calibration-contract.md).
- Generate candidate and persist full prompt snapshot in-repo (WF-001, WF-015).
- Execute Audits 1–6 with recorded execution evidence and browser screenshots at $\ge 320\text{px}$, $640\text{px}$, $1024\text{px}$ (WF-006, WF-008).
- Execute adversarial re-examination gate; route to revision if defects are surfaced (WF-003).
- Execute standing re-verification pass sampling headline claims (WF-008).
- Score against operational Stage 1 dimension anchors (WF-007).

---

## Success and Regression Thresholds

- **Success:**
  - Weighted score $\ge 3.70$, all hard gates $\ge 3.5$.
  - Rendered output verification clean with zero console errors and body font $\ge 16\text{px}$ across all breakpoints.
  - Adversarial re-examination executed with documented methods and covered elements.
  - All prompt and audit outputs persisted in-repo.
- **Regression:**
  - Any failure of the 11 depth-calibration contract targets.
  - Unhandled layout clipping or responsive overflow at 320px.

---

## Results and Uncertainty

*Experiment is in Planned status; ready for execution when scheduled.*

---

## Decision and Follow-up

To be recorded upon run execution and evaluation.

---

## Memory Disposition

To be recorded upon run execution and evaluation.
