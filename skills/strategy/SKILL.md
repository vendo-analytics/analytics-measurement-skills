---
name: strategy
description: Start or resume strategy, analytics, and measurement work. Turn what the customer wants to get out of the work into documented outcomes, success measures, and a plan, then carry out the next useful step through diagnosis, requirements, implementation, verification, maintenance, or outcome evaluation. Use for a business goal such as improving retention, a general request such as help with analytics or what to do next, or resuming earlier work. Specific setup, requirements, implementation, verification, or maintenance requests can go straight to that work without a strategy interview.
license: MIT
---

# Strategy

Strategy owns what the customer wants to get out of this work: the business context, the glossary, goals and outcomes, success measures, the approach, and the work plan. It is also the single entry point. It finds where the work stands and continues with the next useful step in the same conversation, so the customer never needs to learn skill names.

Setup owns how the skill set is used in this project: tools, platforms and applications, work locations, permission defaults, workflows in play, and tracking conventions. Strategy reads those records and does not ask those questions again.

A specific request, such as implementing an agreed event or verifying a destination, proceeds directly at the appropriate depth without a strategy interview.

## Find where the work stands

Follow the project instructions or the customer's entry document to the resource index. Read the setup record, relevant tools, business context, glossary, existing strategy, definitions, decisions, the progress section, and recent evidence. Resolve relative links from the document that contains them; use available connectors or browser access for remote records. Missing access is not proof that a record does not exist.

If there is no resource index, or the setup record lacks something the next step needs, use analytics-setup when it is installed for only the missing items, then continue here. When analytics-setup is not installed, ask where to save the strategy, record that location in a small resource index, and list the other setup items as open. Do not collect tool, platform, or convention details beyond what the next step strictly needs.

Check the relevant code or configuration before trusting a saved completion claim. Summarize what is known, what is unresolved, and the next useful action. If sources conflict, identify the conflict instead of silently overwriting a customer choice.

## Record the business context and glossary

Keep one business context record for the project and reuse it across goals: what the product does, who it serves (end customers, users, accounts, and how they relate), main journeys, known business owners, and constraints. Read existing product documents and the code before asking, then show a short sourced summary for correction. Record only what the current goal needs; do not run a full company interview.

Reuse the existing glossary, such as CONTEXT.md, when there is one. Record a term when its meaning is resolved. Distinguish observed facts, customer statements, hypotheses, and unknowns. Surface conflicting definitions before dependent work; do not infer business meaning from field names. The [strategy record](references/strategy-format.md) describes both records.

## Understand the goal

Start with what the customer wants to improve and the decision the work should support. Reflect answers already given instead of repeating the opening. Inspect documents, code, available data, and tool capabilities for facts before asking questions.

Ask no more than three unresolved questions per round. Resolve the next material uncertainty: the entity or segment in scope, desired behavior or outcome, current problem, constraints, success definition, timeframe, or evidence. Do not demand a complete business canvas or automatically recommend new tools or events.

For "improve retention", establish what the retained entity and return behavior mean, the cohort and window, and whether usable evidence already exists. Do not invent a baseline, target, cause, or intervention. Technical setup completion and customer value can be different milestones.

## Write the strategy as it develops

Use the [strategy record](references/strategy-format.md) to create or update the plan in the recorded document location. Capture the goal and decision, current evidence, success measures, approach and rationale, bounded work, dependencies, and open choices. Link definitions and specialist findings rather than duplicate them.

Keep proposed and agreed choices distinct. The next milestone should produce useful evidence or a working outcome for this goal; it need not be a new event.

## Choose and do the next step

Use the host's actual skill list or discovery and read only the workflow needed now. Select by capability, inputs, tool access, and scope, not merely by name. Route only to workflows that the setup record lists as in play; when none are recorded, every installed workflow is in play. If the next useful step falls outside them, say so and ask whether to widen the scope. Explain the next action briefly and continue in the same conversation instead of telling the customer to type another command.

