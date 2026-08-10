# Module 2: Math & Statistics for ML

**Course:** AIML-4<br>
**Package status:** Active — all classes share this module package; this README is the single navigation surface for every source and generated artifact (ADR-0001; a class-level package directory scheme was evaluated in draft ADR-0005 and rejected, see the [convention change history](../../../docs/02-system/content-package-convention.md))<br>
**Source-rights status:** Class 1 — [Self-authored; public distribution authorized with rights retained](../../../records/sources/SRC-2026-0001-aiml-4-module-02.md). Class 2 — awaiting source; no redistribution until classified<br>
**Governed-generation status:** The historical `generated/linear-algebra-foundations-v1.html` (preserved from the initial commit under the name `index.html`) has no reconstructable run or evaluation record. A Stage 1 private pilot ([RUN-20260804-0001](../../../records/runs/run-20260804-0001-linear-algebra-foundations-v2.md)) produced the governed candidate `linear-algebra-foundations-v2.html`; it closed as `private-pilot-complete` with a non-independent review and is **not a public release, benchmark result, or efficacy claim**. A second governed candidate (`linear-algebra-foundations-v3.html`, identity CAN-2026-0002) was generated cross-model under [RUN-20260804-0002](../../../records/runs/run-20260804-0002-linear-algebra-cross-model.md); its generation is complete and it carries full provenance, but its evaluation pass is still pending, so it likewise is **not a public release, benchmark result, or efficacy claim**. A third governed candidate (`linear-algebra-foundations-v4.html`, identity CAN-2026-0003) was generated under [RUN-20260810-0001](../../../records/runs/run-20260810-0001-linear-algebra-foundations-v4.md) as a redesign driven by a comparative evaluation of v1–v3 and an evidence-based learning-design pass; it closed as `private-pilot-complete` under a non-independent review ([EVAL-2026-0002](../../../records/evaluations/eval-2026-0002-linear-algebra-foundations-v4.md)) and is likewise **not a public release, benchmark result, or efficacy claim**

## Classes and material

Each class runs its own governed pipeline (source package → concept model → learning plan → experience specification → generation → evaluation), per the [lesson generation workflow](../../../docs/03-workflows/lesson-generation-workflow.md). Class identity lives in records and README rows; files are disambiguated by `<note-slug>-v<N>` filenames.

| Class | Material | Open |
| --- | --- | --- |
| 1 · Mathematical Foundations & Linear Algebra Fundamentals | Source notebook | [Open notebook](sources/Mathematical_Foundations_&_Linear_Algebra_Fundamentals.ipynb) |
| | Generated — historical artifact (renamed to `-v1` on 2026-08-11; bytes unchanged) | [v1](generated/linear-algebra-foundations-v1.html) |
| | Generated — candidate CAN-2026-0001 (private pilot; not released) | [v2](generated/linear-algebra-foundations-v2.html) |
| | Generated — candidate CAN-2026-0002, v3 (evaluation pending; not released) | [v3](generated/linear-algebra-foundations-v3.html) |
| | Generated — candidate CAN-2026-0003, v4 (redesign; non-independent review; not released) | [v4](generated/linear-algebra-foundations-v4.html) |
| 2 · Probability Basics | Awaiting source — notes not yet supplied; intake will create SRC-2026-0002 via workflow P0 | — |

## Provenance and notes

Both files were restored byte-for-byte from the repository's initial commit. The notebook is authorized for public distribution through [SRC-2026-0001](../../../records/sources/SRC-2026-0001-aiml-4-module-02.md). The interactive notes are an owner-authorized public historical artifact, but their prior generation history and evaluation evidence are unavailable; they are not a governed Learning OS release or benchmark result. The page loads unassessed third-party runtime resources, so this preservation decision makes no hosting, learner-release, accessibility, privacy, dependency, or reproducibility claim. On 2026-08-11 the historical artifact was renamed from the generic `index.html` to `linear-algebra-foundations-v1.html` to join the `<note-slug>-v<N>` scheme; this was a **filename-only correction — bytes and SHA-256 unchanged** — permitted and recorded per the [naming conventions](../../../docs/10-governance/naming-conventions.md), resolving the documented naming exception. When this module next enters the governed workflow, create a new run and evaluation record rather than retroactively certifying this artifact.

### Generated-version lineage

Governed rebuilds of each class's interactive notes are named `<note-slug>-v<N>.html`, where the slug is derived from the source note's title and `<N>` is the ordinal rebuild version (see [Naming conventions](../../../docs/10-governance/naming-conventions.md)). The filename version is a display version; the stable identity of each governed candidate is its CAN identifier, recorded in the artifact's provenance header and run ledger.

| Class | Version | File | Stable identity | Status |
| --- | --- | --- | --- | --- |
| 1 | v1 | `generated/linear-algebra-foundations-v1.html` (renamed from `index.html` on 2026-08-11) | none — historical artifact; naming exception resolved | preserved bytes; hash unchanged; not a governed release |
| 1 | v2 | `generated/linear-algebra-foundations-v2.html` | CAN-2026-0001 | private-pilot-complete; not released |
| 1 | v3 | `generated/linear-algebra-foundations-v3.html` | CAN-2026-0002 | generation complete; evaluation pending; not released |
| 1 | v4 | `generated/linear-algebra-foundations-v4.html` | CAN-2026-0003 | private-pilot-complete (EVAL-2026-0002, non-independent); not released |

## Governed work

| Record | Title |
| --- | --- |
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
