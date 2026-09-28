# Strategy and Measurement Skills

Give your agent one starting point for a business goal: understand the context, save a strategy, and choose the next useful work. Shared project records carry preferences, vocabulary, plans, and evidence between skills and assistants.

Seven portable skills: Strategy, the compatible analytics-start entry, and five focused measurement workflows for Codex, Claude Code, and other agents that support `SKILL.md`. Bring your own analytics, advertising, CRM, experimentation, CDP, and tag management tools. No Vendo account required.

## Choose your assistant

Open the **project you want to work on**, then install the skills there. Terminal commands below require Node.js/npm, which supplies `npx`. The skills themselves are Markdown; they do not require a Node.js application.

- [Codex](#codex)
- [Claude Code](#claude-code)
- [Claude app and Cowork](#claude-app-and-cowork)
- [Cursor, GitHub Copilot, Gemini CLI, and other coding assistants](#other-coding-assistants)
- [Manual installation or an assistant without skill discovery](#manual-installation-and-other-assistants)

Using both Codex and Claude Code? Install for both in one command:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a codex -a claude-code
```

For an unmerged review branch, run `npx skills add /path/to/skills-checkout --skill '*' -a codex -a claude-code` from your application project, pointing to a checkout of that branch. Repository-based commands below use the default branch.

### Codex

Run in your application's repository:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a codex
```

Open that project in Codex and send:

```text
$strategy Help me improve onboarding for this application.
```

Project skills are stored in `.agents/skills/`. If a skill is missing, start a new session in that project and check the installed files. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) and [project customization](https://learn.chatgpt.com/docs/customization/overview#skills).

### Claude Code

Run in your application's repository:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a claude-code
```

Open Claude Code in the same project and send:

```text
/strategy Help me improve onboarding for this application.
```

Claude Code reads `.claude/skills/`. The installer may link those folders to shared copies in `.agents/skills/`; keep the targets with your project. See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

### Claude app and Cowork

Local Claude Code installation does not install skills into your Claude account. For the app's custom-skill upload:

1. Open a ZIP link below, then click GitHub's **Download raw file** button (download icon). Each ZIP contains one complete skill, its references, and the MIT license. Install all seven for the full set, or start with `strategy` alone. Existing `analytics-start` installations remain supported.
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, upload each ZIP, and enable it. Follow [Claude's current setup requirements](https://support.claude.com/en/articles/12512180-use-skills-in-claude), including code execution/file creation where required.
3. Ask: “Use strategy to help me understand and improve this application.” Give the session access to the relevant project files.

| Download | Purpose |
| --- | --- |
| [strategy.zip](downloads/strategy.zip) | Save a strategy and perform the next relevant work |
| [analytics-start.zip](downloads/analytics-start.zip) | Compatible measurement entry point |
| [analytics-setup.zip](downloads/analytics-setup.zip) | Shared profile, glossary links, document/task homes, and tools |
| [analytics-requirements.zip](downloads/analytics-requirements.zip) | Outcomes and event definitions |
| [analytics-implement.zip](downloads/analytics-implement.zip) | Instrument the application |
| [analytics-verify.zip](downloads/analytics-verify.zip) | Verify destination receipt |
| [analytics-maintain.zip](downloads/analytics-maintain.zip) | Keep measurement current |

These archives are generated from the skill source in this revision. Do not upload the whole repository as one skill. If downloading the repository instead, the same ZIPs are in `downloads/`.

Available repository, browser, and device access depends on the session. With uploaded documents only, start with Strategy, setup, or requirements; implementing and verifying an application requires access to its actual code and test environment. Account-synced skills and local project files have different loading rules; see [Cowork and cloud-session guidance](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions).

### Other coding assistants

Run the matching command from your application's repository:

```sh
# Cursor
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a cursor

# GitHub Copilot
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a github-copilot

# Gemini CLI
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a gemini-cli
```

Open the same project in your assistant's agent mode and ask:

```text
Use strategy to help me understand and improve this application.
Read the existing resource index and linked records first, if there is one.
```

Use the host's skill picker or discovery controls if it does not load the skill. Gemini CLI provides `/skills list` and `/skills reload`. See the current instructions for [Cursor](https://cursor.com/docs/skills), [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), and [Gemini CLI](https://geminicli.com/docs/cli/skills/).

For another host, use the [installer's supported-agent list](https://github.com/vercel-labs/skills#supported-agents) or choose your host interactively:

```sh
npx skills add vendo-analytics/analytics-measurement-skills
```

### Manual installation and other assistants

Download and extract this repository. Copy each **complete skill folder**, including references, to your host's documented skill directory. Codex uses project `.agents/skills/`; Claude Code uses project `.claude/skills/`. Every skill is self-contained.

If your assistant can read files but has no skill-discovery feature, give it the path to the extracted skill and ask:

```text
Read analytics-measurement-skills/skills/strategy/SKILL.md.
Read our shared resource index, then continue the next useful work for our goal.
Save the strategy and outputs in our chosen document and task locations.
```

Replace the example path with the actual location. For a chat-only assistant, supply the skill and relevant reference files along with your project context. It can help with planning; file edits and receipt checks need suitable connected tools. Automatic discovery and command syntax are host-specific.

### Check, update, or troubleshoot installation

- Installation is project-local by default. Add `--global` for personal use across projects; this does not sync files to hosted or cloud sessions.
- Use `--skill strategy` for the strategy entry point, or select any focused skill by name. `analytics-start` remains available for existing measurement workflows. The entry point uses installed workflows when available and can perform a bounded next step on its own.
- If symlinks are unavailable, add `--copy` to the install command.
- Run `npx skills list` to inspect installed skills. This checks installation, not whether the current assistant session loaded them.
- To update, rerun your original install command and review any replacement prompt. Customer preferences live in your selected project records and should never be stored in the installed skill folder.
- If a command is missing, check the project and installation scope, then reload skills or start a new session. If a reference is missing, reinstall the complete skill folder.
- If a browser, account, or native device is unavailable, continue the work that is possible and retain an explicit verification blocker.

Current installation checks cover isolated Codex and Claude Code projects, including the full set and standalone entry points. The expanded Strategy/shared-record workflow and account-upload flows still need real-user evaluation. Installation alone does not establish live destination success.

## Start with a useful outcome

Ask Strategy what you want to understand or improve. It reads existing records, documents the goal and approach, and performs the next relevant work. It asks at most three unresolved questions at a time and does not require new tracking if existing data is sufficient.

1. **Setup when needed:** establish project facts, preferred document/task locations, existing glossary, tools, and access. Other skills reuse these records.
2. **Strategy:** save the goal, evidence, success measures, chosen or proposed approach, work plan, and next decision.
3. **Do the needed work:** use the included measurement workflows or another suitable available capability. Strategy does not pretend uninstalled specialist skills are present.
4. **Verify and learn:** check implementation separately from business impact. If evaluation needs future observations, save that requirement and resume when asked.

For instrumentation without a defined scope, the measurement workflows can agree one business question and one useful event, then verify its selected routes and cases. A specific repair or verification request proceeds directly without a strategy workshop. Broader requests retain their scope.

The available workflows:

| Skill | What it does | Example request |
| --- | --- | --- |
| [strategy](skills/strategy/SKILL.md) | Documents the strategy and selects/continues relevant work | “Help us improve retention.” |
| [analytics-start](skills/analytics-start/SKILL.md) | Reads project progress and continues the next relevant workflow | “Help me with analytics.” |
| [analytics-setup](skills/analytics-setup/SKILL.md) | Records shared project context, glossary links, document/task destinations, tools, and preferences | “Add our new CRM to the existing analytics setup.” |
| [analytics-requirements](skills/analytics-requirements/SKILL.md) | Starts with outcomes, then refines requirements three questions at a time | “Help us understand why trial accounts fail to activate.” |
| [analytics-implement](skills/analytics-implement/SKILL.md) | Reuses real application triggers and routes events through your chosen tools | “Implement the agreed activation tracking.” |
| [analytics-verify](skills/analytics-verify/SKILL.md) | Exercises the real journey and checks receipt in each final destination | “Verify signup tracking and save the evidence.” |
| [analytics-maintain](skills/analytics-maintain/SKILL.md) | Checks a feature change or requested audit for measurement drift, then updates affected records | “Review the analytics affected by this checkout change.” |

### Resume or switch assistants

Open the same application and analytics workspace in the next assistant, with the needed skill installed. Ask:

```text
Use strategy. Read our shared resource index and summarize agreed decisions, completed work,
and unresolved questions. Continue the next useful step without
repeating answered setup questions. Ask about conflicting information.
```

Use the resource index saved in your project's agent instructions or supplied entry document. Each skill follows its links to relevant authoritative records, including when invoked directly. Another assistant needs access to those records; links do not grant permissions. Reconcile concurrent edits and check current evidence on resume.

## Shared project records

Setup discovers existing records and asks only about missing choices. Documents can live in your selected document system, tasks in your tracker, and code/evidence in appropriate repositories or folders. Record the exact document parent and task project, not just their tool names.

```text
Project instructions or entry document
  → Shared resource index
      → Profile/preferences and work locations
      → Tools, routes, and access references
      → Existing glossary / CONTEXT.md
      → Strategy and authoritative progress
      → Requirements, metrics, and tracking dictionaries
      → Tasks, decisions, and verification evidence
```

One business term has one authoritative meaning. Metrics link to that glossary while owning formulas; event/property definitions own payload and trigger semantics. Skills surface conflicts instead of inventing new definitions.

| Record | Content | Local default, when selected |
| --- | --- | --- |
| Index | Canonical links and one progress summary | README.md |
| Profile | Business/project context, conventions, document/task locations | preferences.md |
| Tools | Accounts, capabilities, secure references, routes | tools.md |
| Glossary | Resolved business terms and relationships | Existing CONTEXT.md or glossary.md |
| Strategy | Goal, evidence, approach, work plan, task/result links | strategy.md |
| Requirements/metrics | Definitions, evidence needs, acceptance criteria | requirements.md |
| Tracking plan | Events, properties, bindings, mappings, cases | tracking-plan.md |
| Decisions | Choices, reasons, superseded meanings | decisions.md |
| Verification | Per-case results and sanitized evidence | `verification/<run>/report.md` |

Create records when they have real content, reuse existing equivalents, and keep customer configuration outside installed skill folders. Each skill saves to the selected home and checks the write when possible. Missing access or readback stays explicit; an unpublished local draft is not presented as a remote document. Private tokens stay in your secret store or ignored configuration.

See the [Setup output format](skills/analytics-setup/references/workspace-format.md) and [Strategy output format](skills/strategy/references/strategy-format.md). Both are instructions for producing your records, not prefilled customer files.

## How implementation works

Each defined trigger has one canonical event binding. Destination delivery belongs in the existing routing layer or analytics owner. If you use a CDP or tag manager, the agent inspects and reuses that path, including any client capabilities that still need their own integration.

The skills discover current official documentation for your selected tools and installed SDKs. There is no fixed destination catalog or bundled provider adapter framework.

[Platform practices](skills/analytics-implement/references/platform-practices.md) cover plain HTML/JavaScript, React and web frameworks, iOS, Android, Flutter, React Native, and how to approach other codebases. They guide the agent's implementation in your application; this repository does not ship an SDK.

## Verification and agent capabilities

Available work depends on document, data, code, and tool access; application implementation requires the actual codebase. Browser, API, and native-device access depend on the host and your connected tools. Setup offers browser-assisted account discovery when available; login and MFA remain yours.

Verification checks the real application journey and each selected final destination. A fired tag, SDK call, or successful HTTP request alone does not prove receipt. Reports distinguish **Pass**, **Fail**, **Blocked**, and **Not run**. Native tracking requires device, simulator, emulator, or attributable user-assisted evidence. Missing access is recorded explicitly.

Maintenance runs during a development session or when requested. These skills do not install a background service, scheduler, or continuous monitor.

## Managed measurement with Vendo

[Vendo](https://vendodata.com/) connects measurement with ongoing data operations:

- First-party tracking and server-side delivery to supported analytics, messaging, and warehouse destinations.
- Connected source data from business tools, with supported server-side integrations.
- Built-in data-quality checks and traceable definitions.
- Shared metrics, customer records, reporting, and supported activation workflows.

Explore [Vendo's documentation](https://docs.vendodata.com/) for current capabilities and setup requirements. The skills remain usable with your chosen stack. Vendo promotion and future product work stay outside the installed skill instructions.

## Development and testing

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/package_skills.py
.venv/bin/python scripts/package_skills.py --check
.venv/bin/python -m unittest discover -s tests -v
```

Edit `skills/` as the source of truth, then regenerate and commit the ZIPs in `downloads/`. CI checks that every archive matches its source and license; archive tests cover extraction, changed sources, corruption, and excluded local files.

Validation checks skill metadata, local file links, and package boundaries. It does not prove an agent's behavior or live destination delivery. Use the [real-workflow evaluation cases](tests/scenarios.md) to test those separately.

Maintainer tasks and improvements live in [To Do](To%20Do/README.md), outside installable skills. A [local tracking library](To%20Do/local-tracking-library.md) for centralized event delivery is being considered for V1; it is not included in this release.

## Credits and license

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills) for focused workflows and setup interviews, and [AI-GTM-QA](https://github.com/Growth-Analytics-Marketing/AI-GTM-QA) for verification from actions through destination evidence. This repository uses generalized workflows; it does not bundle their runtimes or destination-specific integrations.

[MIT](LICENSE) © 2026 Vendo.
