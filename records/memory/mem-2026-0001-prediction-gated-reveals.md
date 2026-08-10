# MEM-2026-0001: Gate high-value interactive reveals behind a committed prediction

**Status:** Supported
**Curator:** Repository maintainer (solo Stage 1 operator)
**Created / review date:** 2026-08-10
**Scope:** Interactive lesson generation for technical/math content in Learning OS
**Tags:** interaction-design, retrieval-practice, prediction-effect, widget-pattern
**Evidence records:** [RUN-20260810-0001](../runs/run-20260810-0001-linear-algebra-foundations-v4.md), [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md), comparative variant audits (v1–v3)
**Supersedes / conflicts-with:** none

## Lesson

Interactive explorers that are immediately visible invite undirected twiddling; learners change sliders without forming an expectation, so the result teaches nothing. In the v4 redesign, the three highest-value reveals (span collapse, opposite-direction dot product, projection leftover) were hidden until the learner committed to a multiple-choice prediction; feedback then referenced the commitment and unlocked the widget.

## Why this is believed

- Literature: pretesting/generation effects and hypercorrection of confident errors (moderate-strong evidence; Bjork Lab; Dunlosky et al. 2013 high-utility rating for practice testing).
- Comparative audit: none of v1–v3 had any prediction-before-reveal; all were rated as having passive-scroll/twiddle risk by independent audits.
- Implementation cost is low (a radio group + hidden container); no learner-facing downside observed.

## Recommended action

Make "predict-then-reveal" the default wrapper for any interactive whose point is a surprising or load-bearing result. Gate on *committing*, never on being correct. Keep gates off of free-exploration widgets whose purpose is open-ended play.

## Counterexamples and limitations

- Do not gate every widget: gate fatigue is real; reserve for 2–4 pivotal reveals per lesson.
- Wrong predictions must receive immediate, explanatory feedback or the effect is wasted.
- Untested with a real learner in Stage 1; confidence is medium until a learner pilot exists.

## Retrieval guidance

Consult when designing any interactive lesson section that contains a manipulable visualization. Pair with MEM-2026-0002 (assessment beyond recognition).

## Privacy, rights, and retention classification

No personal data; retain as a standing design pattern until superseded by learner-pilot evidence.
