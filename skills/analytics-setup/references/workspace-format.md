# Customer workspace format

Use Markdown with short indexes and detailed sections. Reuse existing equivalent records rather than creating duplicates. Create files when they have meaningful content.

| File | Owns |
| --- | --- |
| `README.md` | Navigation and one resumable progress summary linking to current decisions and evidence |
| `preferences.md` | Customer choices and cross-tool conventions |
| `tools.md` | Tool/account facts, routes, access and setup status |
| `requirements.md` | Business outcomes and proposed measurement |
| `tracking-plan.md` | Agreed events, properties, platform bindings, and test cases |
| `decisions.md` | Material decisions, unresolved choices, and superseded choices |
| `verification/<run-id>/report.md` | Observations and results for one actual run |
| `verification/<run-id>/evidence/` | Sanitized API receipts, screenshots, and other evidence |

## Progress in the workspace README

Maintain one `## Progress` section, or reuse the customer's equivalent, with:

- Updated time, current business scope, and stage: setup, requirements, implementation, verification, or maintenance.
- First milestone, when agreed: the business question, event/requirement links, selected routes, and acceptance-case links. Do not invent event IDs before their records exist.
- Completed work: short statements linking to actual files or evidence.
- Open decisions and explicitly deferred scope, linking to their owning records.
- Blockers: affected tool/account/environment, missing access or evidence, who can resolve it when known, and concrete action needed. No credentials.
- One recommended next action that follows the earliest unresolved dependency.

Update after meaningful progress and before yielding, including a blocked stop. Other skills maintain the same section. Keep it concise; contracts and results remain in their owning files. A stage is not proof of completion. If the summary disagrees with current code or linked records, reconcile the difference on resume before changing anything dependent on it. Preserve unrelated README content and customer edits. No separate progress database or percentage-complete estimate is needed.

## Preferences

Use an H1 title and sections for application context, environments, naming/casing, identity, data boundaries, measurement conventions, and working preferences. A small frontmatter block can record `type` and `updated`; add an owner only when known.

Record repositories and platform versions, business vocabulary, environment targets, event naming framework, event and property casing, anonymous/user/account definitions, login/logout behavior, consent expectations, prohibited fields, and relevant currency/timezone/unit conventions. Preserve explicit exceptions. Do not treat an unknown value as a default the customer has approved.

## Tools and routes

Start with an index containing a stable tool ID, actual tool name, role, environment, and setup state. Detailed records include account/project/container IDs, non-secret URLs, SDK/version, official sources and date checked, required setup fields, public/secret classification, secure credential references, and access-check results.

Record only capabilities relevant to the customer's work: collection, identity, name/property restrictions, delivery, and receipt readback. State missing access and constraints. Customer-specific findings belong here even though the skill is tool-neutral.

Give routes stable IDs such as `ROUTE-001`. Describe emission owner → SDK/data layer → routing service, if any → final destination. Identify which component owns transformations and which existing routes must be disabled if the customer agrees to change routing. Do not duplicate routes in every event record; reference their IDs.

## Decisions and links

Each material decision has a stable ID, date, question/decision, reason, affected records, and who agreed it when known. Keep superseded choices linked to replacements. Unresolved questions remain explicit.

Use relative links, stable record headings such as `## REQ-001`, and short tables. Keep lengthy explanations below the table. Dates use ISO format; evidence timestamps include an offset. Never store private credentials, invent approvals, or seed fictional test evidence. A requirements interview should fill the requirements document, not setup guesses.
