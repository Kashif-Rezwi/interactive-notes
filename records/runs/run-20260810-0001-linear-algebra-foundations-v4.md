# RUN-20260810-0001: Redesign generation — linear algebra foundations, candidate 3 (v4)

**Status:** Generation complete; evaluation recorded in [EVAL-2026-0002](../evaluations/eval-2026-0002-linear-algebra-foundations-v4.md)
**Parent runs:** [RUN-20260804-0001](run-20260804-0001-linear-algebra-foundations-v2.md), [RUN-20260804-0002](run-20260804-0002-linear-algebra-cross-model.md)
**Owner:** Repository maintainer (solo Stage 1 operator; Creator pass executed in this run)
**Objective:** Generate redesigned candidate CAN-2026-0003 (v4) that (a) deeply evaluates variants v1–v3 against the source, (b) applies evidence-based learning techniques, (c) repairs the source's and variants' diagnosed defects, and (d) adds the retrieval/scaffolding layer all three variants lacked, per the owner's 30-section brief and the approved plan.
**Budget:** 1 generation iteration plus in-generation verification and corrections; no external model spend beyond the operator's agent session; no learner contact
**Classification:** exploratory
**Operating scope:** Stage 1 private pilot
**Review-independence summary:** non-independent (same operator, Creator and Reviewer passes)
**Public-release eligibility:** ineligible

## Input manifest

