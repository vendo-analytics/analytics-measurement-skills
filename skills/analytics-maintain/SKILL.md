---
name: analytics-maintain
description: Review and maintain analytics when application features, event contracts, or selected tools change. Use to find measurement drift, update the tracking plan, and verify affected paths during development or a requested audit.
license: MIT
---

# Maintain measurement during development

Read the analytics-workspace pointer in project instructions, then preferences, tools/routes, requirements, tracking plan, decisions, and the latest relevant verification. If there is no recorded baseline, say so and discover the current behavior before proposing changes. Do not require another installed skill to inspect or update an existing plan.

## Use shared records

Resolve records through the customer resource index in project instructions or their entry document. Read relevant preferences, work locations, and glossary even when invoked directly. Local paths resolve from the containing document; remote records require available connector/browser access. Filenames below denote record roles, not a requirement to create local duplicates. Use the customer's canonical terms and surface conflicts before dependent work. When the customer resolves a term, update the authoritative glossary and inspect affected definitions rather than creating a second meaning.

Save outputs to the selected document/task/evidence homes. Preserve stable links and customer edits; update the index when records move. Read back writes when possible and retain real IDs/paths. Missing access or unavailable readback stays explicit; inspect for an existing record before retrying an ambiguous creation. Agree any fallback location instead of claiming an unpublished draft is remote. No customer record belongs in the installed skill folder.

## Compare intent, code, and evidence

Scope the review to the requested feature, diff, tool change, or audit boundary. Trace real event owners and callers. Compare required business outcomes with current triggers, payloads, identity/consent handling, route mappings, and verified destination evidence. Read current official documentation when a selected tool's behavior or SDK contract is uncertain.

Look for missing or obsolete events, duplicate bindings, accidental auto-capture overlap, naming/type drift, stale code references, changed login/logout behavior, orphaned routes, and gaps in verification. Distinguish intentional product changes from regressions. An empty destination or an old report is not proof of a newly introduced defect.

## Make a proportionate change

Reuse existing modules and customer preferences. Do not rename events, alter business definitions, replace tools, or change an architecture merely to make the plan tidier. Explain affected consumers before a material contract or route change and resolve the decision with the customer.

For an added or changed tool, update the actual account/capability/credential references in the indexed tools record (`tools.md` when local), check route ownership and duplicate delivery, and identify required implementation work. The setup skill can help if available; installed skill files never store customer configuration.

Apply authorized fixes end to end. If blocked by missing access, leave a precise finding and next action instead of a fake wired path. Background services, schedulers, and continuous monitoring are outside this workflow.

## Keep artifacts useful

- Update current preferences, requirements, tool facts, and event contracts in place, preserving customer edits and stable IDs.
- Keep business-event definitions shared across platforms, with actual codebase-specific bindings.
- Record material decisions and deprecations in `decisions.md`: date, decision, reason, affected IDs, and known approver. Preserve superseded entries and link replacements.
- Keep implementation status separate from evidence. A repaired call site does not prove destination receipt.
- Preserve old verification runs. Update navigation links rather than copying reports into other documents.

For new records, follow the customer's selected location and established format. For local Markdown use short indexes, detailed sections, and relative links; for remote records use native pages and durable record links. Split growing documents only when it improves navigation and preserve stable links.

## Verify the changed path

Run focused checks and repeat affected real web/native journeys. Use the verification skill if installed; otherwise independently inspect receipt in every affected final destination and save a new report with revision, environment, expected/observed values, correlation, and evidence. Use Pass, Fail, Blocked, or Not run according to what is actually known. Include relevant negative and duplicate-emission cases.

Finish with findings, changes, updated files, verification results, and unresolved items. State the scope and time of this review. Do not imply that the agent continues watching after the session ends.

Update one `## Progress` section in the workspace README or linked authoritative progress record after meaningful changes and before yielding: time, scope/stage, completed work with links, open decisions, blockers with concrete next actions, and one recommended next step. Link the current authoritative records, preserving earlier evidence and unrelated content. On resume, reconcile the summary with the current diff and records before continuing; do not repeat completed onboarding or treat an old verified milestone as proof of changed code.
