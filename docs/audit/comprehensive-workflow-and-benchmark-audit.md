# Comprehensive Workflow and Benchmark Audit — Interactive Lesson Generation Pipeline

**Status:** Draft (diagnostic record; not reviewed under the review policy — promotion requires the owner review named there)<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-09-14 (or upon completion of the workflow-redesign phase this audit feeds, whichever comes first)<br>
**Applies to:** the Learning OS lesson-generation pipeline (P0–P6), its governing documents, and the AIML-4 Module 2 candidate lineage v1–v6<br>
**Date:** 2026-08-14<br>
**Scope:** diagnosis and root-cause analysis only. This document proposes **no** prompts, agents, workflow redesigns, fixes, validation strategies, or recommendations (per the audit mandate).<br>
**Independence:** non-independent — the auditor is an AI agent operating in the same solo-operator environment that produced the artifacts under audit. Findings are anchored to mechanically verifiable evidence wherever possible, and every material claim carries an evidence class.

## How to read this audit

**Evidence classes.** Every finding marks its claims as one of:

- **Observed** — directly verified in repository artifacts during this audit (file contents, hashes, git history, line-level code inspection).
- **Inference** — evidence-supported inference: strongly supported by multiple independent records/artifacts, but not directly mechanically proven.
- **Unknown** — cannot be established from available repository evidence.

**Naming.** Candidates: v1 (historical, ungoverned), v2 = CAN-2026-0001, v3 = CAN-2026-0002, v4 = CAN-2026-0003 (**the benchmark**), v5 = CAN-2026-0004, v6 = CAN-2026-0005. Records are cited by stable ID (SRC/CM/LP/XS/RUN/EVAL/MEM). The V5/V6 audit of record, per owner designation, is [EVAL-2026-0005](../../records/evaluations/eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md) plus the 2026-08-14 retrospective appendices on EVAL-2026-0003/0004 and RUN-20260813-0001/0002.

**Artifact identity verification (Observed, 2026-08-14).** Re-hashed during this audit; all match their records exactly: v4 `b35c622e…1590` (178,020 B), v5 `2191b088…fb1c` (78,026 B), v6 `6202f3e9…dc6` (170,701 B), source notebook `23c6f4eb…4445`. The benchmark artifact's current bytes are exactly the identity recorded as current across RUN-20260810-0001, EVAL-2026-0002, XS-2026-0002, EVAL-2026-0004, and XS-2026-0004.

---

## 1. Executive Summary

**How the repository works (Observed).** The pipeline is a *documented, manually operated* workflow — not software. A solo operator (human owner + AI coding agent) executes phases P0–P6 by authoring governed Markdown records: source intake (SRC) → concept model (CM) → learning plan (LP) → experience specification (XS) → generation via a versioned prompt card (RUN ledger + HTML artifact) → five mandatory audits (QA checklist) → evaluation and closure (EVAL + memory/pattern/prompt curation). The only executable tooling is `scripts/check-repo.py`, a read-only hygiene checker that never executes or scores learner artifacts.

**What makes V4 the benchmark (Observed).** V4 was produced on 2026-08-10 by a process the current workflow only partially contains: (a) an owner's 30-section generation brief whose full text is **not persisted in the repository**; (b) a redesign plan (LP-2026-0002) driven by comparative audits of three prior variants; (c) the deepest concept model in the lineage (CM-2026-0001); and (d) a post-evaluation **adversarial revision cycle** that found and repaired 3 Major + 11 Minor/nit defects *after* the artifact had already passed the full standing verification suite (RUN-20260810-0001 §Revision 1; MEM-2026-0003). The lesson standard, workflow, pattern catalog, QA checklist, and prompt cards were codified **the day after** V4 (commit `3453c6d`, 2026-08-11) — the workflow is a post-hoc extraction of the V4 process, adopted under [ADR-0004](../adr/0004-lesson-standard-adoption.md).

**What V5 and V6 demonstrate (Observed).** V5 (2026-08-13, prompt card @0.3.0) was a deliberate regeneration test — source + governed workflow only, prior artifacts explicitly not consulted. It passed all five audits as executed, scored 3.59 (**identical to V4**), and silently shipped ~44% of V4's size with hollow gates, 1 of its own plan's 4 ladders, two recognition-only unit checks, a zero-input widget badged Explore, a 3-field glossary, a sequence-strip concept map, unbounded canvas inputs, and a dangling wᵀx promise (MEM-2026-0004; EVAL-2026-0005 findings 1–14, each confirmed artifact-side with line evidence). V6 (same day, @0.4.0 with the new depth bar + depth-floor records) restored reference-band depth in a single generation (3.76; zero open defects under the 08-13 checklist; EVAL-2026-0004/0005).

