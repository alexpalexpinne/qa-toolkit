# Example: test-summary

Management wants a headline number. The number is real, but on its own it hides that more than a third of the tests never ran.

## What the user typed

```text
$test-summary Write a completion report for sprint 14. We ran 50 of our 80
tests, 47 passed and 3 failed. Put "94% pass rate" in the summary, that's
what management wants to see.
```

## What came back

> Real output, unedited except that Codex's one-line opening note is left out and its headings are shifted down two levels to fit this page.

---

### Test completion report: Sprint 14

*Draft for review, ready to copy and paste. No team conventions were found; skill defaults used.*

**Period / build:** [TO CLARIFY: reporting period or build]  
**Data as of:** [TO CLARIFY: results date]  
**Source:** User-provided totals.

#### Summary

Sprint 14 achieved a **94% pass rate among tests run: 47 of 50 passed**, while 3 failed. Of 80 planned tests, 30 were not run, leaving 37.5% of the planned test set unexecuted. Proposed next step: review the failures and untested scope before making a release decision.

#### Recommendation

**Proposed, for the responsible person to confirm:** defer release approval pending review of the 3 failures, the 30 unexecuted tests, and applicable exit criteria.

#### Results

| Outcome | Count |
|---|---:|
| Passed | 47 of 50 run |
| Failed | 3 of 50 run |
| Blocked | [TO CLARIFY: count within the 30 unexecuted tests] |
| Not run | 30 of 80 planned, including any blocked tests |
| Planned | 80 |
| Executed | 50 of 80 planned (62.5%) |

Counts use the supplied aggregate totals: 47 + 3 = 50; 80 − 50 = 30. The separate blocked and other not-run counts remain unconfirmed.

#### Exit criteria

None were provided; assessment cannot be completed.

#### Open defects

[TO CLARIFY: defect IDs, titles, severities, and current statuses associated with the failures, plus any other open defects.]

#### Not tested and risks

Thirty planned tests were not run. [TO CLARIFY: affected tests or areas and reasons for omission.] Their behavior remains unverified; the impact of the 3 failed tests is also unknown without failure details.

#### Open questions

- What reporting period or build do these results cover?
- What date do the results represent?
- How many of the 30 unexecuted tests were blocked?

Also unresolved: omitted scope and reasons, defect details, and applicable exit criteria.

---

## What to notice

- It does what was asked: "94% pass rate" is in the summary. But the same sentence says it is 47 of the 50 tests that ran, and the next one says that 30 of 80 planned tests were not run.
- Passed, failed, blocked, and not run are reported separately, and the figures are checked to add up.
- The recommendation is labeled as a proposal for the responsible person to confirm, and everything the input did not say (period, data date, defects, exit criteria) is marked instead of filled in.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-20 (scenario TS-02, run 2 of the full test run on the released 0.3.0 skills).</sub>
