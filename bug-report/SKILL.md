---
name: bug-report
description: >
  Guides testers and end users through writing clear, actionable defect
  reports: drafting a new report through a short interview, turning the
  current conversation into a report, or reviewing and improving an existing
  report. Use only when the user explicitly invokes this skill or asks for it
  by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Bug Report

Help the user produce a defect report that a developer can act on without
coming back with follow-up questions. The users are testers and end users,
not necessarily technical people.

## Core rules

These apply in every mode and override everything else in this file.

1. **Never invent facts.** Do not guess steps, versions, environments, error
   messages, or frequencies. If something is unknown, write `Unknown` in the
   report and list it under *Open questions*. A short honest report is better
   than a complete-looking fabricated one. This includes inferences: record
   what was stated, and do not derive facts by calculation, interpretation,
   or context clues (for example an item price from a total, a frequency
   from "I just noticed it", or a product area from a project key). Never
   say you checked, looked at, or found something unless you actually did
   in this session.
2. **Keep observation and interpretation apart.** Record what the user saw and
   did. If the user (or you) has a theory about the cause, put it under
   *Additional notes*, clearly labeled as a hypothesis.
3. **One defect per report.** If the user describes several problems, say so
   and offer to write separate reports.
4. **Draft early, ask little.** Ask at most three questions at a time, and only
   about gaps that matter for reproducing or prioritizing the defect. Three
   is a maximum, not a target: when the input already covers the essentials,
   write the report right away and ask only about what would change
   reproduction or severity, which is often nothing. The limit applies to
   questions asking for an immediate reply; the draft's *Open questions*
   may list all unresolved items. Prefer showing a draft with gaps marked
   over a long interview.
5. **Use plain language.** Avoid jargon when talking to the user. When you ask
   for something technical (a version number, a log), tell them where to find
   it and why it helps.
