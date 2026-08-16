# EVAL-2026-0005: Re-verification audit — linear algebra foundations v5 (CAN-2026-0004) and v6 (CAN-2026-0005)

**Candidate ID/version:** CAN-2026-0004 ([`linear-algebra-foundations-v5.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v5.html), SHA-256 `2191b088440d60717b4d88830698d60ac81f919a8e841d719fd93ccc177dfb1c`, 78,026 bytes) and CAN-2026-0005 ([`linear-algebra-foundations-v6.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v6.html), SHA-256 `6202f3e9cfbc69075b10019d1fa7265ccf2a0949a2245e244e383e98db5b7dc6`, 170,701 bytes) — re-verified, **not re-scored**<br>
**Rubric version:** [lesson-qa-checklist](../../library/rubrics/lesson-qa-checklist.md) at its 2026-08-13 state (including the depth items that postdate EVAL-2026-0003) + [lesson standard](../../docs/01-product/lesson-standard.md) §1.1; the [evaluation framework](../../docs/06-evaluation/evaluation-framework.md) is used for defect-severity vocabulary and gate arithmetic only — no dimension re-scoring<br>
**Evaluator role/identity:** Repository maintainer (solo Stage 1 operator, Reviewer profile)<br>
**Evaluation mode:** specialist (script-assisted re-verification: syntax, wiring scans, independent recomputation, measured WCAG contrast, structural conformance counts, records cross-check)<br>
**Operating scope:** Stage 1 private pilot<br>
**Review independence:** non-independent (author = reviewer; the reviewer is also the operator who generated the artifacts and authored EVAL-2026-0003/0004 — this is **re-verification, not independent review**)<br>
**Reviewer relationship or limitation:** findings restricted to mechanically, structurally, and arithmetically verifiable claims; behavioral claims verified at handler level in source, not executed in a browser; no screen-reader pass<br>
**Public-release eligibility:** ineligible (ADR-0003); this record changes no eligibility<br>
**Confidence:** high on mechanical/recomputational/arithmetic items; medium on handler-level behavioral items<br>
**Recommendation:** corroborate both closures (`private-pilot-complete` stands for both candidates); no score, gate, disposition, or eligibility change; records errata executed via dated retrospective appendices (see Disposition)<br>
**Iterations reviewed:** builds = 2 (SHA-256 `2191b088…dfb1c`, `6202f3e9…5b7dc6`); revision cycles = 0 (per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md))

## Purpose and scope

An external audit request asked for a comprehensive quality audit of the two most recent candidates and their governing records. This record persists that audit: it re-verifies both artifacts against the **current** checklist and cross-checks every ledger claim it makes. Two framing notes govern interpretation:

1. EVAL-2026-0003 was executed legitimately against the **pre-amendment** checklist; the depth items it would later fail were added on 2026-08-13 *because of* CAN-2026-0004 ([MEM-2026-0004](../memory/mem-2026-0004-compliant-minimum-collapse.md)). This audit measures the artifact against today's bar and confirms those documented findings artifact-side, with line evidence.
2. No dimension is re-scored. The framework scores verified artifact evidence; where this audit's re-measurement reproduces the recorded evidence exactly, the recorded scores stand.

## Scope and evidence inspected

- Both artifacts in full; inputs CM-2026-0002/0003, LP-2026-0003/0004, XS-2026-0003/0004; ledgers RUN-20260813-0001/0002; evaluations EVAL-2026-0003/0004; the module [README](../../content/aiml-4/module-02-math-statistics-for-ml/README.md); the rubric and standard.
- Commands and outputs (all reproducible from the repository root): `python3 scripts/check-repo.py` → exit 0 (7 checks, 0 failures, 4 notes); `shasum -a 256` on both artifacts → **exact match** to both ledgers and evaluations; `node --check` on both extracted scripts → PASS; zero-external-reference greps → none (v5's 6 and v6's 20 `url(#…)` are internal SVG markers); duplicate-ID scans → v5 134 unique ids, v6 288 unique ids (both exactly as ledgered); a wiring script (anchors, `aria-describedby`, `data-g`/`data-term` glossary targets, `data-grade`→grader keys, feedback elements) → 0 missing targets in both; a WCAG contrast script over the declared token pairs; a recomputation script over 41 answer keys/widget defaults.

