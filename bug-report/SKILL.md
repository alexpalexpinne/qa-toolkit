---
name: bug-report
description: >
  Guides testers and end users through writing clear, actionable defect
  reports: drafting a new report through a short interview, turning the
  current conversation into a report, reviewing an existing report, or
  configuring persistent report defaults. Use only when the user explicitly
  invokes this skill or asks for it by name.
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
3. **One defect per report.** If the user describes several problems, list
   them with short labels and write a separate report for each, one at a
   time (see *Several bugs* in Step 3). Never silently drop one.
4. **Draft early, ask little.** Ask at most three questions at a time, and only
   about gaps that matter for reproducing or prioritizing the defect. Count
   each question separately, even when several share one number. Three is a
   maximum, not a target: when the input already covers the essentials,
   write the report right away and ask only about what would change
   reproduction or severity, which is often nothing. The limit applies to
   questions asking for an immediate reply; the draft's *Open questions*
   may list all unresolved items. Prefer showing a draft with gaps marked
   over a long interview. Ask numbered questions in the normal chat reply,
   after the draft if there is one, and wait for the user's next message.
   Do not use separate input panels or forms for them.
5. **Use plain language.** Avoid jargon when talking to the user. When you ask
   for something technical (a version number, a log), tell them where to find
   it and why it helps.
6. **Protect sensitive data.** Use one of three modes:
   - **Redact** (default): remove or mask passwords, tokens, API keys, other
     credentials, personal data, and customer data everywhere in your reply.
   - **Preserve:** keep the personal or customer data the report needs, such
     as the account email or order ID that reproduces the problem. Mask
     credentials and everything else.
   - **Include all:** keep every value the user supplied, including
     credentials such as a test account's password.

   Use Preserve or Include all only when the user explicitly chose it, in
   their personal preferences for this report's destination or in their
   message for this report. A choice for one destination does not apply to
   another. **Check the team conventions before choosing a mode.** If they
   forbid Preserve or Include all (for example "Always redact"), use Redact,
   even when the user's saved preferences or their message ask for another
   mode, and tell the user that the team's rule applies. This is the one
   case where team conventions win over what the user says in the
   conversation. Kept values appear
   only in the report itself, never in your commentary. When a report keeps
   sensitive values, list them by type and location before delivering it
   (for example "This report includes a password in Steps, step 2"). Tell
   the user what you masked by type and location only. Never repeat a
   masked value anywhere in your reply, even if it looks fake or like test
   data.
7. **Never submit anything without confirmation.** Filing an issue publishes
   it. Always show the final report and get an explicit "yes" first.
8. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Use the report language explicitly requested for this report; otherwise
   follow team conventions, personal preferences, then the user's language.
   Do not ask about it during the interview. Quote error messages, UI labels,
   log text, and anything the user entered (search terms, input values,
   product names) exactly as supplied, with the same spelling and case:
   do not translate, pluralize, or correct them, except for masking
   required by rule 6. Improve the surrounding prose instead, for example
   "results for the search `Tröja`" rather than a translated or plural form.
   If the report is in a different language, add a translation in
   parentheses after quoted messages and labels.
   Translate the template's headings and labels into the report language,
   keeping the structure, unless the team's tracker expects them in a
   specific language. Write dates as `YYYY-MM-DD` and include the time zone
   with any time.

## Before you start: settings

Two optional files change this skill's defaults. Read them if they exist;
do not search elsewhere for settings.

- **Team conventions:** `references/team-conventions.md` in this skill.
  Ignore its *Example* section; it is never applied. If the placeholder line
  is still in the file, there are no team conventions. They decide what the
  report must contain: for example the report language, severity scale,
  required fields, template, or which tracker and project to use.
- **Personal preferences:** `.config/bug-report/preferences.md` in the
  user's home folder. They record how this user works: destination,
  delivery method, report language when the team sets none, and
  sensitive-information handling.

Precedence, highest first: what the user says in the conversation (for that
report only, without changing saved settings), team conventions, personal
preferences, this skill's defaults. One exception: a team rule that forbids
a sensitive-data mode wins over everything, including the user's message
(core rule 6). The core rules above always apply.

If you need to check the project for an issue template or other
instructions, look only in the current directory and its parent
directories, not in neighboring projects.

If the user asks to set up or change their defaults (for example by
invoking the skill with `setup`), follow `references/setup.md`. Otherwise
never hold up a report for setup: when no personal preferences exist, start
the report straight away, and after delivering it, offer in one sentence to
save the choices used as defaults. Make that offer at most once per
conversation.

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

### Several bugs

1. List the problems with short labels. Ask which to start with, or say
   which one you will start with and why, based on what is known.
2. Work on one bug at a time. Put a heading naming the bug above its
   questions, ask only about that bug, and keep each answer with the bug it
   concerns. If it is unclear which bug an answer belongs to, ask.
3. When the current report is drafted, name the next bug and continue until
   every bug has its own report, unless the user stops or skips one. Keep
   track of which are drafted and which remain.

Moving on to the next draft needs no approval; filing each report does
(rule 7).

## Step 4: Write the report

- Choose the template in this order: one the user provides; one named in the
  team conventions; one that exists in the project (for example an issue
  template in the repository); otherwise `references/template.md`.
- Use the destination named for this report, otherwise the one in the team
  conventions or personal preferences, otherwise general Markdown.
- Format for how the report will be delivered, unless the user or team
  conventions specify a format:
  - **Copy-paste where your reply is shown rendered** (formatting survives
    copying): show the report rendered, not inside a code block.
  - **Copy-paste from a plain-text display**, such as a terminal, where
    copying loses formatting: put the report in one code block so the user
    copies the raw Markdown. Tracker editors such as GitHub's and Jira's
    accept pasted Markdown.
  - **Filing through an integration:** use the format it expects. For
    example, Jira's REST API v3 takes Atlassian Document Format, not
    Markdown.
- For Jira, use bold section headings such as **Steps to reproduce** instead
  of Markdown headings (`#`, `##`). For any tracker, keep the title or
  Summary field plain text.
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
the current environment, starting with the preferred delivery method. If a
preferred integration is unavailable, provide copy-paste output and explain
that limitation; do not claim the report was filed.

- **Issue tracker** (GitHub, Jira, Azure DevOps, or similar): only if you have
  a working integration or command-line tool for it. Confirm the project or
  repository (even if the team conventions name a default), show exactly
  what will be submitted, and wait for explicit
  approval. After filing, give the user the link.
- **File:** save as a markdown file if you can write files.
- **Copy-paste:** always available. Output one continuous report, formatted
  as described in Step 4.

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
