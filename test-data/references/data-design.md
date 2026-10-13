# Data design

How to decide which values a data set needs. Use the categories that matter
for the purpose; most needs are covered by two or three of them.

## Valid values

One typical value per group of inputs the system should treat the same way
(equivalence partitioning). For an age field accepting 18–65, one value such
as 34 covers the valid group; testing every age adds nothing.

## Boundaries

For every known limit, a value at the limit and just outside it (and just
inside, for risky limits).

*Example:* 1–50 characters → 0 (empty), 1, 50, 51.

Look for limits in lengths, amounts, counts, dates, file sizes, and number
precision. If the requirement implies a limit but does not state it, the
limit is `[TO CLARIFY: …]`.

## Invalid values

One value per kind of invalid input, so each rejection path is exercised:

- empty, missing, or only whitespace
- wrong type (letters in a number field)
- wrong format (an email without `@`, a date that does not exist such as
  `2026-02-30`)
- too long or too short
- outside the allowed range
- not in an allowed list (an unsupported currency or country)

Expected handling (rejected, with which message) comes from the source. If
the source does not say, mark it `[TO CLARIFY: …]`.

## International values

When the product is used in several countries or languages:

- **Characters:** diacritics (`Åsa Öberg`, `José Müller`), non-Latin
  scripts (`山田 太郎`, `Алексей Смирнов`), right-to-left scripts
  (`مريم الحسن`), apostrophes and hyphens (`O'Brien`, `Anne-Marie`),
  emoji where free text is allowed
- **Names:** single names, very long names, family name first
- **Addresses:** different orders of street, number, and postal code;
  postal codes with letters (`SW1A 1AA` format) and without
- **Numbers and money:** decimal comma vs decimal point, thousands
  separators, currencies with no or three decimals (`JPY`, `KWD`)
- **Dates and times:** different date orders, time zones, daylight saving
  changes, `29 February`, times near midnight

## Combinations and states

When records relate to each other or must be in a particular state:

- Build complete, consistent records: a customer with an account, an order
  with lines whose totals add up, a payment that matches the order.
- Cover the states the test needs (new, active, locked, expired, deleted)
  and say how each record reaches that state if it cannot be created
  directly.
- For decision rules, one record per combination the requirement defines.
- Keep values unique where the system requires it (email addresses,
  usernames, order numbers), unless a test needs a duplicate on purpose.

## Dates relative to today

Ages, expiry dates, trial periods, and deadlines depend on the day the test
runs. A birth date that makes someone exactly 18 today is wrong tomorrow.

- Describe such values relative to the test day: "today minus 18 years",
  "expires yesterday", "created 31 days ago".
- If a fixed date is needed, give the reference date it was calculated
  from, and say it must be recalculated.
- In a generator, calculate these dates when the generator runs.
- Watch for edge cases around the boundary: 29 February birthdays, month
  ends, and time zones near midnight.

## Input validation probes

Only when the user asks for negative or robustness testing of input
handling: a few harmless strings that check whether input is escaped and
validated, for example a single quote (`O'Brien`), angle brackets
(`<b>bold</b>`), very long strings, and control characters. Keep them
harmless; the goal is to see whether the system handles them safely, not
to attack it.

## Output formats

| Format | Notes |
|--------|-------|
| Table | Default for people; include a *Purpose* column |
| CSV | Column names exactly as the target expects; say which delimiter and encoding (UTF-8 by default) |
| JSON | Field names and types exactly as the schema; valid JSON |
| SQL | Insert statements for the given table and columns only; never run them without an explicit "yes" |

## Volume

- Small sets (up to about 20 rows) for manual tests: every row has a
  purpose.
- Larger sets for load or volume tests: offer a generator with a fixed
  seed instead of pasted rows, and keep the same safety rules in it.

## Common problems in existing data sets

Look for these in review mode:

- Real-looking personal data, possibly copied from production
- Checksum-valid identity, card, or account numbers without a documented
  test source
- Only "happy path" values: no boundaries or invalid values
- Only one country's formats and characters
- Inconsistent records (totals that do not add up, dates in the wrong
  order) that are not labeled as deliberate
- No marker to find and remove the data later
- The same value reused where tests need distinct records (for example one
  email address for several accounts that must be unique)
- Fixed dates for age or expiry tests that have since gone out of date
- A test data marker that breaks the value under test (for example a prefix
  that makes a boundary-length name too long)
