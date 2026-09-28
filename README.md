# Analytics and Measurement Skills

Give your coding agent a measurement workflow: understand the business question, document the tracking plan, implement events, verify destination receipt, and keep it current as your application changes.

Five portable skills for Codex, Claude Code, and other agents that support `SKILL.md`. Bring your own analytics, advertising, CRM, experimentation, CDP, and tag management tools. No Vendo account required.

## Install

From your application's repository, install all five for Codex and Claude Code:

```sh
npx skills add vendo-analytics/analytics-measurement-skills --skill '*' -a codex -a claude-code
```

The [skills installer](https://github.com/vercel-labs/skills) supports other agents and interactive selection:

```sh
npx skills add vendo-analytics/analytics-measurement-skills
```

Installation is project-local by default. Add `--global` for personal use across projects. To install a single workflow, use `--skill analytics-setup`, for example. For manual installation, copy the **entire skill folder**, including its references, into the skill directory documented by your agent. Every skill works independently.

## Start here

In Codex:

```text
$analytics-setup Set up measurement for this application.
```

In Claude Code:

```text
/analytics-setup Set up measurement for this application.
```

Then work through the flows you need:

| Skill | What it does | Example request |
| --- | --- | --- |
| [analytics-setup](skills/analytics-setup/SKILL.md) | Surveys your tools, environments, routing, naming, and setup details; saves preferences | “Add our new CRM to the existing analytics setup.” |
| [analytics-requirements](skills/analytics-requirements/SKILL.md) | Starts with outcomes, then refines requirements three questions at a time | “Help us understand why trial accounts fail to activate.” |
| [analytics-implement](skills/analytics-implement/SKILL.md) | Reuses real application triggers and routes events through your chosen tools | “Implement the agreed activation tracking.” |
| [analytics-verify](skills/analytics-verify/SKILL.md) | Exercises the real journey and checks receipt in each final destination | “Verify signup tracking and save the evidence.” |
| [analytics-maintain](skills/analytics-maintain/SKILL.md) | Checks a feature change or requested audit for measurement drift, then updates affected records | “Review the analytics affected by this checkout change.” |

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

Maintainer roadmap and improvements live in [To Do](To%20Do/README.md), outside installable skills. Future standalone tracker work is deferred beyond V1.

## Credits and license

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills) for focused workflows and setup interviews, and [AI-GTM-QA](https://github.com/Growth-Analytics-Marketing/AI-GTM-QA) for verification from actions through destination evidence. This repository uses generalized workflows; it does not bundle their runtimes or destination-specific integrations.

[MIT](LICENSE) © 2026 Vendo.
