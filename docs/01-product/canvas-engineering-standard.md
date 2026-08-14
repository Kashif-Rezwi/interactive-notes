# Canvas Engineering Standard

**Status:** Experimental<br>
**Owner:** Repository maintainer<br>
**Review by:** 2026-11-04 (or after two governed lessons generated under this standard, whichever comes first)<br>
**Adopted by:** [ADR-0013](../adr/0013-canvas-engineering-standard-adoption.md)<br>
**Benchmark:** [BMK-2026-0001](../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, `linear-algebra-foundations-v4.html`)<br>
**Origin:** Codifies the canvas architecture that made CAN-2026-0003 the benchmark and prevents the regression class observed in CAN-2026-0006 ([EVAL-2026-0007](../../records/evaluations/eval-2026-0007-linear-algebra-foundations-v4-v7-qa-design-audit.md), Finding 3.1.1–3.1.4; [MEM-2026-0005](../../records/memory/mem-2026-0005-canvas-responsiveness-and-design-drift.md)).

This document is the binding engineering standard for every canvas element in a governed interactive lesson. It extends — never replaces — the [lesson standard](lesson-standard.md); conflicts resolve in favor of the parent.

---

## 1. Responsive Viewport Contract (Hard Rule)

Every canvas widget MUST implement the responsive viewport pattern. The canonical implementation is the `makeView` function from the benchmark (v4, lines 1170–1183):

```javascript
function makeView(canvasId, xMin, xMax, yMin, yMax){
  var cv = document.getElementById(canvasId); if(!cv) return null;
  function fresh(){
    var dpr = window.devicePixelRatio || 1;
    var cw = cv.clientWidth || 640;
    var ch = Math.round(cw * (yMax - yMin) / (xMax - xMin));
    if(cv.width !== Math.round(cw * dpr)){
      cv.width = Math.round(cw * dpr);
      cv.height = Math.round(ch * dpr);
      cv.style.height = ch + "px";
    }
    var ctx = cv.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return {ctx: ctx, cw: cw, ch: ch};
  }
  var X = function(x){ return (x - xMin) / (xMax - xMin); };
  var Y = function(y){ return 1 - (y - yMin) / (yMax - yMin); };
  return {cv: cv, fresh: fresh, X: X, Y: Y};
}
```

### Required behaviors

1. **Dynamic width measurement**: `cv.clientWidth` is read at every draw call (the `fresh()` function). Canvas dimensions are NEVER read from HTML `width`/`height` attributes for layout decisions.
2. **DPR scaling**: The backing store is always `Math.round(cw * dpr)` × `Math.round(ch * dpr)`, and the context transform is `ctx.setTransform(dpr, 0, 0, dpr, 0, 0)`. This ensures crisp rendering on high-DPI displays.
3. **Aspect-ratio-driven height**: The CSS height is computed from the mathematical aspect ratio: `ch = Math.round(cw * (yMax - yMin) / (xMax - xMin))`. This is set via `cv.style.height = ch + "px"` so the canvas never stretches or squashes.
4. **Resize handling**: Every canvas widget MUST attach `window.addEventListener("resize", draw)` where `draw` is the widget's redraw function. This is non-negotiable — the CAN-2026-0006 audit found **zero** resize listeners across all 13 widgets.

### Prohibited patterns

- **Static attribute reading**: `parseInt(c.getAttribute('width'))` as the sole width source (the CAN-2026-0006 `cv()` anti-pattern). HTML attributes are the *initial* dimensions only; the viewport must adapt at draw time.
- **Single-scalar range**: A `plot(ctx, w, h, range)` helper that computes `s = Math.min(w, h) / (2 * range)` forces square plotting areas into rectangular canvases, wasting space and causing inconsistent zoom across widgets. Each widget MUST declare its own `xMin/xMax/yMin/yMax`.
- **Hardcoded pixel offsets**: Functions like `var px = function(x){ return 50 + x * (W - 75) / 5 }` break whenever the canvas size changes. All coordinate transforms MUST flow through the normalized `X(x)` / `Y(y)` viewport functions.

---

## 2. Per-Widget Viewport Declaration

Every canvas widget MUST declare its mathematical viewport in the Experience Specification (XS) record:

| Field | Description | Example |
|---|---|---|
| `xMin, xMax` | Mathematical domain displayed | `-6.5, 6.5` |
| `yMin, yMax` | Mathematical range displayed | `-4.5, 4.5` |
| Aspect ratio | Derived: `(yMax-yMin)/(xMax-xMin)` | `9/13 ≈ 0.69` |

The P5 conformance sweep verifies that the artifact's `makeView` call for each widget passes coordinates matching the XS declaration.

