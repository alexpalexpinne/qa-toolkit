# Test cases: review-requirements

## RR-01 Vague user story

**Tests:** Finding real problems, verdict rules, proposals with clarification
markers.

**Input:**
```
/review-requirements
As a customer I want to reset my password so that I can access my account
if I forget it.

Acceptance criteria:
- The user should receive an email quickly.
- The reset link should be valid for a reasonable time.
- The new password must be secure.
- Error handling should be user-friendly.
```

**Must:**
- Verdict: "Needs clarification before development" (there are must-clarify
  findings).
- Flag at least: link validity ("reasonable time"), password rules
  ("secure"), what happens when the email address is not registered, and
  what "user-friendly error handling" means.
- Quote the exact text for each finding and end each with a question.
- Proposed acceptance criteria mark unknown values as `[TO CLARIFY: …]`,
  e.g. `[TO CLARIFY: link validity]`.
- Proposed acceptance criteria match the requirement's bullet format, as
  plain sentences, not Given/When/Then.

**Must not:**
- Invent concrete values such as "24 hours" or "at least 12 characters" as
  if they were decided.

---

## RR-02 Well-written story

**Tests:** Not manufacturing findings (noise).

**Input:**
```
/review-requirements
As a registered user I want to change the display name on my profile so
that other users see the name I prefer.

Acceptance criteria:
1. Given I am logged in and on my profile page, when I enter a new display
   name of 1–50 characters and select Save, then the new name is shown on
   my profile and on all my existing comments within 5 seconds.
2. Given I enter an empty name or more than 50 characters, when I select
   Save, then the name is not saved and the message "Display name must be
   1–50 characters" is shown under the field.
3. Display names may contain letters from any script, digits, spaces,
   hyphens, and apostrophes. Other characters are rejected with the message
   "Display name contains characters that are not allowed".
4. Display names do not need to be unique.
5. Out of scope: changing the login email address.
```

**Must:**
- Verdict: "Ready" or "Ready after minor clarifications".
- Few findings (roughly 0–4), each one genuinely useful (for example leading
  and trailing spaces, or profanity filtering).

**Must not:**
- Produce any *Must clarify* finding that the text already answers.
- Flag "may" in criterion 3 as unclear obligation (it clearly describes
  allowed characters).

---

## RR-03 RFC 2119 wording is respected

**Tests:** Obligation words method, step 2 (document definitions).

**Input:**
```
/review-requirements
The key words MUST, SHOULD, and MAY in this document are to be interpreted
as described in RFC 2119.

REQ-12: The API MUST reject requests without a valid API key with HTTP 401.
REQ-13: The API SHOULD include a Retry-After header in HTTP 429 responses.
REQ-14: Clients MAY cache responses for up to 60 seconds.
```

**Must:**
- Treat MUST, SHOULD, and MAY according to RFC 2119.
- Focus findings on real gaps, for example what counts as a "valid" API key
  (expired, revoked?) or what the 401 response body contains.

**Must not:**
- Flag SHOULD or MAY as unclear obligation words.

---

## RR-04 Requirement in Swedish, no conventions

**Tests:** Core rule 8 (language, headings), format of proposed criteria,
obligation words method step 3–4.

**Input:**
```
/review-requirements
Som administratör vill jag kunna inaktivera användarkonton så att tidigare
anställda inte längre kan logga in.

- Inaktiverade användare ska inte kunna logga in.
- Användaren bör få ett mejl när kontot inaktiveras.
- Administratören kan återaktivera kontot.
- Aktiva sessioner bör avslutas.
```

**Must:**
- Write the whole review in Swedish, including headings, priorities, and
  verdict.
- Write proposed acceptance criteria as plain Swedish sentences or bullets,
  matching the requirement's bullet format.
- Ask whether "bör" items are required or optional, or flag that the
  obligation of "Aktiva sessioner bör avslutas" is unclear given its
  security impact.
- Flag the missing: what happens to the user's data, and what the user sees
  when trying to log in.

**Must not:**
- Assume what "bör" means without asking or flagging it.
- Mix English and Swedish headings.
- Introduce Given/When/Then (neither the requirement nor any convention
  uses it).

---

## RR-05 Team conventions define obligation words

**Tests:** Team conventions take precedence.

**Setup:** Replace the placeholder in
`review-requirements/references/team-conventions.md` with the example from
the same file (German, muss/soll/kann, English Gherkin keywords, Kunde vs
Nutzer).

**Input:**
```
/review-requirements
Als Nutzer möchte ich meine Rechnungen als PDF herunterladen können.

- Der Download muss innerhalb von 3 Sekunden starten.
- Die PDF soll das Logo des Kunden enthalten.
- Der Nutzer kann mehrere Rechnungen gleichzeitig herunterladen.
```

**Must:**
- Write the review in German.
- Treat "soll" as recommended and "kann" as optional, as the conventions
  say, without asking about them.
- Use English Given/When/Then keywords with German content.
- Apply the terminology: "Kunde" is the paying organization.

**Must not:**
- Ask what "muss", "soll", or "kann" mean.

---

## RR-06 Conflict between stories

**Tests:** Mode B (set of items).

**Input:**
```
/review-requirements
Story 1: As a visitor I want to buy products without creating an account,
so that checkout is fast.

Story 2: As the shop owner I want every order to be linked to a customer
account, so that we can offer order history and returns.

Story 3: As a customer I want to see all my previous orders, so that I can
reorder easily.
```

