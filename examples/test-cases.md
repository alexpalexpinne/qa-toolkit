# Example: test-cases

A legacy test case of the kind every test management tool is full of: setup, actions, and expected results mixed together, and two steps with no expected result at all.

## What the user typed

```text
$test-cases Please restructure this test case into a clean format.

CHK-031 Checkout with voucher
Step 1: Log in as test user, put 2 items in cart (SKU-1001, SKU-2002), go
to checkout. Enter voucher WINTER25 and press 'Apply'. Total should be
reduced by 25%.
Step 2: Expected: voucher line shown in order summary
Step 3: Press 'Place order'
Step 4: Check ORDERS.VOUCHER_CODE
```

## What came back

> Real output, unedited except that Codex's one-line opening note is left out.

---

Draft using the skill’s default format; no team conventions were found.

**CHK-031: Checkout with voucher**

**Purpose:** Check the voucher discount and order-summary display, then place the order and inspect `ORDERS.VOUCHER_CODE`.  
**Priority:** High  
**Covers:** Original CHK-031, steps 1–4; no separate requirement provided.  
**Status:** Blocked: pending clarification of expected results for original steps 3 and 4.

**Preconditions** *(setup from original step 1)*:

- Logged in as a test user.
- Cart contains 2 items: `SKU-1001` and `SKU-2002`.
- Checkout is open.

**Test data:** Voucher `WINTER25`. Use a test account and test data; production data should not be used.

| # | Action | Data | Expected result | Original step |
|---|---|---|---|---|
| 1 | Enter the voucher and press 'Apply'. | `WINTER25` | Total is reduced by 25%. A voucher line is shown in the order summary. | 1, 2 |
| 3 | Press 'Place order'. | — | [TO CLARIFY: expected result after pressing 'Place order'] | 3 |
| 4 | Check `ORDERS.VOUCHER_CODE` for this order. | — | [TO CLARIFY: expected stored value] | 4 |

**Scope recommendation:** Scope OK. The display and database checks belong to the same checkout transaction.

**Change summary:** Moved login, cart contents, and checkout setup into preconditions. Merged the expected-result-only step 2 into step 1. Preserved the remaining original step numbers, identifiers, and checks. Left the database expectation unspecified rather than assuming it equals the entered voucher.

**Coverage summary:**

| Source | Case | Status |
|---|---|---|
| CHK-031, original steps 1–4 | CHK-031 | Blocked: expected results for steps 3 and 4 are missing. |

**Open questions:**

1. What observable result should follow pressing 'Place order'?
2. What exact value should `ORDERS.VOUCHER_CODE` contain for this order?
3. Which amount is the basis for the 25% reduction?

Consistency with related cases was not checked because none were provided. This draft is ready to copy and paste; an import version would require the target tool’s format.

---

## What to notice

- Setup moved to preconditions, the result-only step merged into the step it belongs to, and every step names the original step it came from. The steps keep their original numbers (1, 3, 4), so they still match the old test.
- IDs, SKUs, the voucher code, button labels, and `ORDERS.VOUCHER_CODE` are kept exactly.
- The two missing expected results are not filled in. It would be easy to write "`VOUCHER_CODE` is `WINTER25`"; the skill says it did not assume that, marks both `[TO CLARIFY: …]`, and blocks the case, because a guessed expected result is worse than none.

## Without the skill

The same model with no skill installed wrote a clean five-step case, and filled in both missing expected results:

> | Step | Action | Expected result |
> |---|---|---|
> | 4 | Click **Place order**. | The order is created successfully with the discounted total. Record the order ID. |
> | 5 | Find the created order in `ORDERS` using the recorded order ID. Check `VOUCHER_CODE`. | `ORDERS.VOUCHER_CODE` equals `WINTER25`. |

Neither result is in the original test, and nothing marks them as added. It also renumbered the steps, so they no longer match the old test, and asked one question: what the 25% applies to.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-19 (scenario TC-11, run 1 of the full test run on the released 0.3.0 skills). Without the skill: the full run with no skill installed, same model and effort, 2026-10-20.</sub>
