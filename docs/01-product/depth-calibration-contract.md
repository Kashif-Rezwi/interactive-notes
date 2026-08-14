# Depth-Calibration Contract (Interactive Lessons)

**Status:** Experimental  
**Date:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Governing Standard:** [lesson-standard.md](lesson-standard.md)  
**Applies to:** Concept models (CM), learning plans (LP), experience specifications (XS), generation runs (P4), and verification audits (P5).

---

## 1. Purpose and Philosophy

The depth-calibration contract defines the concrete, measurable depth floor required for any governed lesson. As diagnosed in [comprehensive-workflow-and-benchmark-audit.md](../audit/comprehensive-workflow-and-benchmark-audit.md) (WF-002, WF-004, RC-1), encoding *rules* without encoding *calibration* causes the pipeline to converge on a "compliant minimum" (as seen in V5) that satisfies check boxes while losing the explanatory depth, scaffolding, and interactive rigor of the benchmark.

### Nature of the Depth Bar: Rule-Based Floor

The depth criteria below constitute a **rule-based floor**, not a benchmark-relative moving target.
- A candidate that satisfies every item in this contract meets the required Stage 1 depth baseline (scoring 3.0+ on relevant dimensions).
- A candidate that falls below any floor item is **non-conformant** and must be caught upstream (in CM/LP/XS review) or rejected in Audit 4 (Pedagogical Verification).
- The active benchmark ([BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md)) serves as the concrete exemplar illustrating how these floors are realized in practice.

---

## 2. Measurable Per-Lesson Target Contract

Every governed lesson must satisfy the following eleven measurable criteria:

| # | Contract Target | Measurable Specification | Verification Check |
| --- | --- | --- | --- |
| 1 | **Unit Lede + Intuition First** | Every teaching unit begins with a single-sentence lede naming concept & purpose, followed by concrete real-world intuition and a worked numeric example *before* any interactive widget. | Audit 4 (Depth bar) |
| 2 | **Faded Ladder per Computational Skill** | Every distinct computational skill identified in the Learning Plan receives its own full 3-rung faded ladder (Worked Example → Completion Problem → Independent Problem) with tiered, never-auto-opening hints. | Audit 4 (XS conformance) |
| 3 | **Constructed-Response Unit Checks** | Every unit check includes $\ge 1$ constructed-response item (numeric input with tolerance, fill-in-the-blank equation, or explain-in-own-words with model answer). Zero units may be recognition-only multiple choice. | Audit 4 (Per-unit check) |
| 4 | **Explain-in-Own-Words Items** | At least 2 explain-in-own-words items across the lesson with honest, self-evaluated model answer reveals. | Audit 4 (Mastery check) |
| 5 | **Interleaved Mastery & Confidence** | Mastery assessment is sized at $\approx \text{content units} + 2$ items, interleaved across units, includes reasoning + transfer + error-detection items, uses 3-level confidence tags (`sure`/`think so`/`guessing`), and routes confident misses to review. | Audit 4 & Audit 5 (Behavioral sim) |
| 6 | **Misconception Alert Callouts** | Every misconception identified in the CM/LP receives both an assessment distractor and a dedicated, visible alert callout in the unit text. | Audit 4 (Misconceptions) |
| 7 | **Goal-Directed Manipulable Widgets** | Every widget badged `Explore` has $\ge 1$ learner-manipulable variable and a stated goal strip ("🎯 Goal: …"). Zero-input widgets must be explicitly labeled static demonstrations. | Audit 4 (Widget manipulability) |
| 8 | **High-Fidelity Prediction Gates** | Prediction gates hide the manipulable until commitment is confirmed; reveal feedback differentiates by the chosen option and reinforces the governing rule. | Audit 4 (Gate fidelity) |
| 9 | **Bounded & Autoscaling Canvases** | All canvas widgets restrict coordinate inputs via sliders, min/max bounds, or autoscale transforms so no learner action can render elements off-canvas. | Audit 2 (Canvas extrema) |
| 10 | **6-Field Structured Glossary** | Glossary covers every technical term used in the lesson. Every entry contains all 6 required fields: simple definition, precise definition, intuition, example, related terms, and practical/ML application. | Audit 4 (Glossary shape) |
| 11 | **Branched Dependency Concept Map** | Concept map is a multi-branch dependency graph showing causal prerequisite relationships (not a linear sequence strip of unit titles) and is explicitly revisited at lesson close. | Audit 4 (Concept map) |

---

## 3. Upstream Enforcement Across Stages (WF-004)

Upstream records bound downstream generation depth. To prevent thin upstream plans from starving generation:

### Stage P1 — Concept Model (CM) Floor
- **Claim density:** Minimum 1 anchored atomic claim per concept (typically $\ge 25$ claims for a full lesson).
- **Prerequisites:** Complete dependency graph with all use-before-define gaps flagged.
- **Misconceptions:** Minimum 1 diagnosed misconception per major concept with explicit wrong-answer definitions.

### Stage P2 — Learning Plan (LP) Floor
- **Mandatory Depth Pass Table:** Must declare per unit: (1) lede, (2) signature visual, (3) reveal arcs with payoff units named, (4) misconception callouts, and (5) faded ladders for each computational skill.
- **Explain Items:** Explicitly allocate the $\ge 2$ explain-in-own-words items.
- **Benchmark Reference:** Cite [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) as calibration exemplar or document exclusion rationale.

### Stage P3 — Experience Specification (XS) Conformance Contract
- **Widget contract:** Declare manipulable variable(s), bounds, autoscale method, and text equivalent for every widget.
- **Glossary term set:** Exhaustive list of all terms from the CM to be defined in the 6-field glossary.
- **Concept map edges:** Full node and directed edge list for the dependency graph.

---

## 4. Contract Validation Evidence

- **Negative Validation (CM-2026-0002 / V5):** Evaluated against this contract, CM-2026-0002 (38 lines, ~13 claims, no misconception definitions) is immediately caught as **non-conformant**, preventing the thin handoff that caused V5's compliant-minimum collapse.
- **Positive Validation (CM-2026-0003 / LP-2026-0004 / V6):** CM-2026-0003 (151 lines, 40 anchored claims, 15 distractor-ready misconceptions) and LP-2026-0004 (83 lines, complete depth pass table) conform to this contract and successfully produced reference-band depth in CAN-2026-0005.
