# Test cases: test-cases

## TC-01 Clear requirement

**Tests:** Step 3–5 (techniques, traceability, format).

**Input:**
```
/test-cases
As a registered user I want to change the display name on my profile so
that other users see the name I prefer.

Acceptance criteria:
AC1. Given I am logged in and on my profile page, when I enter a new display
     name of 1–50 characters and select Save, then the new name is shown on
     my profile and on all my existing comments within 5 seconds.
AC2. Given I enter an empty name or more than 50 characters, when I select
     Save, then the name is not saved and the message "Display name must be
     1–50 characters" is shown under the field.
AC3. Display names may contain letters from any script, digits, spaces,
     hyphens, and apostrophes. Other characters are rejected with the
     message "Display name contains characters that are not allowed".
AC4. Display names do not need to be unique.
```

**Must:**
- Boundary values for the length: 0, 1, 50, 51 (combined into one
  data-driven case).
- Cases for AC3 with names in non-Latin scripts and with apostrophes or
  hyphens, plus at least one rejected character.
- A case for AC4 (two users with the same name).
- Each case names the criterion it covers; the coverage summary lists AC1–AC4.
- Error messages quoted exactly as in the requirement.
- At most 15 test cases.

**Must not:**
- Invent expected results the requirement does not give (for example what
  happens with leading spaces); those go under *Open questions*.

---

## TC-02 Vague requirement

**Tests:** Step 2 (readiness check), core rule 1 (no invented expected
results).

**Input:**
```
/test-cases
As a customer I want to reset my password so that I can access my account
if I forget it.

- The user should receive an email quickly.
- The reset link should be valid for a reasonable time.
- The new password must be secure.
```

**Must:**
- Point out that the requirement has significant gaps, and suggest
  reviewing it first (mentioning `review-requirements` is fine).
- If the user continues: use markers such as `[TO CLARIFY: link validity]`
  and `[TO CLARIFY: password rules]`, list them under
  *Open questions*, and mark those cases *Blocked: pending clarification*.
- The coverage summary shows the affected criteria as *Blocked* or *Partly
  covered*, not *Covered*.

**Must not:**
- Use concrete values such as "24 hours" or "at least 12 characters" as
  expected results.

---

## TC-03 Decision table with missing combinations

**Tests:** Decision tables, open questions for undefined combinations.

**Input:**
```
/test-cases
Members get 10% off all orders. Orders of 100 EUR or more get free
shipping. A coupon code gives 5 EUR off. Coupons cannot be combined with
the member discount.
```

**Must:**
- Build a decision table or equivalent cases for member / coupon / order
  amount.
- Test the boundary 99.99 / 100.00 EUR for free shipping.
- Ask, or list as open questions: whether 100 EUR is before or after
  discounts, and what happens when a member enters a coupon (which discount
  wins, or is the coupon rejected?).

**Must not:**
- Decide on its own which discount wins when a member uses a coupon.

---

## TC-04 Limit and further ideas

**Tests:** Step 4 (max 15 cases, *Further test ideas*).

**Input:**
```
/test-cases
Users can upload a profile picture. Allowed formats: JPG, PNG, WEBP.
Maximum size 5 MB. The picture is cropped to a square and resized to
400×400 pixels. Users can delete their picture, and then a default avatar
with their initials is shown. Uploading a new picture replaces the old one.
```

**Must:**
- At most 15 test cases.
- Remaining ideas listed one line each under *Further test ideas*.
- Size boundary around 5 MB, and invalid formats (for example GIF, a renamed
  file), with expected results from the requirement or `[TO CLARIFY: …]`
  markers.

**Must not:**
- Produce more than 15 cases without the user asking.
- Invent the error message for a too-large file.

---

## TC-05 Swedish requirement, Given/When/Then

**Tests:** Core rule 7 (language, headings, Gherkin keywords).

**Input:**
```
/test-cases Skriv testfallen som Givet/När/Så.

Som kund vill jag kunna avboka en bokning så att jag inte behöver betala
för något jag inte ska använda.

- Avbokning är möjlig fram till 24 timmar före starttiden.
- Vid avbokning visas meddelandet "Din bokning är avbokad".
- Senare än 24 timmar före starttiden visas "Avbokning är inte längre möjlig".
```

**Must:**
- Write everything in Swedish, including headings and the coverage summary.
- Use *Givet/När/Så*.
- Test the 24-hour boundary (just before and just after).
- Quote the messages exactly.
- Ask about or list time zone handling if relevant (whose time zone is the
  start time in?).

**Must not:**
- Mix English and Swedish headings.

---

## TC-06 Team conventions are applied

**Tests:** Team conventions take precedence.

**Setup:** Replace the placeholder in
`test-cases/references/team-conventions.md` with the example from the same
file (English, Given/When/Then, IDs like SHOP-142-TC-01, P1–P3, required
component and test level).

**Input:**
```
/test-cases Story SHOP-142: As a customer I want to save my cart so that I
can continue shopping later. Saved carts are kept for 30 days.
```

**Must:**
- Use IDs `SHOP-142-TC-01`, `SHOP-142-TC-02`, ...
- Use P1–P3 instead of High/Medium/Low.
- Use Given/When/Then.
- Include component and test level on each case.
- Use the title pattern `<Area> | <scenario> | <expected outcome>`.
- Refer to test users by role.

**Must not:**
- Use the default step-table format or priority scale.

---

## TC-07 Real-looking personal data in the requirement

**Tests:** Core rule 5 (fake test data only).

**Input:**
```
/test-cases
Support staff can search for customers by email. Example from production:
jane.doe@realcompany.com, customer number 884213.
```

**Must:**
- Use only clearly fake data (for example `@example.com` addresses) in the
  test cases.
- Mention that production data should not be used in tests.

**Must not:**
- Use the email address or customer number from the input in any test case.

---

## TC-08 Review existing test cases

**Tests:** Review mode (mode B).

**Input:**
```
/test-cases Review these test cases for the login page:

TC1: Log in. Expected: works.
TC2: Log in with wrong password. Expected: error.
TC3: Log in with correct password after TC2. Expected: user is logged in.
TC4: Log in. Expected: works correctly.
```

**Must:**
- One-line verdict ("needs rework" or similar).
- Flag vague expected results ("works", "error"), the dependency of TC3 on
  TC2, the duplicate TC1/TC4, and missing preconditions and test data.
- Suggest at most 5 new cases for important gaps (for example locked
  account, empty fields), with `[TO CLARIFY: …]` markers where the expected result is
  unknown.

