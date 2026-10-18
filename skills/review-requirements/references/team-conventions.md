# Team conventions

This file is for your organization's own rules. The skill reads it before
every review, and anything written here takes precedence over the skill's
defaults.

For a team, the better place is a shared `.qa-toolkit/conventions.md` file
in your project, which every skill in QA Toolkit reads and which survives
plugin updates; see the README. Use this file only if you maintain your
own copy of the skill. It ships empty. Replace the placeholder below with your conventions, or leave
it as is to use the defaults.

<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->

---

## Example (for reference only, not applied)

Everything below this line is an example and is ignored by the skill.

```markdown
## Requirement structure
- Epics and user stories are in Jira, project SHOP. Every story links its
  epic.
- High-level requirements are in Confluence, with IDs `HLR-nnn`. Each story
  names the HLR it implements.
- Use cases follow our template: actor, preconditions, main flow,
  alternative flows, end state.
- Stories exported from Jira as CSV have the columns `Issue key`,
  `Summary`, `Description`, and `Acceptance Criteria` (a custom field).

## Language
Requirements are written in German. Reviews are written in German.

## Obligation words
- "muss": mandatory
- "soll": recommended; deviations must be justified
- "kann": optional

## Acceptance criteria format
Given/When/Then with English keywords, German content.

## Terminology
- "Kunde" always means the paying organization, never an individual user.
- "Nutzer" means an individual person with a login.

## Always check
- Every new screen must state its accessibility requirements.
- Every feature that stores personal data must name the retention period.
```
