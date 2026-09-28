---
name: analytics-requirements
description: Interview a customer about measurement outcomes and refine them into documented analytics requirements. Use before choosing events, planning instrumentation, or expanding an existing measurement plan.
license: MIT
---

# Refine measurement requirements

Follow the project's resource index and read its setup record, tools, business context, existing requirements, and relevant application behavior. If no index exists, ask where to save the work and capture the minimum needed context there; the setup and strategy skills are useful if installed, but are not dependencies.

## Use shared records

Resolve records through the customer resource index in project instructions or their entry document. Read the setup record (work locations, permission defaults, workflows in play, conventions), business context, and glossary even when invoked directly. Follow the permission defaults: the current request can authorize its own work unless the setup record marks it Not allowed, and production publishing, live account changes, messages to customers, and paid actions always need confirmation for each action. Local paths resolve from the containing document; remote records require available connector/browser access. Filenames below denote record roles, not a requirement to create local duplicates. Use the customer's canonical terms and surface conflicts before dependent work. When the customer resolves a term, update the authoritative glossary and inspect affected definitions rather than creating a second meaning.

Save outputs to the selected document/task/evidence homes. Preserve stable links and customer edits; update the index when records move. Read back writes when possible and retain real IDs/paths. Missing access or unavailable readback stays explicit; inspect for an existing record before retrying an ambiguous creation. Agree any fallback location instead of claiming an unpublished draft is remote. No customer record belongs in the installed skill folder.

## Start with intent

Ask one open question first: “What do you want to understand or improve, and what decision would you make from the answer?” Let the customer describe the outcome before suggesting events or tools. If they have already explained it, reflect it back and proceed rather than repeating the opening.

## Refine three questions at a time

Ask three focused questions per round, wait for the answers, then choose the next three from the remaining uncertainty. If fewer questions remain, ask only those. Do not dump the full interview at once. Offer a recommendation when it helps clarify a choice, label it as a proposal, and avoid treating silence as agreement.

Resolve dependencies in a useful order: business meaning and desired decision; actor and unit of analysis; start/success/failure boundaries; inclusion and exclusion rules; time window and latency; useful breakdowns; identity and available data; then how to collect and verify it. Explore the codebase for facts instead of asking questions it can answer.

Separate an outcome from an implementation hypothesis. “Understand why trials fail to activate” does not automatically mean tracking every click. Existing server records, CRM data, or an already-collected event may answer the question. Distinguish client attempts, completed business actions, persistent traits, and derived metrics.

Use concrete examples to expose ambiguity: whether an imported project counts as activation, whether a failed payment counts as a purchase, or whether a user or account is the conversion unit. Explain how the choice changes measurement.

## Maintain the requirements

For an instrumentation request without an existing scope, propose one business question and one useful event as the first milestone. For broader measurement or strategy work, use existing evidence where possible and choose the smallest useful measurement result; new events are not mandatory. Agree the selected destinations and positive/negative acceptance cases. Keep broader requirements visible and defer optional work only by agreement. This prioritizes delivery; it does not replace the customer's requested scope or prove that one event answers the entire business question.

Write agreed facts and open questions as the interview progresses using [requirements format](references/requirements-format.md). Preserve prior decisions and stable IDs. Keep hypotheses marked Proposed and scoped deferrals marked Deferred. Link existing tracking definitions rather than copying them.

For each requirement, establish its name, description, desired decision, potential measurement, measurable success definition, data/identity needs, acceptance criteria, and unresolved choices. Reuse the linked metric definitions or record the relevant formula, entity/grain, population/exclusions, time window, and sources there. Link glossary terms rather than redefine them; distinguish proposed baselines/targets from measured values. Include only relevant dimensions; don't make optional fields an endless questionnaire.

## Completion

Present the complete requirements document for the customer's review. It is ready for implementation when in-scope definitions and blocking choices are agreed, each outcome has a feasible measurement approach and pass/fail criteria, and deferrals are explicit. Do not mark it Agreed because the interview ended or a file was written. Report unresolved items without inventing answers. Implementation, live account changes, and background monitoring are not part of this interview.

As answers are saved and before yielding, update one `## Progress` section in the resource index or its linked progress record: time, scope/stage, completed work with links, open decisions, blockers with concrete next actions, and one recommended next step. Preserve existing content and link the authoritative records. On resume, check those records and continue unresolved questions instead of repeating the interview.
