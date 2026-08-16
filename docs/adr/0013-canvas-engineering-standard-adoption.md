# ADR-0013: Adopt the canvas engineering standard

**Status:** Accepted  
**Date:** 2026-08-15  
**Owner:** Repository maintainer (Human Accountable Owner)  
**Decision scope:** Lesson generation workflow (P3 experience specification, P4 generation, P5 verification audits); all future governed interactive lesson candidates  
**Supersedes / superseded by:** none

## Context and problem

The QA and design audit of CAN-2026-0006 (v7) against the CAN-2026-0003 (v4) benchmark ([EVAL-2026-0007](../../records/evaluations/eval-2026-0007-linear-algebra-foundations-v4-v7-qa-design-audit.md)) identified a **critical (P0) regression in canvas and graph rendering architecture**:

1. **Zero resize listeners**: v7's `cv()` helper reads static HTML `width`/`height` attributes (always 640×360) and applies DPR once at load. Not a single widget attaches a `window.addEventListener("resize", draw)` listener. When the browser window resizes or the container width differs from 640px, the CSS rule `canvas { width: 100%; height: auto; }` stretches or squashes the canvas bitmap, causing blurry lines, misaligned labels, and severe visual distortion.

2. **Generic single-scalar projection**: v7 uses a `plot(ctx, w, h, range)` helper computing `s = Math.min(w, h) / (2 * range)`. Because all canvases are 640×360, the scale is always constrained by height, leaving massive unused blank margins. v4 uses per-widget `makeView(id, xMin, xMax, yMin, yMax)` with tailored aspect ratios.

3. **Hardcoded pixel offsets**: The least-squares lab (W12) uses `px = function(x){ return 50 + x * (W - 75) / 5 }` — hardcoded pixel offsets that break with any container width change. v4 maps all coordinates through normalized viewport transforms.

4. **Angular arc bug**: The dot product lab (W7) uses `Math.max`/`Math.min` on angles, which flips orientation and draws the reflex angle when vectors cross quadrant boundaries. v4 uses signed angular difference with wrapping.

The root cause is **architectural, not incidental**: the repository has no canvas engineering standard. The generation prompt (`prm-generator-lesson-standard@0.4.0`, item 7) lists "canvas text equivalents; reduced-motion; print fallbacks" but never specifies responsiveness, DPR scaling, resize handling, or coordinate projection contracts. The QA checklist's canvas checks (Audit 2) verify extrema bounds (no off-canvas rendering) but not the responsive viewport contract. The pattern catalog covers pedagogical patterns (P-01 through P-15) but contains no engineering patterns.

## Decision

Adopt the [canvas engineering standard](../01-product/canvas-engineering-standard.md) as a binding standard for all governed interactive lesson candidates. The standard codifies:

1. **Responsive viewport contract**: the `makeView` pattern (dynamic `clientWidth` measurement, DPR scaling, aspect-ratio-driven CSS height, mandatory `resize` listener on every widget).
2. **Per-widget viewport declaration**: every canvas declares its `xMin/xMax/yMin/yMax` in the XS record; P5 verifies conformance.
3. **Widget canvas lifecycle**: standardized initialization → interaction → resize flow.
4. **Color legend contract**: every multi-entity canvas pairs with a `.legend-inline` element.
5. **Angular arc computation**: signed angular difference with wrapping; `Math.max`/`Math.min` on angles prohibited.
6. **Canvas CSS baseline**: `width: 100%; height: auto` with `makeView`-controlled explicit height.
7. **Verification checklist**: eight canvas-specific checks added to P5 Audit 5.

## Decision drivers

- Principle 3 (Plan before generation): canvas architecture must be specified, not improvised per-generation.
- Principle 7 (Explicit contracts): the responsive viewport contract is now a named, verifiable requirement.
- Principle 9 (Measurable and contestable quality): the verification checklist makes canvas correctness mechanically checkable.
- EVAL-2026-0007 Finding 3.1.1–3.1.4: the specific defects this standard prevents.
- The benchmark (CAN-2026-0003) embodies every rule in this standard; v4 is the proof that the pattern works.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| A. Add canvas checks to QA checklist only | Minimal new documentation | Checklist alone doesn't guide generation; the generator still invents arbitrary canvas code | Rejected |
| B. Build a shared JavaScript canvas library | Mechanical enforcement | Premature implementation (charter non-goal; Stage 2+ scope); single-file HTML candidates cannot import shared modules | Rejected for Stage 1 |
| C. Codify the canvas engineering standard as a document with verification checklist (chosen) | Reviewable, linkable, revisable; matches the repository's documentation-first phase; the canonical `makeView` code snippet serves as a copy-ready reference | Requires discipline to keep standard and artifacts in sync | Selected |

## Consequences

- **Positive:** Future generated lessons inherit the benchmark's responsive canvas architecture by contract, not by chance. The eight-point verification checklist makes canvas regressions mechanically detectable at P5. The standard traces every rule back to the audit finding that motivated it.
- **Operational:** The XS template gains a viewport-range declaration requirement. The prompt card (@0.5.0) gains a canvas engineering clause. The QA checklist gains eight canvas checks. The SKILL.md orchestrator gains a canvas verification step.
- **Reversibility:** Fully reversible by superseding this ADR.

## Evidence and validation

- **Negative validation:** Applying the §7 verification checklist to CAN-2026-0006 (v7) detects all four canvas findings from EVAL-2026-0007: zero resize listeners (check 4 fails), static attribute reading (check 1 fails), hardcoded pixel offsets in W12 (check 5 fails), `Math.max`/`Math.min` arc in W7 (check 8 fails).
- **Positive validation:** Applying the same checklist to CAN-2026-0003 (v4) passes all eight checks: 8 resize listeners found, `makeView` reads `clientWidth`, DPR scaling present, aspect-ratio height set, per-widget viewports declared, `.legend-inline` present on multi-entity canvases, signed angular difference used.
- **Forward validation:** Occurs on the next governed generation run.

## Rollback or migration plan

Supersede this ADR; remove `docs/01-product/canvas-engineering-standard.md`; revert the QA checklist, prompt card, XS template, and SKILL.md to their pre-ADR-0013 versions.

## Review evidence

Reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-15 under the Stage 1 solo-maintainer path (see review policy, Status accuracy). Scope inspected: this ADR, EVAL-2026-0007, the canvas engineering standard, and the v4/v7 artifact code. Decision: accept. Limitation: non-independent self-review recorded per policy.

## Review trigger/date

Review at the Stage 1 calibration review (three completed pilots) or 2026-11-04, whichever comes first.
