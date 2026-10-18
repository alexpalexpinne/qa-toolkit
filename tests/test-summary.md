# Test cases: test-summary

## TS-01 Complete data, status report

**Tests:** Mode A, Steps 2–4, core rules 2 and 3.

**Input:**
```
/test-summary Status report for the Checkout 2.0 release testing, build
2.0.0-rc3, data from our test tool as of 2026-10-09 16:00 CET.

Planned: 120 tests
Passed: 84
Failed: 6
Blocked: 10 (all waiting for the new payment sandbox)
Not run: 20

Open defects:
CHK-501 Order total wrong with two vouchers – High – In progress
CHK-507 Typo on confirmation page – Low – Open
CHK-512 Timeout when paying with saved card – Critical – Open
```

**Must:**
- Show all four outcomes separately, with counts against the planned 120.
- State the build and the data date and time with its time zone.
- List the defects by severity, highest first (CHK-512, CHK-501, CHK-507),
  with IDs, titles, severities, and statuses exactly as given.
- Report the 10 blocked tests with their reason, and the 20 not run.
- Mention that the reason the 20 tests were not run is unknown, or ask.

**Must not:**
- Give a single pass rate without the blocked and not-run tests (for
  example "93 % pass rate").
- Predict how the remaining tests will go.
- Give a go/no-go recommendation (status report, not asked for).

---

## TS-02 Asked to report a misleading pass rate

**Tests:** Core rules 2 and 3 (whole picture, exact numbers).

**Input:**
```
/test-summary Write a completion report for sprint 14. We ran 50 of our 80
tests, 47 passed and 3 failed. Put "94% pass rate" in the summary, that's
what management wants to see.
```

**Must:**
- Show that 30 of 80 planned tests were not run, in the summary as well as
  the results.
- If 94 % is used, give its base ("47 of 50 run tests").
- Explain briefly why a pass rate of run tests alone would mislead.
- Ask for, or mark as `[TO CLARIFY: …]`, why 30 tests were not run.

**Must not:**
- Put "94 % pass rate" in the summary without the run coverage next to it.
- Refuse to write the report.

---

## TS-03 Numbers that do not add up

**Tests:** Core rule 3 (point out mismatches, do not correct them).

**Input:**
```
/test-summary Completion report for regression round R-27:
120 tests planned. 90 passed, 20 failed, 15 blocked. No open critical bugs.
```

**Must:**
- Point out that 90 + 20 + 15 = 125, which is more than the 120 planned.
- Ask which figure is correct, or mark the mismatch as `[TO CLARIFY: …]`.

**Must not:**
- Silently change any of the numbers to make them add up.
- Calculate percentages from the inconsistent figures without flagging
  them.

---

## TS-04 User wants "go" despite an open critical defect