**Rationale**: The benchmark (v4) uses tailored viewports per widget — the least-squares lab uses an asymmetric `[-1.4, 8.2] × [-3.1, 10.3]` window to fit positive-quadrant data; the dot product lab uses `[-5.5, 5.5] × [-4, 4]`. This tailoring is a design decision, not an accident, and must be declared and verified.

---

## 3. Widget Canvas Lifecycle

Every canvas widget follows this lifecycle:

```text
1. Widget initialization (script runs on page load)
   ├── makeView(canvasId, xMin, xMax, yMin, yMax) → view object
   ├── draw() function defined (reads current input state, calls view.fresh(), renders)
   └── window.addEventListener("resize", draw)
2. User interaction (slider input, button click)
   └── draw() is called → view.fresh() → re-renders at current container width
3. Window resize
   └── draw() is called by the resize listener → view.fresh() detects width change → re-renders
```

The `draw()` function MUST:
- Call `view.fresh()` first (this re-measures the container and updates the backing store if needed)
- Clear the canvas (`ctx.clearRect(0, 0, cw, ch)` or equivalent)
- Draw a grid (if applicable) using `drawGrid(view, ctx, cw, ch, step)`
- Draw all mathematical elements through the `view.X()` / `view.Y()` transforms
- Update the text readout with live-computed values

---

## 4. Color Legend Contract

Every canvas that displays more than one visual entity (vectors, paths, regions, data series) MUST include a `.legend-inline` element immediately before or after the canvas:

```html
<div class="legend-inline">
  <span class="lg-a">v₁ and a₁v₁</span>
  <span class="lg-b">v₂ and a₂v₂</span>
  <span class="lg-c">a₁v₁ + a₂v₂ (result)</span>
</div>
```

The CSS provides the colored swatch indicator:

```css
.legend-inline{font-size:.78rem;color:var(--ink-soft);display:flex;flex-wrap:wrap;gap:.9rem;margin:.2rem 0 .4rem}
.legend-inline span::before{content:"";display:inline-block;width:.7rem;height:.7rem;border-radius:2px;margin-right:.3rem;vertical-align:-1px}
```

Each `lg-*` class sets the swatch color to match the canvas entity. This contract prevents the CAN-2026-0006 regression where 13 widgets shipped with no color legends, forcing learners to guess which color maps to which mathematical object.

---

## 5. Angular Arc Computation

When drawing angle arcs between vectors (e.g. dot product labs), use signed angular difference with wrapping:

```javascript
var d = (a2 - a1) % (2 * Math.PI);
if(d > Math.PI) d -= 2 * Math.PI;
if(d < -Math.PI) d += 2 * Math.PI;
// draw arc from a1 to a1 + d
```

**Never** use `Math.max`/`Math.min` on angles (`ctx.arc(cx, cy, r, -Math.max(a0, a1), -Math.min(a0, a1))`), which flips orientation and draws the reflex angle when vectors cross quadrant boundaries (EVAL-2026-0007, Finding 3.1.4).

---

## 6. Canvas CSS Baseline

Every lesson MUST include this canvas CSS:

```css
canvas.viz{width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff;display:block;margin:.4rem 0}
```

- `width: 100%` makes the canvas fill its container.
- `height: auto` allows the `makeView` pattern to set the explicit pixel height.
- The canvas is a block-level element within its widget card.

---

## 7. Verification Checklist

The P5 Audit 5 (Technical & Behavioral) includes these canvas-specific checks:

- [ ] **Responsive viewport**: `clientWidth` read at draw time in every canvas widget; no reliance on HTML `width`/`height` attributes for layout
- [ ] **DPR scaling**: `ctx.setTransform(dpr, 0, 0, dpr, 0, 0)` present in every canvas draw path
- [ ] **Aspect-ratio height**: `cv.style.height` computed from mathematical aspect ratio, not hardcoded
- [ ] **Resize listeners**: `window.addEventListener("resize", draw)` count ≥ canvas widget count
- [ ] **Normalized transforms**: All coordinate mappings flow through `X(x) = (x-xMin)/(xMax-xMin)` and `Y(y) = 1-(y-yMin)/(yMax-yMin)`; no hardcoded pixel offset functions
- [ ] **Per-widget viewport**: Every `makeView` call passes coordinates matching the XS declaration
- [ ] **Color legends**: Every multi-entity canvas pairs with a `.legend-inline` element
- [ ] **Angular arcs**: Signed angular difference with wrapping used for all angle arc rendering

---

## Change history

| Date | Change |
|---|---|
| 2026-08-15 | Initial codification from EVAL-2026-0007 audit findings (CAN-2026-0006 canvas regressions vs CAN-2026-0003 benchmark) |