**Must:**
- Identify the conflict between story 1 (no account) and story 2 (every
  order linked to an account) as *Must clarify*.
- Ask how guest orders relate to order history (story 3).

**Must not:**
- Review the stories only one by one without noticing the conflict.

---

## RR-07 Noise limit

**Tests:** Core rule 3 (max 7 non-must findings, summary line).

**Input:**
```
/review-requirements
The search page should be fast and user-friendly. Results should normally
be sorted in a sensible way. The page should look modern and clean. Filters
should be intuitive. It should work on most devices. Loading should be
quick. Errors should be handled gracefully. The design should be
consistent with the rest of the site, etc. Ideally the search should
support synonyms. It should be possible to search in several languages.
```

**Must:**
- Respect the limit: all *Must clarify* findings, plus at most 7 *Should
  clarify* and *Consider* findings combined.
- Summarize the remaining issues in one line.
- Point out the missing basics (what can be searched, what a result shows,
  what happens with no results) rather than only listing vague words.

**Must not:**
- List every "should" as a separate finding.

---

## RR-08 Sensitive data in a requirement

**Tests:** Core rule 6.

**Input:**
```
/review-requirements
As support staff I want to look up a customer's orders. Example: customer
Jane Doe, jane.doe@example.com, phone +46 70 000 00 00. Use the test API
key FAKE-KEY-1234567890 to call the order service.
```

**Must:**
- Not repeat the name, email, phone number, or API key in the review.
- Tell the user that personal data and a credential should be removed from
  the requirement.
- Still review the actual requirement (permissions, what support staff may
  see, logging of lookups).

---

## RR-09 Posting needs an integration and confirmation

**Tests:** Core rule 7, step 6.

**Input:** Complete RR-01, then:
```
Post this as a comment on PROJ-123.
```

**Must (no tracker integration available):**
- Say that it cannot post directly, and offer the review as copy-paste
  text.

**Must (tracker integration available):**
- Confirm the item, show exactly what will be posted, and wait for an
  explicit "yes".

**Must not:**
- Claim to have posted anything it did not post.

---

## RR-10 Story checked against its HLR

**Tests:** Supporting material (Step 1–2): contradiction with the parent,
missing parent requirement, answered questions not asked again, parent not
reviewed.

**Input:**
```
/review-requirements
Review story SHOP-88. HLR-4 is its parent, included for context.

Story SHOP-88: As a customer I want my account to be locked after repeated
failed logins, so that nobody can guess my password.

Acceptance criteria:
- After 3 failed login attempts in a row, the account is locked.
- A locked account shows the message "Your account is locked. Try again
  later."

HLR-4: The system shall lock an account after 5 consecutive failed login
attempts, counted per account regardless of device, and shall notify the
account owner by email. Locked accounts shall be unlocked automatically
after an appropriate period.
```

**Must:**
- Flag the contradiction between 3 attempts (story) and 5 (HLR-4) as
  *Must clarify*, quoting both and naming HLR-4.
- Flag the missing email notification as "Missing", citing HLR-4.
- Ask how long the account stays locked ("Try again later").

**Must not:**
- Ask whether attempts are counted per device or per account (HLR-4
  answers it).
- Report "appropriate period" in HLR-4 as a finding about HLR-4's own
  wording; the HLR is not under review.
- Claim HLR-4 says anything beyond its text.

---

## RR-11 Stories cover their HLR

**Tests:** Mode B with a parent: coverage of the parent by its children.

**Input:**
```
/review-requirements
These are all the stories for HLR-7. Do they cover it?

HLR-7: The system shall let customers export their order history as CSV
and PDF, and shall email the customer a download link when the export is
ready.

Story SHOP-101: As a customer I want to export my order history as a CSV
file, so that I can open it in a spreadsheet.

Story SHOP-102: As a customer I want an email with a download link when my
export is ready, so that I do not have to wait on the page.
```

**Must:**
- Report that no story covers PDF export.
- Still review the two stories themselves (for example what the CSV
  contains, how long the download link is valid).

**Must not:**
- Write the missing story as if it were decided; a proposal is fine if
  labeled as one.
- Review HLR-7's own wording.

---

## RR-12 Use case with missing alternative flows

**Tests:** Use case format, checklist section 6, acceptance criteria in
the requirement's own format.

**Input:**
```
/review-requirements
UC-12 Reset password
Actor: Registered customer
Preconditions: The customer has an account.
Main flow:
1. Customer selects "Forgot password".
2. Customer enters their email address.
3. System sends a reset link and shows "Check your email".
4. Customer opens the link and enters a new password.
5. System saves the password and shows a confirmation.
Alternative flows:
2a. Email address not registered: System shows "Check your email" without
    sending anything, so that it does not reveal which addresses have
    accounts.
End state: The customer can log in with the new password.
```

**Must:**
- Flag missing alternative flows for step 4 at least: expired or already
  used link, and a new password that does not meet the password rules.
- Propose additions in the use case's own numbering (for example "4a."),
  labeled as proposals, with unknown values as `[TO CLARIFY: …]`.

**Must not:**
- Flag 2a as missing or ask what happens for an unregistered address.
- Rewrite the use case as Given/When/Then.

---

## RR-13 Team conventions set the review language

**Tests:** Core rule 8 precedence: team conventions' review language over the
requirement's language.

**Setup:** Replace the placeholder in
`review-requirements/references/team-conventions.md` with:

```markdown
## Language
Requirements may be written in English or Swedish. Reviews are always
written in Swedish.
```

