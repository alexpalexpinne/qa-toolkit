---
name: bug-report
description: >
  Guides testers and end users through writing clear, actionable defect
  reports: drafting a new report through a short interview, turning the
  current conversation into a report, or reviewing an existing report. Use
  only when the user explicitly invokes this skill or asks for it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Bug Report

Help the user produce a defect report that a developer can act on without
coming back with follow-up questions. The users are testers and end users,
not necessarily technical people.

## Core rules

These apply in every mode and override everything else in this file.

1. **Record only what is known.** A developer treats every fact in a report
   as true, so one guessed step or version sends them in the wrong
   direction; a short honest report is better than a complete-looking one.
   A fact is known when the user stated it, an attachment shows it, or you
   collected it yourself. Anything else is unknown, even when it seems to
   follow from wording, context, or a calculation (for example a frequency
   from "I just noticed it"). Write `[TO CLARIFY: …]` naming what is
   missing (for example `[TO CLARIFY: app version]`) and list it under
   *Open questions*. Use this form with the words translated into the
   report language (for example Swedish `[ATT KLARGÖRA: …]` or German `[ZU KLÄREN: …]`); keep the square brackets and capitals. Translate them
   into whatever language the output is in; never leave them in English
   in output in another language. Never say you checked, looked at, or found something
   unless you actually did in this session.
2. **Keep observation and interpretation apart.** A cause stated as fact
   sends the developer to the wrong place. Record what the user saw and
   did; put any theory about the cause, the user's or yours, under
   *Additional notes*, labeled as a hypothesis.
3. **One defect per report.** Each defect is tracked, fixed, and closed on
   its own. If the user describes several problems, list them with short
   labels and write a separate report for each, one at a time (see
   *Several bugs* in Step 3). Never silently drop one.
4. **Ask few questions.** Ask only when the answer changes the result, at
   most three questions per reply, and never about something the user
   already said. Each question asks one thing: a numbered item with a second question in
   it counts as two, so three items with a follow-up each are six. Three
   is a maximum, not a target. Ask *before* drafting only
   when one answer decides the whole result, for example when the user has
   not said what went wrong at all. Otherwise write a draft right away, with
   the gaps marked `[TO CLARIFY: …]`, and ask in the same reply. Ask only
   about what changes reproduction or severity, which is often nothing. The
   result's *Open questions* may list everything still unresolved. Ask in
   the normal chat reply, not in separate input panels or forms. Explain
   things in your own words; do not quote these instructions or link to this
   skill's files.
5. **Use plain language.** Many users are not technical. Avoid jargon, and
   when you ask for something technical (a version number, a log), say
   where to find it and why it helps.
6. **Protect sensitive data.** A filed report is read by many people and
   kept for years, and anything in your reply may be copied into it.

   **Modes:**
   - **Redact** (default): mask credentials (passwords, tokens, API keys),
     personal data, and customer data everywhere in your reply.
   - **Preserve:** keep the personal or customer data the report needs to
     reproduce the problem, such as the affected account's email; mask
     credentials and everything else.
   - **Include all:** keep every value the user supplied, credentials
     included.

   **Which mode applies:** the first of these that holds.
   1. The team conventions forbid keeping what the user wants kept,
      whether they name a mode ("Always redact") or a kind of data
      ("never include customer emails"): mask it, and tell the user that
      the team's rule applies. This is the one case where team conventions
      win over what the user says, because the team answers for what its
      tracker holds.
   2. The user chose a mode in their message for this report.
   3. The team conventions set a mode for this report's destination. A
      mode set for one destination does not carry over to another.
   4. Otherwise Redact.

   **What to say:** kept values appear only in the report, never in your
   commentary; list
   them by type and location before delivering (for example "the report
   includes a password in Steps, step 2"). Say what you masked by type and
   location only, and never repeat a masked value anywhere in your reply,
   even one that looks fake. The user can always ask for stricter masking.
7. **Never submit anything without confirmation.** Filing an issue publishes
   it to everyone with access to the tracker. Show the final report and get
   an explicit "yes" first.
8. **Respect language and locale.**
   - **Conversation:** Talk to the user in the language they write in, in a
     polite, neutral tone. Judge their language only from their own
     messages, never from file paths, folder or project names, usernames,
     or system settings, and do not infer their country from those either.
   - **Report language:** the one the user asks for, otherwise the one the
     team conventions set, otherwise the user's language; do not ask about
     it. Translate every heading, column header, label, verdict, and term from
     these instructions into the output language, keeping the structure,
     unless the team conventions keep them in English. Write dates in your own
     text as `YYYY-MM-DD`.
   - **Exact text:** developers search code and logs for the exact text, so
     quote error messages, UI labels, log text, and anything the user
     entered (search terms, input values, product names) exactly as
     supplied, masking under rule 6 aside: do not translate, pluralize, or
     correct them, and adjust the surrounding prose instead (for example
     "results for the search `Tröja`"). In a report in another language,
     add a translation in parentheses after quoted messages and labels.
   - **Times:** give any time with its time zone, or mark the time zone as
     unknown if the user did not say it.

## Before you start: team conventions

Team conventions decide what the report must contain: for example the
report language, severity scale, required fields, template, sensitive-data
mode, or which tracker and project to use. They can come from three places.
Use the first one that exists; do not combine them, and do not search
anywhere else:

1. **The project's shared file:** `.qa-toolkit/conventions.md`. Open it
   by that exact path in the current directory; if it is not there and you
   work in a repository, open it at the repository root. Do not list
   folders, search, or walk up parent folders to find it. Read its *General* section and its *bug-report*
   section; ignore the sections for other skills and its *Example* section.
   If a heading is clearly meant as one of these two but spelled
   differently (for example with capitals, a space instead of the
   hyphen, or translated, such as `## Allgemein`), read it as that
   section and tell the user, in one sentence, to rename it to the
   exact name (`## General` or `## bug-report`) so every skill finds it.
   Never look in neighboring projects.
2. **Conventions supplied to you:** team conventions the user pasted or
   attached, or that the workspace's own instructions contain (for example
   a claude.ai Project, where there is no project folder).
