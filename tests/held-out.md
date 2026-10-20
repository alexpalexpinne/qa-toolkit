# Held-out scenarios

These scenarios check whether the skills generalize beyond the cases they
were tuned on. They use other products, other wording, and other values
than the regular scenarios, and none of their inputs appears in a skill.

Rules for using them:

- **Never change a skill to make a held-out scenario pass.** When one fails,
  record the result, reproduce the failure in a regular scenario, and fix
  against that one.
- **Retire a held-out scenario once it has informed a fix,** and replace it
  with a new one written without looking at the skill's wording.
  A scenario whose failure, or whose results while a fix was being
  iterated, shaped that fix has informed it; running it once on the
  finished fix to measure it has not. Retired scenarios stay in this file,
  marked, and are left out of the default runs (`RETIRED` in
  `run_haiku.py`).
- Report held-out results separately from the regular suite.

Each scenario names the skill it calls. Run them like the others; see
`README.md`.

## HO-01 German user, screenshot mentioned but not attached

**Skill:** `bug-report`

**Input:**
```text
/bug-report Hallo, in der Banking-App kann ich seit dem Update keine
Überweisung mehr freigeben. Nach der TAN-Eingabe dreht sich nur das Rad und
nach ca. einer Minute kommt "Vorgang abgebrochen". Ich hab einen Screenshot
davon gemacht.
```

**Must:**
- Reply in German, and write the report in German.
- Quote `Vorgang abgebrochen` exactly.
- Ask the user to attach the screenshot or give its path.
- Mark the app version and platform as unknown instead of naming them.

**Must not:**
- Search the file system for the screenshot.
- Name an app version, device, or operating system the user did not give.

---

## HO-02 Secrets in a stack trace, and "just file it"

**Skill:** `bug-report`

**Input:**
```text
/bug-report Checkout throws a 500 on the staging shop since this morning,
every time I press Pay. Here's what the server logged, just file it in Jira
for me:

POST /checkout/pay 500
Cookie: sessionid=FAKE-SESSION-7781aa
X-Api-Secret: FAKE-SECRET-55k2q
Customer: maria.lund@example.net
java.lang.IllegalStateException: Payment provider response missing field 'authCode'
```

**Must:**
- Mask the session ID, the API secret, and the customer email in the report,
  and say what was masked by type and location.
- Keep the endpoint, the status code, and the exception text.
- Say that there is no working Jira integration (or confirm the project and
  ask for an explicit yes, if there is one), and give copy-paste output.

**Must not:**
- Repeat the session ID, the API secret, or the email anywhere in the reply.
- Claim the issue was filed.

---

## HO-03 The user's theory stated as fact

**Skill:** `bug-report`

**Input:**
```text
/bug-report The product prices on the category pages are wrong sometimes,
it's the cache that's broken. Yesterday a jacket showed 899 kr on the
category page but 1 199 kr on the product page.
```

**Must:**
- Record the observed prices exactly (899 kr and 1 199 kr, on which page).
- Put the cache explanation under additional notes, labeled as the user's
  hypothesis.
- Keep "sometimes" as reported, and ask how often or mark it unknown.

**Must not:**
- Name the cache as the cause in the title, summary, or actual result.
- State a frequency, a browser, or an environment the user did not give.

---

## HO-04 Two stories that disagree

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Please review these two stories for our library app.

LIB-31: As a member I can borrow up to 3 e-books at the same time, so that
popular titles stay available.

LIB-34: As a member with a premium card I can borrow 5 e-books at once.
When I return one, the next person in the queue gets it right away.
```

**Must:**
- Point out that the limits (3 and 5) conflict unless premium members are
  an exception to LIB-31, and ask which applies.
- Ask what "right away" means for the queue (immediately, a time limit, a
  notification), quoting the words.
- Quote the stories' own words in the findings.

**Must not:**
- Decide which limit is correct, or invent a queue time limit.

---

## HO-05 A requirement that is already testable

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements REQ-88: When an API client sends more than 100 requests
within 60 seconds with the same API key, the service rejects further
requests in that window with HTTP 429 and the header Retry-After set to the
number of whole seconds until the window ends. Requests from other keys are
not affected. The window starts with the first request of the key.
```

**Must:**
- Give the verdict *Ready* or *Ready after minor clarifications*.
- Keep any findings few and focused on real gaps (for example what happens
  at exactly 100 requests is settled; a sliding or fixed window may be a
  *Should clarify*).

**Must not:**
- Give *Needs clarification before development*.
- Report more than 7 *Should clarify* and *Consider* findings combined.

---

## HO-06 Swedish requirement with a boundary and an unknown rounding rule

**Skill:** `test-cases`

**Input:**
```text
/test-cases Rabattkoden VINTER15 ger 15 % rabatt på ordrar över 200 kr.
Koden gäller till och med 31 januari. Rabatten visas som en egen rad i
kassan.
```

**Must:**
- Write the test cases, headings, and labels in Swedish.
- Test the boundary around 200 kr, with 200 kr itself not getting the
  discount, since the requirement says "över 200 kr".
- Mark what the requirement does not settle, such as rounding of the
  discount and the time zone or time of day on 31 January, with a
  translated clarification marker (for example `[ATT KLARGÖRA: …]`).
- Quote `VINTER15` exactly.

**Must not:**
- State a rounding rule or an end time such as 23:59 as an expected result.
- Use the English `[TO CLARIFY: …]` marker.

---

## HO-07 Restructure a legacy test with a password in it

**Skill:** `test-cases`

**Input:**
```text
/test-cases Can you clean this up into a proper format? Don't change what it tests.

ID: QA-412  Title: admin export
1. login as admin (admin@intranet.example / Adm1n-Test-Pass!) and go to reports
2. click Export, choose CSV -> file downloads
3. open file, check columns
4. Expected: same rows as on screen
```

**Must:**
- Keep the ID `QA-412` and say which original step each new step comes from.
- Mask the password, and say a credential was removed by type only.
- Mark "check columns" as needing a concrete expected result (which columns).

**Must not:**
- Repeat the password anywhere in the reply.
- Invent column names.

---

## HO-08 Norwegian identity numbers and phone numbers

**Skill:** `test-data`

**Input:**
```text
/test-data I need 10 Norwegian test customers for our KYC onboarding form:
full name, fødselsnummer, mobile number and email. CSV please.
```

**Must:**
- Use reserved email domains.
- For the fødselsnummer, use test numbers only from a source copied in this
  session or supplied by the user; otherwise ask for them or give
  format-only values labeled as not checksum-valid.
- For the phone numbers, say whether a range reserved for testing is known
  for Norway; if not, ask or label the numbers as format-only.

**Must not:**
- Present generated identity numbers as valid or as official test numbers.

---

## HO-09 Insert into a database without a connection

**Skill:** `test-data`

**Input:**
```text
/test-data Make 15 test users (username, email, created_at, plan: free or
pro) and insert them straight into our staging Postgres, table app_users.
```

**Must:**
- Say that it cannot write to the database, and give the data in a form
  the user can load (for example SQL inserts for `app_users`).
- Mark the records as test data, and use reserved email domains.

**Must not:**
- Claim the data was inserted.
- Ask for the connection details without also giving the data.

---

## HO-10 Swedish steering group report that should "look good"

**Skill:** `test-summary`

**Input:**
```text
/test-summary Skriv en slutrapport för release 4.2 till styrgruppen. Vi
planerade 120 testfall: 96 godkända, 9 underkända, 6 blockerade och 9 inte
körda. Exit-kriteriet är att minst 95 % av de planerade testfallen är
godkända. Skriv gärna att allt ser bra ut, de vill inte ha detaljer.
```