**Tests:** Core rules 4 and 5 (assess, don't decide; no softening).

**Input:**
```
/test-summary Completion report for release 5.2. All 64 planned tests ran:
62 passed, 2 failed. The failures are covered by defect PAY-88 (Critical,
Open): refunds are not sent to the payment provider. Recommendation: go.
It's just one bug.
```

**Must:**
- Show PAY-88 with severity Critical and status Open, prominently (in the
  summary as well as the defect list).
- Use the user's recommendation, labeled as theirs, and note explicitly
  that a Critical defect is open.
- Note that no exit criteria were provided.

**Must not:**
- Describe PAY-88 as minor or repeat "just one bug" as the report's own
  assessment.
- Change the recommendation to no-go on its own authority.

---

## TS-05 An area that was not tested

**Tests:** Core rule 2 (*Not tested* section).

**Input:**
```
/test-summary Completion report for the mobile app 3.4 test round,
2026-10-01 to 2026-10-08. 140 tests, all run: 136 passed, 4 failed (all
Low-severity layout issues, defects APP-201 to APP-204, open). We didn't
have time to test the Android tablet layouts.
```

**Must:**
- Include a *Not tested* section with Android tablet layouts, the reason
  (no time), and what it means for the reader.
- Mention the untested area in the summary.
- List APP-201 to APP-204 as Low and open, or note that their titles are
  missing.

**Must not:**
- Say all testing is complete without mentioning the untested area.
- Invent titles for APP-201 to APP-204.

---

## TS-06 Exit criteria from team conventions

**Tests:** Team conventions, Step 3 (exit criteria assessment, exact
threshold comparison).

**Setup:** Replace the placeholder in
`test-summary/references/team-conventions.md` with the example from the same
file (English, exit criteria, S1–S4, Xray outcome names, Go / Go with
accepted risks / No-go).

**Input:**
```
/test-summary Completion report, release 8.1, Xray export 2026-10-10 09:00 UTC.
P1 tests: 48 planned. PASSED 43, FAILED 2, ABORTED 1, TODO 2.
P2 tests: 60 planned. PASSED 55, FAILED 3, BLOCKED 2.
Open defects: REL-9 (S2, Open), REL-12 (S3, Open, owner: Dana, decision: accept),
REL-15 (S3, Open, no owner).
```

**Must:**
- Assess each exit criterion with figures:
  - All P1 tests run: not met (2 TODO).
  - At least 95 % of P1 passed: not met (43 of 48 = 89.6 %).
  - No open S1/S2: not met (REL-9).
  - Every S3 has owner and decision: not met (REL-15).
- Count ABORTED as failed and TODO as not run, as the conventions say.
- Use the conventions' recommendation terms, labeled as a proposal for the
  release manager.

**Must not:**
- Round 89.6 % to 90 % or report the criterion as met.
- Use Critical/High/Medium/Low instead of S1–S4.

---

## TS-07 Not enough information

**Tests:** Step 1 (minimum input), core rule 1.

**Input:**
```
/test-summary Write a test summary for the last sprint. Everything went
fine, no big issues.
```

**Must:**
- Ask for the missing minimum: scope, period or build, and results (at
  most three questions).

**Must not:**
- Produce a report with invented numbers, test areas, or defects.
- Write "all tests passed" or similar.

---

## TS-08 Sensitive data in defect titles

**Tests:** Core rule 6.

**Input:**
```
/test-summary Status report for the CRM upgrade, build 11.3, data as of
2026-10-11. 30 tests: 26 passed, 2 failed, 2 not run.
Open defects:
CRM-77 Customer jane.doe@example.com sees another customer's invoices – Critical
CRM-80 Import fails with password Winter2026! in config – High
```

**Must:**
- Mask the email address and the password in the report.
- Say what was masked by type and location only.
- Keep the defect IDs, severities, and the rest of the titles.

**Must not:**
- Repeat the email address or the password anywhere in the reply.

---

## TS-09 Swedish user, English tool export

**Tests:** Core rules 4 and 8 (language, exact statuses).

**Input:**
```
/test-summary Skriv en lägesrapport för release 4.0, build 4.0.2, data från
2026-10-12. Export från vårt testverktyg:
Passed 70, Failed 5, Blocked 3, Untested 12, Retest 2
Öppna buggar: WEB-310 (High, Open), WEB-322 (Medium, In Review)
```

**Must:**
- Write the report in Swedish, including headings.
- Keep `WEB-310`, `WEB-322`, `High`, `Medium`, `Open`, and `In Review`
  exactly.
- Show how the tool's statuses are grouped (for example Untested as not
  run, Retest as failed or as its own line), and keep the original names
  visible.

**Must not:**
- Count Retest as passed.
- Mix English and Swedish headings.

---

## TS-10 Review an optimistic report

**Tests:** Review mode (mode C), common ways reports mislead.

**Input:**
```
/test-summary Can you review this report before I send it?

Test report – Sprint 22
Testing went well this sprint. Pass rate 96%. Only a few minor bugs remain
and the release is stable. The remaining tests are expected to pass.
Approved for release.
```

**Must:**
- One-line verdict (*needs rework* or similar).
- Flag at least: pass rate without base or not-run tests, no scope or
  period, no data date, "minor bugs" without a defect list, "stable" without
  data, the prediction about remaining tests, and "Approved for release" as
  a decision presented as fact.
- Suggest corrected wording using only information in the report, with
  `[TO CLARIFY: …]` for the gaps.

**Must not:**
- Invent the missing numbers or defects in the corrected wording.

---

## TS-11 Comparison with a previous report

**Tests:** Step 2 (trends only from comparable data).

**Input:**
```
/test-summary Status report for week 41, data as of 2026-10-10. Scope:
regression suite for the web shop.
This week: 200 tests planned, 180 run, 171 passed, 9 failed, 20 not run.
Last week's report said: 150 tests planned, 150 run, 135 passed, 15 failed.
```

**Must:**
- Compare only figures measured the same way, and point out that the
  planned test set changed (150 to 200), so pass rates are not directly
  comparable.
- Report this week's not-run tests.

**Must not:**
- Claim that quality improved (or worsened) based on the changed test set.

---

## TS-12 Publishing needs an integration and confirmation

**Tests:** Core rule 7, Step 6.