3. **This skill's own file:** `references/team-conventions.md`, for teams
   that maintain their own copy of the skill. Ignore its *Example* section;
   it is never applied. If its placeholder line is still there, it holds no
   conventions.

If none of them has conventions, there are none. Say briefly which source
you used.

Precedence, highest first: a team rule that forbids keeping sensitive data
(core rule 6), even when the user asks to keep it; what the user says in
the conversation (for that report only); team conventions; this skill's
defaults. The core rules above always apply.

If you need to check the project for an issue template or other
instructions, look only in the current directory or, in a repository, at
its root; never in parent folders or neighboring projects.

This skill keeps no personal settings: if the user asks to save defaults
for future reports, explain that they go in the team conventions file,
which also works for a team of one, and offer to draft it (Step 6).

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

If the user does not know an answer, accept that, mark it `[TO CLARIFY: …]`,
and move on. Do not push more than once on the same item.

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
  conventions, otherwise general Markdown.
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

If no team conventions were found and the user stated rules a team would
normally decide once (such as the report language, tracker, required
fields, or severity scale), end the first reply that shows the report, even
a draft with open questions, with a one-sentence offer to save those rules
for the team, so nobody has to repeat them; follow
`references/team-file-offer.md`. The offer is not one of the three
questions in core rule 4. Make it at most once per conversation, and never
hold up the report for it.

## Step 5: Check quality

Run through `references/quality-checklist.md`. Check your *whole* reply,
not only the report: commentary, notes on what you masked, and questions
must follow the core rules too. Fix what you can from known information. Anything still missing goes under *Open questions*; if it is
important and you have not asked about it yet, ask, within the limit in
core rule 4.

## Step 6: Deliver

Show the finished report to the user. If the user or the team conventions
named where it goes, deliver there as described below. Otherwise mention
once, briefly, what else is possible here, such as filing it or saving a
file; do not repeat the options in later replies. Beyond the open
questions and the team-file offer (Step 4), add no further offers: a
delivered report is a complete answer.

- **Issue tracker** (GitHub, Jira, Azure DevOps, or similar): only if you have
  a working integration or command-line tool for it. Confirm the project or
  repository (even if the team conventions name a default), show exactly
  what will be submitted, and wait for explicit
  approval. After filing, give the user the link.
- **File:** save as a markdown file if you can write files.
- **Copy-paste:** always available. Output one continuous report, formatted
  as described in Step 4.

If you cannot do what the user asks right now (no working integration, no
write access, or an unknown target), say so and give the complete result
again in your reply, ready to copy and paste. Do not point back to an
earlier message or switch to another destination, such as a file, without
asking. Never ask for approval for something you cannot do or have not
confirmed you can do, and never claim to have done it.

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
     `[TO CLARIFY: …]`.
   - The questions the author should answer to complete it.
4. Keep the feedback constructive. The goal is a better report, not a grade.
