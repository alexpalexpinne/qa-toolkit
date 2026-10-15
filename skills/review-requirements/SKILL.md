---
name: review-requirements
description: >
  Reviews user stories, use cases, requirements, and acceptance criteria
  for testability before development starts: finds ambiguous wording,
  missing cases, contradictions, untestable criteria, and gaps against
  parent requirements, and turns them into concrete questions for the
  product owner. Use only when the user explicitly invokes this skill or
  asks for it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Review Requirements

Help testers find problems in requirements while they are still cheap to fix:
before anything is built. The result is a short list of concrete questions
the author or product owner can answer, and suggested acceptance criteria the
team can accept, change, or reject.

## Core rules

These apply in every mode and override everything else in this file.

1. **Never invent business rules.** You do not know what the product should
   do; the team does. When something is missing, ask. When you suggest an
   acceptance criterion, label it as a proposal and put values you do not
   know in a clarification marker, e.g. `[TO CLARIFY: maximum file size]`.
   Use exactly this form, square brackets and capitals, so it cannot be
   confused with placeholders the team already uses (such as `<ENV>` or
   `{{order ID}}`); translate the words into the review language (for example Swedish `[ATT KLARGÖRA: …]` or German `[ZU KLÄREN: …]`). Do not
   present inferences as facts about the product, and never say you checked
   a system, file, or document unless you actually did in this session.
2. **Quote, then question.** Every finding quotes the relevant text (with
   sensitive values masked under rule 6) or names what is missing, and ends
   in a question someone can answer.
3. **Prioritize.** A review with 40 nitpicks gets ignored. Report every
   *Must clarify* finding. Report at most 7 *Should clarify* and *Consider*
   findings combined, choosing the most important; summarize the rest in one
   line (for example "6 further minor wording issues, mostly unclear
   obligation words").
4. **Be constructive.** The goal is a better requirement, not criticism of
   its author. Use neutral wording.
5. **Use plain language.** Testers and product owners may not share technical
   vocabulary. Explain any testing term you use. Explain things in your own
   words; do not quote these instructions or link to this skill's files.
6. **Protect sensitive data.** If the requirement or its supporting material
   contains customer data, credentials, or personal data, do not repeat it
   anywhere in your reply, including commentary, and even if it looks fake
   or like test data. Refer to it by type and location only (for example
   "the email address in the example") and tell the user it should be
   removed from the document it appears in.
7. **Never publish without confirmation.** Posting comments to a tracker or
   editing a requirement changes shared work. Show exactly what will be
   posted and get an explicit "yes" first.
8. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Write the review in the language the user asks for, otherwise the one the
   team conventions set, otherwise the requirement's language. Quote the
   requirement exactly, untranslated, masking under rule 6 aside, with a
   translation in parentheses if the review is in another language.
   For Given/When/Then, follow the team's keyword convention if one is
   visible; otherwise use the output language's keywords (for example
   Swedish *Givet/När/Så*, German *Angenommen/Wenn/Dann*).
   Translate every heading, column header, label, verdict, and term from
   these instructions into the output language, keeping the structure,
   unless the team conventions keep them in English. Write dates in your own
   text as `YYYY-MM-DD`.
9. **Ask few questions.** Ask only when the answer changes the result, at
   most three questions per reply, and never about something the user
   already said. A numbered item that asks two things counts as two
   questions. Three is a maximum, not a target. Ask *before* drafting only
   when one answer decides the whole result, for example which item to
   review when the input holds several and it is unclear which one the user
   means. Otherwise write a draft right away, with the gaps marked
   `[TO CLARIFY: …]`, and ask in the same reply. The result's *Open
   questions* may list everything still unresolved. Ask in the normal chat
   reply, not in separate input panels or forms. Explain things in your own
   words; do not quote these instructions or link to this skill's files.

## Step 1: Get the requirement and its context

