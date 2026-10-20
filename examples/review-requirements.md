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

> Real output, unedited except that Codex's one-line opening note is left out and its headings are shifted down two levels to fit this page.

---

### Requirements review: Password reset

**Verdict:** Needs clarification before development

**Summary:** The customer’s goal is clear, but the reset flow and acceptance criteria leave essential behavior undecided. Different implementations could satisfy the wording while producing different customer experiences.

No team conventions were found; this review uses the skill defaults.

#### Must clarify

1. **Missing: the reset flow and successful outcome.**  
   The story does not define how the customer requests a reset or what happens after submitting a valid new password, so the complete success path cannot be tested.  
   **Question:** What customer-visible sequence should take the customer from requesting a reset to accessing their account?

2. **“The user should receive an email quickly.” / “The reset link should be valid for a reasonable time.” / “The new password must be secure.” / “Error handling should be user-friendly.”**  
   These criteria lack objective acceptance rules, so testers cannot determine whether delivery time, link validity, password validation, or error handling passes.  
   **Question:** What acceptance specification should govern these four criteria, including which outcomes are mandatory?

3. **Missing: reset-link lifecycle rules.**  
   Expiry is implied, but the effect of using a link or requesting another reset is undefined, leaving acceptance of previously issued links undecidable.  
   **Question:** What policy determines whether an issued reset link remains usable after expiry, successful use, or a subsequent reset request?

#### Proposed acceptance criteria

Proposals only: the team can accept, change, or reject these. Markers identify unresolved decisions.

- When a customer submits `[TO CLARIFY: required account-identifying input]` through `[TO CLARIFY: reset entry point]`, the system displays `[TO CLARIFY: request confirmation]`.
- When an eligible reset request is submitted, the reset email reaches `[TO CLARIFY: delivery measurement endpoint]` within `[TO CLARIFY: maximum duration, starting event, and test conditions]`.
- When an unused reset link is opened before `[TO CLARIFY: validity duration measured from the agreed starting event]`, the customer can enter a new password.
- When a link is opened exactly at or after its expiry boundary, the system produces `[TO CLARIFY: boundary behavior and recovery guidance]`.
- When a customer submits a password meeting `[TO CLARIFY: password policy]` through an accepted reset link, the system confirms the password change.
- After a successful reset, signing in with the new password grants access to the account.
- After a successful reset, signing in with the previous password produces `[TO CLARIFY: expected outcome]`.
- When a submitted password violates the agreed policy, the system displays `[TO CLARIFY: actionable validation feedback]`.
- When the submitted account identifier is unregistered, the system displays `[TO CLARIFY: response that follows the agreed account-privacy policy]`.
- When email delivery fails, the system displays `[TO CLARIFY: observable failure or recovery behavior]`.
- When a previously used or superseded link is opened, the system produces `[TO CLARIFY: outcome under the agreed link lifecycle policy]`.

#### Assumptions made in this review

- The story and its four criteria are the entire item under review; no parent requirements or existing policies were supplied.
- The draft interprets “access my account” as successful sign-in after resetting the password; this remains subject to confirmation.

This review is ready to copy into your requirement or tracker.

---

## What to notice

- Every finding quotes the exact words it is about, or says what is missing, and ends in a question the product owner can answer. The four vague criteria share one question instead of four.
- The proposed acceptance criteria are labeled as proposals, and every value the team has not decided is a `[TO CLARIFY: …]` marker. No "24 hours" or "12 characters" appears out of nowhere.
- It covers what the story left out: whether the old password still works, what happens to used or replaced links, and what to show for an unregistered address, left to the team's account-privacy policy.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-19 (scenario RR-01, run 1 of the full test run on the released 0.3.0 skills).</sub>
