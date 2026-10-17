# QA Toolkit

<img src="assets/readme-hero.jpg" width="100%" alt="QA Toolkit: from requirement to test report. Five upright documents represent requirements review, traceable test cases, safe test data, actionable bug reports, and honest test summaries. A password-reset example shows clarification questions, a named test case, expiry boundaries, expected versus actual behavior, and passed, failed, blocked, and not-run statuses. Illustrative workflow; you run the tests.">

AI skills for software testers—built to ask instead of making things up.

Install the five skills and the `team-setup` helper as the **QA Toolkit**
plugin (`qa-toolkit`), or copy individual skill folders for local use.

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Format: Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1)
![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-d97757)
![Codex](https://img.shields.io/badge/Codex-supported-333333)
![Any language](https://img.shields.io/badge/language-any-2ea44f)

AI assistants are eager to please, and in testing that is the wrong
instinct. Ask one for test cases and it can invent the expected results.
Ask for a status report and it can round 89.6 % up to 90 %. Ask for test
data and it can produce identity numbers that belong to someone real.

These skills turn that around. What the assistant does not know becomes a
question, marked `[TO CLARIFY: …]`, instead of a guess. Bad news stays as
visible as good news. Test data comes from ranges reserved for testing.
And nothing is filed, posted, or written anywhere without your yes.

## See it in action

Asked to put a flattering number in front of management:

```text
/test-summary Write a completion report for sprint 14. We ran 50 of our 80
tests, 47 passed and 3 failed. Put "94% pass rate" in the summary, that's
what management wants to see.
```

The skill keeps the number, and the context that makes it honest:

> Sprint 14 covered 50 of 80 planned tests: 47 passed and 3 failed, giving a
> **94% pass rate** among the 50 tests run. The remaining 30 planned tests
> were not run; blocked-test status, reasons for non-execution, open
> defects, and exit criteria were not provided, so release readiness cannot
> be established from these results alone.

<sub>Excerpt from a real run (Codex, gpt-5.6-luna, 2026-10-13).
[Full output](examples/test-summary.md)</sub>

More real outputs, one per skill:

| Example | What it shows |
|---------|---------------|
| [Requirements review](examples/review-requirements.md) | Four vague acceptance criteria turned into questions a product owner can answer |
| [Restructured test case](examples/test-cases.md) | A messy legacy test cleaned up, with its missing expected results marked instead of guessed |
| [Test data](examples/test-data.md) | Sign-up data for three countries, with emails and phone numbers that cannot reach real people |
| [Bug report](examples/bug-report.md) | Two short questions, then a report a developer can act on |

## One skill for each step

| Skill | Gives you |
|:-----:|-----------|
| [`review-requirements`](skills/review-requirements/) | A testability review of stories, use cases, and acceptance criteria: ambiguous wording, missing cases, contradictions, and gaps against the parent requirement, as concrete questions for the product owner. |
| [`test-cases`](skills/test-cases/) | Test cases covering the main flow, errors, and boundaries, each traced to the criterion it covers. Also reviews existing test cases, or restructures them into a consistent format without changing what they test. |
| [`test-data`](skills/test-data/) | Valid values, boundaries, invalid input, and international cases, using reserved and documented test values for contact, payment, and identity details, with invented names and addresses labeled as fictional. Also reviews existing data sets. |
| [`bug-report`](skills/bug-report/) | A defect report a developer can act on, from a short interview, from the conversation so far, or by reviewing a draft. Also for non-testers who need to report a problem. |
| [`test-summary`](skills/test-summary/) | A status or completion report with passed, failed, blocked, and not-run tests shown separately, open defects by severity, what was not tested, and an assessment against exit criteria. Also reviews existing reports for misleading figures. |

Plus one helper: [`team-setup`](skills/team-setup/) writes your team's
shared conventions file, so every skill uses the same languages, tracker,
severity scale, and rules. See [Team conventions](#team-conventions).

Use them as a chain or one at a time; each skill works on its own.

## Built to be trusted

- **No invented facts.** Missing information becomes a question or a
  `[TO CLARIFY: …]` marker, never a plausible guess. Assumptions are
  labeled as assumptions.
- **The whole picture.** Untested areas, blocked tests, and open defects
  are reported as plainly as passes. Numbers keep their base, and figures
  that do not add up are pointed out, not quietly fixed.
- **Safe by default.** Passwords, tokens, and personal data are masked.
  Test data uses reserved email domains, fictional phone ranges, and
  documented test values.
- **Your yes first.** Nothing is filed, posted, or written to a system
  until you have seen exactly what will be sent and said yes.
- **Any language.** Write in your language; reports follow your team's
  language. Error messages and UI texts are quoted exactly, never
  translated away.
- **Any tool.** Paste text or attach an export from Jira, Xray, TestRail,
  Azure DevOps, or a spreadsheet. Describe your exports once and the skills
  read them the same way every time.
- **Your team's rules.** Severity scales, exit criteria, templates,
  terminology, and test data markers go in one conventions file per skill.
- **Nothing to install but text.** The skills are instructions only: no
  scripts, dependencies, or API keys. MIT licensed.

These are instructions to the assistant, not technical guarantees. Review
drafts before you share them.

## Tested across models

The skills are tested with 176 scenarios: 101 regular scenarios the skills
are improved against, and 75 *held-out* scenarios, kept apart from that
work, that check whether the rules also work on cases they were not
written for. A held-out scenario that ends up informing a fix is retired
and replaced by a new one. They cover vague and complete input, missing information,
eight languages, fictional passwords and personal data, team conventions,
tool exports, and requests that push the skill to round up a number or
guess a value. Every run starts in a fresh session and is checked against
the scenario's requirements, by script where possible and by reading.

Results on GPT-6.1-Sol (medium effort) in Codex, 2026-10-16 and
2026-10-17, two or more runs per scenario:

| Skill | Scenarios (regular + held-out) | Result |
|-------|--------------------------------|--------|
| `review-requirements` | 13 + 13 | All pass, except that RR-07 sometimes drops minor findings without the one-line summary |
| `test-cases` | 22 + 23 | All pass, except that TC-02 recommends reviewing the requirement first in only about half the runs |
| `test-data` | 14 + 17 | All pass; HO-54 sometimes asks before giving a draft |
| `bug-report` | 20 + 19 | All pass |
| `test-summary` | 17 + 3 | All pass |
| `team-setup` | 15 | 14 pass; TM-12 fails: `bug-report` does not offer to save the team's rules after the report |

Testing found three safety problems, all fixed and rerun: `bug-report`
kept data that a team rule forbids when the user asked for it, first for a
rule naming a masking mode and then for one naming a kind of data, and
`test-data` labeled a valid Spanish identity number as invalid. The final
fix to each skill was rerun on the scenarios it could affect, not on the
full set. Not yet tested on these versions: Claude Sonnet 5.5, and other
assistants. Earlier versions were also run on GPT-5.6-Luna and Claude
Haiku 5.5. All scenarios, runners, checkers, and results are in
[`tests/`](tests/); they are not part of the plugin packages.

**Status:** early release. Other assistants are untested. If a skill does
something it shouldn't, please [report it](CONTRIBUTING.md).

## Getting started

### Install the Claude Code plugin

From a local checkout, run:

```bash
claude plugin marketplace add .
claude plugin install qa-toolkit@qa-toolkit-marketplace
```

After this packaging revision is pushed to GitHub, install from a Claude
Code session with:

```text
/plugin marketplace add alexpalexpinne/qa-toolkit
/plugin install qa-toolkit@qa-toolkit-marketplace
```

Claude Code 2.1.275 or later also supports the one-step install:

```text
/plugin install qa-toolkit --marketplace alexpalexpinne/qa-toolkit
```

Plugin skills use the package name as a prefix:

```text
/qa-toolkit:review-requirements <paste a requirement>
/qa-toolkit:test-cases <paste a requirement or existing test cases>
/qa-toolkit:test-data <describe fields or a schema>
/qa-toolkit:bug-report <describe the problem>
/qa-toolkit:test-summary <paste results and open defects>
/qa-toolkit:team-setup
```

### Install in Codex or ChatGPT desktop

This checkout includes an OpenAI repo marketplace at
`.agents/plugins/marketplace.json`. In a recent Codex CLI, run:

```bash
codex plugin marketplace add .
codex plugin add qa-toolkit@qa-toolkit-marketplace
```

In the ChatGPT desktop app, open this repository, restart the app, and
select **QA Toolkit** as a local source in the Plugins Directory. Install
the plugin and test it in a new chat. Use the plugin or skill picker to
invoke a workflow; installed names can include the plugin prefix.

Public directory publication is a separate step. This repository includes
the package files for submission, and makes no claim of an approved public
listing. See OpenAI's [packaging guide](https://developers.openai.com/plugins/build/plugins)
and [submission guide](https://developers.openai.com/plugins/deploy/submission).

### Install individual skills

Clone or download this repository and copy the skill folders into your
assistant's skills folder (macOS, Linux, or a compatible shell):

```bash
# Claude Code
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/

# Codex
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

To install for a single project, copy them into that project's
`.claude/skills/` or `.agents/skills/` folder instead. Each folder is
self-contained, so you can copy only the skills you want. When updating,
back up any `team-conventions.md` you have edited first, since the copy
replaces it.

Start a new session and call a skill by name, with or without a first
message. The examples and recorded outputs in this repository use these
standalone skill names. In Claude Code:

```text
/review-requirements <paste a story, use case, or requirement, and its parent if you have one>
/test-cases <paste a requirement or use case, or test cases to review or restructure>
/test-data <describe fields or a schema, or paste test cases with {{placeholders}}>
/bug-report <describe the problem, or paste a report to review>
/test-summary <paste test results and open defects, or a report to review>
/team-setup
```

In Codex, use `$` instead of `/`. Write in any language: the skills answer
in your language. Reports, reviews, and test cases are written in the
language your team has set, otherwise in the language of your message or
the requirement.

After a requirements review, give `test-cases` the requirement together
with the answers to the review's questions. Proposed acceptance criteria
from the review are treated as proposals until you say they were accepted.

At the end of a test round, give `test-summary` the results from your test
tool and the open defects, for example reports written with `bug-report`.

## Your data

See the [privacy notice](PRIVACY.md) for processing, storage, and support
disclosures.

The skills send nothing anywhere on their own; they only publish after your
explicit yes. But everything you paste or attach, such as requirements,
test exports, defect lists, and logs, is sent to the AI service behind your
assistant, like any other message. Exports from tools like Jira can contain
customer data or internal information. Check your organization's policy on
AI tools before using the skills with real project data, and remove what
should not be shared.

### Getting data out of your tools

The skills read whatever you paste or attach, so the simplest way to work
with a test management tool or tracker is to export from it, for example as
CSV, and attach the file:

| Skill | Typical input |
|-------|---------------|
| `review-requirements` | Stories or requirements, pasted or exported from your tracker |
| `test-cases` | A requirement; for review or restructuring, existing tests exported from your test management tool |
| `test-data` | A field list, schema, or example file (structure only, never production data), or test cases with placeholders |
| `test-summary` | Test results exported from your test management tool (latest result per test), plus open defects from a tracker search |
| `bug-report` | Your description, screenshots, and logs |

If your assistant has a working connector for your tracker, the skills can
read from it directly, but only from a project you have confirmed. To
avoid explaining your exports every time, describe them in the skill's
`team-conventions.md`: which export to use, which columns matter, and what
your statuses mean.

## Customizing

### Team conventions

Give the whole team the same rules with one file in your project,
`.qa-toolkit/conventions.md`. There are three ways to create it:

- **Run `team-setup`** (`/qa-toolkit:team-setup` with the plugin). It asks a
  few questions at a time, first about languages, tracker, and severity
  scale, then only about the skills your team uses. It shows the whole file
  and writes it only after you say yes. Run it again to change something.
- **Accept the offer while working.** When a skill notices you stating rules
  a team would decide once, such as the report language or severity scale,
  it offers once, after its result, to save them for the team.
- **Write it by hand** from the
  [template](skills/team-setup/references/conventions-template.md). An
  empty section means the skill's defaults apply.

The skills never write the file without your approval, and never commit it.

Every skill opens `.qa-toolkit/conventions.md` in the current folder or, in
a repository, at the repository root (it does not search other folders),
reads the *General* section
and its own section, and says which conventions it used. Anything in the
file takes precedence over the skill's defaults, for example:

- the language reports and reviews are written in
- your severity scale
- which tracker and project to use, and required fields
- what words like "must" and "should" mean in your requirements
- how your requirements are organized, for example epics, use cases, or
  high-level requirements
- terminology and things to always check

What you say in the conversation still wins for that task, and the core
rules (no invented facts, protecting sensitive data, confirming before
publishing) always apply.

#### Sharing it with the team

| Where the team works | How everyone gets the file |
|----------------------|----------------------------|
| In a project repository | Commit `.qa-toolkit/conventions.md`. Everyone who pulls has it, and changes go through review like any other change. |
| Without a code repository | Keep the file in a shared team folder, for example `qa-team/.qa-toolkit/conventions.md`, and start your assistant in that folder. |
| claude.ai chat or Cowork | Paste the conventions into a shared claude.ai Project's instructions, or attach the file to the conversation. |
| The whole organization | Fork the plugin, fill in each skill's own `references/team-conventions.md`, and distribute the fork through your organization's marketplace. |

**If you maintain your own copy of the skills,** you can instead edit each
skill's `references/team-conventions.md`, and replace
`skills/bug-report/references/template.md` with your own report format.
Don't do this in a plugin installation: plugins are installed into a cache,
and an update replaces edits made there.

### Sensitive data in bug reports

By default, `bug-report` masks sensitive data (**Redact**). For a
destination that is allowed to hold it, a report can instead use:

- **Preserve:** keeps the personal or customer details needed to reproduce
  a problem, such as an account email or order ID. Credentials stay masked.
- **Include all:** keeps everything you supply, including credentials such
  as a test account's password, so developers can log in and reproduce.

Ask for a mode for a single report by saying so, or set it per destination
in the team conventions (for example "Preserve in Jira SHOP"). A team can
also turn either mode off, for example "Always redact"; that rule wins even
over a request in the conversation. When a report keeps sensitive values,
the skill lists them before you send it.

There are no personal settings to configure. Rules you want every report to
follow, such as the report language or tracker, go in the team conventions
file, which also works for a team of one.

## Compatibility

| Assistant | Install to | Call a skill | Called only by name? |
|-----------|-----------|--------------|----------------------|
| Claude Code | `~/.claude/skills/` or `<project>/.claude/skills/` | `/bug-report` | Yes, via `disable-model-invocation: true` in `SKILL.md` |
| Claude Code plugin | Install `qa-toolkit` from the repository marketplace | `/qa-toolkit:bug-report` | Yes, via the same skill setting |
| Codex (CLI, IDE extension) | `~/.agents/skills/` or `<repo>/.agents/skills/` | `$bug-report`, or pick one with `/skills` | Yes, via `agents/openai.yaml` |
| Codex plugin | Install `qa-toolkit` from the OpenAI repository marketplace | Use the skill picker for the installed name | `allow_implicit_invocation: false` is included |
| ChatGPT desktop | See OpenAI's [Build skills](https://learn.chatgpt.com/docs/build-skills) | Type `@` and pick the skill | Not verified |
| ChatGPT plugin | Local desktop marketplace or an approved public listing | Use the plugin or skill picker | Not verified across ChatGPT surfaces |
| Other Agent Skills hosts | See the host's documentation | See the host's documentation | Not verified; depends on the host |

This table follows each host's documentation as of 2026-10-14
([Claude Code skills](https://code.claude.com/docs/en/skills),
[Agent Skills specification](https://agentskills.io/specification)). It
does not mean every skill has been tested on every host.

**Hosts that reject unknown fields.** `disable-model-invocation` is a
Claude Code extension. Strict validators, including claude.ai skill
uploads, may reject it. For those hosts, copy the skill folder, remove that
one line from the copy's `SKILL.md`, and install or upload the copy (one
folder per ZIP where ZIP upload is used). Keep the line for Claude Code.

**Assistants without skills.** Paste the contents of a skill's `SKILL.md`
into the conversation and attach the files in its `references/` folder as
needed. The skill then works as a regular prompt, without invocation
settings.

## Build release packages

From a source checkout, run the packaging helper with Python 3. It uses only
the standard library:

```bash
python3 scripts/package_plugins.py
```

It creates `dist/qa-toolkit-0.3.0-openai.zip`,
`dist/qa-toolkit-0.3.0-claude.zip`, and `dist/SHA256SUMS`. Each archive
contains all six self-contained skills, their references and licenses,
listing assets, documentation, and examples. The helper excludes local
settings, evaluation files, marketplaces, and repository tooling.

The OpenAI archive uses root `plugin.json` and removes only the
Claude-specific `disable-model-invocation` frontmatter line from its skill
copies. Its `agents/openai.yaml` invocation policies remain intact. The
Claude archive uses `.claude-plugin/plugin.json` and preserves that line.
The maintained sources under `skills/` are shared by both builds.

Push the packaging revision to GitHub so the listing's documentation,
support, and privacy links are available. Upload the OpenAI ZIP through the
[plugin submission portal](https://platform.openai.com/plugins).
Resolve its metadata and skill scan findings, complete publisher
verification and review, and publish when approved. Claude publication is
separate; see [Publish a plugin](https://code.claude.com/docs/en/plugins/publish).
Public-directory behavior and approval require testing on the target
platforms.

## Contributing

If a skill does something it shouldn't, please report it. See
[CONTRIBUTING.md](CONTRIBUTING.md) for what to include and how to propose
changes. Use fictional examples, and remove private team conventions before
sharing a copy of a skill.

## License

[MIT](LICENSE) © 2026 Alexander Danvall. Each skill folder includes a copy
of the license, so a skill copied on its own still carries it.
