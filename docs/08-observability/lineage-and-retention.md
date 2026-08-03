# Lineage, Retention, and Incident Learning

## Traceability graph

Maintain links from request → source package → extraction → concept model → learning plan → experience specification → prompt bundle/model → run → candidate → evaluation → decision → release → memory. Links carry version, time, actor role, and relation type such as `derived-from`, `evaluated-by`, `supersedes`, `blocked-by`, or `released-as`.

## Retention classes

| Class | Examples | Rule |
| --- | --- | --- |
| Public durable | Approved docs, ADRs, public benchmark metadata | Retain version history |
| Internal durable | Run ledgers, evaluations, experiments, prompt snapshots | Retain by policy; access controlled |
| Restricted | Rights evidence, sensitive source metadata, learner-related material | Minimize, encrypt/control access, explicit retention owner |
| Ephemeral | Scratch context and temporary drafts | Auto-expire after promotion decision |

Exact time periods are policy decisions to be made before handling production data; they require legal, privacy, and operational review. Until then, retain only what is necessary for documentation work.

## Incident learning

An incident is a material breach of quality, trust, rights, privacy, accessibility, cost control, or workflow integrity. Preserve the evidence, contain further use, notify the accountable owner, assess affected artifacts, record root cause and corrective action, and create a memory/ADR only after review. Blameless analysis is compatible with clear accountability.
