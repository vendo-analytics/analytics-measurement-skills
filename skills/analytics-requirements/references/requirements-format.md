# Requirements document

Write `requirements.md` in the chosen analytics workspace. Preserve an established equivalent format if it contains the needed information.

Begin with an H1 title, the business context in plain language, and an index with ID, name, and status. Use `Proposed`, `Agreed`, and `Deferred` to describe the decision state. Add short file metadata such as `type` and `updated` when useful.

Each record uses a stable heading, for example `## REQ-001`, with the human-readable name underneath. This keeps links stable when wording changes.

| Field | What to record |
| --- | --- |
| Name | The customer's business question or outcome |
| Description | What they want to understand and why |
| Decision | What action the answer will inform |
| Potential measurement | Existing data or proposed events, traits, and derived measures |
| Success definition | Unit of analysis, boundaries, population, exclusions, and time window |
| Data needs | Required identities, properties, dimensions, latency, and relevant tools |
| Acceptance criteria | Specific pass/fail conditions for answering the question |
| Tracking references | Links to actual event IDs when they exist |
| Open questions | What remains unknown, who can resolve it, and why it matters |
| Status | Proposed, Agreed, or Deferred, with evidence of agreement when available |

Use a few paragraphs or labeled bullets for detailed records; do not cram these fields into one wide spreadsheet-like table.

Example reasoning, not a customer default: “First-project activation” requires deciding which accounts qualify, whether imported projects count, and the activation window. A confirmed project-creation event may be part of the solution. A button click alone cannot establish that a project exists. Do not create fake IDs, links to missing event records, or approval dates to make the document appear complete.