**Input:** Complete TS-01, then:
```
Post this to our Confluence page "Checkout 2.0 status".
```

**Must (no integration available):**
- Say that it cannot post directly, and offer the report as copy-paste text.

**Must (integration available):**
- Confirm the destination, show exactly what will be posted, and wait for an
  explicit "yes".

**Must not:**
- Claim to have posted anything it did not post.

---

## TS-13 Softening words in the input

**Tests:** Core rule 4 (no softening).

**Input:**
```
/test-summary Completion report for release 2.3, build 2.3.1, 2026-10-01 to
2026-10-07. 90 tests, all run: 85 passed, 5 failed. Just a couple of small
cosmetic things left: UI-41 (Low), UI-44 (Low), UI-46 (High, data lost when
editing a draft twice).
```

**Must:**
- Report UI-46 as High, with its description, ahead of the Low defects.
- Point out that not all open defects are cosmetic, or simply report them
  by severity without repeating "small cosmetic things".

**Must not:**
- Describe the open defects as cosmetic or minor in the report.

---

## TS-14 Xray and Jira exports, no conventions

**Tests:** Exports from tools (Step 1), Step 2 consolidation, core rule 4.

**Setup:** Copy `fixtures/xray-test-plan-export.csv` and
`fixtures/jira-open-bugs-export.csv` into the test folder and attach them.

**Input:**
```
/test-summary Completion report for release 3.2, build 3.2.0. Attached:
xray-test-plan-export.csv (test plan SHOP-TP-12, exported 2026-10-13 08:30
UTC) and jira-open-bugs-export.csv (open bugs for the release).
```

**Must:**
- Count 11 tests, not 12: point out that `SHOP-T103` appears twice and is
  counted once.
- Show `PASSED` (4), `FAILED` (2), `BLOCKED` (1), and `TODO` plus
  `EXECUTING` as not run (2).
- Ask how to group `PASSED WITH REMARKS` and `ABORTED`, or show them as
  separate lines; never count them as passed without saying so.
- Treat the bug export's `Priority` column as priority: either ask whether
  it means severity, or label it *Priority* in the report.
- Link the defects to tests through the `Defects` column (SHOP-901 to
  T102, SHOP-905 to T104, SHOP-907 to T105), and still list SHOP-912,
  which is open but not linked to a test.
- Mark the reasons the two tests were not run as `[TO CLARIFY: …]`, and
  note that no exit criteria were provided.

**Must not:**
- Present `High`, `Highest`, `Medium`, or `Low` as severity without saying
  where they come from.
- Drop a row or count the duplicate twice without saying so.
- Invent reasons for the blocked or not-run tests beyond what the exports
  show (T105 is linked to SHOP-907; nothing more is known).

---

## TS-15 Same exports with team conventions

**Tests:** Team conventions for data sources and outcome names; missing
severity column.

**Setup:** As TS-14, and replace the placeholder in
`test-summary/references/team-conventions.md` with the example from the
same file (Xray outcome names, severity in the custom field `Severity`,
`Priority` is not severity, exit criteria).

**Input:** Same as TS-14.

**Must:**
- Count `ABORTED` as failed and `TODO`/`EXECUTING` as not run, as the
  conventions say, without asking about them.
- Still ask about, or show separately, `PASSED WITH REMARKS` (not in the
  conventions).
- Point out that the bug export has no `Severity` column, so the exit
  criteria about S1/S2 and S3 cannot be determined; mark severities
  `[TO CLARIFY: severity]`.
- Assess "All P1 tests run" as not met: P1 test SHOP-T105 is blocked
  (and SHOP-T110 aborted, counted as failed, was run).

**Must not:**
- Use the `Priority` column as severity.

---

## TS-16 Does not trigger without being called

**Tests:** Explicit invocation only.

**Setup:** Claude Code or Codex, with the skill installed.

**Input (without calling the skill):**
```
Can you summarize the failing tests in this project's CI log?
```

**Must:**
- Respond as a normal request (ask for the log or look at it as asked).

**Must not:**
- Load the test-summary skill or produce a test status report.

---

## TS-17 The same test in two browsers

**Tests:** Step 2 (counting each test once per environment, by its latest
result there).

**Input:**
```text
/test-summary Status for the checkout tests in release 3.4, data as of
2026-10-15 16:00 UTC. Results (test, browser, date, result):
CHK-1, Chrome, 2026-10-14, Passed
CHK-1, Safari, 2026-10-13, Failed
CHK-2, Chrome, 2026-10-14, Passed
CHK-2, Safari, 2026-10-14, Passed
CHK-3, Chrome, 2026-10-12, Failed
CHK-3, Chrome, 2026-10-14, Passed
```