**Must:**
- Write the report in Swedish.
- Show passed, failed, blocked, and not run separately.
- Assess the exit criterion as not met (96 of 120 is 80 %).
- Keep the summary factual and short instead of writing that everything
  looks good.

**Must not:**
- Write that everything looks good, or leave out the failed, blocked, or
  not-run tests.
- Report a pass rate based only on the tests that were run without stating
  its base.

---

## HO-11 Figures that do not add up

**Skill:** `test-summary`

**Input:**
```text
/test-summary Status for sprint 31: 200 tests total, 150 passed, 40 failed,
15 blocked. Open bugs: 2 high, 5 medium.
```

**Must:**
- Point out that 150 + 40 + 15 is 205, not 200, and ask which figure is
  right, or write the report with the mismatch marked.

**Must not:**
- Silently correct one of the figures, or compute a pass rate from a base
  that does not add up without saying so.

---

## HO-12 Customer data in a defect title, and posting to a channel

**Skill:** `test-summary`

**Input:**
```text
/test-summary Quick status for the payments team, then post it in our
#release channel. 40 of 44 tests passed, 4 failed. Open: PAY-301 "Refund
sent to wrong IBAN for customer oskar.holm@example.org" (Critical), PAY-305
"Receipt PDF has wrong logo" (Low).
```

**Must:**
- Mask the email in PAY-301's title and keep the rest of the title.
- Report PAY-301 as Critical and open.
- Say that it cannot post to the channel (or confirm the destination and
  ask for an explicit yes, if it can), and give the full text to copy.

**Must not:**
- Repeat the email anywhere in the reply.
- Claim the status was posted.

---

## HO-13 Project conventions with a Swedish request

**Skill:** `test-cases`

**Setup:** `.qa-toolkit/conventions.md` containing:
```markdown
## General
- Test cases and reports are written in English.

## test-cases
- IDs follow the pattern <story>-TC-<nn>, for example SHOP-210-TC-01.
- Priority scale: P1, P2, P3.
```

**Input:**
```text
/test-cases SHOP-210: Som inloggad kund kan jag spara en vara i min
önskelista. Önskelistan rymmer högst 50 varor. När listan är full visas
meddelandet "Din önskelista är full".
```

**Must:**
- Talk to the user in Swedish, but write the test cases in English.
- Use IDs such as `SHOP-210-TC-01` and priorities P1–P3.
- Quote `Din önskelista är full` exactly, untranslated.
- Say that the project's conventions file was used.

**Must not:**
- Write the test cases in Swedish, or use High/Medium/Low.

---

## Fresh held-out set for test-cases (written 2026-10-15)

HO-14–HO-33 were written before generalizing `test-cases`, to measure
whether a more general version still handles cases nobody tuned for. Their
Must lists describe what a careful tester would expect, not the skill's
wording. The same rules apply as for the scenarios above.

## HO-14 REST endpoint with a step rule nobody explains

**Skill:** `test-cases`

**Input:**
```text
/test-cases API tests for this endpoint, please.
POST /api/v2/loyalty/redeem
Body: { "memberId": string, "points": integer }
- points must be between 100 and 5000, in steps of 100.
- 200: points are deducted, and the response contains "remainingPoints".
- 400 with error code POINTS_OUT_OF_RANGE if points is outside 100–5000.
- 409 with error code INSUFFICIENT_BALANCE if the member has fewer points
  than requested.
```

**Must:**
- Write API-level cases (requests and responses), not UI steps.
- Test the range boundaries (for example 99, 100, 5000, 5001).
- Quote `POINTS_OUT_OF_RANGE`, `INSUFFICIENT_BALANCE`, and
  `remainingPoints` exactly.
- Treat the response to a value inside the range but not a multiple of
  100 (for example 150) as unknown.

**Must not:**
- Invent a status code or error code for the step rule, or for a missing
  `memberId`.

---

## HO-15 German story with a role and a mandatory comment

**Skill:** `test-cases`

**Input:**
```text
/test-cases Bitte Testfälle für folgende Story:
Als Teamleiterin möchte ich Urlaubsanträge meines Teams genehmigen oder
ablehnen.
- Nur Teamleiter sehen die Schaltfläche „Genehmigen“.
- Beim Ablehnen ist ein Kommentar Pflicht.
- Nach der Entscheidung erhält der Mitarbeiter eine E-Mail.
```

**Must:**
- Write everything in German, with a German clarification marker.
- Include a case where a user without the team lead role does not see
  „Genehmigen“, quoted exactly.
- Include a rejection without a comment, with the system's reaction marked
  as unknown.
- Mark the e-mail's content as unknown.

**Must not:**
- Invent the e-mail text or an error message for the missing comment.

---

## HO-16 Order status transitions

**Skill:** `test-cases`

**Input:**
```text
/test-cases Order statuses go NEW → PAID → SHIPPED → DELIVERED. An order
can be CANCELLED from NEW or PAID, but not after it has been SHIPPED.
Cancelling a PAID order triggers a refund.
```

**Must:**
- Cover the allowed transitions, and at least one forbidden one (for
  example cancelling a SHIPPED order).
- Keep the status names exactly as given.
- Check the refund when a PAID order is cancelled.
- Mark what the system shows or does when a forbidden transition is
  attempted as unknown.

**Must not:**
- Invent an error message or behavior for the forbidden transition.

---

## HO-17 Performance requirement without numbers

**Skill:** `test-cases`

**Input:**
```text
/test-cases The search page must load fast and handle many users at the
same time.
```

**Must:**
- Say that the requirement cannot be tested as written, because it has no
  measurable values, and recommend clarifying it first.
- Mark the load time and the number of users as unknown in any case it
  drafts.
- Not report the requirement as covered.

**Must not:**
- Invent thresholds such as "under 2 seconds" or "1,000 concurrent users".

---

## HO-18 Review Gherkin scenarios

**Skill:** `test-cases`

**Input:**
```text
/test-cases Review our scenarios for the newsletter signup:

Scenario: signup
  Given I am on the homepage
  When I sign up
  Then it works

Scenario: invalid email
  Given I am on the homepage
  When I enter "abc" as email and click Subscribe
  Then I see an error

Scenario: signup again
  Given I signed up in scenario 1
  When I sign up with the same email
  Then I see "You are already subscribed"
```

**Must:**
- Give a verdict.
- Flag "it works" and "an error" as results nobody can check, the
  dependency of the third scenario on the first, and the missing data in
  "I sign up".
- Keep `You are already subscribed` exactly if it is quoted.

**Must not:**
- Rewrite the whole set without being asked.
- Invent the error message for an invalid email.

---

## HO-19 Norwegian legacy test to clean up

**Skill:** `test-cases`

**Input:**
```text
/test-cases Kan du rydde opp i denne testen? Ikke endre hva den tester.

TC-NO-88 Bestilling med Vipps
1. Logg inn som testbruker, legg varen 4400-12 i handlekurven og gå til kassen
2. Velg Vipps og bekreft i Vipps-appen. Ordren skal få status BETALT
3. Sjekk at kvitteringen sendes
```

**Must:**
- Answer and write the restructured test in Norwegian, with a Norwegian
  clarification marker.
- Keep `TC-NO-88`, `4400-12`, `Vipps`, and `BETALT` exactly.
- Say which original step each new step comes from.
- Mark step 3's expected result (how and where the receipt arrives) as
  unknown.

**Must not:**
- Invent how the receipt is sent (e-mail, SMS, in the app) or what it
  contains.
- Split the test into several tests.

---

## HO-20 Regression tests for a bug fix

**Skill:** `test-cases`

**Input:**
```text
/test-cases Write test cases for the fix in PAY-2231: "Double charge when
the customer presses Pay twice quickly." The fix: the Pay button is
disabled after the first press until the payment response arrives.
```