**Must not:**
- Invent the exact error message for a wrong password.
- Rewrite the whole set without being asked.

---

## TC-09 Import to a tool

**Tests:** Step 7 (import format, confirmation).

**Input:** Complete TC-01, then:
```
Can you give me these as a CSV so I can import them?
```

**Must:**
- Ask which tool the CSV is for (unless the team conventions say), before
  producing the file.

**Must not:**
- Guess a column layout without asking.

---

## TC-10 Does not trigger without being called

**Tests:** Explicit invocation only.

**Setup:** Claude Code, with the skill installed.

**Input (without calling the skill):**
```
Can you add unit tests for the discount calculation in this project?
```

**Must:**
- Respond as a normal coding request.

**Must not:**
- Load the test-cases skill or produce manual test cases.

---

## TC-11 Restructure a messy test case

**Tests:** Mode C, core rules 1, 8, 9, field placement, traceability.

**Input:**
```
/test-cases Please restructure this test case into a clean format.

CHK-031 Checkout with voucher
Step 1: Log in as test user, put 2 items in cart (SKU-1001, SKU-2002), go
to checkout. Enter voucher WINTER25 and press 'Apply'. Total should be
reduced by 25%.
Step 2: Expected: voucher line shown in order summary
Step 3: Press 'Place order'
Step 4: Check ORDERS.VOUCHER_CODE
```

**Must:**
- Keep the ID `CHK-031`.
- Keep `SKU-1001`, `SKU-2002`, `WINTER25`, `'Apply'`, `'Place order'`, and
  `ORDERS.VOUCHER_CODE` exactly.
- Move "Total should be reduced by 25%" into an expected result, and merge
  original step 2 (expected result only) into the step it belongs to.
- Name the original step or steps on every new step.
- Mark the missing expected results for original steps 3 and 4 as
  `[TO CLARIFY: …]`, and mark the test *Blocked: pending clarification*.
- Include a scope recommendation (*Scope OK*), a change summary, and a note
  that consistency with related tests was not checked.

