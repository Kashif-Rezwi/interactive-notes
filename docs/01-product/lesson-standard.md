# Lesson Standard (Creative Interactive Notes)

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04 (or after two governed lessons generated under this standard, whichever comes first)<br>
**Adopted by:** [ADR-0004](../adr/0004-lesson-standard-adoption.md)<br>
**Benchmark:** [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, `linear-algebra-foundations-v4.html`, RUN-20260810-0001, EVAL-2026-0002; see [ADR-0011](../adr/0011-benchmark-definition-and-artifact-change-protocol.md))<br>
**Depth calibration:** [depth-calibration-contract.md](depth-calibration-contract.md) defines the measurable rule-based depth floors.

This document is the binding standard for interactive lessons generated from source notes. It codifies the pedagogy validated across four generations of the AIML-4 Module 2 lesson. It extends — never replaces — the [experience principles](experience-principles.md) and the [product brief](product-brief.md); conflicts resolve in favor of those parents.

Two levels are distinguished throughout: **principles** are permanent rules (change only with new evidence); **implementation patterns** are reusable techniques chosen per concept (catalog: [lesson-patterns](../../library/patterns/lesson-patterns.md)). Never confuse the two: a future lesson may replace every pattern and still comply with this standard.

## 1. The Consistency Contract

### 1.1 Required — every lesson MUST have all of these

- **Source coverage with a coverage matrix.** Every source topic is either included or explicitly dispositioned (transcribed / expanded / deliberately excluded with reason). The matrix ships with the evaluation record. Omission is a decision, never an accident.
- **Measurable learning outcomes** in the linked learning plan, each exercised by at least one assessment item.
- **Explain-before-use.** No concept is used to explain another unless already taught or genuinely trivial for the declared learner (rule and detection mechanism in §2).
- **Layered content labels.** Every block is labeled: `CLASS CORE` (from the source) · `FOUNDATION` (prerequisite the source assumed) · `DEEP DIVE` (added intuition) · `ML LINK` (application) · `EXTENSION` (optional, beyond the source) — plus provenance tags `source` / `constructed example` / `supplemental`.
- **Per-symbol formula keys.** Every displayed formula names every symbol in plain language, and states why the formula makes sense and how to read its result.
- **Practice with faded scaffolding** for every computational skill: full worked example → completion problem → independent problem with tiered, never-auto-opening hints.
- **Retrieval-based checks per unit**, each including at least one constructed-response item (numeric entry, fill-in-equation, or explain-in-own-words with a model answer). Feedback on every miss states the governing rule.
- **A mastery assessment** that is interleaved across units, includes at least one reasoning item, one transfer item (a situation not seen in the lesson), and one error-identification item, and does not reuse the lesson's worked numbers.
- **Misconception handling** for every major concept: the anticipated beginner error is named and tested by a distractor a misconception-holder would actually choose.
- **ML connections as mechanisms** where the source makes them (see §6).
- **A glossary** covering every term used, with simple + precise definitions, an example, related terms, and where it appears in practice/ML; in-lesson terms link to it without losing the reader's place.
- **A concept map** (dependency graph) visible early and revisited at the end.
- **Accessibility baseline:** semantic landmarks, logical heading order, keyboard-operable native controls, no drag-only or hover-only interaction, text equivalents for every canvas carrying the same numbers, color never the sole encoder, `prefers-reduced-motion` honored, measured WCAG AA contrast, print fallback for every interactive.
- **Technical baseline:** single file, zero external requests, fully functional offline, graceful behavior with storage unavailable, no-console-error load.
- **Governed provenance:** an HTML header comment records candidate, run, source, model, and prompt identities; lineage lives in the run ledger, and the artifact makes no public-release, benchmark, or efficacy claims anywhere. The learner-facing page carries no governance banner or provenance footer — its only closing element is the standard **colophon**: two muted lines — "Built with ♥ using Interactive Notes" and "AI-generated, so mistakes can sneak in — double-check what matters." — subtle, reduced-motion-safe, printing as plain text, and carrying no status, release, benchmark, or efficacy claims. (Amended 2026-08-13 by owner decision: visible governance banners/footers replaced by the header comment plus the standard colophon.)

