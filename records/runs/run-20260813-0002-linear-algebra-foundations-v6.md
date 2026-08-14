# RUN-20260813-0002: Linear algebra foundations v6 — prompt-card @0.4.0 comparison run

**Status:** Pilot complete<br>
**Parent run:** none (compares against RUN-20260813-0001 outputs)<br>
**Owner:** Repository maintainer<br>
**Objective:** first governed use of prm-generator-lesson-standard@0.4.0 — test its hypothesis that an explicit depth bar + conformance sweep reproduces reference-implementation (CAN-2026-0003) richness in a single governed generation, where @0.3.0 (CAN-2026-0004) collapsed to the compliant minimum (MEM-2026-0004)<br>
**Budget:** one solo-operator session; no external review<br>
**Iteration counts:** generation = 1 ; in-generation corrections = 10 ; revision cycles = 0 (per ADR-0006)<br>
**Classification:** production<br>
**Operating scope:** Stage 1 private pilot<br>
**Review-independence summary:** non-independent (author = reviewer)<br>
**Public-release eligibility:** ineligible (ADR-0003)

## Input manifest

| Input | Identity | Note |
| --- | --- | --- |
| Source | SRC-2026-0001, SHA-256 `23c6f4eb…f94445` (63 markdown cells) | reused per P0; hash re-verified at intake |
| Concept model | [CM-2026-0003](../concepts/cm-2026-0003-linear-algebra-foundations.md) | fresh, template depth floors (40 anchored claims) |
| Learning plan | [LP-2026-0004](../plans/lp-2026-0004-linear-algebra-foundations.md) | fresh, mandatory depth pass per unit |
| Experience spec | [XS-2026-0004](../specifications/xs-2026-0004-linear-algebra-foundations-v6.md) | fresh, element-level conformance contract |
| Prompt card | prm-generator-lesson-standard@0.4.0, SHA-256 digest `b8d8bd93e94f` | first governed use — the comparison run its card awaited |
| Pattern catalog | lesson-patterns.md (2026-08-13 state) | P-01/02/03/04/10/11/12/13/14/15 applied |
| Prior artifacts | v1–v5 | not read during P1–P4 authoring; v4/v5 consulted only at P6 for the comparison table (their depth counts from MEM-2026-0004) |

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-13 | CAN-2026-0005 | Claude (Anthropic) via Cline terminal harness; exact model identifier not exposed | @0.4.0 `b8d8bd93e94f` | one session | none |

P0 intake: source authorization confirmed (SRC record exists, hash re-verified); learner = AIML-4 student, basic algebra + 2-D plotting only; scope = all 63 cells; class ordinal 1; filename `linear-algebra-foundations-v6.html` per `<note-slug>-v<N>`.
P1–P3: CM/LP/XS authored fresh at template depth floors (repairs R1–R3 carried as labeled re-sequencing: independence-before-basis, matrices-before-least-squares, proof-after-dot-product).
P4: single HTML artifact, zero external requests, provenance header comment + standard colophon per @0.4.0; self-verification (item 9) and conformance sweep (item 13) executed in-generation.

**In-generation corrections (10):** (1) W4 lattice heredoc syntax slip (caught on read-back, syntax re-verified); (2) W5 garbled readout sentence; (3) U6 explain-item prompt wording; (4) duplicate id `w8cv` (canvas vs slider-value span — scripted duplicate-ID scan); (5) explain self-grade path never completed unit progress dots (found while designing the behavioral simulation); (6) Lasso/ridge one-line glosses + L1 phrasing (Audit 3 terminology pass); (7) W4 span lattice could render off-canvas at extremes (canvas-extrema check); (8) W5 slider bounds vs autoscale mismatch (same); (9) W12 fitted value drawn unclamped for extreme point sets (same); (10) M5/M12 surfaced as visible alert callouts in addition to gate feedback (XS-conformance sweep).

## Candidate

