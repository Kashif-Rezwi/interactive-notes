# EXP-2026-0001: Cross-Source and Cross-Model Variance Experiment Plan

**Status:** Planned  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision this informs:** De-risking single-source and single-model variance (WF-010, WF-013, WF-014); calibrating generalizability of the depth-calibration contract and workflow improvements.  
**Budget and end date:** 1 generation run per treatment condition; review by 2026-11-04 (or upon arrival of Class 2 source notes, whichever comes first).

---

## Hypothesis

The improved lesson generation workflow (incorporating the [depth-calibration contract](../../docs/01-product/depth-calibration-contract.md), mandatory adversarial re-examination per [ADR-0009](../../docs/adr/0009-forced-adversarial-re-examination-gate.md), and rendered-output verification per [ADR-0010](../../docs/adr/0010-rendered-output-verification.md)) will reliably reproduce benchmark-band depth ($\ge 3.5$ weighted score, all depth floor targets met, zero open Critical/Major defects) when executed on a **novel source package** (AIML-4 Class 2: Probability Basics) or across an **alternative model family**.

---

## Baseline and Treatment

- **Baseline:** V6 (CAN-2026-0005, RUN-20260813-0002) on SRC-2026-0001 (Linear Algebra Foundations) under Claude Opus 4.6 via the Stage 1 operating profile.
- **Treatment Condition A (Cross-Source):** Novel source document (Class 2 notes) processed through full P0–P6 with the improved workflow.
- **Treatment Condition B (Cross-Model):** Same source (SRC-2026-0001) processed through the improved workflow using an alternative frontier model (e.g. Gemini / GPT series).

---

## Variables Held Constant

- **Governing Standard:** [lesson-standard.md](../../docs/01-product/lesson-standard.md) and [depth-calibration-contract.md](../../docs/01-product/depth-calibration-contract.md).
- **Prompt Card:** [PRM-generator-lesson-standard@0.4.0.md](../../library/prompts/prm-generator-lesson-standard@0.4.0.md).
- **Evaluation Rubric:** [evaluation-framework.md](../../docs/06-evaluation/evaluation-framework.md) with operational Stage 1 dimension anchors.
- **Checklist:** [lesson-qa-checklist.md](../../library/rubrics/lesson-qa-checklist.md) (Audits 1–6 + adversarial gate).
- **Operating Profile:** Solo-operator manual execution following [stage-1-operating-profile.md](../../docs/04-agents/stage-1-operating-profile.md).

---

## Benchmark/Cases and Evaluation Plan

1. Execute full P0–P6 pipeline.
2. Execute standing Audits 1–6 including rendered verification in a real browser.
3. Execute mandatory adversarial re-examination gate.
4. Execute re-verification pass sampling $\ge 3$ claims.
5. Score against operational rubric anchors and evaluate depth conformance.

---

## Success and Regression Thresholds

- **Success Threshold:**
  - Weighted evaluation score $\ge 3.50$.
  - All hard gates $\ge 3.5$.
  - All 11 depth-calibration contract targets satisfied with documented evidence.
  - Zero unhandled console errors in Audit 6.
  - Zero open Major/Critical defects post-adversarial re-examination.
- **Regression Threshold:**
  - Any collapse to recognition-only checks in unit assessments.
  - Omission of faded ladders for named computational skills.
  - Any unhandled off-canvas rendering at extrema.

---

## Calibrated Evidence Claim

> [!IMPORTANT]
> **What one success does and does not prove:**
> - A single successful replication on Class 2 proves that the depth-calibration contract and workflow mechanisms generalize beyond the linear algebra domain.
> - It does **not** prove zero-variance execution across all mathematical domains, nor does it replace the multi-source calibration commitment for public release eligibility.

---

## Results and Uncertainty

*Experiment is in Planned status awaiting source delivery for Class 2 or designated model replication window.*

---

## Decision and Follow-up

To be recorded upon experiment conclusion.

---

## Memory Disposition

To be recorded upon experiment conclusion.
