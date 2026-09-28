# Improvement candidates

Status: Ideas for evaluation, not approved scope or instructions to installed skills.

Use evidence from the first real skill runs to decide which of these are worth building. Keep V1's generalized tool workflow and no-background-service boundary intact.

## First improvements to evaluate

The main usability risk is making customers learn our five-skill structure before achieving one useful result. Prioritize time to the first verified event and continuity between sessions. The README now provides assistant-specific installation, a first-journey guide, and a resume prompt. The following changes to skill behavior remain proposals.

| Priority | Task | Customer experience | Observable acceptance |
| --- | --- | --- | --- |
| 1 | Provide one entry point that chooses the next workflow | “Help me with analytics” discovers the current state and recommends setup, requirements, implementation, verification, or maintenance | A new project starts with setup; an instrumented project with a receipt problem goes to verification; installing a single skill does not create a missing-skill dead end |
| 1 | Shorten onboarding to the decisions needed now | Show discovered facts for correction, recommend defaults with reasons, and allow “not sure” or a deferred destination | No questions repeat facts already verified in code or saved preferences; deferred optional tools do not block the first useful event |
| 1 | Make one verified event the initial milestone | Guide a customer from one business question to a precise trigger and destination evidence before expanding the plan | The customer can explain what the event means, where it fires, and which destinations actually received it; pending evidence remains visible |
| 1 | Add a resumable progress summary to the existing workspace README | Show completed work, open decisions, blocked access, and one recommended next action | A new chat or different assistant continues from the same files without rerunning the survey; the summary links to authoritative records rather than copying them |
| 2 | Make connection blockers actionable | Explain which account, environment, permission, or manual action is missing and offer browser-assisted setup when available | A customer can resolve the stated blocker without guessing which credential to supply; private tokens never enter the plan |
| 2 | Show the measurement impact of a code change | Present affected requirements, events, destinations, and verification work before changing a contract | The customer can distinguish an intentional definition change from a regression; unrelated events and previous evidence stay intact |
| 2 | Offer ready-to-upload skill archives | Claude app users download one complete skill ZIP instead of manually packaging folders | Each generated archive contains exactly one skill and its references, matches the source revision, and excludes maintainer planning and marketing |

Recommended sequence: test the new README with one new customer, observe their first setup/requirements session, then choose the smallest behavior change that removes an observed obstacle. An entry point should coordinate the existing workflows rather than duplicate their instructions.

## Further candidates

| Candidate | Problem to validate | Possible outcome | Evidence before pickup |
| --- | --- | --- | --- |
| Static HTML handover | Some customers may find long Markdown reports difficult to navigate | An optional generated view of the same records, with no second editable plan or hosted service | Review the actual Markdown artifacts with customers first |
| Large-plan navigation | Requirements and event definitions may outgrow a few documents | Split records into linked files while preserving stable IDs and a useful index | A real plan where navigation or agent retrieval becomes difficult |
| Portable evidence capture | Agent hosts expose different browser, device, and file capabilities | Small reusable helpers for repeated capture or redaction work | Demonstrated repeated failures or manual work across real verification runs |
| Cross-agent regression cases | Skill revisions may behave differently in different hosts | Repeatable evaluations of onboarding, configuration updates, and honest verification outcomes | An initial working workflow and observed regressions worth retaining |
| Workspace format upgrades | Future format changes could overwrite customer choices or break record links | Explicit, reviewable migrations that preserve customer edits | A real format change requiring migration, not a speculative versioning framework |

These candidates do not add prompts, upsells, provider-specific recipes, or background jobs to the skills. Create implementation tasks only after the problem and desired outcome are agreed.
