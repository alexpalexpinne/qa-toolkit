# Example: review-requirements

A password-reset story with four acceptance criteria that sound fine until someone has to test them.

## What the user typed

```text
$review-requirements
As a customer I want to reset my password so that I can access my account
if I forget it.

Acceptance criteria:
- The user should receive an email quickly.
- The reset link should be valid for a reasonable time.
- The new password must be secure.
- Error handling should be user-friendly.
```

## What came back

> Real output, unedited except that its headings are shifted down two levels to fit this page.

---

### Requirements review: Password reset

**Verdict:** Needs clarification before development  
**Summary:** The customer’s goal is clear, but the main flow and acceptance thresholds need definition before the team can make consistent pass/fail decisions.

#### Must clarify

1. **Missing: how the customer requests and completes a reset.**  
   The account-identifying input, email destination and successful end state are unspecified, preventing an end-to-end acceptance test.  
   **Question:** What must the customer enter, which email address receives the link, and what should happen after the new password is accepted?

2. **“The user should receive an email quickly.”**  
   Without a measurable delivery target, testers cannot decide whether the timing passes.  
   **Question:** What is the maximum delay, measured from which event to which delivery point, and under what test conditions?

3. **“The reset link should be valid for a reasonable time.”**  
   The validity period and its boundaries are undefined, so link-expiry behavior cannot be accepted consistently.  
   **Question:** How long is the link valid, when does that period start, and is the link accepted exactly at the expiry time?

4. **“The new password must be secure.”**  
   No password policy defines which passwords must be accepted or rejected.  
   **Question:** Which password policy applies, including length limits and rules for allowed or rejected passwords?

5. **“Error handling should be user-friendly.”**  
   Neither the required failure cases nor their observable responses are defined, preventing acceptance of error handling.  
   **Question:** Which failures must be covered—for example invalid input, expired links or email delivery failure—and what message and recovery action are required for each?

#### Should clarify

1. **Missing: link reuse and repeated reset requests.**  
   The expected behavior of previously used links and earlier links is unspecified.  
   **Question:** Can a link be used again after a successful reset, and does requesting another link invalidate earlier links?

2. **Missing: requests that do not match an account.**  
   The response and whether it may reveal account existence are undefined.  
   **Question:** What should the requester see when the supplied details match no account, and may that response reveal whether an account exists?

3. **“should” and “must”**  
   Different obligation words leave the required status of the criteria unclear.  
   **Question:** Must all four criteria pass for acceptance, or are the criteria using “should” recommendations?

#### Proposed acceptance criteria

Proposals only: the team decides. Clarification markers identify unresolved decisions.

- When a customer submits `[TO CLARIFY: required account-identifying input]` matching an account, a reset email reaches `[TO CLARIFY: recipient and delivery measurement point]` within `[TO CLARIFY: maximum delay]` of `[TO CLARIFY: start event]`, under `[TO CLARIFY: test conditions]`.
- When a customer opens a reset link within `[TO CLARIFY: validity period, start event and exact expiry boundary]`, the password-entry form is displayed.
- When an expired or invalid reset link is opened, the page displays `[TO CLARIFY: message and recovery action for each case]`.
- When a password meeting `[TO CLARIFY: password policy, including boundary values]` is submitted through a valid reset link, the customer can sign in with that password.
- When a submitted password fails `[TO CLARIFY: password policy]`, the form displays `[TO CLARIFY: validation message and correction guidance]`.
- When a reset request matches no account, the requester sees `[TO CLARIFY: agreed response and account-disclosure behavior]`.
- When email delivery fails, the requester sees `[TO CLARIFY: notification and recovery action]`.

#### Assumptions made in this review

- This story was reviewed on its own; no parent requirement, design or existing password policy was supplied.
- All four bullets were reviewed as intended acceptance conditions; their required status remains to be confirmed.

You can copy this review directly; I can also save it as Markdown. After clarification, the next step is to derive test cases from the agreed criteria.

---

## What to notice

- Every finding quotes the exact words it is about, or says what is missing, and ends in a question the product owner can answer.
- The proposed acceptance criteria are labeled as proposals, and every value the team has not decided is a `[TO CLARIFY: …]` marker. No "24 hours" or "12 characters" appears out of nowhere.
- It spots the missing account-enumeration decision (what to show when no account matches), a classic security gap in reset flows.

<sub>Codex, gpt-6.1-sol, reasoning effort xhigh, 2026-10-13 (scenario RR-01). The skills have changed since some of these runs, so current output may differ in detail.</sub>
