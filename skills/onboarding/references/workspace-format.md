# Onboarding workspace records

Use the customer's existing documents and native formats. Onboarding coordinates a broader growth setup; it does not replace the owning workflows or require a fixed set of new files.

## Record ownership

| Record | Owner and onboarding behavior |
| --- | --- |
| Resource index and progress | Reuse the setup convention. Keep canonical links and one resumable progress summary. |
| Setup, preferences, and tools | Extend through analytics-setup when installed. Otherwise record only choices needed now and leave full setup open. |
| Business context and glossary | Extend through strategy when installed. Keep confirmed claims, research, inference, and unknowns distinct. |
| Strategy, goals, and initiatives | Use one existing or new strategy per coherent goal. Onboarding supplies discovery and priorities; it does not create a second plan. |
| Public research and competitor candidates | Reuse an existing research record. When local storage is selected and none exists, use `research.md` linked from the index. |
| Decisions and evidence | Link existing records; add only material onboarding decisions and source evidence. Never copy secrets into them. |

When setup is unavailable, a minimal local index may link setup notes, business context, research, strategy, decisions, and evidence that actually exist. A later setup or strategy workflow extends these records in place. Do not create empty files to fill the table.

## Provenance

Attach one state and its basis to every material claim, goal value, competitor relationship, and initiative assumption:

| State | Meaning | Required basis |
| --- | --- | --- |
| `customer_confirmed` | The customer explicitly confirmed this statement or value | Confirmation date and customer statement or record reference; retain underlying sources where relevant |
| `observed` | Directly inspected in an accessible project, account, document, data set, or tool | Actual path, URL, account-safe identifier, observation date, and relevant scope |
| `researched` | Supported by retrieved public material | Publisher, canonical URL, retrieval date, and the exact supported claim |
| `inferred` | A reasoned hypothesis not directly confirmed or observed | Supporting claim links, concise reasoning, and what would confirm or reject it |
| `unknown` | Missing, inaccessible, conflicting, or not yet established | What is missing and, when known, who or what can resolve it |

A source's confidence or promotional language does not change these states. Customer confirmation of a researched claim may change its state to `customer_confirmed`; preserve the original research source. Conflicting claims remain separate until resolved. Do not silently replace a customer edit with a newer search result.

Use stable claim or record IDs when the native format supports them. Otherwise use stable headings and links. Keep dates and source references next to the claims they support rather than maintaining an unconnected bibliography.

## Public research record

For each research topic, record:

1. **Question and scope:** the business, segment, market, or comparison being investigated.
2. **Claims:** concise findings with provenance and source links.
3. **Competitor candidates:** name, relationship or alternative type, relevant segment or customer job, evidence, candidate status, and unknowns.
4. **Source log:** publisher, canonical URL, publication date when known, retrieval date, and access or freshness limitations.
5. **Open questions:** contradictions, missing evidence, and claims needing customer confirmation.

Customer-named competitors can be `customer_confirmed`; research discoveries remain candidates even when several sources mention them. Separate direct competitors, indirect substitutes, and customer alternatives when that distinction matters. A blank comparison is preferable to guessed pricing, market share, features, or performance.

Cite the material actually retrieved. A search-result snippet is not equivalent to reading the linked page. Record inaccessible pages and stale sources as limitations rather than evidence for a stronger claim.

## Business context additions

Extend the established business context only with growth-relevant material:

- Offering, customer value, business model, and relevant market or category.
- End customers, users, accounts, segments, and their relationships.
- Acquisition, activation, retention, revenue, or referral journeys that matter to the requested goals.
- Known owners, constraints, and existing competitor or alternative understanding.
- Claim-level provenance and links to more detailed research.

Reuse the glossary for resolved category, customer, and journey terms. Surface conflicting meanings before goals or comparisons depend on them.

## Goals and measurement gaps

Each goal belongs in the strategy and includes:

- Desired outcome, target customer or segment, and the decision the goal supports.
- Baseline, target, unit, timeframe, owner, and guardrails; each value has provenance or remains `unknown`.
- Current evidence, source coverage, definition or identity gaps, and what measurement is needed.
- Agreed, proposed, or deferred status. Saving a goal does not imply agreement.

Do not convert relative ambitions into invented percentages or dates. If no baseline exists, propose a bounded measurement or research step rather than filling the gap.

## Tool and data options

Record the actual goal or question before evaluating a provider. For each feasible option note its role, available operation, account or environment, read/write verification, expected freshness, known cost or approval requirement, and gaps.

Possible routes include an existing connection, a customer-owned export, direct third-party access, public research, or a managed capability exposed by the current host. These are options, not claims that every route exists. Never mark a provider connected from a login page, installed package, or credential reference alone.

## Prioritized initiatives

Keep initiatives in the strategy work plan. Each contains:

| Field | Meaning |
| --- | --- |
| Outcome | The customer or business change sought, linked to a goal |
| Impact | Expected magnitude or qualitative significance, with rationale and uncertainty |
| Confidence | Strength of supporting evidence and major assumptions |
| Effort | Relative work and operational burden using the customer's convention |
| Dependencies | Evidence, access, decisions, capabilities, and owners required |
| Status | Proposed, agreed, deferred, or another existing native state |
| Delivery links | Actual tasks, implementation, reports, and evaluation when separately created |

Use scores only when the customer has a scoring convention and enough evidence. Otherwise use short qualitative assessments. A priority is a recommendation until agreed. A work-plan row is not a tracker task.

## Progress and resume checks

The single progress entry contains the update time, onboarding scope, completed record links, unresolved choices, source or access blockers and owners, and one next action. Link details instead of copying them.

Before resuming, verify:

1. Existing canonical records and stable IDs are reused.
2. Customer edits and unrelated content survive unchanged.
3. Confirmed answers are not asked again unless evidence conflicts.
4. Proposed and inferred claims remain distinct from confirmed facts.
5. Unknown numbers and inaccessible capabilities remain explicit.
6. No duplicate record, tracker task, schedule, external message, or paid action was created.
7. Important writes were read back, or the readback limitation is recorded.

On handback, name saved records, substantive changes, unresolved gaps, and one next action. The saved records and handback must be usable without the earlier chat transcript.