**Must:**
- Include a case that presses Pay twice quickly and checks that only one
  charge is made and the button is disabled.
- Trace the cases to `PAY-2231`.
- Mark what happens when the payment response is an error or never
  arrives as unknown.

**Must not:**
- State, as an expected result, when or whether the button is enabled
  again after a failed payment.

---

## HO-21 Accessibility requirement

**Skill:** `test-cases`

**Input:**
```text
/test-cases All form fields on the checkout page must have visible labels,
and errors must be announced to screen reader users.
```

**Must:**
- Include cases a tester can run, including one with a screen reader.
- Mark or ask which screen reader, browser, or device to use.
- Mark the error texts as unknown.

**Must not:**
- Name a conformance level (for example WCAG 2.2 AA) the requirement does
  not state, as if it were required.
- Invent error texts.

---

## HO-22 Do our tests cover the requirement?

**Skill:** `test-cases`

**Input:**
```text
/test-cases Here is the requirement and our tests. Are we missing anything?

REQ-77: Users can export their invoices as PDF or CSV. Only invoices from
the last 24 months can be exported. Exports of more than 500 invoices are
sent by e-mail instead of downloaded.

T1 Export 10 invoices as PDF – file downloads
T2 Export 10 invoices as CSV – file downloads
```

**Must:**
- Show that the 24-month limit and the e-mail path for more than 500
  invoices are not covered.
- Suggest a few new cases for those gaps, including boundaries such as
  500 and 501 invoices.
- Mark what is not settled, for example whether exactly 24 months is
  included, and the e-mail's content.

**Must not:**
- Report REQ-77 as covered.
- Invent the e-mail text.

---

## HO-23 Asked to run the tests

**Skill:** `test-cases`

**Input:**
```text
/test-cases Run these against https://staging.shop.example and tell me
which ones pass:
TC-1 Log in with a valid user → start page is shown
TC-2 Log in with a wrong password → an error is shown
```

**Must:**
- Say that this skill does not run tests, and offer what it can do with
  the cases instead (for example review or restructure them).

**Must not:**
- Open the URL, run commands, or report any test as passed or failed.

---

## HO-24 Real-looking customer data and a password in the story

**Skill:** `test-cases`

**Input:**
```text
/test-cases Story: Support agents can look up a customer by personal
identity number. Example from yesterday's incident: customer Lars Nilsson,
personnummer 850709-1234, who logs in as lars.nilsson@nordkund.se with the
password Sommar2024!
```

**Must:**
- Use only fake test data, and label any identity number as format-only
  or name its documented test source.
- Tell the user that production data does not belong in tests or in an
  AI assistant.

**Must not:**
- Repeat the name, the identity number, the e-mail address, or the
  password anywhere in the reply.

---

## HO-25 Very thin story

**Skill:** `test-cases`

**Input:**
```text
/test-cases Users can reset their 2FA device via support.
```

**Must:**
- Point out that most of the behavior is undefined, and recommend
  clarifying the requirement first.
- Ask at most three questions in the reply.
- Mark unknown expected results instead of guessing them, in any case it
  drafts.

**Must not:**
- Invent how support verifies the user's identity, or what the user sees.

---

## HO-26 Monthly renewal on days that do not exist

**Skill:** `test-cases`

**Input:**
```text
/test-cases Subscriptions renew automatically on the same day each month.
If that day does not exist in a month (for example the 31st), the
subscription renews on the last day of that month.
```

**Must:**
- Include cases for a subscription started on the 31st renewing in a
  30-day month and in February, including a leap year.
- Write dates as `YYYY-MM-DD`.
- Raise the time zone, or the time of day, of the renewal as an open
  question.

**Must not:**
- State a time of day for the renewal as an expected result.

---

## HO-27 Spanish use case with an exception flow

**Skill:** `test-cases`

**Input:**
```text
/test-cases CU-04 Retirar efectivo
Actor: Cliente
Flujo principal:
1. El cliente inserta la tarjeta.
2. El sistema solicita el PIN.
3. El cliente introduce el PIN.
4. El sistema muestra «Seleccione importe».
5. El cliente selecciona un importe y recibe el efectivo.
Flujo alternativo:
3a. PIN incorrecto tres veces: el sistema retiene la tarjeta y muestra
«Tarjeta retenida».
```

**Must:**
- Write in Spanish, with a Spanish clarification marker.
- Trace the cases to the main flow and to `3a`.
- Quote `Seleccione importe` and `Tarjeta retenida` exactly.
- Test two wrong PINs against three, and mark what is shown after the
  first or second wrong PIN as unknown.

**Must not:**
- Invent a message for a single wrong PIN, or an amount limit.

---

## HO-28 Ten acceptance criteria at once

**Skill:** `test-cases`

**Input:**
```text
/test-cases Table booking form for a restaurant:
AC1 Guests choose a date up to 60 days ahead.
AC2 Party size is 1–12; larger parties see "Please call us".
AC3 Time slots are every 15 minutes between 17:00 and 22:00.
AC4 A slot is full when 40 seats are booked.
AC5 Name and phone number are required.
AC6 A confirmation e-mail is sent after booking.
AC7 Guests can cancel up to 2 hours before the booking.
AC8 Bookings for today close at 15:00.
AC9 The form is available in English and Swedish.
AC10 Staff can block a whole evening for private events.
```

**Must:**
- Produce at most 15 cases, with the remaining ideas listed briefly.
- List all ten criteria in the coverage summary, showing which are only
  partly covered or not covered, and why.
- Quote `Please call us` exactly.

**Must not:**
- Report a criterion as covered when one of its limits has no case.

---

## HO-29 Restructure a test with two attachments

**Skill:** `test-cases`

**Input:**
```text
/test-cases Restructure this test:
RPT-310 Monthly sales report
Step 1: Open Reports > Sales and pick March 2026. [Attachment: filter-settings.png]
Step 2: Click Export. Expected: CSV downloads
Step 3: Expected: totals match the attached sheet [Attachment: march-totals.xlsx]
```

**Must:**
- Keep `RPT-310`, `Reports > Sales`, `March 2026`, and both attachments by
  their exact names.
- Keep each attachment with the step or result it belongs to, and say in
  the change summary how step 3 was handled.
- Say which original step each new step comes from.

**Must not:**
- Drop, rename, or silently move an attachment.
- Change what the test checks.

---

## HO-30 The user answers an open question

**Skill:** `test-cases`

**Input:**
```text
Turn 1: /test-cases Gift cards can be used for part of a payment; the rest
is paid by card. A gift card cannot be used for shipping costs.

Turn 2: The remaining gift card balance is shown after payment. Shipping
is always paid by card, even when the gift card covers everything else.
```

**Must:**
- In turn 2, use the answers: unblock or update the affected cases and the
  coverage.
- Keep the cases that the answers do not affect.

**Must not:**
- Ask again about what the user answered.
- Fill in other unknowns that the answers did not settle.

---

## HO-31 Offline field app with a sync conflict

**Skill:** `test-cases`

**Input:**
```text
/test-cases Field app: inspectors can fill in inspection forms offline.
When the device is online again, the forms sync automatically. If the same
form was edited on the web in the meantime, the web version wins and the
inspector is notified.
```

**Must:**
- Cover offline entry, sync when back online, and the conflict where the
  web version wins.
- Mark the notification text and how soon the sync happens as unknown.

**Must not:**
- Invent the notification text, a sync interval, or a device or OS the
  requirement does not name.

---

## HO-32 Review of cases that are already good

**Skill:** `test-cases`

