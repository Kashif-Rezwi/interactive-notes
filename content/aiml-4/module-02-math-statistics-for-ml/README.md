# Module 2: Math & Statistics for ML

**Course:** AIML-4<br>
**Package status:** Active — all classes share this module package; this README is the single navigation surface for every source and generated artifact (ADR-0001; a class-level package directory scheme was evaluated and rejected in [ADR-0005](../../../docs/adr/0005-class-packages-within-modules.md), see the [convention change history](../../../docs/02-system/content-package-convention.md))<br>
**Source status:** Class 1 — captured; source identity recorded in [SRC-2026-0001](../../../records/sources/src-2026-0001-aiml-4-module-02.md). Class 2 — captured; source identity recorded in [SRC-2026-0002](../../../records/sources/src-2026-0002-matrix-decompositions-applications.md)<br>
**Governed-generation status:** The **active benchmark is [BMK-2026-0001](../../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md)** (CAN-2026-0003, `linear-algebra-foundations-v4.html`, EVAL-2026-0002; per [ADR-0011](../../../docs/adr/0011-benchmark-definition-and-artifact-change-protocol.md)). The **current reference candidate for new authoring is `linear-algebra-foundations-v10.html`** (candidate CAN-2026-0009), generated under [RUN-20260904-0001](../../../records/runs/run-20260904-0001-linear-algebra-foundations-v10.md) as the full-verification reproduction run: it reproduces the validated v9 reference design under the unchanged prompt card @0.6.0 and completes the live rendered-output verification ([ADR-0010](../../../docs/adr/0010-rendered-output-verification.md) Audit 6) that RUN-20260903-0001 could not perform in degraded mode, repairing four inherited defect classes along the way (title identity, §10.6 per-element slider encapsulation, §10.1 body-font floor, 320px overflow/clipping). It closed as `private-pilot-complete` under a non-independent review ([EVAL-2026-0010](../../../records/evaluations/eval-2026-0010-linear-algebra-foundations-v10.md), weighted 3.85, live-browser Audit 6 — no degraded-mode caps) and is **not a public release, benchmark result, or efficacy claim**. The previous reference candidate `linear-algebra-foundations-v9.html` (CAN-2026-0008, RUN-20260903-0001, EVAL-2026-0009; including its post-evaluation norm-clarification fix at commit `201a778`) is superseded and preserved as a historical version. Earlier candidates — v1 (historical), v2 (CAN-2026-0001), v3 (CAN-2026-0002), v4 (CAN-2026-0003), v5 (CAN-2026-0004), v6 (CAN-2026-0005), v7 (CAN-2026-0006), v8 (CAN-2026-0007) — are preserved as historical versions; see the Version history table below and the run ledgers of the governed candidates (v1, preserved from the initial commit, has no reconstructable run or evaluation record).

## Classes and material

Each class runs its own governed pipeline (source package → concept model → learning plan → experience specification → generation → evaluation), per the [lesson generation workflow](../../../docs/03-workflows/lesson-generation-workflow.md). Class identity lives in records and README rows; files are disambiguated by `<note-slug>-v<N>` filenames.

| Class | Material | Open |
| --- | --- | --- |
| 1 · Mathematical Foundations & Linear Algebra Fundamentals | Source notebook | [Open notebook](sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb) |
| | Interactive notes — **reference version** (CAN-2026-0009, v10; non-independent review; not released) | [Open the v10 notes](generated/linear-algebra-foundations-v10.html) |
| | Interactive notes — **previous reference** (CAN-2026-0008, v9; non-independent review; not released; superseded by v10) | [Open v9 (historical)](generated/linear-algebra-foundations-v9.html) |
| 2 · Matrix Decompositions & Applications | Source notebook | [Open notebook](sources/Matrix_Decompositions_&_Applications.ipynb) |
| | Interactive notes — **reference version** (CAN-2026-0011, v2; non-independent review; not released) | [Open the v2 notes](generated/matrix-decompositions-applications-v2.html) |
| | Interactive notes — **previous reference** (CAN-2026-0010, v1; non-independent review; not released; superseded by v2) | [Open v1 (historical)](generated/matrix-decompositions-applications-v1.html) |

