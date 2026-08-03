# Content-package convention

**Status:** Approved  
**Owner:** Repository maintainer  
**Audience:** Repository maintainers, Source Stewards, generators, and documentation agents  
**Review date:** 2026-11-03  
**Related decision:** [ADR-0001](../adr/0001-content-package-layout.md)

## Purpose

Define one discoverable, format-neutral location for learning material without mixing it into the Learning OS operating manual. The convention preserves source artifacts and makes every source and generated result reachable from a nearby README.

## Scope and non-goals

This convention governs repository-local course and module material. It does not define source-rights approval, generation-run records, publishing, or application routing; those remain governed by the artifact contracts and operational records.

## Package layout

```text
content/
├── README.md
└── <course-slug>/
    ├── README.md
    └── <module-slug>/
        ├── README.md
        ├── sources/
        └── generated/
```

A course directory is an index of modules. A module directory is a leaf package and must contain `sources/`, `generated/`, and its README. A standalone topic may use the same leaf-package layout under its subject or course directory.

## Storage rules

- `sources/` contains original notebooks, PDFs, Markdown, slides, and other supplied input files. Preserve filenames and bytes after capture; source format is metadata, not a directory boundary.
- `generated/` contains learner-facing outputs derived from the package. Generated artifacts sit directly in this directory; do not create nested artifact directories. If a future output needs companion files, name them with the artifact's lowercase `kebab-case` prefix and document the relationship in the module README.
- The module README is the navigation surface. It must link to every source and generated artifact so a reader never has to browse both storage directories to discover material.
- The root and course READMEs are indexes only. They link downward and do not duplicate module-level file inventories.
- Directory names use lowercase `kebab-case`. Original source filenames are retained to preserve provenance.
- A package README records title, scope, source-rights status, provenance, and whether generated outputs have governed run and evaluation records. Unknown status must be stated as unknown, never inferred; owner-supplied material with unknown rights must carry a no-redistribution restriction until classified.

## Traceability boundary

A location under `content/` does not by itself make a source authorized or an output released. When the governed workflow begins, source-package identities, runs, evaluations, decisions, and memory remain in their canonical `records/` locations and are linked from the package README.

## Acceptance criteria

- Every module has one README that opens every contained source and output.
- No format-specific directory is introduced below `sources/`.
- Source bytes remain unchanged after organization.
- Generated artifacts have clear, direct filenames and no nested output directories.

## Change history

| Date | Change |
| --- | --- |
| 2026-08-03 | Approved initial convention and applied it to the restored AIML module. |