**Must not:**
- Invent expected results for steps 3 and 4 (for example "an order
  confirmation is shown" or "`VOUCHER_CODE` is `WINTER25`").
- Remove the `Expected:`-style text without keeping its meaning.

---

## TC-12 Several scenarios in one test

**Tests:** Scope recommendation, never splitting without being asked.

**Input:**
```
/test-cases Restructure this test:

PAY-118 Payment methods
1. Pay for an order with a credit card. Expected: order status PAID.
2. Pay for another order with invoice. Expected: order status
   AWAITING_PAYMENT and invoice email sent.
3. Pay for a third order with a gift card that covers the full amount.
   Expected: order status PAID and gift card balance reduced.
```

**Must:**
- Recommend *Consider split*, explaining that the three payment methods
  follow different rules and can fail independently.
- Keep the statuses `PAID` and `AWAITING_PAYMENT` exactly.
- Keep it as one restructured test (or ask whether to split).

**Must not:**
- Produce three separate test cases without the user asking.

---

## TC-13 Step with an attachment

**Tests:** Attachment rules.

**Input:**
```
/test-cases Restructure this test:

INV-077 Invoice PDF layout
Step 1: Open order 5001 and select 'Download invoice'. Compare the PDF with
the attached reference. Check logo, address block and VAT lines.
[Attachment: invoice-reference.pdf]
Step 2: Expected: PDF matches reference
```

**Must:**
- Keep `invoice-reference.pdf` attached to the step it was on, with the
  same name.
- Leave step 1 unsplit, even though it contains several checks, and explain
  in an open question that splitting it is a decision for a person because
  of the attachment.
- Merge original step 2 ("PDF matches reference") into the expected result
  of step 1, keep step 1's action unchanged, and mention the merge in the
  change summary.

**Must not:**
- Split step 1 into several steps.
- Drop, rename, or move the attachment.
- Leave original step 2 as a step with no action.

---

## TC-14 Exact technical content and existing placeholders

**Tests:** Core rule 8 (exact content, three kinds of placeholder).

**Input:**
```
/test-cases Restructure this test:

DB-009 Archive old sessions
Step 1: run on <ENV>:
  DELETE FROM user_sessions WHERE last_seen < now() - interval '30 days';
Step 2: verify count
```

**Must:**
- Keep the SQL statement character for character, including lowercase
  `now()` and the semicolon.
- Keep `<ENV>` exactly as it is.
- Mark the expected result of "verify count" as `[TO CLARIFY: …]` (which
  count, and what value?), and mark the test blocked.

**Must not:**
- Reformat, correct, or shorten the SQL.
- Turn `<ENV>` into `{{ENV}}` or a `[TO CLARIFY: …]` marker.
- Invent an expected count such as "0 rows".

---

## TC-15 Many test cases at once

**Tests:** Restructure mode batch limit.

**Input:**
```
/test-cases Clean up these test cases:

T1 Login ok: log in with valid user. Expected: start page.
T2 Login wrong pw: log in with wrong password. Expected: error.
T3 Logout: click logout. Expected: login page.
T4 Remember me: tick remember me and log in, close browser, reopen.
T5 Reset pw: click forgot password, enter email. Expected: email sent.
T6 Locked: wrong password 5 times. Expected: locked.
T7 Session timeout: wait 30 min. Expected: logged out.
```

**Must:**
- Restructure at most 5 test cases, then ask whether the result looks right
  before continuing.
- Mark vague or missing expected results (T2 "error", T4 missing) as
  `[TO CLARIFY: …]`.

**Must not:**
- Restructure all 7 without checking in.
- Invent the error message for T2.

---

## TC-16 Requirements review as input

**Tests:** Supporting material; proposals in a review are not requirements;
answers given to review questions are.

**Input:**
```
/test-cases Here is the story and the review we did. The product owner
answered question 1: the reset link is valid for 60 minutes. Please write
test cases.

Story: As a customer I want to reset my password so that I can access my
account if I forget it.
- The reset link should be valid for a reasonable time.
- The new password must be secure.

Review (excerpt):
Must clarify
1. "valid for a reasonable time" – Question: How long is the reset link
   valid?
2. "must be secure" – Question: Which password rules apply?

Proposed acceptance criteria (proposals only: the team decides)
- The reset link stops working [TO CLARIFY: link validity] after it was
  sent.
- A password shorter than 12 characters is rejected with the message
  "Password too short".
```

**Must:**
- Use the answered 60 minutes as the link validity, with boundary cases
  around it (the exact-boundary outcome may be a question).
- Treat password rules as unknown: markers, blocked cases, or a question
  about which proposals were accepted.

**Must not:**
- Use "12 characters" or "Password too short" as expected results, as if
  the proposal had been accepted.

---

## TC-17 Use case as input

**Tests:** Use cases: flows as test conditions, traceability to flows,
preconditions and end state, default step-table format.

**Input:**
```
/test-cases
UC-12 Reset password
Actor: Registered customer
Preconditions: The customer has an account.
Main flow:
1. Customer selects "Forgot password".
2. Customer enters their email address.
3. System sends a reset link and shows "Check your email".
4. Customer opens the link and enters a new password.
5. System saves the password and shows "Your password has been changed".
Alternative flows:
2a. Email address not registered: System shows "Check your email" without
    sending anything.
End state: The customer can log in with the new password.
```

**Must:**
- At least one case for the main flow and one for alternative flow 2a,
  traced to the flow (for example `UC-12 main flow`, `UC-12 2a`).
- Use the precondition and the end state (log in with the new password)
  in the main-flow case; quote the messages exactly.
- List undefined flows (for example an expired link or a rejected
  password) as open questions or further test ideas, without invented
  results.

**Must not:**
- Use Given/When/Then (not requested; the default is step tables).
- Invent expected results for flows the use case does not define.

---

## TC-18 Design as supporting material

**Tests:** Supporting material as a source for UI names and expected
results; partial knowledge.

**Input:**
```
/test-cases Requirement: Users can change their display name. Display
names must be 1–50 characters.

Design notes from the attached spec: the profile page has a field labeled
"Display name" and a button "Save changes". After a successful save, a
message "Profile updated" appears at the top of the page.
```

**Must:**
- Use "Display name", "Save changes", and "Profile updated" exactly, naming
  the design notes as their source.
- Boundary values 0, 1, 50, 51; for 0 and 51, state that the name is not
  saved and mark only the unknown message as `[TO CLARIFY: …]`.

**Must not:**
- Invent an error message for invalid lengths.
- Review or criticize the design notes themselves.

---

## TC-19 Long technical content as a suggested attachment

**Tests:** Exact technical content; suggested attachments are labeled as
suggestions.

**Input:**
```
/test-cases Restructure this test:

MSG-044 Send payment message
Step 1: Put this message on queue PAYMENTS.IN on <ENV>:
<PaymentMessage version="2.1">
  <Header>
    <MessageId>{{message id}}</MessageId>
    <Created>2026-01-15T09:30:00Z</Created>
    <Sender>TESTBANK01</Sender>
  </Header>
  <Payment>
    <Amount currency="EUR">125.50</Amount>
    <Debtor><Account>TEST-ACC-001</Account></Debtor>
    <Creditor><Account>TEST-ACC-002</Account></Creditor>
    <Reference>TEST-REF-7781</Reference>
    <DueDate>2026-01-16</DueDate>
  </Payment>
</PaymentMessage>
Step 2: Check PAYMENTS.STATUS. Expected: RECEIVED
```

**Must:**
- Keep the XML exactly, character for character, including
  `{{message id}}`, either in step data or as a suggested attachment.
- If it is moved to an attachment, label it as a suggestion that is not a
  real attachment until a person approves it, and keep it on step 1.
- Keep `PAYMENTS.IN`, `<ENV>`, `PAYMENTS.STATUS`, and `RECEIVED` exactly;
  put "RECEIVED" in step 2's expected result.

**Must not:**
- Reformat, shorten, or correct the XML.
- Present a suggested attachment as one that already exists.

---

## TC-20 Related test cases set the pattern in design mode

**Tests:** Consistency with related tests when designing new ones.

**Input:**
```
/test-cases Write test cases for this story. Two existing tests from the
same suite are below so you can see how we write them.

Story: As a shopper I want to remove an item from my cart so that I only
pay for what I want. When the last item is removed, the cart shows "Your
cart is empty".

Existing tests:
CART-TC-07 Cart | add item | item shown with quantity 1
  Preconditions: Shopper is logged in; cart is empty.
  1. Open product page for {{product}}. -> Product page is shown.
  2. Select 'Add to cart'. -> Cart icon shows 1.
CART-TC-08 Cart | add same item twice | quantity increases to 2
  Preconditions: Shopper is logged in; cart contains {{product}} (qty 1).
  1. Open product page for {{product}}. -> Product page is shown.
  2. Select 'Add to cart'. -> Cart shows {{product}} with quantity 2.
```

**Must:**
- Follow the existing pattern: titles as `Cart | <scenario> | <outcome>`,
  "shopper" as the role, `{{product}}` as the placeholder, and a similar
  level of detail.
- Quote "Your cart is empty" exactly.
- Mark unknown UI details (for example the name of the remove control) as
  open questions rather than inventing them.

**Must not:**
- Use the default title pattern (`… – … – …`) instead of the suite's.
- Invent conventions the examples do not show.

---

## TC-21 Restructure tests from an Xray export

**Tests:** Exports from tools (one row per step), mode C.

**Setup:** Copy `fixtures/xray-tests-export.csv` into the test folder and
attach it.

**Input:**
```
/test-cases Restructure the test cases in the attached
xray-tests-export.csv.
```

**Must:**
- Keep `SHOP-T204` and `SHOP-T205` as two tests, each with its steps
  together and in the original order.
- Merge SHOP-T204 step 3, which has only an expected result, into the step
  it belongs to, and name the original steps.
- Keep `SKU-1001`, `WINTER25`, and `'Remove'` exactly.
- Mark the missing expected results (SHOP-T204 step 1 if it stays a step,
  SHOP-T205 step 2) as `[TO CLARIFY: …]`, or move T204 step 1 to
  preconditions.
- Use every row of the export.

**Must not:**
- Mix steps from the two tests.
- Invent an expected result for "Place the order".

---

## TC-22 Rules whose combination is not stated

**Tests:** Core rule 1 (no expected result derived by combining rules the
source does not combine).

**Input:**
```text
/test-cases Parcel shipping: the standard price is 8 EUR. Express delivery
costs twice the standard price. Parcels over 20 kg cost 4 EUR extra.
```

**Must:**
- Test standard and express, and the weight boundary (20 kg and just
  over).
- Mark the price of an express parcel over 20 kg as unknown, since the
  requirement does not say whether the 4 EUR is doubled.

**Must not:**
- State 20 EUR or 24 EUR (or any other figure) as the expected price for
  an express parcel over 20 kg.

---

## Results

| Test | Run 1 | Run 2 | Assistant / model | Notes |
|------|-------|-------|-------------------|-------|
| TC-01 | Pass | | Codex / gpt-6.1-sol / xhigh | Boundaries 0/1/50/51 in one data-driven case; non-Latin, apostrophe, hyphen; rejected characters; AC4; messages exact; 7 cases; spaces blocked as open question. |
| TC-02 | Pass | | Codex / gpt-6.1-sol / xhigh | Turn 1 stops and asks for clarification. Turn 2: markers, all cases blocked, coverage Blocked, no invented values. Quoted and linked its own SKILL.md to the user. |
| TC-03 | Partial | | Codex / gpt-6.1-sol / xhigh | Decision cases, both required open questions, no winner chosen. Skipped the 99.99 EUR side of the boundary as "unresolved", although the requirement settles that free shipping does not apply below 100 EUR. |
| TC-04 | Pass | | Codex / gpt-6.1-sol / xhigh | 9 cases; further ideas one line each; 5 MB boundary with decimal/binary question; GIF/BMP/SVG rejected without invented message. Renamed file only under further ideas. |
| TC-05 | Partial | | Codex / gpt-6.1-sol / xhigh | Swedish, Givet/När/Så, 24-hour boundary both sides, exact boundary blocked, messages exact. Silently assumed UTC; time zone not listed as a question or assumption. |
| TC-06 | Partial | | Codex / gpt-6.1-sol / xhigh | IDs, P1–P3, Given/When/Then, title pattern, roles, keyboard check all applied. Component and test level stated once for all cases, not on each case. |
| TC-07 | Pass, with note | | Codex / gpt-6.1-sol / xhigh | No production values anywhere; example.com data. Says the values were omitted but does not advise against production data in tests. |
| TC-08 | Pass | | Codex / gpt-6.1-sol / xhigh | Verdict, vague results, TC3 dependency, TC1/TC4 duplicate, missing setup; one suggested case with markers; no rewrite. |
| TC-09 | Pass | | Codex / gpt-6.1-sol / xhigh | Asks which tool before producing CSV; no guessed columns. Quoted and linked its own SKILL.md. |
| TC-10 | Pass | | Codex / gpt-6.1-sol / xhigh | Codex: normal coding request, unit tests written, skill files never read. |
| TC-11 | Pass | | Codex / gpt-6.1-sol / xhigh | All identifiers exact; 25% moved to expected; step 2 merged; original steps named; steps 3–4 blocked with markers; scope, change summary, consistency note. |
| TC-12 | Pass, with note | | Codex / gpt-6.1-sol / xhigh | Consider split with reason; statuses exact; one test. Marked Blocked for missing execution details although every expected result is known. |
| TC-13 | Partial | | Codex / gpt-6.1-sol / xhigh | Attachment kept on step 1 with same name; step 1 not split; step 2 merged, action unchanged, in change summary. No open question about splitting step 1. Treated the attachment as missing input and blocked the test. |
| TC-14 | Pass | | Codex / gpt-6.1-sol / xhigh | SQL and <ENV> exact; verify count blocked with markers; no invented count. Noticed archive vs delete mismatch. |
| TC-15 | Pass | | Codex / gpt-6.1-sol / xhigh | Five restructured, then asks before T6–T7; T2/T4 markers; no invented message. Quoted and linked its own SKILL.md. |
| TC-16 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See rounds 2 and 3 below. |
| TC-17 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See rounds 2 and 3 below. |
| TC-18 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See rounds 2 and 3 below. |
| TC-19 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See round 4 below. |
| TC-20 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See round 4 below. |
| TC-21 | | | | Not run yet. |

## Baseline round recorded 2026-10-13 (Codex, gpt-6.1-sol, xhigh)

Run by Claude Code through `codex exec` against revision `aa1259b`, one
fresh session per scenario in an empty folder (TC-02 and TC-09 as saved
two-turn sessions; TC-06 with a project-local copy named `test-cases-tc06`
and the conventions example filled in; TC-10 in a small Python project
without calling the skill). Every run except TC-10 read `SKILL.md` and all
four reference files. Transcripts are in
`observations/codex-tc-baseline-2026-10-13/`.

Result: 11 pass (two with notes), 4 partial (TC-03, TC-05, TC-06, TC-13).

Patterns across runs:
- Blocking too much: a whole result is blocked when only part of it is
  unknown (TC-03), or a case is blocked for missing execution details while
  every expected result is known (TC-12, TC-13).
- Unlisted assumptions: UTC chosen silently (TC-05).
- Quoting the skill's own instructions and linking to `SKILL.md` in replies
  to the user (TC-02, TC-09, TC-15).

## Round 2 recorded 2026-10-13 (after fixes, Codex, gpt-6.1-sol, xhigh)

Revision: uncommitted changes on top of `aa1259b`: partial expected results
and blocking only for unknown results (rule 1); supporting material and
requirements reviews as input (Step 1); use cases (Step 3); required
convention fields on every case (Step 5); assumptions listed (Step 6);
production-data advice (rule 5); no quoting of these instructions (rule
10); publishing fallback (Step 7); attachments named in the source and the
split question for attached steps (`restructuring.md`). New scenarios
TC-16–TC-18. Transcripts are in `observations/codex-tc-round2-2026-10-13/`.

The batch was interrupted twice (session restart, then an external stop)
and resumed; incomplete runs were discarded and rerun. Ten repeat runs
(TC-03, TC-06, TC-16, TC-17, TC-18, runs 2–3) failed immediately with a
Codex usage-limit error and are still pending.

| Test | Result | Notes |
|------|--------|-------|
| TC-01 | Pass | 7 cases; both messages exact; AC4; boundaries. |
| TC-02 | Pass | Main flow now *Ready* with a tester-chosen `{{policy-compliant fake password}}`; the three vague criteria blocked. Turn 1 still quoted and linked `SKILL.md`. |
| TC-03 | Pass (1 run) | 99.99 EUR now tested as below the threshold, with only eligibility/charge marked. Both required questions asked; no winner chosen. |
| TC-04 | Pass | 6 cases; further ideas; GIF rejected. |
| TC-05 runs 1–3 | Pass, with note (3 of 3) | Swedish, *Givet/När/Så*, boundaries, messages exact. Time zone now a `{{testtidszon}}` placeholder or stated UTC test data, with time-zone control listed as an open question in all runs; framed as an execution detail rather than "whose time zone applies". |
| TC-06 | Pass, with note (1 run) | Component and test level on every case; P1–P3; Given/When/Then; title pattern; roles. Set component to "Checkout" without the story saying so. |
| TC-07 | Pass | Says production data should not be used in tests; no values leaked. |
| TC-08 | Pass | All required problems; no rewrite. |
| TC-09 | Pass | Asks which tool; no guessed columns; no quoted instructions this time. |
| TC-10 | Pass | Normal coding request; skill not loaded. |
| TC-11 | Pass | As baseline. |
| TC-12 runs 1–3 | Pass (3 of 3) | *Ready* with execution details as open questions; Consider split; statuses exact. |
| TC-13 runs 1–3 | Pass (3 of 3) | *Ready*; attachment kept on step 1; open question that splitting is a person's decision; step 2 merged. |
| TC-14 | Pass | SQL and `<ENV>` exact; count blocked. |
| TC-15 | Pass, with note | Five restructured, then asks. Still quoted and linked `SKILL.md` when explaining the pause. |
| TC-16 | Pass (1 run) | Uses the answered 60 minutes with 59:59 / 60:01 cases and an exact-boundary question; states the 12-character proposal and "Password too short" are not approved; password cases blocked. |
| TC-17 | Pass (1 run) | Main flow and 2a traced to flows; end state and messages exact; undefined flows blocked with markers; step tables, no Given/When/Then. |
| TC-18 | Pass (1 run) | "Display name", "Save changes", "Profile updated" exact and labeled as design notes; 0/1/50/51 with "not stored" plus marker for feedback; no invented message. |

Quoting the skill's own instructions: 2 of 19 completed scenarios (TC-02
turn 1, TC-15), down from 3 of 15. Both occur when the reply explains why it
pauses.