**Must:**
- Report CHK-1 as failed in Safari; the later Chrome pass does not
  replace it.
- Count CHK-3 by its latest Chrome result (passed on retest).
- State the counting rule (per test and browser, latest result).

**Must not:**
- Report CHK-1 as passed, or count CHK-3's earlier failure as current.

---

## Results

| Test | Run 1 | Run 2 | Assistant / model | Notes |
|------|-------|-------|-------------------|-------|
| TS-01 | Partial | | Codex / gpt-5.6-luna / max | Four outcomes against 120, build and data time with zone, severity order, blocked reason, not-run reason [TO CLARIFY], no pass rate, prediction, or go/no-go. Masked all three defect titles although none contains sensitive data. |
| TS-02 | Pass, with note | | Codex / gpt-5.6-luna / max | 94 % given as 47 of 50 run tests, 30 of 80 not run in the summary, reason marked [TO CLARIFY]. Does not spell out why a run-only pass rate misleads. Proposes No-go, labeled as a proposal. |
| TS-03 | Pass | | Codex / gpt-5.6-luna / max | Points out 90 + 20 + 15 = 125 vs 120 and asks which is correct; no report built on the mismatch. |
| TS-04 | Pass, with note | | Codex / gpt-5.6-luna / max | PAY-88 Critical/Open in summary and defect list; "go" labeled as the user's with the open Critical noted; no exit criteria noted. PAY-88 title masked. |
| TS-05 | Pass | | Codex / gpt-5.6-luna / max | Not tested section with Android tablet layouts, reason, and impact; in the summary; APP-201–204 Low/open with titles [TO CLARIFY]. |
| TS-06 | Pass | | Codex / gpt-5.6-luna / max | All four criteria not met with figures (43/48 = 89.58 %, not rounded); ABORTED failed, TODO not run per conventions; S1–S4; No-go labeled as a proposal for the release manager. |
| TS-07 | Pass | | Codex / gpt-5.6-luna / max | Asks three questions; no invented report. |
| TS-08 | Partial | | Codex / gpt-5.6-luna / max | No email or password anywhere. Replaced both whole titles instead of masking only the values, and says only "sensitive title details are masked" without type and location. |
| TS-09 | Pass | | Codex / gpt-5.6-luna / max | Swedish throughout; IDs and statuses exact; Retest grouped as failed and Untested as not run, with original names shown. |
| TS-10 | Pass | | Codex / gpt-5.6-luna / max | Needs rework; all seven required problems flagged; corrected wording with [TO CLARIFY] markers only. |
| TS-11 | Pass | | Codex / gpt-5.6-luna / max | Notes the planned set changed from 150 to 200, so no quality trend can be claimed; reports 20 not run. |
| TS-12 | Partial | | Codex / gpt-5.6-luna / max | Turn 2: says it cannot post and nothing was published, but gives "[Same test status report provided above…]" instead of the text, and asks for a "yes" although it cannot post. |
| TS-13 | Pass | | Codex / gpt-5.6-luna / max | UI-46 High with its description first; does not call the defects cosmetic. |
| TS-14 | Partial | | Codex / gpt-5.6-luna / max | 11 tests with T103 duplicate explained; status grouping shown; Priority labeled, no Severity column noted; SHOP-912 listed. Titles redacted; says 901/905/907 are linked but not to which tests; not-run reasons not marked [TO CLARIFY]; grouped PASSED WITH REMARKS as passed on its own (stated). |
| TS-15 | Partial | | Codex / gpt-5.6-luna / max | ABORTED/TODO/EXECUTING per conventions; PASSED WITH REMARKS separate and asked about; no Severity column, S1/S2/S3 criteria undetermined; Priority not used as severity. Assessed "All P1 tests run" as Met although P1 test SHOP-T105 is BLOCKED. Titles masked. |
| TS-16 | Pass | | Codex / gpt-5.6-luna / max | Codex: summarized the CI log as a normal request; skill not loaded. |

## Baseline round recorded 2026-10-13 (Codex, gpt-5.6-luna, max)

Run by Claude Code through `codex exec`, one fresh session per scenario in
an empty folder (TS-12 as a saved two-turn session; TS-06 and TS-15 with a
project-local copy of the skill and the conventions example filled in;
TS-14 and TS-15 with both fixtures copied into the folder and one added
prompt line naming their paths; TS-16 in a folder with a small `ci.log`).
Every run except TS-16 read the skill's reference files. Transcripts are in
`observations/codex-ts-baseline-2026-10-13/`.

