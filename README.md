# Analytics and Measurement Skills

Give your coding agent a measurement workflow: understand the business question, document the tracking plan, implement events, verify destination receipt, and keep it current as your application changes.

Five portable skills for Codex, Claude Code, and other agents that support `SKILL.md`. Bring your own analytics, advertising, CRM, experimentation, CDP, and tag management tools. No Vendo account required.

## Choose your assistant

Open the **application you want to measure**, then install the skills there. Terminal commands below require Node.js/npm, which supplies `npx`. The skills themselves are Markdown; they do not require a Node.js application.

- [Codex](#codex)
- [Claude Code](#claude-code)
- [Claude app and Cowork](#claude-app-and-cowork)
- [Cursor, GitHub Copilot, Gemini CLI, and other coding assistants](#other-coding-assistants)
- [Manual installation or an assistant without skill discovery](#manual-installation-and-other-assistants)

Using both Codex and Claude Code? Install for both in one command:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a codex -a claude-code
```

### Codex

Run in your application's repository:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a codex
```

Open that project in Codex and send:

```text
$analytics-setup Set up measurement for this application.
```

Project skills are stored in `.agents/skills/`. If a skill is missing, start a new session in that project and check the installed files. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) and [project customization](https://learn.chatgpt.com/docs/customization/overview#skills).

### Claude Code

Run in your application's repository:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a claude-code
```

Open Claude Code in the same project and send:

```text
/analytics-setup Set up measurement for this application.
```

Claude Code reads `.claude/skills/`. The installer may link those folders to shared copies in `.agents/skills/`; keep the targets with your project. See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

### Claude app and Cowork

Local Claude Code installation does not install skills into your Claude account. For the app's custom-skill upload:

1. Download this repository with GitHub's **Code → Download ZIP**, then extract it.
2. Inside `skills/`, ZIP each skill folder you want to use, including its `SKILL.md` and references. For example, `analytics-setup.zip` should contain `analytics-setup/SKILL.md` and `analytics-setup/references/workspace-format.md`. Do not upload the whole repository as one skill.
3. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, upload each ZIP, and enable it. Follow [Claude's current setup requirements](https://support.claude.com/en/articles/12512180-use-skills-in-claude), including code execution/file creation where required.
4. Ask: “Use analytics-setup to help me set up measurement for this application.” Give the session access to the relevant project files.

Available repository, browser, and device access depends on the session. With uploaded documents only, start with setup and requirements; implementing and verifying an application requires access to its actual code and test environment. Account-synced skills and local project files have different loading rules; see [Cowork and cloud-session guidance](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions).

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
Use the analytics-setup skill to set up measurement for this application.
Read the existing analytics workspace first, if there is one.
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
Read analytics-measurement-skills/skills/analytics-setup/SKILL.md.
Use it for this application's measurement setup, reading the linked
references as needed. Save preferences in the application workspace.
```

Replace the example path with the actual location. For a chat-only assistant, supply the skill and relevant reference files along with your project context. It can help with planning; file edits and receipt checks need suitable connected tools. Automatic discovery and command syntax are host-specific.

### Check, update, or troubleshoot installation

- Installation is project-local by default. Add `--global` for personal use across projects; this does not sync files to hosted or cloud sessions.
- Use `--skill analytics-setup` to install only setup. Other skills are optional.
- If symlinks are unavailable, add `--copy` to the install command.
- Run `npx skills list` to inspect installed skills. This checks installation, not whether the current assistant session loaded them.
- To update, rerun your original install command and review any replacement prompt. Customer preferences live in your separate analytics workspace and should never be stored in the installed skill folder.
- If a command is missing, check the project and installation scope, then reload skills or start a new session. If a reference is missing, reinstall the complete skill folder.
- If a browser, account, or native device is unavailable, continue the work that is possible and retain an explicit verification blocker.

Installer checks cover Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI. Full agent workflows and account-upload flows still need evaluation. Installation alone does not establish live destination success.

## Your first measurement journey

Start with **one business question and one useful event**. You can expand after the first destination receipt is verified:

1. **Setup:** discover existing tracking, choose where analytics work lives, and save your tools and preferences. You can answer “not sure” and leave a decision open.
2. **Requirements:** explain what you want to understand and the decision it should support. Refine the event's meaning before writing code.
3. **Implementation and verification:** implement the agreed event, exercise the actual journey, and check each selected destination. An unavailable account becomes a specific next action.
4. **Maintenance:** when a feature or tool changes, ask the agent to review the affected measurement.

If you already have tracking, start with a scoped verification or maintenance request. You do not need to restart onboarding or invoke every skill.

The available workflows:

| Skill | What it does | Example request |
| --- | --- | --- |
| [analytics-setup](skills/analytics-setup/SKILL.md) | Surveys your tools, environments, routing, naming, and setup details; saves preferences | “Add our new CRM to the existing analytics setup.” |
| [analytics-requirements](skills/analytics-requirements/SKILL.md) | Starts with outcomes, then refines requirements three questions at a time | “Help us understand why trial accounts fail to activate.” |
| [analytics-implement](skills/analytics-implement/SKILL.md) | Reuses real application triggers and routes events through your chosen tools | “Implement the agreed activation tracking.” |
| [analytics-verify](skills/analytics-verify/SKILL.md) | Exercises the real journey and checks receipt in each final destination | “Verify signup tracking and save the evidence.” |
| [analytics-maintain](skills/analytics-maintain/SKILL.md) | Checks a feature change or requested audit for measurement drift, then updates affected records | “Review the analytics affected by this checkout change.” |

### Resume or switch assistants

Open the same application and analytics workspace in the next assistant, with the needed skill installed. Ask:

```text
Read our analytics workspace and summarize agreed decisions, completed work,
and unresolved questions. Continue the next measurement step without
repeating answered setup questions. Ask about conflicting information.
```

Use the workspace path saved in your project's agent instructions. The files carry the handover; a new assistant does not need the previous chat history. Keep one editable workspace across assistants and reconcile concurrent edits before continuing.

## Your measurement workspace

Setup asks where to store your analytics work and records a pointer in your project's agent instructions. The same customer-owned Markdown files guide every installed skill and agent. Preferences stay with the application; rerunning setup merges changes without rewriting installed skills.

Files grow as work happens:

| Artifact | Content |
| --- | --- |
| `README.md` | Workspace navigation, scope, and ownership |
| `preferences.md` | Platforms, environments, event/property casing, identity and data rules |
| `tools.md` | Selected tools, account references, capabilities, credentials references, and delivery routes |
| `requirements.md` | Business questions, definitions, potential measurements, and acceptance criteria |
| `tracking-plan.md` | Event contracts, properties, real code bindings, destination mappings, and cases |
| `decisions.md` | Material decisions, reasons, and affected records |
| `verification/<run>/report.md` | Per-case results and links to sanitized API evidence or screenshots |

These are working records, created when there is content to record. Existing equivalent documents can be reused. Private tokens belong in your secret store or ignored environment configuration, with references in the workspace.

## How implementation works

Each defined trigger has one canonical event binding. Destination delivery belongs in the existing routing layer or analytics owner. If you use a CDP or tag manager, the agent inspects and reuses that path, including any client capabilities that still need their own integration.

The skills discover current official documentation for your selected tools and installed SDKs. There is no fixed destination catalog or bundled provider adapter framework.

[Platform practices](skills/analytics-implement/references/platform-practices.md) cover plain HTML/JavaScript, React and web frameworks, iOS, Android, Flutter, React Native, and how to approach other codebases. They guide the agent's implementation in your application; this repository does not ship an SDK.

## Verification and agent capabilities

Your agent needs code/file access for planning and implementation. Browser, API, and native-device access depend on the host and your connected tools. Setup offers browser-assisted account discovery when available; login and MFA remain yours.

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
.venv/bin/python -m unittest discover -s tests -v
```

Validation checks skill metadata, local file links, and package boundaries. It does not prove an agent's behavior or live destination delivery. Use the [real-workflow evaluation cases](tests/scenarios.md) to test those separately.

Maintainer tasks and improvements live in [To Do](To%20Do/README.md), outside installable skills. A [local tracking library](To%20Do/local-tracking-library.md) for centralized event delivery is being considered for V1; it is not included in this release.

## Credits and license

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills) for focused workflows and setup interviews, and [AI-GTM-QA](https://github.com/Growth-Analytics-Marketing/AI-GTM-QA) for verification from actions through destination evidence. This repository uses generalized workflows; it does not bundle their runtimes or destination-specific integrations.

[MIT](LICENSE) © 2026 Vendo.