**Input:**
```
/review-requirements
As a shop owner I want to offer discount codes so that I can run
campaigns.

- A discount code gives a percentage off the order total.
- Codes should expire.
- Only one code can be used per order.
```

**Must:**
- Write the review in Swedish, including headings, priorities, verdict, and
  clarification markers.
- Quote the English requirement text exactly, untranslated, with Swedish
  translations in parentheses where helpful.
- Still find real gaps, for example when codes expire and what the customer
  sees for an expired or invalid code.

**Must not:**
- Write the review in English because the requirement is in English.

---

## Results

The user confirmed that every run and rerun in this requirements-review round
used **ChatGPT 5.6 Terra** with reasoning effort **xhigh** in Codex. This is
user-reported attribution, recorded using the supplied model label. Earlier
observations that say the model was not supplied describe the evidence
available at the time; this confirmation resolves that missing metadata.
Limits concerning omitted tool activity or rendered output still apply.

| Test | Run 1 | Later runs | Assistant / model / effort | Notes |
|------|-------|-------|-------------------|-------|
| RR-01 | Pass: supplied content | | Codex / ChatGPT 5.6 Terra / xhigh | User-supplied response and shown skill-reference reads, reviewed 2026-10-13. All scenario content checks pass. Duplicate criterion was confirmed to be a copy-paste error. See dated observation below. |
| RR-02 | Fail: verdict and focus | Pass: supplied rerun content | Codex / ChatGPT 5.6 Terra / xhigh | Run 1 over-prioritized edge cases. After the focused correction, run 2 uses Ready after minor clarifications and only lower-priority findings. It has six findings, slightly above the rough 0–4 target but all are relevant and non-duplicative. See dated observations below. |
| RR-03 | Pass: supplied content | | Codex / ChatGPT 5.6 Terra / xhigh | Respects the stated RFC 2119 definitions and raises concrete API-key, endpoint-scope, retry-header, and cache-scope questions without treating SHOULD or MAY as unclear. See dated observation below. |
| RR-04 | Fail: missing data handling | Pass: supplied rerun content | Codex / ChatGPT 5.6 Terra / xhigh | The initial Swedish review missed existing-data handling. After the focused account-lifecycle correction, the rerun asks what happens to data and permissions while inactive and after reactivation, and meets all scenario checks. See dated observations below. |
| RR-05 | Fail: obligation-word prioritization | Pass: supplied rerun content | Codex / ChatGPT 5.6 Terra / xhigh | The first review did not apply the convention-defined priorities. After the focused correction, the rerun identifies `soll` as recommended and `kann` as optional, keeps them in Should clarify, and meets every scenario check. See dated observations below. |
| RR-06 | Pass: supplied content | | Codex / ChatGPT 5.6 Terra / xhigh | Treats the related stories as a set, identifies the guest-checkout versus account-linked-order conflict as Must clarify, and asks how a guest can access order history. See dated observation below. |
| RR-07 | Partial: duplicate question | Runs 2–3: partial; run 4: pass, supplied content | Codex / ChatGPT 5.6 Terra / xhigh | Runs 2 and 3 miss result-display information. After the main-flow correction, run 4 covers searchable content, result information, and no matches; groups related wording; and has six Should plus one Consider finding. RR-08 may proceed. See dated observations below. |
| RR-08 | Pass: supplied content | | Codex / ChatGPT 5.6 Terra / xhigh | Does not repeat the example's personal details or API key, recommends their removal/replacement, and still reviews access scope, displayed order information, lookup behavior, service failures, and audit logging. See dated observation below. |
| RR-09 | Pass: no-connection path, supplied excerpt | | Codex / ChatGPT 5.6 Terra / xhigh | Checks available integrations, explains that it cannot post without a tracker connection, and offers the password-reset review as copy-paste text. No posting claim or publication action is shown. Connected-tracker confirmation path remains untested. See dated observation below. |
| RR-10 | Pass | | Codex / gpt-6.1-sol / xhigh | See the 2026-10-13 regression round below. |
| RR-11 | Pass | | Codex / gpt-6.1-sol / xhigh | See the 2026-10-13 regression round below. |
| RR-12 | Pass | | Codex / gpt-6.1-sol / xhigh | See the 2026-10-13 regression round below. |
| RR-13 | Pass (3 of 3) | | Codex / gpt-6.1-sol / xhigh | See the 2026-10-13 regression round below. |

## Codex RR-01 supplied response review recorded 2026-10-13

The user supplied the response to the password-reset story and a tool summary
showing reads of the installed skill, conventions, review checklist, and
ambiguity patterns. The review gives "Needs clarification before development",
with four Must clarify findings quoting the supplied criteria. It covers
delivery timing, link validity and the expiry boundary, password policy, and
observable error messages/recovery. Four Should clarify findings cover the
missing unregistered-address response, link reuse/repeated requests,
post-reset behavior, and the mixed obligation words. Each finding includes
a concrete question; the non-must findings stay within the limit of seven.
The questions within review findings are not an immediate interview batch.

Proposed acceptance criteria remain plain bullet sentences rather than
Given/When/Then, explicitly labeled as proposals, with unresolved values and
behavior expressed using [TO CLARIFY: ...] markers. No expiry duration,
password length, or other undecided business value is supplied as an agreed
fact. Assumptions distinguish the proposed email-address input scenario from
the requirement's known details. No posting or unsupported inspection claim
appears in the supplied reply. These RR-01 supplied-content checks pass.

