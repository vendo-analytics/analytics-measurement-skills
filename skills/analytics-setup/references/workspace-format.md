# Shared project records

The customer owns these records outside installed skill folders. Setup owns the resource index, the setup record, and the tools record: how the skill set is used in this project. Strategy owns the business context, the glossary, and strategies: what the customer wants to get out of the work. Reuse existing documents instead of requiring new files.

## One entry point

Project instructions or a customer entry page point to one resource index. Reuse an existing analytics README when suitable. Every skill follows relevant links even when invoked directly.

Each index entry has a purpose and actual canonical path or URL/ID. Resolve local links relative to their containing document. Use durable remote links, not temporary signed downloads or session URLs. Mark an unresolved destination explicitly rather than inventing a link.

| Record role | Owner | Owns | Local default when selected |
| --- | --- | --- | --- |
| Index and progress | Setup creates; every skill updates progress | Navigation and one resumable progress summary | README.md |
| Setup record | Setup | Platforms and applications, work locations, permission defaults, workflows in play, tracking conventions, open choices | preferences.md |
| Tools and routes | Setup | Account facts, capabilities, access checks, secure references, delivery routes | tools.md |
| Business context | Strategy | Product, who it serves, journeys, business owners, constraints | business-context.md |
| Glossary | Strategy; any skill updates a resolved term | Agreed entity meanings, relationships, examples, avoided synonyms | Existing CONTEXT.md or glossary.md |
| Strategy | Strategy | Goal, evidence, approach, priorities, work and result links | strategy.md |
| Requirements and metrics | Requirements | Questions, precise measures, acceptance criteria | requirements.md; split metrics only if useful |
| Tracking | Implementation | Event and property contracts, bindings, routes, cases | tracking-plan.md |
| Decisions | Any skill | Choices, conflicts, superseded decisions | decisions.md |
| Tasks | Any skill, within permission | Bounded work, dependencies, acceptance criteria | Chosen tracker or existing local convention |
| Verification | Verification | Per-run observations, results, sanitized evidence | `verification/<run-id>/report.md` and `evidence/` |

These filenames are defaults, not instructions to duplicate remote records. Create only records with real content and preserve customer edits.

## Setup record

Record applications and environments, work locations, permission defaults, workflows in play, tracking conventions (naming, identity, consent and data boundaries, timezone, currency), and working constraints such as release rules. Business context and goals belong to strategy; link them from the index instead.

For work locations, save the document system and exact space, folder, or parent; the task tracker and team, project, or board; applicable statuses and templates; code, query, and evidence homes; existing record links; observed access; and open placement choices.

A location preference is not proof of access. Native pages and tracker records preserve the same meaning as local outputs. For an unavailable destination, distinguish an agreed fallback from an unpublished draft; keep the canonical index accurate.

## Permission defaults

Record the customer's choice for each action: Allowed, Ask, or Not allowed. When the customer has no view, use these defaults and record them as defaults:

| Action | Default |
| --- | --- |
| Save records in the recorded work locations | Allowed |
| Edit code in the project's repositories | Ask |
| Create or update tracker tasks | Ask |
| Change tool configuration in a test or development environment | Ask |
| Production publishing, live account changes, messages to customers, paid actions | Confirm each action; cannot be set to Allowed |

The customer's current request can authorize its own work unless the action is Not allowed. A request to plan or interview does not authorize implementation.

## Workflows in play

Record which workflows this project uses, for example planning only (strategy and requirements), planning and implementation, or the full implement, verify, and maintain loop. List other available capabilities the customer wants used, such as analysis or reporting tools. When nothing is recorded, every installed workflow is in play. Strategy routes only within this list and asks before widening it.

## Tools and routes

Use a short tool index with stable ID, name, role, environment, and setup state. Detailed records contain actual account, project, or container references, SDK and version, relevant official sources and date checked, relevant capabilities, and gaps.

Credentials record field name, public or secret classification, secure storage reference, and observed access status. Never store private values in the setup record, index, glossary, or client bundles.

Routes have stable IDs and one definition: emission owner → SDK or data layer → routing service when used → final destination. Identify transformation ownership and explicit provider mappings. Events link to routes rather than repeat them.

## Business context and glossary

Strategy owns both. Setup links existing ones it discovers and does not define business terms or goals. Metrics link to glossary terms while owning formulas and windows; event and property definitions link to terms while owning trigger and payload semantics. A skill that resolves a term with the customer updates the glossary and inspects affected consumers before changing an existing term or ID.

## Links and writes

Use stable record IDs and section links where supported. Prefer short indexes with detailed sections. Tasks link to strategy or requirements and have an observable outcome and acceptance criteria, using the customer's conventions.

After a requested write, keep the returned ID or path and read back affected fields when possible. Report discrepancies or unavailable readback. Check for an existing target before retrying a creation with an ambiguous result.

When moving records, update the index and known inbound references. An inaccessible link is a limitation, not a reason to create a competing replacement. Old downloaded content is not authoritative unless the customer chooses it.

## Progress and decisions

Maintain one progress section at the index or its linked progress record. A local README can simply link to remote progress. Record time, goal and scope, agreed milestone and acceptance links, completed work and evidence, open or deferred choices, concrete blockers, and one next action.

Keep implementation, verification, and business outcomes distinct. Do not invent tasks, approvals, percentages, baselines, or event IDs to fill a template. On resume, reconcile progress with current records and code.

For material decisions record date, stable ID, choice or question, reason, affected records, and known approver. Preserve superseded choices with replacement links.

## Example instruction pointer

Replace the symbolic path with the customer's actual index and adapt to the host's conventions before saving:

```text
For strategy and measurement work, read <actual resource-index path or URL>.
Follow its links to the setup record, business context, glossary, strategy, and relevant contracts.
Follow the recorded permission defaults and workflows in play.
Save documents, tasks, and evidence in the locations recorded there.
Update authoritative records and progress; do not copy them into skill folders.
```

Preserve unrelated project instructions. The pointer shares context; it grants no access and starts no background synchronization.
