# Test skills

Agent skills that help testers and end users with everyday testing work:
reviewing requirements, designing test cases, and writing clear defect
reports. They accept input in any language and use the
[Agent Skills](https://agentskills.io) format, with invocation settings for
Claude Code and Codex. Other hosts may need the small adaptation described
below. Creating them with Claude does not make the instructions Claude-only.

> **Status:** experimental. `bug-report` has recorded manual runs in Claude
> Code, including failures. `review-requirements` and `test-cases` have test
> scenarios but no recorded runs. Codex and other hosts have no recorded
> behavioral validation.

These are instruction-only skills: no scripts, dependencies, API keys, or
tracker integrations are required to produce drafts. Filing reports or
updating shared work requires an integration supplied by your assistant.

## Skills

| Skill | What it does |
|-------|--------------|
| [`review-requirements`](review-requirements/) | Reviews user stories, requirements, and acceptance criteria for testability. Finds ambiguous wording, missing cases, and contradictions, and turns them into concrete questions for the product owner. |
| [`test-cases`](test-cases/) | Designs test cases from requirements, covering the main flow, errors, and boundaries, each traced to the criterion it covers. Can also review existing test cases, or restructure them into a consistent format without changing what they test. |
| [`bug-report`](bug-report/) | Helps write defect reports a developer can act on: drafts a new report through a short interview, turns a conversation into a report, or reviews an existing one. |

The skills are meant to run only when you call them by name. How reliably
that is enforced depends on the assistant; see the table below.

## Assistant compatibility

The installation guidance below follows host documentation. It does not
mean all three skills have been tested on each host.

| Assistant | Install to | Call a skill | Explicit-only enforced by |
|-----------|-----------|--------------|---------------------------|
| Claude Code | `~/.claude/skills/` (all projects) or `<project>/.claude/skills/` | `/bug-report` | `disable-model-invocation: true` in `SKILL.md` |
| Codex (CLI, IDE extension) | `~/.agents/skills/` (all projects) or `<repo>/.agents/skills/` | `$bug-report`, or `/skills` to pick one | `policy.allow_implicit_invocation: false` in `agents/openai.yaml` |
| ChatGPT desktop | See OpenAI's [Build skills](https://learn.chatgpt.com/docs/build-skills) documentation | Type `@` and pick the skill | **Not verified here.** Check the host's invocation behavior. |
| Other Agent Skills hosts | See the host's documentation and the adaptation below | See the host's documentation | **Not verified.** The `description` requests invocation by name; the host must enforce it. |

Sources: [Claude Code skills](https://code.claude.com/docs/en/skills),
OpenAI's [Build skills](https://learn.chatgpt.com/docs/build-skills), and the
[Agent Skills specification](https://agentskills.io/specification) (checked
2026-10-11). Assistants change quickly; check their current documentation.

### Hosts that validate only the standard fields

`disable-model-invocation: true` is a Claude Code extension, outside the
standard frontmatter fields. Strict validators and uploaders, including
claude.ai skill uploads, can reject it. For those hosts:

1. Make a copy of the skill folder you want to install.
2. Remove only `disable-model-invocation: true` from that copy's `SKILL.md`.
3. Keep the other files, including `references/`, `agents/`, and `LICENSE`.
4. Follow the host's installation or upload instructions. For hosts that
   accept ZIP uploads, package one skill folder per ZIP.

Keep the extension when using Claude Code so invocation stays manual.
`agents/openai.yaml` is separate OpenAI metadata; other hosts may ignore it.
Removing the Claude setting does not give another host invocation controls.
Check that host's settings if invocation only by name matters to you.

## Installation

Download or clone this repository, then run the following from its root.
Each skill is a self-contained folder; copy the complete folders you want.
The commands below are for macOS/Linux or a compatible shell. If a skill
with the same name is already installed, back up that copy first.

```bash
# Claude Code, all projects
mkdir -p ~/.claude/skills
cp -r bug-report review-requirements test-cases ~/.claude/skills/

# Codex, all projects
mkdir -p ~/.agents/skills
cp -r bug-report review-requirements test-cases ~/.agents/skills/
```

For a project installation, use `.claude/skills/` or `.agents/skills/` in
that project instead. Start a fresh session after installation and check
that the three names appear in the skill selector. Cloning the repository
alone does not put the root skill folders in an assistant's discovery path.

If your assistant does not support skills, you can paste the contents of a
skill's `SKILL.md` into a conversation, and attach or paste the files in
`references/` as needed. This is a manual prompt workflow; discovery and
invocation settings will not apply.

## Usage

Call the skill by name, with or without a first message. In Claude Code:

```
/review-requirements <paste a user story or requirement>
/test-cases <paste a requirement, or test cases to review or restructure>
/bug-report <describe the problem, or paste a report to review>
```

In Codex, use `$` instead of `/`. Started without any text, a skill asks
what you need.

Write in any language. The skills answer in the language you use, and write
reviews and reports in the language of the requirement or the language your
team uses.

## Customizing for your team

Each skill has a `references/team-conventions.md` file. It ships empty, with
an example you can copy from. Anything you write there takes precedence over
the skill's defaults, for example:

- the language reports and reviews are written in
- your severity scale
- which tracker and project to use, and required fields
- what words like "must" and "should" mean in your requirements
- terminology and things to always check

You can also replace `bug-report/references/template.md` with your own
report format.

The skills instruct the assistant to follow these rules even when team
conventions differ:

- **No invented facts.** Missing information is marked `Unknown` in
  reports or with clarification markers in reviews and test cases.
- **Sensitive data is masked.** Passwords, tokens, and personal data are
  removed from reports and reviews.
- **Nothing is published without confirmation.** Before filing an issue or
  posting a comment, the skill shows exactly what will be sent and waits for
  an explicit yes.

These are instructions to the model, not technical guarantees. Review
drafts before sharing them; the recorded runs include failures to mask
values and avoid unsupported inferences.

## Testing

Historical `bug-report` runs in Claude Code found failures involving
sensitive values, unsupported inferences, claimed inspections, language
inferred from paths, and an attempted filesystem search without permission.
Those results do not identify the exact skill revision and do not validate
the current files. No behavioral runs are recorded for the other two
skills or for Codex and other hosts.

To evaluate a skill, use fictional inputs in fresh sessions and check the
output against its core rules. Record the assistant version, model, date,
and skill revision alongside the result. See
[CONTRIBUTING.md](CONTRIBUTING.md#validate-behavior) for guidance.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for reporting problems, proposing
changes, and recording validation. Use fictional examples and remove
private team conventions before sharing a copy of a skill.

## License

[MIT](LICENSE) © 2026 Alexander Danvall. Each skill folder includes a copy
of the license, so a skill copied on its own still carries it.
