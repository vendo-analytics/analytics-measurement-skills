# Strategy record

Use the customer's selected document location and native format. The local default, only when local storage is chosen, is strategy.md linked from the existing resource index. Reuse a relevant strategy instead of creating another. Create records only when they contain useful information.

## Contents

1. **Goal and decision:** what to improve, for whom, and the decision this work supports.
2. **Current understanding:** sourced observations, customer-confirmed context, hypotheses, and evidence gaps.
3. **Success:** linked metric definitions, known baseline/target, timeframe, and guardrails. Unknown values stay unknown.
4. **Approach:** selected or proposed approach, why it fits, material alternatives, and unresolved choices.
5. **Work plan:** bounded work items, required capabilities, inputs, expected outputs, dependencies, and known owners.
6. **Delivery and evidence:** canonical task/specification/code/report/evaluation links, added as they exist.
7. **Progress:** completed work, blockers or pending observations, and the next decision/action. Reuse existing authoritative progress rather than duplicating it.

A short plan for one goal may fit in a few paragraphs and a work table. Do not force a long template or a whole-stack redesign for a narrow request.

## Reference ownership

The resource index links preferences, selected work locations, tools, glossary, current strategy, definitions, and evidence. Customer records can live in different systems; link them by actual paths/URLs/IDs. Local links resolve from the containing file, not this skill.

Use glossary terms consistently. Metrics own formulas/windows, event contracts own triggers/payloads, and the strategy owns the approach and priorities. Link those definitions rather than restating them. When a meaning is resolved, update its authoritative record and inspect affected consumers before changing existing terms.

## Work items and tasks

A work item records:
- The bounded question or change and its reason.
- Its required input and expected observable result.
- Relevant capability or actual selected skill, dependencies, and owner when known.
- Proposed/agreed/deferred status, actual delivery state, and links to evidence.

Use the customer's tracker states when creating authorized tasks. Search for existing related tasks first; a work-plan row is not itself proof that a tracker task exists. Include acceptance criteria and a link to the plan, rather than copying the full strategy.

Implementation, verification, and outcome evaluation remain distinct. A shipped intervention can await observations. An analysis can be complete and inconclusive.

## Illustrative example

For “improve account retention,” a possible first work item is:

> Determine which account cohorts have lower retention. Input: an agreed account-retention definition and usable activity data. Output: reproducible cohort analysis with limitations. Capability: analysis. Status: Proposed until the needed source and scope are established.

This example provides neither a real baseline nor a causal explanation. If source records are unreliable, the next work changes to understanding/repairing that gap.

## Updating and saving

Preserve customer edits and stable references. Record important changes of approach with date, evidence, and reason; link superseded choices. Do not treat document creation as customer approval.

After writing, retain the returned ID/path and read back important fields when possible. If the result is ambiguous, check for an existing record before creating another. Verify index/task links point to the intended strategy. If remote access is missing, label an accessible draft as unpublished and retain the missing prerequisite.

The final handover names the saved strategy, substantive changes, evidence and limitations, and one next action. It must work without the earlier chat transcript.