| Input | Identity | Version/pin |
| --- | --- | --- |
| Source package | [SRC-2026-0001](../sources/SRC-2026-0001-aiml-4-module-02.md) | Notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445`, re-verified unchanged 2026-08-10 |
| Concept model | [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) | Unchanged; reused as pinned input |
| Learning plan | [LP-2026-0002](../plans/lp-2026-0002-linear-algebra-foundations.md) | New; supersedes LP-2026-0001 for new generation work |
| Experience specification | [XS-2026-0002](../specifications/xs-2026-0002-linear-algebra-foundations-v4.md) | New |
| Prior candidates | index.html (v1), CAN-2026-0001 (v2), CAN-2026-0002 (v3) | Evaluated comparatively in this run; bytes untouched |
| Prompt | Owner's 30-section brief + approved plan; condensed snapshot preserved in Appendix A, SHA-256 `f1a43cbf21cf6b894ad8f1f0b4b7b0218e3e55dfcefd024b3d988cdf4015f29e`, digest `f1a43cbf21cf` | Snapshot mechanism per RUN-20260804-0002 finding (e) |
| Model/configuration | Claude (Anthropic), operated through the Cline terminal shell harness | Exact model identifier and configuration labels not exposed to the operator; recorded as best-known-not-inferred |
| Rubric | [Evaluation framework](../../docs/06-evaluation/evaluation-framework.md) | Shaped Creator verification; scored pass in EVAL-2026-0002 |
| Workflow | [Quality loop](../../docs/03-workflows/quality-loop.md) | Stage 1 model per ADR-0002/ADR-0003 |
| Benchmarks | None | No benchmark suite exists; none used or claimed |

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-10 | CAN-2026-0003 | Claude (Anthropic) via Cline terminal shell; exact model ID not exposed | `f1a43cbf21cf` | Single operator session | 2 in-generation defects found and repaired (dead markup in debug card; invalid CSS declaration); 1 stray closing tag and 1 redundant JS condition found in self-review and repaired before verification |

Candidate: [`linear-algebra-foundations-v4.html`](../../content/aiml-4/module-02-mathematical-foundations-linear-algebra/generated/linear-algebra-foundations-v4.html), SHA-256 `22b4047e7834ce233ff5088ff3d2e603242b8932e321f62004b823d076f445d6`, 172,736 bytes, zero external runtime dependencies. Filename per `<note-slug>-v<N>.html` convention (v4 = fourth generation: historical index.html = v1, CAN-2026-0001 = v2, CAN-2026-0002 = v3).

## Verification evidence (Creator pass, scripted)

- **Syntax:** extracted inline script passes `node --check`.
- **Zero-dependency claim:** 0 external `src`/`href`, 0 `@import`; single internal `url(#arr)` SVG marker reference only.
- **Structure:** no duplicate IDs; tag balance clean for div/section/button/fieldset/label/table/svg/details; all `data-g` glossary references resolve to glossary entries; all `getElementById` targets exist; all `data-num`/`data-fb` references resolve.
- **Mathematics:** 44 scripted recomputations, all PASS — every widget default (vector builder, summation, linear model, linear combination, norms, dot product incl. cos θ ≈ 0.984 and θ ≈ 10.3°, projection k = 1.04 with e·y = 0 and x̂ + e = x, least squares m = 0.7 / c = 0.3 / SSE = 0.30 and outlier m = 1.7 / c = −1.7 / SSE = 12.30, AB = [[0,−1],[2,0]] vs BA = [[0,−2],[1,0]], area tests) and every quiz/ladder/mastery answer key (12 numeric keys, all radio keys spot-verified against feedback text).
- **Runtime smoke test:** full script executed under a DOM/canvas stub; all 12 widgets initialize without errors; default readouts contain the independently recomputed values (14/14 effective checks; one stub artifact — innerHTML vs textContent — confirmed not a defect); no NaN/undefined in any readout; glossary renders 32 entries.
- **Defect class from RUN-20260804-0002 (assembly defects) not observed:** the standing verification suite ran before ledger closure and caught the two in-generation defects listed above.

## Reflection and lessons

(a) The dominant defect class across v1–v3 was not visual or mathematical but *assessment-shaped*: recognition-only questions let a learner finish without retrieving. The fix (constructed-response items, prediction gates, faded ladders) is reusable and is proposed as MEM-2026-0001/0002. (b) Parallel independent variant audits (three isolated evaluators with identical rubric and source map) produced consistent, cross-validating diagnoses with no coordination cost — keep this pattern. (c) Writing the artifact in one coherent pass by a single author, then running the standing scripted verification suite, avoided the assembly-defect class observed in the cross-model run. (d) A DOM/canvas stub smoke test with value assertions (not just no-throw assertions) is cheap and caught real wiring issues; promote it to the mandatory pre-evaluation gate alongside the existing suite. (e) The dependency-rule rewrite (transpose and cosine bridged before use, proof re-sequenced, determinant avoided via the area test) demonstrates that CM-layer dependencies and LP-layer teaching order should be reviewed separately: identical concept graph, different pedagogy.

## Memory disposition

Proposed for promotion: MEM-2026-0001 (prediction-gated reveals pattern), MEM-2026-0002 (assessment must include constructed response, not recognition only). Both recorded under `records/memory/` with this run as evidence.

## Lineage audit

- Source notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` — re-verified unchanged 2026-08-10.
- v1 `index.html` SHA-256 `687bccda2b71b8fd50b84a1198b194697598de6fa6c54e992c71ccdf5122fee1`; v2 `linear-algebra-foundations-v2.html` SHA-256 `e7e1bc6546ca2cc51a4c3636e655fdc49646f01ad7382f30e33b62ecaca14dd3`; v3 `linear-algebra-foundations-v3.html` SHA-256 `256201e20174b37ad8193817c37d4d69d3186d334de9f433db6b8d17748e0ac9` — all re-verified unchanged; none modified by this run.
- Chain: SRC-2026-0001 → CM-2026-0001 → LP-2026-0002 → XS-2026-0002 → CAN-2026-0003 → this run → EVAL-2026-0002. All links resolve within this repository.

## Appendix A — Prompt snapshot

Condensed snapshot preserved out-of-band at generation time (operator session log); SHA-256 `f1a43cbf21cf6b894ad8f1f0b4b7b0218e3e55dfcefd024b3d988cdf4015f29e`, digest (first 12 hex) `f1a43cbf21cf`. The snapshot condenses the owner's 30-section brief and the approved plan: variant evaluation; evidence-based redesign; dependency-rule teaching order; layered content labeling; prediction gates, faded ladders, misconception checks, mixed retrieval, interleaved mastery with confidence calibration; glossary, concept map, localStorage review; zero-dependency accessible single file with governed provenance.
