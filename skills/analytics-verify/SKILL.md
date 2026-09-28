---
name: analytics-verify
description: Verify analytics tracking against requirements, from real web or native interactions through final destination receipt. Use for tracking QA, regression checks, payload validation, and evidence-backed verification reports.
license: MIT
---

# Verify tracking end to end

Find the analytics workspace through project instructions and read preferences, tools/routes, requirements, tracking plan, and prior verification. If records are missing, establish the expected event behavior and test scope with the customer before declaring results. Other skills are optional, not required dependencies.

## Use shared records

Resolve records through the customer resource index in project instructions or their entry document. Read relevant preferences, work locations, and glossary even when invoked directly. Local paths resolve from the containing document; remote records require available connector/browser access. Filenames below denote record roles, not a requirement to create local duplicates. Use the customer's canonical terms and surface conflicts before dependent work. When the customer resolves a term, update the authoritative glossary and inspect affected definitions rather than creating a second meaning.

Save outputs to the selected document/task/evidence homes. Preserve stable links and customer edits; update the index when records move. Read back writes when possible and retain real IDs/paths. Missing access or unavailable readback stays explicit; inspect for an existing record before retrying an ambiguous creation. Agree any fallback location instead of claiming an unpublished draft is remote. No customer record belongs in the installed skill folder.

## Establish the test boundary

Identify the actual application/build revision, environment, URLs or app identifiers, destination accounts, SDK/container configuration, test identities, and available browser/device/API access. Use authorized test accounts and actions. A request to verify tracking is not permission to place a real paid order, send customer messages, or publish a production tag container. Use a safe authorized journey or state the missing prerequisite.

Inspect current official documentation for the selected tool's receipt readback, payload constraints, batching/delay, region, and supported correlation fields. Do not depend on a bundled destination-specific logger or assume all providers have a query API. Prefer an available read API that proves receipt; otherwise inspect the actual destination interface.

## Build cases

For an agreed first-event milestone, verify its full selected route and case scope. A passing event in one destination must not hide a required destination or negative case that remains blocked. Prefer exercising the real business action over creating a synthetic event solely to obtain a receipt.

Map each in-scope requirement/event to relevant positive, negative, property, identity, consent, configuration, and receipt cases. Each has steps, expected observations, route, and bounded observation window. Use the real trigger owner and distinguish intended behavior from current implementation. Existing disagreement needs resolution, not automatic acceptance of whichever source is easiest to inspect.

## Run the journey

Exercise real web interactions in the browser. For native apps, use available device, simulator, emulator, or user-assisted interaction with attributable evidence. A browser simulation cannot verify a native SDK. Don't substitute synthetic DOM clicks for an interaction whose real behavior differs.

Observe the chain separately:

1. The business action and canonical emission occurred as expected.
2. The event, property values/types, identity, consent, and route mapping match the plan.
3. The transport accepted the request, if that evidence is available.
4. Each selected final destination independently shows receipt with the required semantics.

An SDK call, fired tag, intercepted network request, HTTP success, or intermediate live feed alone is not final receipt. If an observation is unavailable, report that gap without manufacturing it from another layer. A receipt case may pass with independent destination evidence while an unobserved trigger-count case remains blocked.

Correlate using the tool's supported event/request IDs or an isolated test identity and time window. Avoid adding arbitrary payload fields that the destination rejects. Bound polling using known latency and the test's deadline. If receipt is still pending at the deadline, record Blocked with the last observation; record Fail when evaluable evidence contradicts the expected outcome. Negative cases require evidence of absence in a stated window.

Check relevant route changes, repeated renders/recomposition, restarts, failed actions, denied/revoked consent, login/logout, absent optional values, duplicates, and independent destination failure. Save sanitized API evidence or destination screenshots. Capture UI evidence with the host's native file/image tools; do not require a special screenshot receiver or hosted database.

## Report and rerun

Use [verification format](references/verification-format.md). Preserve a result per case and route, with Pass, Fail, Blocked, or Not run. Save new runs separately and compare only equivalent cases/revisions. Include exact missing access and user-assisted observations. Do not mark the whole implementation verified if required cases remain unproven.

Recommend fixes with their actual owner. Apply fixes only within the user's authorized scope, then repeat affected cases in a new run. Refresh preview/debug sessions after relevant configuration changes; old previews may show old behavior. Respect existing production publishing rules without inventing approval steps for already-authorized reversible fixes.

Return the report path, results, evidence links, and unresolved prerequisites. Verification is bounded work for this session, not an ongoing monitoring service.

Update one `## Progress` section in the workspace README or linked authoritative progress record after a result changes and before yielding: time, scope/stage, completed work with links, open decisions, blockers with concrete next actions, and one recommended next step. Mark a first-event milestone verified only when all its agreed cases pass, including each selected destination's receipt. Otherwise name the missing account/environment/access or unresolved evidence. Link this run without copying its result table. On resume, check the recorded revision and current code before reusing evidence.