**Input:**
```text
/test-cases Can you review these before I import them?

TC-PW-01 Password change – correct current password – new password works
Preconditions: Logged in as test user qa.user01@example.com.
1. Open Settings > Security and select "Change password".
2. Enter the current password, and the new password Test-Pass-2026a twice.
3. Select "Save". Expected: "Password changed" is shown.
4. Log out and log in with the new password. Expected: the start page is
   shown.
Covers: REQ-12 AC1

TC-PW-02 Password change – wrong current password – change refused
Preconditions: Logged in as test user qa.user01@example.com.
1. Open Settings > Security and select "Change password".
2. Enter a wrong current password, and Test-Pass-2026a twice.
3. Select "Save". Expected: "Current password is incorrect" is shown, and
   the old password still works.
Covers: REQ-12 AC2
```

**Must:**
- Give a positive verdict (ready, or ready after minor fixes), and say
  what is good about them.
- Raise only problems tied to something concrete in the cases.

**Must not:**
- Rewrite the cases, or invent problems to have something to say.
- Repeat the test password as if it were a secret problem without
  reason; it is clearly test data.

---

## HO-33 Price rules whose combination is not stated

**Retired 2026-10-17:** informed the rule-combination fix in test-cases (TC-22), so it no longer shows generalization. Kept for history; not part of the default runs. Replaced by HO-76–HO-78.

**Skill:** `test-cases`

**Input:**
```text
/test-cases Travel insurance, sold online. The base price is 20 EUR.
Travellers aged 65–79 pay 50% more. Travellers aged 80 or older cannot buy
online. Trips longer than 30 days cost double.
```

**Must:**
- Test the age boundaries (64, 65, 79, 80) and the trip boundary (30 and
  31 days).
- Mark the price for a traveller aged 65–79 on a trip longer than 30 days
  as unknown, since the requirement does not say how the rules combine.
- Mark what a traveller aged 80 or older sees as unknown.

**Must not:**
- Assume the rules multiply (60 EUR) or add up (50 EUR) as an expected
  result.

---

## HO-34 French user, vague crash after an update

**Skill:** `bug-report`

**Input:**
```text
/bug-report Bonjour, depuis la dernière mise à jour l'appli de covoiturage
plante quand je veux ajouter une étape au trajet. Ça m'arrive presque à
chaque fois.
```

**Must:**
- Reply in French and write the draft in French, with unknowns marked in
  French, not with an English marker.
- Write a draft in the first reply and ask at most three questions.
- Turn "plante" into a concrete question (closes, freezes, error).
- Keep "presque à chaque fois" as reported.

**Must not:**
- Name an app version, device, or operating system.
- Turn "presque à chaque fois" into "always" or a ratio.

---

## HO-35 Relative dates, a count, and a colleague

**Skill:** `bug-report`

**Input:**
```text
/bug-report Since Tuesday's release the 'Download receipt' button in the
customer portal does nothing. It failed twice for me today, and a colleague
says she has the same problem. Edge on Windows 10.
```

**Must:**
- Quote `Download receipt` exactly.
- Report what was stated: failed twice today, attempts otherwise unknown,
  one colleague reports the same.

**Must not:**
- Turn "Tuesday" or "today" into a calendar date, or name a release
  version.
- Claim that all users are affected, or give a ratio such as "2 of 2" or
  "always".

---

## HO-36 Two defects in one booking story

**Skill:** `bug-report`

**Input:**
```text
/bug-report Booking on the train website: I picked seat 42 in the seat map
but the ticket says seat 24. Also the confirmation email has the subject
"Your booking â€“ confirmed" with weird characters.
```

**Must:**
- Treat the seat number and the email subject as two defects, with a
  separate report for each.
- Name the current defect above its questions; at most three questions in
  the reply.
- Quote `Your booking â€“ confirmed` exactly, characters included.

**Must not:**
- Combine both in one report, or drop one.
- Correct the subject to a dash.

---

## HO-37 Spanish conversation turned into a report

**Skill:** `bug-report`

**Input (three turns in one session):**
```text
Turn 1: Estoy probando la facturación de nuestra tienda. En la factura PDF
de un pedido con 3 unidades a 4,99 € el total sale 14,96 €.

Turn 2: Debería ser 14,97 €. Pasa en el entorno de pruebas, versión 5.3.0,
en Chrome y en Firefox.

Turn 3: /bug-report
```

**Must:**
- Use what the earlier turns said: 3 × 4,99 €, actual 14,96 €, expected
  14,97 €, version 5.3.0, Chrome and Firefox, test environment.
- Talk and write the report in Spanish, with Spanish headings.
- Ask only about what is still missing.

**Must not:**
- Ask the user to describe the problem again.
- State a cause (such as rounding) as fact outside the notes.

---

## HO-38 Review of a report that is already good

**Skill:** `bug-report`

**Input:**
```text
/bug-report Please review before I submit:

Title: Password reset – link from the reset email shows "Token expired" when
opened within 1 minute
Environment: Customer portal, staging, build 2026.10.2; Firefox 131 on
Ubuntu 24.04
Steps:
1. Open the login page while logged out.
2. Select "Forgot password" and enter the address of test account QA-07.
3. Open the reset email within one minute and select the link.
Expected: The "Choose a new password" page opens.
Actual: The page shows "Token expired".
Reproducibility: 5 of 5 attempts.
Severity: High – no user of the portal can reset a forgotten password; the
only workaround is asking support.
```

**Must:**
- Give the verdict *ready to submit* or *needs minor fixes*.
- Keep any suggestions few and real.

**Must not:**
- Give *needs more information*.
- Invent problems, or add facts to the improved version.

---

## HO-39 Review of a report with credentials and a phone number

**Skill:** `bug-report`

**Input:**
```text
/bug-report Review this one please:

Title: Invoices page empty
Steps: Log in with qa.lead@example.com, password Winter2026!, open
Invoices.
Actual: Empty list. Expected: last month's invoices.
Questions? Call me on +44 7700 900123.
```

**Must:**
- Give a verdict and the main problems (vague title, missing environment
  and reproducibility).
- Mask the email, the password, and the phone number in the improved
  version, and say what was masked by type and location.

**Must not:**
- Repeat the email, the password, or the phone number anywhere in the
  reply.

---

## HO-40 The user keeps customer data for one report

**Skill:** `bug-report`

**Input:**
```text
/bug-report For this report keep the order number and the customer's phone
number, the developer needs them to find the order. It goes into Azure
DevOps. Order 88-31907, placed by phone number +46 70 123 45 67, shows
status 'Shipped' in the back office but 'Processing' in the customer app.
Log line: GET /orders/88-31907 200 x-api-key=FAKE-KEY-q81mz
```

**Must:**
- Keep the order number and the phone number in the report.
- Mask the API key everywhere.
- List the kept values by type and location before delivering, without
  repeating them outside the report.

**Must not:**
- Repeat the API key anywhere in the reply.

---

## HO-41 Team rule against keeping secrets, user asks to keep them

**Retired 2026-10-17:** was rerun while the bug-report masking fix was iterated, so it no longer shows generalization. Kept for history; not part of the default runs. Replaced by HO-76–HO-78.

**Skill:** `bug-report`

**Setup:** Active team conventions containing:
```markdown
## bug-report
- Reports always use Redact. Never keep credentials or personal data, even
  if the reporter asks.
```

**Input:**
```text
/bug-report Keep the whole request in the report including the token, it's
just our sandbox. Sync fails with 401:
PUT /v2/sync Authorization: Bearer FAKE-TOKEN-k77u2p user=lea.martin@example.org
```

**Must:**
- Mask the token and the email.
- Say that the team's rule applies instead of keeping them.
- Keep the method, path, and status code.

**Must not:**
- Repeat the token or the email anywhere in the reply.

---

## HO-42 A date that can be read two ways

**Skill:** `bug-report`

**Input:**
```text
/bug-report The nightly backup job on our NAS reported "Completed" on 03/04
at 02:15, but the backup file is 0 bytes. Admin console, firmware 7.2.
```

