# QA Toolkit team conventions

<!--
Save this file as `.qa-toolkit/conventions.md` at the root of your project
and commit it, so everyone on the team uses the same rules. The team-setup
skill can write it for you. Every QA Toolkit skill reads the *General*
section and its own section. An empty section means "use the skill's
defaults". Keep the section headings exactly as they are, in English, even
if you write the content in another language: the skills look for these
names.

Skills write to this file only when you ask them to and approve the draft.
Their core rules (no invented facts, protecting sensitive data, confirming
before publishing) always apply. Don't put passwords, tokens, or real
customer data in this file.

The *Example* section at the end is never applied. Delete it when you have
filled in your own conventions.
-->

## General

<!-- Rules for every skill: languages, tracker and project, severity scale,
terminology, and where test users and test data live. -->

## review-requirements

<!-- How requirements are organized, obligation words, acceptance criteria
format, things to always check. -->

## test-cases

<!-- Format, ID scheme, title pattern, priority scale, required fields,
test management tool, and how existing tests are exported. -->

## test-data

<!-- Markets, test data marker, test accounts and test cards, file formats,
volume limits. -->

## bug-report

<!-- Tracker fields, required fields, duplicate search, how reports are
delivered, sensitive-data rules (for example "Always redact", or "Preserve
in Jira SHOP"), where to find versions and logs. -->

## test-summary

<!-- Exit criteria, outcome names in your test tool, counting rule,
recommendation terms, audience, where reports are published. -->

---

## Example (for reference only, not applied)

```markdown
## General
- Reports, reviews, and test cases are written in English. Error messages
  and UI texts are quoted in their original language.
- Tracker: Jira, project SHOP. Test management: Xray in the same project.
- Severity: S1 (production down or data loss), S2 (major function broken,
  no workaround), S3 (impaired, workaround exists), S4 (cosmetic).
- Test users are listed on the wiki page "Test accounts". Refer to them by
  role ("standard user", "admin"), never by real names.

## review-requirements
- Stories link their epic; high-level requirements are `HLR-nnn` in
  Confluence.
- "must" is mandatory, "should" is recommended, "may" is optional.
- Every new screen must state its accessibility requirements.

## test-cases
- Given/When/Then with English keywords.
- IDs: `<story key>-TC-<two digits>`, for example SHOP-142-TC-01.
- Priority: P1 (every release), P2 (when the area changes), P3 (when time
  allows).

## test-data
- Markets: Sweden, Norway, Germany, United Kingdom.
- Every customer's last name starts with `TEST-`; order references start
  with `QA-`.
- Payment cards: only the test cards on the wiki page "PSP test cards".

## bug-report
- Issue type Bug; component is required (Checkout, Search, Account, Admin).
- Always redact. Preserve and Include all are not allowed, even on request.

## test-summary
- Exit criteria for release testing: all P1 tests run; at least 95 % of P1
  tests passed; no open S1 or S2 defects.
- Xray outcomes: PASSED → passed; FAILED, ABORTED → failed; BLOCKED →
  blocked; TODO, EXECUTING → not run.
- Recommendation terms: Go / Go with accepted risks / No-go. The release
  manager decides.
```
