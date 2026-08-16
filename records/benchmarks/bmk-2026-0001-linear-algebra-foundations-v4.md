# BMK-2026-0001: Linear Algebra Foundations Benchmark Definition (CAN-2026-0003)

**Status:** Active  
**Date registered:** 2026-08-14  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Governing ADR:** [ADR-0011](../../docs/adr/0011-benchmark-definition-and-artifact-change-protocol.md)  
**Target family:** AIML-4 Module 2 (Math & Statistics for ML — Linear Algebra Foundations)  
**Candidate ID:** CAN-2026-0003  
**Artifact file:** [linear-algebra-foundations-v4.html](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v4.html)  
**Current SHA-256:** `b35c622e5a40a830b50aa22e705b6305a415feae76a60d65b16999a4c0fa1590`  
**Byte size:** 178,020 bytes  
**Primary generation run:** [RUN-20260810-0001](../../records/runs/run-20260810-0001-linear-algebra-foundations-v4.md)  
**Primary evaluation:** [EVAL-2026-0002](../../records/evaluations/eval-2026-0002-linear-algebra-foundations-v4.md)  

---

## 1. Benchmark Purpose and Authority

BMK-2026-0001 is the single authoritative benchmark representing reference quality for the AIML-4 Module 2 lesson lineage. It defines the depth, interactive rigor, assessment design, and pedagogical scaffolding that subsequent generation runs must calibrate against.

Per [ADR-0011](../../docs/adr/0011-benchmark-definition-and-artifact-change-protocol.md), this definition replaces previous divergent "reference implementation" and "reference lesson" designations.

---

## 2. Reconstructed Generation Intent (WF-001)

> [!NOTE]
> **Provenance declaration:** The full text of the owner's original 30-section generation brief (digest `f1a43cbf21cf`) was not preserved in-repo at generation time (WF-001). The statement below is a curated **authoritative reconstruction** derived from surviving records ([RUN-20260810-0001](../../records/runs/run-20260810-0001-linear-algebra-foundations-v4.md) Appendix A, [EVAL-2026-0002](../../records/evaluations/eval-2026-0002-linear-algebra-foundations-v4.md), [LP-2026-0002](../../records/plans/lp-2026-0002-linear-algebra-foundations.md), and [MEM-2026-0003](../../records/memory/mem-2026-0003-standing-audit-gates.md)).

### Reconstructed Core Instructions

1. **Comparative Redesign:** Overcome the passive, recognition-only flaws of prior variants (v1–v3) by investing the complexity budget into assessment, scaffolding, and interactive causal understanding rather than decorative visuals.
2. **Pedagogical Sequence:**
   - Orientation Unit (U0) teaching how to learn with the page (loop table, label legend, branched concept map).
   - Units U1–U9 following the canonical anatomy: Learn (intuition first, worked numeric example) → Predict (committed choice) → Explore (goal-directed manipulation) → Practice (faded scaffolding) → Check (constructed response) → Connect (ML mechanisms).
   - Synthesis + interleaved mastery assessment + localStorage review list + glossary.
3. **Assessment & Scaffolding Standards:**
   - One full faded ladder (worked → completion → independent) with tiered hints for each computational skill.
   - Prediction gates that hide the manipulable until commitment is made and provide rule-re-deriving feedback.
   - Constructed response (numeric entry with tolerance or self-graded explain-in-own-words) in every unit check; strictly avoid recognition-only multiple choice.
   - Interleaved mastery items with 3-level confidence calibration (`sure` / `think so` / `guessing`) and routing of confident misses to the review list.
4. **Interactive & Visual Standards:**
   - 12 goal-directed manipulable widgets with live-computed mathematical invariants (no hard-coded outcomes).
   - Aspect-preserving canvas data windows with bounds guards and autoscale.
   - WCAG AA measured contrast, `prefers-reduced-motion` support, and default-state print fallbacks.

---

## 3. Measured Characteristics Inventory (WF-005)

Directly measured and verified against `linear-algebra-foundations-v4.html` (EVAL-2026-0002, EVAL-2026-0005, and 2026-08-14 audit):

| Characteristic | Measured Value | Verification Method |
| --- | --- | --- |
| File size / lines | 178,020 bytes / 1,772 lines | File inspection |
| Content units | 10 (Orientation U0 + Units U1–U9) | Source inspection |
| Interactive widgets | 13 (12 manipulable canvases + 1 term matching) | Element scan |
| Prediction gates | 3 (`data-gate="lc|dp|pj"`, commitment hiding) | Handler audit |
| Faded ladders | 4 (Σ-notation, vector norm, dot product, projection) | Structural scan |
| Assessment items | 9 unit checks + 10 interleaved mastery items | DOM inspection |
| Constructed response | Present in all 9 unit checks (numeric / fill / explain) | Per-unit audit |
| Mastery confidence UI | 10 items × 3-level confidence + routing to review list | Handler simulation |
| Glossary entries | 39 entries with 6-field structured data (post-R11) | Data structure audit |
| Concept map | 18 nodes, branched graph with dependencies, closing revisit | SVG/DOM inspection |
| Reveal arcs | $w^T x$ setup in U2, full derivation payoff in U5 | Text dependency pass |
| Mathematical recomputations | 44 distinct values independently verified | Scripted recomputation |
| Worst measured contrast | 4.86:1 (meets WCAG AA 4.5:1 requirement) | Scripted contrast audit |
| Offline / Dependencies | 0 external requests, single self-contained HTML file | Security / network scan |

---

## 4. Known Limitations and Non-Magical Traits

The benchmark exhibits known limitations documented in the audit:
1. **Sub-breakpoint font size:** At viewport width $\le 640\text{px}$, CSS line 186 sets `body { font-size: 15.5px; }`, falling slightly below the standard's $16\text{px}$ hard floor.
2. **Binary gate feedback:** Gate feedback differentiates correct vs incorrect commitments (`data-ok` / `data-no`), but does not provide the distinct per-option feedback branches ($GATES[g].fb[choice]$) introduced in V6.
3. **Pre-revision scoring:** The initial scorecard (weighted 3.59) evaluated the pre-revision build; the shipped artifact's benchmark quality relies on the 15 repairs in Revision 1.
4. **No rendered browser pass:** Like all candidates prior to ADR-0010, the benchmark had no browser-rendered execution evidence recorded at evaluation time.

---

## 5. Post-Evaluation Mutation History (WF-009)

The artifact's hash (`b35c622e…1590`) represents the cumulative result of governed generation, Revision 1, and three controlled owner edits:
1. **2026-08-10 (RUN-20260810-0001 Revision 1):** 15 repairs (R1–R15: matrix product dependency, confidence routing, angle arc, no-JS safety, glossaries).
2. **2026-08-11 (Commit `2ee0f38`):** Clarifying edits and un-gating of exploratory widgets (+75 / -29 lines; append-only record note).
3. **2026-08-13 (Commit `5da2754`):** Standard colophon added to footer (append-only record note).
4. **2026-08-13 (Commit `27de79e`):** Visible governance banner removed; metadata moved to HTML header comment (append-only record note).

---

## 6. Context-Assembly Policy (P1–P4)

Per [ADR-0011](../../docs/adr/0011-benchmark-definition-and-artifact-change-protocol.md):
- P2 (Learning design) and P3 (Experience design) MUST consume this benchmark definition as the calibration exemplar for depth, widget richness, and assessment design.
- Deliberate exclusion of this benchmark from generation context is permitted ONLY when executing a documented experiment (such as testing prompt generalization), and MUST be formally recorded in the run manifest with rationale.
