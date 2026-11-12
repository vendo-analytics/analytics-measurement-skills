# Session handoff records

Session wrap-up owns a bounded handoff artifact and coordinates updates to existing records. It does not create a parallel context store or take over domain verification.

## Contents

1. Record ownership
2. Handoff artifact
3. Provenance and completion states
4. Revision and write safety
5. Final checks

## Record ownership

| Record | Session wrap-up behavior |
| --- | --- |
| Resource index and progress | Reuse the existing index. Link the handoff and maintain one progress summary. |
| Setup, preferences, and tools | Update only confirmed changes through their owning workflow or native record. Leave unrelated setup untouched. |
| Business context, glossary, and strategy | Apply only resolved session changes; preserve existing ownership, stable IDs, proposed states, and open choices. |
| Decisions | Add material decisions with date, stable ID, choice, reason, affected records, known approver, and supersession links. |
| Artifacts and domain outputs | Link real IDs and revisions. Do not copy full reports, plans, analyses, or code into the handoff. |
| Evidence and runs | Link or append sanitized session evidence under its owning convention. Preserve prior runs and their actual results. |
| Tasks and external actions | Link existing objects when relevant. Create or change nothing without separate authorization. |
| Session handoff | Create or update one record for this session, or reuse the workspace's native equivalent. |

Create only records with real content. Do not create an empty session log, decision, task, or evidence file to satisfy a template.

## Handoff artifact

Use an existing session-log convention when present. When local storage is selected and no suitable convention exists, use `sessions/<session-id>.md` linked from the resource index. A short session with no separate handoff record may use the existing progress record if it can hold the required links and limitations without duplication.

Include the artifact envelope in the native format or associated structured payload:

- `schema_version` and `artifact_type: session_handoff`.
- `skill_id` and `skill_revision` for traceability to the workflow source.
- `created_at`, plus session start and end times when known.
- `context_revision`, or `unknown` when unavailable.
- `inputs` linking the prior progress, session instructions, and supplied records without secrets.
- `evidence` linking actual artifacts, observations, queries, sources, and run records.
- `limitations` for missing access, unresolved conflicts, uncertainty, and unverified work.
- `related_objects` with real stable IDs and direct links to changed records, decisions, tasks, and reports that exist.

The handoff body contains:

1. **Goal and scope:** the bounded session purpose and what was not in scope.
2. **Starting point:** prior progress and relevant record revisions used for reconciliation.
3. **Confirmed changes:** customer-confirmed updates with links to their owning records.
4. **Artifacts and decisions:** actual created or updated objects, with proposed and agreed states preserved.
5. **Evidence and results:** implementation, verification, destination receipt, and business impact stated separately.
6. **Unresolved work:** open questions, blockers, owners, missing access, and pending evidence.
7. **Next action:** one bounded action, required input or permission, and the record to read first.

## Provenance and completion states

Use the shared states consistently:

| State | Session requirement |
| --- | --- |
| `customer_confirmed` | Preserve the explicit confirmation and its date or conversation/record reference. Silence and document creation are not confirmation. |
| `observed` | Link the actual file, object, account-safe identifier, observation, and scope inspected. |
| `researched` | Retain publisher, canonical URL, retrieval date, supported claim, and limitations for material actually retrieved. |
| `inferred` | Keep the reasoning and confirmation or falsification step visible. Never record an inference as a completed outcome. |
| `unknown` | Name the missing fact or access and who or what can resolve it. |

Do not collapse these distinctions when summarizing. A previously confirmed fact may retain its original provenance; a new agent summary does not make it newly confirmed.

Use precise delivery language:

- **Saved:** the record exists at the stated destination and, when available, readback succeeded.
- **Implemented:** the actual code or configured object changed; this does not prove delivery or impact.
- **Verified:** named acceptance evidence passed for the same revision and scope.
- **Blocked:** an identifiable missing input, access, or failed prerequisite prevents the result.
- **Proposed:** a recommendation or plan has not been agreed or activated.

A successful intermediate call is not final receipt. An analysis can be complete and inconclusive. An intervention can await an observation window.

## Revision and write safety

Before updating, retain each target's stable ID and revision, hash, or exact current content. Use revision-checked host writes where supported.

For local records, change only the relevant sections with the smallest exact edit. Use atomic replacement when available. If a recovery copy is needed, keep it outside the canonical record set and do not index it as a second authority. Retain it only until readback succeeds, then follow the host's cleanup convention.

If the target changed after the read:

1. Stop the affected write; do not force it.
2. Re-read the latest record and identify customer or concurrent changes.
3. Reconcile the session's still-relevant update against that revision.
4. Preserve unrelated edits and record any unresolved conflict in the handoff.

After an ambiguous write, retain any returned ID and search for the object before retrying. Read back important fields and links. If readback is unavailable, report the limitation rather than claiming verification. Never place secrets or private provider values in the handoff, evidence, progress, or recovery copies.

## Final checks

Before yielding, verify:

1. This session's changes are separated from earlier work and linked to their owning records.
2. Existing stable IDs and one progress authority are reused; no duplicate handoff or domain record was created.
3. Customer edits and unrelated content survive, and stale writes stopped safely.
4. Confirmed, observed, researched, inferred, and unknown claims retain their meanings.
5. Implementation, verification, receipt, and business impact are not conflated.
6. Open questions, blockers, owners, and pending evidence remain visible.
7. One next action names its required input or permission and first record to read.
8. Important writes were read back, or their limitations are explicit.
9. No unapproved task, schedule, external message, paid call, provider connection, or production change occurred.
10. The handoff works without the earlier chat transcript.