| Need now | Workflow if installed | Work to carry out, with or without the workflow |
| --- | --- | --- |
| A tool, platform, work location, permission, or convention is missing or changed | analytics-setup | Ask only the unresolved setup items needed for this step and save them in the setup record |
| Metric or event meaning is unclear, or there is no evidence plan | analytics-requirements | Start from the decision; refine success, exclusions, identity, and acceptance criteria three questions at a time; save Proposed versus Agreed requirements |
| An agreed contract needs real code | analytics-implement | Trace the actual trigger owner and current SDK documentation; emit once through the existing routing owner; test the affected path |
| Tracking exists but correctness or receipt is uncertain | analytics-verify | Exercise the real web or native journey; check each final destination through its API or interface; record Pass, Fail, Blocked, or Not run |
| A feature or tool changed and measurement may have drifted | analytics-maintain | Compare the change with the plan, update affected records and code within permission, and verify again |
| The journey or end-customer motivation is uncertain | Research or product capability, or a bounded investigation | Observations and hypotheses kept distinct |
| A business pattern needs explaining from available data | Analysis capability | Reproducible findings, data fitness, competing explanations, and limits |
| Sources need joining, transformation, or modeling | Data or engineering capability | Agreed flow and working, permitted changes with validation |
| A recurring decision needs a report | Reporting capability | A working, source-backed report that uses shared definitions |
| Evidence supports a possible intervention | Product, experiment, or coding capability | Change specification and evaluation method; implementation within permission |
| An intervention has enough observations | Evaluation or analysis capability | Results, uncertainty, guardrails, and the next decision |

The capability rows are not promises that extra skills are installed. An unavailable workflow is not a dead end: perform the bounded step from this table when available tools and evidence can meet its requirements, using current official documentation for exact APIs. Otherwise return the precise missing input or capability. Do not fabricate an invocation, SDK, approval, code binding, or passing result, and do not install a skill without permission.

For new measurement work without a specified scope, propose one business question, one meaningful event, and the destinations needed to answer it. Agree that first milestone, including its positive and negative cases. Reuse existing tracking when suitable. A required destination cannot be silently dropped to claim success; defer optional tools only by agreement.

For analysis, inspect definitions, coverage, grain, duplicates, joins, and time windows before drawing conclusions. Preserve reproducible queries or calculations and source references. Association can suggest a hypothesis but does not establish causality. Use research when behavioral data cannot explain why.

For implementation, inspect the real owner and consumers, agree material semantics, and complete the permitted path with focused checks. For tracking, keep one binding per defined business trigger, reuse routing, keep private credentials out of clients, and verify each final destination. Do not create a service, connector framework, or SDK to bypass a missing capability.

For interventions, specify the change, target population, hypothesis, success measure, guardrails, and a feasible evaluation method before assessing results. Do not impose an experiment on every bug fix. Planning is not launching.

## Act within permission

Follow the permission defaults in the setup record. The customer's current request can authorize its own work unless the setup record marks that action as not allowed. A planning or interview request ends with the plan; it does not authorize implementation. Production publishing, live account changes, messages to customers, and paid actions always need the customer's confirmation for that action. Moving between workflows keeps the same scope and permission.

## Inspect results and close the loop

Pass a workflow the goal, bounded task, relevant canonical links, scope and permission, and expected evidence. Inspect its result, source revision, limits, and next action before using it. A completed document is not proof that the described system works.

Separate implementation success, trustworthy measurement, and business impact. Evaluate against agreed definitions, exposure, observation window, baseline or comparison, and guardrails. Record uncertainty and plausible alternative explanations. If observations are insufficient, save the pending evidence need and resume when invoked later; do not claim impact or start a monitor.

Update the strategy when evidence changes the approach. Create or update tracker tasks only within permission; use the recorded project and conventions, search for existing work first, link the strategy, and include observable acceptance criteria.

## Save and hand back

Save results to the recorded locations and keep real IDs and paths. Read back writes and check links when possible. Report unavailable readback or partial writes, and look for an existing record before retrying a creation. If the recorded location is inaccessible, agree a fallback or return an explicitly unpublished draft.

Keep one progress section in the resource index or its linked progress record: updated time, goal and scope, completed work with links, open decisions, blockers and who can resolve them, and one next action. Link authoritative records instead of copying them. Never store secrets or infer completion from a stage label.

On resume, reconcile progress with current records, code, and customer edits, then continue from the first unresolved dependency without repeating answered questions. Return the strategy link, what changed, and the next action. If nothing can be written, give an explicit handover in the response and name the missing access.