### 1.2 Recommended — include unless there is a reason not to

- Prediction-before-reveal gates on the 2–4 most consequential reveals (MEM-2026-0001): the manipulable stays hidden until the learner commits, and the feedback differentiates by the chosen option — a hollow gate that shows answer-independent text teaches nothing. (Amended 2026-08-13 after CAN-2026-0004 shipped hollow gates.)
- Goal-directed exploration tasks on every manipulable (a stated objective, not free play).
- Self-verifying readouts (the widget recomputes an invariant, e.g. residual · direction = 0).
- A "why this matters" motivation block per unit.
- A worked edge case (zero vector, parallel vectors, outlier) — degenerate states teach.
- Confidence calibration on the final assessment only (sure / think so / guessing), with confident misses routed to review.
- A local review list of missed topics, with an explicit invitation to return after a gap (spacing).
- A closing synthesis that re-reads the hardest formula piece by piece after the learner can verify every part.

### 1.3 Conditional — only when the concept genuinely calls for it

- Interactive visualizations/simulations (admit only via the §4 test; a concept with no manipulable causal structure gets none).
- Code examples (when the target learner reads code and it shortens the explanation, e.g. Σ as a for-loop).
- Advanced/extension sections (collapsed, clearly optional, never on the main path).
- Step-through proofs (interview skills; collapsed by default; only where the source or plan calls for them).
- Cross-lesson links (only to concepts that genuinely exist in earlier governed lessons; see §8).

### 1.4 Forbidden — never ship these