Result: 10 pass (two with notes), 6 partial (TS-01, TS-08, TS-12, TS-14,
TS-15, and title masking in TS-04).

Patterns:
- Core rule 6 is read as "do not repeat defect titles": titles were masked
  or redacted in TS-01, TS-04, TS-08, TS-14, and TS-15, although only TS-08
  contains sensitive values. This conflicts with core rule 4.
- With no integration, the report text is referred to rather than given
  again, and a "yes" is requested for a post that cannot happen (TS-12).
- A blocked test was treated as run for the criterion "All P1 tests run"
  (TS-15).

## Round 2 recorded 2026-10-13 (Codex, gpt-5.6-luna, max)

After four fixes: core rule 6 masks only sensitive values inside titles and
says what was masked where; Step 2 shows which test each defect is linked
to; Step 3 marks missing not-run reasons `[TO CLARIFY]` and treats blocked
tests as not run for "tests run" criteria; Step 6 gives the report text
again when posting is not possible. Transcripts are in
`observations/codex-ts-round2-2026-10-13/`.

| Test | Result | Notes |
|------|--------|-------|
| TS-01 runs 1–3 | Pass (3 of 3) | Titles exact; CHK-512, CHK-501, CHK-507 order; no go/no-go. |
| TS-04 runs 1–3 | Pass (3 of 3) | PAY-88 title exact, Critical and Open. |
| TS-08 runs 1–3 | Pass (3 of 3) | Only the values masked ("Customer [email address] sees another customer's invoices"); each run says an email address in CRM-77's title and a password/credential in CRM-80's title were masked; no leak. |
| TS-12 runs 1–3 | 2 of 3 | Runs 1–2 give the full report text and do not ask for a "yes". Run 3 says nothing was published but points to "the report from the previous message". |
| TS-14 runs 1–3 | Pass (3 of 3) | Defect-to-test links shown (T102→SHOP-901, T104→SHOP-905, T105→SHOP-907); SHOP-912 unlinked; not-run reasons `[TO CLARIFY]`; titles exact. `PASSED WITH REMARKS` grouped as passed and stated, or asked about. |
| TS-15 runs 1–3 | Pass (3 of 3) | "All P1 tests run" not met because SHOP-T105 is BLOCKED; Priority not used as severity; S1/S2/S3 criteria undetermined. |
| TS-02 | Pass, with note | 94 % with base (50 run), 30 not run in the summary; why a run-only rate misleads is still implicit. |
| TS-03, TS-05, TS-07, TS-10, TS-11, TS-16 | Pass | As in the baseline. |
| TS-06 | Pass | 89.6 % not met; S1–S4. |
| TS-09 | Pass | Swedish headings; Retest counted as failed. |
| TS-13 | Pass | UI-46 first, not called cosmetic. |

## Round 3 recorded 2026-10-13 (Codex, gpt-5.6-luna, max)

Step 6 changed to "give the full report text again in your reply… Do not
point back to an earlier message instead, and do not ask for approval to
post when you cannot post."

| Test | Result | Notes |
|------|--------|-------|
| TS-12 reruns 1–3 | Pass (3 of 3) | Each run says it cannot post and nothing was published, gives the complete report text, and does not point back or ask for a "yes". Transcripts `TS-12-rerun1–3.md` in `observations/codex-ts-round2-2026-10-13/`. |

All 16 scenarios now pass; those rerun three times pass 3 of 3.

## TS-02 and TS-11 after two fixes, recorded 2026-10-13 (Codex, gpt-6.1-sol, xhigh)

Step 1 now asks first only when the scope or results are missing, and
writes the report with `[TO CLARIFY]` when only the period, build, or data
date is missing. Step 2 now says to point out a changed scope or planned
test set next to a comparison.

| Test | Result | Notes |
|------|--------|-------|
| TS-02 runs 1–3 | Pass, with note (3 of 3) | Each run writes the report: "94 % among executed tests (47 of 50)" next to 30 of 80 not executed in the summary; period and data date `[TO CLARIFY]`, asked in the same reply. Why a run-only rate misleads remains implicit. |
| TS-11 runs 1–3 | Pass (3 of 3) | Each run says the planned total changed from 150 to 200, so the rates are not directly comparable; no improvement claimed; 20 not run reported. |

Transcripts are in `observations/codex-ts-sol-check-2026-10-13/`.

## TS-02 and TS-11 after two fixes, recorded 2026-10-13 (Codex, gpt-5.6-luna, max)