The pasted response initially appeared to repeat the expired-link criterion.
The user confirmed that this was a copy-paste error, so it is not a skill
finding. Other copy formatting glitches are not grounds to infer a runtime
formatting failure. Original rendered styling, model/version, omitted tool
arguments/activity, and a second independent run remain unverified.

Installed manifest SHA-256 inspected for this review:
`eb909ff57ae8a3921c6edb8781c774279e11952f3448a510e6c2753c2fce1dfb`.
Installed conventions SHA-256 (placeholder, no active team conventions):
`a2fea1c91eaaa3d6aeb9bfc40272fd72301a0e44005464f823031bf23c0d3849`.
No skill changes are needed. Continue to RR-02 in a fresh chat.

## Codex RR-02 supplied response review recorded 2026-10-13

The user supplied a review with "Needs clarification before development".
Three Must clarify findings concern character counting, the precise allowed
character categories, and timing/live-refresh behavior. Three Should clarify
findings concern whitespace, validation message location/conflicts, and
unsuccessful saves. The review recognizes the stated main behavior, errors,
uniqueness, and scope, and does not incorrectly flag "may contain" as an
unclear obligation. Quotes, concrete questions, and clarification markers
appear in the supplied response.

Record a failure against RR-02's expected verdict (Ready or Ready after minor
clarifications) and focused findings (roughly zero to four). The proposed gaps
can be useful refinements, especially for international names and update
behavior, but the response does not establish why they must all block this
feature rather than merit lower-priority clarification. The broad technical
questions also increase the amount of detail requested for a well-specified
story. Do not discard those concerns or introduce decided product rules just
to obtain a Ready verdict.

Parts of the pasted proposed criteria appear truncated or joined. Based on
the earlier confirmed copy-paste issues, do not infer an original formatting
or generation failure from those fragments. No tool activity, model/version,
or complete original rendered output was supplied for this run.

The inspected Codex manifest before correction had SHA-256
`eb909ff57ae8a3921c6edb8781c774279e11952f3448a510e6c2753c2fce1dfb`.
Step 2 now explains that an unanswered detail is not automatically a blocker:
identify the intended behavior or acceptance decision that cannot be
established, and use lower priority for additional precision or edge cases
unless their consequences justify blocking development. Related questions
should be grouped and scoped to decisions that matter. The verdict table,
finding limits, and core rules are unchanged.

The corrected manifest was synced to Codex and Claude installs; the Claude
manifest was inspected as an older version before replacement. Source and
both installed conventions were byte-checked unchanged. Structural validation
passed on a temporary strict-host copy removing only the existing Claude
frontmatter extension. No behavioral rerun has occurred, so this correction
does not change the failed result. Rerun RR-02 in a fresh chat.

Corrected source and installed manifest SHA-256:
`2e69a2a7927b6011f297342a037c7438d45953d5a034ad2d93b186f649047a7d`.

### Codex RR-02 rerun review recorded 2026-10-13

The rerun gives "Ready after minor clarifications" with no Must clarify
findings. It does not flag "may contain" as an unclear obligation. The five
Should clarify findings concern character counting, whitespace, permitted
marks and punctuation variants, the timing/scope of comment updates, and
save failures; the one Consider finding concerns validation-error precedence
and placement. Each is relevant to a display-name feature and asks a concrete
question. The proposed acceptance criteria retain the requirement's
Given/When/Then format and mark unresolved behavior with [TO CLARIFY: ...].

This passes RR-02's verdict and no-noise requirements. Six findings are
slightly above the scenario's rough target of zero to four, but are focused,
non-duplicative, and substantially less disruptive than the original
blocking review. No further instruction change is warranted from one run.
The pasted output contains joined or repeated fragments; prior confirmed
copy-paste artifacts mean those fragments are not treated as behavioral
formatting failures. Tool activity, original rendered formatting, and
model/version were not supplied. The corrected skill behavior is accepted
on the supplied rerun content; continue to RR-03.

## Codex RR-03 supplied response review recorded 2026-10-13

The supplied review recognizes that MUST, SHOULD, and MAY have their stated
RFC 2119 meanings. It does not describe SHOULD or MAY as unclear obligation
words. Instead, it asks concrete questions about API-key transport and
validity conditions, which endpoints require a key, Retry-After value format
and exceptions, and cacheable response scope/mechanism. These are real
implementation and testability gaps; no particular business rule is invented.

"Needs clarification before development" is supported by the undefined valid
API-key conditions and protected-endpoint scope. Each finding quotes the
relevant text and ends with an answerable question. The proposed criteria are
explicit proposals with unresolved content marked [TO CLARIFY: ...]. The
pasted repeated fragments under the caching question and assumptions are
treated as copy-paste artifacts, consistent with previously confirmed output
copying issues. Tool activity, original rendered formatting, and model/version
were not supplied. Record a pass for the supplied RR-03 content. No skill
change is needed; continue to RR-04 in a fresh chat.

## Codex RR-04 supplied response review recorded 2026-10-13

The supplied review is consistently Swedish, including its headings,
priorities, verdict, questions, and clarification markers. It does not
introduce Given/When/Then. The review identifies access-control roles,
affected login paths, notification obligations, active sessions/tokens, and
reactivation behavior. It explicitly asks whether both `bör` statements are
mandatory or optional, including the security-relevant session behavior. The
denied-login criterion includes [ATT KLARGÖRA: användarens meddelande], so the
review does cover what a deactivated user sees when attempting to sign in.

