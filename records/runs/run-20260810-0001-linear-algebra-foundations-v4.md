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
| Source package | [SRC-2026-0001](../sources/src-2026-0001-aiml-4-module-02.md) | Notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445`, re-verified unchanged 2026-08-10 |
| Concept model | [CM-2026-0001](../concepts/cm-2026-0001-linear-algebra-foundations.md) | Unchanged; reused as pinned input |
| Learning plan | [LP-2026-0002](../plans/lp-2026-0002-linear-algebra-foundations.md) | New; supersedes LP-2026-0001 for new generation work |
| Experience specification | [XS-2026-0002](../specifications/xs-2026-0002-linear-algebra-foundations-v4.md) | New |
| Prior candidates | `linear-algebra-foundations-v1.html` (v1; renamed from `index.html` on 2026-08-11, bytes unchanged), CAN-2026-0001 (v2), CAN-2026-0002 (v3) | Evaluated comparatively in this run; bytes untouched |
| Prompt | Owner's 30-section brief + approved plan; condensed snapshot preserved in Appendix A, SHA-256 `f1a43cbf21cf6b894ad8f1f0b4b7b0218e3e55dfcefd024b3d988cdf4015f29e`, digest `f1a43cbf21cf` | Snapshot mechanism per RUN-20260804-0002 finding (e) |
| Model/configuration | Claude (Anthropic), operated through the Cline terminal shell harness | Exact model identifier and configuration labels not exposed to the operator; recorded as best-known-not-inferred |
| Rubric | [Evaluation framework](../../docs/06-evaluation/evaluation-framework.md) | Shaped Creator verification; scored pass in EVAL-2026-0002 |
| Workflow | [Quality loop](../../docs/03-workflows/quality-loop.md) | Stage 1 model per ADR-0002/ADR-0003 |
| Benchmarks | None | No benchmark suite exists; none used or claimed |

## Generation events

| Time | Candidate ID | Model/configuration | Prompt digests | Cost/latency | Warnings/errors |
| --- | --- | --- | --- | --- | --- |
| 2026-08-10 | CAN-2026-0003 | Claude (Anthropic) via Cline terminal shell; exact model ID not exposed | `f1a43cbf21cf` | Single operator session | 2 in-generation defects found and repaired (dead markup in debug card; invalid CSS declaration); 1 stray closing tag and 1 redundant JS condition found in self-review and repaired before verification |

Candidate: [`linear-algebra-foundations-v4.html`](../../content/aiml-4/module-02-math-statistics-for-ml/generated/linear-algebra-foundations-v4.html), SHA-256 `22b4047e7834ce233ff5088ff3d2e603242b8932e321f62004b823d076f445d6`, 172,736 bytes, zero external runtime dependencies. Filename per `<note-slug>-v<N>.html` convention (v4 = fourth generation: historical index.html = v1, CAN-2026-0001 = v2, CAN-2026-0002 = v3).

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

## Revision 1 — post-evaluation adversarial audit (2026-08-10, same run, pre-closure)

**Trigger:** Owner-requested thorough audit of CAN-2026-0003 against the owner brief and LP-2026-0002/XS-2026-0002. Method: scripted structural audit + two isolated adversarial sub-audits (content/mathematics; pedagogy) + operator technical audit (WCAG contrast measurement, handler-level runtime simulation under an instrumented DOM stub).

**Observed defects → root cause → disposition (all repaired in-place pre-closure; regression checks re-run):**

| # | Defect (severity) | Root cause | Fix |
| --- | --- | --- | --- |
| R1 | Unit 6 used matrix products (AᵀA, Aᵀb) before defining them — dependency-rule breach at the lesson's climax (MAJOR) | Plan mandated bridging only the inverse; the product was a blind spot inherited from the plan | Foundation block added: A shown explicitly (column of x's + column of 1s); AᵀA = [[55,15],[15,5]] and Aᵀb = [43,12] derived entry-by-entry via Unit 5 dot products, with forward link to Unit 7 |
| R2 | Confidence-calibration logic covered only radio items; numeric mastery items silently skipped the high-value flag and review routing — dead UI contradicting the Unit 0 contract (MAJOR) | Implementation oversight; radios and numerics grade through separate paths and only one was wired | NUM_CONF map added; numeric misses now trigger the flag and review routing (verified by handler simulation: confident miss on ‖(−8,15)‖₂ routes "L2 norm — Unit 4" to the review list) |
| R3 | Dot-lab angle arc could sweep the reflex angle in some quadrants (MAJOR, visual) | arc() end-angle normalization logic was quadrant-sensitive | Replaced with normalized signed sweep (−π, π]; anticlockwise flag from sign |
| R4 | Three gated widgets hidden via static HTML `hidden` attribute — invisible to no-JS readers (MINOR, fail-soft) | Gate state baked into markup | `hidden` now applied by JS at boot; no-JS readers see all content |
| R5 | wᵀx reveal described the transpose direction backwards (MINOR, wording) | Authoring slip | Corrected: transpose lays the column w down to a row; row × column = scalar |
| R6 | m7 option "rank drops by one" over-assumed a full-rank starting matrix (MINOR) | Phrasing | Rephrased: "columns become dependent — rank falls short of the column count" |
| R7 | Matrix-lab note called every area≈0 matrix "rank 1" (zero matrix is rank 0) (MINOR) | Overclaim | Rephrased: "rank is less than 2" |
| R8 | Footer claimed the "Scaler" typo was flagged in-body; it was not (MINOR, honesty) | Footer/body mismatch | In-body flag added in Unit 1 |
| R9 | Embedding-dimension figure carried a `source` tag; not from the source (MINOR, provenance) | Tagging error | Retagged `supplemental`, range corrected to 50–1,000 |
| R10 | Mastery norm item used the well-known (−6,8)→10 triple, answerable from memory (MINOR, pedagogy) | Item selection | Changed to ‖(−8,15)‖₂ = 17 (item, feedback, and answer key updated together) |
| R11 | Jargon cluster (gradient descent, Lasso, covariance, backpropagation, PCA, embedding, regularization) had no glossary rescue (MINOR) | Glossary scope | 7 glossary entries added (32 → 39) |
| R12 | Unit 0 oversold loop uniformity; concept map promised a revisit that never happened (MINOR) | Copy drift | Wording scoped to reality; "The map, completed" revisit added in Unit 9 |
| R13 | Notation collision (x = data vs unknown; x̂ = shadow vs solution) unmarked (MINOR) | Inherited from source conventions | "Notation honesty" note added at first collision in Unit 6 |
| R14 | Least-squares canvas rendered ~1240 px tall (portrait) (MINOR, UX) | Aspect-preserving view window on a tall data range | Window widened (−1.4…8.2 × −3.1…10.3), ~920 px |
| R15 | Dead width expression in residual-square drawing; stray empty fraction span; Python pseudo-code off-by-one; m5 scenario actor garbled; SSE/"pink areas" literal claim; aria-pressed on a non-toggle button (NITs) | Assorted | All repaired |

**Regression checks (post-revision, all PASS):** `node --check`; zero external references; duplicate-ID scan; tag balance; all data-g references resolve (39 glossary entries); AᵀA bridge values re-verified (55/15/5/43/12); m2 key consistency (item text, feedback, key = 17, recomputed ‖(−8,15)‖₂ = 17); DOM-stub load smoke test (14/14 effective); **handler-level simulation: 21/21** (gate commitment flow incl. refusal-without-choice, quiz grading with weak-topic record/clear, mastery scoring with confident-numeric-miss flagging and review routing, presets, matching, reveals, hints, reset); **WCAG contrast measured for all 12 text/background pairs — every pair ≥ 4.5:1 (AA normal)**.

**Revised artifact:** SHA-256 `9b621dee626b2801e6b1c7692ee251e56b8b487594d96ea372917f1a3fb5707b`, 178,754 bytes (supersedes the pre-audit build `22b4047e…f445d6`, 172,736 bytes; the earlier hash is retained in EVAL-2026-0002 for provenance).

## Lineage audit

- Source notebook SHA-256 `23c6f4ebe147e63db7adb5f6aa04e773d66bdf02a82f80605f9d8e1611f94445` — re-verified unchanged 2026-08-10.
- v1 `linear-algebra-foundations-v1.html` (renamed from `index.html` on 2026-08-11; bytes and hash unchanged) SHA-256 `687bccda2b71b8fd50b84a1198b194697598de6fa6c54e992c71ccdf5122fee1`; v2 `linear-algebra-foundations-v2.html` SHA-256 `0f0c499cfb94528938dee2f2e46b2a285b011157da9c8beb58761767542006f4`; v3 `linear-algebra-foundations-v3.html` SHA-256 `256201e20174b37ad8193817c37d4d69d3186d334de9f433db6b8d17748e0ac9` — all re-verified unchanged; none modified by this run.
- Chain: SRC-2026-0001 → CM-2026-0001 → LP-2026-0002 → XS-2026-0002 → CAN-2026-0003 → this run → EVAL-2026-0002. All links resolve within this repository.

## Appendix A — Prompt snapshot

Condensed snapshot preserved out-of-band at generation time (operator session log); SHA-256 `f1a43cbf21cf6b894ad8f1f0b4b7b0218e3e55dfcefd024b3d988cdf4015f29e`, digest (first 12 hex) `f1a43cbf21cf`. The snapshot condenses the owner's 30-section brief and the approved plan: variant evaluation; evidence-based redesign; dependency-rule teaching order; layered content labeling; prediction gates, faded ladders, misconception checks, mixed retrieval, interleaved mastery with confidence calibration; glossary, concept map, localStorage review; zero-dependency accessible single file with governed provenance.

## Appendix B — Retrospective iteration accounting (2026-08-11)

Per [ADR-0006](../../docs/adr/0006-record-iteration-accounting.md), this run's reconstructed counts: **generation iterations = 1** · **in-generation corrections = 4** (dead debug markup; invalid CSS declaration; stray closing tag; redundant JS condition — the latter two found in self-review before verification, matching the generation-events row above) · **revision cycles = 1** (Revision 1 — the post-evaluation adversarial audit; defect table above). Retrospective appendix; the run ledger's original body is unchanged.

## Appendix C — Current candidate identity at closure (2026-08-13)

Editorial clarity note (append-only): the candidate paragraph in Generation events records the pre-revision build (SHA-256 `22b4047e…f445d6`, 172,736 bytes). The current build — the one evaluated at closure — is SHA-256 `9b621dee626b2801e6b1c7692ee251e56b8b487594d96ea372917f1a3fb5707b`, 178,754 bytes (see Revision 1 above and EVAL-2026-0002). Future ledgers restate the final build identity in Decision and approvers per the 2026-08-13 run-template rule.