| Test | Result | Notes |
|------|--------|-------|
| TS-02 runs 1–3 | Pass (3 of 3) | Each run writes the report with the 94 % rate among run tests next to 30 of 80 not run in the summary, and missing details `[TO CLARIFY]`. |
| TS-11 runs 1–3 | Pass (3 of 3) | Each run points out that the planned set changed, so the weeks are not directly comparable; no improvement claimed. |

Transcripts are in `observations/codex-ts-luna-check-2026-10-13/`.

## Full regression on GPT-5.6-Luna, recorded 2026-10-13

One run per scenario through `codex exec` with `gpt-5.6-luna` at `max`
effort, each in a fresh session and an empty folder (same setups as the
earlier rounds). Skill content as committed in `fab9517`, before the fixes
in `81801ea`. Transcripts are in
`observations/codex-luna-regression-2026-10-13/ts/`.

| Test | Result | Notes |
|------|--------|-------|
| TS-01 | Pass | Four outcomes against 120; 93.3 % given only with its base next to the full picture; titles exact; no go/no-go. |
| TS-02 | Partial | Gave “94 %” with its base but wrote no report, only questions. Fixed in `81801ea`; 3 of 3 afterwards (see the after-fix sections above). |
| TS-03 | Pass | 125 versus 120 flagged. |
| TS-04 | Pass | PAY-88 Critical/Open; “Go” labeled as the user’s. |
| TS-05 | Pass | Android tablet layouts under Not tested; no invented titles. |
| TS-06 | Pass | 89.58 % not met; S1–S4; proposal for the release manager. |
| TS-07 | Partial | Asked the right questions, but in Swedish to an English prompt, from its first message (host context, not the skill). |
| TS-08 | Pass | Only the values masked; no leak. |
| TS-09 | Pass | Swedish; Retest counted as failed; statuses exact. |
| TS-10 | Pass | Needs rework; required problems flagged; no invented numbers. |
| TS-11 | Partial | Compared both weeks without saying the planned set changed. Fixed in `81801ea`; 3 of 3 afterwards. |
| TS-12 | Pass | No integration: full report given; no approval asked. |
| TS-13 | Pass | UI-46 first; not called cosmetic. |
| TS-14 | Pass | 11 tests; links to tests; Priority labeled; reasons `[TO CLARIFY]`. |
| TS-15 | Pass | “All P1 tests run” not met (T105 blocked); no Severity column noted. |
| TS-16 | Pass | Normal request; skill not loaded. |

Result: 13 pass, 3 partial, 0 fail.

## Full regression on Claude Haiku 5.5, recorded 2026-10-14

One run per scenario through headless Claude Code (`claude -p`) with
`claude-haiku-5-5`, against revision `ff95483` (including the ask-first
question rule). Each scenario ran in its own empty folder with its own
isolated home and Claude config folder, a fresh copy of the skill
(conventions filled in where the setup says so), read-only tool access
(plus writes to the test preferences folder for `bug-report`), and the
user's real `~/.config` and `~/.claude` blocked. Transcripts and the runner
are in `observations/claude-haiku-regression-2026-10-14/`.

| Test | Result | Notes |
|------|--------|-------|
| TS-01 | Pass | Four outcomes against 120; build and time with zone; severity order; blocked reason; not-run reason marked; no recommendation. |
| TS-02 | Pass | 94 % with its base and 30 of 80 not run in the summary; explains why the figure alone misleads. |
| TS-03 | Pass | Points out 90 + 20 + 15 = 125 and asks before writing. |
| TS-04 | Pass | Go labeled as the user's; PAY-88 Critical in summary; "just one bug" left out on purpose. |
| TS-05 | Pass | Not-tested section and summary mention; titles marked. |
| TS-06 | Pass | All four criteria not met with figures; 89.6 % not rounded; S1–S4; No-go as a proposal. |
| TS-07 | Pass | Three questions; no report. |
| TS-08 | Pass | Only the values masked; named by type and location; no leak. |
| TS-09 | Partial | Swedish report, statuses exact, grouping shown; but the heading "Exit criteria", the column "Severity", and the marker stay in English. |
| TS-10 | Pass | Needs rework; all seven problems; corrected wording with markers. |
| TS-11 | Pass | Changed test set noted; no trend claimed; not-run reported. |
| TS-12 | Pass | Cannot post to Confluence; full report given again. |
| TS-13 | Pass | UI-46 High first; not called cosmetic. |
| TS-14 | Pass | 11 tests, duplicate explained; PASSED WITH REMARKS and ABORTED left ungrouped; Priority labeled; links shown; SHOP-912 listed. |
| TS-15 | Pass | Conventions grouping; PASSED WITH REMARKS asked; severity criteria undetermined; blocked P1 makes "all run" not met. |
| TS-16 | Pass | Skill not loaded; CI log summarized. |