[`linear-algebra-foundations-v6.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v6.html), SHA-256 `6202f3e9cfbc69075b10019d1fa7265ccf2a0949a2245e244e383e98db5b7dc6`, 170,701 bytes, 1,443 lines, zero external runtime dependencies. Stable identity: CAN-2026-0005 (filename version is display only).

## Verification evidence (P5 five audits)

1. **Coverage:** 63/63 cells dispositioned; matrix ships in [EVAL-2026-0004](../evaluations/eval-2026-0004-linear-algebra-foundations-v6.md) Appendix A. PASS.
2. **Mathematical:** 58/58 independent scripted recomputations PASS (every worked example, ladder rung, widget default incl. W7 θ=45°, gate value 4·3·cos120°=−6, both AB/BA worked pairs, all projection checks, least-squares m=0.9/c=1.0/SSE=0.70, outlier m=1.8/c=−0.5, all mastery keys, rank examples); all widget results computed live (behavioral evidence below); edge guards verified (zero-y projection, zero-vector norms, parallel span, cos clamp, rank degenerates). Canvas extrema: every canvas input-bounded or autoscaling; three overflow defects found and fixed in-generation (7–9 above). PASS.
3. **Dependency order:** read-in-order pass with an empty taught-so-far set; repairs R1–R3 labeled; forward references are promises only and all pay off (ᵀ/ℝⁿ promised U1 → taught U2; norm promised U2 → taught U5; wᵀx promised U2 → paid off U6; (AᵀA)⁻¹ condition promised U8 → closed U9). PASS.
4. **Pedagogical:** anatomy per unit; per-unit constructed response named (U1 numeric+explain, U2–U9 numeric, U6 explain; mastery explain); 3 gates with manipulables hidden-until-commitment and choice-differentiated feedback (simulated); 4 ladders (Σ, norms, dot, projection); 3 explain items (floor ≥2); mastery 11 items = 9 units + 2, interleaved, reasoning/transfer/error-ID present, fresh numbers (verified against worked set), 3-level confidence; 15 misconceptions M1–M15 each surfaced (13 callouts + 2 gate alerts now also callouts) and encoded as distractors; labels + provenance tags on every block (64 badges, 53 tags); glossary 40 entries × 6 fields (240/240); concept map a branched dependency graph (18 nodes, dashed promise edges) revisited in U10; per-unit ledes and pre-widget worked examples present. PASS.
5. **Technical & behavioral:** `node --check` PASS; zero external refs scan PASS; 288 ids unique; all anchors/aria/data-wiring/glossary refs resolve (scripted); handler-level behavioral simulation **41/41 PASS** (gate refuse/commit/differentiate/reveal, mcq/numeric grading + tolerance, multi-input ladders, hint never-auto-open + on-demand, explain model-answer + self-grade routing, mastery confidence routing of confident misses to the review list, matching, live recomputation on input for W12/W6/W13, W11 degenerate guard, glossary popover); contrast measured for 20 text/background pairs — worst 4.86:1 (AA PASS); reduced-motion honored; colophon per standard; no-JS: gated content hidden by JS only, glossary static; print notes on all 13 widgets. PASS.

## Evaluation and defects

Evaluation: [EVAL-2026-0004](../evaluations/eval-2026-0004-linear-algebra-foundations-v6.md) — weighted 3.76, all hard gates ≥ 3.5, diagnostically passing. No unresolved Major/Critical defects at closure.

## Reflection and root-cause hypothesis

The @0.4.0 hypothesis is **supported**: at 170,701 bytes with 13 manipulable widgets, 3 verified-fidelity gates, 4 full ladders, 11 mastery items with 3-level confidence, a 40×6 glossary, and a branched concept map, CAN-2026-0005 matches the reference implementation (CAN-2026-0003: 178,020 bytes, 12 widgets, 3 gates, 4 ladders, 10 items, 32×6 glossary) technique-for-technique and exceeds it on several counts — from the same source, in a single generation, where @0.3.0 produced the compliant-minimum CAN-2026-0004 (78,026 bytes; 9 widgets, 2 hollow gates, 1 ladder, 6 items, 18×3 glossary). The depth gap that @0.3.0 left closed once depth was (a) specified in CM/LP/XS as conformance targets and (b) demanded in the prompt with a conformance sweep. Residual risk: the remaining thin spots of v5's pipeline stage (a thin CM starving downstream) were addressed by template floors, not proven unnecessary.

## Revision history and regression checks

None (single build; revision cycles = 0).

## Decision and approvers

**Final candidate identity at closure:** SHA-256 `6202f3e9cfbc69075b10019d1fa7265ccf2a0949a2245e244e383e98db5b7dc6`, 170,701 bytes.<br>
**Disposition:** private-pilot-complete<br>
**Decision scope:** private pilot (public-release eligibility: ineligible — non-independent review, ADR-0003)<br>
**Approvers and limitations:** solo Stage 1 operator; no independent review; not a public release, benchmark result, or efficacy claim.

## Memory disposition

No new MEM items. MEM-2026-0004's recommended actions were executed (depth-bar prompt, spec depth floors, checklist depth items) and are validated by this run — its "untested hypothesis" limitation is resolved in favor; an in-place dated note on MEM-2026-0004 is NOT made (records are append-only; the resolution lives here and in EVAL-2026-0004). MEM-2026-0001 (gates), MEM-2026-0002 (constructed response), MEM-2026-0003 (behavioral audit gates) applied, not extended. Pattern catalog: P-01/02/03/04/12/14/15 re-applied successfully — evidence links to this run strengthen confidence (curation deferred to the prompt-card update only, per workflow P6 minimality; catalog text already cites CAN-2026-0004 contrast cases).

## Lineage audit

SRC-2026-0001 → CM-2026-0003 → LP-2026-0004 → XS-2026-0004 → (prm-generator-lesson-standard@0.4.0 `b8d8bd93e94f`) → CAN-2026-0005 → EVAL-2026-0004. Prompt card @0.4.0's "Last evaluated" field updated by this run (see library/prompts).

## Retrospective appendix (2026-08-14) — independent re-verification

[EVAL-2026-0005](../evaluations/eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md) reproduced this ledger's verification evidence exactly (SHA-256, 288 unique ids, structural counts, 4.86:1 worst measured contrast, 3.76 weighted arithmetic, syntax and zero-dependency scans, bounded-input verification). No new defects; the @0.4.0 "supported" judgment is corroborated by scripted re-measurement. No outcome, disposition, or eligibility change.