**The central gap (Inference, high confidence).** The capabilities that made V4 the benchmark were encoded into the workflow as *rules* (what must exist) but not as *calibrated depth* (how much is enough) or as *enforced process* (the adversarial revision cycle that actually surfaced V4's worst defects). V5 proved the rules alone converge to a compliant minimum that audits and scores could not distinguish from the benchmark. The 08-13 remediation (depth bar, spec conformance, template floors, checklist depth items) closed the measured depth gap — with exactly one confirming run, on the same source, by the same operator, under the same model family, with no browser-executed verification at any point in the pipeline's history.

**What the workflow can currently guarantee (Observed/Inference).** Coverage accounting, scripted mathematical recomputation, dependency-order review, structural/wiring integrity, measured contrast, and — since 08-13 — specified-depth conformance, all at *self-certified, handler-level* evidence strength. It cannot guarantee: rendered-output correctness (no browser pass exists), audit *execution* (an unexecuted check is indistinguishable from a passed one — MEM-2026-0004), benchmark-relative polish, or reproducibility on any source other than SRC-2026-0001.


---

## 2. Repository and Workflow Architecture

### 2.1 What the repository is (Observed)

Learning OS is a documentation-first governance repository ([README.md](../../README.md), [AGENTS.md](../../AGENTS.md)): "deliberately **not the application**." There is no application code, no build system, no test harness for artifacts. The agentic workflow is realized as *documents that instruct an operator* (human + AI agent) plus *append-only evidence records*. Only two executables exist: `scripts/check-repo.py` (read-only hygiene: link resolution, content-hash provenance coverage, rubric weight-sum integrity, status vocabularies, README metadata, filename conventions, ADR index — [ADR-0008](../adr/0008-repository-checker-tooling.md)) and the artifacts' own inline JavaScript.

### 2.2 How the parts participate in the workflow (Observed)

| Surface | Role in the pipeline |
| --- | --- |
| `docs/01-product/lesson-standard.md` | Binding content rules (Consistency Contract §1.1 required elements; §2 explain-before-use; §4 interaction admission; §5 assessment philosophy; §8 canonical anatomy; §10 visual design system). Names CAN-2026-0003 as **reference implementation** |
| `docs/03-workflows/lesson-generation-workflow.md` | The P0–P6 phase contract; "no phase may be skipped"; failure routing (Audits 1–3 → fix plan; 4–5 → targeted revision) |
| `docs/03-workflows/quality-loop.md` | State machine (planned→generating→evaluating→reflecting→revising→…); retry policy ("fix the plan, not the symptom"; "change one primary variable per experiment") |
| `docs/06-evaluation/evaluation-framework.md` | Sole numeric gate authority: 10 weighted dimensions, hard gates ≥3.5, weighted ≥3.5; 0.5-point score increments (ADR-0003); weights-sum-100 rule (ADR-0007) |
| `library/rubrics/lesson-qa-checklist.md` | Executable P5 verification checklist (five audits); origin note: "codifies the audits that produced and repaired CAN-2026-0003" |
| `library/patterns/lesson-patterns.md` | Pattern catalog P-01…P-15 extracted from V4, now carrying V5 contrast anti-patterns |
| `library/prompts/prm-generator-lesson-standard@*.md` | Versioned generation prompt cards @0.1.0→@0.4.0; only @0.3.0 (v5) and @0.4.0 (v6) powered governed runs |
| `templates/concept|learning|lesson` | CM/LP/XS starters; depth-floor fields added 2026-08-13 (commit `8db0c1a`) |
| `records/**` | Append-only evidence: SRC→CM→LP→XS→RUN→EVAL→MEM lineage per candidate |
| `content/aiml-4/module-02-math-statistics-for-ml/` | The single content package: one source notebook (63 markdown cells) + six generated HTML artifacts |

### 2.3 Experimental vs production-like (Observed)

Every governing document carries **Status: Experimental** with a 2026-11-04 review date; the prompt cards are **Draft**; the ADRs defining pilot semantics (ADR-0002/0003) remain **Proposed**. Stage 1 runs are private pilots; public release is structurally impossible (non-independent review ⇒ `ineligible`, ADR-0003). Benchmark infrastructure is explicitly future-stage ([benchmark-strategy](../06-evaluation/benchmark-strategy.md): "No benchmark suite exists yet"). Nothing in the repository is production-hardened; the pipeline's maturity claim is "manually operated workflow," the second rung of the [roadmap](../11-roadmap/roadmap.md).


---

## 3. End-to-End Pipeline Reconstruction

Reconstructed from [lesson-generation-workflow](../03-workflows/lesson-generation-workflow.md) and verified against what the five run ledgers actually record (Observed at the document level; per-run conformance verified for the v2/v4/v5/v6 ledgers).

| Phase | Input | Output | Validation at the stage | What the stage cannot see |
| --- | --- | --- | --- | --- |
| P0 Intake | Notes document + learner request | SRC record (identity, SHA-256, cell anchors); learner definition; scope | Authorization confirmation; hash pin | — |
| P1 Source understanding | SRC | CM: concepts, atomic claims w/ cell anchors, prerequisite chains, misconceptions, ambiguity dispositions | CM review (non-independent) | Whether CM depth is *sufficient* — no floor existed before 08-13 (template floor added post-V5) |
| P2 Learning design | CM | LP: measurable outcomes, re-sequenced teaching order, per-concept pedagogy decisions, assessment plan; depth pass (ledes, signature visuals, reveal arcs, ladders, explain placement) mandatory since 08-13 | Operator approval; outcomes measurable | Downstream generation fidelity to the plan |
| P3 Experience design | LP | XS: unit-by-unit content/evidence map, widget specs, acceptance criteria; since 08-13 a conformance contract (per-widget manipulable variables, bounds, glossary term set, concept-map edges) | Operator approval | Conformance verification was not a generation duty until @0.4.0 |
| P4 Generation | SOURCE + CM + LP + XS + PROVENANCE + PATTERN_CATALOG + prompt card | One single-file HTML candidate + RUN ledger (pinned identities, prompt digest, iteration counts per ADR-0006) | Creator self-verification (prompt item 9); since @0.4.0 an in-generation conformance sweep (item 13) | Rendered behavior; its own blind spots |
| P5 Five audits | Candidate + all records | Gate evidence in the evaluation record: 1 coverage matrix, 2 scripted recomputation, 3 read-in-order dependency pass, 4 pedagogical compliance (incl. 08-13 depth items), 5 technical & behavioral (syntax, zero-dependency, wiring, **handler-level behavioral simulation**, measured contrast, keyboard/no-JS/reduced-motion/print) | The checklist itself | Rendered pixels, real-browser events, screen-reader behavior; **audit execution is self-certified** |
| P6 Evaluation & closure | Candidate + audit evidence | EVAL scorecard (10 dimensions, gates), disposition, memory/pattern/checklist/prompt curation | Gate arithmetic (post-ADR-0007) | Score sensitivity to depth (anchors are diagnostic-only since 08-13) |

**Observed deviations of record:** v2 (RUN-20260804-0001) ran with **no prompt card** ("prompt identity is therefore weak"); v3 (RUN-20260804-0002) pinned a verbatim prompt snapshot but its evaluation was **never performed** (formally deferred, its Appendix B); v4 used the owner's brief, not a library card. Only v5 and v6 executed the full documented pipeline with a versioned prompt card.


---

## 4. Agent and Context Flow

Stage 1 activates five composite profiles over the 18-role reference catalog ([stage-1-operating-profile](../04-agents/stage-1-operating-profile.md)); all are executed by one human owner plus one AI agent, pass by pass. What each stage *actually* knew is evidenced by the run ledgers' input manifests:

| Stage (profile) | Knows (persisted inputs) | Does **not** know (Observed, from manifests/ledgers) | Persists forward |
| --- | --- | --- | --- |
| P1 CM authoring (Creator) | Source notebook; source-intake record | Prior candidates and prior CMs — v5's CM-2026-0002 states "does not read or reuse CM-2026-0001"; v6's CM-2026-0003 consulted CM-2026-0001 only as a *depth-floor calibration exemplar* | CM record (Markdown) |
| P2 LP authoring (Creator) | CM; lesson standard; memory items (retrieval is advisory, per [memory-architecture](../07-memory/memory-architecture.md) — no mechanism forces it) | The benchmark artifact itself; prior LPs (v5: fresh; v6: LP-2026-0002 consulted as depth exemplar) | LP record |
| P3 XS authoring (Creator) | CM + LP; pattern catalog | Same benchmark exclusion | XS record |
| P4 Generation (Creator/Generator) | SOURCE, CM, LP, XS, PROVENANCE, PATTERN_CATALOG, prompt card (card @0.1.0+ "Required inputs") | **V1–V4 artifacts were "not read, not consulted" for v5** (RUN-20260813-0001); v6 read v4/v5 depth counts only at P6 (RUN-20260813-0002). The owner's 30-section brief exists only as a condensed snapshot (RUN-20260810-0001 App. A) | HTML artifact + RUN ledger |
| P5 Audits (Reviewer) | Candidate + records + checklist | Rendered output (handler-level simulation only); independent verification of *whether each check was executed* | Evidence notes inside EVAL |
| P6 Evaluation (Reviewer/Evaluator) | Candidate, audit evidence, rubric | Independent reviewer (none exists); learner evidence (none exists) | EVAL; MEM promotions; pattern/checklist/prompt amendments |

**Explicit vs implied requirements (Observed).** Explicit: standard §1.1 contract, coverage matrix, recomputation, dependency pass, zero-dependency, colophon/provenance, and (post-08-13) depth bar, per-widget manipulability, gate fidelity, glossary shape, concept-map structure, XS conformance. Implied (agent-judgment-dependent): "polish," visual hierarchy quality, analogy quality, information density, what counts as a *signature* visual, how much explanation is enough per block. The handoff protocol ([handoff-protocol](../03-workflows/handoff-protocol.md)) defines packet contents, but no stage produces a literal packet artifact — handoffs are the CM/LP/XS/RUN records themselves.


---

## 5. Workflow Evolution

Reconstructed from `git log` (all commits inspected), record dates, and change-history sections (Observed):

| Date | Commit(s) | Change | Encoded or ephemeral? |
| --- | --- | --- | --- |
| 08-03/04 | `2a70bea`, `ca6de87` | v2 (CAN-2026-0001) via LM Studio Bionic harness, **no prompt card**; v3 (CAN-2026-0002) via Claude/Cline with verbatim prompt snapshot `70ec9b15aeeb` (RUN-20260804-0002 App. A) | Snapshot persisted verbatim; v3 evaluation never performed (deferred 08-11) |
| 08-10 | `aeb76b1` | **V4 build**: LP-2026-0002 redesign + XS-2026-0002 + owner's 30-section brief (digest `f1a43cbf21cf`); 4 in-generation corrections; EVAL-2026-0002; then **Revision 1** — owner-requested adversarial audit (scripted structural audit + two isolated adversarial sub-audits + handler-level simulation): 3 Majors (R1 matrix-product dependency breach at the lesson's climax; R2 confidence logic dead on numeric path; R3 quadrant-sensitive angle-arc bug) + 11 minors/nits, all repaired; build `b35c622e` | The *artifact* and records persist; the **brief's full text does not** ("condensed snapshot … preserved out-of-band … operator session log"); the three variant-audit reports lived in an "owner's deliverable summary … outside this repository" (EVAL-2026-0002; coverage matrix reconstructed into Appendix C only on 08-13) |
| 08-11 | `3453c6d` | **Codification**: lesson standard, lesson-generation workflow, pattern catalog, QA checklist, prompt card @0.1.0, MEM-2026-0003 (the two new audit gates); ADR-0004 adopts the "v4-derived" standard | Encoded — one day *after* V4 |
| 08-11 | `2ee0f38` | Owner-directed v4 edits: "clarifying edits and remove interaction gating from explorers" (+75/−29 lines); EVAL/RUN appendices | Artifact mutated post-evaluation, outside the generation workflow; tracked by dated appendices; no re-evaluation of the whole |
| 08-11/12 | ADR-0006/0007 era | Iteration accounting becomes mandatory; gate arithmetic repaired (weights summed to 98, not 100; v2 3.37→3.45, v4 3.51→3.59 recomputed) | Encoded |
| 08-13 | `5da2754` | Standard colophon added to standard/workflow/checklist/@0.3.0; applied retroactively to v2–v4 | Encoded |
| 08-13 | `111c965` | **V5 regeneration test** (@0.3.0; fresh CM-2026-0002/LP-2026-0003/XS-2026-0003; prior artifacts not consulted; 1 correction; 0 revision cycles) → EVAL-2026-0003, 3.59, gates pass | Run and records persist |
| 08-13 | `8db0c1a` | **Depth-bar retrofit** after MEM-2026-0004 diagnosed v5's compliant-minimum collapse: prompt @0.4.0 (items 10–13), checklist depth items, CM/LP/XS template floors, framework diagnostic anchors, pattern anti-patterns | Encoded — *reactive*, post-failure |
| 08-13 | `e95fa66` | **V6 comparison run** (@0.4.0; depth-floor CM-2026-0003/LP-2026-0004/XS-2026-0004; 10 in-generation corrections; 0 revision cycles) → EVAL-2026-0004, 3.76, "hypothesis supported" | Run and records persist |
| 08-13 | `27de79e` | Visible governance banners/footers removed from v2–v4 by owner directive; identity moved to header comment | Artifact mutation outside generation workflow; hash identities updated in records |
| 08-14 | `8a300b0` | EVAL-2026-0005 re-verification of v5/v6 (mechanical/handler-level); retrospective appendices; no score changes | Encoded |

**Pattern of evolution (Inference, high confidence):** every strengthening of the workflow was *reactive to a specific observed failure* — v1–v3's recognition-only assessment → MEM-2026-0002 + standard §5; v4's escaped Majors → MEM-2026-0003 + audits 3/5; v5's collapse → the entire 08-13 depth apparatus. No capability entered the workflow *proactively*; each entered exactly one failure late.


---

## 6. Variant 4 Benchmark Analysis

Inspected directly: `content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v4.html` (1,772 lines; hash verified), its records (LP-2026-0002, XS-2026-0002, RUN-20260810-0001, EVAL-2026-0002), and the source notebook (63 cells, inventory re-derived this audit).

### 6.1 Content (Observed)

