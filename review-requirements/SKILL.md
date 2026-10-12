---
name: review-requirements
description: >
  Reviews user stories, requirements, and acceptance criteria for
  testability before development starts: finds ambiguous wording, missing
  cases, contradictions, and untestable criteria, and turns them into
  concrete questions for the product owner. Use only when the user
  explicitly invokes this skill or asks for it by name.
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
   `{{order ID}}`); translate the words into the review language. Do not
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
   vocabulary. Explain any testing term you use.
6. **Protect sensitive data.** If the requirement contains customer data,
   credentials, or personal data, do not repeat it anywhere in your reply,
   including commentary, and even if it looks fake or like test data. Refer
   to it by type and location only (for example "the email address in the
   example") and tell the user it should be removed from the requirement.
7. **Never publish without confirmation.** Posting comments to a tracker or
   editing a requirement changes shared work. Show exactly what will be
   posted and get an explicit "yes" first.
8. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Write the review in the language of the requirement unless the
   user asks otherwise. Quote the requirement exactly, untranslated, except
   for masking required by rule 6; add a translation in parentheses if the
   review is in another language.
   Translate all headings, labels, priorities, and verdicts from this file
   into the review language, keeping the structure. If you write
   Given/When/Then (see Step 4), follow the team's keyword convention if one
   is visible (some teams keep the English keywords); otherwise use the
   keywords of the review language (for example Swedish *Givet/När/Så*,
   German *Angenommen/Wenn/Dann*). Write dates as `YYYY-MM-DD`.

## Step 1: Get the requirement and its context

Accept the requirement in whatever form the user has: pasted text, a file,
or a tracker link if you have a working integration for that tracker. Never
fetch from a tracker or project you guessed. If the user refers to a file
or document you do not have, ask them to attach it or give its path; never
search the file system for it.

Choose the mode:

| Mode | When |
|------|------|
| **A. Single item** | One story, requirement, or feature description |
| **B. Set of items** | Several stories, an epic, or a specification section. Also check for conflicts and gaps *between* items |

Ask only if it changes the review, and at most three questions. Three is a
maximum, not a target; often no questions are needed. This limit applies to
questions asking the user for an immediate reply. The review's findings
may each include their required clarification question. For example:
- Who are the users of this feature (roles, permissions)?
- Is there a related design, specification, or existing behavior it should
  match?
- Is anything deliberately out of scope?

If the user has no context to give, proceed and note your assumptions in the
review.

## Step 2: Review

First read `references/team-conventions.md`. Ignore its *Example* section;
it is never applied. If the placeholder line is still in the file, there
are no team conventions. Otherwise its conventions take precedence over
the defaults in this skill wherever they conflict. Conventions the user
states in the conversation take precedence over the file. The core rules
always apply.

Then work through `references/review-checklist.md`, and use
`references/ambiguity-patterns.md` to spot vague wording. The patterns are
written in English, but look for the same kinds of wording in any language.

For each problem found, record:
- **Where:** the quoted text, or "Missing" with what is missing
- **Problem:** why it blocks building or testing, in one sentence
- **Question:** the concrete question that would resolve it
- **Priority:**
  - **Must clarify:** cannot be built or tested correctly without an answer
  - **Should clarify:** likely to cause defects, rework, or disagreement
  - **Consider:** wording or clarity improvements

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
     a numbered list, or "The system shall …" statements): match it.
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
- [ ] The finding limits from core rule 3 are respected.
- [ ] The verdict matches the table in Step 3.
- [ ] Every proposed acceptance criterion is presented as a proposal, and
      every unknown value is a `[TO CLARIFY: …]` marker, not a guess.
- [ ] Assumptions you made are listed under *Assumptions made in this
      review*.
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

When the open questions have been answered, suggest the next step: writing
test cases from the clarified requirement (for example with the
`test-cases` skill, if the user has it).
