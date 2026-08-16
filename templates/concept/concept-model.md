# CM-YYYY-NNNN: Concept model title

**Status:** Draft | Reviewed | Superseded (per ADR-0007; Reviewed = reviewed within the declared scope and usable as a governed input)<br>
**Supersedes / iteration position:** e.g. "Iteration 2, supersedes CM-YYYY-NNNN" or "Iteration 1 — original" (per ADR-0006, mandatory for records created on or after 2026-08-11)<br>
**Owner:**<br>
**Source package:**<br>
**Domain review status:**<br>
**Confidence:** high | medium | low

## Scope and learning boundary

## Concepts and definitions

## Atomic claims and evidence anchors

(Depth floor: one anchored claim per concept, including the load-bearing ones the source states only once. A thin claim list starves every downstream layer — CM-2026-0002 at ~1/3 the depth of CM-2026-0001 preceded the compliant-but-thin CAN-2026-0004 lesson; MEM-2026-0004.)

## Prerequisites and relationships

(Include the full dependency chain with every use-before-define case the source commits, plus each visual convention the lesson will rely on — e.g. vectors drawn as arrows — so it is taught before first use.)

## Examples, non-examples, and misconceptions

(Depth floor: every source example with its cell anchor; at least one non-example per distinction the source draws; at least one misconception per major concept — each becomes an assessment distractor or an alert callout downstream. Name the misconception's wrong answer precisely enough to author a distractor from it.)

## Ambiguities, gaps, and assumptions

## Review and acceptance criteria

## Conformance checklist (depth-calibration contract)

Before approval, verify against [depth-calibration-contract.md](../../docs/01-product/depth-calibration-contract.md):
- [ ] $\ge 1$ anchored atomic claim per concept (no compressed lists; typically $\ge 25$ claims for a full lesson)
- [ ] Full dependency graph covering every prerequisite and flagging every source use-before-define case
- [ ] $\ge 1$ diagnosed misconception per major concept with clear wrong-answer definitions for distractors/alerts
- [ ] Every source example anchored to cell/section
- [ ] $\ge 1$ non-example per conceptual distinction the source draws

A CM failing any of these items is non-conformant and will starve downstream generation depth (WF-004; MEM-2026-0004).