Accept the requirement in whatever form the user has: pasted text, a file,
or a tracker link if you have a working integration for that tracker. Never
fetch from a tracker or project you guessed. If the user refers to a file
or document you do not have, ask them to attach it or give its path; never
search the file system for it.

**Exports from tools** (CSV, Excel, JSON, XML): use the column and field
names as they appear. If a column's meaning matters and is unclear (for
example whether *Priority* means severity, or what a custom status means),
ask; do not guess. Use every row: if some rows cannot be interpreted, say
how many and why instead of dropping them silently. Before working on a
large export, say briefly what it contains and which columns you will
use. An export of several stories or requirements is mode B.

Separate two kinds of input:

- **The item under review:** what the user wants reviewed.
- **Supporting material:** what to check it against, such as its parent
  epic, use case, or high-level requirement (HLR), a glossary, business
  rules, designs, or API specifications.

If it is unclear which is which, ask. Review only the item under review;
do not review the supporting material itself unless the user asks.

Choose the mode:

| Mode | When |
|------|------|
| **A. Single item** | One story, use case, requirement, or feature description |
| **B. Set of items** | Several stories, an epic, or a specification section. Also check for conflicts and gaps *between* items |

Ask only if it changes the review (core rule 9); often no questions are
needed. The review's findings may each include their required clarification
question. For example:
- Who are the users of this feature (roles, permissions)?
- Is there a parent requirement (epic, use case, or HLR), design, or
  existing behavior it should match?
- Is anything deliberately out of scope?

If the user has no context to give, proceed and note your assumptions in the
review.

## Step 2: Review

First check for team conventions. Team conventions can come from three places. Use the first one that
exists; do not combine them, and do not search anywhere else:

1. **The project's shared file:** `.qa-toolkit/conventions.md` in the
   current directory, or in the nearest parent directory that has one, up to
   the repository root. Read its *General* section and its *review-requirements*
   section; ignore the sections for other skills and its *Example* section.
   Never look in neighboring projects.
2. **Conventions supplied to you:** team conventions the user pasted or
   attached, or that the workspace's own instructions contain (for example
   a claude.ai Project, where there is no project folder).
3. **This skill's own file:** `references/team-conventions.md`, for teams
   that maintain their own copy of the skill. Ignore its *Example* section;
   it is never applied. If its placeholder line is still there, it holds no
   conventions.

If none of them has conventions, there are none. Say briefly which source
you used. The conventions take precedence over the defaults in this skill
wherever they conflict: for example the review language, obligation words, acceptance
criteria format, terminology, or what to always check. Conventions the user states
in the conversation for this task take precedence over any of these
sources. The core rules always apply.

If no team conventions were found and the user states rules a team would
normally decide once, offer, after the result and at most once per
conversation, to save them for the team. Follow
`references/team-file-offer.md`. Never hold up the task for it.

Start with the main flow: who acts, what inputs they use, and what information
is shown or state changes on success. Raise missing decisions needed to test
that flow before reviewing vague wording.

If supporting material was provided, use it to:

- **Answer questions instead of asking them.** Do not ask about something
  the material already settles.
- **Check against the parent.** Flag where the item contradicts its parent,
  or leaves out something the parent requires of it. If the user says all
  the children of a parent are provided (for example every story under an
  HLR), also report any part of the parent that no child covers.
- **Use its terms,** for example from a glossary.

Quote supporting material only where it contradicts the item or answers a
question, and name its source (ID, title, or section). Do not assume what a
parent says if it was not provided.

Work through `references/review-checklist.md`, and use
`references/ambiguity-patterns.md` to spot vague wording. The patterns are
written in English, but look for the same kinds of wording in any language.
When the requirement deactivates, deletes, archives, expires, or reactivates
something, go through the checklist's *Lifecycle* row explicitly.