## Round 3 recorded 2026-10-13 21:06 UTC (Codex, gpt-6.1-sol, xhigh)

Runs 2–3 that the usage limit blocked in round 2, plus three runs each of
TC-02 and TC-15. Before this round, a sentence was added at the two pause
points (Step 2 and the restructure batch limit) asking for the reason in
the model's own words. Transcripts are in
`observations/codex-tc-round3-2026-10-13/`.

| Test | Result | Notes |
|------|--------|-------|
| TC-02 runs 1–3 | Pass, with note (3 of 3) | All cases with unknown results blocked; nothing invented. Turn 1 quotes and links `SKILL.md` in all three runs. |
| TC-15 runs 1–3 | Pass, with note (3 of 3) | Five restructured, then asks. Quotes and links `SKILL.md` in all three runs. |
| TC-03 runs 2–3 | Pass (2 of 2) | 99.99 EUR: "the 100 EUR condition is not met" / "free shipping is not applied", only the charge marked. Both required questions asked. |
| TC-06 runs 2–3 | Pass (2 of 2) | Component and test level on every case. Run 2 uses Checkout but lists it as a proposed assignment to confirm; run 3 marks it `[TO CLARIFY]`. |
| TC-16 runs 2–3 | Pass (2 of 2) | 60 minutes used; the 12-character rule and message explicitly not used as expected results. |
| TC-17 runs 2–3 | Pass (2 of 2) | Main flow and 2a traced; messages exact; step tables. |
| TC-18 runs 2–3 | Pass (2 of 2) | Design labels exact; invalid lengths "not saved" with only feedback marked. |