Record RR-04 as a failure because it does not ask what happens to the user's
existing data after deactivation. It asks about tokens, sessions, and login
credentials, but none answers whether account data is retained, hidden,
deleted, or otherwise handled. That is a distinct lifecycle decision required
by the scenario. The repeated notification criterion and joined fragments in
the pasted output are not assessed as formatting failures because prior runs
have established copy-paste artifacts. Tool activity, original rendering, and
model/version were not supplied.

Step 2 now explicitly directs reviews of account deactivation, deletion, and
reactivation to check existing-data handling and denied-access feedback. This
is a narrow account-lifecycle clarification rather than a general new review
requirement. It was synced to the Codex and Claude installations. The bundled
quick validator rejects the existing Claude-specific `disable-model-invocation`
frontmatter field; no other validation failure was reported. The corrected
behavior needs a fresh RR-04 run and does not alter this failed result.

Corrected source and installed manifest SHA-256:
`3841b9d001959e0d076b568c96a81c4d8057500f06c147a8f21b2cd64ee523ff`.

## Codex RR-04 supplied rerun review recorded 2026-10-13

The rerun passes all scenario checks. It is wholly in Swedish, uses Swedish
headings and plain Swedish acceptance-criteria bullets, and does not introduce
Given/When/Then. It treats both `bör` statements as requiring clarification
rather than silently assigning them a requirement level.

It asks what an inactive user sees on denied login and, critically, asks what
happens to existing user data and permissions while the account is inactive
and after reactivation. The questions about administrator roles, self-
deactivation, session scope, delivery failure, and login methods are relevant
clarifications within the stated account-lifecycle scope. As in prior supplied
responses, joined list fragments are treated as copy-paste artifacts rather
than output-format failures. Record the corrected RR-04 run as a pass.

## Codex RR-05 supplied response review recorded 2026-10-13

The supplied review passes the language and formatting parts of this
scenario: it is in German, uses English `Given`/`When`/`Then` keywords with
German content, and correctly states that `Kunde` means the paying
organization. It also does not ask what `muss`, `soll`, or `kann` mean.

Record the run as a failure because it does not apply the convention's
defined meanings in its prioritization. It does not state that the `soll`
logo behavior is recommended or that the `kann` multiple-download behavior
is optional. Instead, the summary identifies the scope of multiple downloads
as unresolved alongside mandatory concerns, and its criterion treats that
optional behavior as an assumed implementation path. The supplied text has
joined and duplicated fragments, so the assessment uses the observable
content rather than treating those copying artifacts as separate failures.

Step 2 now requires defined obligation words to guide priorities, prevents
undefined details of recommended or optional items from becoming *Must
clarify* findings solely for that reason, and calls for their status to be
stated when it affects scope or priority. The corrected behavior needs a
fresh RR-05 run.

## Codex RR-05 supplied rerun review recorded 2026-10-13

The rerun passes all scenario checks. It is wholly in German, uses English
`Given`/`When`/`Then` keywords with German content, and explicitly preserves
the convention that `Kunde` is the paying organization. It identifies `soll`
as recommended and `kann` as optional without asking what either word means.
The logo and multiple-download questions are correctly placed under *Sollte
geklärt werden*, while access rights and the mandatory three-second limit are
appropriately blocking. The optional multiple-download question asks whether
the behavior belongs in the story, rather than treating its presence as a
mandatory requirement. Record the corrected RR-05 run as a pass.

## Codex RR-06 supplied response review recorded 2026-10-13

The supplied review correctly handles the three stories as a related set. It
identifies the direct conflict between checkout without an account and the
requirement that every order be linked to a customer account as *Must
clarify*. Its question explicitly asks which account-linking model applies to
guest checkout and how the visitor can access the resulting order history.

The additional access-control, checkout-speed, failure, and order-state
questions are relevant and remain within the non-Must finding limit. The
proposed criteria preserve the unresolved business decisions as clarification
markers. Record RR-06 as a pass.

## Codex RR-07 supplied response review recorded 2026-10-13

The supplied review covers the missing search basics: searchable content and
fields, what each result shows, and empty-query/no-match behavior. It groups
related vague wording instead of listing every `should` separately. Its four
Should clarify findings and zero Consider findings remain within the limit
of seven non-Must findings.

Record a partial result because Must clarify 4 and Should clarify 4 both ask
whether synonym support is required. That violates the existing Step 5 check
to merge duplicate questions and adds avoidable noise. The absent summary
line is not independently counted as a failure: such a line is needed when
further minor issues are omitted, and the supplied response does not establish
that this happened. No instruction change is warranted for a rule already
stated clearly; a fresh RR-07 run is pending to check deduplication.

## Codex RR-07 supplied rerun review recorded 2026-10-13

The rerun fixes the duplicated synonym-scope question, groups related vague
wording, and has six Should clarify findings with no Consider findings. It
therefore passes the noise-limit and deduplication checks. It also asks what
content and fields are searched and covers empty-query/no-match behavior.

Record a partial result because it does not ask what information each result
must display. Searchable fields and expected matching records establish
result inclusion, not the information presented in each result. That distinct
completeness check is explicitly required by RR-07 and was covered in run 1
but missing in run 2.

The completeness checklist now includes a general Outputs row asking what
information must be shown or returned and in what format. This is not
search-specific. The source, Codex, and Claude copies were updated together;
a further fresh run is pending.

## Codex RR-07 third supplied run review recorded 2026-10-13

The third run has five Should clarify findings, no Consider findings, and no
duplicated questions. Related vague phrases are grouped. It passes the
noise-limit checks and covers searchable content, matching, and no-result
behavior, but again does not ask what information a result must display.
It therefore remains partial against the full scenario criteria.

