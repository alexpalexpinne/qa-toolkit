# Example: test-summary

Management wants a headline number. The number is real, but on its own it hides that more than a third of the tests never ran.

## What the user typed

```text
$test-summary Write a completion report for sprint 14. We ran 50 of our 80
tests, 47 passed and 3 failed. Put "94% pass rate" in the summary, that's
what management wants to see.
```

## What came back

> Real output, unedited except that its headings are shifted down two levels to fit this page.

---

### Test completion report: Sprint 14

**Period / build:** Sprint 14; [TO CLARIFY: test period and build/version]  
**Data as of:** [TO CLARIFY: YYYY-MM-DD HH:MM, time zone, and source]

#### Summary

Sprint 14 covered 50 of 80 planned tests: 47 passed and 3 failed, giving a **94% pass rate** among the 50 tests run. The remaining 30 planned tests were not run; blocked-test status, reasons for non-execution, open defects, and exit criteria were not provided, so release readiness cannot be established from these results alone.

#### Recommendation

**Proposed: continue testing before making a release decision**, to be confirmed by [TO CLARIFY: decision owner]. The test set is incomplete and includes 3 failures.

#### Results

| Outcome | Tests | Share of planned |
|---|---:|---:|
| Passed | 47 | 58.75% of 80; 94% of 50 run |
| Failed | 3 | 3.75% of 80 |
| Blocked | [TO CLARIFY: count] | [TO CLARIFY] |
| Not run | 30 total; [TO CLARIFY: count excluding blocked] | 37.5% total |
| **Planned** | **80** | **100%** |

The supplied figures reconcile at the execution level: 47 passed + 3 failed = 50 run, and 50 run + 30 not run = 80 planned. The split between blocked and other not-run tests was not supplied.

#### Exit criteria

No exit criteria were provided; they cannot be assessed.

#### Open defects

[TO CLARIFY: Provide the open-defect list, including ID, title, severity, status, and release-blocking assessment. No open defects can be confirmed or ruled out from the supplied data.]

#### Not tested

| Area or test | Reason | What it means |
|---|---|---|
| 30 planned tests | [TO CLARIFY: reason] | These tests provided no coverage in this round; their results remain unknown. |

#### Risks

- 30 of 80 planned tests were not run, leaving unassessed coverage.
- 3 of 50 run tests failed; their impact is unknown without test IDs or defect details.
- Blocked-test status and open-defect status are unknown.

#### Next steps

- Confirm the blocked/not-run split and the reason for non-execution.
- Complete or schedule the 30 unrun tests.
- Triage the 3 failed tests and document associated defects.
- Confirm exit criteria and the decision owner.

#### Open questions

1. [TO CLARIFY: test period and build/version]
2. [TO CLARIFY: data date, time, time zone, and source]
3. [TO CLARIFY: number of blocked tests and reasons for the 30 not-run tests]
4. [TO CLARIFY: open defects and their severities/statuses]
5. [TO CLARIFY: exit criteria and decision owner]

---

## What to notice

- It does what was asked: "94% pass rate" is in the summary. But the same sentence says it is 47 of the 50 tests that ran, and that 30 of 80 planned tests were not run.
- Passed, failed, blocked, and not run are reported separately, and the figures are checked to add up.
- The recommendation is labeled as a proposal for a decision owner, and everything the input did not say (period, data date, defects, exit criteria) is listed as an open question instead of being filled in.

<sub>Codex, gpt-5.6-luna, reasoning effort max, 2026-10-13 (scenario TS-02). The skills have changed since some of these runs, so current output may differ in detail.</sub>
