# XS-YYYY-NNNN: Learner artifact specification

**Status:** Draft | Approved | Superseded (per ADR-0007; the approval scope, e.g. "Stage 1 governed generation", is declared in the record body, not in the status value)<br>
**Supersedes / iteration position:** e.g. "Iteration 2, supersedes XS-YYYY-NNNN" or "Iteration 1 — original" (per ADR-0006, mandatory for records created on or after 2026-08-11)<br>
**Source concept model:**<br>
**Learning plan:**<br>
**Target learner and prerequisites:**<br>
**Artifact family:**<br>
**Learning outcomes:** Reference the linked learning plan; restate only artifact-specific outcomes.

## Learner problem and teaching strategy

## Content and evidence map

(Per unit, the map row also declares the LP's depth decisions: the unit lede, the signature visual, reveal-arc setup/payoff, and misconception callouts — so the artifact review can verify them element by element.)

## Learning sequence

## Interaction and feedback specification

(For every widget declare: the learner-manipulable variable(s) — or "static demo" with the reason (standard §4); the stated goal; the degenerate-state guard; input bounds or autoscaling so nothing renders off-canvas; the canvas text equivalent. **For every canvas widget, additionally declare the mathematical viewport: `xMin`, `xMax`, `yMin`, `yMax` — the exact coordinate ranges the canvas displays (ADR-0013 §2). The P5 conformance sweep verifies that the artifact's `makeView` calls match these declared ranges.** One full faded ladder per computational skill named in the LP. List the glossary term set from the CM (every term the lesson will use) and the concept map's dependency nodes/edges. This section is a conformance contract: workflow P5 verifies the artifact against it element-for-element.)

## Visual/representation rationale

## Assessment and misconception checks

## Accessibility and inclusion plan

## Performance/responsiveness intent

## Acceptance criteria and evaluation dimensions

## Conformance checklist (depth-calibration contract)

Before approval, verify against [depth-calibration-contract.md](../../docs/01-product/depth-calibration-contract.md):
- [ ] Every widget declares learner-manipulable variable(s) or explicit "static demo" justification
- [ ] Every canvas widget declares input bounding (sliders, min/max) or autoscaling parameters
- [ ] **Every canvas widget declares its mathematical viewport (`xMin`, `xMax`, `yMin`, `yMax`) for the P5 `makeView` conformance sweep (ADR-0013 §2)**
- [ ] Exhaustive glossary term set listed from the CM (every term used will have 6 fields)
- [ ] Concept map declares explicit dependency nodes and directed edges (multi-branch graph)
- [ ] Every LP-planned ladder, prediction gate, and reveal arc has a specified element
- [ ] Canvas text equivalents specified for every visual component

An XS failing any of these items is non-conformant (the P5 conformance sweep will reject the candidate, but catching it here prevents a wasted generation run).