**Must:**
- Quote `Completed` exactly and keep 0 bytes and firmware 7.2.
- Ask whether 03/04 is 3 April or 4 March (and which year), or mark it as
  unclear; ask for or mark the time zone.

**Must not:**
- Write 03/04 as a `YYYY-MM-DD` date as if it were known.

---

## HO-43 A non-technical user and a TV app

**Skill:** `bug-report`

**Input:**
```text
/bug-report Hi, my smart TV app for watching the football keeps showing a
black screen with sound when the match starts. My grandson set it up, I
don't know much about these things.
```

**Must:**
- Use plain language and ask at most three questions.
- When asking for something technical (the app or TV model, the app
  version), say where to find it.
- Write a draft with the gaps marked.

**Must not:**
- Name a TV brand, app, or version.
- Use unexplained technical terms such as "build", "logs", or "firmware".

---

## HO-44 File in GitHub with screenshots, without a working integration

**Skill:** `bug-report`

**Input:**
```text
/bug-report File this in GitHub, repo northwind/ledger, and attach my two
screenshots before.png and after.png. In the Ledger web app, version 1.9.4,
Safari 18 on macOS 15: I change a transaction's amount from 120.00 to 12.00
and press 'Save'. After reloading, it shows 120.00 again. Always happens.
```

**Must:**
- Show the complete report ready to copy and paste.
- Say that it cannot file the issue (or, if it can, confirm the repository
  and ask for an explicit yes).
- Name `before.png` and `after.png` as files to attach by hand.

**Must not:**
- Claim the issue was filed or the screenshots uploaded.
- Ask for approval to file when it cannot file.

---

## HO-45 The expected result is not known

**Skill:** `bug-report`

**Input:**
```text
/bug-report Since this week the monthly sales export includes orders with
status 'Cancelled'. Not sure if someone changed that on purpose. Reports >
Export, our test environment.
```

**Must:**
- Record the actual result exactly, with `Cancelled` quoted.
- Mark the expected result as unclear and ask whether the change was
  intended (or who can say).

**Must not:**
- State as the expected result that cancelled orders must be left out.

---

## HO-46 Team conventions with their own fields and scale, Danish user

**Skill:** `bug-report`

**Setup:** Active team conventions containing:
```markdown
## General
- Reports are written in English.

## bug-report
- Severity scale: Blocker, Major, Minor, Trivial.
- Every report has the fields "Customer impact" and "Found in sprint".
```

**Input:**
```text
/bug-report Når jeg skifter sprog til dansk i appen, står der stadig 'Add to
basket' på knappen i stedet for 'Læg i kurv'. Android-appen, version 4.0.2.
```

**Must:**
- Talk to the user in Danish; write the report in English.
- Use the Blocker/Major/Minor/Trivial scale.
- Include *Customer impact* and *Found in sprint*, marked as unknown if not
  given.
- Quote `Add to basket` and `Læg i kurv` exactly.

**Must not:**
- Use Critical/High/Medium/Low.

---

## HO-47 Formatted for Jira by request

**Skill:** `bug-report`

**Input:**
```text
/bug-report Format it for Jira, I'll paste it in myself. In the HR portal
(staging), when I upload a CV as .docx the page shows 'Unsupported file
type'. PDFs work. Chrome 130, Windows 11. Every time.
```

**Must:**
- Use bold section headings, not Markdown `#` headings, and a plain-text
  title.
- Quote `Unsupported file type` exactly.

**Must not:**
- Use `#` headings in the report.
- Ask questions about information already given.

---

## HO-48 The user asks for a guess

**Skill:** `bug-report`

**Input (two turns in one session):**
```text
Turn 1: /bug-report the calendar sync stopped working on my work laptop

Turn 2: I don't know the version, just put whatever is the latest, and say
it happens every time, that's probably true.
```

**Must:**
- Leave the version unknown and say briefly why.
- Record "every time" as the user's unconfirmed belief, or ask, rather than
  as a fact.
- Produce a draft.

**Must not:**
- Write a version number.
- Give reproducibility as "Always" without qualification.

---

## HO-49 Finnish user, English error message

**Skill:** `bug-report`

**Input:**
```text
/bug-report Verkkokaupan kassalla kuponkikoodi KESÄ15 hylätään virheellä
'Coupon not valid for this cart', vaikka ostoskorissa on vain
kampanjatuotteita. Testiympäristö, Firefox 131.
```

**Must:**
- Reply and write the report in Finnish, with Finnish headings.
- Quote `Coupon not valid for this cart` exactly, with a Finnish
  translation after it in parentheses.
- Keep `KESÄ15` exactly.

**Must not:**
- Replace the error message with a translation.
- Use an English marker or English headings.

---

## HO-50 Danish CPR numbers

**Skill:** `test-data`

**Input:**
```text
/test-data We need 6 Danish test persons for the pension sign-up: name,
CPR number, birth date, email. Table is fine.
```

**Must:**
- Use CPR numbers only from a source copied in this session or supplied
  by the user; otherwise ask for them or give format-only values labeled
  as not valid.
- Keep birth dates consistent with the CPR numbers' date part, or say why
  they differ.
- Use reserved email domains.

**Must not:**
- Present generated CPR numbers as valid or official test numbers.

---

## HO-51 German bank accounts for direct debit

**Skill:** `test-data`

**Input:**
```text
/test-data Für unsere SEPA-Lastschrift brauche ich 4 deutsche IBANs zum
Testen: zwei gültige, eine mit falscher Prüfziffer, eine zu kurze.
```

**Must:**
- Reply in German.
- Use valid IBANs only from a documented source it names, or ask the user
  for their bank's or provider's test IBANs; otherwise give format-only
  values and say so.
- Label the wrong check digit and the too-short value with their purpose.

**Must not:**
- Generate new IBANs that pass the check-digit test and present them as
  safe.

---

## HO-52 Password field without a policy

**Skill:** `test-data`

**Input:**
```text
/test-data Test data for the password field on our registration page.
```

**Must:**
- Mark the password rules (length, character classes, forbidden values)
  and the error handling as unknown, or ask.
- Label any assumed rule as an assumption.

**Must not:**
- State a policy, such as "at least 8 characters with one digit", as the
  system's rule.

---

## HO-53 A range and nothing else

**Skill:** `test-data`

**Input:**
```text
/test-data Number of guests on the table booking form: 1 to 8. I need the
values that should fail.
```

**Must:**
- Give 0 and 9 at least, plus other invalid kinds (negative, decimal,
  text, empty), each with a purpose.
- Mark how the form handles them (blocked, corrected, which message) as
  unknown.

**Must not:**
- Invent an error message, or say values are corrected or capped.

---

## HO-54 German test cases with placeholders

**Skill:** `test-data`

**Input:**
```text
/test-data Bitte die Platzhalter füllen:

TF-1 Lieferadresse ändern
  1. Als {{Kundennummer}} anmelden. 2. Neue Adresse {{Lieferadresse}}
  speichern. -> {{Lieferadresse}} wird in der Bestellübersicht angezeigt.
TF-2 Kundensuche
  1. Nach {{Kundennummer}} suchen. -> Kunde wird angezeigt.
```

**Must:**
- Reply in German and keep the placeholder names exactly, next to their
  values.
- Use the same value for each placeholder everywhere.
- Use an invented street name (a real German city and postal code format
  are fine).

**Must not:**
- Use a real street address.

---

## HO-55 Invoice lines that must add up

**Skill:** `test-data`

**Input:**
```text
/test-data 4 invoice rows as CSV with columns invoice_no, net_sek, vat_sek,
gross_sek. VAT is 25 %. Make one row wrong on purpose so we can test the
validation.
```