The updated Outputs checklist row is present and identical in the source,
Codex, and Claude copies. The pasted response does not show tool activity,
so reading that updated reference in the tested session is not independently
confirmed. No further instruction changes were made. Retain the completeness
gap as open while proceeding to RR-08; do not record RR-07 as a full pass.

### RR-07 follow-up correction recorded 2026-10-13

The user challenged moving on with an unmet acceptance check. Testing RR-08
is now on hold while RR-07 is resolved. The repeated result-information
omission is not accepted as a pass.

Step 2 now starts with the feature's main flow: actor, inputs, and the
information shown or state changed on success. Missing decisions needed to
test that flow must be raised before vague-word findings. This general
workflow correction was synced to Codex and Claude. It has not yet been
behaviorally validated; a fresh run using the unchanged RR-07 input is needed.

## Codex RR-07 fourth supplied run review recorded 2026-10-13

The fourth run meets the full scenario criteria. Its first Must clarify
question explicitly asks which users can search which content and fields,
what information each result must show, and what happens when there are no
matches. This resolves the result-information omission in runs 2 and 3.

It groups related vague wording instead of listing every `should` separately.
Six Should clarify findings plus one Consider finding exactly meet the
seven-finding non-Must limit. The synonym release-scope question is not
duplicated across priority sections. No further omitted issues are evidenced,
so a summary of omitted findings is not required for this response.

Record a pass for the supplied RR-07 content. Tool-read activity and the model
version were not supplied, so the assessment is limited to the pasted review.
RR-08 is no longer on hold. No additional skill changes were made.

## Codex RR-08 supplied response review recorded 2026-10-13

The supplied review passes all scenario checks. None of the example's name,
email address, phone number, or API key is repeated. The summary explicitly
says that the personal data and credential should be removed from the
requirement; a finding asks for anonymized references and approved secret
management.

The review still assesses the actual feature: permitted support roles and
access scope, required order information, matching behavior, service failures,
and lookup audit/masking expectations. It does not attempt an order-service
call. Record a pass for the supplied content; no skill change is needed.
Tool activity, other commentary, and the model version were not supplied,
so the assessment is limited to the pasted review.

## Codex RR-09 supplied response review recorded 2026-10-13

The supplied excerpt passes the no-tracker branch. It reads the installed
review skill, announces that any available posting path would require a
preview and approval, and searches for integrations using plugin-management.
When no connection is available, it explicitly says it cannot post to the
requested item and offers the password-reset review as copy-paste text.
It neither claims that a comment was posted nor shows a publication action.

Only the opening of the fallback review was supplied. This supports the
delivery-behavior checks, not verification of the entire copied comment.
The connected-tracker confirmation path remains untested. No skill change
is needed for the observed no-connection behavior.

All nine RR scenarios now have a passing observed result, including corrected
reruns. Earlier failures and partial results are preserved. These observations
span skill revisions and do not constitute a complete repeated regression run
against the final installed revision.

## Regression round recorded 2026-10-13 (Codex, gpt-6.1-sol, xhigh)

Run by Claude Code through `codex exec`, one fresh ephemeral session per
scenario, in an empty folder. Skills were loaded from the installed copy in
`~/.agents/skills/`; RR-05 used a project-local copy named
`review-requirements-rr05` with the conventions example filled in. The event
logs show each run reading `SKILL.md`, `review-checklist.md`,
`ambiguity-patterns.md`, and `team-conventions.md`. Prompts and answers are
in `observations/codex-rr-regression-2026-10-13/`.

Revision: uncommitted changes on top of `56ff8f7` that add supporting
material (item under review versus parent), parent coverage checks, use-case
review, the *Lifecycle* checklist row, and the obligation-word priority note
in `ambiguity-patterns.md`.

A first attempt with Codex's read-only sandbox is not counted: the sandbox
could not start inside Claude Code's sandbox, every file read failed, and
the reviews were written without the reference files.

| Test | Result | Notes |
|------|--------|-------|
| RR-01 | Pass | Correct verdict; all four required findings; markers, no invented values. |
| RR-03 | Pass | SHOULD/MAY not flagged. Key validity rated *Must clarify*, so the verdict is stricter than the earlier Terra run; the scenario allows either. |
| RR-04 run 1 | Partial | Swedish, "bör" questioned, data during deactivation and after reactivation asked. Missed what the user sees when login is denied. |
| RR-04 runs 2–4 | Pass (3 of 3) | After adding a pointer to the *Lifecycle* row in Step 2 of `SKILL.md`, every run asks for the message shown to a deactivated user, plus data handling and "bör". |
| RR-05 | Pass | soll/kann applied without asking, English Gherkin keywords, "Kunde" as the paying organization. Also applied the example's new *Requirement structure* section and asked for the epic and HLR link. |
| RR-06 | Pass | Conflict as *Must clarify*; asks how guest orders reach order history. |
| RR-10 | Pass | 3 vs 5 attempts as *Must clarify* quoting HLR-4; missing notification cited to HLR-4; lock duration asked; HLR wording not reviewed. It suggests the per-device rule from HLR-4 be included in the criteria rather than asking about it. |
| RR-11 | Pass | PDF export reported as uncovered (*Must clarify*); both stories still reviewed; PDF criterion labeled as a proposal. |
| RR-12 | Pass | Missing flows for expired/used link and rejected password, proposed as 4a/4b with markers; 2a not flagged as missing; no Given/When/Then. Proposals are sentences rather than use-case step style. |
| RR-02 | Pass, with note | Ready after minor clarifications; no *Must clarify*; "may" not flagged. Six *Should clarify* findings, above the rough 0–4 target (as in the earlier accepted Terra run). Findings 2 and 4 overlap (Unicode counting and character forms). |
| RR-07 | Pass | Four *Must clarify* plus six *Should clarify*, within the limit. Covers searchable content, result information, and no matches; related vague wording grouped rather than one finding per "should". |
| RR-08 | Pass, with note | No name, email, phone number, or API key repeated in any message; removal recommended by type. Permissions and displayed order information reviewed. Unlike the earlier Terra run, it does not mention audit logging of lookups, which the scenario lists as an example. |
| RR-09 | Partial | Turn 2 (no tracker connected): searched available plugins for Jira, did not post, and did not claim to have posted. It did **not** offer the review as copy-paste text; it asked the user to connect a tracker and share the item URL. It also inferred Jira from the `PROJ-123` key when searching plugins. |

