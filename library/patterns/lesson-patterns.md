# Lesson Pattern Catalog

**Status:** Experimental (curated from one reference implementation; strengthen with each new lesson)<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04<br>
**Provenance:** extracted from CAN-2026-0003 (`linear-algebra-foundations-v4.html`) and its records (RUN-20260810-0001, EVAL-2026-0002), with earlier-variant audits as contrast evidence. Each entry cites its evidence and confidence.

Patterns are **implementation techniques**, not principles. The principles they serve live in [lesson-standard.md](../../docs/01-product/lesson-standard.md). Choose a pattern per concept; never copy one by habit. Categories follow the standard's interaction taxonomy: Manipulate · Predict · Explore · Compare · Build · Solve · Debug · Reveal · Simulate · Explain · Practice.

---

## P-01 Prediction-gated reveal (Predict)

- **Problem:** manipulables invite undirected twiddling; without an expectation, the result teaches nothing.
- **Applicability:** the 2–4 most consequential, counterintuitive reveals per lesson (e.g. span collapse, opposite-direction dot product).
- **Learner benefit:** committed predictions force a falsifiable model; confident errors correct hardest (pretesting/hypercorrection evidence, moderate-strong).
- **Trade-offs:** gate fatigue if overused; adds a click before play.
- **Accessibility:** native radio + button; the gated content must be hidden by JS (not markup) so no-JS readers still see it.
- **Evidence/confidence:** MEM-2026-0001 (Supported); implemented ×3 in v4; Bjork Lab / Dunlosky et al. 2013.
- **Anti-patterns:** gating on correctness; gating every widget; punishment framing.
- **Do not use when:** the widget is for open-ended exploration with no single surprise, or the prediction options would give away the reveal.

## P-02 Faded worked-example ladder (Practice)

- **Problem:** explanation → hard exercise is a cliff for unconfident learners; pure worked examples produce passive agreement.
- **Applicability:** every computational skill (compute a norm, a dot product, a projection, expand Σ).
- **Learner benefit:** worked-example effect (strong for novices) + fading transfers agency gradually.
- **Trade-offs:** authoring cost ×3 per skill; click-through risk on rung 1 (mitigate with a per-step "why" line).
- **Accessibility:** all text/inputs; hints never auto-open (screen-reader and keyboard safe).
- **Evidence/confidence:** Sweller; Renkl & Atkinson (strong); implemented ×4 in v4.
- **Anti-patterns:** rung 3 solvable by copying rung 1's numbers; hints visible by default; more than one new difficulty per rung.
- **Do not use when:** the skill is conceptual rather than computational (use an explain-item instead).

## P-03 Goal-directed explorer (Manipulate/Explore)

- **Problem:** free play without a target rarely builds a causal model.
- **Applicability:** any concept with manipulable causal structure (vectors, transformations, fits).
- **Learner benefit:** a stated objective ("make them orthogonal", "reach (3.5, 2.5)") converts play into hypothesis testing.
- **Trade-offs:** goal text must be designed, not generated.
- **Accessibility:** sliders/number inputs, not drag-only; every canvas has a text readout with the same numbers.
- **Evidence/confidence:** ICAP framework (constructive > active > passive); v2/v3 audit contrast (unguided = weaker).
- **Anti-patterns:** "play with the sliders"; multiple simultaneous variables on first contact.
- **Do not use when:** the concept has no meaningful manipulable variable (choose another category).

## P-04 Self-verifying readout (Simulate/Explore support)

- **Problem:** learners trust boxes; they should verify invariants.
- **Applicability:** any widget whose result obeys a checkable identity (x̂ + e = x; e·y = 0; area = 0 when dependent).
- **Learner benefit:** the invariant becomes visible and memorable; models the mathematical habit of checking.
- **Trade-offs:** readout length — keep to 3–4 lines.
- **Accessibility:** the readout *is* the canvas's text equivalent (aria-describedby); keep it non-live to avoid slider chatter, readable on demand.
- **Evidence/confidence:** v2/v3 audits praised the pattern; v4 extended it; dual-coding support (moderate-strong).
- **Anti-patterns:** readouts that dump raw numbers without interpretation; live regions that chatter on every input tick.
- **Do not use when:** no invariant exists to check.

