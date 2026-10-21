# Example: one team file, two skills

A tester reports a bug, and the release summary later judges that bug against the same team's rules. Both skills read the same conventions file; nobody repeats the rules in the request.

## The team's conventions file

`.qa-toolkit/conventions.md`, written once with `team-setup` or by hand:

```markdown
## General
- Reports are written in English.
- Tracker: Jira, project SHOP. Test management: Xray.
- Severity: S1 (production down or data loss), S2 (major function broken,
  no workaround), S3 (impaired, workaround exists), S4 (cosmetic).

## bug-report
- Component is required: Checkout, Search, Account, or Admin.
- Name the Xray test the bug was found with, if any.

## test-summary
- Exit criteria for release testing: all P1 tests run; no open S1 or S2
  defects.
- Xray outcomes: PASSED → passed; FAILED, ABORTED → failed; BLOCKED →
  blocked; TODO, EXECUTING → not run.
- Recommendation terms: Go / Go with accepted risks / No-go. The release
  manager decides.
```

## Step 1: the bug report

```text
$bug-report Checkout in the test environment, build 3.4.1, Chrome
130 on Windows 11. Logged in as the standard test user, added one item
(SKU-1001, 50.00 EUR), entered the voucher WINTER25 and pressed Apply. The
total became 25.00 EUR instead of 37.50 EUR, so the 25 % discount is
applied twice. Every time, also with SKU-2002. Found while running Xray
test SHOP-T104.
```

> Real output, unedited except that Codex's one-line opening note is left out.

---

Using `.qa-toolkit/conventions.md` for English, Jira project SHOP, and the team severity scale. This draft uses your observations; I haven’t reproduced the issue. No Jira integration is available here, so the report is ready to copy.

**Title**

Checkout – WINTER25 reduces 50.00 EUR total to 25.00 EUR instead of 37.50 EUR

**Summary**

Applying voucher `WINTER25` produces an incorrect checkout total for the standard test user.

**Environment**

- Component: Checkout
- Environment: test
- Build: 3.4.1
- Browser: Chrome 130
- OS: Windows 11
- Account: standard test user
- Xray test: SHOP-T104

**Steps to reproduce**

1. Log in to the test environment as the standard test user.
2. Add one item, `SKU-1001`, priced at 50.00 EUR.
3. Open checkout.
4. Enter voucher `WINTER25`.
5. Press `Apply`.

**Expected result**

The 25 % discount produces a total of 37.50 EUR.

**Actual result**

The total becomes 25.00 EUR.

**Reproducibility**

Every time, according to the tester. The issue also occurs with `SKU-2002`.

**Severity**

[TO CLARIFY: severity under the team scale; workaround availability is unknown]. The observed impact is an incorrect checkout total.

**Additional notes**

Hypothesis from the tester: the 25 % discount is applied twice. The observed total alone does not confirm the cause.

**Open questions**

- [TO CLARIFY: workaround availability, needed to assess severity]. Is there a way to obtain the correct discounted total?

---

## Step 2: the release summary, in the same session

```text
$test-summary Completion report for release 3.4, build 3.4.1,
data as of 2026-10-21. Xray test plan SHOP-TP-14. P1: 12 tests, 10 PASSED,
1 FAILED (SHOP-T104), 1 TODO (SHOP-T111). P2: 8 tests, 7 PASSED, 1 BLOCKED
(SHOP-T118). The only open defect is the voucher bug above, filed as
SHOP-931 with severity S2, status Open.
```

> Real output, unedited except that Codex's one-line opening note is left out.

---

**Draft test completion report — Release 3.4**

**Build:** 3.4.1  
**Data as of:** 2026-10-21  
**Scope:** Xray test plan SHOP-TP-14  
**Source:** User-supplied results; assessment uses `.qa-toolkit/conventions.md`.

**Summary**

Of 20 planned tests, 17 passed, 1 failed, 1 was blocked, and 1 was not run. Both release exit criteria are **not met**: P1 test SHOP-T111 remains TODO, and S2 defect SHOP-931 remains Open. **Proposed recommendation: No-go**, for the release manager to confirm.

**Results**

| Priority | Planned | Passed | Failed | Blocked | Not run |
|----------|--------:|-------:|-------:|--------:|--------:|
| P1 | 12 | 10 | 1 | 0 | 1 |
| P2 | 8 | 7 | 0 | 1 | 0 |
| **Total** | **20** | **17** | **1** | **1** | **1** |

Counts use the supplied totals for this build, without adding separate attempts. Xray mapping: PASSED → passed; FAILED → failed; BLOCKED → blocked; TODO → not run. Totals reconcile.

**Exit criteria**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| All P1 tests run | Not met | 11 of 12 run; SHOP-T111 is TODO |
| No open S1 or S2 defects | Not met | SHOP-931 is S2, Open |

**Open defects**

| ID | Title from the preceding report | Severity | Status | Related test | Blocks release? |
|----|-------|----------|--------|--------------|-----------------|
| SHOP-931 | Checkout – WINTER25 reduces 50.00 EUR total to 25.00 EUR instead of 37.50 EUR | S2 | Open | SHOP-T104 | Yes |

Open defects: **1 S2**, the only open defect reported.

**Not tested**

| Test | Status | Reason | Implication |
|------|--------|--------|-------------|
| SHOP-T111 (P1) | TODO | [TO CLARIFY: reason not run] | P1 coverage is incomplete |
| SHOP-T118 (P2) | BLOCKED | [TO CLARIFY: blocking reason] | Coverage remains incomplete |

**Risks and next steps**

- SHOP-T104 and SHOP-931 show incorrect voucher totals in checkout. Resolve the defect and retest the affected behavior.
- SHOP-T111 and SHOP-T118 leave behavior unverified. Run SHOP-T111, unblock and run SHOP-T118, then reassess the exit criteria.

**Open questions**

1. Why was SHOP-T111 not run?
2. What blocked SHOP-T118?

---

## What to notice

- Neither request mentions the language, tracker, component list, severity scale, exit criteria, or recommendation terms. Both skills say they used `.qa-toolkit/conventions.md` and apply it.
- The bug report names the component and the Xray test, as the team requires. It leaves the severity open and asks whether there is a workaround, because the team's own scale separates S2 from S3 by exactly that.
- The summary counts each priority separately, judges both exit criteria with the evidence (SHOP-T111 not run, SHOP-931 open at S2), links the bug to the test it was found with, and carries over the title from step 1. "No-go" uses the team's terms and is labeled as a proposal for the release manager, who decides.
- `TODO` is counted as not run and `BLOCKED` as blocked, as the team's Xray mapping says, not as failures.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-21 (scenario TM-16, run 2 of 3 on the released 0.3.0 skills; all three runs passed).</sub>
