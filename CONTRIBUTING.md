# Contributing

Each root skill folder is distributed independently. Keep its instructions,
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
- When a shared rule changes, check the other skills for the same issue.
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

Check that the README doesn't claim more than has been tested, local
settings and credentials are excluded, and no private conventions or real
customer examples have entered the skill folders. Keep the root MIT license
and its copies in each skill folder consistent.
