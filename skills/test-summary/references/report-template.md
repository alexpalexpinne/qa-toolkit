# Default report structure

Teams can replace this structure through `team-conventions.md`. Headings are
shown in English; translate them into the report language, keeping the
structure. Leave out optional sections that do not apply; never fill them
with "N/A".

```markdown
# Test <status / completion> report: <scope>

**Period / build:** <YYYY-MM-DD – YYYY-MM-DD, build or version>
**Data as of:** <YYYY-MM-DD HH:MM, time zone, and source, e.g. "export from <tool>">
**Prepared by:** <name or role, if the user gives it>

## Summary
Two or three sentences: where testing stands, the main risks, and the
recommendation or next steps. A reader who stops here must not be misled.

## Recommendation (completion report)
<Go / Go with known risks / No-go, or the team's own terms>
<"Proposed – to be confirmed by <role>" if the user did not give it>
One or two sentences of reasoning, referring to the exit criteria and risks.

## Results

| Outcome | Tests | Share of planned |
|---------|-------|------------------|
| Passed | <n> | <n %> |
| Failed | <n> | <n %> |
| Blocked | <n> | <n %> |
| Not run | <n> | <n %> |
| **Planned** | **<total>** | **100 %** |

<Counting rule, e.g. "Each test counted once by its latest result.">
<Status grouping, if not obvious, e.g. "'Retest' counted as failed.">

### By area (optional)

| Area | Passed | Failed | Blocked | Not run |
|------|--------|--------|---------|---------|
| <area> | <n> | <n> | <n> | <n> |

## Exit criteria (if available)

| Criterion | Result | Figures |
|-----------|--------|---------|
| <criterion as written> | Met / Not met / Cannot be determined | <the numbers it is based on> |

## Open defects

| ID | Title | Severity | Status | Blocks release? |
|----|-------|----------|--------|-----------------|
| <exact ID> | <exact title, sensitive data masked> | <exact severity> | <exact status> | Yes / No / [TO CLARIFY: …] |

<Totals by severity, e.g. "Open: 1 Critical, 2 High, 5 Medium, 3 Low.">

## Not tested
| Area or test | Reason | What it means |
|--------------|--------|---------------|
| <what was not tested or only partly tested> | <why> | <risk for the reader> |

## Risks
- <risk> – follows from <failed test, defect, or untested area>

## Next steps (optional)
- <what happens next, and who does it, if the user gives it>

## Open questions
1. <each [TO CLARIFY: …] marker, and who could answer it>
```

## Status report (mode A)

Same structure, but:
- The recommendation section is replaced by *Next steps*, unless the user
  asks for a recommendation.
- *Not run* includes tests not run *yet*; say how many remain and, if the
  user gives it, the plan for running them. Do not predict their outcome.

## Example summary

Weak:

> Testing went well. 94 % pass rate and only a few minor bugs left. Ready
> for release.

Strong:

> 50 of 80 planned tests were run: 47 passed, 3 failed. 30 tests were not
> run, including all tests for the payment integration (test environment
> unavailable). One High-severity defect (SHOP-311) is open. Exit criteria
> are not met. Proposed recommendation, to be confirmed by the release
> manager: no-go until the payment tests have run and SHOP-311 is resolved
> or accepted.
