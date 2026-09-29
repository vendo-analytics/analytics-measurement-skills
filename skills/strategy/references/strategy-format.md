# Strategy records

Strategy owns three records: the business context, the glossary, and one strategy per goal. Use the customer's recorded document location and native format. Local defaults, only when local storage is chosen, are business-context.md, the existing CONTEXT.md or glossary.md, and strategy.md, each linked from the resource index. Reuse existing equivalents instead of creating another. Create records only when they contain useful information.

Setup owns tools, platforms, work locations, permission defaults, workflows in play, and tracking conventions. Link to those records; do not copy them here.

## Business context

One record for the project, reused by every strategy:

- What the product does and how it creates value.
- Who it serves: end customers, users, and accounts, and how they relate.
- Main journeys, with links to where they are documented or implemented.
- Known business owners and constraints.
- Source links for each statement, and which statements the customer confirmed.

Goal-specific context, such as the segment in scope or the current problem, belongs in the strategy. Keep the record short; add detail when a goal needs it.

## Glossary

Reuse existing domain documentation. Define a term once when resolved: canonical name, definition, relationships, useful boundary examples, and avoided synonyms. Preserve disagreements separately; neither code nor a new suggestion automatically wins.

Metrics link to business terms while owning formulas and windows. Event and property definitions link to terms while owning trigger and payload semantics. Decisions record why a meaning changed. The glossary is not a strategy, schema dump, or implementation manual.

Any workflow that resolves a term with the customer updates the glossary. Before changing an existing term or ID, inspect affected requirements, metrics, properties, tasks, and code references. Preserve superseded meanings; do not silently rename consumers.

## Strategy contents

1. **Goal and decision:** what to improve, for whom, and the decision this work supports.
2. **Current understanding:** sourced observations, customer-confirmed context, hypotheses, and evidence gaps.
3. **Success:** linked metric definitions, known baseline and target, timeframe, and guardrails. Unknown values stay unknown.
4. **Approach:** selected or proposed approach, why it fits, material alternatives, and unresolved choices.
5. **Work plan:** bounded work items, required capabilities, inputs, expected outputs, dependencies, and known owners.
6. **Delivery and evidence:** canonical task, specification, code, report, and evaluation links, added as they exist.
7. **Status:** the state of each work item and any pending observations. Cross-workflow progress lives in the resource index's progress section; link to it rather than keep a second summary.

A short plan for one goal may fit in a few paragraphs and a work table. Do not force a long template or a whole-stack redesign for a narrow request.

## Reference ownership

The resource index links the setup record, tools, business context, glossary, strategies, definitions, and evidence. Customer records can live in different systems; link them by actual paths, URLs, or IDs. Local links resolve from the containing file, not this skill.

Use glossary terms consistently. Metrics own formulas and windows, event contracts own triggers and payloads, and the strategy owns the approach and priorities. Link those definitions rather than restating them.

## Work items and tasks

A work item records:
- The bounded question or change and its reason.
- Its required input and expected observable result.
- The relevant capability or actual selected workflow, dependencies, and owner when known.
- Proposed, agreed, or deferred status, actual delivery state, and links to evidence.

Use the customer's tracker states when creating permitted tasks. Search for existing related tasks first; a work-plan row is not proof that a tracker task exists. Include acceptance criteria and a link to the plan, rather than copying the full strategy.

Implementation, verification, and outcome evaluation remain distinct. A shipped intervention can await observations. An analysis can be complete and inconclusive.

## Illustrative example

For "improve account retention," a possible first work item is:

> Determine which account cohorts have lower retention. Input: an agreed account-retention definition and usable activity data. Output: reproducible cohort analysis with limitations. Capability: analysis. Status: Proposed until the needed source and scope are established.

This example provides neither a real baseline nor a causal explanation. If source records are unreliable, the next work changes to understanding or repairing that gap.

## Updating and saving

Preserve customer edits and stable references. Record important changes of approach with date, evidence, and reason; link superseded choices. Do not treat document creation as customer approval.

After writing, keep the returned ID or path and read back important fields when possible. If the result is ambiguous, check for an existing record before creating another. Verify that index and task links point to the intended record. If remote access is missing, label an accessible draft as unpublished and record the missing prerequisite.

The final handover names the saved strategy, substantive changes, evidence and limitations, and one next action. It must work without the earlier chat transcript.
