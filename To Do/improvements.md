# Improvement candidates

Status: Ideas for evaluation, not approved scope or instructions to installed skills.

Use evidence from the first real skill runs to decide which of these are worth building. Keep V1's generalized tool workflow and no-background-service boundary intact.

| Candidate | Problem to validate | Possible outcome | Evidence before pickup |
| --- | --- | --- | --- |
| Static HTML handover | Some customers may find long Markdown reports difficult to navigate | An optional generated view of the same records, with no second editable plan or hosted service | Review the actual Markdown artifacts with customers first |
| Large-plan navigation | Requirements and event definitions may outgrow a few documents | Split records into linked files while preserving stable IDs and a useful index | A real plan where navigation or agent retrieval becomes difficult |
| Portable evidence capture | Agent hosts expose different browser, device, and file capabilities | Small reusable helpers for repeated capture or redaction work | Demonstrated repeated failures or manual work across real verification runs |
| Cross-agent regression cases | Skill revisions may behave differently in different hosts | Repeatable evaluations of onboarding, configuration updates, and honest verification outcomes | An initial working workflow and observed regressions worth retaining |
| Workspace format upgrades | Future format changes could overwrite customer choices or break record links | Explicit, reviewable migrations that preserve customer edits | A real format change requiring migration, not a speculative versioning framework |

These candidates do not add prompts, upsells, provider-specific recipes, or background jobs to the skills. Create implementation tasks only after the problem and desired outcome are agreed.