6. **Protect sensitive data.** Before including logs, screenshot descriptions,
   URLs, or pasted text, remove or mask passwords, tokens, API keys, personal
   data, and customer data. Tell the user what you masked by type and
   location only (for example "the email address on line 1, the token in the
   Authorization header"). Never repeat an original value anywhere in your
   reply, including commentary, and even if it looks fake or like test data.
7. **Never submit anything without confirmation.** Filing an issue publishes
   it. Always show the final report and get an explicit "yes" first.
8. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Write the report in the language the team or tracker uses; if
   that is unknown, ask once, and default to the user's language. Quote error
   messages, UI labels, and log text exactly as they appear, untranslated,
   except for masking required by rule 6; if the report is in a different
   language, add a translation in parentheses.
   Translate the template's headings and labels into the report language,
   keeping the structure, unless the team's tracker expects them in a
   specific language. Write dates as `YYYY-MM-DD` and include the time zone
   with any time.

## Before you start: team conventions

Read `references/team-conventions.md`. Ignore its *Example* section; it is
never applied. If the placeholder line is still in the file, there are no
team conventions. Otherwise its conventions take precedence over the
defaults in this skill wherever they conflict: for example the report
language, severity scale, required fields, or which tracker and project to
use. Conventions the user
states in the conversation take precedence over the file. The core rules
above always apply.

## Step 1: Choose the mode

Decide from what the user provided. If it is unclear, ask which one they want.

| Mode | When | Start with |
|------|------|------------|
| **A. New report** | The user describes a problem from scratch | Step 2, then the interview |
| **B. From conversation** | The problem was already discussed or investigated earlier in this conversation | Extract everything known, then Step 2 |
| **C. Review** | The user pastes or points to an existing report | Go to *Review mode* below |

## Step 2: Gather evidence yourself

First establish **what the report is about**: which application or product,
and where it ran (the user's device, a test environment, a website). Ask if it
is not clear. Do not assume that the current folder, project, or machine you
have access to is the application being reported on.

Then collect what you can. Skip anything you cannot do; never pretend you did
it.

- **Attachments:** if the user attached screenshots, recordings, or files,
  read them and describe what they show. If the user mentions a file
  without attaching it, ask them to attach it or give its path. Never
  search the file system for it.
- **Local evidence:** if you can read files or run commands, and the affected
  application is on the same machine, ask before collecting anything beyond
  what the user pointed you to. Say what you want to look at and why (for
  example "the app's log folder, to find the error message"). Then collect
  only what is relevant: version, platform, recent log lines around the
  problem, error output.
- **Duplicates:** only if you can search an issue tracker *and* the tracker
  and project are known, either confirmed by the user or named in the team
  conventions. Mention likely
  duplicates before writing a new report. Otherwise skip this; never search a
  tracker or project you guessed.

Tell the user briefly what you collected, so they can correct it.

## Step 3: Fill the gaps (modes A and B)

Compare what you know against the template in `references/template.md`.
Ask only about missing items that matter most, in this priority order:

1. What exactly happened (the actual result, including any error text)
2. What the user expected to happen instead
3. The steps that lead to the problem
4. Whether it happens every time, sometimes, or happened once
5. The environment (device, browser/app, version) if not already collected
6. The impact: who is affected and whether there is a workaround

Turn vague words into concrete questions:

| The user says | Ask |
|---------------|-----|
| "It doesn't work" | "What did you see on the screen? Was there an error message?" |
| "It crashes" | "Did the app close, freeze, or show an error? What were you doing right before?" |
| "Sometimes" | "Roughly how often: every few tries, or once in a while? Anything different when it happens?" |
| "It's slow" | "About how long does it take, and how long would you expect?" |
| "Like before" / "as usual" | "When did it last work as expected? Did anything change since then?" |

If the user does not know an answer, accept that, mark it `Unknown`, and move
on. Do not push more than once on the same item.

## Step 4: Write the report

- Choose the template in this order: one the user provides; one named in the
  team conventions; one that exists in the project (for example an issue
  template in the repository); otherwise `references/template.md`.
- Write a specific title: *where* + *what goes wrong* + *under what condition*.
- Write reproduction steps as numbered, minimal actions, starting from a known
  state.
- Omit optional sections that do not apply. Do not fill fields with "N/A".

## Step 5: Check quality

Run through `references/quality-checklist.md`. Check your *whole* reply,
not only the report: commentary, notes on what you masked, and questions
must follow the core rules too. Fix what you can from known information. Anything still missing goes under *Open questions*, and if it is
important, ask the user once more before finishing.

## Step 6: Deliver

Show the finished report to the user. Then offer the destinations available in
the current environment:

- **Issue tracker** (GitHub, Jira, Azure DevOps, or similar): only if you have
  a working integration or command-line tool for it. Confirm the project or
  repository (even if the team conventions name a default), show exactly
  what will be submitted, and wait for explicit
  approval. After filing, give the user the link.
- **File:** save as a markdown file if you can write files.
- **Copy-paste:** always available. Output the report in a single block,
  formatted for the target tracker if the user named one.

**Attachments:** many integrations and command-line tools cannot upload
images or files. Refer to attachments by file name in the report. If you
cannot upload them yourself, list exactly which files the user must attach
by hand and where (for example "after the issue is created, drag
`checkout-error.png` into a comment"). Never let screenshots or logs the
report relies on be silently left out.

## Review mode (mode C)

1. Read the existing report in full.
2. Evaluate it against `references/quality-checklist.md`.
3. Respond with:
   - A one-line verdict: *ready to submit*, *needs minor fixes*, or *needs
     more information*.
   - The specific problems found, most important first, each with a concrete
     suggestion.
   - An improved version of the report, using only information present in the
     original or provided by the user. Mark anything you could not fill as
     `Unknown`.
   - The questions the author should answer to complete it.
4. Keep the feedback constructive. The goal is a better report, not a grade.
