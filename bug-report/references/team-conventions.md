# Team conventions

This file is for your team's shared rules. The skill reads it before every
report, and anything written here takes precedence over the skill's defaults
and over each user's personal preferences. The skill's core rules (no
invented facts, protecting sensitive data, confirming before filing) always
apply.

It ships empty. Replace the placeholder below with your conventions, or leave
it as is to use the defaults. The skill never writes to this file. Personal
defaults, such as delivery method, are saved separately in each user's home
folder (see `setup.md`).

<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->

---

## Example (for reference only, not applied)

Everything below this line is an example and is ignored by the skill.

```markdown
## Language
Reports are written in English, even when the tester writes in another
language. Error messages are quoted in their original language.

## Tracker
- Jira, project key SHOP.
- Issue type: Bug. Component is required.
- Valid components: Checkout, Search, Account, Admin.
- Duplicate search: `project = SHOP AND type = Bug AND statusCategory !=
  Done AND text ~ "<keywords>"`.

## Severity
We use our own scale instead of the default:
- S1: production down or data loss
- S2: major function broken, no workaround
- S3: function impaired, workaround exists
- S4: cosmetic

## Required fields
In addition to the default template:
- Test case ID, if the defect was found while running a test case.
- Build number, from the footer of the test environment.

## Sensitive information
Always redact. Personal Preserve and Include all preferences do not apply.

## Where to find things
- App version: Settings → About.
- Logs (desktop app): Help → Export diagnostics.
```
