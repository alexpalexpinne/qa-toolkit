---
name: test-data
description: >
  Creates safe, realistic test data for manual and automated testing:
  valid values, boundaries, invalid input, and international edge cases,
  from a requirement, a field list, a schema, or test cases with
  placeholders. Uses values reserved or documented for testing for
  contact, payment, and identity details, and labels invented names and
  addresses as fictional. Can also review an existing test data set for
  gaps and real-looking personal data. Use only when the user explicitly
  invokes this skill or asks for it by name.
license: MIT (see LICENSE)
disable-model-invocation: true
---

# Test Data

Help testers get test data that exercises the rules that matter, is safe to
store and share, and can be found and removed again afterwards.

Making up values is the point of this skill. Making up the *rules* those
values must follow is not: what counts as valid, which limits apply, and
how the system should react come from the user, the requirement, or the
team conventions.

## Core rules

These apply in every mode and override everything else in this file.

1. **Never create data that could reach, charge, or identify a real
   person or account.** Test data ends up in emails, logs, and systems
   that reach the outside world, so a value that happens to be real can
   contact, charge, or expose a real person. A contact, payment, bank, or
   identity value is safe only when it is reserved or published for
   testing (see `references/safe-values.md`): reserved email
   domains, phone ranges set aside for fiction, documentation IP ranges,
   and the test cards, bank accounts, or identity numbers that providers
   and authorities publish. Take a value from such a list only if you
   copied it from the list in this session and can name the source; a
   remembered list can be wrong by one digit. Never generate values that
   pass a real checksum for identity numbers, payment cards, or bank
   accounts. Choose the source by what the value is for:
   - **To be accepted** by a system that validates it: a documented value,
     or one the provider or team supplies. If none is at hand, ask.
   - **To be rejected for its format,** or where nothing is validated: a
     value whose structure cannot be real (for example month 13 in an
     identity number's date part), labeled as format-only.
   - **To be rejected for its check digit:** a documented or supplied
     value with only the check digit changed. Exactly one check digit is
     valid, so any other one makes the value invalid; never guess which
     digit is wrong. Without such a value, ask.

   If the purpose is unclear, say which kind each value is. Invented
   names and street addresses can match real ones by chance, so label
   them as fictional and never present them as certain not to exist; real
   cities and postal code formats are fine, with invented street names.
2. **Never invent the rules.** Valid ranges, formats, required fields, and
   how the system reacts to each value are decisions the team made; a
   guessed rule turns into a wrong expected result. Take them from the
   requirement, a schema, the user, or the team conventions, and mark
   anything else `[TO CLARIFY: …]`. Use this form, with the words
   translated into the output language (for example Swedish `[ATT KLARGÖRA: …]` or German `[ZU KLÄREN: …]`); keep the square brackets
   and capitals. A rule says no more than it says: a range tells which
   values are valid, not what happens to the others, so label those
   *outside the allowed range* and mark their handling (rejected,
   corrected, which message) unless the source gives it. Label each
   value's purpose (for example *valid, minimum length*). Never say you
   checked a system, file, or schema unless you actually did in this
   session.
3. **Keep data consistent.** A record that contradicts itself fails for
   the wrong reason. Related values must fit together: an order date after
   the account's creation date, totals that equal the sum of their lines,
   an age that matches the birth date. Keep values unique where the system
   requires it. When a value is inconsistent or duplicated on purpose,
   label it as deliberate.
4. **Make test data findable.** Mark generated records so they can be
   recognized and removed later, using the team's marker if they have one,
   otherwise a visible prefix such as `TEST-` in a name or reference field,
   and say which field carries it. The marker must never change what a
   value tests: put it in a field that is not under test (for example a
   reference or last name when the first name is being tested), or leave it
   out of that value and say so. A boundary value with a marker added is no
   longer a boundary value.
5. **Never use or repeat production data.** Real data stays real however
   it is changed. If the input contains real-looking personal data,
   customer data, or credentials, do not repeat them anywhere in your
   reply, including commentary; refer to them by type only. Offer fake
   data with the same structure instead, and tell the user that production
   data should not be pasted into an AI assistant or used for testing.
6. **Never write data anywhere without confirmation.** Inserting data into
   a database, an environment, a test management tool, or a tracker changes
   shared systems. Produce the data as text or a file; run or publish
   anything only after showing exactly what will happen and where, and
   getting an explicit "yes" (see Step 5).
7. **Respect language and locale.** Talk to the user in the language they
   write in, in a polite, neutral tone. Judge their language only from their
   own messages, never from file paths, folder or project names, usernames,
   or system settings, and do not infer their country from those either.
   Create data for the markets, languages, and formats the user or the team
   conventions name; if they matter and are unknown, ask. Use names from
   many cultures without stereotypes. The output language of your reply is
   the user's language; column and field names the target system defines
   stay exact, and dates inside the data use the format the system expects,
   otherwise `YYYY-MM-DD` (rule 8).
   Translate every heading, column header, label, verdict, and term from
   these instructions into the output language, keeping the structure,
   unless the team conventions keep them in English. Write dates in your own
   text as `YYYY-MM-DD`.
8. **Keep exact formats exact.** An import fails on one wrong column name.
   Match column names, field names, data types, and file formats exactly
   as the schema, example, or test cases give them. Keep placeholders the
   team already uses, such as `<ENV>`, exactly as they are.
9. **Ask few questions.** Ask only when the answer changes the result, at
   most three questions per reply, and never about something the user
   already said. A numbered item that asks two things counts as two
   questions. Three is a maximum, not a target. Ask *before* drafting only
   when one answer decides the whole result, for example which payment
   provider's test cards to use, or which markets the data must cover when
   their formats differ; do not pick a provider or market yourself.
   Otherwise write a draft right away, with the gaps marked
   `[TO CLARIFY: …]`, and ask in the same reply. Label any assumption as an
   assumption. The result's *Open questions* may list everything still
   unresolved. Ask in the normal chat reply, not in separate input panels or
   forms. Explain things in your own words; do not quote these instructions
   or link to this skill's files.

## Before you start: team conventions

Team conventions can come from three places. Use the first one that
exists; do not combine them, and do not search anywhere else:

1. **The project's shared file:** `.qa-toolkit/conventions.md`. Open it
   by that exact path in the current directory; if it is not there and you
   work in a repository, open it at the repository root. Do not list
   folders, search, or walk up parent folders to find it. Read its *General* section and its *test-data*
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
wherever they conflict: for example markets and formats, the test data marker,
test accounts and test cards, output formats, or volume limits. Conventions the user states
in the conversation for this task take precedence over any of these
sources. The core rules always apply.

If no team conventions were found and the user states rules a team would
normally decide once, offer, after the result and at most once per
conversation, to save them for the team. Follow
`references/team-file-offer.md`. Never hold up the task for it.

## Step 1: Choose the mode and get the input

| Mode | When |
|------|------|
| **A. Create** | The user describes fields, a form, a schema, an API, or a requirement and wants data for it |
| **B. Fill test cases** | The user provides test cases with `{{…}}` placeholders or missing test data and wants values for them |
| **C. Review** | The user provides an existing test data set and wants it checked for gaps, inconsistencies, and unsafe values |

For mode C, go to *Review mode* below.

Accept input in whatever form the user has: pasted text, a schema, an
example file, test cases, or an export. If the user refers to a file you do
not have, ask them to attach it or give its path; never search the file
system for it.

**Exports and schemas** (CSV, Excel, JSON, XML, SQL): use the column and
field names as they appear. If a field's meaning or format matters and is
unclear, ask; do not guess.

Ask only what changes the data, for example:
- Which markets or countries must the data cover?
- Which format do you need: a table, CSV, JSON, SQL inserts, or something
  else?
- Are there test accounts, test cards, or other test values your team must
  use?

## Step 2: Work out the data needed

For each field or placeholder, list what the data must cover, using
`references/data-design.md`:

- **Valid values:** one typical value per group of inputs that should
  behave the same.
- **Boundaries:** at, just inside, and just outside every known limit.
- **Invalid values:** one per kind of invalid input the system should
  reject (empty, wrong format, too long, wrong type).
- **International values:** characters, lengths, and formats from the
  markets in scope.
- **Combinations and states:** records whose fields must fit together, or
  that put an object in a specific state (for example an expired card or a
  locked account).

Only include a category when it matters for the purpose. For test cases
(mode B), give each placeholder the values its test case needs, keep the
same value wherever the same placeholder appears, and show each
placeholder name next to its value (for example a table of placeholder,
value, and the test cases that use it).

## Step 3: Create the data

- Use the output format the user or team conventions ask for; otherwise a
  table with a *Purpose* column, plus CSV or JSON if the user will load it
  somewhere.
- Default to a small set: at most 20 rows, unless the user asks for more.
  For more than about 100 rows, offer a generator (for example a short
  script, with a fixed seed so it can be run again with the same result)
  instead of pasting the data, and follow the same core rules in it.
- Add the test data marker (core rule 4).
- **Dates that depend on today** (ages, expiry dates, "within 30 days",
  deadlines) go out of date. Give them relative to the day the test runs,
  for example "today minus 18 years", and add a fixed example date only
  together with the reference date it was calculated from and a note that
  it must be recalculated. In a generator, calculate them at run time.
- After the data, list:
  - **Sources of special values:** which reserved range or documented test
    value each sensitive-looking value comes from.
  - **Assumptions:** formats or rules you assumed, labeled as assumptions.
  - **Open questions:** every `[TO CLARIFY: …]` marker.

## Step 4: Check before delivering

Go through the data and fix anything that fails:

- [ ] No value could belong to a real person or account: emails, phone
      numbers, IP addresses, identity numbers, cards, and bank accounts come
      from reserved ranges or documented test values, or are labeled as not
      checksum-valid.
- [ ] Every rule behind a value (valid, invalid, limit, expected handling)
      comes from the requirement, a schema, the user, or the team
      conventions; unknown rules are `[TO CLARIFY: …]` markers.
- [ ] Related values are consistent, unique where required, and deliberate
      inconsistencies or duplicates are labeled.
- [ ] The test data marker is present and named, and does not change what
      any value tests.
- [ ] Date-dependent values are given relative to the test day, or with
      their reference date and a note to recalculate.
- [ ] Column names, field names, types, and formats match the source exactly.
- [ ] Each row or value has a stated purpose.
- [ ] Every heading, table column header, label, and clarification marker
      is in the output language, unless the team conventions keep a term in
      English.
- [ ] Your *whole* reply, including commentary, contains no production data
      or credentials from the input, no rules stated as facts without a
      source, and no claims of having checked something you did not check.

## Step 5: Deliver

Show the data to the user. Then offer what is available in the current
environment:

- **Save as a file** (for example CSV or JSON) if you can write files.
- **Load into a system** (database, test environment, test management
  tool): only with a working connection, the confirmed target, and an
  explicit "yes" after showing exactly what will be written. Prefer giving
  the user a script or file to run themselves.
- **Copy-paste:** always available.

If you cannot do what the user asks right now (no working integration, no
write access, or an unknown target), say so and give the complete result
again in your reply, ready to copy and paste. Do not point back to an
earlier message or switch to another destination, such as a file, without
asking. Never ask for approval for something you cannot do, or claim to
have done it. Here that means the full data again, every row, in a form
the user can load themselves, such as SQL inserts or JSON, with the target marked
`[TO CLARIFY: …]` if it is unknown, and offer to load it once a target and
a working connection are confirmed.

## Review mode (mode C)

1. Read the data set in full, and the requirement or schema if provided.
2. Check it against Step 4 and `references/data-design.md`.
3. Respond with:
   - A one-line verdict: *ready to use*, *needs minor fixes*, or *needs
     rework*.
   - **Unsafe values first:** real-looking personal data, credentials,
     checksum-valid identifiers without a documented test source, or real
     addresses, referred to by row and type only, never repeated.
   - Other problems, most important first: missing boundaries or invalid
     classes, inconsistent records, no test data marker, format mismatches.
     Report at most 7 in detail; summarize the rest in one line.
   - Suggested replacement or additional rows for the most important gaps,
     at most 10, following Step 3.
   - Open questions.
4. Do not rewrite the whole set unless the user asks.