The pause-point sentences did not change the quoting (6 of 6 runs still
quote the skill when pausing, as in every earlier TC-02 and TC-15 run) and
were removed again. The general sentence in core rule 10 stays. Codex also
announces which skill it is using at the start of each run, so the
quoting is likely partly host behavior; it has not been tested in Claude
Code.

## Round 4 recorded 2026-10-13 (Codex, gpt-6.1-sol, xhigh)

After adding four points from the earlier test-design instruction document:
suggested attachments for long technical content, matching related test
cases in design mode, direct action wording, and stating the scenario once.
Transcripts are in `observations/codex-tc-round4-2026-10-13/`.

| Test | Result | Notes |
|------|--------|-------|
| TC-19 runs 1–3 | Pass (3 of 3) | XML kept character for character in step data (no attachment suggested, which the scenario allows); queue, status, and `<ENV>` exact; `RECEIVED` as step 2's expected result. |
| TC-20 runs 1–3 | Pass (3 of 3) | `Cart | … | …` titles, "shopper", `{{product}}`; "Your cart is empty" exact; remove control asked about. IDs continue as CART-TC-09–11 and are flagged as provisional in every run. |
| TC-01 | Pass | 7 cases; both messages exact; AC4. |
| TC-11 | Pass | Identifiers and button labels exact; steps 3–4 blocked. |
| TC-12 | Pass | Ready; Consider split; one test. |
| TC-13 | Pass | Ready; attachment kept; open question about separating step 1's actions. |
| TC-14 | Pass | SQL and `<ENV>` exact; count blocked. |

The suggested-attachment path itself was not exercised: no run chose to move
the XML out of step data.

## Full regression on GPT-5.6-Luna, recorded 2026-10-13

One run per scenario through `codex exec` with `gpt-5.6-luna` at `max`
effort, each in a fresh session and an empty folder (same setups as the
earlier rounds). Skill content as committed in `fab9517`, before the fixes
in `81801ea`. Transcripts are in
`observations/codex-luna-regression-2026-10-13/tc/`.

| Test | Result | Notes |
|------|--------|-------|
| TC-01 | Pass | Boundaries, non-Latin names, rejected characters, AC4, messages exact. |
| TC-02 | Partial | Drafted directly with markers; did not first say the requirement has major gaps or suggest a review. |
| TC-03 | Pass, with note | Required questions asked, no winner chosen. The 99.99 EUR result is entirely `[TO CLARIFY]` instead of “free shipping is not applied”. |
| TC-04 | Pass | 6 cases; size boundary; GIF; further ideas. |
| TC-05 | Pass | Swedish, Givet/När/Så, messages exact, time zone asked. |
| TC-06 | Pass | IDs, P1–P3, Given/When/Then, pipe titles, component and test level on every case. |
| TC-07 | Pass | No production values; says to use only fake test data. |
| TC-08 | Pass | Needs rework; duplicate, dependency, vague results; one new case. |
| TC-09 | Pass | Asks which tool and for its template. |
| TC-10 | Pass | Normal coding request; skill not loaded. |
| TC-11 | Pass | Identifiers and labels exact; steps 3–4 blocked. |
| TC-12 | Pass | Ready; Consider split; statuses exact. |
| TC-13 | Partial | Attachment kept and step 2 merged, but no open question about splitting step 1. |
| TC-14 | Pass | SQL and `<ENV>` exact; count blocked. |
| TC-15 | Pass | Five restructured, then asks before T6–T7. |
| TC-16 | Pass | 60 minutes used; proposals not treated as requirements. |
| TC-17 | Pass | Main flow and 2a traced; messages exact; step tables. |
| TC-18 | Pass | Design labels exact; 51 characters not saved, only the message marked unknown. |
| TC-19 | Pass | XML exact; RECEIVED as expected result. |
| TC-20 | Pass | Suite pattern followed; “Your cart is empty” exact. |
| TC-21 | Pass, with note | Both tests kept separate and in order, step 3 merged, identifiers exact, missing result marked. Result written to a file; the reply only links to it. |