## P-05 Misconception-first distractors (assessment design)

- **Problem:** plausible-but-generic distractors test reading, not understanding.
- **Applicability:** every multiple-choice item.
- **Learner benefit:** each wrong option corresponds to a diagnosed beginner error, so feedback can name and correct it (error-based learning).
- **Trade-offs:** requires a misconception inventory (source: CM records + audit findings).
- **Accessibility:** none special.
- **Evidence/confidence:** v4 audit confirmed distractors match documented misconceptions; CM template already collects misconceptions.
- **Anti-patterns:** obviously-joke options; "all of the above".
- **Do not use when:** the misconception set is unknown — then prefer a constructed-response item.

## P-06 Debug-the-math (Debug)

- **Problem:** learners who can compute still can't catch the classic procedural error.
- **Applicability:** procedures with a famous error class (row-vs-column matrix product; sign slips; index slips).
- **Learner benefit:** error identification is a distinct, transfer-friendly skill; validates the learner's own bug history.
- **Trade-offs:** one per lesson is plenty.
- **Accessibility:** fully textual.
- **Evidence/confidence:** v4 Unit 7 instance; error-based learning literature (moderate).
- **Anti-patterns:** errors no real learner makes; multiple simultaneous bugs.
- **Do not use when:** the procedure is still new (place after the ladder, not before).

## P-07 Layer + provenance labels (Explain/content architecture)

