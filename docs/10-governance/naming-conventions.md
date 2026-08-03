# Naming Conventions

## General rules

Use lowercase `kebab-case` for directory and Markdown filenames. Use a stable typed identifier in record content, independent of its filename. Names describe a responsibility or outcome, never a transient implementation detail.

## IDs

| Object | Pattern | Example |
| --- | --- | --- |
| Architecture decision | `ADR-NNNN` | `ADR-0007` |
| Source package | `SRC-YYYY-NNNN` | `SRC-2026-0042` |
| Concept model | `CM-YYYY-NNNN` | `CM-2026-0011` |
| Learning plan | `LP-YYYY-NNNN` | `LP-2026-0011` |
| Experience specification | `XS-YYYY-NNNN` | `XS-2026-0011` |
| Prompt card | `PRM-role-slug` + semantic version | `PRM-teacher-concept-explain@1.2.0` |
| Generation run | `RUN-YYYYMMDD-NNNN` | `RUN-20260803-0001` |
| Candidate artifact | `CAN-YYYY-NNNN` | `CAN-2026-0011` |
| Evaluation | `EVAL-YYYY-NNNN` | `EVAL-2026-0011` |
| Experiment | `EXP-YYYY-NNNN` | `EXP-2026-0003` |
| Memory item | `MEM-YYYY-NNNN` | `MEM-2026-0020` |
| Benchmark suite/case | `BMK-name@version` / `CASE-name@version` | `BMK-core@1.0` |

## Titles and versions

Use sentence case for document titles. Record titles begin with their ID and a concise outcome, such as `ADR-0007: Preserve prompt snapshots for reproducibility`. Use ISO 8601 dates and UTC timestamps in future structured records. Never use “final”, “new”, “v2”, or “latest” as identity; use status and explicit version instead.
