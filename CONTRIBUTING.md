# Contributing

Each folder under `skills/` is distributed independently and is also bundled
in the QA Toolkit plugin. Keep its instructions,
references, invocation metadata, and license together. The shared README
and contribution guidance live outside the installed skills.

## Report a problem

Include the skill name, assistant and version, model, date, input, actual
behavior, and expected behavior. Include a small fictional reproduction.
Remove credentials and private information from inputs and outputs before
posting them.

Distinguish installation or invocation problems from problems in the
generated report, review, or test cases.

## Propose a change

- Explain which task or observed failure the change addresses.
- Keep references relative to the skill folder and avoid machine-specific
  paths or dependencies on another installed skill.
- Preserve invocation by name in Claude Code and Codex. The Claude setting
  is an extension; see the README for strict hosts.
- Keep conventions in `references/team-conventions.md` empty by default.
  Examples belong in its explicitly ignored example section.
- Before adding a sentence to fix an observed failure, check whether an
  existing rule should already cover it, and reword that rule instead. If
  the failure comes from two rules pulling in different directions, decide
  which one comes first rather than adding a third.
- When a shared rule changes, check the other skills for the same issue.
  The packaging helper fails if the team conventions sources,
  `team-file-offer.md`, or the shared core wording differ between the
  workflow skills; change them in all five.
- Update documentation when behavior changes and include a reproduction
  of the affected scenario. Record what you checked and what remains
  untested.

## Validate behavior

For instruction changes, run representative scenarios in fresh sessions.
Include complete input, missing information, different languages, and
fictional sensitive values where they matter to the change. Check the
whole reply against the skill's core rules, including commentary and
questions. Repeat scenarios to account for variation between runs.

Record the assistant version, model, date, and skill revision (commit SHA)
alongside the inputs, observed behavior, and result. Keep earlier results
as history and add dated rerun results; do not turn a previous failure into
a pass without rerunning it.

A valid manifest or a successful installation does not demonstrate correct
behavior. Include failures and partial runs so readers can judge the result.

## Before publishing

Keep the identity fields in root `plugin.json` and
`.claude-plugin/plugin.json` synchronized. Update both versions for a new
release. OpenAI presentation metadata lives under
`extensions.com.openai.interface` in root `plugin.json`; the two marketplace
files describe local and GitHub installation sources.

Build release ZIPs with `python3 scripts/package_plugins.py`. The helper
checks shared identity fields and packages an explicit set of release files.
The OpenAI build removes only Claude's `disable-model-invocation`
frontmatter line from the release copies; keep the source line and the
explicit invocation policy in `agents/openai.yaml`.

Validate the Claude plugin and marketplace with:

```bash
claude plugin validate --strict .claude-plugin/plugin.json
claude plugin validate --strict .claude-plugin/marketplace.json
```

Test installation from both local marketplaces in isolated configuration
folders before sharing a release. Validate the OpenAI release skills with
the Codex skill validator, and review the portal's package and skill scan
results before submitting. Installation checks verify packaging and
discovery; they do not replace behavioral testing on the target hosts.

Check that the README doesn't claim more than has been tested, local
settings and credentials are excluded, and no private conventions or real
customer examples have entered the skill folders. Keep the root MIT license
and its copies in each skill folder consistent.
