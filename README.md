# Test skills

Three agent skills for everyday testing work: reviewing requirements,
designing test cases, and writing bug reports a developer can act on. They
are written for testers and end users, work in any language, and follow the
open [Agent Skills](https://agentskills.io) format, so they run in Claude
Code and Codex and can be adapted to other assistants.

## The skills

| Skill | What it does |
|-------|--------------|
| [`review-requirements`](review-requirements/) | Reviews user stories, requirements, and acceptance criteria for testability. Finds ambiguous wording, missing cases, and contradictions, and turns them into concrete questions for the product owner. |
| [`test-cases`](test-cases/) | Designs test cases from requirements, covering the main flow, errors, and boundaries, each traced to the criterion it covers. Can also review existing test cases, or restructure them into a consistent format without changing what they test. |
| [`bug-report`](bug-report/) | Helps write defect reports a developer can act on: drafts a new report through a short interview, turns a conversation into a report, or reviews an existing one. |

The skills are instructions only: no scripts, dependencies, or API keys.
They run only when you call them by name.

## Getting started

Clone or download this repository and copy the skill folders into your
assistant's skills folder (macOS, Linux, or a compatible shell):

```bash
# Claude Code
mkdir -p ~/.claude/skills
cp -r bug-report review-requirements test-cases ~/.claude/skills/

# Codex
mkdir -p ~/.agents/skills
cp -r bug-report review-requirements test-cases ~/.agents/skills/
```

To install for a single project, copy them into that project's
`.claude/skills/` or `.agents/skills/` folder instead. Each folder is
self-contained, so you can copy only the skills you want. When updating,
back up any `team-conventions.md` you have edited first, since the copy
replaces it.

Start a new session and call a skill by name, with or without a first
message. In Claude Code:

```text
/review-requirements <paste a user story or requirement>
/test-cases <paste a requirement, or test cases to review or restructure>
/bug-report <describe the problem, or paste a report to review>
/bug-report setup
```

`/bug-report setup` saves your own defaults, such as report language and
destination; see [Personal defaults](#personal-defaults-for-bug-report).
In Codex, use `$` instead of `/`. Write in any language: the skills answer
in your language. Reports, reviews, and test cases are written in the
language your team has set, otherwise in the language of your message or
the requirement.

## What the skills always do

These rules apply whatever your settings say:

- **No invented facts.** Anything missing is marked `Unknown` or turned
  into a question, never guessed.
- **Sensitive data is masked.** Passwords, tokens, and personal data are
  removed from what the skill writes. `bug-report` can keep personal or
  customer data a report needs if you explicitly choose that (see below);
  credentials are always masked.
- **Nothing is published without your yes.** Before filing an issue or
  posting a comment, the skill shows exactly what will be sent and waits
  for explicit approval.

These are instructions to the assistant, not technical guarantees. Review
drafts before you share them.

## Customizing

### Team conventions

Each skill has a `references/team-conventions.md` file for your team's
shared rules. It ships empty, with an example to copy from. Anything you
write there takes precedence over the skill's defaults, for example:

- the language reports and reviews are written in
- your severity scale
- which tracker and project to use, and required fields
- what words like "must" and "should" mean in your requirements
- terminology and things to always check

You can also replace `bug-report/references/template.md` with your own
report format.

### Personal defaults for `bug-report`

`bug-report` can remember your report language, destination (for example
Jira), and delivery method. After your first report it offers to save the
choices you used, or you can run `/bug-report setup` (`$bug-report setup`
in Codex) at any time.

Your choices are saved in `~/.config/bug-report/preferences.md`
(`%USERPROFILE%\.config\bug-report\preferences.md` on Windows), outside the
skill folder, so updating the skill keeps them. Team conventions win over
personal defaults, and anything you say for a single report wins over both
without changing what is saved.

By default, personal and customer data are masked. If your tracker is
allowed to hold such data, you can choose **Preserve** for that destination:
reports then keep the details needed to reproduce a problem, such as an
account email or order ID. Credentials are always masked, and a team can
turn Preserve off in its conventions file.

## Compatibility

| Assistant | Install to | Call a skill | Called only by name? |
|-----------|-----------|--------------|----------------------|
| Claude Code | `~/.claude/skills/` or `<project>/.claude/skills/` | `/bug-report` | Yes, via `disable-model-invocation: true` in `SKILL.md` |
| Codex (CLI, IDE extension) | `~/.agents/skills/` or `<repo>/.agents/skills/` | `$bug-report`, or pick one with `/skills` | Yes, via `agents/openai.yaml` |
| ChatGPT desktop | See OpenAI's [Build skills](https://learn.chatgpt.com/docs/build-skills) | Type `@` and pick the skill | Not verified |
| Other Agent Skills hosts | See the host's documentation | See the host's documentation | Not verified; depends on the host |

This table follows each host's documentation as of 2026-10-11
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

## Contributing

If a skill does something it shouldn't, please report it. See
[CONTRIBUTING.md](CONTRIBUTING.md) for what to include and how to propose
changes. Use fictional examples, and remove private team conventions before
sharing a copy of a skill.

## License

[MIT](LICENSE) © 2026 Alexander Danvall. Each skill folder includes a copy
of the license, so a skill copied on its own still carries it.
