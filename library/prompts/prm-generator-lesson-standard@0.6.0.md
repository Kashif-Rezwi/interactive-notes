# PRM-generator-lesson-standard@0.6.0

**Status:** Draft (registered during Stage 1 per ADR-0004; promotion to Approved requires the prompt promotion process and owner approval)  
**Owner:** Repository maintainer  
**Layer:** Task  
**Compatible roles:** Generator / Creator profile (Stage 1 five-profile model)  
**Last evaluated:** 2026-09-03 (adds component layout contracts for sliders and option stacks, callout discipline, formula manifest, term definition registry, and assessment modality constraints)  
**Replaces / replaced by:** supersedes [@0.5.0](prm-generator-lesson-standard@0.5.0.md) (2026-09-03: addresses slider width shifts, slider-value decoupling, option alignment, missing formulas, incomplete term explanations, inappropriate open-textarea assessment modalities, and extraneous callout bloat); earlier lineage in @0.4.0 and @0.5.0

## Purpose and scope

Generate a governed, single-file interactive HTML lesson from an authorized source notes document, implementing the [lesson standard](../../docs/01-product/lesson-standard.md) end-to-end, including the [canvas engineering standard](../../docs/01-product/canvas-engineering-standard.md) (ADR-0013), the component layout contracts (§10.6–10.7), and the callout discipline contract (§10.8). Scope: learner-facing artifact generation only; the plan (LP) and specification (XS) are inputs, not outputs.

## Required inputs and source of truth

- `{SOURCE}` — the notes document (truth about *what was taught*, not about order or completeness).
- `{CONCEPT_MODEL}`, `{LEARNING_PLAN}`, `{SPEC}` — the pinned CM/LP/XS records; claims must trace to CM. The XS declares per-widget viewport ranges (`xMin/xMax/yMin/yMax`), the Formula Manifest, and the Term Definition Registry.
- `{PROVENANCE}` — candidate ID, run ID, source ID, model/configuration, date, prompt digest for the HTML header comment.
- `{PATTERN_CATALOG}` — the current lesson-patterns catalog.

## Output contract

One self-contained `.html` file: governed header comment carrying the provenance identity; the standard colophon (brand + AI-honesty lines per the lesson standard) as the page's only closing element; orientation unit with concept map; units following the canonical anatomy; synthesis + interleaved mastery assessment; review list; glossary; zero external requests; offline-capable; passes the standing verification suite (syntax, structure, zero-dependency, recomputation, behavioral simulation, mechanical component constraints). **The contract is the standard at full depth, not at minimum compliance: everything below and everything declared in {LEARNING_PLAN} / {SPEC} ships — or its absence is a stated, labeled decision, never a silent omission.**

## Hard constraints and prohibited behavior

- Explain-before-use (standard §2); layered content labels + provenance tags on every block (§1.1).
- Coverage: every inventory item present or dispositioned (§3).
- **Assessment modality:** strictly structured, auto-evaluated checks — diagnostic MCQs with option-specific misconception feedback, interactive visual/manipulative target challenges, or bounded numeric inputs. Passive open text `<textarea>` or unvalidated free text inputs are **strictly forbidden** in checks.
- Interaction only via the admission test (§4); goal-directed; live-computed values only — never hard-code what can be computed.
- **Formulas:** all formulas declared in the XS Formula Manifest MUST be emitted inside `<div class="formula">` blocks with per-symbol keys (`<ul class="symkey">`), plain-language meaning, and geometric/statistical interpretation. Never drop formal equations for purely verbal summaries.
- **Term definitions & zero jargon:** every domain term introduced (including ML links and tables) MUST have an introductory definition/intuition at first mention and a 6-field glossary entry. "Promise for a later course" deferrals are prohibited.
- Zero external dependencies; accessibility and technical baselines (standard §1.1).
- **Spec conformance:** every widget, ladder, gate, check, and assessment element declared in {LEARNING_PLAN} / {SPEC} exists in the artifact at the specified depth.
- **Canvas engineering (canvas engineering standard §1):** every canvas widget uses the responsive `makeView(id, xMin, xMax, yMin, yMax)` pattern — measures `clientWidth` at draw time, applies DPR scaling, computes CSS height from the mathematical aspect ratio, and attaches `window.addEventListener("resize", draw)`.
- **Component layout contracts (standard §10.6–10.7):**
  - Every slider is wrapped in `.slider-control` inside a `.ctrl-grid` with a dedicated `.slider-head` (`.slider-label` and `.slider-val` with `font-variant-numeric: tabular-nums` and `min-width: 4.5ch`) and `.slider-track`. Never emit bare range inputs as loose siblings in raw flex containers.
  - Every option selection set (radios/checkboxes in `.predict`, `.check`, `.q`) is wrapped in an `.option-stack` (`flex-direction: column`) with card-style `.option-item` containers. Never emit raw unparented `<label>` tags or horizontal option rows.