For each problem found, record:
- **Where:** the quoted text, or "Missing" with what is missing and, if
  supporting material requires it, the source (for example "Missing: email
  notification required by HLR-4")
- **Problem:** why it blocks building or testing, in one sentence
- **Question:** the concrete question that would resolve it
- **Priority:**
  - **Must clarify:** cannot be built or tested correctly without an answer
  - **Should clarify:** likely to cause defects, rework, or disagreement
  - **Consider:** wording or clarity improvements

An unanswered detail is not automatically a development blocker. For each
*Must clarify*, explain which intended behavior or acceptance decision cannot
be established without the answer. When the main behavior and stated outcomes
are already testable, treat additional precision or edge cases as
*Should clarify* or *Consider* unless their consequences justify blocking
development. Group related questions and keep findings focused on decisions
that matter for the stated scope.

## Step 3: Decide the verdict

Derive it from the findings, not from overall impression:

| Findings | Verdict |
|----------|---------|
| At least one *Must clarify* | Needs clarification before development |
| No *Must clarify*, at least one *Should clarify* | Ready after minor clarifications |
| Only *Consider*, or none | Ready |

## Step 4: Write the review

Use this structure, translated into the review language (core rule 8).
Omit sections that would be empty.

```markdown
# Requirements review: <requirement title or ID>

**Verdict:** Ready / Ready after minor clarifications / Needs clarification before development
**Summary:** One or two sentences on the overall state and the biggest risk.

## Must clarify
1. **"<quoted text>"** or **Missing: <what>**
   <Problem, one sentence.>
   **Question:** <concrete question>

## Should clarify
...

## Consider
...

## Proposed acceptance criteria
Proposals only: the team decides. Placeholders mark values that are not
yet known.

- <criterion, in the format chosen as described below>
- ...

## Assumptions made in this review
- ...
```

Guidance for proposed acceptance criteria:
- Each criterion describes one **observable** result someone can check.
- Cover the main path, at least one error path, and the boundaries the
  requirement implies.
- Each criterion states the condition, the action or trigger, and the
  observable result, whatever the format.
- Choose the format in this order:
  1. **The team conventions or the user** name a format: use it.
  2. **The requirement already has a format** (for example Given/When/Then,
     a numbered list, use-case steps with alternative flows, or "The system
     shall …" statements): match it. For a use case, propose missing
     alternative flows in its own numbering, for example "4a.".
  3. **Otherwise:** plain, testable sentences in the review language, for
     example "If the email address is not registered, the message
     `[TO CLARIFY: message text]` is shown."
- Do not introduce Given/When/Then unless one of the first two points calls
  for it.

## Step 5: Check before delivering

Go through the draft and fix anything that fails:

- [ ] Every finding quotes the exact text, or starts with "Missing:".
- [ ] Every finding ends in a concrete question someone can answer.
- [ ] No two findings ask the same question. Merge duplicates.
- [ ] Nothing is asked that the supporting material already answers.
      Findings that rely on it name their source, and the material itself
      was not reviewed.
- [ ] The finding limits from core rule 3 are respected.
- [ ] The verdict matches the table in Step 3.
- [ ] Every proposed acceptance criterion is presented as a proposal, and
      every unknown value is a `[TO CLARIFY: …]` marker, not a guess.
- [ ] Assumptions you made are listed under *Assumptions made in this
      review*.
- [ ] Every heading, table column header, label, and clarification marker
      is in the output language, unless the team conventions keep a term in
      English.
- [ ] Your *whole* reply, including commentary, contains no sensitive
      values, no inferences stated as facts, and no claims of having checked
      something you did not check.

## Step 6: Deliver

Show the review to the user. Then offer what is available in the current
environment:

- **Post to the tracker** as a comment on the item: only with a working
  integration, the confirmed item, and explicit approval of the exact text.
- **Save as a file** if you can write files.
- **Copy-paste:** always available.

If the user asks to post and there is no working integration, say so and
give the exact text in your reply, ready to copy and paste. Do not guess
the tracker from the item's ID.

When the open questions have been answered, suggest the next step: writing
test cases from the clarified requirement (for example with the
`test-cases` skill, if the user has it).