*Rows are in class sequence. Files on disk are ordered alphabetically by convention (source filenames are preserved originals, generated files follow `<note-slug>-v<N>`), so use this table — never file enumeration — to determine class order.*

## Provenance and notes

The source notebook and the historical v1 artifact were restored byte-for-byte from the repository's initial commit; their provenance, including v1's rename from `index.html` to `linear-algebra-foundations-v1.html` on 2026-08-11 (a **filename-only correction — bytes and SHA-256 unchanged**, per the [naming conventions](../../../docs/10-governance/naming-conventions.md)), is recorded here and in the run ledgers. The historical v1 artifact predates the governed workflow: its generation history and evaluation evidence are unavailable, and it loads unassessed third-party runtime resources, so this preservation decision makes no hosting, learner-release, accessibility, privacy, dependency, or reproducibility claim. When this module next enters the governed workflow, create a new run and evaluation record rather than retroactively certifying this artifact. On 2026-08-13 the visible governance status banners and provenance footers were removed from the three governed artifacts (v2–v4) by owner decision; each file retains its candidate/run/source identity in an HTML header comment, and the governing rule was amended in the [lesson standard](../../../docs/01-product/lesson-standard.md) and workflow P4. The same change introduced the standard **colophon** — "Built with ♥ using Interactive Notes" plus the AI-honesty line — as each lesson's only footer (prompt card @0.3.0); the resulting SHA-256 identities are recorded in the run ledgers and evaluations.

### Version history (provenance record — the reference entry point is the table above)

The reference entry point for each class is the **reference version** in the Classes and material table above. The table below is preserved for provenance only: history of this module's Class 1 interactive notes, in generation order. Governed rebuilds are named `<note-slug>-v<N>.html`, where the slug is derived from the source note's title and `<N>` is the ordinal rebuild version (see [Naming conventions](../../../docs/10-governance/naming-conventions.md)). The filename version is a display version; the stable identity of each governed candidate is its CAN identifier, recorded in the artifact's provenance header and run ledger.

| Class | Version | File | Stable identity | Status |
| --- | --- | --- | --- | --- |
| 1 | v1 | `generated/linear-algebra-foundations-v1.html` (renamed from `index.html` on 2026-08-11) | none — historical artifact; naming exception resolved | preserved bytes; hash unchanged; not a governed release |
| 1 | v2 | `generated/linear-algebra-foundations-v2.html` | CAN-2026-0001 | private-pilot-complete; not released |
| 1 | v3 | `generated/linear-algebra-foundations-v3.html` | CAN-2026-0002 | generation complete; evaluation deferred 2026-08-11 (v4 redesign prioritized — see RUN-20260804-0002 appendix); not released |
| 1 | v4 | `generated/linear-algebra-foundations-v4.html` | CAN-2026-0003 | private-pilot-complete (EVAL-2026-0002, non-independent); not released |
| 1 | v5 | `generated/linear-algebra-foundations-v5.html` | CAN-2026-0004 | private-pilot-complete (EVAL-2026-0003, non-independent); pipeline regeneration test; not released |
| 1 | v6 | `generated/linear-algebra-foundations-v6.html` | CAN-2026-0005 | private-pilot-complete (EVAL-2026-0004, non-independent); prompt-card @0.4.0 comparison run — hypothesis supported; not released |
| 1 | v7 | `generated/linear-algebra-foundations-v7.html` | CAN-2026-0006 | private-pilot-complete (EVAL-2026-0006, non-independent, weighted 3.58, degraded-mode Audit 6); reproduction of reference depth from the unchanged source; not released |
| 1 | v8 | `generated/linear-algebra-foundations-v8.html` | CAN-2026-0007 | private-pilot-complete (EVAL-2026-0008, non-independent, weighted 3.85, live-browser Audit 6); engineering remediation run — ADR-0013 + lesson-standard §10; @0.5.0 comparison run hypothesis supported; not released |
| 1 | v9 | `generated/linear-algebra-foundations-v9.html` | CAN-2026-0008 | private-pilot-complete (EVAL-2026-0009, non-independent, weighted 3.58, degraded-mode Audit 6); autonomous @0.6.0 comparison run — component layout contracts (§10.6–10.8), formula manifest, term registry, and structured assessment modality; hypothesis supported; not released |
| 1 | v10 | `generated/linear-algebra-foundations-v10.html` | CAN-2026-0009 | private-pilot-complete (EVAL-2026-0010, non-independent, weighted 3.85, live-browser Audit 6); full-verification reproduction run — completed ADR-0010 rendered verification, repaired four inherited defect classes (title identity, §10.6 per-element encapsulation, §10.1 font floor, 320px overflow/clipping); not released |
| 2 | v1 | `generated/matrix-decompositions-applications-v1.html` | CAN-2026-0010 | private-pilot-complete (EVAL-2026-0011, non-independent, weighted 3.45); superseded by v2; not released |
| 2 | v2 | `generated/matrix-decompositions-applications-v2.html` | CAN-2026-0011 | private-pilot-complete (EVAL-2026-0012, non-independent, weighted 3.50, live-browser Audit 6); from-scratch rebuild closing the v1 gaps (numeric SVD, persistent progress, confidence-calibrated mastery); not released |

