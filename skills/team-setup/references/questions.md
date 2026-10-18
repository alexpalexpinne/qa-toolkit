# Questions for each section

Ask at most three questions per reply, starting with the ones marked
**first**. Skip any the user has already answered. Every answer can be
"use defaults" or "skip", which leaves the rule out.

## General

- **First:** Which language should reports, reviews, and test cases be
  written in? Or should they follow the language of each requirement or
  message?
- **First:** Which tracker and project do you use for defects and
  requirements (for example Jira project SHOP, GitHub repository, Azure
  DevOps)?
- **First:** Which severity scale do you use, and what does each level mean?
- Which test management tool do you use, if any?
- Do you use terms that must always mean the same thing (for example
  "customer" versus "user")?
- Where are test users and test data kept? (Record where, never the
  passwords.)

## Which skills

- Which of these does your team use: reviewing requirements, test cases,
  test data, bug reports, test summaries?

## review-requirements

- **First:** How are requirements organized (stories, use cases, epics,
  high-level requirements), and where do they live?
- **First:** What do "must", "should", and "may" (or the words in your
  language) mean in your requirements?
- In which format should proposed acceptance criteria be written (for
  example Given/When/Then, or plain sentences)?
- Is there anything every review must check (for example accessibility or
  data retention)?

## test-cases

- **First:** Which format do you use: step tables or Given/When/Then? With
  English or translated keywords?
- **First:** What ID scheme and title pattern do test cases follow?
- **First:** What priority scale do you use?
- Which fields are required on every test case (for example component or
  test level)?
- How do you export existing test cases (tool and columns)?

## test-data

- **First:** Which markets or countries must test data cover?
- **First:** How do you mark test data so it can be found and removed (for
  example a `TEST-` prefix in a last name)?
- **First:** Where are your test cards, test accounts, or test identity
  numbers listed? (Record where, never the values if they are secret.)
- Which file formats do imports need (delimiter, encoding)?
- How many rows may be pasted before a generator should be used?

## bug-report

- **First:** Which fields are required in a report (for example component,
  build number, test case ID)?
- **First:** How should sensitive data be handled: always redact, or may
  reports for a named tracker keep the personal data (Preserve) or also the
  test credentials (Include all) needed to reproduce a problem, by default
  or only when someone asks?
- Is there a report template or issue type to use?
- How should people search for duplicates (for example a tracker query)?
- Where do people find the app version and logs?

## test-summary

- **First:** What are your exit criteria for a test round or release?
- **First:** How do your test tool's statuses map to passed, failed,
  blocked, and not run?
- **First:** Which recommendation terms do you use, and who decides?
- How is each test counted when it was run more than once?
- Who reads the reports, and where are they published?