- **Callout discipline (standard §10.8):** maximum **1** `.callout` block per unit. Embed beginner misconceptions directly into explanatory prose or MCQ distractor explanations.
- **Design system (standard §10.1–10.4):** use the pinned design token set from the lesson standard §10.1. Frosted-glass sticky nav (`backdrop-filter: blur(6px)`), single-line horizontal scroll, pill-style links, and `[aria-current="true"]` active styling. Left-aligned header with metadata chips. Multi-entity canvases include `.legend-inline` color swatches. Descriptive slider labels (`a₁ (scale v₁)`).
- Prohibited: decorative interaction, recognition-only assessment, passive textarea inputs, unexplained jargon, unsupported claims, gamification, autoplay, efficacy claims, CDN references, excessive callouts.

## Prompt content

> You are generating a governed interactive lesson. Inputs: {SOURCE}, {CONCEPT_MODEL}, {LEARNING_PLAN}, {SPEC}, {PROVENANCE}, {PATTERN_CATALOG}.
> 1. Obey the lesson standard (attached/linked) in full; where source order conflicts with the dependency rule, follow the learning plan's sequence.
> 2. Teach to the declared learner: nothing unexplained is ever load-bearing; bridge or define immediately. No "promise for a later course" cop-outs for domain terms.
> 3. For each unit emit: Learn (intuition→example→visual→definition→keyed formula→interpretation) → Predict → Explore (goal-directed) → Practice (faded ladder for computational skills) → Check (diagnostic MCQs / visual challenges; rule-explaining feedback) → Connect (relationship strip + ML mechanism).
> 4. Labels: every block carries a layer badge and provenance tag.
> 5. Build interactions only from the pattern catalog; compute every displayed value live in the page's script.
> 6. Emit the mastery assessment per standard §5 and the glossary per the glossary-as-data pattern (6 fields per entry).
> 7. **Engineering — canvas:** Every canvas widget uses the responsive `makeView(id, xMin, xMax, yMin, yMax)` pattern: measure `clientWidth` at draw time, apply DPR scaling (`ctx.setTransform(dpr,0,0,dpr,0,0)`), compute CSS height from the mathematical aspect ratio (`cv.style.height = ch + "px"`), and attach `window.addEventListener("resize", draw)`. Use per-widget `xMin/xMax/yMin/yMax` from {SPEC}. All coordinate transforms flow through normalized `X(x)`/`Y(y)` functions.
> 8. **Engineering — component layout:**
>    - **Sliders:** Every slider MUST be wrapped in `.slider-control` inside `.ctrl-grid`. Pair label and value inside `.slider-head` with `.slider-val` set to `font-variant-numeric: tabular-nums` and `min-width: 4.5ch`. Wrap `<input type="range">` in `.slider-track` (`width: 100%`).
>    - **Option stacks:** Every radio/checkbox group in `.predict`, `.check`, and `.q` MUST use `.option-stack` (`display: flex; flex-direction: column; gap: 0.55rem; width: 100%;`) with `.option-item` card wrappers.
>    - **Callouts:** Maximum 1 `.callout` block per unit. Integrate misconceptions into narrative prose or MCQ distractor explanations.
> 9. **Engineering — design system:** Use the pinned `:root` token set from lesson standard §10.1. Frosted-glass sticky nav (`backdrop-filter: blur(6px)`), single-line horizontal scroll (`overflow-x: auto`), pill-style links, and `[aria-current="true"]` active state styling. Left-aligned header with `.head-meta` chips. Multi-entity canvases include `.legend-inline` color swatches. Descriptive slider labels (`a₁ (scale v₁)`).
> 10. **Engineering — assessments:** Prohibit passive `<textarea>` and unvalidated text inputs. Assessment checks MUST be diagnostic MCQs with per-option feedback, dynamic visual target checks, or auto-graded numeric inputs with tolerance.
> 11. **Engineering — formulas & terms:** Every equation in {SPEC}'s Formula Manifest MUST appear in a `.formula` block with a `.symkey` list. Every domain term in {SPEC}'s Term Registry MUST be defined on first appearance and linked to the glossary.
> 12. **Engineering — general:** single file; zero external requests; semantic HTML; keyboard-operable native controls; canvas text equivalents; reduced-motion; print fallbacks; local-only state with reset.
> 13. Provenance: header comment exactly as specified in {PROVENANCE}; close the page with the standard colophon (brand + AI-honesty lines, per the lesson standard); no governance banner or provenance footer; no release, benchmark, or efficacy claims anywhere.
> 14. Self-verify before returning: every formula, every default value, every answer key; list what you verified.
> 15. **Conformance sweep before returning.** Diff the artifact against {SPEC} and {LEARNING_PLAN} element by element:
>     - Confirm all Formula Manifest equations exist in `.formula` blocks.
>     - Confirm all Term Registry domain terms are defined with no deferral cop-outs.
>     - Confirm all sliders follow `.ctrl-grid` + `.slider-control` + tabular `.slider-val`.
>     - Confirm all options follow `.option-stack` + `.option-item`.
>     - Confirm zero `<textarea>` elements in checks.
>     - Confirm `.callout` density $\le 1$ per unit.
>     - Confirm canvas engineering contract (`addEventListener("resize")` count $\ge$ canvas count, `clientWidth` measured, no hardcoded pixel offsets, `.legend-inline`).

