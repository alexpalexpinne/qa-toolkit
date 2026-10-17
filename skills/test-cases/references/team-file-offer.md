# Offer to save team conventions

Teams can keep shared rules in `.qa-toolkit/conventions.md` in their project,
so nobody has to repeat them. This file says when and how to offer that.

## When to offer

Offer only when all of these are true:

- No team conventions were found in any source (the project file,
  conventions supplied to you, or this skill's own file).
- During this task the user stated something a team would normally decide
  once, for example the test case format, ID scheme, title pattern, priority scale, or test management tool.
- You have not made this offer earlier in the conversation.

Make the offer in the same reply as the result, after it, in one sentence:
say what the team could save and where, and ask whether to draft it. Do
not wait until the result has been filed, posted, or saved. Never hold up the
task for it, and never repeat it.

## If the user says yes

1. **Draft only what was stated.** Write a *General* section and a
   *test-cases* section, using only rules the user stated in this conversation.
   Do not invent rules, fill gaps with defaults, or include sensitive values
   such as passwords, tokens, or real customer data. Keep the section
   headings exactly as `## General` and `## test-cases` in English, whatever
   language the content is in, because every skill looks for these names.
   Start the file with the heading `# QA Toolkit team conventions`.
2. **Choose the location.** Use `.qa-toolkit/conventions.md` at the root of
   the project the user is working in (the repository root, or the current
   folder if there is no repository). Name the full path and let the user
   change it.
3. **Show the whole draft** and write it only after an explicit "yes". If
   the user is not the person who decides the team's rules, suggest they
   share the draft with that person first.
4. **Write, then read back.** After writing, read the file back and state
   its actual path. Never commit, push, or share it yourself. Tell the user
   to commit it so the team gets it, or, without a repository, to keep it in
   a folder the team shares.
5. **If you cannot write files** (for example in claude.ai chat), give the
   text and say where it can go: in `.qa-toolkit/conventions.md` in the
   project, or in the instructions of a shared claude.ai Project.

If the user has the `team-setup` skill, mention that it can set up the
sections for the other skills too.
