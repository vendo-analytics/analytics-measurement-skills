# Real-workflow evaluation

Run these in an isolated application checkout with an installed skill and authorized test accounts. Capture host/model, skill commit, initial files, conversation, resulting diff, and evidence. Judge outcomes, not exact wording. These cases are a test protocol; their presence does not mean they have been executed.

| Case | Request and starting conditions | Observable acceptance |
| --- | --- | --- |
| Single entry point | Ask analytics-start for help in a project with existing instrumentation and missing receipt proof. | Agent chooses verification, reads that skill if installed, and continues without repeating setup or asking the customer to choose a command. |
| Starter alone | Install only analytics-start and ask to plan the first useful event. | Agent discovers actual context, starts the bounded requirement work, and records open decisions without pretending other skills are installed or requiring their installation. |
| Minimal onboarding | Existing SDK and naming are visible in code; customer is unsure about a future CRM. | Agent summarizes discovered facts, asks at most three unresolved questions per round, and defers that optional destination by agreement while progressing the selected journey. |
| First milestone | Agree one event and two destinations; one receipt is unavailable. | Code completion and the passing destination are preserved, but the milestone remains unverified with a concrete blocker for the other destination; scope is not silently reduced. |
| Resume across assistants | Stop during requirements, edit one answer manually, and open the same workspace in another assistant. | Progress and linked records preserve the answer, the assistant resolves conflicts, and the next questions cover unresolved decisions rather than restarting onboarding. |
| Stale progress | README says verified, but the event contract or implementation changed after the evidence. | Agent notices the revision mismatch, preserves old evidence, and identifies re-verification instead of repeating the stale completion claim. |
| Claude app upload | Download one packaged skill ZIP and upload it through the account's skill interface. | Host accepts the archive, the named skill loads, and its local references remain accessible. A successful ZIP round-trip alone is not this test. |
| Initial setup | A working app already has an SDK and partial tracking notes. Ask to set up measurement. | Agent finds the real owner, asks for unresolved preferences and folder choice, saves references without secrets, and preserves existing instrumentation. |
| Setup rerun | Edit a saved preference manually, then ask to add a new tool. | Customer edits survive; account facts and affected routes update; installed skill files do not change; no duplicate send is added. |
| Requirements | Ask why trial accounts do not activate, with activation still ambiguous. | Agent begins with intent, asks three questions per round, discovers available code facts, and leaves unresolved definitions Proposed. |
| Implementation | Provide agreed completion semantics in a React or native application with repeated renders. | One real completion binding routes through the existing owner; failed attempts and rerenders do not become completions; focused tests and real interaction evidence identify actual limits. |
| Native coverage | Ask to track an iOS, Android, Flutter, or React Native journey. | Agent uses the actual platform's lifecycle and SDK contract; no web-only workaround or fictitious native API is presented as implemented. |
| Destination proof | The SDK emits and transport accepts, but destination access is missing. | Report preserves transport observations; final receipt is Blocked and never Pass. |
| Multiple routes | One final destination receives the event, another has a payload mismatch, a third cannot be read. | Results are separate: Pass, Fail, and Blocked with attributable evidence. |
| Maintenance | Change a business-success boundary and ask to check affected analytics. | Agent compares intent and actual code, resolves semantic changes, updates affected bindings and decisions, preserves old evidence, and does not start a monitor. |

For real provider verification, use that tool's current official documentation and selected test environment. Confirm receipt independently in its API or interface. A local fixture can evaluate decision-making, but cannot establish real destination delivery.
