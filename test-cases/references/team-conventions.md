# Team conventions

This file is for your organization's own rules. The skill reads it before
every run, and anything written here takes precedence over the skill's
defaults. The skill's core rules (no invented expected results, fake test
data only, confirming before publishing) always apply.

It ships empty. Replace the placeholder below with your conventions, or leave
it as is to use the defaults.

<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->

---

## Example (for reference only, not applied)

Everything below this line is an example and is ignored by the skill.

```markdown
## Language
Test cases are written in English.

## Format
Given/When/Then with English keywords. One scenario per test case.

## IDs
<story key>-TC-<two-digit number>, e.g. SHOP-142-TC-01.

## Titles
<Area> | <scenario> | <expected outcome>, e.g.
"Checkout | expired card | payment rejected".

## Placeholders
Technical placeholders in our tests: <ENV>, <BASE_URL>, <TODAY>.
Keep them as they are.

## Priority
P1 (must run every release), P2 (run when the area changes), P3 (run when
time allows).

## Tool
Xray in Jira, project SHOP. Test cases are created as issue type "Test".

## Required fields
- Component (Checkout, Search, Account, Admin)
- Test level: UI, API, or Integration

## Test environment
Test users are listed on the wiki page "Test accounts". Refer to them by
role ("standard user", "admin"), never by real names.

## Always include
- At least one accessibility check (keyboard only) for every new screen.
```
