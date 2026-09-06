# RUN-20260906-0001: Matrix decompositions and applications v1

**Status:** Pilot complete  
**Owner:** Repository maintainer (solo Stage 1 operator)  
**Objective:** Generate governed interactive notes from `Matrix_Decompositions_&_Applications.ipynb` for an AIML-4 learner, preserving the source scope while adding live mathematical readouts and explain-before-use sequencing.  
**Budget:** One generation; maximum two revision cycles  
**Classification:** production  
**Operating scope:** Stage 1 private pilot  
**Review independence:** non-independent  
**Public-release eligibility:** ineligible

## Input manifest

- Source: [SRC-2026-0002](../sources/src-2026-0002-matrix-decompositions-applications.md), SHA-256 `9616d9bd736974bb2d1a3ca2cc7f696834b13d22bbb66958d1c99dfdc1465ef5`
- Concept model: [CM-2026-0008](../concepts/cm-2026-0008-matrix-decompositions-applications.md)
- Learning plan: [LP-2026-0009](../plans/lp-2026-0009-matrix-decompositions-applications.md)
- Experience specification: [XS-2026-0009](../specifications/xs-2026-0009-matrix-decompositions-applications-v1.md)
- Candidate: `CAN-2026-0010`, `matrix-decompositions-applications-v1.html`
- Prompt card: `prm-generator-lesson-standard@0.6.0`, digest `532febec136b`

## Iteration accounting

- Generation iterations: 1
- In-generation corrections: 0
- Revision cycles: 0

## P5 audit evidence

- Audit 1 Coverage: PASS. Cells 1–40 dispositioned as orientation, five units, or synthesis; no silent drops.
- Audit 2 Mathematical: PASS. Recomputed eigen readout `λ·1 = λ`; diagonal powers `2^6=64`, `3^6=729`; PCA energy `25/29` and `29/29` match live output.
- Audit 3 Dependency order: PASS. Eigenpair precedes diagonalization; SVD precedes PCA and low rank; application names follow mechanisms.
- Audit 4 Pedagogical/depth: PASS. Five unit paths, one callout maximum per unit, three ladders, prediction gate, two explain/reasoning checks, and mastery transfer item.
- Audit 5 Technical: PASS. `verify-candidate.py --strict` returned 0 failures; 0 textareas; 0 external resources; unique IDs; all range inputs wrapped in slider tracks.
- Audit 6 Rendered: PASS in browser. File opened from `file://`; live sliders and checks updated; body font measured 16px; scroll width equaled viewport at the active 617px viewport; no over-wide elements observed; screenshot captured.

## Adversarial re-examination

Fresh read-through confirmed no forward promise without a payoff. Edge traces covered negative eigenvalue, high matrix power, full component retention, prediction refusal until commitment, and mastery feedback. Provenance and colophon were present; no release, benchmark, or efficacy claim appears in the learner-facing page.

## Reflection and memory disposition

The source's terse agenda benefited from a single repeated model: directions plus scales. The candidate intentionally uses SVG rather than canvas because the supplied concepts did not require a continuous geometric manipulator; the text equivalents keep the visuals inspectable. No new memory record promoted; the run's evidence is sufficient for this pilot.

## Lineage

SRC-2026-0002 → CM-2026-0008 → LP-2026-0009 → XS-2026-0009 → CAN-2026-0010 → EVAL-2026-0011.

## Prompt snapshot

User trigger: `hey lets use the repo setup to build interactive notes for this @attachment:Matrix_Decompositions_&_Applications.ipynb notes!`

Workflow directive: execute governed P0–P6 lesson generation with source coverage, concept model, learning plan, experience specification, single-file offline candidate, strict verification, six audits, adversarial re-examination, evaluation, module README update, and repository checker.
