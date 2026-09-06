# EVAL-2026-0011: Matrix decompositions and applications v1

**Candidate ID/version:** CAN-2026-0010, [matrix-decompositions-applications-v1.html](../../content/aiml-4/module-02-math-statistics-for-ml/generated/matrix-decompositions-applications-v1.html), SHA-256 `423ec96635f7e5be3e0a0c6a6dd3c4efd1d93eddc884840435b6f01c976e2425`  
**Rubric version:** Stage 1 evaluation framework + lesson standard §10.6–10.8  
**Evaluator role/identity:** Repository maintainer, Reviewer profile  
**Evaluation mode:** script-assisted, browser-assisted, non-independent  
**Operating scope:** Stage 1 private pilot  
**Review independence:** non-independent  
**Public-release eligibility:** ineligible  
**Confidence:** medium  
**Recommendation:** private-pilot-complete  
**Iterations reviewed:** builds = 1; revision cycles = 0

## Scope and evidence inspected

Source notebook and SHA identity; CM/LP/XS records; candidate HTML; strict verifier output; live browser interaction trace and screenshot; run ledger. Coverage includes all 40 source cells: agenda, eigenpairs/spectrum, diagonalization, SVD, applications, PCA, low-rank approximation, and latent-space close.

## Dimension scorecard

| Dimension | Score | Evidence | Defects/severity | Remedy | Confidence |
|---|---:|---|---|---|---|
| Educational quality | 3.5 | Five dependency-ordered units, formula keys, ladders, prediction, checks, model-answer feedback | Minor: no full numeric SVD computation | Future extension only | medium |
| Factual/mathematical accuracy | 3.5 | Live eigen, power, and PCA energy recomputation; source claims softened where broad | None observed | — | medium-high |
| Source grounding | 3.5 | All 40 cells dispositioned and anchored in CM/XS | Minor: source has no numeric SVD example | Keep constructed examples labeled | medium |
| Interactivity and agency | 3.5 | Four sliders, prediction gate, five checks, live feedback | None material | — | medium-high |
| Accessibility and inclusion | 3.5 | Native controls, SVG text alternatives, labels, reduced motion, print fallback | No screen-reader specialist pass | Specialist review before any public release | medium |
| Visual clarity | 3.5 | Pinned tokens, frosted nav, readable cards, labeled SVG pipeline | Screenshot evidence at active viewport only | Broaden breakpoint capture | medium |
| User experience | 3.5 | Orientation, map, goal strips, live readouts, feedback | No persistent progress state beyond browser session | Consider in next iteration | medium |
| Completeness | 3.0 | Glossary, map, formulas, checks, colophon, provenance | Source asks for more applications than this compact pilot expands | Add application cases only with evidence | medium |
| Readability | 3.5 | Short blocks, explicit symbol keys, direct definitions | None material | — | medium-high |
| Technical feasibility/performance intent | 3.5 | 24.8KB single file, zero external requests, strict verifier clean | Browser viewport helper could not be resized through the available wrapper | Repeat with full breakpoint harness | medium |

## Weighted result and gate check

Weighted score: **3.45 / 4.00**. All hard-gate dimensions are at least 3.5 except completeness, which is non-hard-gate; no score is 0–1, no critical defect is unresolved, and the candidate is private-pilot-complete only. Public release is ineligible because review is non-independent.

## Non-negotiable blockers

None for private-pilot scope. The candidate must not be described as a public release, benchmark result, or efficacy claim.

## Reviewer sign-off

Disposition: **private-pilot-complete**. Non-independent review; future work should add a second browser breakpoint capture and, if expanding application claims, a domain review.
