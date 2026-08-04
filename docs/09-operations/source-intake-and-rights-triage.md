# Source intake and rights triage

**Status:** Experimental<br>
**Owner:** Repository maintainer / Human Accountable Owner<br>
**Review by:** 2026-11-04<br>
**Validation and promotion trigger:** Three completed private pilots plus the review evidence required by the review policy.

## Purpose

Classify a source package before extraction, transformation, benchmark use, or release. This operational playbook records permitted use; it is not legal advice and does not resolve ambiguous legal questions.

## Trigger, owner, and output

**Trigger:** a new source is proposed for Learning OS work.<br>
**Primary owner:** Source Steward.<br>
**Approver for public use or exceptions:** Human Accountable Owner.<br>
**Output:** a `SRC-YYYY-NNNN` manifest in `records/sources/`, linked from the nearest content-package README.

## Classification procedure

| Classification | Minimum evidence | Permitted default | Escalate when |
| --- | --- | --- | --- |
| Self-authored, private-use | Owner attestation | Private research and internal pilots only | Public distribution or external contribution is proposed |
| Self-authored, public distribution authorized | Owner attestation naming the permitted distribution | Public display and distribution in the named repository or channel; reuse rights remain reserved unless separately licensed | A license, third-party reuse, or a new distribution channel is proposed |
| Openly licensed | License text or durable URL, attribution requirements, and derivative terms | Use only within recorded license terms | Compatibility, attribution, or derivative-work terms are unclear |
| Institutional or restricted | Usage agreement, institutional policy, or written permission | Only the documented scope; no public redistribution by default | Any transformation, publication, or scope expansion is proposed |
| Unknown origin or rights | Investigation note and absent/uncertain evidence | No transformation, benchmark use, or public release; retain only under explicit no-redistribution controls | Any use beyond private inspection is proposed |

## Required manifest checks

1. Identify the exact source files and record immutable identities such as SHA-256 hashes.
2. Record origin, author or owner attestation, language, retrieval or capture time, scope, and sensitive-content flags.
3. Record the classification, approved uses, prohibited uses, attribution requirements, and review trigger.
4. Link the manifest from the content package. Do not infer authorization from a file path or public availability.
5. Escalate unclear rights, sensitive data, or a proposed public release before generation begins.

## Exit criteria

The package may enter the applicable workflow only when a manifest exists, its classification supports the proposed use, and any required owner decision is recorded. A historical artifact without a governed run remains unreleased even if public distribution is authorized.
