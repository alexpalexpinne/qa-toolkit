# Example: bug-report

A tester describes a checkout problem in a few sentences. The skill asks two questions, then writes the report.

## What the tester wrote (scenario input)

```text
/bug-report In the web shop (test environment, build 4.12.0), Chrome 129 on
Windows 11: I add one item to the cart, go to checkout and enter the
discount code SPRING10. The total stays at 50.00 EUR instead of 45.00 EUR.
No error message. I tried three times, same result every time. All
customers using discount codes would pay full price.
```

## What the skill asked first

```text
To complete the reproduction steps and clarify impact:

1. Which item did you add, and did you take any action after entering the code, such as clicking an apply button?
2. Did you complete a purchase and see a full-price charge, or was the issue observed only in the checkout total?
```

The tester answered:

```text
1.A mouse, clicked apply
2. Full-price charge
```

## What came back

> Real output, unedited, shown as plain text as it was supplied.

---

```text
Web shop checkout – SPRING10 leaves total unchanged and purchase is charged at full price

Summary

After entering SPRING10 and clicking apply, the checkout total remains 50.00 EUR instead of 45.00 EUR. The tester also confirms a full-price charge.

Environment

- Application: Web shop
- Environment: Test
- Build: 4.12.0
- Browser: Chrome 129
- Operating system: Windows 11
- Item: A mouse

Steps to reproduce

1. In the web shop’s test environment, add a mouse to the cart.
2. Go to checkout.
3. Enter discount code SPRING10.
4. Click the button to apply the code.

Expected result

The checkout total changes to 45.00 EUR.

Actual result

The total stays at 50.00 EUR. No error message appears. A full-price charge is also confirmed by the tester.

Reproducibility

The checkout issue occurred in all three reported attempts.

Severity

High (suggested) — the reported purchase was charged at full price despite the expected discount.

Additional notes

Hypothesis reported by the tester: all customers using discount codes would pay full price. The broader impact remains unverified.

Open questions

- Effect on other customers or discount codes: Unknown.
- Workaround: Unknown.
```

---

## What to notice

- Two short questions, only about what changes reproduction and impact. Nothing the tester already said is asked again.
- The tester's claim that "all customers" are affected is kept, but labeled as the tester's hypothesis rather than stated as fact.
- Expected and actual results are separate, reproducibility is "all three reported attempts", and the severity is a suggestion with a reason. Unknowns stay unknown.

<sub>Codex, run and supplied by the user, 2026-10-12 (scenario BR-02); model not recorded. The exact first message of that run was not recorded; the input shown is the scenario's. The skills have changed since some of these runs, so current output may differ in detail.</sub>
