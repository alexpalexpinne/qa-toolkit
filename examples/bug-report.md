# Example: bug-report

A tester describes a checkout problem in a few sentences. The skill writes the report right away and asks only what it could not know.

## What the tester wrote

```text
$bug-report In the web shop (test environment, build 4.12.0), Chrome 129 on
Windows 11: I add one item to the cart, go to checkout and enter the
discount code SPRING10. The total stays at 50.00 EUR instead of 45.00 EUR.
No error message. I tried three times, same result every time. All
customers using discount codes would pay full price.
```

## What came back

> Real output, unedited except that Codex's one-line opening note is left out.

---

No team conventions were found; I used the skill’s default template. This draft uses your observations and is ready to copy into a tracker.

**Title**  
Checkout – entering SPRING10 leaves the total unchanged

**Summary**  
In the web shop’s test environment, entering `SPRING10` at checkout leaves the total at 50.00 EUR instead of the expected 45.00 EUR. No error message appears.

**Environment**

- Product: Web shop
- Environment: Test
- Build: 4.12.0
- Browser: Chrome 129
- OS: Windows 11

**Steps to reproduce**

1. Add one item to the cart. [TO CLARIFY: which item]
2. Go to checkout.
3. Enter `SPRING10`. [TO CLARIFY: whether a separate action was taken to apply the code]

**Expected result**  
The total changes to 45.00 EUR.

**Actual result**  
The total remains 50.00 EUR. No error message appears.

**Reproducibility**  
Same result in all three reported attempts.

**Severity**  
Suggested: High — the checkout total does not reflect the expected discount in the reported test.

**Additional notes**  
Hypothesis reported by the tester: all customers using discount codes could pay full price. The observed evidence covers this code and checkout scenario in the test environment; broader impact and the amount actually charged remain unconfirmed.

**Open questions**

1. [TO CLARIFY: item used] Which item did you add?
2. [TO CLARIFY: code application action] Did you take any action after entering the code, such as clicking an apply button?
3. [TO CLARIFY: payment impact] Did you complete a purchase and observe the amount charged?

---

## What to notice

- The report comes first. What the tester did not say (which item, whether the code was applied with a button, what was actually charged) is marked in the report and asked as three short questions at the end, instead of holding the report up.
- The tester's claim that "all customers" are affected is kept, but labeled as the tester's hypothesis rather than stated as fact.
- `SPRING10`, `50.00 EUR`, and `45.00 EUR` are kept exactly. Expected and actual results are separate, reproducibility is "all three reported attempts", and the severity is a suggestion with a reason.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-19 (scenario BR-02, run 1 of the full test run on the released 0.3.0 skills).</sub>
