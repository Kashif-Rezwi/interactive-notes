# ADR-0001: Adopt course and module content packages

**Status:** Accepted  
**Date:** 2026-08-03  
**Owner:** Repository maintainer  
**Decision scope:** Repository-local learning material storage and navigation  
**Supersedes / superseded by:** None

## Context and problem

Learning OS needs to keep heterogeneous input material and learner-facing outputs together without scattering them by source type or mixing them with architecture documents. Readers and agents should be able to find a module's notebook and interactive notes from one stable README.

## Decision

Store learning material beneath `content/`, grouped first by course or subject and then by leaf module package. Each module package contains only `sources/`, `generated/`, and a README that links to every item. Preserve original source filenames and bytes. Every generated artifact sits directly in `generated/`; nested output directories are not used.

## Decision drivers

- Fast human and agent discovery.
- Preservation of source provenance.
- Format-neutral storage that accommodates future inputs.
- A simple, direct output location for every generated artifact.
- Clear separation between learning material, governing documentation, and run evidence.

## Considered options

| Option | Benefits | Costs/risks | Why selected or rejected |
| --- | --- | --- | --- |
| Type-specific top-level folders | Familiar for each input type | Splits a module across locations and grows with every new format | Rejected |
| Place outputs beside each source file | Minimal hierarchy | Ambiguous with multiple sources and outputs; weak navigation | Rejected |
| Course/module packages with direct `sources/` and `generated/` files | Cohesive, navigable, extensible, and shallow | Requires README discipline and artifact filename care | Selected |

## Consequences

Package READMEs become required navigation documents. This adds a small documentation obligation but avoids folder discovery work. Source authorization and release governance remain explicit because `content/` is storage, not evidence of approval. Generated artifacts must have descriptive direct filenames; a future need for deeply packaged output requires a new ADR. The layout is reversible with file moves and does not commit the future application to a storage technology.

## Evidence and validation

The convention is applied to the restored AIML Module 2 notebook and interactive notes. Verification must confirm both historical source and generated file hashes are unchanged after the move and that README links resolve locally.

## Rollback or migration plan

Move package directories to a replacement convention while preserving file bytes, then update package and index links in one migration commit. Retain this ADR as historical rationale and supersede it if the decision changes.

## Review evidence

Recorded retrospectively on 2026-08-13 per the review policy's status-accuracy rule: this ADR was reviewed and accepted by the repository maintainer (Human Accountable Owner) on 2026-08-03 under a solo-maintainer self-review — the practice later codified as the Stage 1 solo-maintainer path. Scope inspected: the content-package layout, the repository-map placement, and the convention's application to the restored AIML module. Evidence considered: byte-identical preservation of the source notebook and historical artifact across the move (hashes re-verified) and local resolution of all package README links. Decision: accept. Limitation: non-independent self-review — no second reviewer existed at Stage 1.

## Review trigger/date

Review when a package needs restricted access, more than one independent source lineage, or a source/output relationship that cannot be represented clearly by the module README; otherwise review by 2026-11-03.
