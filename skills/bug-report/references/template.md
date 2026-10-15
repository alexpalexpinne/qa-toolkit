# Default defect report template

Teams can replace this file with their own format. Keep the section names
stable if possible, since `quality-checklist.md` refers to them.

Sections marked *(optional)* are left out when they do not apply.

Headings are shown in English. Translate them into the report language,
keeping the same structure.

The Markdown headings below define the report's sections. Format the
finished report for its destination and delivery method as described in
Step 4 of `../SKILL.md`; for Jira, that means bold section headings such as
**Steps to reproduce** instead of `##` headings.

---

```markdown
## Title
<Where> – <what goes wrong> <under what condition>

## Summary
One or two sentences: what is wrong and who it affects.

## Environment
- Application / product:
- Version or build:
- Platform (OS, device, browser and version):
- Language and region settings: (optional)
- Account type / role / test data used: (optional)
- Test environment (e.g. production, staging, test): (optional)
- Observed at: YYYY-MM-DD HH:MM, time zone (optional, helps match logs)

## Steps to reproduce
1. Start from <known state, e.g. "logged in as a standard user on the start page">
2. ...
3. ...

## Expected result
What should have happened.

## Actual result
What actually happened. Include the exact error message, if any, in its
original language (with a translation in parentheses if needed).

## Reproducibility
Always / Intermittent (about X of Y attempts) / Happened once / Not tried again

## Severity
Critical / High / Medium / Low – with one sentence explaining why.

## Evidence (optional)
Screenshots, recordings, log excerpts, stack traces. Sensitive data masked
as described in core rule 6.
Refer to attached files by name, e.g. `checkout-error.png`.

## Workaround (optional)
A way to avoid the problem, if one is known.

## Additional notes (optional)
When it started, recent changes, related issues, hypotheses about the cause
(clearly labeled as hypotheses).

## Open questions (optional)
Information that is still unknown and who might be able to provide it.
```

---

## Severity guide

Severity describes the **impact** of the defect. Priority (how soon to fix it)
is decided by the team and is not part of this report unless the team's own
template asks for it.

| Severity | Meaning | Example |
|----------|---------|---------|
| **Critical** | Data loss, security problem, or a core function completely unusable with no workaround | Payments fail for all users |
| **High** | A major function is broken or wrong; a workaround is difficult or unavailable | Exported reports contain wrong totals |
| **Medium** | A function is impaired but a reasonable workaround exists | Search ignores filters, but manual browsing works |
| **Low** | Cosmetic or minor inconvenience | Misaligned button, typo in a label |

If the user is unsure, suggest a severity with a short reason and let them
confirm or change it.

## Title examples

| Weak | Strong |
|------|--------|
| Login broken | Login – "Invalid session" error after password reset on mobile app |
| Upload doesn't work | File upload – files over 10 MB fail silently in Firefox |
| Bug in report | Monthly report – totals exclude transactions from the last day of the month |