| RR-09 reruns 1–3 | 2 of 3 pass | After adding to Step 6 "If the user asks to post and there is no working integration, say so and give the exact text ready to copy and paste. Do not guess the tracker from the item's ID." Runs 1 and 3: say nothing was posted and include the full review in the reply. Run 2: wrote the review to a file `PROJ-123-comment.md` in the working folder and only linked to it. No run guessed Jira; plugin searches used generic queries. |
| RR-09 reruns 4–6 | Pass (3 of 3) | After changing the line to "give the exact text in your reply, ready to copy and paste". All three say nothing was posted and include the full review in the reply; no files written; plugin searches (two runs) used generic queries. |
| RR-13 runs 1–3 | Pass (3 of 3) | Added after a full read-through found that core rule 8 ignored the team conventions' review language. After changing rule 8 to "the language the user asks for; otherwise the review language set by the team conventions; otherwise the language of the requirement", all three runs write the review in Swedish (headings, verdict, priorities, `[ATT FÖRTYDLIGA/KLARGÖRA: …]` markers), keep the English quotes untranslated, and ask about expiry rules and what the customer sees for an expired or unknown code. |

RR-09 ran as a saved (non-ephemeral) Codex session so the second turn could
resume it; the thread ID is in the local run folder.

## Full regression on GPT-5.6-Luna, recorded 2026-10-13

One run per scenario through `codex exec` with `gpt-5.6-luna` at `max`
effort, each in a fresh session and an empty folder (same setups as the
earlier rounds). Skill content as committed in `fab9517`, before the fixes
in `81801ea`. Transcripts are in
`observations/codex-luna-regression-2026-10-13/rr/`.

| Test | Result | Notes |
|------|--------|-------|
| RR-01 | Pass | Needs clarification; link validity, password rules, unregistered email, error handling; no invented values. |
| RR-02 | Fail | Well-written story rated “Needs clarification”: Unicode length counting and the 5-second timer start as Must clarify, plus seven further findings. |
| RR-03 | Pass | SHOULD and MAY not flagged; key validity questioned. |
| RR-04 | Pass | Swedish; data handling, the message shown when login is denied, and “bör” all asked. |
| RR-05 | Partial | German, “kann” read as optional, English Gherkin keywords, “Kunde” correct. Still made the optional bulk download Must clarify and asked whether it is mandatory; one English “Missing:” label. |
| RR-06 | Pass | Guest versus account conflict as Must clarify; guest order history asked. |
| RR-07 | Partial | Within the limit; searchable content and result information covered, but not what happens with no results. |
| RR-08 | Pass | No personal data or key repeated; removal recommended. |
| RR-09 | Pass, with note | No integration: full text given, nothing posted. Named Jira/Atlassian, a guess from the item ID. |
| RR-10 | Pass | 3 versus 5 attempts as Must clarify citing HLR-4; missing notification cited; HLR wording not reviewed. |
| RR-11 | Pass | PDF export reported as uncovered; stories still reviewed. |
| RR-12 | Partial | Missing flows found, no Given/When/Then, 2a not flagged; proposals written as plain numbered sentences rather than in use-case numbering (4a). |
| RR-13 | Pass | Review in Swedish per the team conventions; English quotes kept. |

Result: 9 pass, 3 partial, 1 fail.

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
| RR-01 | Pass | Correct verdict; all four required findings; proposals as plain bullets with markers; no invented values. |
| RR-02 | **Fail** | "Needs clarification before development" for a well-written story; a *Must clarify* finding on combining marks and normalization. |
| RR-03 | Pass | SHOULD and MAY not flagged; key validity as the real gap. |
| RR-04 | Pass, with note | Swedish throughout, "bör" flagged, data and login message covered, Swedish marker. The finding label "Missing:" stays in English. |
| RR-05 | Pass, with note | German; soll and kann applied from the conventions without asking; English Given/When/Then with German content. Marker left as `[TO CLARIFY]`. |
| RR-06 | Pass | Conflict between stories 1 and 2 as *Must clarify*; guest access to history asked. |
| RR-07 | Pass | Five *Must clarify*, seven others; missing basics found. |
| RR-08 | Pass | No personal data or key repeated; removal and key rotation advised; access and logging reviewed. |
| RR-09 | Pass | Cannot post; review given as copy-paste text; tracker not guessed. |
| RR-10 | Pass | 3 versus 5 attempts with HLR-4 named; email and unlock missing; counting rule raised as a consistency point, not asked. |
| RR-11 | Pass | PDF export not covered by any story; both stories still reviewed; proposals labeled. |
| RR-12 | Pass | Step 4 alternative flows proposed as 4a–4c with markers; use case not rewritten. |
| RR-13 | Pass, with note | Swedish review of an English requirement, with translations. The same sentence appears as both a *Must* and a *Should* finding. |

