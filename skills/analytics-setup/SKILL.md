---
name: analytics-setup
description: Set up how the strategy and measurement skills work in this project. Record tools, platforms and applications, where documents, tasks, and evidence are saved, what the assistant may do without asking, which workflows are in play, and tracking conventions; save a resource index that every skill reads. Use for first-time setup, a new or changed tool, or changed working preferences. Business goals and context belong to strategy.
license: MIT
---

# Set up how the skill set works

Produce a customer-owned setup record and resource index that every skill can find. Use [workspace format](references/workspace-format.md) for records and links. Setup records how the skill set is used in this project. It does not set goals, record business context, or define business terms; strategy owns those. Setup does not replace existing instrumentation.

## Discover before asking

Read project instructions or the customer-supplied entry document. Follow an existing resource index, including remote links through available connectors or browser access. Look for existing setup preferences, tools records, tracking plans, task conventions, and prior evidence. Note any business context, glossary, or strategy you find so the index can link them, but leave their content to strategy. Resolve relative paths from the containing document, never from this installed skill folder.

Inspect the actual repositories, entry points, SDK initialization, event owners, routing, consent handling, and backend outcomes relevant to the request. Include native codebases when applicable. Distinguish confirmed facts, observations, proposals, and unknowns.

If records compete for ownership, surface the ambiguity. An inaccessible linked record is an access gap, not permission to replace it with guessed contents.

## Gather the needed setup choices

Show a short sourced summary for correction. Ask at most three unresolved questions per round, prioritizing what the next useful task needs. Allow "not sure" and explicit deferral. Do not require a complete setup record before useful work or force a first event for a strategy or analysis request.

Cover these areas as relevant:

- **Platforms and applications:** repositories, platforms, environments, URLs, native bundle or package identifiers, and current implementation.
- **Tools:** actual and desired sources, analytics, advertising, CRM, experiments, routing or tag tools, warehouses, and consent systems. Record roles, not a fixed provider list.
- **Work locations:** documents, tasks, code or queries, and evidence. Ask for the exact document space, folder, or parent and the task team, project, or board, not only tool names. Discover existing templates, task states, and conventions.
- **Permission defaults:** what the assistant may do without asking in this project: save records, edit code, create or update tracker tasks, and change tool configuration in test environments. Record Allowed, Ask, or Not allowed for each. Production publishing, live account changes, messages to customers, and paid actions always need confirmation for each action; setup cannot pre-authorize them.
- **Workflows in play:** which parts of the skill set this project uses, for example planning only, planning and implementation, or the full implement, verify, and maintain loop. Strategy routes only to workflows in play.
- **Tracking conventions:** event naming and casing, identity, consent, sensitive-field exclusions, timezone, currency, and existing release rules.

For local records, propose an existing suitable folder or analytics/ and confirm it. For external records, use the selected native pages and tracker. Keep a discoverable entry pointer, not duplicate local copies of remotely owned documents. If no preference exists, propose a simple arrangement suited to available tools and record the customer's choice. Where the customer has no view on a permission or workflow, record the defaults from the workspace format and say so.

For tracking, identify the routing owner: browser or server tag manager, CDP, direct SDKs, or combinations. Reuse one canonical emission path and inspect legitimate client-capability exceptions. Offer Object–Action names with independent event and property casing choices; preserve existing contracts and provider-reserved names.

## Verify relevant access

For tools needed now, inspect installed versions and current official documentation for identifiers, regions, credential scopes, supported operations, and verification. Offer available connectors, APIs, or browser assistance; let the customer handle login and MFA. Store private credentials in their secure store or ignored configuration, with references only in project records. Native bundles are also client-distributed code.

Distinguish observed read access, write access, and untested capabilities. A visible page does not prove permission to create a child; a token's presence does not prove access. Record checks with account, environment, and date. Do not request credentials for deferred tools.

If a selected document system or tracker is inaccessible, name the gap and offer an accessible draft or user-assisted transfer. Agree any alternate authoritative location; never claim a local draft was published remotely. Continue independent work.

## Save the setup record and index

Extend existing setup and tools records in place. Save work locations with exact destination IDs, permission defaults, workflows in play, conventions, and open choices. The index links each record by purpose and actual path, URL, or ID, including business context, glossary, and strategy records that exist; it does not copy their contents.

Add or update a concise pointer in the instructions the customer's assistant reads, preserving existing imports and surrounding content. If several instruction files need pointers, point them to the same index. In a document-only session, use the accessible entry page. Instruct every skill to read the index, setup record, business context, and glossary first, then save outputs at the recorded locations.

Verify created or updated records by reading them back when possible. If a write succeeds but readback is unavailable, keep the returned ID and report the gap; check for an existing record before retrying creation. Verify that links resolve to intended records and update known inbound references when moving them.

Reruns preserve customer edits, stable IDs, existing choices, and unrelated tools. Record changed preferences in the setup record, inspect affected routes and consumers, and identify required implementation and verification. Never put customer configuration inside installed skill folders.

## Return a usable handover

Return the index link, saved setup and tools records, observed access, unresolved choices, and one next action. When no goal has been recorded yet, the next action is usually strategy. Update the progress section in the resource index or its linked progress record. Link completed work and blockers rather than duplicating results. Distinguish saved records from proposals.

A usable setup record can have a blocked tool; do not declare every account ready. Future skills and assistants re-read the same index. Setup installs no synchronization, scheduler, or background monitor.
