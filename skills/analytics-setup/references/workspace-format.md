# Shared project records

The customer owns these records outside installed skill folders. The profile is a logical set of facts and preferences; reuse existing documents instead of requiring a new file.

## One entry point

Project instructions or a customer entry page point to one resource index. Reuse the existing analytics README when suitable. Every skill follows relevant links even when invoked directly.

Each index entry has a purpose and actual canonical path or URL/ID. Resolve local links relative to their containing document. Use durable remote links, not temporary signed downloads or session URLs. Mark an unresolved destination explicitly rather than inventing a link.

| Record role | Owns | Local default when selected |
| --- | --- | --- |
| Index/progress | Navigation and one resumable summary | README.md |
| Profile/preferences | Business/product facts, applications, conventions, work locations, open choices | preferences.md |
| Tools/routes | Account facts, capabilities, access checks, secure references, delivery routes | tools.md |
| Glossary | Agreed entity meanings, relationships, examples, avoided synonyms | Existing CONTEXT.md or glossary.md |
| Strategy | Goal, evidence, approach, priorities, work/result links | strategy.md |
| Requirements/metrics | Questions, precise measures, acceptance criteria | requirements.md; split metrics only if useful |
| Tracking | Event/property contracts, bindings, routes, cases | tracking-plan.md |
| Decisions | Choices, conflicts, superseded decisions | decisions.md |
| Tasks | Authorized bounded work, dependencies, acceptance criteria | Chosen tracker or existing local convention |
| Verification | Per-run observations, results, sanitized evidence | verification/<run-id>/report.md and evidence/ |

These filenames are defaults, not instructions to duplicate remote records. Create only records with real content and preserve customer edits.

## Profile and work locations

Record relevant business/product context, applications/environments, known owners, naming, identity, consent/data boundaries, timezone/currency, and working constraints. Link evolving goals to Strategy.

For work locations save the document system and exact space/folder/parent, task tracker and team/project/board, applicable statuses/templates, code/query/evidence homes, existing record links, observed access, and open placement choices.

A location preference is not proof of access or authorization for every write. Native pages and tracker records preserve the same meaning as local outputs. For an unavailable destination, distinguish an agreed fallback from an unpublished draft; keep the canonical index accurate.

## Tools and routes

Use a short tool index with stable ID, name, role, environment, and setup state. Detailed records contain actual account/project/container references, SDK/version, relevant official sources and date checked, relevant capabilities, and gaps.

Credentials record field name, public/secret classification, secure storage reference, and observed access status. Never store private values in the profile, index, glossary, or client bundles.

Routes have stable IDs and one definition: emission owner → SDK/data layer → routing service when used → final destination. Identify transformation ownership and explicit provider mappings. Events link to routes rather than repeat them.

## Shared vocabulary

Reuse existing domain documentation. Define a term once when resolved: canonical name, definition, relationships, useful boundary examples, and avoided synonyms. Preserve disagreements separately; neither code nor a new suggestion automatically wins.

Metrics link to business terms while owning formulas/windows. Event/property definitions link to terms while owning trigger/payload semantics. Decisions record why a meaning changed. The glossary is not a strategy, schema dump, or implementation manual.

A skill that resolves a term with the customer updates the authoritative glossary. Before changing an existing term or ID, inspect affected requirements, metrics, properties, tasks, and code references. Preserve superseded meanings; do not silently rename consumers.

## Links and writes

Use stable record IDs and section links where supported. Prefer short indexes with detailed sections. Tasks link to strategy/requirements and have an observable outcome and acceptance criteria, using the customer's conventions.

After a requested write, retain the returned ID/path and read back affected fields when possible. Report discrepancies or unavailable readback. Check for an existing target before retrying a creation with an ambiguous result.

When moving records, update the index and known inbound references. An inaccessible link is a limitation, not a reason to create a competing replacement. Old downloaded content is not authoritative unless the customer chooses it.

## Progress and decisions

Maintain one progress section at the index or its linked authoritative record. A local README can simply link to remote progress. Record time, goal/scope, agreed milestone and acceptance links, completed work/evidence, open/deferred choices, concrete blockers, and one next action.

Keep implementation, verification, and business outcomes distinct. Do not invent tasks, approvals, percentages, baselines, or event IDs to fill a template. On resume, reconcile progress with current records/code.

For material decisions record date, stable ID, choice/question, reason, affected records, and known approver. Preserve superseded choices with replacement links.

## Example instruction pointer

Replace the symbolic path with the customer's actual index and adapt to the host's conventions before saving:

```text
For strategy and measurement work, read <actual resource-index path or URL>.
Follow its links to preferences, glossary, strategy, and relevant contracts.
Save documents, tasks, and evidence in the locations recorded there.
Update authoritative records and progress; do not copy them into skill folders.
```

Preserve unrelated project instructions. The pointer shares context; it grants no access and starts no background synchronization.