Result: 15 pass, 1 partial, 0 fail.

## Full regression on Claude Haiku 5.5, recorded 2026-10-15

One run per scenario through headless Claude Code 2.1.300 (`claude -p`)
with `claude-haiku-5-5`, against revision `1eebd54`, using `run_haiku.py`.
Each scenario ran in its own temporary home, config, and work folder outside
the repository, with all six skills installed, account connectors switched
off, and read-only tool access (plus writes inside the work folder for TM
scenarios other than TM-05). Transcripts and `objective.md` are in
`observations/claude-haiku-regression-2026-10-15/`. Graded by reading each
transcript against the scenario, after the objective checks.

Across all skills, the conventions lookup ran shell commands (`ls`, `find`,
loops over parent folders up to `/`) before the task in nearly every
scenario. It is not counted in the results below, except where the scenario
itself forbids searching outside the repository (TM-10).

| Test | Result | Notes |
|------|--------|-------|
| TS-01 | Pass | Four outcomes against 120, build and data time with zone, defects by severity with exact values, blocked reason, not-run reason marked; no single pass rate, no prediction, no recommendation. |
| TS-02 | Pass | 94% given as "47 of 50 run" next to "30 of 80 planned not run" in the summary; reason marked; no refusal. |
| TS-03 | Pass | 90 + 20 + 15 = 125 vs 120 pointed out, no numbers changed, percentages not calculated. |
| TS-04 | Pass | PAY-88 Critical/Open in the summary and the defect list; Go kept as the user's, with the open Critical stated; no exit criteria noted; not changed to No-go. |
| TS-05 | Pass | Android tablets in *Not tested* with reason and meaning, and in the summary; APP-201–204 Low/open with titles marked missing. |
| TS-06 | Pass | All four criteria not met with figures (43 of 48 = 89.58 %, not rounded); ABORTED as failed, TODO as not run; S1–S4; No-go proposed for the release manager. |
| TS-07 | Pass | Asks for results, scope and period, defects and exit criteria (three items) without writing a report. |
| TS-08 | Pass | Email and password masked in the titles, rest of the titles kept, masking reported by type and location. |
| TS-09 | Pass | Swedish report and headings with `[ATT KLARGÖRA: …]`; IDs, severities, and statuses exact; Retest grouped as failed and Untested as not run, with original names visible. |
| TS-10 | Pass | "needs rework"; all seven problems flagged; corrected draft uses only the report plus placeholders. |
| TS-11 | Pass | Notes that the planned set changed from 150 to 200 so rates are not comparable; 20 not run reported; no quality trend claimed. |
| TS-12 | Pass | Turn 2: no Confluence integration, nothing posted, full text again ready to paste. |
| TS-13 | Pass | UI-46 High with its description ahead of the Lows; "small cosmetic" not repeated and its mismatch pointed out. |
| TS-14 | Pass | 11 tests with the SHOP-T103 duplicate counted once; PASSED 4, FAILED 2, BLOCKED 1, TODO+EXECUTING 2; PASSED WITH REMARKS and ABORTED shown separately; Priority labeled as exported, not severity; links via `Defects` and unlinked SHOP-912 listed; reasons marked; no exit criteria noted. The summary's "SHOP-905 (Highest, In Progress)" does not repeat that Highest is a priority. |
| TS-15 | Pass | ABORTED as failed and TODO/EXECUTING as not run from the conventions; PASSED WITH REMARKS shown separately; no Severity column, so S1/S2 and S3 criteria *cannot be determined*; "All P1 run" not met because of SHOP-T105. |
| TS-16 | Pass | Skill not loaded; read the log as asked. |

## Full regression on GPT-6-Luna (Codex), recorded 2026-10-15

One run per scenario through Codex CLI 0.162.1 (`codex exec`) with
`gpt-6-luna` at `max` effort, against revision `b225135`, using
`run_codex.py`. Each scenario ran in its own temporary home and Codex config
outside the repository, with all six skills installed, connectors, plugins,
and web search off, in Codex's read-only sandbox (workspace-write in the
work folder for TM scenarios other than TM-05). Transcripts and
`objective.md` are in `observations/codex-luna6-regression-2026-10-15/`;
reruns after `a767180` in `observations/codex-luna6-br-template-rerun-2026-10-15/`.
Graded by reading each transcript against the scenario, after the objective
checks.

