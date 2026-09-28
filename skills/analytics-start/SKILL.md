---
name: analytics-start
description: Start or resume analytics and measurement work when the customer wants help choosing the next step. Inspect existing project progress and guide them to setup, requirements, implementation, verification, or maintenance without repeating completed work.
license: MIT
---

# Start or resume measurement

Give the customer one starting point. Follow their requested outcome and existing scope; do not turn a specific fix or verification request into a full onboarding exercise.

## Establish where the work stands

Read project instructions and any analytics-workspace pointer. Inspect the workspace README progress, linked preferences, requirements, event contracts, and latest relevant evidence. Check the relevant actual code or configuration before trusting a saved completion claim. If there is no workspace, discover existing instrumentation and ask where to save the work; suggest a suitable existing folder or `analytics/`.

Summarize what is known, what is unresolved, and the next useful action. Ask only about a decision that affects that action. If sources conflict, identify the conflict instead of silently overwriting customer choices. Do not ask the customer to pick a skill name.

## Choose and do the next step

Use the host's available-skill list or discovery mechanism to find the relevant workflow. Read its instructions when available and continue within the same session and authorization; do not merely tell the customer to type another command. Only read the workflow needed now.

| Current need | Workflow if installed | Work to carry out |
| --- | --- | --- |
| Missing project preferences or a changed tool | `analytics-setup` | Discover existing SDK/routing; ask only unresolved platform, tool, naming, identity, consent, and environment decisions needed for the selected journey; save preferences and credential references |
| Business outcome or event meaning unclear | `analytics-requirements` | Start with the customer's decision; refine success, exclusions, identity, and acceptance criteria in rounds of three questions; save Proposed versus Agreed requirements |
| Agreed contract needs real code | `analytics-implement` | Trace the actual trigger owner and current SDK docs; implement one canonical emission through the existing routing owner, then test the affected path |
| Tracking exists but correctness or receipt is uncertain | `analytics-verify` | Exercise the actual web/native journey and inspect each final destination through its API or interface; preserve Pass, Fail, Blocked, and Not run evidence |
| Feature or tool changed; measurement may have drifted | `analytics-maintain` | Compare changed behavior with the existing plan, update authorized affected work, and reverify it |

An unavailable specialist skill is not a dead end. Perform the bounded step using this table and the customer's existing records; use current official platform/tool documentation for exact APIs. Keep one canonical binding per defined trigger, follow agreed naming/identity/consent, keep private tokens out of client bundles and tracked records, and verify actual destination receipt. If records are absent, create only those needed now with stable IDs, exact definitions, open questions, and real evidence links. Do not invent an SDK, approval, code binding, or passing result. Mention the optional specialist only when it would help; do not install it without authorization.

## Aim for one useful result

For new measurement work without a specified scope, propose one business question, one meaningful event, and the destinations needed to answer it. Agree that first milestone, including its success and negative cases. Reuse existing tracking when suitable. Defer optional tools only with the customer's agreement; a required destination cannot be silently dropped to claim success.

Continue through ready steps while authorized. An interview request ends with requirements; it does not authorize implementation. A request to implement and verify can proceed when definitions and access are ready. A milestone is verified only when its agreed cases, including each selected destination's receipt, pass with attributable evidence. HTTP acceptance or a local log alone is insufficient. Missing browser/device/account access becomes an explicit blocker with a concrete next action. No background service is part of this workflow.

## Preserve the handover

Update one `## Progress` section in the customer workspace README as decisions or milestones change and before yielding. Use the customer's equivalent section if one exists. Record the updated time, current scope/stage, completed work with links, open decisions, blockers and who can resolve them when known, and one next action. Link authoritative preferences, contracts, and verification reports instead of copying them. Never store secrets or infer completion from a stage label.

On resume, reconcile that summary with its linked records and current code. Continue from the first unresolved dependency for the requested work without repeating answered questions. Return the workspace path, what changed, and the next action. If no workspace can be written, provide an explicit handover in the response and identify the missing file access.
