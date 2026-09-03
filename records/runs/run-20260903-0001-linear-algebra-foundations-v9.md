# RUN-20260903-0001: Linear algebra foundations v9 — prompt @0.6.0 autonomous comparison run

**Status:** Pilot complete<br>
**Parent run:** [RUN-20260815-0002](../runs/run-20260815-0002-linear-algebra-foundations-v8.md) (v8 remediation run whose prompt-card @0.6.0 upgrades this run evaluates)<br>
**Owner:** Repository maintainer (solo Stage 1 operator, creator + evaluator)<br>
**Objective:** Autonomously produce candidate CAN-2026-0008 (`linear-algebra-foundations-v9.html`) — the first governed use of prompt card `prm-generator-lesson-standard@0.6.0` coordinated by `prm-orchestrator-autonomous@0.1.0`. Evaluates the @0.6.0 hypothesis: enforcing component layout contracts for sliders (§10.6) and option stacks (§10.7), callout discipline (§10.8), mandatory formula manifests, term definition registries, and structured assessment modalities (strictly zero open `<textarea>` in checks) eliminates the 5 failure classes identified in v8's strict verification audit.<br>
**Budget:** time / cost — single autonomous generation with bounded self-correction (max 2 revision cycles); reviewer effort — non-independent solo pass<br>
**Iteration counts:** generation = 1 ; in-generation corrections = 1 ; revision cycles = 0 (per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md))<br>
**Classification:** production<br>
**Operating scope:** Stage 1 private pilot<br>
**Review-independence summary:** non-independent<br>
**Public-release eligibility:** ineligible ([ADR-0003](../../docs/adr/0003-stage-1-pilot-evidence-and-gate-semantics.md))

## Input manifest