- Decorative interaction or animation (no learner action changes a meaningful model).
- Unexplained terminology used as if known (see §2); acronyms expanded nowhere.
- Formula dumping: a formula with no plain-language meaning, symbol key, or interpretation.
- Recognition-only assessment (all multiple choice / matching) — MEM-2026-0002.
- Hard-coded computed values that could be computed live (v3's interview-Q2 contradiction class).
- Unsupported claims: efficacy, "proven to improve", unverifiable external facts; anything beyond the source not labeled supplemental.
- Gamification chrome (points, badges, streaks, leaderboards) and learning-styles framing.
- Walls of text (a block teaching two or more new ideas at once).
- Progress indicators that reward scrolling rather than demonstrating understanding.
- Autoplaying motion; anything moving without a learner action.
- External runtime dependencies (CDN CSS/JS/fonts) in the artifact.

## 2. Explain-before-use (the dependency rule)

**Rule:** never use an unexplained concept to explain another concept, unless the concept is genuinely trivial for the declared learner. "Common in mathematics" is not a triviality test.

**Applies to:** technical terms, nested terminology (a definition containing another new term), mathematical notation, acronyms, CS and ML terms, and prerequisite math.

**Handling, in preference order:** (a) teach it first in a `FOUNDATION` block at the point of need; (b) bridge it inline in one sentence and glossary-link it; (c) defer it, clearly labeled `EXTENSION`, ensuring nothing on the main path depends on it; (d) remove the dependence by re-sequencing (v4 moved the linearity proof after the dot product) or by choosing a more elementary equivalent (v4's area test instead of the determinant).

**Detection mechanism (mandatory):** the dependency-order audit — a separate read of the near-final artifact, in order, maintaining the set of "concepts taught so far"; every new explanation is checked against that set. Any use-before-explain is a Major defect. This gate exists because structural checks cannot see it (RUN-20260810-0001, finding R1).

## 3. Content coverage requirement (the do-not-skip rule)

Pipeline: **Source → Content Inventory → Concept Map → Learning Architecture → Lesson → Coverage Audit → Final**.

- The inventory enumerates every topic, subtopic, definition, formula, example, terminology item, relationship, instructor assumption, and underexplained or missing-but-necessary concept. "Minor-looking" items are included.
- The concept model record (CM) anchors every claim to the source (cell/section anchors).
- Every inventory item receives a disposition: included-as-taught / included-expanded / transcribed-from-opaque-format / added-foundation / added-extension / excluded-with-reason.
- The coverage matrix ships as part of the evaluation evidence. A lesson with an unexplained gap fails the gate.

## 4. Interaction philosophy

**Admission test — answer all five before building:** (1) What concept does it teach? (2) What learner action is required? (3) What does the learner observe? (4) What misconception does it address? (5) What understanding would be weaker without it? No good answers → no interaction; static explanation is a legitimate choice and is recorded as one.

**Approved pattern categories:** Manipulate · Predict · Explore (goal-directed) · Compare · Build · Solve · Debug · Reveal · Simulate · Explain · Practice. Full pattern catalog with trade-offs and anti-patterns: [lesson-patterns](../../library/patterns/lesson-patterns.md).

**Rules:** one manipulated variable at a time before free play; every canvas pairs with a live symbolic readout (dual coding); compute live, never hard-code; guard degenerate states and turn them into teaching moments; unlock-by-commitment, never by correctness; a widget with no learner-manipulable variable is a static demonstration — a legitimate choice that is recorded as one and never badged as an explorer. (Amended 2026-08-13.)

## 5. Assessment philosophy

Assessment is the learning engine, not a quiz appended to content (the single largest defect class in v1–v3; MEM-2026-0002).

- **Mix by intent:** every unit check combines recall (terminology), understanding (explain/interpret), and application (compute). The mastery assessment adds reasoning (why does X happen), transfer (an unfamiliar scenario), and error identification (debug-the-math), interleaved across units.
- **Never** "did you read the page?" items: no option may be selectable purely by recognizing lesson text; distractors encode diagnosed misconceptions.
- **Constructed response required:** numeric entry with tolerance, fill-in-equation, or explain-in-own-words with a model-answer reveal that is honestly self-graded (no fake auto-scoring of free text).
- **Feedback teaches:** every miss states the governing rule, re-deriving the distractor where useful. Confident errors are framed as high-value moments, never punished; attempts are unlimited; nothing is timed.
- **Mastery items never reuse worked-example numbers** (a learner must compute, not recall).
- **Explain floor:** every lesson includes at least two explain-in-own-words items with honest model-answer reveals — the constructed-response depth that separates explanation from recognition (LP-2026-0002 outcome 11; MEM-2026-0002). (Added 2026-08-13.)
- **Mastery size:** about one item per content unit + 2 (pattern P-12), with three-level confidence tags (sure / think so / guessing). (Added 2026-08-13.)
- No scores leave the device; no efficacy claim is derived from self-assessment.

## 6. ML-connection framework

For each concept the source connects to ML, follow: **Mathematical concept → what it represents → computational interpretation → where it appears in ML → why ML needs it → smallest honest example.**

Rules: connections appear at the learner's current level (a `FOUNDATION` bridge first if needed); one concrete anchor per concept, not a list of name-drops; advanced ML terms get a one-line gloss or a glossary entry; forced connections are worse than none — if the link needs machinery the learner lacks, mark it `EXTENSION` with a promise, not an explanation.

## 7. Additional-knowledge policy (scope control)

- **Must add:** prerequisites without which the source content cannot be understood (label `FOUNDATION`).
- **Should add:** concepts that significantly improve understanding of source content (label `DEEP DIVE`).
- **Could add:** useful extensions, clearly optional and collapsed (label `EXTENSION`).
- **Do not add:** interesting but unnecessary topics; anything whose inclusion raises cognitive load without paying for it; anything the lesson cannot explain properly (a bad half-explanation is worse than a pointer).
Every addition carries a reason in the learning plan and a label in the artifact.

## 8. Canonical lesson anatomy

Lesson skeleton: **Orientation** (how to learn with this page; the map; time expectation) → **units** → **synthesis + mastery assessment** → **review/next steps** → **glossary** → provenance footer.

Unit anatomy (order is the default; deviate only with a stated reason in the learning plan):

1. **Learn** — real-world intuition → simple example → visual → formal definition → annotated formula with per-symbol key → why the formula makes sense → what the result tells us.
2. **Predict** — committed choice before the key reveal.
3. **Explore** — goal-directed manipulation of the concept's own model.
4. **Practice** — the faded ladder for computational skills.
5. **Check** — retrieval items incl. constructed response; feedback with governing rules.
6. **Connect** — relationship strip ("you learned X → it feeds Y → Z") + the ML mechanism.

Progress indicators reflect cleared checks, never scroll position.

## 9. Learning progression and scaffolding fade

Stages: **Beginner** (recognizes nothing; needs intuition + full examples) → **Familiar** (follows a worked example) → **Understanding** (explains why steps work) → **Guided application** (completes partially-hidden steps) → **Independent application** (solves fresh problems) → **Transfer** (uses the idea in an unfamiliar context, incl. ML settings). The ladder enacts the middle three stages per skill; the mastery assessment tests the last two. Scaffolding fades within a unit (full → completion → independent) and across the lesson (early units explain notation inline; later units assume it).

## 10. Visual design system

**Standardize** (different lessons must feel like chapters of one platform): the token set (ink/paper/line neutrals + one accent + semantic good/bad/warn), system font stack with mono for math/readouts, the badge system (`CLASS CORE`/`FOUNDATION`/`DEEP DIVE`/`ML LINK`/`EXTENSION`) and provenance tags, callout styles (info/warn/good/ml), widget card with `EXPLORE` tag and goal strip, check block with `CHECK`/`MASTERY` tag, feedback ok/no states with ✓/✗ + text, predict block (dashed), ladder rungs, readout styling, print-note pattern, sticky unit nav with completion dots, canvas conventions (grid, labeled arrows, dashed auxiliary lines, right-angle markers, color legends on multi-entity canvases, bounded inputs or autoscaling so no learner action can render content off-canvas — amended 2026-08-13).

**Flexible:** layout within the reading column, which patterns a unit uses, number and size of widgets, section ordering inside the anatomy, illustrative analogies.

**Hard rules:** measured WCAG AA contrast for every text/background pair; 16 px minimum body text; one accent hue; no gradients/shadows used decoratively; nothing animated without a learner action; `prefers-reduced-motion` disables what little motion exists.

### 10.1 Pinned design tokens

The following token set is the default for every governed lesson. A lesson may adjust individual values only with documented rationale in the XS record; the token *names* and *categories* are fixed. The benchmark (BMK-2026-0001) embodies these values and serves as the calibration exemplar.

```css
:root{
  --ink:#1c2430; --ink-soft:#3d4a5a; --ink-faint:#66727f;
  --paper:#f7f6f2; --card:#ffffff; --line:#e3e0d8; --line-soft:#eeece5;
  --accent:#2f5fd0; --accent-soft:#e8eefa; --accent-deep:#1e3f8f;
  --good:#1e7a46; --good-soft:#e4f3ea; --bad:#b3382e; --bad-soft:#fae9e7;
  --warn:#8a6116; --warn-soft:#faf3e2;
  --core:#2f5fd0; --foundation:#8a6116; --deep:#0f6f6a; --ml:#1e7a46; --ext:#6d4fa3;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --radius:10px; --maxw:46rem;
}
```

**Requirements:**
- The `:root` block MUST declare ≥ 20 custom properties covering: ink/paper/line neutrals, one accent hue (with soft/deep variants), semantic good/bad/warn (with soft backgrounds), badge colors (core/foundation/deep/ml/ext), font stacks (`--mono`, `--sans`), and layout constants (`--radius`, `--maxw`).
- `body` MUST set `font-size: ≥16px`, `line-height: ≥1.6`, and `-webkit-font-smoothing: antialiased`.
- The `--paper` background MUST be a warm neutral (not pure white); `--card` is the content surface.

### 10.2 Navigation design contract

The sticky unit navigation is a defining visual element. The benchmark (v4, lines 46–52) establishes the pattern:

- **Frosted glass**: `background: rgba(247,246,242,.94); backdrop-filter: blur(6px); border-bottom: 1px solid var(--line);` — never a solid opaque background.
- **Single-line horizontal scroll**: the inner container uses `overflow-x: auto; scrollbar-width: thin; white-space: nowrap` — never `flex-wrap: wrap`, which causes multi-line wrapping that consumes excessive viewport height on smaller screens (EVAL-2026-0007, Finding 3.2.2).
- **Pill-style links**: `border-radius: 999px; border: 1px solid transparent; padding: .32rem .6rem;` — not rectangular buttons.
- **Active state**: `.topnav a[aria-current="true"]` MUST have distinct styling (accent background, deeper accent text, border color change, `font-weight: 600`). Active state is driven by an IntersectionObserver, not scroll position.
- **Completion dots**: `.dot` circles next to each link, filled only when the unit's check is cleared.

### 10.3 Header design contract

The page header MUST be left-aligned (not centered) and include:
- A `.kicker` eyebrow label (small, uppercase, accent color).
- A `h1` title and `.sub` subtitle.
- A `.head-meta` row of `.chip` metadata chips: estimated duration, unit count, offline capability, and progress persistence (e.g. `⏱ 3–5 hours`, `9 units + mastery check`, `Works offline`, `Progress saved locally`).

### 10.4 Widget control labels

Slider and input labels MUST be descriptive and mathematical, not single letters. Use subscript notation where applicable: `a₁ (scale v₁)`, not `a`. Every control labels its mathematical purpose so the learner never guesses which dial controls which quantity (EVAL-2026-0007, Finding 3.3.2).

### 10.5 Canvas engineering

Canvas widgets follow the [canvas engineering standard](canvas-engineering-standard.md) (ADR-0013): responsive `makeView` pattern, per-widget viewport declaration, DPR scaling, mandatory resize listeners, and `.legend-inline` color legends on multi-entity canvases.

## 11. Cross-lesson continuity

- Each module's concept model (CM) is a node set in the course knowledge graph; when a later lesson depends on an earlier concept, its CM references the earlier CM record by ID and the artifact links to the earlier lesson's unit.
- Glossary data is authored as a reusable structured list per lesson (term, simple, precise, intuition, example, related, ML/practice use). When a second module exists, a shared registry is curated from the two lists into `library/references/` — not before (earn complexity).
- The pattern catalog, misconception knowledge, and QA checklist are updated after every lesson (workflow phase P6).

## 12. Research and enrichment rules

- Research when it materially changes the lesson: a suspected misconception pattern, a sequencing decision the source gets wrong, an unfamiliar pedagogy claim. Do not research decoratively.
- Acceptable sources: peer-reviewed literature or reputable summaries (university labs/teaching centers), primary documentation for technical claims. Paywalled primaries may be cited via credible secondary summaries with the limitation disclosed.
- Every pedagogical technique adopted must answer: what is it, why does it help, evidence strength, fit for this learner, implementation cost, cognitive-load risk. Weak-evidence popular techniques (gamification, learning styles) are rejected by default.
- Mathematical claims are verified by independent recomputation before they ship; ML-application claims must be accurate at the level stated and labeled by provenance tier.

## Change history

| Date | Change |
| --- | --- |
| 2026-08-11 | Initial codification from V4 benchmark (ADR-0004) |
| 2026-08-13 | Standard colophon, 16px font rule, explain floor, mastery size, and canvas extrema bounds |
| 2026-08-14 | Pointed reference implementation to BMK-2026-0001 benchmark record (ADR-0011); added depth-calibration contract cross-reference |
| 2026-08-15 | Added §10.1 pinned design tokens, §10.2 navigation design contract, §10.3 header design contract, §10.4 widget control labels, §10.5 canvas engineering cross-reference (ADR-0013); codified from EVAL-2026-0007 audit findings |