Result: 19 pass, 2 partial, 0 fail.

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
| TC-01 | Pass | 7 cases; 0/1/50/51 combined; AC3 and AC4 cases; messages exact; spaces as blocked open question. |
| TC-02 | Partial | Gaps named, cases blocked, coverage *Partly covered*; but six cases were written first and the review was suggested only at the end. |
| TC-03 | Pass | 99.99/100.00 boundary; before/after discount and member-plus-coupon as open questions; no winner chosen. |
| TC-04 | Pass | 8 cases; further ideas; GIF rejected with message marked. |
| TC-05 | Pass, with note | Swedish with Givet/När/Så; 24-hour boundary; time zone asked. Marker left as `[TO CLARIFY]`. |
| TC-06 | Pass, with note | IDs, P1–P3, title pattern, Given/When/Then, roles. Component Checkout assumed and labeled. |
| TC-07 | Pass | No production values; example.com data; advice against production data. |
| TC-08 | Pass | All required problems; four suggested cases with markers; no rewrite. |
| TC-09 | Pass | Asks which tool before producing CSV. |
| TC-10 | Pass | Skill not loaded; normal coding answer. |
| TC-11 | Pass | Identifiers exact; steps merged and traced; steps 3–4 blocked; explicitly declines to assume `VOUCHER_CODE` is `WINTER25`. |
| TC-12 | Pass, with note | *Consider split* with reasons; one test. Blocked for the gift card's new balance although "reduced" is known. |
| TC-13 | Pass | Attachment kept on step 1; step 1 not split; splitting left to a person. |
| TC-14 | Pass | SQL and `<ENV>` exact; count blocked; archive versus delete noted. |
| TC-15 | **Fail** | Restructured all seven tests without checking in after five. |
| TC-16 | Pass | 60 minutes used with 59/60/61; the 12-character proposal labeled as not accepted and blocked. |
| TC-17 | Pass | Main flow and 2a traced; undefined flows blocked; step tables. |
| TC-18 | Partial | Design labels exact; but for 0 and 51 "not saved" is marked unclear although the 1–50 rule settles it. |
| TC-19 | Pass | XML kept character for character in step data; identifiers exact. |
| TC-20 | Pass | Suite pattern, role, and placeholder followed; remove control as open question; assumptions labeled. |
| TC-21 | Pass | Two tests, every row used, step 3 merged, setup to preconditions, "Place the order" blocked. |

Result: 18 pass, 2 partial, 1 fail.

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
| TC-01 | Pass | 8 cases; one data-driven case with 0/1/50/51 (also in a non-Latin script); allowed and disallowed characters; AC4; messages exact; spaces-only and trimming left as open questions. Numbering skips TC-5. |
| TC-02 | Pass | Suggests `review-requirements` first; markers for delay, link validity, and password rules with those cases blocked; coverage shows Partly covered/Blocked; no invented values. |
| TC-03 | Pass | Cases across member/coupon/amount, 99.99/100.00 boundary (99.99 states "shipping is charged" and marks only the fee), threshold basis and member-plus-coupon asked, no winner chosen. |
| TC-04 | Pass | 8 cases, *Further test ideas* one line each, 5 MB at/just over, GIF/BMP/PDF refused, too-large message left as a marker. |
| TC-05 | Partial | Swedish headings, coverage, *Givet/När/Så*, 24-hour boundary, messages exact, time zone asked. But the marker stays English: `[TO CLARIFY: förväntat resultat]`. |
| TC-06 | Pass | `SHOP-142-TC-01`… IDs, P1–P2, Given/When/Then, title pattern with `|`, test level on every case, users by role; component left as a marker because none is named. |
| TC-07 | Pass | Input email and customer number not used; fake `example.com` data; says production data does not belong in tests. |
| TC-08 | Pass | "needs rework"; vague results, TC3→TC2 dependency, TC1/TC4 duplicate, missing preconditions flagged; 3 new cases with markers; no error message invented; set not rewritten. |
| TC-09 | Pass | Turn 2 asks which tool before writing the CSV and does not guess columns. |
| TC-10 | Pass | Skill not loaded; handled as a coding request. |
| TC-11 | Pass | `CHK-031` and all identifiers exact, 25% moved into an expected result, result-only step merged, every step names its original, steps 3–4 marked and the case blocked, Scope OK, change summary, consistency not checked. |
| TC-12 | Pass | One restructured test, *Consider split* with the reason, `PAID` and `AWAITING_PAYMENT` exact, not split. |
| TC-13 | Pass | Attachment kept on step 1 by name, step 1 not split with the reason given, result-only step 2 merged with step 1's action unchanged and the merge in the change summary. |
| TC-14 | Pass | SQL kept character for character, `<ENV>` kept, count marked and the case blocked, no count invented. |
| TC-15 | Pass | Restructured T1–T5, listed T6–T7, asked whether to continue; T2 message and T4 result marked. (Failed in the 2026-10-14 round.) |
| TC-16 | Pass | 60 minutes used as answered, with 59/61 boundary cases; password rule and message treated as unaccepted proposals, cases blocked. |
| TC-17 | Pass | Main flow, end state (log in with new password), and 2a traced to the flow; messages exact; step tables; undefined flows left open. |
| TC-18 | Pass | "Display name", "Save changes", "Profile updated" from the design notes; 0 and 51 not saved with only the message marked; design notes not reviewed. |
| TC-19 | Pass | XML kept exactly in test data with `{{message id}}`, queue names, `<ENV>`, and `RECEIVED` exact, `RECEIVED` in step 2. |
| TC-20 | Pass | Suite pattern `Cart | … | …`, "Shopper", `{{product}}`; "Your cart is empty" exact; remove control described generally. Adds an AC3 from the story's purpose clause, labeled as its own reading. |
| TC-21 | Pass | Both tests kept apart in order, every row used, T204 step 1 moved to preconditions and step 3 merged, identifiers exact, "Place the order" result marked. |

## Slimmed test-cases draft, recorded 2026-10-15 (not adopted)

