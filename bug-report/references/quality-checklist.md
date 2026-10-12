# Defect report quality checklist

Use this when finishing a new report (Step 5) and when reviewing an existing
one (Review mode). Items are in order of importance.

## Must have

A report missing any of these is not ready to submit.

- [ ] **Actual result is concrete.** Describes what was observed, not a
      judgment. Includes exact error text if there was one.
      - Weak: "The page doesn't work."
      - Strong: "The page stays blank and the browser console shows
        `TypeError: items is undefined`."
- [ ] **Expected result is stated.** It is clear what should have happened.
      - Weak: (missing, or "it should work")
      - Strong: "The order list should show my three recent orders."
- [ ] **Steps can be followed by someone else.** Numbered, start from a known
      state, one action per step, no skipped steps.
- [ ] **Single defect.** The report describes one problem. Several problems
      should be split into separate reports.
- [ ] **No invented information.** Every fact comes from the user, an
      attachment, or evidence that was actually collected. Unknowns are marked
      `Unknown`. Nothing is inferred and stated as fact (prices from totals,
      frequency from wording, language or country from file paths).
- [ ] **Sensitive data matches the chosen mode.** With Redact (the
      default), credentials, personal data, and customer data are masked
      everywhere. With an explicit Preserve choice, only personal or customer
      data the report needs is kept; credentials are masked. With an
      explicit Include all choice, supplied values are kept. Kept values
      appear only in the report, and the reply lists them by type and
      location. Notes about masking name types and locations, never values.
- [ ] **No false claims about actions.** The reply does not say you checked,
      looked at, or found anything you did not actually check in this
      session.

## Should have

- [ ] **Specific title.** Says where, what goes wrong, and under what
      condition. Someone scanning a list of issues can tell them apart.
- [ ] **Environment.** Version or build and platform are given, or marked
      `Unknown`.
- [ ] **Reproducibility.** States whether it happens always, sometimes, or once.
- [ ] **Severity with a reason.** Uses the scale in `template.md` and explains
      the impact in one sentence.
- [ ] **Evidence attached or referenced** when available (screenshot, log
      excerpt, recording). Files that must be attached by hand are named.
- [ ] **Original text preserved.** Error messages and UI labels are quoted
      exactly as shown, except for required masking of sensitive values.
      Search terms, entered values, and product names keep their supplied
      spelling and case, untranslated and unpluralized. Any translation is
      separate from the original quote.
- [ ] **Unambiguous dates and times.** `YYYY-MM-DD`, with time zone for times.

## Nice to have

- [ ] Workaround, if one is known.
- [ ] When the problem started or what changed recently.
- [ ] Links to related or possibly duplicate issues.

## Common problems to flag in review

| Problem | Why it matters | Suggestion |
|---------|----------------|------------|
| Vague words: "broken", "weird", "doesn't work" | The developer cannot tell what to look for | Describe what was seen on screen |
| Cause stated as fact: "the database is down" | Can send the developer in the wrong direction | Report the symptom; move the theory to *Additional notes* as a hypothesis |
| Steps start mid-flow: "click Save" | Cannot be reproduced from scratch | Add the starting state and the steps before |
| Fields filled with "N/A" or "see above" | Noise that hides real information | Remove the field or provide the information |
| Emotional or blaming language | Distracts from the facts | Keep to neutral, factual wording |
| Several issues in one report | Hard to track, fix, and close | Split into one report per defect |