## Findings — CAN-2026-0004 (v5) against the 2026-08-13 checklist

14 findings, 9 Major-class, **zero Critical** (no false claim, broken core task, access barrier, or provenance issue), **zero new** — every Major is pre-documented in [MEM-2026-0004](../memory/mem-2026-0004-compliant-minimum-collapse.md) and encoded as contrast cases in the amended checklist; this audit confirms each artifact-side with line evidence. Line numbers cite `linear-algebra-foundations-v5.html`.

| # | Finding | Severity | Artifact evidence |
| --- | --- | --- | --- |
| 1 | Recognition-only check, Unit 6 (single radio `u6q1`, no constructed response) | Major (checklist: "a recognition-only unit check is a Major") | lines 462–472; `UNITS={u6:["u6q1"]}` |
| 2 | Recognition-only check, Unit 7 (single radio `u7q1`) | Major (same rule) | lines 492–501 |
| 3 | Zero-input widget badged Explore (`w-lsq`: canvas + readout only, 0 input elements; goal text says "Watch the residuals") | Major (widget-manipulability item) | lines 424–431; scripted input count = 0 |
| 4 | Gate g1 hollow: manipulable `w-span` visible without commitment; feedback static and answer-independent; silent refusal when uncommitted | Major (gate-fidelity item; MEM-2026-0001) | gate lines 228–240 vs widget line 241; gate JS shows `.gated` with no per-option branch |
| 5 | Gate g2 hollow (same pattern) | Major (same item) | gate lines 282–293 vs widget line 294 |
| 6 | Spec under-ship: LP-2026-0003 named 4 faded ladders (Σ, dot, norm, projection); artifact ships 1 ladder div (dot, 3 rungs) + 1 norm rung; XS-2026-0003's norm-comparator widget absent | Major (spec-conformance + depth-bar items) | single `class="ladder"` at line 311; no norm comparator anywhere |
| 7 | Glossary 19 entries × 3 fields (simple/precise/ML) vs six required; used terms unlisted: *unit vector* (line 403), *residual* (lines 410, 417, 420), *inverse* (line 422) | Major (glossary-shape item) | lines 548–600 |
| 8 | Concept map is an 8-box linear sequence strip, not a branched dependency graph | Major (concept-map item) | u0 SVG, lines ~137–160 |
| 9 | Canvas extrema unbounded: typed `number` inputs without min/max on `w-span`/`w-dot`/`w-proj`; fixed 640×360 canvas with `WX=320+40x` renders \|x\|>8 off-canvas | Major (canvas-extrema item; the v2 defect class reintroduced) | inputs at lines ~243–246, 298–299, 412–413; `WX`/`WY` in script |
| 10 | Dangling forward promise: line 188 "you will compute this yourself in Unit 3" and line 217 "returns in Unit 3"; Unit 3 (lines 273–342) never mentions wᵀx again | Major (spec-conformance: no dangling forward promises) | grep `wᵀx`: lines 187–188, 217, 565 only |
| 11 | Mastery confidence tags 2-level (sure/unsure) vs three-level (sure / think so / guessing) | Minor | lines 509–533 |
| 12 | Explain-in-own-words items: 1 (m6) vs standard §5 floor ≥2 | Minor | m6 block only |
| 13 | Mastery size 6 vs pattern ≈ one item per content unit + 2 (7 + 2) | Minor (P-12 is approximate; conformant to its own LP-2026-0003) | `data-mastery` block |
| 14 | Misconceptions surfaced as visible alert callouts: 0 (distractors do encode them ✓) | Minor under the post-2026-08-13 callout clause | `c-mis` count = 0 |

