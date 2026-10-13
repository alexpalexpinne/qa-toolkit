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

> Real output, unedited except that its headings are shifted down two levels to fit this page.

---

**Draft — CHK-031: Checkout with voucher – total reduced by 25%**

**Purpose:** Check voucher application at checkout and inspect the stored voucher code after placing the order.  
**Priority:** High  
**Covers:** Original CHK-031, steps 1–4. No separate requirement or acceptance criterion supplied.  
**Status:** Blocked: pending clarification of expected results for original steps 3 and 4.

**Preconditions** *(moved from original step 1)*:

- Logged in as a test user.
- Cart contains 2 items: `SKU-1001` and `SKU-2002`.
- Checkout is open.

**Test data:** Voucher `WINTER25`.

| # | Action | Data | Expected result | Original step |
|---|---|---|---|---|
| 1 | Enter the voucher and select 'Apply'. | `WINTER25` | Total is reduced by 25%. A voucher line is shown in the order summary. | 1, 2 |
| 2 | Select 'Place order'. | — | [TO CLARIFY: expected result after selecting 'Place order'] | 3 |
| 3 | Inspect the voucher code for the order placed in this test. | `ORDERS.VOUCHER_CODE` | [TO CLARIFY: expected value of ORDERS.VOUCHER_CODE] | 4 |

**Scope recommendation:** Scope OK. The discount, summary display, and database check belong to one checkout transaction.

**Change summary:** Moved the setup from original step 1 into preconditions. Merged the result-only original step 2 into the voucher application step. Preserved the ID, test data, button labels, database identifier, and execution order. Missing expected results remain unresolved.

**Coverage:** Blocked pending clarification; this case does not count as confirmed coverage. Requirement coverage could not be assessed.

**Open questions:**

1. What observable result is expected after selecting 'Place order'?
2. What value should `ORDERS.VOUCHER_CODE` contain?
3. Which test user should be used, and how should the tester identify the relevant order record?
4. Which requirement or acceptance criterion should this case link to?

Consistency with related tests was not checked because none were provided.

This draft is ready to copy and paste; I can also save it as a Markdown file.

---

## What to notice

- Setup moved to preconditions, the result-only step merged into the step it belongs to, and every new step names the original step it came from.
- IDs, SKUs, the voucher code, button labels, and `ORDERS.VOUCHER_CODE` are kept exactly.
- The two missing expected results are not filled in. It would be easy to write "`VOUCHER_CODE` is `WINTER25`"; the skill marks them `[TO CLARIFY: …]` and blocks the case instead, because a guessed expected result is worse than none.

<sub>Codex, gpt-6.1-sol, reasoning effort xhigh, 2026-10-13 (scenario TC-11). The skills have changed since some of these runs, so current output may differ in detail.</sub>