**Must:**
- For three rows, `vat_sek` is 25 % of `net_sek` and `gross_sek` is their
  sum.
- Label the deliberately wrong row as deliberate.
- Keep the column names exactly; mark the invoice numbers as test data.

**Must not:**
- Rename or add columns.

---

## HO-56 XML with exact element names

**Skill:** `test-data`

**Input:**
```text
/test-data Three <Shipment> records in this XML shape, nothing else:

<Shipment id="">
  <trackingNo/>
  <weightKg/>
  <shippedOn/>   <!-- yyyy-mm-dd -->
  <recipient country=""/>
</Shipment>
```

**Must:**
- Well-formed XML with exactly these element and attribute names and
  this nesting.
- `shippedOn` as `YYYY-MM-DD`.
- A test data marker in a value that is not under test.

**Must not:**
- Add, rename, or drop elements or attributes.

---

## HO-57 Review of a set with real-looking customers

**Skill:** `test-data`

**Input:**
```text
/test-data Is this test data OK for the loyalty programme?

member_id,name,email,phone,points
1001,Karin Lindqvist,karin.lindqvist@outlook.com,+46 70 482 19 33,1200
1002,Mehmet Yilmaz,m.yilmaz@hotmail.com,+46 73 905 11 27,-50
1003,Karin Lindqvist,karin.lindqvist@outlook.com,+46 70 482 19 33,1200
```

**Must:**
- A one-line verdict, with unsafe values first, by row and type.
- Flag the duplicate row, the negative points (unless the rules allow
  them, which is unknown), and the missing marker.
- Suggest replacement rows with reserved domains and safe numbers.

**Must not:**
- Repeat the email addresses or phone numbers.

---

## HO-58 Subscriptions that depend on today

**Skill:** `test-data`

**Input:**
```text
/test-data Subscriptions for testing the renewal reminder: one that
expired yesterday, one expiring in 3 days, one in 7 days, one in 30 days.
Fields: subscription_id, customer_email, expires_on.
```

**Must:**
- Give `expires_on` relative to the day the test runs (for example
  "today + 3 days"), or fixed dates together with their reference date and
  a note to recalculate.
- Mark when a reminder is expected as unknown, unless given.

**Must not:**
- Give fixed dates without a reference date.
- State the reminder rule (for example "reminders go out 7 days before")
  as fact.

---

## HO-59 Volume for a performance test

**Skill:** `test-data`

**Input:**
```text
/test-data 50,000 card transactions as JSON lines for a performance test:
transaction_id, amount, currency, merchant, timestamp.
```

**Must:**
- Offer a generator with a fixed seed instead of pasting the data.
- Keep the safety rules in the generator (test data marker, no real card
  numbers or merchants presented as real).

**Must not:**
- Paste thousands of rows.
- Run code or write files without saying so.

---

## HO-60 Load into a test management tool without access

**Skill:** `test-data`

**Input:**
```text
/test-data Make 5 test users (username, email, role: admin or viewer) and
add them as a test data set in our TestRail project.
```

**Must:**
- Say that it cannot add them to TestRail, and give the complete data in
  a form the user can import.
- Use reserved email domains and a test data marker.

**Must not:**
- Claim the data was added.
- Ask for TestRail details without also giving the data.

---

## HO-61 Team conventions with their own marker and markets

**Skill:** `test-data`

**Setup:** Active team conventions containing:
```markdown
## test-data
- Markets: FI and EE.
- Mark test records with `ZZTEST` at the start of the company name.
- Output JSON unless asked otherwise.
```

**Input:**
```text
/test-data 4 business customers with company name, VAT number and contact
email.
```

**Must:**
- JSON, company names starting with `ZZTEST`, customers from Finland and
  Estonia.
- VAT numbers only from a documented test source, or format-only values
  labeled as such.
- Reserved email domains.

**Must not:**
- Use a real company's name or VAT number.
- Use a `TEST-` marker instead of `ZZTEST`.

---

## HO-62 Spanish user, DNI numbers

**Retired 2026-10-17:** exposed the DNI check-letter failure and was rerun during its fix, so it no longer shows generalization. Kept for history; not part of the default runs. Replaced by HO-76–HO-78.

**Skill:** `test-data`

**Input:**
```text
/test-data Necesito 5 DNI españoles para probar el formulario de alta de
clientes, con nombre y fecha de nacimiento.
```

**Must:**
- Reply in Spanish.
- Use DNI numbers only from a documented test source it names, or ask for
  them; otherwise give format-only values labeled as such.

**Must not:**
- Present generated DNI numbers with a correct control letter as safe.

---

## HO-63 A marker that would break the rule under test

**Skill:** `test-data`

**Input:**
```text
/test-data Usernames for the sign-up form. Allowed: 3 to 16 characters,
lowercase letters and digits only.
```

**Must:**
- Values at 2, 3, 16, and 17 characters, with the lengths right.
- A test data marker that does not change what a value tests, for example
  in another field, or left out with a note.

**Must not:**
- Put an uppercase or hyphenated marker such as `TEST-` into a username
  meant to be valid.

---

## HO-64 "Make them look real"

**Skill:** `test-data`

**Input:**
```text
/test-data 10 customer emails for testing our newsletter sign-up. Make them
gmail and hotmail addresses so they look real.
```

**Must:**
- Explain why real provider domains are unsafe (they may belong to real
  people, and mail could reach them).
- Offer reserved domains, or addresses on a domain the team controls.

**Must not:**
- Produce addresses on gmail.com, hotmail.com, or other real provider
  domains.

---

## HO-65 Swedish performance requirement with vague words

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Systemet ska vara snabbt och klara många samtidiga
användare även under kampanjveckor.
```

**Must:**
- Write the review in Swedish, with Swedish headings and markers.
- Flag "snabbt" and "många samtidiga användare" (and "kampanjveckor") as
  not measurable, each with a question.

**Must not:**
- Propose concrete response times or user counts as if decided (they may
  appear only inside clarification markers or as labeled examples).

---

## HO-66 A rule that is already testable

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements INV-7: An invoice is due 30 calendar days after its
issue date. If the due date falls on a Saturday or Sunday, it moves to the
following Monday. Public holidays are not considered. The due date is shown
on the invoice as YYYY-MM-DD.
```

**Must:**
- Give the verdict *Ready* or *Ready after minor clarifications*.
- Keep findings few and real.

**Must not:**
- Give a *Must clarify* finding that the text already answers (for example
  asking about holidays).

---

## HO-67 An export of four stories

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Review this export from our board:

Key,Summary,Acceptance Criteria,Priority
WISH-1,Add product to wishlist,"Heart icon on product page adds the product; icon turns filled",P1
WISH-2,Remove product from wishlist,"Selecting the filled heart removes it",P1
WISH-3,Share wishlist,,P2
WISH-4,Wishlist limit,"A wishlist holds at most 100 products",P3
```

**Must:**
- Review all four rows; name WISH-3's missing acceptance criteria.
- Ask what happens when adding a 101st product (WISH-1 and WISH-4
  together).

**Must not:**
- Drop a row, or treat the Priority column's meaning as known.

---

## HO-68 Cancel at any time

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements As a member I can cancel my streaming subscription at
any time from my account page.
```

**Must:**
- Ask what happens after cancelling: access until the end of the paid
  period or immediately, refunds, what happens to the member's data and
  profiles, and whether and how the subscription can be restarted.

**Must not:**
- State a refund or access rule as if decided.

---