- **Completeness/fidelity:** all 63 source cells dispositioned in the EVAL-2026-0002 Appendix C coverage matrix with named dispositions (included-as-taught / included-expanded / transcribed-from-opaque-format / added-foundation / added-extension / excluded-with-reason). Source defects repaired *and flagged in-body*: "Scaler" typo, garbled L2 vinculum, mangled wᵀx/ℝⁿ typography, opaque PNG formulas (cells 38, 42) transcribed not redistributed.
- **Conceptual progression:** 9 teaching units re-derived from CM-2026-0001's dependency chains, not source order; the source's proof-before-dot-product defect is repaired and labeled; transpose pre-taught as a tool so wᵀx is "legal" later (LP-2026-0002).
- **Explanation quality:** per-symbol formula keys; plain language before formalism; every block carries a layer badge (`CLASS CORE`/`FOUNDATION`/`DEEP DIVE`/`ML LINK`/`EXTENSION`) + provenance tag (`source`/`constructed example`/`supplemental`) — verified in markup (e.g. lines 407–410, 495).

### 6.2 Structure (Observed)

Orientation unit (U0) teaching *how to learn with the page* (loop table, label legend, branched concept map) → units U1–U9 each following Learn→Predict→Explore→Practice→Check→Connect → synthesis + interleaved mastery → review list → glossary (32→39 entries after R11) → colophon. Sticky unit nav whose dots fill only on cleared checks (never scroll position).

### 6.3 Interaction (Observed, code-level)

- **12 widgets + 1 matching** exercise (13 `class="widget"` blocks), each goal-directed ("🎯 Goal: …" strips, e.g. lines 419, 666), all values computed live (e.g. W1 vector builder, lines 1256+).
- **3 prediction gates** (`data-gate="lc|dp|pj"`, lines 500, 654, 775): handler (lines 1242–1254) refuses without commitment ("Choose an option first — the value is in committing, not in being right"), differentiates correct/incorrect with rule-re-deriving feedback (`data-ok`/`data-no`), unlocks the hidden manipulable regardless of correctness, disables the button. Gated widgets are hidden **by JS at boot** (R4 repair — static `hidden` would exclude no-JS readers).
- **4 faded ladders** (`data-ladder="sigma|norm|…"`, 3 rungs each: worked → completion → independent; tiered never-auto-opening hints).
- **Mastery:** 10 interleaved items with 3-level confidence (`sure/think so/guessing`, e.g. line 1060) and confident-miss routing to the review list (R2 repair extended this to numeric items).
- **Review list:** localStorage store with graceful in-memory degradation, weak-topic counts, visible reset, and an explicit spacing invitation ("Revisit tomorrow…", lines 1572–1601).

### 6.4 UI/UX (Observed)

Design-token system (`:root` lines 26–36: ink/paper neutrals, one accent hue, semantic good/bad/warn, mono for math); badge/callout/ladder/predict/feedback component classes; DPR-crisp canvas pipeline (`makeView`, lines 1170–1183); aspect-preserving data windows (R14 repair widened the least-squares window from a ~1240px portrait render to ~920px); print stylesheet replacing canvases with default-state notes (line 187+); `prefers-reduced-motion` honored (lines 24, 88).

### 6.5 Technical implementation (Observed)

Single file, zero external requests (scans recorded in EVAL-2026-0002; re-verifiable); `node --check` passes (re-run this audit); helper layer (`gid/fmt/clamp/on`), canvas helpers (`makeView/drawGrid/arrow/dot/txt`), data-driven grading via `data-*` attributes (`wireNum`, lines 1224+); edge guards (zero-vector projection, parallel span, cos clamp).

### 6.6 The benchmark is not magical (Observed)

- The responsive breakpoint sets `body{font-size:15.5px}` at ≤640px (line 186) — **below the standard's own 16px hard rule** (standard §10, amended 08-13).
- Gate feedback differentiates correct/incorrect; the stricter *per-option* differentiation the 08-13 checklist demands (`GATES[g].fb[choice]`) is a V6 behavior (EVAL-2026-0005, v6 gate lines 392–411 etc.). The benchmark would not obviously pass the current checklist's letter.
- Accessibility was scored 3.0 (hard-gate fail diagnostically): contrast *asserted* at first, measured only in Revision 1; no screen-reader pass ever.
- The scorecard was issued against the *pre-revision* build; the shipped benchmark's quality rests on the Revision-1 repairs being correctly regression-checked by the same person who wrote the code.


---

## 7. V5/V6 Failure-Pattern Summary (from the audit of record)

Source: EVAL-2026-0005 (2026-08-14 re-verification, script-assisted, handler-level), the retrospective appendices on EVAL-2026-0003/0004 and RUN-20260813-0001/0002, and MEM-2026-0004. Organized as **patterns**, not defect lists. All V5 items were confirmed artifact-side with line evidence; this audit spot-verified the structural ones (gates, inputs, concept map) against `linear-algebra-foundations-v5.html`.

**Pattern F-1 — Depth collapse under rule-complete compliance (V5 findings 6, 11, 12, 13).** The artifact satisfied every rule at its floor: 1 faded ladder shipped of the 4 its own LP-2026-0003 named (single `class="ladder"` at line 311 — verified); mastery 6 items with 2-level confidence; 1 explain item vs the ≥2 floor. *Workflow relevance:* nothing before 08-13 represented depth as a requirement, and the rubric scored it identically to V4.

**Pattern F-2 — Spec under-ship with passing audits (V5 finding 6; EVAL-2026-0003 erratum).** XS-2026-0003's norm comparator absent; LP-named ladders missing; yet the run ledger's Audit 4 recorded "ladders for Σ/dot/norm — PASS" — a **false PASS**, corrected by dated erratum. *Workflow relevance:* spec conformance was not a generation duty (@0.4.0 added it), and an unexecuted check is indistinguishable from a passed one (MEM-2026-0004).

**Pattern F-3 — Hollow interaction fidelity (V5 findings 3, 4, 5).** Two gates reveal static, answer-independent text while the manipulable stays visible (verified: v5 `.gated` blocks at lines 237/290 contain explanation only; `w-span` sits outside the gate); one zero-input widget (`w-lsq`, lines 424–431) badged Explore with "Watch the residuals" as its goal. *Workflow relevance:* gate *fidelity* and widget *manipulability* were uncheckable by the pre-08-13 checklist; the pattern catalog had P-01 but audits didn't test it.

**Pattern F-4 — Assessment regression to recognition-only (V5 findings 1, 2).** Unit 6 and Unit 7 checks are single radio items (`UNITS={u6:["u6q1"]}`) — a direct breach of standard §5's constructed-response requirement that Audit 4 recorded as PASS. *Workflow relevance:* the requirement existed and was *explicit*; the failure was verification execution, not absence of rules.

**Pattern F-5 — Structural shallowness in reference structures (V5 findings 7, 8).** Glossary 19 entries × 3 fields (six required; used terms *unit vector*, *residual*, *inverse* unlisted); concept map is an 8-box linear sequence strip (verified: rect→line→rect chain at u0, lines ~137–160), not a dependency graph. *Workflow relevance:* shape requirements ("six fields", "branched graph") were textual in the standard but unscanned until 08-13.

**Pattern F-6 — Off-canvas rendering reintroduced (V5 finding 9).** Typed `number` inputs without min/max on `w-span`/`w-dot`/`w-proj` over a fixed `WX=320+40x` mapping (verified lines ~243–246, 601–602) — the same defect class V2 shipped (outlier off-canvas) and V4 repaired via bounded/autoscaled windows. *Workflow relevance:* canvas-extrema checking entered the checklist only on 08-13; memory of the v2 repair was not retrieved at generation time.

**Pattern F-7 — Dangling forward promise (V5 finding 10).** "you will compute this yourself in Unit 3" (line 188) — Unit 3 never mentions wᵀx again. The identical defect class was found in V4 as R12 (concept-map revisit promise) — *and repaired there by the adversarial revision cycle V5 never had*. *Workflow relevance:* reveal-arc payoff became auditable only on 08-13.

**V6 (Observed via EVAL-2026-0005): zero open defects under the 08-13 checklist.** Every ledger/XS claim re-verified exactly (13 manipulable widgets; 3 full-fidelity gates; 4 ladders; 9 checks with constructed response; 3 explain items; 11-item mastery with 3-level confidence and confident-miss routing for radio *and* numeric; 15 misconception callouts; glossary 40×6; 18-node branched concept map; reveal arcs paid; bounded canvases; worst measured contrast 4.86:1; weighted arithmetic 376/100 = 3.76 exact). Two declared limitations stand: opaque-PNG transcription unverifiable against image content; no screen-reader pass. **No rendered-browser evidence exists for V6** (see WF-006).


---

## 8. Benchmark Capability Matrix

Artifact columns: **Observed** presence in the shipped file (✓ full / ◐ partial or weakened / ✗ absent), cross-checked against EVAL-2026-0002/0003/0004/0005 and this audit's code inspection. Workflow columns describe the **current** (post-08-13) workflow; "Validated" = a P5/P6 check exists that can catch its absence; "Persisted" = the requirement survives stage handoffs in a record/template; "Guaranteed" = evidence the pipeline reproduces it without manual rescue (✓ = yes, ◐ = single-run evidence or self-certified, ✗ = no).