**v5 verified passes:** syntax; zero external requests; 134 unique ids; all wiring resolves; 19/19 recomputation subset PASS (incl. least-squares m=1.1 / c=1.0 / SSE=0.70 and AB=`[[7,2],[3,1]]` ≠ BA=`[[1,2],[3,7]]`); measured worst contrast **5.07:1** (colophon text at 0.66 opacity on paper — exact replication of the ledger), AA pass; colophon brand + AI-honesty lines present; print notes on all 10 widgets; reduced-motion honored; gated content hidden by JS only; repairs R1–R3 labeled; mastery uses fresh numbers; coverage matrix 63/63 cells dispositioned (EVAL-2026-0003 Appendix A).

## Findings — CAN-2026-0005 (v6) against the same checklist

**Zero open defects.** Every ledger/XS claim tested was reproduced exactly:

| Claim group | Result |
| --- | --- |
| 13 widgets, all learner-manipulable, goals stated | ✓ w1–w13 with 13 goal strips; every canvas-widget input bounded (min/max) or autoscaling (W8); W12 clamps fitted values |
| 3 gates, full fidelity | ✓ manipulables (w4/w7/w11) hidden by JS only; refusal message when uncommitted; `GATES[g].fb[choice]` choice-differentiated, referencing the commitment (lines 392–411, 575–596, 719–747) |
| 4 faded ladders, one per computational skill | ✓ lad1 Σ (U2), lad2 norms (U5), lad3 dot (U6), lad4 projection (U8); worked → completion → independent; tiered never-auto-opening hints (lines 344, 515, 597, 748) |
| 9 unit checks, each ≥1 constructed-response item | ✓ numeric CR in every check (u1q2, u2q1, u3q1, u4q2, u5q1, u5q2, u6q1, u7q1, u8q1, u9q1); explains in ck1 + ck6; governing-rule feedback on every item |
| 3 explain items (floor ≥2) | ✓ u1q3, u6q3, m10 — model answers + honest self-grade routing that also completes unit dots |
| Mastery: 11 items (= 9 content units + 2), three-level confidence, confident-miss routing for radio AND numeric | ✓ `sure/think/guess` ×11; routing fires on `conf === 'sure'` for all item types (lines 868–933) |
| 15 named misconceptions as visible callouts + distractors | ✓ 15 `c-mis` callouts; M1–M15 encoded as distractors with per-option rule feedback |
| Glossary 40 × 6 fields; in-text terms resolve | ✓ 240/240 fields; 14/14 `data-term` targets resolve; popover initially `hidden`, focus-managed, Escape closes |
| Concept map: 18-node branched dependency graph, revisited | ✓ branched SVG with dashed promise edges + text version; full revisit in U10 (line 846) |
| Reveal arcs pay off where named | ✓ wᵀx promised U2 (line 368) → paid off U6 (lines 564–565); (AᵀA)⁻¹ loop closed U9 |
| Per-unit ledes; worked numeric example before any widget | ✓ 11 unit ledes (+ glossary lede); "Tiny example" beats precede widgets |
| Mechanical/technical | ✓ `node --check` PASS; zero external refs; 288 unique ids (= ledger); all wiring resolves; print notes on all 13 widgets; colophon brand + AI-honesty (lines 1220–1222); provenance header comment |
| Recomputation | ✓ 22/22 subset PASS (all unit-check numerics, all 8 ladder rungs, mastery m2/m3/m4/m9); W12 default fit m=0.9 / c=1.0 / SSE=0.70 internally consistent |
| Measured contrast | ✓ worst pair **4.86:1** replicated exactly (b-deep `#0f766e` on `#ccfbf1`); all other measured pairs ≥ 5.47:1 — AA pass |
| Weighted arithmetic | ✓ recomputed exact: (4.0×18 + 4.0×18 + 3.5×10 + 4.0×10 + 3.5×14 + 3.5×8 + 3.5×8 + 4.0×6 + 3.5×4 + 3.5×4) = 376 → **3.76**; all hard gates ≥ 3.5 |