- **Problem:** learners cannot tell what was taught from what was added; trust erodes when additions are invisible.
- **Applicability:** every lesson that extends its source (all of them).
- **Learner benefit:** the main path stays identifiable; optional depth is safe to skip; constructed numbers are never mistaken for source facts.
- **Trade-offs:** label discipline is tedious; too many badge types dilute the signal (cap at five layers + three provenance tiers).
- **Accessibility:** labels are text, not color-only; badge colors meet AA.
- **Evidence/confidence:** v2 introduced, v3 tiered, v4 made universal; audits consistently praised it as a trust device.
- **Anti-patterns:** labeling only examples while new claims go untagged (v3's determinant defect).
- **Do not use when:** the artifact is a verbatim revision asset with zero additions.

## P-08 Notation decompressor (Explain)

- **Problem:** compact notation (Σ, ᵀ, sub/superscripts) blocks learners who could do the underlying math.
- **Applicability:** any notation the lesson relies on heavily.
- **Learner benefit:** seeing Σ expand into a plain sum (or a row flip into a column) converts symbols into operations the learner already owns; programmer analogies (for-loops) shorten the path for code-fluent learners.
- **Trade-offs:** one small widget or worked expansion per notation; diminishing returns beyond that.
- **Accessibility:** text-first; the widget is an enhancement, never the only explanation.
- **Evidence/confidence:** v4 Units 2 instances (summation expander, transpose flip); cognitive-load/pre-training support (moderate).
- **Anti-patterns:** teaching notation for its own sake; decompression without later reuse.
- **Do not use when:** the notation is standard for the declared learner (e.g. plain fractions).

## P-09 Per-symbol formula key (Explain)

- **Problem:** formulas get memorized as shapes when symbols go unnamed.
- **Applicability:** every displayed formula on the main path.
- **Learner benefit:** naming each symbol, why the formula makes sense, and how to read the result converts recognition into comprehension.
- **Trade-offs:** vertical space; keep keys to one line per symbol.
- **Accessibility:** pure text; excellent for screen readers (math as annotated HTML, never images).
- **Evidence/confidence:** universal in v4; directly targets the owner's stated failure mode ("can recognize formulas but cannot explain").
- **Anti-patterns:** keys that restate the symbol ("xᵢ is x-sub-i") instead of its meaning.
- **Do not use when:** never, on the main path; optional for extension material.

## P-10 Glossary-as-data with in-place popover (Explain/reference)

- **Problem:** definitions scattered in prose are unfindable; leaving the page loses the thread.
- **Applicability:** every lesson; entries follow the fixed shape (simple / precise / intuition / example / related / where it appears).
- **Learner benefit:** one click on a dotted term opens its card without losing place; the full glossary doubles as a revision asset.
- **Trade-offs:** entries must be authored, not generated ad hoc.
- **Accessibility:** popover is a focus-managed, Escape-closable dialog; the glossary section contains the same content for non-JS readers.
- **Evidence/confidence:** v4 (39 entries); single JS data source is designed for cross-lesson reuse (standard §11).
- **Anti-patterns:** glossary terms that never appear in text; popovers that trap focus.
- **Do not use when:** the lesson defines fewer than ~10 terms (inline definition suffices).

## P-11 Concept map + closing revisit (Orient)

- **Problem:** learners memorize isolated definitions; relationships are where understanding lives.
- **Applicability:** every lesson; the map is the lesson's dependency graph made visible.
- **Learner benefit:** orientation before complexity; the closing revisit ("every arrow is now something you computed") converts the map into an achievement summary.
- **Trade-offs:** hand-placed SVG has authoring cost; keep to ~15–20 nodes.
- **Accessibility:** the SVG carries a full text description; the same chain appears as a text strip per unit.
- **Evidence/confidence:** v4 Units 0/9; advance-organizer support (moderate).
- **Anti-patterns:** maps with unlabeled arrows; maps that include concepts the lesson never teaches.
- **Do not use when:** the lesson teaches a single concept (a one-line chain suffices).

## P-12 Interleaved mastery check with confidence calibration (assessment)

- **Problem:** end-of-lesson quizzes that repeat worked examples certify attendance, not mastery.
- **Applicability:** once per lesson, after synthesis.
- **Learner benefit:** interleaving + retrieval strengthen durable memory; confidence tags expose miscalibration; confident misses are routed to review as highest-value fixes.
- **Trade-offs:** confidence tags on every micro-item cause fatigue — mastery check only.
- **Accessibility:** native controls; numeric inputs with tolerance; free-text is self-graded honestly.
- **Evidence/confidence:** v4 Unit 9; interleaving/testing-effect literature (strong); calibration flagged as an evidence gap in EVAL-2026-0002 Revision 1 (fixed: numeric path now wired).
- **Anti-patterns:** reusing lesson numbers; recognition-only items; scoring transmitted anywhere.
- **Do not use when:** never — but its size scales with lesson length (~1 item per unit + 2).

## P-13 Weak-topic review list with spacing invitation (Review)

- **Problem:** one-pass completion feels like learning; retention requires return.
- **Applicability:** every lesson with checks.
- **Learner benefit:** missed topics persist locally as a personal review queue; the invitation to return tomorrow makes spacing a feature, not homework.
- **Trade-offs:** localStorage may be unavailable — degrade gracefully with an in-memory fallback and a note.
- **Accessibility:** the review list is plain text; reset control visible and keyboard-reachable.
- **Evidence/confidence:** v4 Unit 9; distributed-practice literature (strong); privacy-preserving (no data leaves the device).
- **Anti-patterns:** streaks/shame mechanics; storing anything beyond topic-level misses.
- **Do not use when:** the artifact has no persistent checks (e.g. a pure explorable).

---

## Curation rule

After each governed lesson (workflow P6): patterns observed working are strengthened (evidence links added), new reusable patterns are drafted, and any pattern observed failing is marked with the failure evidence. A pattern promoted to `Established` requires the review policy's memory-promotion review.
