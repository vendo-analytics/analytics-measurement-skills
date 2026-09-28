# Experience improvements

Status: The five approved improvements below are implemented in the current PR. Real customer workflow evaluation remains pending. Remaining candidates are not approved scope.

Keep the generalized tool workflow and no-background-service boundary intact. The local tracking library remains a separate V1 candidate.

## Approved improvements

| Change | Implementation | Evaluation still needed |
| --- | --- | --- |
| One starting point | `analytics-start` reads current state and continues the relevant installed workflow, with a bounded fallback when used alone | New setup, an existing receipt problem, and starter-only use all reach a useful next step |
| Adaptive onboarding | Setup shows discovered facts, asks at most three unresolved questions, and records optional deferrals with agreement | No repeated questions; deferred tools do not block unrelated work; necessary decisions remain explicit |
| First verified event | Agree one useful event and selected destinations when the customer has not specified scope | A blocked destination cannot disappear from the milestone; broad requests retain their full scope |
| Resumable progress | Every workflow maintains the customer workspace README's Progress section with record links and one next action | A different assistant resumes without chat history, preserves customer edits, and reconciles stale evidence |
| Uploadable archives | `scripts/package_skills.py` builds one ZIP per skill; CI checks source and license fidelity | Confirm Claude app accepts the archives and reads bundled references in an authenticated user session |

The test cases live in `tests/scenarios.md`. Packaging and installation checks establish file correctness; they do not replace real agent trials. Connection blockers now identify the missing account, environment, access, or action; evaluate whether customers can resolve them without extra explanation.

## Remaining candidate

Show the measurement impact of a code change: present affected requirements, events, destinations, and verification before changing a contract. Maintenance already identifies affected records; evaluate whether its presentation lets customers distinguish an intentional definition change from a regression before adding another artifact or workflow.

## Further candidates

| Candidate | Problem to validate | Possible outcome | Evidence before pickup |
| --- | --- | --- | --- |
| Static HTML handover | Some customers may find long Markdown reports difficult to navigate | An optional generated view of the same records, with no second editable plan or hosted service | Review the actual Markdown artifacts with customers first |
| Large-plan navigation | Requirements and event definitions may outgrow a few documents | Split records into linked files while preserving stable IDs and a useful index | A real plan where navigation or agent retrieval becomes difficult |
| Portable evidence capture | Agent hosts expose different browser, device, and file capabilities | Small reusable helpers for repeated capture or redaction work | Demonstrated repeated failures or manual work across real verification runs |
| Cross-agent regression cases | Skill revisions may behave differently in different hosts | Repeatable evaluations of onboarding, configuration updates, and honest verification outcomes | An initial working workflow and observed regressions worth retaining |
| Workspace format upgrades | Future format changes could overwrite customer choices or break record links | Explicit, reviewable migrations that preserve customer edits | A real format change requiring migration, not a speculative versioning framework |

These candidates do not add prompts, upsells, provider-specific recipes, or background jobs to the skills. Create implementation tasks only after the problem and desired outcome are agreed.