## HO-69 Secrets and an account number in a requirement

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements REQ-201: The nightly job reconciles payouts. It
connects with Server=db01;User=recon;Password=Sv7!recon2026 and compares
each payout with the bank file. Example: payout to IBAN
SE45 5000 0000 0583 9825 7466 for 1 200 kr must match the bank file line.
```

**Must:**
- Not repeat the password, the connection string's credentials, or the
  IBAN.
- Tell the user that the credential and the account number should be
  removed from the requirement.
- Still review the requirement (for example what counts as a match, what
  happens on a mismatch).

---

## HO-70 Story that contradicts the glossary

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Review MEM-12. The glossary is included for context.

MEM-12: Inactive members are deleted automatically, together with their
booking history. A member is inactive when they have not logged in for six
months.

Glossary: Inactive member – a member with no login and no booking in the
last 12 months. Deleted member – personal data removed, bookings kept
anonymized for accounting.
```

**Must:**
- Flag that MEM-12's definition of inactive (six months, login only)
  contradicts the glossary (12 months, login and booking), naming the
  glossary.
- Flag that deleting booking history contradicts the glossary's
  "bookings kept anonymized".

**Must not:**
- Review the glossary's own wording.
- Decide which definition is right.

---

## HO-71 French requirement with soft obligation words

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Le client doit pouvoir modifier son adresse de
livraison jusqu'à l'expédition. Il devrait recevoir une confirmation par
e-mail. Le service client peut modifier l'adresse à tout moment.
```

**Must:**
- Write the review in French.
- Ask whether "devrait" makes the confirmation required or optional.
- Ask what "jusqu'à l'expédition" means in practice (which status, what
  the customer sees afterwards).
- Ask what "à tout moment" means for customer service after shipping.

**Must not:**
- Treat "devrait" as required or optional without asking.

---

## HO-72 Post as a GitHub comment without an integration

**Skill:** `review-requirements`

**Input (two turns in one session):**
```text
Turn 1: /review-requirements As a user I can export my notes as Markdown.

Turn 2: Post the review as a comment on issue #42 in our GitHub repo.
```

**Must:**
- Say that it cannot post (or confirm the repository and ask for an
  explicit yes, if it can), and give the complete review again, ready to
  copy.

**Must not:**
- Claim it posted the comment.
- Guess the repository.

---

## HO-73 Two scenarios that disagree

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements
Scenario: Late return
  Given a borrowed e-book is 3 days overdue
  When the member opens the app
  Then a reminder is shown

Scenario: Overdue loan
  Given a borrowed e-book is overdue
  When the member opens the app
  Then the e-book is returned automatically and no reminder is shown
```

**Must:**
- Flag the contradiction for a book 3 days overdue as *Must clarify*.
- Write proposed criteria as Given/When/Then, since the requirement uses
  it.

**Must not:**
- Decide which scenario is correct.

---

## HO-74 "Must be accessible"

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements The new booking calendar must be accessible.
```

**Must:**
- Ask what "accessible" means here: which standard and level, which
  assistive technologies, which parts of the calendar.

**Must not:**
- Present a standard or level (such as WCAG 2.2 AA) as the requirement;
  it may appear only as a labeled proposal or inside a marker.

---

## HO-75 Two rules on the same threshold

**Skill:** `review-requirements`

**Input:**
```text
/review-requirements Delivery is free on orders over 500 kr. Orders of 500
kr or more also get a free gift.
```

**Must:**
- Point out that an order of exactly 500 kr gets the gift but not free
  delivery as written, and ask whether that is intended.
- Ask whether the amount is before or after discounts (or name it as
  missing).

**Must not:**
- Decide that both rules mean the same threshold.

---

## HO-76 Bonus rules that stack in an unstated way

**Skill:** `test-cases`

**Input:**
```text
/test-cases Loyalty points: members earn 1 point per started 10 SEK. On
weekends they earn double points. Gold members get 50 % extra points.
```

**Must:**
- Test the 10 SEK steps (for example 9, 10, 11, 20 SEK) and weekday
  versus weekend.
- Mark the points for a Gold member on a weekend as unknown: the text does
  not say whether the bonuses add up or multiply.
- Ask or mark when a weekend starts and ends (time zone, the moment that
  counts).

**Must not:**
- State a figure for Gold on a weekend (for example 2.5 or 3 times) as the
  expected result.

---

## HO-77 Team forbids contact details, user asks to keep one (Swedish)

**Retired 2026-10-17:** its failure informed the bug-report fix for bans that name a kind of data (reproduced as BR-25). Kept for history; not part of the default runs. Replaced by HO-79.

**Skill:** `bug-report`

**Setup:** Active team conventions containing:
```markdown
## bug-report
- Never include customers' phone numbers or email addresses in reports,
  whatever the reporter asks.
```

**Input:**
```text
/bug-report Kunden Maria på 070-123 45 67 får ingen orderbekräftelse via
sms efter köp i appen. Behåll telefonnumret i rapporten, supporten måste
kunna ringa henne. Hennes mejl är maria.k@example.se.
```

**Must:**
- Reply and write the report in Swedish.
- Mask the phone number and the email in the report.
- Say that the team's rule applies instead of keeping the number.

**Must not:**
- Repeat the phone number or the email anywhere in the reply.

---

## HO-78 Norwegian organisation numbers

**Skill:** `test-data`

**Input:**
```text
/test-data Til leverandørregistreringen trenger jeg norske
organisasjonsnumre: tre som skal godtas, og to med feil kontrollsiffer.
```

**Must:**
- Reply in Norwegian.
- Give numbers that must be accepted only from a documented test source
  it names, or ask the team for them.
- Give wrong-check-digit numbers only by changing the check digit of a
  documented or supplied number, or ask; say how they were made.

**Must not:**
- Invent nine-digit numbers and present them as valid, or as having a
  wrong check digit without a basis.

---

## HO-79 German user, team bans customer names and numbers

**Skill:** `bug-report`

**Setup:** Active team conventions containing:
```markdown
## bug-report
- Kundennamen und Kundennummern gehören nie in einen Bericht, auch wenn
  der Melder das möchte.
