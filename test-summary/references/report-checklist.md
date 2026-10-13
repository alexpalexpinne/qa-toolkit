# Test report checklist

Use this before delivering a report (Step 5) and when reviewing an existing
one (mode C). Items are in order of importance.

## Must have

A report missing any of these is not ready to share.

- [ ] **Scope, period or build, and data date are stated.** The reader knows
      what the numbers cover and how current they are.
- [ ] **All four outcomes are shown:** passed, failed, blocked, not run.
      They add up to the planned total, or the mismatch is pointed out.
- [ ] **Not tested is reported,** with reasons and what it means for the
      reader, or explicitly marked `[TO CLARIFY: …]`.
- [ ] **Open defects are listed by severity,** with IDs, titles, severities,
      and statuses exactly as given.
- [ ] **No invented information.** Every figure and statement comes from
      the user, the material provided, or the team conventions. No
      predictions, estimates, or quality claims beyond the data.
- [ ] **The summary does not mislead.** A reader who reads only the summary
      gets the same picture as one who reads everything.
- [ ] **The recommendation is labeled** as the user's or as a proposal for
      the responsible person, and does not contradict the exit criteria
      without saying so.
- [ ] **No sensitive data anywhere in the reply,** including commentary.

## Should have

- [ ] Exit criteria assessed one by one with supporting figures, or a note
      that none were provided.
- [ ] Every percentage shows its base, and threshold comparisons use exact
      values.
- [ ] Counting rule and status grouping are stated when they matter.
- [ ] Risks each name the data they follow from.
- [ ] Short: the summary fits in a few sentences, and the whole report can be
      read in a few minutes.

## Common ways reports mislead

Look for these in your own drafts and in reports you review.

| Pattern | Example | Instead |
|---------|---------|---------|
| **Pass rate of executed tests only** | "94 % pass rate" when 30 of 80 tests never ran | "47 of 50 run tests passed; 30 of 80 planned tests not run" |
| **Blocked counted as passed or left out** | Blocked tests missing from the totals | Show blocked tests as their own outcome, with the reason |
| **Missing "not tested"** | No mention of an area that was skipped | A *Not tested* section with reasons and impact |
| **Rounding across a threshold** | 89.6 % reported as "90 %, criterion met" | "89.6 %, criterion of 90 % not met" |
| **Softened severity** | "a few minor issues" when a High defect is open | Defects by severity as recorded |
| **Quality claims without data** | "The release is stable" | State what was tested and what was found |
| **Predictions** | "The remaining tests are expected to pass" | "30 tests remain; planned for <date>, if known" |
| **Trend from one data point or changed measurement** | "Quality improved" when the test set changed | Compare only figures measured the same way |
| **Retests counted twice** | A test failed, then passed, counted as one fail and one pass | Count each test once by its latest result, and say so |
| **Missing data date** | Numbers without "as of" | "Data as of <date and time>, source <tool>" |
| **Decision presented as fact** | "Approved for release" written by the tester | "Proposed recommendation: go, to be confirmed by <role>" |
| **Percentages of tiny numbers** | "Failure rate up 100 %" (from 1 to 2) | Give the counts |
