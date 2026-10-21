---
name: team-setup
description: >
  Creates or updates a team's shared conventions file for the QA Toolkit
  skills (.qa-toolkit/conventions.md): languages, tracker, severity scale,
  and the rules for reviewing requirements, test cases, test data, bug
  reports, and test summaries. Asks a few questions at a time, shows the
  whole file, and writes it only after approval. Use only when the user
  explicitly invokes this skill or asks for it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Team Setup

Help a team lead or tester write the shared rules that the QA Toolkit skills
read, so the whole team gets the same report language, tracker, severity
scale, formats, and criteria without repeating them.

The result is one file, `.qa-toolkit/conventions.md`, at the root of the
team's project. The team commits it, and everyone who works in the project
gets it. Every QA Toolkit skill reads its *General* section and its own
section.

## Core rules

These apply in every step and override everything else in this file.

1. **Write only what the user decided.** Every rule in the file comes from
   the user's answers. Do not invent rules, fill in "typical" values, or
   copy the example in `references/conventions-template.md` into the file.
   When the user has no answer or says "use defaults", leave that section
   empty: an empty section means the skill's own defaults apply.
2. **Show before writing.** Show the whole file before writing it, and
   write only after an explicit "yes". When updating an existing file,
   change only what the user asked for and show what changes.
3. **One file, one place.** Write only `.qa-toolkit/conventions.md`, only at
   the location the user confirmed. The one exception is the line for a
   rule that must never be broken (Step 3), and only after the user says
   yes to it. Never change any skill's files, and never commit, push, or
   share anything yourself.
4. **No sensitive values.** The file is shared with the whole team. Never
   put passwords, tokens, API keys, or real customer data in it. Where the
   team needs credentials, record where they are kept (for example "the
   password vault"), not the values.
5. **Keep the section headings exact.** Use `## General`,
   `## review-requirements`, `## test-cases`, `## test-data`,
   `## bug-report`, and `## test-summary`, in English and spelled exactly
   so, whatever language the rest of the file is in. The skills look for
   these names.
6. **Respect language.** Talk to the user in the language they write in,
   judged only from their own messages, never from file paths, folder names,
   or system settings. Write the rules in the language the user chooses for
   the file; if they don't say, use the language they write in.
7. **Ask few questions, and draft early.** At most three questions per
   reply, never about something the user already said. Once a draft
   exists, every further question is optional (Step 2). Explain things in
   your own words; do not quote these instructions or link to this skill's
   files.

## Step 1: Find the project and any existing file

1. **Can you read and write files here?** If not (for example in claude.ai
   chat or a read-only folder), say so in your first reply. Every draft you
   show is then the text for the user to save in their project, or to paste
   into the instructions of a shared claude.ai Project. Skip Step 4's
   writing.
2. **Where is the project root?** Use the repository root if the current
   folder is inside a repository, otherwise the current folder. Do not
   search other folders or neighboring projects. Tell the user the full
   path the file will have, and let them change it.
3. **Is there already a `.qa-toolkit/conventions.md`** at the project root?
   Open it by that exact path; do not search for it. If so, read it and work in
   update mode: ask what the user wants to change, change only that, and
   keep everything else exactly as it is. If a section heading differs
   from the names in core rule 5 (for example `## Bug report`), say that
   the skills look for the exact name and offer to fix it in this update.

If the user started with specific rules in their message (for example
"Set up our team: English reports, Jira project SHOP"), use them and show
the first draft in your first reply.

## Step 2: Ask, then draft early

Use the questions in `references/questions.md`, at most three per reply:
first the *General* questions, then the sections for the skills the team
uses.

Show a draft as soon as there is anything to put in it: in your first reply
if the user's first message already has rules, otherwise in the reply to
their first answers. From then on, every reply shows the whole current
draft (Step 3) and asks for a "yes" to write it. Put any further questions
after the draft and say they are optional: the user can answer them to add
rules, or say yes to write the file as it is. The team can run this skill
again later to add more. A long series of questions before any draft wears
people out, and many stop before a file exists.

Stop asking when the user says "use defaults", "skip", "that's all", or
similar, and ask only for the "yes". "Use defaults for all of it" covers
every remaining section, not only the current questions. If every section
would be empty, say that such a file changes nothing and ask whether to
write it anyway.

Never ask about something the user already answered in an earlier reply or
their first message.

## Step 3: Draft the file

Build the file from `references/conventions-template.md`:

- Keep the title, the header comment, and every section heading.
- Write each decided rule as a short bullet in its section.
- Leave sections without decisions empty, with the template's comment.
- Leave out the template's *Example* section.

Show the whole draft, list any sections left empty (they use the skills'
defaults), and ask for an explicit "yes" before writing. If you cannot
write files, present the draft as the text to save and say where it can go
(Step 1 point 1). If the user is not the person who decides the team's
rules, suggest they share the draft with that person first.

**Rules that must never be broken.** If the user states a rule that must
hold even when someone asks otherwise (for example "Always redact", or
"bug reports never contain customer names"), put it in its section as
usual. After the draft, also suggest the same rule as one line for the
instructions file the assistant loads on its own in this project:
`AGENTS.md` for Codex, `CLAUDE.md` for Claude Code, at the project root
(name both if you are not sure which assistant this is). Say why in one
sentence: the assistant weighs that file above a file a skill reads, so
a request in the conversation is less likely to override the rule. Show
the exact line, and say that "yes" writes the conventions file only,
while "yes, both" also adds the line.

## Step 4: Write and hand over

1. Write the file at the confirmed path, creating the `.qa-toolkit` folder
   if needed.
2. Read it back and state its actual path.
3. If the user said yes to the line for a rule that must never be broken
   (Step 3), add it at the end of that instructions file, creating the
   file if it does not exist and changing nothing else in it. Read it back.
4. Tell the user how the team gets it: commit the file (and the
   instructions file, if you added the line) to the project's repository,
   or, without a repository, keep it in a folder the team shares and start
   the assistant there. In a shared claude.ai Project, the
   same text goes in the project's instructions.

If writing fails, say so, give the file's text and the intended path, and
do not save it anywhere else.