## Known failure modes

1. Assessment drifts to recognition-only when content volume grows (MEM-2026-0002).
2. Added bridges outgrow the main path (scope creep) — enforce additional-knowledge policy.
3. Hard-coded widget results drift from live UI — compute live only.
4. Provenance tags applied to examples but not to new claims.
5. Readouts that dump numbers without interpretation.
6. Compliant-minimum collapse (CAN-2026-0004 class).
7. Spec drift: declared elements quietly missing from artifact.
8. Canvas responsiveness collapse (CAN-2026-0006 class).
9. Design system drift (CAN-2026-0006 class).
10. **Slider layout shift & decoupling (CAN-2026-0007 / v8 class):** bare range inputs and unconstrained readout spans wrap unpredictably or shift neighboring controls during drag events.
11. **Option alignment squeezing:** radio/checkbox options lack vertical flex-column stacking, collapsing into squeezed single lines.
12. **Formula omission:** theoretical sections dropping formal equations in favor of verbal summaries.
13. **Deferred jargon cop-outs:** introducing advanced terms with "words belong to a later course" instead of clear geometric/conceptual intuition.
14. **Passive open-textarea checks:** falling back to ungradable `<textarea>` fields instead of active, reactive MCQs or interactive visual widgets.
15. **Callout banner bloat:** fracturing reading flow with dozens of warning callout blocks.

## Change rationale and compatibility impact

**0.6.0 (2026-09-03):** adds component layout contracts for sliders (§10.6) and option stacks (§10.7), callout discipline (§10.8), mandatory formula manifest, term definition registry, and assessment modality constraints (prohibiting open `<textarea>` fields). Addresses failure modes 10–15 identified in recent candidate audits.