## Governed work

| Record | Title |
| --- | --- |
| [SRC-2026-0002](../../../records/sources/src-2026-0002-matrix-decompositions-applications.md) | Matrix decompositions and applications source manifest |
| [CM-2026-0008](../../../records/concepts/cm-2026-0008-matrix-decompositions-applications.md) | Concept model |
| [LP-2026-0009](../../../records/plans/lp-2026-0009-matrix-decompositions-applications.md) | Learning plan |
| [XS-2026-0009](../../../records/specifications/xs-2026-0009-matrix-decompositions-applications-v1.md) | Experience specification |
| [RUN-20260906-0001](../../../records/runs/run-20260906-0001-matrix-decompositions-applications-v1.md) | Stage 1 private-pilot run ledger |
| [EVAL-2026-0011](../../../records/evaluations/eval-2026-0011-matrix-decompositions-applications-v1.md) | Candidate v1 evaluation |
| [CM-2026-0009](../../../records/concepts/cm-2026-0009-matrix-decompositions-applications.md) | Concept model for the v2 from-scratch rebuild (iteration of CM-2026-0008; deeper re-read, 38 anchored claims) |
| [LP-2026-0010](../../../records/plans/lp-2026-0010-matrix-decompositions-applications.md) | Learning plan for candidate v2 (full depth pass; 3 gates, 5 ladders, 7-item confidence-calibrated mastery) |
| [XS-2026-0010](../../../records/specifications/xs-2026-0010-matrix-decompositions-applications-v2.md) | Experience specification for candidate v2 (formula manifest EQ-001–011, 32-term registry, per-widget viewports) |
| [RUN-20260906-0002](../../../records/runs/run-20260906-0002-matrix-decompositions-applications-v2.md) | v2 from-scratch rebuild run ledger (CAN-2026-0011; live-browser Audit 6; adversarial gate) |
| [EVAL-2026-0012](../../../records/evaluations/eval-2026-0012-matrix-decompositions-applications-v2.md) | Candidate v2 evaluation (non-independent; weighted 3.50; live-browser Audit 6; private-pilot-complete) |
| [CM-2026-0001](../../../records/concepts/cm-2026-0001-linear-algebra-foundations.md) | Concept model grounded in SRC-2026-0001 |
| [LP-2026-0001](../../../records/plans/lp-2026-0001-linear-algebra-foundations.md) | Learning plan |
| [XS-2026-0001](../../../records/specifications/xs-2026-0001-linear-algebra-foundations-v2.md) | Experience specification for the candidate |
| [RUN-20260804-0001](../../../records/runs/run-20260804-0001-linear-algebra-foundations-v2.md) | Stage 1 private-pilot run ledger |
| [RUN-20260804-0002](../../../records/runs/run-20260804-0002-linear-algebra-cross-model.md) | Cross-model generation run ledger for candidate CAN-2026-0002 (evaluation pending) |
| [EVAL-2026-0001](../../../records/evaluations/eval-2026-0001-linear-algebra-foundations-v2.md) | Candidate evaluation (non-independent; public-release eligibility ineligible) |
| [LP-2026-0002](../../../records/plans/lp-2026-0002-linear-algebra-foundations.md) | Redesign learning plan (re-sequenced teaching order; retrieval-first pedagogy) |
| [XS-2026-0002](../../../records/specifications/xs-2026-0002-linear-algebra-foundations-v4.md) | Experience specification for candidate v4 |
| [RUN-20260810-0001](../../../records/runs/run-20260810-0001-linear-algebra-foundations-v4.md) | Redesign generation run ledger (CAN-2026-0003) |
| [EVAL-2026-0002](../../../records/evaluations/eval-2026-0002-linear-algebra-foundations-v4.md) | Candidate v4 evaluation (non-independent; public-release eligibility ineligible) |
| [CM-2026-0002](../../../records/concepts/cm-2026-0002-linear-algebra-foundations.md) | Fresh concept model for the regeneration test (no reuse of CM-2026-0001) |
| [LP-2026-0003](../../../records/plans/lp-2026-0003-linear-algebra-foundations.md) | Fresh learning plan (repairs R1–R3) |
| [XS-2026-0003](../../../records/specifications/xs-2026-0003-linear-algebra-foundations-v5.md) | Experience specification for candidate v5 |
| [RUN-20260813-0001](../../../records/runs/run-20260813-0001-linear-algebra-foundations-v5.md) | Regeneration-test run ledger (CAN-2026-0004) |
| [EVAL-2026-0003](../../../records/evaluations/eval-2026-0003-linear-algebra-foundations-v5.md) | Candidate v5 evaluation (non-independent; public-release eligibility ineligible) |
| [CM-2026-0003](../../../records/concepts/cm-2026-0003-linear-algebra-foundations.md) | Concept model for the @0.4.0 comparison run (template depth floors) |
| [LP-2026-0004](../../../records/plans/lp-2026-0004-linear-algebra-foundations.md) | Learning plan with the mandatory depth pass |
| [XS-2026-0004](../../../records/specifications/xs-2026-0004-linear-algebra-foundations-v6.md) | Experience specification for candidate v6 (conformance contract) |
| [RUN-20260813-0002](../../../records/runs/run-20260813-0002-linear-algebra-foundations-v6.md) | Comparison-run ledger (CAN-2026-0005) |
| [EVAL-2026-0004](../../../records/evaluations/eval-2026-0004-linear-algebra-foundations-v6.md) | Candidate v6 evaluation + three-way depth comparison (non-independent; public-release eligibility ineligible) |
| [EVAL-2026-0005](../../../records/evaluations/eval-2026-0005-linear-algebra-foundations-v5-v6-reverification.md) | Re-verification audit of CAN-2026-0004 and CAN-2026-0005 against the 2026-08-13 checklist (non-independent; corroborates both closures; carries the EVAL-2026-0003/RUN-20260813-0001 ladder-wording and MEM-2026-0004 glossary-count errata; no score or disposition change) |
| [CM-2026-0004](../../../records/concepts/cm-2026-0004-linear-algebra-foundations.md) | Concept model for the v7 reproduction run (iteration of CM-2026-0003; stable claim set, re-grounded) |
| [LP-2026-0005](../../../records/plans/lp-2026-0005-linear-algebra-foundations.md) | Learning plan for the v7 reproduction run (iteration of LP-2026-0004; full depth pass) |
| [XS-2026-0005](../../../records/specifications/xs-2026-0005-linear-algebra-foundations-v7.md) | Experience specification for candidate v7 (conformance contract) |
| [RUN-20260815-0001](../../../records/runs/run-20260815-0001-linear-algebra-foundations-v7.md) | Reproduction-run ledger (CAN-2026-0006, v7) |
| [EVAL-2026-0006](../../../records/evaluations/eval-2026-0006-linear-algebra-foundations-v7.md) | Candidate v7 evaluation (non-independent; weighted 3.58; degraded-mode Audit 6 (no browser); not released) |
| [EVAL-2026-0007](../../../records/evaluations/eval-2026-0007-linear-algebra-foundations-v4-v7-qa-design-audit.md) | QA and design audit of v7 against the v4 benchmark standard (CAN-2026-0006 vs CAN-2026-0003; BMK-2026-0001; root-cause analysis and remediation roadmap; led to [ADR-0013](../../../docs/adr/0013-canvas-engineering-standard-adoption.md) canvas engineering standard and prompt card @0.5.0) |
| [MEM-2026-0005](../../../records/memory/mem-2026-0005-canvas-responsiveness-and-design-drift.md) | Canvas responsiveness collapse and design system drift (v7 regression class; implementation-contract remedy) |
| [CM-2026-0005](../../../records/concepts/cm-2026-0005-linear-algebra-foundations.md) | Concept model for the v8 remediation run (iteration of CM-2026-0004; stable claim set, re-grounded) |
| [LP-2026-0006](../../../records/plans/lp-2026-0006-linear-algebra-foundations.md) | Learning plan for the v8 remediation run (iteration of LP-2026-0005; full depth pass; ADR-0013 engineering-remediation obligation) |
| [XS-2026-0006](../../../records/specifications/xs-2026-0006-linear-algebra-foundations-v8.md) | Experience specification for candidate v8 (per-widget viewport declarations per ADR-0013 §2; design-system conformance contract) |
| [RUN-20260815-0002](../../../records/runs/run-20260815-0002-linear-algebra-foundations-v8.md) | Engineering-remediation run ledger (CAN-2026-0007, v8; @0.5.0 comparison run) |
| [EVAL-2026-0008](../../../records/evaluations/eval-2026-0008-linear-algebra-foundations-v8.md) | Candidate v8 evaluation (non-independent; weighted 3.85; live-browser Audit 6; private-pilot-complete) |
| [BMK-2026-0001](../../../records/benchmarks/bmk-2026-0001-linear-algebra-foundations-v4.md) | Linear Algebra Foundations benchmark definition (CAN-2026-0003, v4; ADR-0011) |
| [CM-2026-0006](../../../records/concepts/cm-2026-0006-linear-algebra-foundations.md) | Concept model for the v9 @0.6.0 autonomous comparison run (iteration of CM-2026-0005; stable claim set, re-grounded) |
| [LP-2026-0007](../../../records/plans/lp-2026-0007-linear-algebra-foundations.md) | Learning plan for candidate v9 (component layout & assessment modality contracts; full depth pass) |
| [XS-2026-0007](../../../records/specifications/xs-2026-0007-linear-algebra-foundations-v9.md) | Experience specification for candidate v9 (formula manifest, term definition registry, §10.6–10.8 contracts) |
| [RUN-20260903-0001](../../../records/runs/run-20260903-0001-linear-algebra-foundations-v9.md) | Autonomous @0.6.0 comparison run ledger (CAN-2026-0008, v9) |
| [EVAL-2026-0009](../../../records/evaluations/eval-2026-0009-linear-algebra-foundations-v9.md) | Candidate v9 evaluation (non-independent; weighted 3.58; degraded-mode Audit 6; private-pilot-complete) |
| [CM-2026-0007](../../../records/concepts/cm-2026-0007-linear-algebra-foundations.md) | Concept model for the v10 full-verification reproduction run (iteration of CM-2026-0006; stable claim set, re-grounded) |
| [LP-2026-0008](../../../records/plans/lp-2026-0008-linear-algebra-foundations.md) | Learning plan for candidate v10 (iteration of LP-2026-0007; full depth pass) |
| [XS-2026-0008](../../../records/specifications/xs-2026-0008-linear-algebra-foundations-v10.md) | Experience specification for candidate v10 (conformance contract re-pinned to CAN-2026-0009) |
| [RUN-20260904-0001](../../../records/runs/run-20260904-0001-linear-algebra-foundations-v10.md) | Full-verification reproduction run ledger (CAN-2026-0009, v10; live-browser Audit 6; audit-script appendices) |
| [EVAL-2026-0010](../../../records/evaluations/eval-2026-0010-linear-algebra-foundations-v10.md) | Candidate v10 evaluation (non-independent; weighted 3.85; live-browser Audit 6; private-pilot-complete) |


