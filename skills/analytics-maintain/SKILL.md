---
name: analytics-maintain
description: Review and maintain analytics when application features, event contracts, or selected tools change. Use to find measurement drift, update the tracking plan, and verify affected paths during development or a requested audit.
license: MIT
---

# Maintain measurement during development

Read the analytics-workspace pointer in project instructions, then preferences, tools/routes, requirements, tracking plan, decisions, and the latest relevant verification. If there is no recorded baseline, say so and discover the current behavior before proposing changes. Do not require another installed skill to inspect or update an existing plan.

## Compare intent, code, and evidence

Scope the review to the requested feature, diff, tool change, or audit boundary. Trace real event owners and callers. Compare required business outcomes with current triggers, payloads, identity/consent handling, route mappings, and verified destination evidence. Read current official documentation when a selected tool's behavior or SDK contract is uncertain.

Look for missing or obsolete events, duplicate bindings, accidental auto-capture overlap, naming/type drift, stale code references, changed login/logout behavior, orphaned routes, and gaps in verification. Distinguish intentional product changes from regressions. An empty destination or an old report is not proof of a newly introduced defect.

## Make a proportionate change

Reuse existing modules and customer preferences. Do not rename events, alter business definitions, replace tools, or change an architecture merely to make the plan tidier. Explain affected consumers before a material contract or route change and resolve the decision with the customer.

For an added or changed tool, update the actual account/capability/credential references in `tools.md`, check route ownership and duplicate delivery, and identify required implementation work. The setup skill can help if available; installed skill files never store customer configuration.

Apply authorized fixes end to end. If blocked by missing access, leave a precise finding and next action instead of a fake wired path. Background services, schedulers, and continuous monitoring are outside this workflow.

## Keep artifacts useful

- Update current preferences, requirements, tool facts, and event contracts in place, preserving customer edits and stable IDs.
- Keep business-event definitions shared across platforms, with actual codebase-specific bindings.
- Record material decisions and deprecations in `decisions.md`: date, decision, reason, affected IDs, and known approver. Preserve superseded entries and link replacements.
- Keep implementation status separate from evidence. A repaired call site does not prove destination receipt.
- Preserve old verification runs. Update navigation links rather than copying reports into other documents.

For new records, follow the customer's established format. Use plain Markdown, short indexes, detailed sections, and relative links. Split growing documents only when it improves navigation and preserve stable links.

## Verify the changed path

Run focused checks and repeat affected real web/native journeys. Use the verification skill if installed; otherwise independently inspect receipt in every affected final destination and save a new report with revision, environment, expected/observed values, correlation, and evidence. Use Pass, Fail, Blocked, or Not run according to what is actually known. Include relevant negative and duplicate-emission cases.

Finish with findings, changes, updated files, verification results, and unresolved items. State the scope and time of this review. Do not imply that the agent continues watching after the session ends.