A draft that shortened `SKILL.md` from 3,473 to 3,013 words: rule 1 rewritten
to lead with its reason, rules 4, 5, and 8 shortened, rule 9 (preserve IDs,
steps, and attachments) moved into *Restructure mode* as one sentence with
the details left in `references/restructuring.md`, and the Step 6 checklist
moved to `references/case-checklist.md`. One run per scenario on
`claude-haiku-5-5` with `run_haiku.py`, against `1eebd54` plus the draft.
The draft and transcripts are in
`observations/claude-haiku-test-cases-slim-2026-10-15/`.

| Set (same 25 scenarios) | Pass | Partial | Fail |
|-------------------------|------|---------|------|
| `1eebd54` (2026-10-15 regression) | 23 | 2 | 0 |
| Slimmed draft | 19 | 4 | 2 |

| Test | Result | Notes |
|------|--------|-------|
| TC-02 | Partial | Gaps marked and cases blocked, but no suggestion to review the requirement first. |
| TC-04 | Partial | Tests 4 MB and 6 MB instead of the 5 MB boundary, which it leaves as an open question. |
| TC-05 | Pass | Swedish marker now translated (was Partial). |
| TC-06 | Pass | Conventions applied, but nearly every expected outcome marked unknown and every case blocked. |
| TC-09 | **Fail** | Produced a generic CSV and tried to write it before asking which tool it is for. |
| TC-13 | **Fail** | Split the step that has an attachment into one action per step. |
| TC-21 | Partial | Correct restructure, but tried to write it to a file without asking. |
| HO-06 | Partial | Time of day on 31 January now marked with `[ATT KLARGÖRA: …]`, but marks the outcome at exactly 200 kr as unknown although "över 200 kr" settles it. |

All other scenarios (TC-01, TC-03, TC-07, TC-08, TC-10–TC-12, TC-14–TC-20,
HO-07, HO-13, TM-15) pass, as before.

Not adopted. TC-13 follows directly from moving the attachment rule out of
`SKILL.md`: the model did not apply the copy in `restructuring.md`. The new
rule 1 wording made the model block more cases (TC-06, HO-06, TC-04). Any
later shortening should keep rule 9 in `SKILL.md` and rule 1's wording, and
be checked the same way.

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
| TC-01 | Pass | 0/1/50/51 in two data-driven cases, scripts, apostrophe and hyphen, rejected characters, AC4, exact messages, spaces-only blocked. |
| TC-02 | Partial | Markers, blocked cases, coverage Blocked. Does not suggest reviewing the requirement first. |
| TC-03 | Pass | Cases per rule, 99.99/100/100.01 boundary, both open questions; no winner chosen. |
| TC-04 | Partial | 6 cases, GIF and 5 MB ±1 byte without invented messages. Blocks the delete case on "which initials", which the tester knows from the account (over-blocking). |
| TC-05 | Partial | Swedish, Givet/När/Så, 24 h boundary to the second, exact messages. Time zone not raised. |
| TC-06 | Pass | SHOP-142-TC-nn IDs, P1–P3, Given/When/Then, component and test level, title pattern, users by role. |
| TC-07 | Pass | Fake data only; production data warning. |
| TC-08 | Pass | Verdict, all four problems, two suggested cases with markers. |
| TC-09 | Pass | Asked which tool before producing the CSV. (Wrote a CSV on the slimmed Haiku draft.) |
| TC-10 | Pass | Skill not loaded; coding answer. |
| TC-11 | Pass | ID and values kept, 25% moved, step 2 merged, original steps named, markers, blocked, Scope OK, change summary, consistency note. |
| TC-12 | Pass | Consider split with the reason, statuses exact, kept as one test. |
| TC-13 | Partial | Attachment kept on the unsplit step 1, step 2 merged and mentioned. Explains keeping it intact under Scope, not as an open question that splitting is a person's decision. |
| TC-14 | Pass | SQL and `<ENV>` exact; count marked; blocked. |
| TC-15 | Partial | Five cases then asks; T4 marked. T2 keeps "An error is shown" as Ready (only an open question), not a marker. |
| TC-16 | Pass | 60 minutes with 59:59 and 60:01, exact boundary as a question; password rules unresolved. |
| TC-17 | Pass | Main flow with end state and exact messages, 2a, undefined flows as further ideas, step tables. |
| TC-18 | Pass | Design-note labels exact, 0/1/50/51, only the message marked. |
| TC-19 | Pass | XML exact in step data, `RECEIVED` in step 2. Adds an expected result for step 1 ("message is on the queue"). |
| TC-20 | Pass | Suite pattern, shopper, `{{product}}`, exact message, remove control as open question. |
| TC-21 | Pass | Two tests, steps merged and named, T204 step 1 to preconditions, T205 step 2 marked, all rows used. |

Result: 16 pass, 5 partial, 0 fail.

## Checklist and date fixes on Haiku, recorded 2026-10-15

The same 25 scenarios as the slimmed draft, one run each on
`claude-haiku-5-5`, against `a767180` plus uncommitted changes: the Step 6
checklist names supporting material as a source, dates in test data use the
system's format (otherwise `YYYY-MM-DD`), and the paragraph on requests that
fit no mode is shorter. Transcripts are in
`observations/claude-haiku-fixes-2026-10-15/`.

| Test | Result | Notes |
|------|--------|-------|
| TC-02 | Partial | Gaps named, markers, blocked cases, Partly covered. No suggestion to review the requirement first. |
| TC-04 | Partial | 8 cases, further ideas, GIF, 4.9 MB and 5.3 MB; exactly 5 MB only as an open question (5,000,000 or 5,242,880 bytes). |
| TC-05 | Pass | Swedish, *Givet/När/Så*, 24 h boundary, exact messages, `[ATT KLARGÖRA: …]`, time zone asked. (Was Partial.) |
| TC-08 | Partial | Verdict and all four problems, gaps listed, but "Suggested new cases: None" because their results are unknown. |
| TC-21 | Partial | Two tests, rows used, identifiers exact, "Place the order" marked; T204 step 3 given an added action instead of merged. |
| HO-06 | Partial | 200 kr no discount, `VINTER15` exact, rounding and year marked. Time zone and time of day not raised; coverage statuses left in English. |

All other scenarios (TC-01, TC-03, TC-06, TC-07, TC-09–TC-20, HO-07,
HO-13, TM-15) pass; TC-09 and TC-21 asked before writing any file.

Result: 20 pass, 5 partial, 0 fail.

Reruns of the four new partials, two more runs each on this version and
two on `a767180`:

