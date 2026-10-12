# Test design techniques

Short guide to the techniques used in Step 3. Use the ones that fit the
requirement; most requirements need only two or three of them.

## Equivalence partitioning

Divide inputs into groups that the system should treat the same way, and
test one value from each group.

*Example:* age field accepting 18–65 → groups: below 18, 18–65, above 65,
not a number. Four cases instead of testing every age.

## Boundary value analysis

Defects cluster at limits. For every limit, test the value at the limit and
just outside it (and just inside, for high-risk limits).

*Example:* 18–65 → test 17, 18, 65, 66.

Look for limits in: lengths, amounts, counts, dates, file sizes, and
time-outs. If the requirement implies a limit but does not state it, the
limit is an open question.

## Decision tables

When the result depends on a combination of conditions, list the
combinations and the expected result for each.

*Example:* discount rules

| Member | Coupon | Order ≥ 100 | Expected discount |
|--------|--------|-------------|-------------------|
| Yes | Yes | Yes | <from requirement> |
| Yes | No | Yes | ... |
| No | Yes | No | ... |

If the requirement does not say what happens for a combination, that
combination is an open question. Do not fill it in yourself.

## State transitions

When behavior depends on the state of something (an order, an account, a
document), test valid transitions and at least the most likely invalid
ones.

*Example:* order states Draft → Placed → Shipped → Delivered. Test placing
a draft, and also trying to cancel a shipped order.

## Error guessing

Common failure points, worth considering for most features:

- Empty, missing, or only-whitespace input
- Leading and trailing spaces
- Very long input, or input at the maximum length
- Double-click or submitting twice
- Going back with the browser's back button after submitting
- Lost connection or a time-out halfway through
- Two users changing the same item at the same time
- A user without permission trying the action (also through a direct link)
- The session expiring in the middle of the flow

## Locale and international input

Add these when the feature handles text, dates, numbers, or money, and the
product is used in more than one country or language.

- **Characters:** letters with diacritics (`Åsa Öberg`, `José Müller`),
  non-Latin scripts (`山田太郎`, `Алексей`), right-to-left scripts (`مريم`),
  emoji, apostrophes and hyphens in names (`O'Brien`, `Anne-Marie`)
- **Length:** names and addresses longer than in the designer's own country
- **Formats:** decimal comma vs decimal point, date order, currency symbol
  placement, phone numbers with country codes
- **Time:** time zones, daylight saving time changes, dates near midnight,
  29 February
- **Sorting:** alphabetical order differs between languages
