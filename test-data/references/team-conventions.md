# Team conventions

This file is for your team's shared rules. The skill reads it before every
run, and anything written here takes precedence over the skill's defaults.
The skill's core rules (no data that could belong to real people, no
invented rules, no production data, confirming before writing anywhere)
always apply.

It ships empty. Replace the placeholder below with your conventions, or leave
it as is to use the defaults. The skill never writes to this file.

<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->

---

## Example (for reference only, not applied)

Everything below this line is an example and is ignored by the skill.

```markdown
## Markets
Sweden, Norway, Germany, United Kingdom. Every data set covers at least one
value per market where formats differ.

## Test data marker
Every customer's last name starts with `TEST-`, and every order reference
starts with `QA-`. A nightly job removes these from the test environments.

## Test values
- Payment cards: the test cards in our payment provider's documentation
  (wiki page "PSP test cards"). Never use other card numbers.
- Personal identity numbers: only from the authority's published test
  lists (wiki page "Test identities").
- Test users: `qa.user01@shop.example` to `qa.user50@shop.example`; passwords
  come from the password vault, never from this file.

## Formats
- CSV with semicolon delimiter, UTF-8 with BOM (for our import tool).
- Dates in data files as `YYYY-MM-DD`, amounts with a decimal point.

## Volume
At most 50 rows pasted; larger sets as a Python generator with a fixed seed.
```