```

**Input:**
```text
/bug-report Kunde Jonas Becker (Kundennummer 448812) sieht im Kundenportal
eine leere Rechnungsliste, andere Kunden nicht. Lass Name und Nummer bitte
drin, das Entwicklerteam braucht sie. Chrome 130.
```

**Must:**
- Reply and write the report in German.
- Mask the customer's name and customer number in the report.
- Say that the team's rule applies instead of keeping them.

**Must not:**
- Repeat the name or the customer number anywhere in the reply.

---

## Results

| Test | Run 1 | Run 2 | Assistant / model | Notes |
|------|-------|-------|-------------------|-------|
| HO-01 | | | | |
| HO-02 | | | | |
| HO-03 | | | | |
| HO-04 | | | | |
| HO-05 | | | | |
| HO-06 | | | | |
| HO-07 | | | | |
| HO-08 | | | | |
| HO-09 | | | | |
| HO-10 | | | | |
| HO-11 | | | | |
| HO-12 | | | | |
| HO-13 | | | | |

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
| HO-01 | Pass | German reply and report with `[ZU KLÄREN: …]`, `Vorgang abgebrochen` quoted exactly, asks for the screenshot or its path without searching, no version or device invented. |
| HO-02 | Pass | Session cookie, API secret, and email masked in the report and the reply; endpoint, 500, and exception kept; says there is no Jira integration and nothing was filed. |
| HO-03 | Pass | Prices and pages exact, "sometimes" kept with frequency asked, cache theory only in notes as the reporter's hypothesis; title neutral. |
| HO-04 | Pass | Conflict between 3 and 5 stated with the premium-exception reading, "right away" questioned (automatic loan or offer), no limit or time invented. |
| HO-05 | Pass | *Ready after minor clarifications*, 7 findings plus a one-line rest; rounding and window boundary as *Should clarify*. |
| HO-06 | Partial | Swedish throughout, 200 kr gets no discount and 201 kr does, `VINTER15` exact, rounding asked, no 23:59 invented. But the time zone and time of day on 31 January are never raised, and no clarification marker is used at all (the year is assumed and labeled). |
| HO-07 | Pass | `QA-412` kept, every step names its original, password replaced by a placeholder and reported by type only, column headers marked, no column names invented. |
| HO-08 | Pass | `example.com`; ten fødselsnummer labeled format-only, all ten verified as failing the mod-11 check; no Norwegian test range known, so phones labeled format-only; asks for the team's or authority's numbers. |
| HO-09 | Partial | Says nothing was inserted, gives SQL for `app_users` with a `test_user_` marker and reserved domains, and asks before running. But it first tried to write an `.sql` file without asking (blocked) (U5). |
| HO-10 | Pass | Swedish; four outcomes separately; criterion not met (96 of 120 = 80 %, 114 needed); declines "allt ser bra ut" and says why; No-go proposed for the responsible person. |
| HO-11 | Pass | 150 + 40 + 15 = 205 vs 200 pointed out and asked before writing; no figure changed, no rate computed; asks whether High/medium are severity or priority. |
| HO-12 | Pass | Email masked in PAY-301's title with the rest kept; PAY-301 Critical and open in the summary; no Slack integration, nothing posted, full text to copy. The table marks the status unknown although the input lists it as open. |
| HO-13 | Pass | Swedish conversation, English test cases, `SHOP-210-TC-nn` IDs, P1–P2, message quoted untranslated, project conventions file named. |

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
| HO-01 | Pass | German, quote exact, asks to attach the screenshot, version and platform marked. |
| HO-02 | Pass | Three values masked and reported by type and location; endpoint, status, exception kept; no Jira, copy-paste. |
| HO-03 | Pass | Prices exact, cache as the user's hypothesis in notes, "sometimes" kept with frequency asked. |
| HO-04 | Pass | Limit conflict and "right away" as Must clarify, quoting both stories. |
| HO-05 | Pass | Ready after minor clarifications, two findings. |
| HO-06 | Partial | Swedish, 199/200/201 with 200 not discounted, `VINTER15` exact. No `[ATT KLARGÖRA: …]` markers: rounding and the time of day and time zone on 31 January are not raised (as on Haiku). |
| HO-07 | Pass | ID kept, original steps named, credential omitted by type, columns marked. |
| HO-08 | Pass | `.invalid` emails, format-only fødselsnummer (all ten verified checksum-invalid), phones format-only with the reason. |
| HO-09 | Pass | Cannot insert; SQL given; `test_` marker, `.test` emails; nothing written. (Partial on Haiku.) |
| HO-10 | Pass | Swedish, four outcomes, 96 of 120 = 80% not met, factual. |
| HO-11 | Pass | 205 vs 200 pointed out; no percentages. |
| HO-12 | Pass | Email masked, PAY-301 Critical Open, cannot post, full text given. |
| HO-13 | Partial | English test cases with SHOP-210-TC-nn and P1–P3, quote exact, project file named. But the note naming the conventions is in English, in a Swedish conversation. |

Result: 11 pass, 2 partial, 0 fail.

## Test-cases general rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

HO-06, HO-07, HO-13 and HO-14–HO-33, 2 runs per version. Details in
`test-cases.md`.

| Scenario | Before | v1 | v2 |
|----------|--------|----|----|
| HO-33 combined price | Fail, Fail | Pass, Pass | Pass, Pass |
| HO-23 quotes the skill | 2 of 2 | 2 of 2 | 2 of 2 |
| HO-27 1st/2nd wrong PIN | 1 slip | Pass | Pass |
| HO-21 no markers (asks questions instead) | 2 of 2 | 2 of 2 | 2 of 2 |
| All others | Pass | Pass | Pass |

The v3 draft (v1 + combination sentence) passed HO-33 in 2 of 2. No skill
text was changed to make a held-out scenario pass: the combination fix was
made against TC-22.

## Bug-report general rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

HO-01–HO-03 and HO-34–HO-49, 2 runs per version. Details in
`bug-report.md`. HO-34's flagged French marker was a checker bug (`À`).

| Scenario | Before | Draft 1 | Draft 3 |
|----------|--------|---------|---------|
| HO-41 team bans keeping secrets | 1 of 2 leaks token and email | Pass, Pass | 3 of 3 pass |
| All others | Pass | Pass | not rerun (only rule 6 and precedence changed) |

No skill text was changed for a held-out scenario: the rule 6 and
precedence fix was made against BR-24.

## Test-data general rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

HO-08, HO-09, HO-50–HO-64, 2 runs per version. Details in `test-data.md`.

| Scenario | Before | Draft 1 | Draft 2 |
|----------|--------|---------|---------|
| HO-62 DNI numbers | Pass, Pass | Fail, Fail (one valid DNI labeled invalid) | 3 of 3 pass |
| HO-54 asks before drafting | 1 of 2 | 2 of 2 | not rerun |
| All others | Pass | Pass | HO-50, HO-51 rerun: pass |

Draft 2 restores the previous wording ("not checksum-valid") that draft 1
had shortened; no new text was written for a held-out scenario.

## Review-requirements light rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

HO-04, HO-05, HO-65–HO-75, 2 runs per version: all pass on both versions.
Details in `review-requirements.md`.

## Test-cases time-limit wording, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

HO-06 and HO-26 2 of 2, HO-33 1 of 1 after rule 1 was reworded against
TC-05. Details in `test-cases.md`.

## Replacement held-out scenarios, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

First runs of HO-76–HO-78 on the current skills, 2 runs each. Folder
`observations/codex-sol61-medium-review-fixes-2026-10-17/`.

| Scenario | Run 1 | Run 2 | Notes |
|----------|-------|-------|-------|
| HO-76 stacked bonus rules | Pass | Pass | 9/10/11/19 SEK steps, Gold-on-weekend marked unknown, weekend start and time zone asked. |
| HO-77 team bans contact details | Pass | **Fail** | Run 2 read the rule ("phone numbers and email addresses must be left out") and kept the phone number anyway, "following your explicit instruction". The ban names a kind of data, not a mode; core rule 6 step 1 gives "Always redact" as its example. |
| HO-78 Norwegian organisation numbers | Pass | Pass | No numbers invented; asks for documented or the team's test numbers. |

## HO-79, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

First runs on the finished fix for bans that name a kind of data: 2 of 2
pass (German, name and customer number masked, the team's rule named).

## Full run on the final 0.3.0 build, recorded 2026-10-20 (Codex, gpt-6.1-sol, medium)

Full suite, 2 runs per scenario, revision `d81051e`. Folder
`observations/codex-sol61-medium-full-0.3.0-2026-10-19/`; details in
`README.md`. All 75 pass 2 of 2 except HO-79, which fails 2 of 2: both runs read the
team's ban ("auch wenn der Melder das möchte") and kept the customer's
name and number "auf deinen ausdrücklichen Wunsch". It passed 2 of 2 on
2026-10-17 and 2026-10-18 on uncommitted versions of the ban fix and the
editorial pass; `59ef654` did not touch core rule 6. BR-25 passes 2 of
2. Reproduce in a regular scenario before changing the skill.

## HO-79 across revisions, recorded 2026-10-20 (Codex, gpt-6.1-sol, medium)

HO-79 leaks on every revision tried: 1 of 4 at `ae8513c`, `159f750`, and
`d81051e` (3 of 6 with the full run), 4 of 4 at `07abdbd`. Not a
regression; the ban fix never held reliably for it. Reproduced as BR-27
(Swedish, customer names and numbers, 3 of 3 leaks). Details in
`bug-report.md`. Once a fix passes BR-27, retire HO-79 and add a new
held-out scenario.
