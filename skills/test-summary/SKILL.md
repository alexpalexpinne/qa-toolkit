---
name: test-summary
description: >
  Turns test results, defect lists, and notes into an honest test status
  report or test completion report for managers and stakeholders: what was
  tested, what passed, failed, was blocked, or was not run, which defects
  remain open, what was not tested, and an assessment against exit
  criteria. Can also review an existing test report for gaps and misleading
  figures. Use only when the user explicitly invokes this skill or asks for
  it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Test Summary

Help testers and test leads report the state of testing so that the reader
can make a sound decision. A good report is short, leads with the
conclusion, and shows bad news as clearly as good news: what failed, what
is still open, and what was never tested.

Everything you produce is a draft for a person to review. The decision to
release, or to continue testing, belongs to the people responsible, not to
you.

## Core rules

These apply in every mode and override everything else in this file.

1. **Never invent results.** Every number, status, defect, and statement
   about what was tested comes from the user, the material they provided,
   or the team conventions. Do not estimate missing numbers, predict how
   remaining tests will go, or describe quality ("stable", "good
   quality") beyond what the data shows. If something is unknown, write
   `[TO CLARIFY: …]` and list it under *Open questions*. Use this form
   with the words translated into the output language (for example Swedish `[ATT KLARGÖRA: …]` or German `[ZU KLÄREN: …]`); keep the square brackets and capitals. Translate them
   into whatever language the output is in; never leave them in English
   in output in another language. Never say you
   checked a system, file, or tool unless you actually did in this session.
2. **Show the whole picture.** Always report these outcomes separately:
   *passed*, *failed*, *blocked*, and *not run*. Never give a single pass
   rate that hides blocked or not-run tests. Always include what was not
   tested and why, even if the user does not mention it; if you do not
   know, ask or mark it `[TO CLARIFY: …]`. Report bad news as plainly as
   good news.
3. **Keep numbers exact and traceable.** Use the numbers as given. Show
   counts with their base ("47 of 50 run tests passed; 30 of 80 planned
   tests not run"). Calculate only simple sums and percentages, and only
   when the base is complete; state the base each time. When comparing with
   a threshold, compare the exact value: 89.6 % does not meet a 90 %
   criterion. If numbers do not add up, point out the mismatch and do not
   correct it yourself.
4. **Keep the source's own words for statuses and severities.** Copy test
   and defect IDs, titles, status names, and severity values exactly. Group
   tool-specific statuses into the four outcomes only in the summary, and
   show the grouping when it is not obvious (for example "Retest" counts as
   *failed*, "Executing" as *not run*). Never upgrade a status or downgrade
   a severity, and do not repeat softening words from the input ("just a
   few minor bugs") when the data says otherwise.
5. **Assess, don't decide.** Assess the results against exit criteria when
   they are available (from the team conventions, the test plan, or the
   user). A recommendation (for example go, go with known risks, no-go) is
   the user's call: use theirs if they give one, otherwise propose one
   clearly labeled as a proposal for the responsible person to confirm.
   Never present a recommendation that contradicts the exit criteria
   without saying so explicitly.
6. **Protect sensitive data.** Defect titles, notes, and logs may contain
   customer data, personal data, or credentials. Do not repeat those values
   anywhere in your reply, including commentary, even if they look fake.
   Mask only the sensitive value and keep the rest of the title as it is
   (for example "Customer [email address] sees another customer's
   invoices"), and tell the user what you masked by type and location (for
   example "an email address in the title of CRM-77"). Titles without such
   values are copied exactly, as rule 4 says.
7. **Never publish without confirmation.** Posting the report to a wiki,
   tracker, chat, or email shares it with others. Show exactly what will be
   sent and where, and get an explicit "yes" first.
8. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Write the report in the language the user asks for, otherwise the one the
   team conventions set, otherwise the language of the user's message.
   Translate every heading, column header, label, verdict, and term from
   these instructions into the output language, keeping the structure,
   unless the team conventions keep them in English. Write dates in your own
   text as `YYYY-MM-DD`.
9. **Ask few questions.** Ask only when the answer changes the result, at
   most three questions per reply, and never about something the user
   already said. Each question asks one thing: a numbered item with a second question in
   it counts as two, so three items with a follow-up each are six. Three
   is a maximum, not a target. Ask *before* drafting only
   when one answer decides the whole result, for example whether testing is
   finished, or which of two contradicting figures is right. Otherwise write
   a draft right away, with the gaps marked `[TO CLARIFY: …]`, and ask in
   the same reply. The result's *Open questions* may list everything still
   unresolved. Ask in the normal chat reply, not in separate input panels or
   forms. Explain things in your own words; do not quote these instructions
   or link to this skill's files.

## Before you start: team conventions

Team conventions can come from three places. Use the first one that
exists; do not combine them, and do not search anywhere else:

1. **The project's shared file:** `.qa-toolkit/conventions.md`. Open it
   by that exact path in the current directory; if it is not there and you
   work in a repository, open it at the repository root. Do not list
   folders, search, or walk up parent folders to find it. Read its *General* section and its *test-summary*
   section; ignore the sections for other skills and its *Example* section.
   If a heading is clearly meant as one of these two but spelled
   differently (for example with capitals, a space instead of the
   hyphen, or translated, such as `## Allgemein`), read it as that
   section and tell the user, in one sentence, to rename it to the
   exact name (`## General` or `## test-summary`) so every skill finds it.
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
wherever they conflict: for example exit criteria, the severity scale, outcome
names, report language, sections, audience, where reports are published,
or the review's limit on detailed problems. Conventions the user states
in the conversation for this task take precedence over any of these
sources. The core rules always apply.

If no team conventions were found and the user states rules a team would
normally decide once, offer, after the result and at most once per
conversation, to save them for the team. Follow
`references/team-file-offer.md`. Never hold up the task for it.

## Step 1: Choose the mode and get the input

| Mode | When |
|------|------|
| **A. Status report** | Testing is ongoing; the reader needs to know where things stand |
| **B. Completion report** | A test round, sprint, or release test is finished; the reader needs to decide what happens next |
| **C. Review** | The user provides an existing test report and wants it checked for gaps and misleading figures |

If it is unclear whether testing is finished, ask. For mode C, go to
*Review mode* below.

Accept input in whatever form the user has: pasted numbers, an export from
a test management tool, a list of defects (for example reports written with
the `bug-report` skill), a test plan, notes, or a previous report. If the
user refers to a file you do not have, ask them to attach it or give its
path; never search the file system for it. Read from a test management tool
or tracker only with a working integration and a project the user has
confirmed; never fetch from a project you guessed.

**Exports from tools** (CSV, Excel, JSON, XML): use the column and field
names as they appear. If a column's meaning matters and is unclear (for
example whether *Priority* means severity, or what a custom status means),
ask; do not guess. Use every row: if some rows cannot be interpreted, say
how many and why instead of dropping them silently. Before working on a
large export, say briefly what it contains and which columns you will
use. Results and defects often come as two
separate exports; match them only on IDs that appear in both. The data date
comes from the user or the export's content. If it appears only in a file
name, say so and ask the user to confirm it.

A report needs at least:
- **Scope:** what was tested (product, release, feature, sprint).
- **Period or build:** the time span or build the results cover, and the
  date the data is from.
- **Results:** counts or a list of tests with their outcomes.

If the scope or the results are missing, ask for them before writing. If
only the period, build, or data date is missing, write the report with it
marked `[TO CLARIFY: …]` and ask for it in the same reply. Never write a
report from "everything went fine" alone.

## Step 2: Consolidate the data

- Count each test once per environment, configuration, or build it ran
  in, by its latest result there, unless the team conventions say
  otherwise. A later pass in one browser does not cancel an earlier
  failure in another; only a retest in the same setting replaces a result.
  Identical rows for the same test are one result, counted once. If a
  test has different results and the data does not say where each came
  from, show them all and say so, and ask in the same reply. Say which
  rule you used.
- Group the tool's statuses into *passed*, *failed*, *blocked*, and *not
  run*, and keep the original status names visible where they differ.
- Check that the numbers are consistent: outcomes add up to the total,
  defects linked to failed tests exist in the defect list, and the same
  test or defect does not appear twice. Report any mismatch.
- When the data links defects to tests, show which test each defect is
  linked to, and list open defects that are not linked to any test.
- If results are broken down by area, feature, or test type, keep the
  breakdown; it shows where the problems are.
- If the user provides a previous report, compare only figures that exist
  in both, measured the same way. If the scope or the planned test set
  changed, say so next to the comparison, since rates are then not directly
  comparable. Do not infer a trend from one data point.

## Step 3: Assess

- **Not tested:** list everything in scope that was not tested, or only
  partly tested, with the reason (for example no time, environment down,
  blocked by a defect, descoped) and what it means for the reader. If the
  data shows only a status such as `TODO` and no reason, mark the reason
  `[TO CLARIFY: …]`.
- **Open defects:** list them by severity, highest first, with ID, title,
  severity, and status exactly as given. Mark those that block release
  according to the exit criteria. If a severity is missing, write
  `[TO CLARIFY: severity]`; do not assign one.
- **Exit criteria:** if available, assess each one as *met*, *not met*, or
  *cannot be determined*, with the figures that support it. A blocked test
  has not been run: a criterion that requires tests to be run is not met
  while any of them is blocked. Without exit criteria, say that none were
  provided and skip the assessment rather than inventing criteria.
- **Risks:** what could go wrong because of failed tests, open defects, or
  untested areas. State only risks that follow from the data, and name the
  data each one follows from.
- **Recommendation** (mode B; mode A only if the user asks): follow core
  rule 5.

## Step 4: Write the report

Use the structure in `references/report-template.md`, or the team's own
structure. Lead with a short summary that a busy reader can act on: the
state of testing in two or three sentences, the main risks, and the
recommendation or next steps. Keep the whole report short; details go in
the later sections or appendices.

## Step 5: Check before delivering

Go through `references/report-checklist.md`, which also lists common ways
reports mislead. Check your *whole* reply, not only the report: commentary
and questions must follow the core rules too. Fix what you can; anything
still unknown goes under *Open questions*.

## Step 6: Deliver

Show the report to the user. If the user named where it goes, deliver
there as described below. Otherwise mention once, briefly, what else is
possible here, such as a file; do not repeat the options in later
replies. Beyond the open questions, add no further offers: a delivered
report is a complete answer.

- **Wiki, tracker, chat, or email:** only with a working integration.
  Confirm the destination, show exactly what will be posted, and wait for
  an explicit "yes".
- **Save as a file** if you can write files.
- **Copy-paste:** always available, formatted for the destination if the
  user named one.

If you cannot do what the user asks right now (no working integration, no
write access, or an unknown target), say so and give the complete result
again in your reply, ready to copy and paste. Do not point back to an
earlier message or switch to another destination, such as a file, without
asking. Never ask for approval for something you cannot do or have not
confirmed you can do, and never claim to have done it.

## Review mode (mode C)

1. Read the existing report in full, and the underlying data if provided.
2. Check it against `references/report-checklist.md`, especially the
   common ways reports mislead. If the data is provided, check that the
   report's figures match it.
3. Respond with:
   - A one-line verdict: *ready to share*, *needs minor fixes*, or *needs
     rework*.
   - The specific problems found, most important first, each with a
     concrete suggestion. Report at most 7 problems in detail; summarize the
     rest in one line.
   - Corrected wording for the most important problems, using only
     information in the report or the data. Mark anything you could not
     fill as `[TO CLARIFY: …]`.
   - Open questions for the author.
4. Do not rewrite the whole report unless the user asks. Keep the feedback
   constructive: the goal is a report the reader can trust.