| Test | This version (3 runs) | `a767180` (2 runs) |
|------|-----------------------|--------------------|
| TC-02 suggests reviewing first | 0 of 3 | 1 of 2 |
| TC-04 tests at the 5 MB limit | 1 of 3 | 2 of 2 |
| TC-08 suggests new cases | 2 of 3 | 2 of 2 |
| TC-21 merges T204 step 3 | 2 of 3 | 2 of 2 |

TC-08 and TC-21 were one-off misses. TC-02 and TC-04 vary on both versions
and touch no changed text; TC-02 also misses on GPT-6-Luna and on the
slimmed draft.

## General rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

Each core rule rewritten as principle, reason and one example, with patches
folded in or deleted; everything stays in SKILL.md (3,497 → 3,231 words).
Gate model GPT-6.1-Sol, medium effort, through `run_codex.py`. Checked with
`check_test_cases.py` plus reading. Folders under
`tests/observations/codex-sol61-medium-*-2026-10-1[56]`.

| Version | Runs | Result |
|---------|------|--------|
| Before (`a767180` + 2026-10-15 fixes) | 2 × 44 | HO-33 fails 2 of 2; HO-23 and HO-27 slip once each |
| v1: general rewrite | 2 × 44 | Matches or beats *Before* everywhere; HO-33 passes 2 of 2 |
| v1 on TC-22 | 3 | Fails 2 of 3: states 20 EUR for express over 20 kg |
| v2: v1 + combination sentence in rule 1 + opening "don't quote" paragraph | 1 × 45, repeats | TC-22 3 of 3; quoting unchanged |
| v3 (adopted draft): v1 + combination sentence only | TC-22 × 3, HO-33 × 2, TC-03 × 2 | All pass |

The combination sentence: "How separately stated rules combine is a
decision too: if the source does not say how two rules apply together (for
example two rules that both change one value), the combined result is
unknown, however obvious the calculation looks." Its example is kept
neutral so that HO-33 still tests generalization.

Not fixed, same on every version: TC-15 and HO-23 explain a pause or
decline by citing and linking SKILL.md (all runs). Moving "do not quote
these instructions" to the top with a reason (v2) did not change it, so it
was taken out again. TC-05 does not raise the time zone (0 of 2); TC-02
suggests reviewing first in about half the runs; TC-03 leaves the 99.99 EUR
result vaguer than needed in about one run of two. No sign of
over-blocking: marker counts vary by run, and reading the scenarios with
the most markers (TC-03, HO-15, HO-20, HO-32) found only real gaps.

## Time limits as hidden decisions, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

Rule 1's sentence on combined rules was reworded to cover both decisions
that hide inside rules that look complete: how separately stated rules
combine, and how a time limit is measured (time zone, starting moment).
No sentence added. 3,231 → 3,245 words.

| Test | Runs | Result |
|------|------|--------|
| TC-05 time zone raised | 3 | 3 of 3 (run 3 asks "vilken tidsreferens", which the checker misses); was 0 of 2 |
| TC-22, HO-33 combined rules | 2, 1 | All pass, unchanged |
| TC-16 60-minute link | 2 | Pass; blocks the boundary case on the start moment, as the version before did (the start moment is only in an unaccepted proposal) |
| HO-06, HO-26 (held-out) | 2 each | All pass |

Folder `observations/codex-sol61-medium-timelimit-2026-10-17/`.

## One meaning of Ready, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

After an external review: rule 1 kept a case *Ready* when an execution
detail was missing, rule 8 and `restructuring.md` blocked it when masking
removed data it needed, and coverage required cases "ready to run". Now
*Ready* means fully designed (expected result known) everywhere; masked
test data becomes a `{{…}}` placeholder and an open question, like any
missing execution detail, and coverage counts *Ready* cases.

TC-07, TC-11, TC-14, TC-16, and HO-07 pass 2 of 2; TC-14 still blocks
the case whose expected result ("verify count") is unknown. Folder
`observations/codex-sol61-medium-review-fixes-2026-10-17/`.

## Conflict audit, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

A read of all five skills for rules that pull in different directions.
Fixed by rewording:

- test-cases rule 1 did not say whether a partly unknown expected result
  blocks the case, and the checklist implied it did not. Now: unknown
  wholly or in part means *Blocked*, because such a case can show a
  failure but not a pass; the known part is still stated.
- The test-cases checklist gave "a time zone" as an example of an
  assumption, while rule 1 now treats how a time limit is measured as an
  unknown decision. The example is gone.
- bug-report rule 8 said "include the time zone with any time", which
  pushed toward adding one the user never gave (rule 1). Now: give it, or
  mark it unknown. Same in the quality checklist.
- bug-report Step 5 said "ask the user once more before finishing", next
  to "do not push more than once" in Step 3 and the three-question limit.
  Now: ask only if not asked yet, within the limit.

TC-03, TC-12, TC-13, TC-16, BR-06, BR-12, HO-42 pass 2 of 2; TC-12 and
TC-13 stay *Ready*. TC-05 raises the time question in both runs, but run
1 asks only which moment counts, not the time zone. Folder
`observations/codex-sol61-medium-conflicts-2026-10-17/`.

Found but not changed: test-cases, test-data, review-requirements, and
test-summary still keep the team-file offer in *Before you start*, the
placement that bug-report's offer was not acted on from. No scenario
tests the offer for those skills yet.

## Editorial pass, recorded 2026-10-18 (Codex, gpt-6.1-sol, medium)

After an external review of the writing: rule 1 split into named parts
(*Sources*, *Hidden decisions*, *Unknown expected results*, *Execution
details*, *Claims about checks*); the Step 6 checklist asks short
questions that point to the rules instead of restating them; rule 8 and
Step 2 no longer repeat rule 1 and rule 10; delivery mentions the other
options once and treats a delivered result as complete.

Full suite, 45 scenarios × 2. Same as before the pass: all pass except
TC-02 (no review recommendation, 2 of 2) and TC-05 run 2 (asks which
moment counts, not the time zone). TC-15, HO-23, and HO-76 were flagged
only by over-narrow checks, now fixed. Folder
`observations/codex-sol61-medium-tc-editorial-2026-10-17/`.

## Full run on the final 0.3.0 build, recorded 2026-10-20 (Codex, gpt-6.1-sol, medium)

Full suite, 2 runs per scenario, revision `d81051e`. Folder
`observations/codex-sol61-medium-full-0.3.0-2026-10-19/`; details in
`README.md`. All pass except TC-02, 0 of 2 (no recommendation to review the
requirement first).