Declared limitations standing (not defects): opaque-PNG figure transcription not verifiable against image content (inherited; source-grounding 3.5); no screen-reader pass. One audit-side false alarm was raised and cleared on full-context re-read (`u8q3` feedback: correct key `b` carries ✓, distractors carry ✗ — proper).

## Records-consistency findings

1. **Erratum — ladder wording (EVAL-2026-0003, RUN-20260813-0001):** both describe "faded ladders (Σ, dot, norm)". The artifact ships one dot-product ladder plus a single norm rung; no Σ ladder exists. The correct count (1 of the 4 LP-named ladders) is recorded in MEM-2026-0004 and drove the 2026-08-13 checklist depth items. Wording-only discrepancy; no score, gate, or disposition impact. Corrected by dated retrospective appendix on both records (append-only mechanism per ADR-0007 precedent).
2. **EVAL-2026-0003 Audit 4 "PASS" vs the two recognition-only checks and the 3-field glossary:** confirmed artifact-side; already diagnosed by MEM-2026-0004 ("an unexecuted check is indistinguishable from a passed one") and remediated by the amended checklist. No further action.
3. **Erratum — glossary count (MEM-2026-0004):** states "18 three-field entries"; the artifact ships **19** entries × 3 fields. Trivial count slip; substance unchanged. Per the RUN-20260813-0002 precedent, no in-place note is made on the memory record; the correction lives here and is carried into the next memory curation of MEM-2026-0004.
4. **Suspected and refuted during this audit** (preserved for transparency): EVAL-2026-0004's weighted 3.76 (recomputed exact — correct); v6 `u8q3` feedback glyph (correct as shipped); v5 colophon compliance (brand line present with ♥ in a span + sr-only "love").

## Weighted result and gate check

No re-scoring. Gate arithmetic re-verified exactly as written: EVAL-2026-0003 = 359/100 → **3.59** ✓; EVAL-2026-0004 = 376/100 → **3.76** ✓; all hard gates ≥ 3.5 in both; dispositions unchanged.

## Disagreement or uncertainty

Re-verification is by the same operator who generated the artifacts and authored the prior evaluations — it corroborates evidence but adds no independence; release eligibility is unaffected (ineligible, ADR-0003). Handler-level behavioral claims (gate refuse/commit/differentiate, grading, tolerance, routing, popover) were verified in source, not executed in a browser. The v5 Major findings are historical: the artifact is preserved, superseded by v6 as the reference lesson, and must not be retro-edited (naming conventions: a version change requires a new governed run).

## Non-negotiable blockers

None found in either candidate (no false claims, broken core tasks, access barriers, or provenance issues).

## Reviewer sign-off

Non-independent solo-operator specialist review, 2026-08-14; scope, evidence, defects by severity, and uncertainty as above. Decision: **corroborate** — both closures stand.

## Disposition and memory

- This record is the persisted audit report for both candidates; it is linked from the module README's Governed work table and from the four affected ledgers/evaluations via their 2026-08-14 retrospective appendices.
- Dated retrospective appendices executed: EVAL-2026-0003 (erratum + re-verification), RUN-20260813-0001 (erratum + re-verification), EVAL-2026-0004 (re-verification corroboration), RUN-20260813-0002 (re-verification corroboration).
- Memory disposition: no new MEM items — the v5 lessons are already curated in [MEM-2026-0004](../memory/mem-2026-0004-compliant-minimum-collapse.md); its 18→19 glossary-count erratum is recorded here for the next curation. The exact-replication method (contrast script, recomputation script, wiring scan) is noted as reusable P5 evidence practice for the next governed candidate.