Result: 12 pass, 0 partial, 1 fail.

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
| RR-01 | Pass | Needs clarification; link validity, password rules, unregistered email, and error handling all flagged with quotes and questions; proposals are plain sentences with markers, no invented values. |
| RR-02 | **Fail** | Verdict "Needs clarification before development" for the well-written story, with a *Must clarify* on spaces-only names and 4+ *Should clarify* findings. Same miss as in the 2026-10-14 round. |
| RR-03 | Pass | MUST/SHOULD/MAY not flagged; findings on what "valid API key" means, Retry-After format, 401 body. |
| RR-04 | Pass | All Swedish with translated priorities, verdict, and markers; "bör" flagged with its security impact; missing login message and user data flagged; no Given/When/Then. |
| RR-05 | Partial | German review; "soll" and "kann" applied from the conventions without asking; English Given/When/Then keywords with German content; "Kunde" read as the organization. But the finding label `Missing:` stays English six times. |
| RR-06 | Pass | Conflict between story 1 and story 2 is the first *Must clarify*, with its effect on order history (story 3). |
| RR-07 | Pass | 5 *Must clarify*, 6 *Should clarify* + 1 *Consider* (7), rest summarized in one line; missing basics (scope, ordering, no-result state) flagged. |
| RR-08 | Pass | Name, email, phone, and API key not repeated; tells the user to remove them and rotate the key; reviews permissions, displayed data, and logging. |
| RR-09 | Pass | Turn 2: no integration, nothing posted, full text given to copy, tracker not guessed from the ID. |
| RR-10 | Partial | 3 vs 5 attempts flagged as *Must clarify* quoting both and naming HLR-4; missing email flagged citing HLR-4; unlock period asked. But it asks whether attempts on all devices share a counter, which HLR-4 already answers ("per account regardless of device"). |
| RR-11 | Pass | Missing PDF story reported; SHOP-101 and SHOP-102 reviewed on their own (link validity, what the export contains). |
| RR-12 | Pass | Expired/used link and password rules for step 4 flagged; proposals in the use case's numbering (4a., 4b. …); no Given/When/Then; unregistered address not asked. |
| RR-13 | Partial | Swedish review from the skill's own conventions, English quotes with Swedish translations, real gaps (expiry time zone, second code). But the label `Missing:` stays English eight times. |

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
| RR-01 | Partial | Verdict, password rules and link validity flagged, plain-sentence proposals with markers. The unregistered email and "user-friendly error handling" are not findings (only mentioned in the summary). |
| RR-02 | Pass | Ready after minor clarifications; two useful findings (character set, spaces-only name). (Failed on Haiku.) |
| RR-03 | Pass | RFC 2119 respected; finding on what a valid API key is; MAY not flagged as unclear. |
| RR-04 | Partial | Swedish throughout, both "bör" flagged. The missing "what happens to the user's data" and "what the user sees when logging in" are not flagged. |
| RR-05 | Pass | German, soll/kann per conventions, English Gherkin keywords, Kunde vs Nutzer applied. No English `Missing:` label (Haiku partial). |
| RR-06 | Partial | Conflict between story 1 and 2 as Must clarify. Does not ask how guest orders relate to order history. |
| RR-07 | Pass | 1 Must and 2 Should, remaining vague phrases summarized in one line, missing basics named. |
| RR-08 | Partial | Nothing repeated; says to remove personal data and the credential. Does not review permissions, what staff may see, or logging. |
| RR-09 | Pass | Says it cannot post; review given again as copy-paste text. |
| RR-10 | Partial | 3 vs 5 contradiction quoted with HLR-4; missing email notification flagged. Turns HLR-4's "appropriate period" into a finding and does not ask about "Try again later". |
| RR-11 | Pass | PDF export missing; contents and failure behavior asked; proposals labelled. |
| RR-12 | Pass | Invalid or expired link and password policy flagged; proposals as 3a/4a/5a; 2a not flagged. |
| RR-13 | Pass | Swedish review with `Saknas:` and `[ATT KLARGÖRA: …]`, English quoted with translations. No English label (Haiku partial). |

Result: 8 pass, 5 partial, 0 fail.

## General rewrite on GPT-6.1-Sol (medium), recorded 2026-10-16

A light rewrite: rules 1, 2, 6, and 8 now say why they matter; nothing was
removed (the skill had no scenario-specific patches worth folding in).
2,388 → 2,434 words. Gate model GPT-6.1-Sol, medium effort, `run_codex.py`,
RR-01–RR-13 and held-out HO-04, HO-05, HO-65–HO-75, 2 runs per version.
Checked with `check_review_requirements.py`, `grade_objective.py`, and
reading. Folders `tests/observations/codex-sol61-medium-rr-*-2026-10-16`.

| Version | Runs | Result |
|---------|------|--------|
| Before (`971c369`) | 2 × 26 | All pass, except RR-07 run 1: minor vague phrases dropped without the summary line |
| Draft | 2 × 26, RR-07 × 3 more | All pass, except RR-07: same miss in 2 of 5 |

RR-07 misses on both versions and touches no changed text. RR-10 run 1
was flagged by the checker only because it wrote "five" in words.
