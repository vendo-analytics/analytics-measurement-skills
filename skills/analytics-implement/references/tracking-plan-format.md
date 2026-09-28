# Tracking plan format

Maintain `tracking-plan.md` in the customer's analytics workspace, or extend an equivalent existing record. Use a short index and detailed sections, with stable headings such as `## EVT-001`. Link requirements by ID. Keep the business contract separate from implementation and verification status.

## Event contract

Record name, description/meaning, requirement, precise firing condition, conditions where it must not fire, authoritative emission owner, required identities, consent/data restrictions, and route IDs from the tools document. Use `Draft`, `Agreed`, or `Deprecated` for the contract state. Preserve the evidence of agreement; do not invent it.

Use a property table with name, type, required/optional, meaning/allowed values, and source when needed. State timestamp, currency/unit, enum, and missing-value semantics where relevant. Never send the literal strings `undefined` or `null` in place of absent values. Legitimate nulls must follow the actual contract.

Keep persistent user and account/group traits in distinct sections. Share a property definition only when it has the same semantics. If a dictionary becomes large, move it into a linked file rather than maintaining two copies.

## Bindings and routes

For each applicable codebase, record the real emission owner, module/function reference, environment, and `Planned`, `Implemented`, or `Blocked` state. One shared event can have several platform bindings without duplicating its business definition. Explain client/server correlation or deduplication when both participate.

Reference routes defined in the tools document. Record actual destination name/property transformations and reserved-name exceptions per route. Do not assert all tools accept the same event envelope. Include a labeled synthetic payload only when it clarifies a non-obvious shape.

## Test cases and change history

Give each case a stable ID, event/route references, steps, inputs, expected values, and a pass/fail assertion. Cover relevant positive, negative, property, identity, consent, initialization, duplicate-emission, and final-receipt behavior. Record an observation window for absence/delay assertions.

Link verification evidence by run. A binding being Implemented is not evidence of receipt. Keep old run evidence intact when definitions change. Material renames, deprecations, or route changes identify affected consumers and link the agreed decision.
