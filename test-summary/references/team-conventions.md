# Team conventions

This file is for your team's shared rules. The skill reads it before every
report, and anything written here takes precedence over the skill's
defaults. The skill's core rules (no invented results, showing the whole
picture, protecting sensitive data, confirming before publishing) always
apply.

It ships empty. Replace the placeholder below with your conventions, or leave
it as is to use the defaults. The skill never writes to this file.

<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->

---

## Example (for reference only, not applied)

Everything below this line is an example and is ignored by the skill.

```markdown
## Language
Reports are written in English.

## Audience
Completion reports go to the release manager and product owners. Keep the
summary to three sentences.

## Exit criteria (release testing)
- All P1 tests run.
- At least 95 % of P1 tests passed.
- No open defects with severity S1 or S2.
- Every S3 defect has an owner and a decision (fix or accept).

## Severity scale
S1 (production down or data loss), S2 (major function broken, no
workaround), S3 (impaired, workaround exists), S4 (cosmetic).

## Data sources
- Results: the release's Xray Test Plan (for example SHOP-TP-12), exported
  as CSV. Its status column shows each test's latest result across all
  executions.
- Defects: Jira search
  `project = SHOP AND type = Bug AND fixVersion = "<release>" AND statusCategory != Done`,
  exported as CSV.
- Severity is the custom field `Severity`. The `Priority` column is
  scheduling priority, not severity.

## Outcome names (Xray)
- PASSED → passed
- FAILED → failed
- ABORTED → failed
- BLOCKED → blocked
- TODO, EXECUTING → not run

## Counting
Count each test once by its latest result in the test execution.

## Recommendation terms
Go / Go with accepted risks / No-go. The release manager decides.

## Publishing
Completion reports go to Confluence, space QA, under "Release reports".
```
