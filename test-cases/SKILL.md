---
name: test-cases
description: >
  Designs test cases from user stories, use cases, requirements, and
  acceptance criteria, covering the main flow, error cases, boundaries, and invalid
  input, with each case traced to the criterion it covers. Can also review
  existing test cases for gaps and weaknesses, or restructure them into a
  clean, consistent format without changing what they test. Use only when
  the user explicitly invokes this skill or asks for it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Test Cases

Help testers turn a requirement into test cases that someone else can run
without asking questions, and that together show clearly what is and is not
covered. Also help them improve test cases they already have.

Everything you produce is a draft for a person to review. You are not the
source of truth for how the product should behave.

## Core rules

These apply in every mode and override everything else in this file.

1. **Never invent expected results.** The expected result of a test must
   come from the requirement, supporting material the user provided, the
   existing test, the user, or the team conventions. If the source settles
   part of a result, state that part and mark only the rest, for example
   "Free shipping is not applied; shipping fee `[TO CLARIFY: shipping
   fee]`". If nothing says what should happen, write a clarification marker
   such as `[TO CLARIFY: expected result]`, mark the case *Blocked: pending
   clarification*, and list the question under *Open questions*. Block a
   case only because an expected result is unknown; missing execution
   details, such as which test account to use, go under *Open questions*
   and the case stays *Ready*. A blocked case does not count as coverage. A
   test with a guessed expected result is worse than no test. Proposed
   acceptance criteria the team has not accepted, such as those in a
   requirements review, are not requirements. The same applies to
   inferences: do not present assumptions about the product as facts, and
   never say you checked a system, file, or document unless you actually
   did in this session.
2. **Trace every case.** Each test case names the acceptance criterion or
   requirement it covers. Criteria without test cases are listed as
   uncovered, not hidden. When restructuring, each new step names the
   original step or steps it came from.
3. **Right-size the set.** More test cases is not better. Choose the cases
   that find the most important defects; see the limits in Step 4.
4. **Make cases runnable by someone else.** Concrete preconditions, concrete
   test data, one action per step (a short sequence whose intermediate
   actions have no result of their own may share a step, for example
   entering a search term and selecting *Search*), observable expected
   results. No "verify it works correctly". Take screens, buttons, and
   flows from the requirement, supporting material such as a design, or the
   existing test. Where they are not named, describe the
   action generally (for example "submit the change") and list the missing
   detail under *Open questions*; do not invent UI elements.
5. **Use only fake test data.** Never use real personal data, customer data,
   or credentials in test cases, even if the input contains them. Use
   clearly fake values (for example `example.com` addresses). Never repeat
   credentials from the input (passwords, tokens, keys, connection strings)
   anywhere in your reply, however fake they look. Do not repeat
   real-looking personal or customer data either; refer to it by type only,
   and tell the user that production data should not be used in tests.
   Clearly fake values, such as `example.com` addresses, may be reused.
6. **Never publish without confirmation.** Adding or changing cases in a
   test management tool or tracker changes shared work. Show exactly what
   will be created or changed and get an explicit "yes" first.
7. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Write the test cases in the language of the input unless the team
   conventions or the user say otherwise. Translate headings and labels
   from this file into that language, keeping the structure. For
   Given/When/Then, follow the team's convention if one is visible;
   otherwise use the keywords of the output language (for example Swedish
   *Givet/När/Så*, German *Angenommen/Wenn/Dann*). Write dates in test
   data and in your own text as `YYYY-MM-DD`. Keep dates in UI texts,
   messages, and formats under test exactly as they are (rule 8).
8. **Keep exact text exact, and placeholders apart.** Copy UI texts,
   messages, and technical identifiers exactly: names of tables, columns,
   fields, statuses, scripts, jobs, files, paths, queues, APIs, message
   types, and requirement or defect IDs. Never rewrite, shorten, or "fix"
   scripts, queries, payloads, or configuration, except to mask sensitive
   values as required by rule 5. Preserve the remaining text exactly and
   disclose redactions by type only. If a runnable value was removed, mark
   the case *Blocked: pending clarification* until safe test data is
   supplied. Keep three kinds of placeholder apart:
   - `[TO CLARIFY: …]`: unknown; a person must provide it. Use exactly this
     form, translating the words into the output language.
   - `{{…}}`: a value the tester chooses when running the test, for example
     `{{order number}}`.
   - The team's own technical placeholders, such as `<ENV>` or
     `<CURRENT_DATE>`: keep them exactly as they are.

   Do not wrap fixed names of products or systems in placeholders.
9. **Preserve what exists.** When working with existing test cases, keep
   their IDs, original step numbers, and attachments. Never split a test
   case into several, and never split, merge, reorder, or delete steps that
   have attachments, unless the user explicitly asks; recommend it instead.
   One exception: a step that contains only an expected result may be
   merged into the step with the attachment that it belongs to. The
   attachment stays on that step, the step's action is not changed, and
   the change summary says so.
10. **Ask few questions.** Ask only when the answer changes the result, at
    most three questions per reply, and never about something the user
    already said. Three is a maximum, not a target; often no questions are
    needed. Ask *before* writing only when one answer decides the whole
    result, for example whether the user wants a review or a restructure,
    or which test level the cases are for when the requirement fits several;
    a draft without it would be guesswork. When answers would only fill in
    details, write the draft with the gaps marked `[TO CLARIFY: …]` and ask
    in the same reply. This limit applies to questions asking for an immediate reply;
    the deliverable's *Open questions* may list all unresolved items.
    Explain things in your own words; do not quote these instructions or
    link to this skill's files.

## Before you start: team conventions

Read `references/team-conventions.md`. Ignore its *Example* section; it is
never applied. If the placeholder line is still in the file, there are no
team conventions. Otherwise its conventions take precedence over the
defaults in this skill wherever they conflict: for example the format, ID
scheme, title pattern, priority scale, required fields, or test management
tool. Conventions the user states in the conversation take precedence over
the file. The core rules always apply.

## Step 1: Choose the mode and get the input

| Mode | When |
|------|------|
| **A. Design** | The user provides a requirement, story, use case, or acceptance criteria and wants test cases |
| **B. Review** | The user provides existing test cases and wants them checked: problems, gaps, and suggestions |
| **C. Restructure** | The user provides existing test cases and wants them cleaned up, normalized, or brought into a standard format |

If the user provides existing test cases and it is unclear whether they want
a review or a restructured version, ask.

If the request fits none of the modes (for example running tests, writing
automated test code, or something unrelated), say briefly what this skill
does and which mode, if any, comes closest, and ask how the user wants to
continue. Do not start other work, such as running tests or commands, under
this skill.

Accept input in whatever form the user has: pasted text, a file, or a link
if you have a working integration for that tool. Never fetch from a tool or
project you guessed. If the user refers to a file or document you do not
have, ask them to attach it or give its path; never search the file system
for it. If a path the user gives does not exist, say so and ask. You may
name a folder or file with the same name in the current working folder as
the likely intended one, but do not open it until the user confirms.

**Exports from tools** (CSV, Excel, JSON, XML): use the column and field
names as they appear. If a column's meaning matters and is unclear (for
example whether *Priority* means severity, or what a custom status means),
ask; do not guess. Use every row: if some rows cannot be interpreted, say
how many and why instead of dropping them silently. Before working on a
large export, say briefly what it contains and which columns you will
use. Exports of test cases often have one row per step, with the test's
ID repeated on each row; keep each test's steps together and in their
original order.

The user may also provide supporting material: a parent requirement, a
design, a specification, or a requirements review. Use it as a source for
screens, flows, and expected results, and name it when a case relies on it.
In a requirements review, the requirement and the answers given to its
questions are decided; its proposed acceptance criteria are not. If it is
unclear which proposals the team has accepted, ask.

For mode B, go to *Review mode* below. For mode C, go to *Restructure mode*
below.

## Step 2: Check the requirement is ready (mode A)

Skim the requirement for gaps that would make expected results unknowable:
vague criteria ("fast", "user-friendly"), missing error behavior, undefined
limits.

- **A few gaps:** continue, and use `[TO CLARIFY: …]` markers for the
  unknown expected results.
- **Many gaps, or the main flow itself is unclear:** say so briefly, and
  suggest reviewing the requirement first (for example with the
  `review-requirements` skill, if the user has it). Continue only if the
  user wants to.

Ask only if it changes the result (core rule 10). For example:
- Which level are these tests for: manual tests through the user interface,
  API tests, or something else?
- Which format do you want: step tables or Given/When/Then?
- Are there areas that are especially risky or that have failed before?

If the user has no preference, use the defaults: manual tests, step-table
format from `references/test-case-template.md`.

## Step 3: Find test conditions

For each acceptance criterion, list what needs to be tested. Use the
techniques in `references/test-design-techniques.md` where they fit:

- **Equivalence partitioning:** one representative per group of inputs that
  should behave the same.
- **Boundary values:** at, just inside, and just outside every limit.
- **Decision tables:** combinations of conditions that lead to different
  results.
- **State transitions:** behavior that depends on the current state.
- **Error guessing:** common failure points (empty input, double submit,
  lost connection, missing permissions).

For a use case, the main flow and each alternative flow are test
conditions. Its preconditions become test preconditions, and its end state
is an expected result. Trace each case to its flow, for example `UC-12 main
flow` or `UC-12 4a`.

Also look for conditions the requirement implies but does not list:
permissions, locale (characters, formats, time zones), and concurrency.
Only add these when they matter for this requirement.

## Step 4: Select and prioritize

Assign each case a priority:

- **High:** main flow, and failures that would cause data loss, security
  problems, or block users
- **Medium:** important error cases and boundaries
- **Low:** rare combinations and cosmetic checks

Limits, unless the user asks for more:
- At most **15 test cases** per requirement. If more conditions remain,
  list them in one line each under *Further test ideas*, so the user can
  ask for them.
- Combine cases that differ only in input data into **one data-driven
  case** with a table of values (for example all boundary values for one
  field).

Each case should test one coherent behavior, rule, or flow, with one clear
reason to fail. See *What is one test case?* in
`references/restructuring.md`.

## Step 5: Write the test cases

Use the format in `references/test-case-template.md`, or the team's format.
Fields the team conventions require go on every case, even when the value
is the same for all of them. If the user provides related test cases, for
example from the same suite, match their naming, terminology, placeholders,
and level of detail where that does not change meaning; do not invent a
pattern they do not show. For each case:

- A title: *feature or process – scenario or condition – expected outcome*.
- A purpose: what the test proves, in one or two sentences.
- The criterion it covers.
- Its status: *Ready*, or *Blocked: pending clarification* if any expected
  result is a `[TO CLARIFY: …]` marker.
- Preconditions that put the system in a known state.
- Concrete test data, fake only.
- Numbered steps, one action each, written as a direct instruction
  (`Select 'Save'.`), with step data where the step needs input values.
  State the scenario once rather than in every step.
- An observable expected result: what is shown, stored, sent, or blocked.

Then add:

- **Coverage summary:** a table mapping each acceptance criterion (or
  use-case flow) to its test cases, with one of these statuses:
  - *Covered:* every part of the criterion (each condition, limit, and
    outcome it states) has a case, and all its cases are ready to run
  - *Partly covered:* some part of the criterion has no case, or some of
    its cases are blocked; say which
  - *Blocked:* all its cases are blocked pending clarification
  - *Not covered:* no cases, with the reason
- **Open questions:** every `[TO CLARIFY: …]` marker and assumption.
- **Further test ideas:** conditions left out because of the limit.

## Step 6: Check before delivering

Go through the draft and fix anything that fails:

- [ ] Every expected result comes from the requirement, the existing test,
      the user, or the team conventions. Unknown ones are `[TO CLARIFY: …]`
      markers listed under *Open questions*, and their cases are marked
      *Blocked: pending clarification*.
- [ ] Where the source settles part of a result, that part is stated and
      only the rest is marked. Cases are blocked only for unknown expected
      results, not for missing execution details.
- [ ] Every assumption you made, for example a time zone or a unit, is
      listed under *Open questions*.
- [ ] Every case names the criterion it covers, and the coverage summary
      matches the cases.
- [ ] No case says "works correctly", "as expected", or similar instead of
      an observable result.
- [ ] Every case can run on its own: it does not depend on another case
      having run first, unless that is stated in its preconditions.
- [ ] No duplicates. Cases that differ only in data are combined.
- [ ] The limit from Step 4 is respected.
- [ ] All test data is fake.
- [ ] Every screen, button, and flow in the steps comes from the
      requirement, the existing test, or the user; missing details are open
      questions.
- [ ] UI texts, messages, and technical identifiers are copied exactly, and
      the three kinds of placeholder are not mixed up.
- [ ] Your *whole* reply, including commentary, contains no credentials
      from the input, no real-looking personal data, no inferences stated as
      facts, and no claims of having checked something you did not check.

## Step 7: Deliver

Show the test cases to the user. Then offer what is available in the
current environment:

- **Test management tool or tracker:** only with a working integration.
  Confirm the project or test suite, show exactly what will be created or
  changed, and wait for an explicit "yes".
- **Import file:** if the user wants to import the cases into a tool, ask
  which tool and use its import format. Never guess the column layout.
- **Save as a file** if you can write files.
- **Copy-paste:** always available.

If the user asks to create or change cases in a tool and there is no
working integration, say so and give the exact content in your reply, ready
to copy and paste. Do not guess the tool from an ID.

## Review mode (mode B)

1. Read the existing test cases in full, and the requirement if provided.
2. Check each case against Step 6 and the common problems in
   `references/restructuring.md`. If the requirement is available, also
   check coverage: which criteria have no cases, and which important
   conditions from Step 3 are missing.
3. Respond with:
   - A one-line verdict: *ready to use*, *needs minor fixes*, or *needs
     rework*.
   - The specific problems found, most important first, each with a
     concrete suggestion. Report at most 7 problems in detail; summarize the
     rest in one line.
   - A scope note for any case that looks like several tests in one
     (*Consider split*, with the reason).
   - Suggested new test cases for the most important gaps, at most 5,
     following Step 5.
   - The coverage summary, if the requirement was provided.
   - Open questions.
4. Do not rewrite the set unless the user asks; offer to restructure it
   (mode C) instead. Keep the feedback constructive.

## Restructure mode (mode C)

Rewrite existing test cases into a clean structure **without changing what
they test**. Follow `references/restructuring.md` for the detailed rules on
where content belongs, when steps may be merged or split, attachments, and
scope.

1. Read each test case in full, including IDs, step numbers, attachments,
   and any grouping (suite, folder, test set). If related test cases from
   the same group are provided, read them too, to match their naming and
   style.
2. For each test case, produce:
   - The restructured test case, in the team's format or the default from
     `references/test-case-template.md`, with each step naming its original
     step or steps.
   - A **scope recommendation:** *Scope OK* or *Consider split*, with the
     reason. Never split it yourself unless the user asks.
   - A short **change summary:** what was moved, merged, split, or
     reworded, and what was left as it was on purpose. Describe the changes;
     do not tell the reviewer what to decide.
   - **Open questions:** missing expected results, unclear mappings, and
     attachment decisions a person must make.
3. If related test cases were not provided, say that consistency with the
   group was not checked. Do not invent the group's conventions.
4. Check the result against Step 6 and the checklist in
   `references/restructuring.md`, then deliver as in Step 7.

If more than 5 test cases are provided, restructure the first 5 and ask whether
the result looks right before continuing.