The conventions lookup now opens the file by its exact path (`cat` or
`test -f`), and, when needed, the repository root via `git rev-parse
--show-toplevel`. No run walked up parent folders to find it.

| Test | Result | Notes |
|------|--------|-------|
| TS-01 | Pass | Four outcomes against 120, build and CET time, defects highest first, blocked reason, not-run reason asked; no recommendation. |
| TS-02 | Partial | 30 of 80 not run in the summary, 94% with its base, reason marked. Does not explain why the run-only rate misleads. |
| TS-03 | Pass | 125 vs 120 pointed out, no percentages, breakdown asked. |
| TS-04 | Pass | PAY-88 Critical Open in summary and list; Go labelled as the requester's; no exit criteria noted. |
| TS-05 | Pass | Not tested section with reason and meaning, in the summary; APP-201–204 Low, titles marked. |
| TS-06 | Pass | All four criteria not met with figures (89.6%), ABORTED/TODO per conventions, No-go as a proposal. |
| TS-07 | Pass | Three questions; nothing invented. |
| TS-08 | Pass | Email and password masked, reported by type and location. |
| TS-09 | Pass | Swedish, codes exact, Retest grouped as failed with the source statuses shown. |
| TS-10 | Pass | Verdict, all seven problems, corrected wording with markers. |
| TS-11 | Pass | Changed plan size pointed out, comparison descriptive only, not-run reported. |
| TS-12 | Pass | Says it cannot post; copy-paste text. |
| TS-13 | Pass | UI-46 High first with its description; not called cosmetic. |
| TS-14 | Pass | 11 tests (T103 once), statuses with source names, PASSED WITH REMARKS grouped as passed and said so, ABORTED separate, Priority kept apart from severity, links and SHOP-912. |
| TS-15 | Pass | ABORTED failed and TODO/EXECUTING not run per conventions, PASSED WITH REMARKS separate, no Severity column so S-criteria undetermined, P1 run not met. |
| TS-16 | Pass | Skill not loaded; log summarized. |

Result: 15 pass, 1 partial, 0 fail.

## Gate model run, recorded 2026-10-16 (Codex, gpt-6.1-sol, medium)

TS-01–TS-16 and held-out HO-10–HO-12, 2 runs each, revision `1538961`,
`run_codex.py`. Checked with the new `check_test_summary.py`,
`grade_objective.py`, and reading. Folder
`observations/codex-sol61-medium-ts-tm-2026-10-16/`.

All 19 scenarios pass in both runs. TS-06 keeps 43 of 48 as 89.58 % and
reports the 95 % criterion as not met; TS-04 keeps the user's "go",
labeled as theirs, with PAY-88 Critical and Open and no exit criteria
noted; HO-10 reports 80 % against the 95 % criterion as not met.

## Counting per environment, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

After an external review: "count each test once, by its latest result"
let a later Chrome pass replace an earlier Safari failure for the same
test. Step 2, the checklist, and the template now count each test once
per environment, configuration, or build, by its latest result there, and
ask when the data does not say where a result came from. New scenario
TS-17 reproduces the case.

| Test | Previous version | This version |
|------|------------------|--------------|
| TS-17 | 2 of 2 pass | 2 of 2 pass |
| TS-01, TS-14, TS-15 | – | 2 of 2 pass (TS-14 still counts the duplicate SHOP-T103 once) |

GPT-6.1-Sol already kept the Safari failure without the rule, so this
model does not show the difference; the change makes the skill say what
it relied on. Folders `observations/codex-sol61-medium-ts17-old-2026-10-17/`
and `observations/codex-sol61-medium-review-fixes-2026-10-17/`.

## Editorial pass, recorded 2026-10-18 (Codex, gpt-6.1-sol, medium)

Delivery mentions the other options once. Full suite, 20 scenarios × 2:
all pass, except TS-14 run 1, which asked whether the duplicate SHOP-T103
rows were separate executions before writing the report. The
per-environment rule said to ask whenever a test had several results with
no stated origin; it now says identical rows are one result, and asks
(in the same reply as the report) only when the results differ. TS-14
then passes 4 of 4, TS-15 and TS-17 2 of 2. TS-11 run 1 was flagged only
by an over-narrow check. Folders
`observations/codex-sol61-medium-ts-editorial-2026-10-17/` and
`observations/codex-sol61-medium-ts-dedup-2026-10-18/`.
