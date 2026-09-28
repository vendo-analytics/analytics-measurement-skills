---
name: analytics-implement
description: Implement or repair agreed analytics instrumentation in web or native codebases. Use to bind business triggers, integrate the customer's chosen SDK or routing layer, and keep event contracts aligned with application behavior.
license: MIT
---

# Implement tracking

Read the project's analytics-workspace pointer, preferences, tools, requirements, and tracking plan. Reuse equivalent existing documents. If missing, collect only the requirements and decisions needed for the requested change and record them before editing. Do not require another installed skill to proceed.

## Trace ownership

Find the module that owns the real business action and the existing analytics path. Read actual callers, initialization, identity/consent handling, automatic capture, tag/container routes, and destination mappings. A similarly named file is not proof of ownership. Inspect other relevant codebases when a shared event crosses client/server or mobile/web boundaries.

Use [platform practices](references/platform-practices.md) for the affected codebase. Preserve working application conventions. Do not introduce an oversized analytics abstraction or custom connector framework just because several SDK calls look similar.

## Resolve the event contract

Use [tracking-plan format](references/tracking-plan-format.md) to record event meaning, exact firing and exclusion conditions, properties, identity, consent, route IDs, platform bindings, and test cases. Follow the customer's naming/casing choices. Resolve unknown business semantics with them instead of choosing new rules based on TypeScript or SDK signatures.

Bind each defined trigger once, then route from that canonical emission. Choose the authoritative emission owner for each business fact. A client submission attempt and a confirmed server outcome are different facts unless an explicit correlation/deduplication contract says otherwise. Do not promise global exactly-once delivery.

## Discover the selected tool's contract

Inspect the installed SDK/version and current official documentation for collection, initialization, identity, consent, reserved names, payload limits, supported platforms, and receipt verification. Record relevant links and verified constraints in the customer's tools document. Do not use a fixed provider catalog or assume a capability exists because another tool has it.

- With an existing CDP or tag manager, emit through its existing interface and manage downstream routes there where supported. Distinguish browser and server containers.
- With direct SDKs, keep routing and transformations in the application's existing analytics owner, outside individual UI handlers.
- An experimentation or advertising tool may need its own client capability. Document the reason and keep the business-event delivery path unambiguous.

Public collection IDs may belong in clients; private API credentials do not belong in web or native bundles. Use the customer's credential references and environment boundaries. Browser/connector tools can configure selected accounts when authorized; local code authorization does not automatically authorize production publishing.

## Implement and verify

Complete the actual requested path: initialization, trigger, payload, identity transitions, consent behavior, route mapping, and failure isolation. Preserve supported SDK behavior for retries/buffering instead of building a background service. A tracking exception must not block the customer's business action. Do not silently drop fields or normalize reserved names in ways that change their meaning.

Run the smallest relevant checks for the changed path. Exercise actual interactions in the browser or native device/simulator when available. Check repeated rendering, navigation, reload/restart, failed business actions, denied consent, logout, and existing automatic capture where relevant. A local unit test or emitted request alone does not prove destination receipt.

Then verify each selected final destination through a read API or its interface, correlated to the test event/identity and time window. Use the verification skill if installed, or record the same evidence yourself: revision, environment, steps, expected/observed values, receipt, and limitations. Missing receipt access remains Blocked, not Pass. Keep authorized changes and blocked external configuration clearly distinguished; never present a partly wired path as complete.

Update real code references and implementation states in the tracking plan. Mark the contract Agreed only from customer agreement, a binding Implemented only after it exists, and receipt verified only from evidence. Report what changed, focused checks, per-destination results, and remaining prerequisites.
