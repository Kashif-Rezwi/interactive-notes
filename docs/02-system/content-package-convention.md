# Content-package convention

**Status:** Approved<br>
**Owner:** Repository maintainer<br>
**Audience:** Repository maintainers, Source Stewards, generators, and documentation agents<br>
**Review by:** 2026-11-04<br>
**Related decision:** [ADR-0001](../adr/0001-content-package-layout.md)

## Purpose

Define one discoverable, format-neutral location for learning material without mixing it into the Learning OS operating manual. The convention preserves source artifacts and makes every source and generated result reachable from a nearby README.

## Scope and non-goals

This convention governs repository-local course and module material. It does not define source authorization, generation-run records, publishing, or application routing; those remain governed by the artifact contracts and operational records.

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

A course directory is an index of modules. A module directory is a leaf package and must contain `sources/`, `generated/`, and its README. Multi-session modules keep this single layout: all classes' sources and generated artifacts share the `sources/`/`generated/` pairs, and the module README is the single navigation surface mapping each class to its files. Class identity lives in `records/` and README rows, and files are disambiguated by `<note-slug>-v<N>` filenames. A standalone topic may use the same leaf-package layout under its subject or course directory.

## Storage rules

- `sources/` contains original notebooks, PDFs, Markdown, slides, and other supplied input files. Preserve filenames and bytes after capture; source format is metadata, not a directory boundary.
- `generated/` contains learner-facing outputs derived from the package. Generated artifacts sit directly in this directory; do not create nested artifact directories. Future outputs use descriptive lowercase `kebab-case` filenames. Rebuilds of the same note append a trailing ordinal version — `<note-slug>-v<N>.<ext>` per the [naming conventions](../10-governance/naming-conventions.md) — so every generation of a note is discoverable by name, while the candidate ID remains the stable identity. A historical `index.html` may remain only when its module README labels it as a historical naming exception.
- The module README is the navigation surface. Its reference table links each class's **current** material — the source note and the **reference candidate**: the highest-ordinal `<note-slug>-v<N>` generation whose evaluation has closed pilot-complete or better; if no generation qualifies, the row links the source only. Rows are listed in **class sequence** (the order classes were actually taught), with new classes appended, never re-ordered, and never annotated with chronology. Historical versions stay preserved on disk and remain traceable through run ledgers and a clearly labeled version-history table; they are never listed as open entry points.
- Directory listings (`sources/`, `generated/`) are alphabetical and are **not an ordering signal**. Class sequence is defined exclusively by the module README's classes table; never infer class order from file enumeration. Source filenames are preserved originals; generated filenames follow the `<note-slug>-v<N>` contract.
- The root and course READMEs are indexes only. They link downward and do not duplicate module-level file inventories.
- Directory names use lowercase `kebab-case`. Original source filenames are retained to preserve provenance.
- A package README records title, scope, source provenance, and whether generated outputs have governed run and evaluation records. It links to its source-identity record when one exists. Unknown provenance must be stated as unknown, never inferred.

## Traceability boundary

A location under `content/` does not by itself make a source authorized or an output released. When the governed workflow begins, source-package identities, runs, evaluations, decisions, and memory remain in their canonical `records/` locations and are linked from the package README.

## Historical artifact boundary

A preserved historical artifact may be retained without being a governed release. Its README and source record must identify immutable bytes, unavailable lineage, and any unassessed third-party runtime dependencies. Do not treat that artifact as approved for hosting, learner release, accessibility, privacy, security, reproducibility, or benchmark use until a new governed run establishes the required evidence. Preserve its bytes; create a new candidate rather than modernizing or retroactively certifying it.

## Acceptance criteria

- Every module has one README whose reference table opens each class's source and reference candidate (when one qualifies); every contained artifact remains discoverable through that table, the version-history table, and record links.
- No format-specific directory is introduced below `sources/`.
- Source bytes remain unchanged after organization.
- Generated artifacts have clear, direct filenames and no nested output directories.

## Change history

| Date | Change |
| --- | --- |
| 2026-08-03 | Approved initial convention and applied it to the restored AIML module. |
| 2026-08-04 | Clarified source-identity links and the historical `index.html` naming exception. |
| 2026-08-04 | Added the versioned generated-artifact filename rule (`<note-slug>-v<N>.<ext>`) and linked it to the naming conventions; applied it to AIML-4 Module 2 (`linear-algebra-foundations-v3.html`, CAN-2026-0002). |
| 2026-08-11 | Evaluated a class-package level for multi-session modules ([ADR-0005](../adr/0005-class-packages-within-modules.md)) and rejected it: modules keep the leaf-package layout with a single README as the navigation surface; class identity lives in `records/` and README rows, and files are disambiguated by note-slug. Applied to AIML-4 Module 2 ("Math & Statistics for ML"), which retains a single package whose `sources/` and `generated/` are shared by Class 1 (linear algebra) and the upcoming Class 2 (probability basics). |
| 2026-08-11 | Reference-candidate rule: module READMEs list each class's source and reference candidate only, in class sequence (appended, never annotated); parallel version enumeration becomes a clearly labeled version-history table. |