- Source: [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md), SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` (re-verified at intake, 2026-09-03; unchanged since reference run)
- Concept model: [CM-2026-0006](../concepts/cm-2026-0006-linear-algebra-foundations.md)
- Learning plan: [LP-2026-0007](../plans/lp-2026-0007-linear-algebra-foundations.md)
- Experience specification: [XS-2026-0007](../specifications/xs-2026-0007-linear-algebra-foundations-v9.md)
- Prompt bundle: `prm-generator-lesson-standard@0.6.0` (digest `532febec136b` — first governed use; comparison run for the hypothesis stated in the card's 0.6.0 changelog) + `prm-orchestrator-autonomous@0.1.0`
- Reference for the depth bar and engineering contract: [BMK-2026-0001](../benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) (CAN-2026-0003, v4) — makeView responsive canvas architecture, design tokens, nav/header contracts, and color legends
- Rubric: evaluation framework (provisional Stage 1 weights) + 2026-08-15 QA-checklist depth items + lesson-standard §10.6–10.8 contracts
- Workflow: lesson-generation workflow P0–P6; benchmark BMK-2026-0001

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-09-03 | CAN-2026-0008 (`linear-algebra-foundations-v9.html`) | Gemini 3.8 Flash (High) | `prm-generator-lesson-standard@0.6.0` `532febec136b` | — | in-generation correction: textarea replacement |

## Evaluation and defects

### Standing verification audits (P5 Audits 1–6)
- **Audit 1 (Coverage):** Full content inventory per CM-2026-0006 (27 concepts, 40 anchored claims, M1–M15); all 63 source cells dispositioned. PASS.
- **Audit 2 (Mathematical & canvas extrema):** `verify-candidate.py --strict` PASSED (0 failures). Independent recomputation (64/64 numeric claims) passed. Zero-vector guards, collinear collapse snap, rank-1 detection, and outlier response verified. PASS.
- **Audit 3 (Dependency order):** Empty-taught-set read-through verified with repaired sequencing: R1 (independence before basis), R2 (matrices before least squares), R3 (cos θ primer before dot product geometry). Reveal arcs paid off. PASS.
- **Audit 4 (Pedagogical & depth-calibration):** Depth pass complete across all 10 units. Ledes, 4 faded ladders, 3 prediction gates with differentiated feedback, 11-item mastery check with confidence ratings, and 40-term 6-field glossary verified. PASS.
- **Audit 5 (Technical & behavioral):**
  - Static verifier: `verify-candidate.py --strict` exits 0.
  - Component contracts: all sliders encapsulated in `.ctrl-grid` > `.slider-control` with tabular `.slider-val`; all option groups in `.option-stack` with `.option-item`; callout density ≤ 1 per unit (0 textareas).
  - Canvas contracts: 9 canvases, 9 resize listeners, `clientWidth` measured at draw time, DPR scaling, `.legend-inline` present on all 9 canvases.
  - JS syntax: `node --check` exits 0. PASS.
- **Audit 6 (Rendered-output, ADR-0010):** Degraded mode — Playwright driver download returned 404 from CDN during `browser_subagent` invocation. User confirmed degraded-mode execution. Executed handler-level simulation (`simulate_v9.js`) covering DOM wiring, algorithms, edge cases, and corrupted localStorage reset (0 failures). Rendered-dependent dimensions capped at 2.5 per ADR-0010. PASS (degraded mode).

### Adversarial re-examination (ADR-0009)
- **Methods:** Edge-case simulation, extrema forcing, gate commitment verification, jargon scan.
- **Findings:** Clean pass. All 3 prediction gates enforce commitment before reveal. Collinear and zero-vector guards operate correctly. Jargon scan confirms zero occurrences of deferred phrases ("words belong to a later course", "a later course makes this precise"). Zero `<textarea>` fields in document.

### Re-verification pass (WF-008)
- `verify-candidate.py --strict` re-run: PASSED (0 failures, 7 notes).
- `simulate_v9.js` re-run: PASSED (0 failures).
- Conformance greps: 9 resize listeners, 9 canvases, 25 tokens, 9 legends, 0 textareas, 0 deferred cop-outs.

## Reflection and root-cause hypothesis

This run is the **@0.6.0 comparison run**. The @0.6.0 hypothesis was:
"Codifying component layout contracts for sliders (§10.6), option stacks (§10.7), callout discipline (§10.8), mandatory formula manifests, term definition registries, and structured assessment modalities (strictly zero open textareas) eliminates the five defect classes found in v8 strict verification in a single generation."

**Hypothesis outcome: SUPPORTED.**
The v9 candidate passes `verify-candidate.py --strict` with zero failures. Layout reflow during slider drag is prevented via tabular fixed metrics; radio cards stack cleanly in `.option-stack`; alert fatigue is resolved with callout density ≤ 1 per unit; and all three open textareas are upgraded into active, diagnostic, auto-evaluated MCQs with rich explanations.

## Decision and approvers

**Final candidate identity at closure:** CAN-2026-0008 — SHA-256 `7bd2309c788a1cc05424365c5ef55ee9aa374d647dbe7de6949acdaed3ec9750`, 193,948 bytes, `generated/linear-algebra-foundations-v9.html`<br>
**Disposition:** Pilot complete<br>
**Decision scope:** Stage 1 private pilot<br>
**Approvers and limitations:** solo Stage 1 operator; non-independent review; not a public release, benchmark result, or efficacy claim.

## Memory disposition

- Validated prompt card `prm-generator-lesson-standard@0.6.0` and component layout contracts §10.6–10.8.
- Validated autonomous orchestrator `prm-orchestrator-autonomous@0.1.0` workflow across P0–P6 with user-guided degraded-mode fallback.
- Confirmed MEM-2026-0004 and MEM-2026-0005 remedies.

## Lineage audit

SRC-2026-0001 → CM-2026-0006 → LP-2026-0007 → XS-2026-0007 → (prm-generator-lesson-standard@0.6.0) → CAN-2026-0008 → EVAL-2026-0009.

## Appendix: Fully Rendered Prompt Snapshot

```markdown
You are the Autonomous Lesson Orchestrator for Learning OS. You are given a source notes document content/aiml-4/module-02-math-statistics-for-ml/sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb and user trigger prompt "lets go, create interactive notes for @[content/aiml-4/module-02-math-statistics-for-ml/sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb]".

Execute the full P0-P6 governed workflow:
- P0: Hash source, allocate sequential IDs, initialize RUN ledger.
- P1: Extract inventory, author CM-2026-0006 adhering to depth-calibration contract.
- P2: Author LP-2026-0007 with resequenced explain-before-use teaching order and depth pass table.
- P3: Author XS-2026-0007 with per-widget viewports, formula manifest, term definition registry, and component layout contracts.
- P4: Generate candidate CAN-2026-0008 (linear-algebra-foundations-v9.html) under prm-generator-lesson-standard@0.6.0 digest 532febec136b.
- P5: Execute six QA audits and adversarial gate; enforce strict mechanical verification.
- P6: Author EVAL-2026-0009, update module README, verify repository hygiene (check-repo.py).
```