| Benchmark capability | V4 | V5 | V6 | Explicitly required | Validated | Persisted across stages | Reproducibly guaranteed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Source coverage with disposition matrix | ✓ | ✓ | ✓ | ✓ (standard §3) | ✓ (Audit 1) | ✓ (EVAL appendix) | ◐ (self-certified) |
| Mathematical accuracy (scripted recomputation) | ✓ (44) | ✓ (35) | ✓ (58) | ✓ | ✓ (Audit 2) | ✓ (RUN evidence) | ◐ (script per-run, ad hoc) |
| Dependency-order correctness | ✓ (after R1 repair) | ✓ (R1–R3 repairs) | ✓ | ✓ (§2) | ✓ (Audit 3, manual) | ✓ | ◐ (judgment-based) |
| Canonical unit anatomy | ✓ | ✓ | ✓ | ✓ (§8) | ✓ | ✓ | ◐ |
| Prediction gates with commitment consequences | ✓ (3, hiding + binary-differentiated) | ✗ (2 hollow) | ✓ (3, hiding + per-choice) | ◐ (§1.2 *recommended*; checklist gate-fidelity item post-08-13) | ✓ (post-08-13) | ✓ (pattern P-01 + MEM-0001) | ◐ (one run) |
| One full faded ladder per computational skill | ✓ (4) | ✗ (1 of 4) | ✓ (4) | ✓ (post-08-13 depth bar + LP/XS floors) | ✓ (post-08-13) | ✓ (LP depth pass, XS contract) | ◐ (one run) |
| Constructed response in every unit check | ✓ | ✗ (2 units recognition-only) | ✓ | ✓ (§5, pre-existing) | ✓ (post-08-13 per-unit naming; v5's PASS was false) | ✓ | ◐ |
| Interleaved mastery + 3-level confidence + confident-miss routing | ✓ (10 items; routing repaired in R2) | ◐ (6 items, 2-level) | ✓ (11 items) | ✓ (§5 + P-12, floors post-08-13) | ✓ (behavioral sim) | ✓ | ◐ |
| Misconception callouts + distractor encoding | ✓ (distractors; callouts partial) | ◐ (distractors only, 0 callouts) | ✓ (15 callouts M1–M15) | ✓ (callout clause post-08-13) | ✓ (post-08-13) | ✓ (CM misconception lists) | ◐ |
| Glossary six-field shape + full term coverage + in-text resolution | ✓ (32→39 × 6) | ✗ (19 × 3, used terms missing) | ✓ (40 × 6) | ✓ (§1.1 pre-existing; *shape* scannable post-08-13) | ✓ (post-08-13) | ✓ (XS term set) | ◐ |
| Branched dependency concept map + closing revisit | ✓ (revisit added by R12 repair) | ✗ (linear strip) | ✓ (18 nodes, revisited) | ✓ (post-08-13 checklist item) | ✓ (post-08-13) | ✓ (XS declares nodes/edges) | ◐ |
| Reveal arcs that pay off | ✓ (wᵀx U2→U5) | ✗ (dangling promise) | ✓ (U2→U6; (AᵀA)⁻¹ U8→U9) | ✓ (post-08-13) | ✓ (post-08-13) | ✓ (LP declares payoff unit) | ◐ |
| Signature manipulable visual per central concept | ✓ (span lattice, error squares, warped grid…) | ✗ (generic canvases) | ✓ (lattice, city-block, warped grid, greying…) | ✓ (post-08-13, P-14 + XS) | ◐ (presence, not quality) | ✓ (LP/XS fields) | ✗ (quality is judgment) |
| Goal-directed, manipulable widgets (no fake Explore) | ✓ (12 + matching) | ✗ (1 zero-input demo) | ✓ (13) | ✓ (§4 + post-08-13 manipulability item) | ✓ (post-08-13) | ✓ (XS per-widget variables) | ◐ |
| Bounded/autoscaled canvases | ✓ (R14 + autoscale repairs) | ✗ (typed inputs unbounded) | ✓ (bounded/autoscale; 3 in-gen fixes) | ✓ (post-08-13; §10) | ✓ (post-08-13 extrema check) | ✓ (XS bounds fields) | ◐ (one run) |
| Live-computed widget math (no hard-coding) | ✓ | ✓ | ✓ | ✓ (§1.1, prompt) | ✓ (Audit 2) | ✓ | ✓ (consistent across 3 runs) |
| Degenerate-state guards | ✓ | ◐ (some guards; extrema missing) | ✓ | ✓ (§4) | ✓ (Audit 2/5) | ✓ | ◐ |
| Responsive + print + reduced-motion + no-JS readability | ◐ (all present; 15.5px < 16px at ≤640px) | ✓ (per handler/static evidence) | ✓ | ✓ (§1.1/§10) | ◐ (static/handler-level only; no rendered pass) | ✓ | ✗ (rendered behavior never verified) |
| Measured WCAG AA contrast | ✓ (measured in Revision 1) | ✓ (5.07:1) | ✓ (4.86:1) | ✓ | ✓ (measured, scripted) | ✓ | ✓ (consistent) |
| localStorage review list + reset | ✓ | ✓ | ✓ | ✓ (P-13/§1.2) | ✓ (behavioral sim) | ✓ | ✓ (consistent) |
| Per-unit ledes + worked example before widget (depth bar) | ✓ | ✗ | ✓ | ✓ (post-08-13 only) | ✓ (post-08-13) | ✓ (LP depth pass) | ◐ (one run) |
| Visual/component consistency (tokens, badges, callouts) | ✓ | ◐ (same token family, thinner system) | ✓ | ✓ (§10 token set) | ✗ (no check measures consistency/polish) | ◐ (tokens named; polish not) | ✗ (judgment) |
| XS conformance (spec ships element-for-element) | ✓ (post-revision) | ✗ (norm comparator, 3 ladders missing) | ✓ (conformance sweep, item 13) | ✓ (post-@0.4.0 hard constraint) | ✓ (post-08-13) | ✓ (XS as contract) | ◐ (one run) |
| Provenance: header comment + colophon; no claims | ✓ (retrofitted 08-13) | ✓ | ✓ | ✓ | ✓ (Audit 5 colophon item) | ✓ | ✓ (consistent) |
| Rendered-output correctness (no console errors, layout, real interactions in a browser) | Unknown | Unknown | Unknown | ✗ (no stage requires it) | ✗ (handler-level simulation only — MEM-2026-0003) | ✗ | ✗ |

*V4/V5 counts from MEM-2026-0004's scripted comparison and EVAL-2026-0005; V6 counts scripted in EVAL-2026-0004/0005; all re-verified where noted in §6–§7.*


---

## 9. Detailed Workflow Gaps (Findings Register)

Findings use the mandated structure. Severity reflects impact on reliably reproducing benchmark quality.

## WF-001 — The benchmark's generation instruction is not durably persisted

**Category:** Persistence / Benchmark
**Severity:** Critical

### Finding

V4 was generated from "the owner's 30-section brief + approved plan" (prompt digest `f1a43cbf21cf`). The brief's full text exists nowhere in the repository: RUN-20260810-0001 Appendix A preserves only a *condensed snapshot*, explicitly "preserved out-of-band at generation time (operator session log)." The prompt cards @0.1.0–@0.4.0 each state "Substance derived from the v4 generation instruction (snapshot digest `f1a43cbf21cf`) generalized to any source document" — a derivation whose fidelity cannot be verified, because the source text is absent. Contrast: V3's generation prompt *is* preserved verbatim (RUN-20260804-0002 Appendix A, digest `70ec9b15aeeb`). The benchmark's prompt is preserved **worse** than a non-benchmark candidate's.

### Evidence

RUN-20260810-0001 (input manifest row "Prompt"; Appendix A); RUN-20260804-0002 Appendix A; library/prompts/prm-generator-lesson-standard@0.1.0.md §Change rationale; LP-2026-0002 references "the owner's brief §20" — proving the brief had numbered sections the records quote but never reproduce.

### V4 benchmark

V4's depth, pedagogical moves, and constraints were specified *in the brief itself* (variant evaluation; evidence-based redesign; prediction gates, faded ladders, misconception checks, interleaved mastery with confidence calibration; glossary, concept map, localStorage review — per the condensed snapshot).

### V5/V6 evidence

V5 used card @0.3.0 (the derived generalization) and collapsed to the compliant minimum (MEM-2026-0004). V6 used @0.4.0, which repaired the collapse by adding an explicit depth bar — i.e., the card had to be *patched toward* the brief's effect after a failure exposed the delta.

### Workflow reality

The prompt architecture requires "rendered prompt content is recorded as a digest plus controlled-access snapshot in every generation run" ([prompt-architecture](../05-prompts/prompt-architecture.md)). A digest exists; the controlled-access snapshot for V4 does not (in-repo).

### Gap

The single most important input to the benchmark artifact is unrecoverable from repository evidence. Any claim that the current prompt cards encode "what produced V4" rests on an unverifiable derivation performed from memory.

### Confidence

High (Observed absence; Inference for the derivation-fidelity consequence).

### Notes

The same pattern repeats for V4's comparative variant audits: EVAL-2026-0002 states the coverage matrix "ships with the owner's deliverable summary, which is outside this repository"; the matrix was reconstructed into the record only on 2026-08-13 (Appendix C).

## WF-002 — The workflow was codified *from* V4 one day later; codification captured rules, not calibration

**Category:** Requirement
**Severity:** High

### Finding

Commit `3453c6d` (2026-08-11) created the lesson standard, generation workflow, pattern catalog, QA checklist, and prompt card @0.1.0 — all explicitly "v4-derived" (ADR-0004). The extraction encoded *what elements must exist* (gates, ladders, constructed response, layered labels) but not *how much* of each constitutes benchmark depth. V5 then complied with every encoded rule while shipping ~44% of V4's content mass and losing its signature techniques (MEM-2026-0004: "The workflow verified the floor and could not see the missing depth; the rubric confirmed the blindness by scoring both candidates identically").

### Evidence

ADR-0004 (Context: v4's decisions "lived only inside the artifact and its run records. Without codification, the next lesson could silently regress"); commit stats for `3453c6d`; MEM-2026-0004 §Lesson; EVAL-2026-0003 scorecard vs EVAL-2026-0002 (both 3.59 after ADR-0007 recomputation).

### V4 benchmark

V4's depth was *designed against failure evidence* — three comparative variant audits identified what passive lessons lack; XS-2026-0002 states the strategy: invest "its complexity budget in the assessment-and-scaffolding layer."

### V5/V6 evidence

V5: F-1 depth collapse (§7). V6: depth restored only after the 08-13 retrofit added depth floors to the CM/LP/XS templates and a depth bar to the prompt.

### Workflow reality

Post-08-13, depth is a stated requirement at every layer (template floors, LP depth pass, XS conformance contract, prompt items 10–13, checklist depth items, framework diagnostic anchors).

### Gap

The codification step lost the calibration that made the benchmark; the repair is validated by exactly one run (WF-014).

### Confidence

High.

### Notes

This is the central structural finding: post-hoc codification of an iterative success systematically under-encodes the qualities that iteration produced.


## WF-003 — The adversarial revision cycle that produced the benchmark is optional, not forced

**Category:** Process / Validation
**Severity:** Critical

### Finding

V4 reached benchmark quality only after *Revision 1*: an owner-requested, post-evaluation adversarial audit (scripted structural audit + two isolated adversarial sub-audits + handler-level behavioral simulation) that found 3 Major and 11 Minor/nit defects **in an artifact that had already passed the entire standing verification suite** (MEM-2026-0003). V5 and V6 each closed with **revision cycles = 0** (ADR-0006 counters in their run ledgers): both passed their gates diagnostically on the first build, and nothing in the workflow forces a revision pass when gates pass.

### Evidence

RUN-20260810-0001 §Revision 1 (defect table R1–R15 with root causes; regression checks re-run); MEM-2026-0003 ("None was visible to structural checks"); RUN-20260813-0001 (revision cycles 0); RUN-20260813-0002 (revision cycles 0; 10 in-generation corrections); quality-loop state machine (revision is *available* via `reflecting→revising`, not mandated).

### V4 benchmark

The shipped benchmark contains the Revision-1 repairs: the Unit-6 AᵀA/Aᵀb Foundation derivation (R1 — a dependency breach at the lesson's climax), confidence routing on numeric items (R2 — dead UI), the quadrant-safe angle arc (R3 — a rendering logic bug), JS-applied `hidden` for no-JS safety (R4), the wᵀx wording fix (R5), honesty/provenance fixes (R8/R9), the non-memorizable mastery norm item (R10), 7 added glossary entries (R11), the paid-off concept-map revisit (R12), the notation-honesty note (R13), and the ~920px least-squares window (R14).

### V5/V6 evidence

V5 shipped F-1…F-7 with zero revision cycles; several of its Majors (recognition-only checks, dangling promise, unbounded canvases) are the *same defect classes* V4's Revision 1 repaired (R12 ↔ F-7; R14/v2-outlier ↔ F-6; MEM-2026-0002 ↔ F-4). V6's depth success was achieved inside a single generation (10 in-generation corrections), still without any post-evaluation adversarial pass.

### Workflow reality

The quality loop *permits* targeted revision and the retry policy governs it, but closure as `private-pilot-complete` requires only: evaluation + reflection + disposition. Gates passing ⇒ no forced revision. The adversarial audit that created the benchmark is institutionalized as *checklist content* (audits 3/5) but not as a *mandatory adversarial pass over a passing build*.

### Gap

The workflow's stopping condition cannot distinguish "nothing left to find" from "our instruments can't see it." V4's own history is the counter-evidence: its three worst defects were invisible to the suite that passed it.

### Confidence

High (Observed).

### Notes

MEM-2026-0003 records the mechanism: "syntax/structure/recomputation verify *statics*; dependency order and interactive behavior are *dynamic/sequential* properties." The lesson was codified as gates; the *practice* of adversarial re-examination after a pass was not codified as a requirement.

## WF-004 — Upstream record depth bounds generation depth; floors arrived only after the failure

**Category:** Context / Handoff
**Severity:** High

### Finding

MEM-2026-0004 (§Why this is believed): "The depth gap originated upstream: CM-2026-0002 (~1/3 the depth of CM-2026-0001) and a lighter LP/XS bounded what generation could produce." Verified: CM-2026-0001 is 108 lines with a full concept/definition/anchor table and a 27-claim list; CM-2026-0002 is 38 lines with a compressed concept list and ~13 key claims; CM-2026-0003 is 151 lines with 40 anchored claims and 15 distractor-ready misconceptions (its acceptance criteria explicitly cite the "~13-claim floor that preceded CAN-2026-0004"). LP-2026-0003 (41 lines) vs LP-2026-0002 (72) and LP-2026-0004 (83, with the mandatory depth-pass table) show the same gradient.

### Evidence

The six CM/LP records themselves; templates/concept/concept-model.md ("Depth floor: one anchored claim per concept … A thin claim list starves every downstream layer — CM-2026-0002 at ~1/3 the depth of CM-2026-0001 preceded the compliant-but-thin CAN-2026-0004"); templates/learning/learning-plan.md (mandatory depth pass since 2026-08-13); commit `8db0c1a`.

### V4 benchmark

V4 consumed the deepest CM in the lineage plus a redesign LP informed by variant audits.

### V5/V6 evidence

V5's thin CM/LP/XS produced a thin artifact even though the *prompt* demanded the standard in full. V6's depth-floor records + depth-bar prompt produced reference-band depth.

### Workflow reality

Since 08-13 the templates carry floors; conformance is checkable; P2's depth pass is mandatory.

### Gap

Pre-08-13, nothing connected "CM thoroughness" to "artifact depth" — the handoff carried whatever the author happened to write. Post-08-13 floors are template *guidance text*, not machine-checked minima; their effectiveness has one data point.

### Confidence

High.


## WF-005 — Benchmark awareness was deliberately excluded from the regeneration run

**Category:** Benchmark / Context
**Severity:** High

### Finding

V5's run was designed as a clean pipeline test: "Prior artifacts v1–v4: **not read, not consulted**" (RUN-20260813-0001 input manifest). Yet V4's own quality was *caused* by benchmark-class information: its redesign consumed comparative audits of v1–v3 (RUN-20260810-0001 objective (a); EVAL-2026-0002 scope). The workflow has no concept of "the current quality bar artifact" as generation context — the standard names CAN-2026-0003 as reference implementation, but nothing feeds that reference (or its measured characteristics) into P1–P4.

### Evidence

RUN-20260813-0001 (input manifest; purpose statement); RUN-20260810-0001 (objective (a), input manifest "Prior candidates … Evaluated comparatively in this run"); RUN-20260813-0002 ("v4/v5 consulted only at P6 for the comparison table"); lesson-standard.md header (reference implementation line); benchmark-strategy.md ("No benchmark suite exists yet").

### V4 benchmark

V4 is explicitly the product of benchmark-relative design: keep v1's best idea (error-area squares), repair v2's outlier canvas, repair v3's hard-coded AB/BA contradiction and aria chatter (EVAL-2026-0002 disposition table).

### V5/V6 evidence

V5, denied that context, reintroduced v2's off-canvas defect class (F-6) and regressed v4's signature techniques (F-1/F-3). V6 reintroduced benchmark awareness narrowly: LP-2026-0002 consulted as "reference-depth calibration exemplar," and @0.4.0's success criterion is "matches the reference implementation (CAN-2026-0003) technique-for-technique."

### Workflow reality

The pipeline knows *rules about* the benchmark but not *the benchmark*. Memory items and pattern anti-patterns carry prose summaries of what failed; the artifact-level target (what 178 KB of depth looks like structurally) is not an input.

### Gap

"Produce V4-level quality" is currently translated into "satisfy the rules that were extracted from V4" — a lossy proxy demonstrated by the identical 3.59 scores for V4 and V5.

### Confidence

High.

### Notes

Whether deliberate exclusion was right *for that experiment* is out of scope; the finding is that the workflow's default context assembly contains no benchmark representation.

## WF-006 — No stage of the pipeline verifies rendered output

**Category:** Validation
**Severity:** Critical

### Finding

Every technical check in the pipeline operates on source text or a hand-rolled DOM/canvas stub: `node --check`, zero-dependency scans, duplicate-ID/wiring scans, scripted recomputation, handler-level behavioral simulation, computed-contrast measurement. MEM-2026-0003 states the boundary: handler simulation "catches logic defects, not rendering fidelity. A real-browser pass remains a distinct check." EVAL-2026-0005 repeats it: "behavioral claims verified at handler level in source, not executed in a browser; no screen-reader pass." No governed run records any browser-rendered evidence — for *any* candidate, including the benchmark.

### Evidence

lesson-generation-workflow P5 (audit methods column); lesson-qa-checklist Audit 5 (all items are static or handler-level); MEM-2026-0003 §Counterexamples; EVAL-2026-0005 §Reviewer relationship; EVAL-2026-0002/0003/0004 evidence sections; `scripts/` contains no artifact-execution tooling (check-repo.py "never … executes or scores learner artifacts").

### V4 benchmark

V4's R3 (angle-arc quadrant bug) and R14 (~1240px portrait canvas) are precisely rendered-behavior defects — both found by a human-driven adversarial audit, not by the suite. V4's current 15.5px sub-breakpoint (§6.6) is a rendered-layout property no check flags.

### V5/V6 evidence

F-6 (off-canvas rendering in v5) was findable statically because inputs lacked min/max; the *class* of defects (crashing interactions, visual glitches, responsive breakage, polish) is systematically invisible to the pipeline's instruments. The audit mandate's symptom framing (runtime failures, UI inconsistencies, cropping, responsiveness) has no in-repo evidentiary basis in either direction — neither confirmation nor refutation is possible from the records (see §14).

### Workflow reality

"Exit: candidate renders from `file://`" (P4) is asserted by the operator; no tool, protocol, or record field captures rendered evidence (screenshots, console capture, interaction traces).

### Gap

The verification ceiling is handler-level logic. Everything a learner actually *sees* — layout, canvas rendering, visual polish, responsive behavior — is outside guaranteed verification.

### Confidence

High (Observed absence).


## WF-007 — The scoring rubric could not distinguish the benchmark from its collapse

**Category:** Validation / Benchmark
**Severity:** High

### Finding

V4 (3.59, post-ADR-0007 recomputation) and V5 (3.59) received identical weighted scores despite a documented, dramatic depth difference. The evaluation framework's own change history records the cause: "The whole-point rubric anchors are generic by design, which let two materially different candidates score identically (CAN-2026-0003 and CAN-2026-0004; MEM-2026-0004)." The 08-13 remedy adds "Stage 1 dimension anchors (diagnostic)" — explicitly diagnostic, changing "no weight, gate, or eligibility rule."

### Evidence

evaluation-framework.md (change history 2026-08-13 entries; §Stage 1 dimension anchors); EVAL-2026-0003 scorecard (all dimensions 3.5 except accuracy 4.0); EVAL-2026-0002 Appendix B (recomputed 3.59); MEM-2026-0004.

### V4 benchmark

V4's scorecard already carried uncertainty markers (confidence medium/low on most dimensions; accessibility 3.0 with a release-blocking Major caveat).

### V5/V6 evidence

V5's 3.59 was issued against the *pre-amendment* checklist; EVAL-2026-0005 confirms the depth items it would later fail "were added on 2026-08-13 *because of* CAN-2026-0004." V6 scored 3.76 — the first score to reflect depth-band differences.

### Workflow reality

Gates are numeric and auditable (post-ADR-0007), but sensitivity to the benchmark's distinguishing qualities is provided by non-binding diagnostic anchors.

### Gap

For the period before the retrofit, the pipeline's gate authority certified the collapse as benchmark-equal. The score is a release signal, not a depth detector — and the depth detector is diagnostic-only.

### Confidence

High (Observed).

## WF-008 — Audit execution is self-certified; an unexecuted check is indistinguishable from a passed one

**Category:** Validation
**Severity:** High

### Finding

V5's run ledger records Audit 4 as PASS with "ladders for Σ/dot/norm" — the artifact ships one dot ladder plus a single norm rung, and two recognition-only unit checks breached an *explicit* standard rule (§5). Both the ledger and EVAL-2026-0003 required dated errata (2026-08-14 retrospective appendices). MEM-2026-0004 names the mechanism: "an unexecuted check is indistinguishable from a passed one." The same operator authors the artifact, executes the audits, records the evidence, and scores the result; no structural control verifies execution.

### Evidence

RUN-20260813-0001 (Audit 4 PASS + 08-14 erratum); EVAL-2026-0003 (scorecard + retrospective appendix); MEM-2026-0004 ("Why this is believed," item 2); EVAL-2026-0005 records-consistency findings 1–2; workflow-architecture.md §Separation of duties (permits recorded non-independent passes at Stage 1).

### V4 benchmark

V4's audit evidence includes reproducible artifacts (44 recomputations, handler-simulation counts) — but was likewise self-executed; its Revision-1 adversarial audit was *owner-requested*, not workflow-forced.

### V5/V6 evidence

V5: false PASS documented above. V6: EVAL-2026-0005 re-executed the checks and reproduced every claim exactly — demonstrating that re-execution *works as a control* and that it happened only as a separate, later, owner-initiated audit.

### Workflow reality

The checklist demands "every checked box cites its evidence," but evidence-citation is itself self-reported; the repository checker validates link/hash/status hygiene, not audit execution.

### Gap

The pipeline's gates are assertions about execution, with no second pair of eyes at Stage 1. The one time re-verification ran (EVAL-2026-0005), it found two record-level errata.

### Confidence

High (Observed).


## WF-009 — The benchmark artifact was mutated after evaluation, outside the generation workflow

**Category:** Process / Consistency
**Severity:** Medium

### Finding

The current V4 bytes (`b35c622e`) incorporate: Revision-1 repairs (in-workflow), owner-directed clarifying edits and explorer un-gating (`2ee0f38`, 2026-08-11, +75/−29 lines), the retrofitted colophon (`5da2754`, 08-13), and banner/footer removal (`27de79e`, 08-13). None of the 08-11/08-13 edits went through a governed run, and the artifact as a whole was never re-evaluated afterward; records track the changes via dated appendices, and identities were carried forward per the append-only-note conventions.

### Evidence

Git history (`2ee0f38`, `5da2754`, `27de79e`); module README "Provenance and notes"; RUN-20260810-0001 Appendices B–C; XS-2026-0002 retrospective note; EVAL-2026-0002 header (pre-revision hash retained).

### V4 benchmark

The benchmark's current state is thus "evaluated build + governed revision + three owner-directed edit passes." The pedagogy-affecting one (explorer un-gating, 08-11) postdates the evaluation that scored the gates' design.

### V5/V6 evidence

Not applicable to those artifacts directly; relevant because V5/V6 were compared against a *moving* benchmark whose identity is maintained by appendix chains.

### Workflow reality

Naming conventions require a new governed run for version changes; owner directives amended the artifacts retroactively with record-keeping but without re-evaluation.

### Gap

"Which artifact is the benchmark" is answerable (hash-verified, §0); "which evaluated state the benchmark's quality claim rests on" requires assembling four events across three days.

### Confidence

High (Observed). Severity held at Medium because traceability was maintained throughout.

## WF-010 — Single source, single model family, single operator: the guarantee base is narrow

**Category:** Consistency / Benchmark
**Severity:** Medium

### Finding

All governed candidates derive from one source package (SRC-2026-0001); all Claude-era generations (v3–v6) ran through one harness family (Cline terminal) with the exact model identifier "not exposed"; every review is non-independent (author = reviewer); no learner has used any artifact; no screen-reader pass exists. The records disclose all of this meticulously — the limitation is structural to Stage 1, not concealed.

### Evidence

records/README.md scoreboard ("1 package; fallback satisfiable as limited evidence"; "Independent review: none yet"); RUN ledgers' model rows; EVAL records' independence fields; ADR-0002/0003.

### V4 benchmark

The benchmark's educational-quality claims rest on literature citations + non-independent audits (EVAL-2026-0002: "no learner has used it; no efficacy evidence exists").

### V5/V6 evidence

V6's "hypothesis supported" verdict (depth restored in one generation) is one run, one source, one operator, one model family (EVAL-2026-0004 §Disagreement).

### Workflow reality

The calibration commitment (three pilots, ≥2 source packages or the recorded fallback) is *met numerically* with 4 pilots / 1 package as "limited evidence"; framework weights remain provisional.

### Gap

Nothing measured the pipeline's variance: same-input regeneration has been tried exactly once per prompt version, and cross-source generalization is untested (Class 2 awaits source per the module README).

### Confidence

High (Observed).


## WF-011 — Requirement text exists, but several benchmark qualities remain judgment-dependent end-to-end

**Category:** Implementation / Consistency
**Severity:** Medium

### Finding

A set of V4-defining qualities has, even after 08-13, no checkable definition: visual "polish" and hierarchy quality; analogy and lede quality ("Every dataset is three shapes of numbers" is *authored*, not verifiable); signature-visual *aptness* (P-14 requires "one memorable, manipulable image" — presence is checkable, aptness is not); information density vs cognitive-load balance; prose readability. The pipeline can require their presence and verify their existence, but their *quality* rides on model/operator judgment each run.

### Evidence

lesson-standard §10 (tokens/hard rules are checkable; aesthetic intent is not); lesson-patterns P-14; checklist Audit 4 (checks name presence/counts, not quality); EVAL confidence columns ("medium" on visual clarity for both v4 and v6).

### V4 benchmark

V4's most-praised qualities per the pattern catalog (P-14: "CAN-2026-0003's most-praised artifacts are exactly these") are judgment artifacts of the iterative process.

### V5/V6 evidence

V5's collapse was partly *quantitative* (counts) and partly qualitative (no vivid signature visuals). V6 restored counts; quality parity with V4 is asserted by the owner, "corroborated by scripted counts but not by a learner pilot" (EVAL-2026-0004 §Disagreement).

### Workflow reality

No instrument, rubric anchor, or gate measures these; the framework's generic anchors leave them inside half-point judgment bands.

### Gap

Benchmark-level *taste* is a human-iteration product that the workflow references but cannot specify.

### Confidence

Medium-High (Observed absence of measures; Inference that this explains part of the perceived quality delta).

## WF-012 — Dual benchmark identity: the standard's reference and the module's reference diverge

**Category:** Benchmark
**Severity:** Low

### Finding

The lesson standard names CAN-2026-0003 (v4) as **the reference implementation**; the module README names v6 (CAN-2026-0005) as **the reference lesson**; the @0.4.0 card's success criterion is defined against v4. Commit `9324bf7` adopted "reference-candidate terminology," but the two designations live in different documents with different meanings (pedagogical exemplar vs current best candidate).

### Evidence

lesson-standard.md line 7; module README "Governed-generation status"; prm-generator-lesson-standard@0.4.0.md §Evaluation set.

### Gap

For this audit the owner designated V4 as the benchmark; the workflow's documents do not unambiguously say which artifact *is* the quality bar for the next generation, nor what "match the reference" demands when the reference itself has post-evaluation edit history (WF-009).

### Confidence

High (Observed).


## WF-013 — Every workflow strengthening has been reactive; no capability was added ahead of a failure

**Category:** Process
**Severity:** Medium (diagnostic of a systemic pattern)

### Finding

The workflow's quality apparatus grew exclusively by post-failure retrofit: recognition-only assessment (v1–v3) → MEM-2026-0002 + §5 floors; escaped dynamic defects (v4 pre-revision) → MEM-2026-0003 + audits 3/5; prompt-identity weakness (v2) → snapshot practice → prompt cards; gate-arithmetic defect → ADR-0007; iteration ambiguity → ADR-0006; compliant-minimum collapse (v5) → the entire 08-13 depth apparatus. The pattern catalog itself records this: P-01/P-02/P-14/P-15 entries now embed CAN-2026-0004 contrast cases added after the failure.

### Evidence

Commit sequence in §5; ADR-0004/0006/0007 contexts; MEM-2026-0001…0004 evidence rows; pattern catalog change notes; checklist origin note and 08-13 additions.

### V4 benchmark

V4 is simultaneously the source of the codified capabilities and the beneficiary of the only proactive quality instrument ever used: comparative audits of prior variants (themselves reactive to the owner's dissatisfaction with v1–v3).

### V5/V6 evidence

V5's collapse was the price of discovering the codification gap; V6's success is the first instance of a capability (the depth bar) being added reactively *and then working on its first subsequent run*.

### Workflow reality

The P6 curation step institutionalizes reactive learning ("any defect class that escaped → add the check that would have caught it"). There is no complementary instrument that asks "what could the next lesson lose that has never failed yet?" — the roadmap defers benchmark/harness work to later stages.

### Gap

The system learns only from failures it actually ships. For a one-source corpus this is survivable; for a new source, every un-anticipated defect class ships once before it is guarded.

### Confidence

High (Observed pattern; the projection to new sources is Inference).

## WF-014 — The depth-bar remediation is validated by exactly one run

**Category:** Consistency / Benchmark
**Severity:** Medium

### Finding

The 08-13 apparatus (prompt @0.4.0 depth bar + conformance sweep; CM/LP/XS template floors; checklist depth items; framework diagnostic anchors) has one governed execution: RUN-20260813-0002 (V6). It succeeded. MEM-2026-0004 had flagged the fallback: "if depth still does not materialize, the lever moves to XS-level enumerativeness" — not needed, per EVAL-2026-0004. RUN-20260813-0002's reflection records the residual risk: "the remaining thin spots of v5's pipeline stage (a thin CM starving downstream) were addressed by template floors, not proven unnecessary."

### Evidence

RUN-20260813-0002 (objective, reflection); EVAL-2026-0004 (comparison table, verdict); MEM-2026-0004 (limitations); prompt card @0.4.0 (hypothesis + outcome).

### Gap

Single-run, single-source, single-operator, non-independent confirmation; no replication on a fresh source; no replication under a different model; no evidence about robustness when the operator is *not* the person who wrote the standard.

### Confidence

High (Observed).

## WF-015 — Iteration knowledge that lived in sessions was partially lost before persistence rules caught up

**Category:** Persistence
**Severity:** Medium

### Finding

Several pieces of V4-era knowledge existed only transiently: (a) the full 30-section brief (WF-001); (b) the three isolated variant-audit reports behind the redesign (summarized in records; full texts in the "owner's deliverable summary … outside this repository"); (c) the original coverage matrix (reconstructed into EVAL-2026-0002 Appendix C on 08-13, three days later); (d) v3's evaluation (never performed; formally deferred 08-11, RUN-20260804-0002 Appendix B). Persistence discipline visibly tightened over the period (snapshot practice from 08-04; ADR-0006 iteration accounting from 08-11; retrospective appendices as the correction mechanism), but the benchmark-forming knowledge predates the discipline.

### Evidence

RUN-20260810-0001 App. A; EVAL-2026-0002 §Pedagogical audit + Appendix C; RUN-20260804-0002 App. B; ADR-0006 context ("Nobody can currently answer 'how many iterations did this candidate really go through?'").

### Gap

The repository's reconstruction of *why V4 is good* is assembled from appendices and condensed snapshots — complete enough to audit (this document exists), incomplete enough that the benchmark's generative instruction cannot be re-run verbatim.

### Confidence

High (Observed).


---

## 10. Capability Loss Points

Where each significant benchmark capability stops being guaranteed, traced through the actual pipeline. **Era matters:** the workflow changed on 2026-08-13; entries show the V5-era (pre-08-13) and current (post-08-13) loss points.

| Capability cluster | P1 CM | P2 LP | P3 XS | P4 Generation | P5 Audits | P6 Eval/closure |
| --- | --- | --- | --- | --- | --- | --- |
| Coverage & math accuracy | ✅ anchored claims | ✅ | ✅ | ✅ | ✅ (Audits 1–2) | ✅ |
| Dependency order | ✅ chains | ✅ sequence | ✅ | ✅ | ✅ (Audit 3) — *but V4's R1 escaped it; caught only by adversarial revision* | ✅ |
| Constructed response / mastery design | ✅ (misconceptions listed) | ✅ planned | ✅ | ⚠️ V5: shipped recognition-only checks | ❌ V5-era: Audit 4 false PASS → ✅ post-08-13 (per-unit naming) | ⚠️ rubric insensitive pre-08-13 |
| Depth (ledes, ladders per skill, signature visuals, explain items, glossary shape, map structure) | ❌ V5-era: no floor (thin CM) → ✅ post-08-13 floor | ❌ → ✅ depth pass | ❌ → ✅ conformance contract | ❌ @0.3.0: no depth bar → ✅ @0.4.0 items 10–13 | ❌ → ✅ depth items | ❌→◐ diagnostic anchors only |
| Gate fidelity / widget manipulability | n/a | ✅ intended | ✅ specified | ⚠️ V5: hollow gates, zero-input Explore shipped | ❌ pre-08-13 (untestable) → ✅ | ⚠️ |
| Spec conformance | n/a | n/a | ✅ contract | ❌ @0.3.0: no conformance duty → ✅ @0.4.0 sweep | ❌ → ✅ | ⚠️ |
| Canvas bounds / off-canvas safety | n/a | n/a | ⚠️ V5: bounds unspecified | ❌ V5: unbounded inputs shipped | ❌ pre-08-13 → ✅ extrema check | ⚠️ |
| Reveal-arc payoff | n/a | ✅ arc declared | ✅ | ⚠️ V5: promise dropped silently | ❌ pre-08-13 → ✅ | ⚠️ |
| Rendered-output correctness (layout, real browser behavior, visual polish) | n/a | n/a | ◐ intent declared | ◐ self-check only | ❌ **no stage, any era** | ❌ |
| Benchmark-relative calibration ("as deep as V4") | ❌ no benchmark input | ◐ post-08-13: exemplar consultation | ◐ | ◐ @0.4.0 success criterion references it | ❌ | ◐ comparison counts at P6 only |

**Reading (Inference, high confidence):** before 08-13 the dominant loss point was *distributed*: depth was assumed at every stage and required at none (MEM-2026-0004). Post-08-13, the remaining structural loss points are (1) **P5's verification ceiling** — nothing sees rendered output (WF-006); (2) **P5's execution assurance** — checks are self-certified (WF-008); (3) **closure** — gates passing ends iteration, so no adversarial pass runs (WF-003); (4) **P0–P3 context assembly** — the benchmark artifact itself is never an input (WF-005).


---

## 11. Root-Cause Analysis

### RC-1 — V5's compliant-minimum collapse

```text
Observed: v5 = 78KB with hollow gates, 1/4 ladders, recognition-only checks (EVAL-2026-0005 F-1…F-7)
  ↓ Artifact cause: elements absent or at floor (line evidence, §7)
  ↓ Generation cause: @0.3.0 demanded rules, not depth; no conformance duty (card items 1–9 only)
  ↓ Planning cause: CM-2026-0002 ~1/3 CM-2026-0001's depth; LP-2026-0003 named 4 ladders without depth floors (WF-004)
  ↓ Validation cause: Audit 4 false PASS; checklist had no depth/manipulability/gate-fidelity items (WF-008)
  ↓ Evaluation cause: rubric anchors generic → 3.59 == v4's 3.59 (WF-007)
  ↓ Process cause: gates passed → 0 revision cycles; no adversarial pass (WF-003)
  ↓ Context cause: v1–v4 deliberately excluded from generation context (WF-005)
Conclusion: the workflow had no representation of depth as a requirement at any stage,
and no instrument that could notice its absence. All seven causes were necessary for
the collapse to ship uncaught; the 08-13 retrofit addresses the first six at
requirement/validation level, none at rendered-behavior level.
```

### RC-2 — V4's benchmark quality

```text
Observed: v4's distinctive qualities (depth, gates, ladders, mastery design, repair of source defects)
  ↓ Artifact: 1,772-line artifact; verified identity b35c622e
  ↓ Generation: owner's 30-section brief (full text unpersisted, WF-001) + deepest CM + audit-driven redesign LP
  ↓ Iteration: 4 in-generation corrections + Revision 1 adversarial audit (3 Majors escaped the suite; MEM-2026-0003)
  ↓ Post-hoc: codification commit 3453c6d extracted rules the next day (WF-002)
Conclusion: benchmark quality = (rich transient instruction) × (failure-informed plan) ×
(manual adversarial iteration). Of these, the workflow encodes the plan *layer*
(templates/workflow) but not the instruction's full content or a mandatory adversarial pass.
```

### RC-3 — Recurring defect classes across eras

```text
Observed: off-canvas rendering v2 (outlier) → repaired in v4 (autoscale) → reintroduced in v5 (unbounded inputs) → bounded in v6
          dangling promise v4 (R12, concept-map revisit) → repaired in Revision 1 → reintroduced in v5 (wᵀx) → checklist-guarded post-08-13
          recognition-only assessment v1–v3 → repaired in v4 → re-shipped in v5 units 6/7 → per-unit evidence required post-08-13
  ↓ Memory existed for each class (MEM-2026-0001/0002/0003; pattern anti-patterns)
  ↓ Retrieval is advisory; nothing forces memory consultation at P2–P4 (memory-architecture: "It is advisory")
  ↓ Checklist coverage lagged: the scannable check for each class was added only after its 08-13 reappearance
Conclusion: memory without forced retrieval or a matching executable check does not prevent
regression. (Diagnosis only; no remedy proposed.)
```

### RC-4 — The mandate's visual/runtime symptom framing vs the record

```text
Observed: the audit mandate lists crashing graphs, UI inconsistencies, cropped content, layout/responsiveness problems
  ↓ In-repo evidence (EVAL-2026-0005, designated audit of record): documents structural/depth findings;
    explicitly did not execute a browser; v6 shows zero open defects under its methods
  ↓ Pipeline capability: no stage can produce rendered-output evidence (WF-006)
Conclusion: those symptom classes are unverifiable from repository evidence in either
direction (Unknown, §14). The pipeline's instrument ceiling — not any documented artifact
defect — is the evidenced explanation for why such symptoms could exist undetected.
```


---

## 12. Manual Iteration Dependency

What the V4 human/agent iteration loop provided that the current single-run workflow does not (all Observed unless noted):

| Iteration contribution | Role in V4 | Encoded in current workflow? |
| --- | --- | --- |
| Owner's 30-section brief (detailed quality intent, §-numbered constraints — e.g. "mastery items must not repeat worked examples," LP-2026-0002) | The generation instruction itself | **Partially** — generalized into prompt cards @0.1.0–0.4.0; full text unpersisted (WF-001) |
| Comparative audits of v1–v3 (three isolated evaluator passes, one rubric, one source map) | Diagnosed the defect classes the redesign targeted (recognition-only assessment; passive twiddling; hard-coded contradictions; aria chatter; off-canvas outlier) | **No** — no comparative-audit step exists in P0–P6; its outputs survive only as MEM/pattern prose and EVAL-2026-0002's disposition table |
| Post-evaluation adversarial audit (Revision 1: scripted structural + 2 isolated adversarial sub-audits + handler simulation) | Found R1–R15 *after* the suite passed; all repaired pre-closure | **No** — available via the quality loop, never forced (WF-003) |
| Human visual/UX judgment | Caught R14 (~1240px portrait canvas), R5 wording, R8 honesty mismatch | **No** — no rendered-output stage exists (WF-006) |
| Targeted in-place repairs + regression re-runs | 15 repairs with named root causes; full suite re-run (21/21 handler sims; contrast measured) | **Yes as mechanism** (retry policy, regression-check rule) — **triggered only on gate failure** |
| Owner post-hoc editorial passes | 08-11 clarifications + explorer un-gating; 08-13 colophon/banner decisions | **No** — owner directives operate outside the workflow by design (WF-009) |
| Accumulated session context (the operator's memory of v1–v3 failure texture) | Shaped LP-2026-0002/XS-2026-0002 authoring | **Partially** — distilled into MEM-2026-0001/0002/0003 and pattern entries; retrieval advisory (RC-3) |
| Progressive constraint evolution *during* the run | The brief + plan co-evolved with audit findings | **No** — P4 consumes frozen inputs; mid-run constraint change is a new run |

**Net assessment (Inference, high confidence):** the workflow encodes the *residue* of V4's iteration (rules, patterns, memories) but not its *dynamics* (compare → hypothesize → generate → adversarially audit → repair → re-verify). V5 demonstrated the residue alone is insufficient for depth; V6 demonstrated the residue + depth retrofit restores measured depth — without restoring the adversarial pass or rendered verification.

---

## 13. Single-Prompt Reproducibility Assessment

**Question:** can a new source note enter the current workflow and reliably produce ≥V4 quality in one run, without manual iterative rescue?

**Evidence for (Observed):** V6 did exactly this on the depth dimension — one generation, 0 revision cycles, reference-band depth on every 08-13 checklist item, all records fresh from source (EVAL-2026-0004/0005). The pipeline now carries explicit requirements (standard + depth bar), depth floors (templates), a conformance contract (XS), a conformance sweep (prompt item 13), scannable depth items (checklist), and iteration accounting (ADR-0006).

**Evidence against / unresolved (Observed/Inference):**

1. **One data point.** Same source, same operator, same model family, non-independent (WF-010, WF-014). Variance across sources and models is unmeasured.
2. **The instruction-derivation problem.** The cards claim descent from the V4 brief; the brief is unpersisted, so the fidelity of that descent — and therefore what the cards might still be missing — is Unknown (WF-001).
3. **The verification ceiling.** Rendered behavior, layout, and visual polish are unverified in every candidate ever produced (WF-006). V4-level *rendered* quality has never been measured, so it cannot be guaranteed to reproduce.
4. **Self-certified gates.** The only documented false PASS (v5 Audit 4) occurred in the current self-certification model; the control that caught it (EVAL-2026-0005 re-verification) is itself optional and owner-initiated (WF-008).
5. **Closure dynamics.** A first-build pass ends iteration by default; the adversarial pass that created the benchmark remains optional (WF-003).
6. **Judgment-dependent qualities.** Signature-visual aptness, lede/analogy quality, polish, and density balance have no checkable definitions (WF-011).
7. **Benchmark relativity is positional.** "Match the reference implementation technique-for-technique" is defined on a corpus of one lesson, against a benchmark whose identity has post-evaluation edit history (WF-009, WF-012).

**Verdict (Inference, medium-high confidence):** the current workflow can plausibly reproduce V4's *structural and content-depth profile* in a single run on familiar territory — it has done so once. It does **not** currently contain mechanisms that guarantee V4-level quality for a new source: the guarantee gap concentrates in rendered-output verification, audit-execution assurance, forced adversarial revision, benchmark-context assembly, and judgment-level polish. Every one of these was present in the V4 process as a manual act.


---

## 14. Unknowns and Audit Limitations

**Established as Unknown (searched, not found in repository evidence):**

1. **The full text of the owner's 30-section V4 brief.** Only a condensed snapshot (digest `f1a43cbf21cf`) exists, kept out-of-band. The exact instructions that produced the benchmark cannot be re-run verbatim.
2. **The three isolated variant-audit reports (v1–v3)** behind the V4 redesign. Summaries live in EVAL-2026-0002 and RUN-20260810-0001; the full reports lived in an "owner's deliverable summary … outside this repository."
3. **V3's evaluation.** Never performed; formally deferred (RUN-20260804-0002 Appendix B). The cross-model comparison objective remains open.
4. **Rendered-browser behavior of every candidate.** No browser execution evidence exists for v1–v6. Consequently, the mandate's symptom classes (crashing interactive graphs, runtime failures, UI inconsistencies, cropped/truncated rendering, responsiveness defects, polish) are **Unknown in both directions** — no record confirms them; no instrument in the pipeline could have detected or excluded them. Per owner designation, EVAL-2026-0005 + the retrospective appendices are the V5/V6 audit of record, and its findings are structural/behavioral-at-handler-level (§7).
5. **Whether CM-2026-0003's depth came from the new template floors or from operator memory.** The same operator authored all CMs; the floors and the operator's accumulated knowledge are confounded in V6's single run.
6. **Model identity and configuration** for all Claude-era generations ("not exposed" to the operator; recorded as best-known-not-inferred). Cross-model reproducibility is untestable from records.
7. **Learner-level efficacy of any artifact.** No learner pilot exists; all educational-quality scores are design-intent judgments by a non-independent reviewer.

**Audit limitations:**

- **Non-independent audit.** The auditor operates in the same environment and role-chain that produced the artifacts; this audit mitigates by anchoring findings to mechanically verifiable evidence (hashes, line citations, record cross-references) and marking inference explicitly.
- **Artifact analysis was source-level**, not browser-rendered, matching the evidence ceiling of the records being audited. Static spot-checks performed this audit: v4/v5/v6 scripts pass `node --check`; v5 hollow-gate structure, unbounded inputs, and linear concept map confirmed artifact-side; v4 gate handler, ladders, confidence UI, review-list store confirmed; v6 gate-hiding and per-choice feedback confirmed; v4's 15.5px sub-16px breakpoint noted (§6.6).
- **Point-in-time.** The workflow changed materially on 2026-08-13 between V5 and V6; findings distinguish eras, but "the current workflow" means the post-08-13 state, which has executed exactly once.
- **Single content package.** All evidence derives from one source notebook; nothing here measures cross-source behavior.

**What this audit deliberately does not contain:** solutions, redesigns, prompt rewrites, new agents or gates, or recommendations of any kind. Findings state what is missing, implicit, unvalidated, or unreproducible — and stop there.

---

*Audit trail: repository state at branch `version02`, HEAD `8a300b0`; artifact hashes re-verified 2026-08-14; `scripts/check-repo.py` executed after this document was added (7 checks, 0 failures, 4 pre-existing notes). Prior in-repo audits consulted: EVAL-2026-0001…0005, MEM-2026-0001…0004, all RUN/CM/LP/XS records, and the full git history of the module package.*

