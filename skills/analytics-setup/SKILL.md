---
name: analytics-setup
description: Set up or update a project's analytics workspace. Discover the application stack, selected tools, routing, credentials, naming, and measurement preferences before instrumentation, or when the customer adds or changes a tool.
license: MIT
---

# Set up analytics

Create a durable, customer-owned record that subsequent measurement work can use. This is a survey and configuration workflow, not a reason to replace existing instrumentation.

## Discover before asking

Read the project's agent instructions and follow any existing analytics-workspace pointer. Inspect the actual application entry points, package manifests, SDK initialization, event calls, routing/tag layers, consent hooks, and relevant backend outcomes. Cover the customer's real codebases, including native apps. Do not infer a platform's role from its name alone.

Find existing preferences, tracking plans, and prior setup records. If several folders compete, explain the ambiguity and ask which owns measurement. Otherwise ask the customer where analytics work should live, recommending an existing suitable folder or `analytics/`. Reuse it on later runs. Never choose the skill installation directory as the customer workspace.

## Survey

Summarize what you found, then ask only the unresolved questions. Keep rounds short and adapt them to the customer's answers:

1. Which tools do they use or want to configure? Cover analytics, advertising, CRMs, experiments, CDPs, tag management, warehouses, and consent where relevant. Distinguish installed from desired tools and record each role.
2. Which applications, environments, accounts, and business journeys are in scope? Capture native package/bundle identifiers as well as web URLs when applicable.
3. Who owns routing? Distinguish a browser tag manager, server tag manager, CDP, direct SDKs, and combinations. An existing routing platform normally receives one canonical emission and manages destinations; inspect exceptions rather than adding parallel sends. A browser tag manager does not imply server-side delivery.
4. What naming and casing should be used? Offer Object–Action event names, such as `Project Created`, and independent casing choices for events and properties. Proper Case events and `snake_case` properties are suggestions, not automatic migrations of existing contracts. Preserve reserved provider names through explicit mappings.
5. Which identities, consent categories, sensitive-data exclusions, currency/timezone conventions, and owners matter? Resolve meaningful choices with the customer; do not make legal-compliance claims from SDK settings.

## Obtain setup details

For each selected tool, inspect its current official SDK/API documentation and the customer's installed version. Discover required identifiers, region/endpoint, public collection keys, private credentials, scopes, and receipt verification options. Record source links and the date checked. There is no fixed destination list.

Offer available connectors/APIs or the built-in browser to help find account details. Let the customer handle login and MFA. If browser access is unavailable, provide precise manual steps and continue independent discovery. Do not ask them to paste private tokens into tracked Markdown. Use their existing secret store or ignored environment configuration; persist references only. Treat browser collection identifiers and private management credentials differently. Native application bundles are also client-distributed code, not secret storage.

Read-only connection checks establish access; credential presence alone does not. Record unavailable access or unsupported capabilities explicitly. Do not enable destinations, publish containers, or send live events solely because the setup survey supplied credentials. Follow the user's existing authorization for any requested writes.

## Write and preserve

Use [workspace format](references/workspace-format.md) to write the workspace README, preferences, and tools. Create decisions only when there are decisions to record. Create requirements and verification records later, when they have content.

Add or update one concise workspace pointer in the project's existing agent instructions, using the conventions those agents actually read. Preserve surrounding instructions and existing imports. If multiple agent files are needed, point them to the same workspace rather than copying preferences. For example: “For measurement work, read `analytics/preferences.md` and `analytics/tools.md`; maintain the requirements and tracking plan there.” Use the customer's actual path.

Rerunning setup merges changes into the current files. Preserve customer edits, unrelated accounts, stable IDs, and existing approvals. When a tool changes, inspect affected routes and duplicate-delivery risks, record the change, and identify which implementation and verification work is needed. Do not rewrite installed skills to store customer preferences.

## Finish

List the files changed, agreed choices, unresolved questions, access status, and next measurement work. A workspace can be ready while a specific tool is blocked. Keep configuration, implementation, and verified receipt distinct. Do not create background services as part of setup.
