# Example: test-data

Sign-up form data for three countries, with a length limit and an age limit.

## What the user typed

```text
$test-data I need test data for our sign-up form, for Sweden, Germany and
the UK. Fields: full name (1–50 characters), email, date of birth (must be
18 or older), country, mobile number.
```

## What came back

> Real output, unedited except that Codex's one-line opening note is left out.

---

Here’s a draft covering all three markets, name boundaries, and the age cutoff. No team conventions were found; I used the skill defaults. All names are fictional.

**Baseline records**

`TEST-` in `email` identifies the records without affecting name lengths. Sweden and Germany need documented test mobiles before these can become complete valid submissions.

| Purpose | full name | email | date of birth | country | mobile number |
|---|---|---|---|---|---|
| Sweden; accented characters | Åsa Lindström | TEST-se01@example.com | 1990-04-12 | Sweden | [TO CLARIFY: Swedish test mobile] |
| Germany; accented characters | Deniz Weiß | TEST-de01@example.com | 1992-08-23 | Germany | [TO CLARIFY: German test mobile] |
| UK; hyphen and apostrophe | Amira-Jane O’Connell | TEST-uk01@example.com | 1994-11-05 | United Kingdom | +447700900001 |

**Boundary and invalid-input cases**

For each row, copy the UK baseline and replace the indicated field. Use a distinct email such as `TEST-b01@example.com` matching the case ID, except when testing email itself. Reusing the baseline mobile is intentional; run these as independent tests.

Let **T** be the test date and **C = T minus 18 calendar years**.

| Case | Field | Replacement value | Purpose |
|---|---|---|---|
| B01 | full name | `""` (empty string) | 0 characters; outside allowed range |
| B02 | full name | `A` | 1 character; minimum |
| B03 | full name | `Al` | 2 characters; just inside minimum |
| B04 | full name | `AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghi` | 49 characters |
| B05 | full name | `AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghij` | 50 characters; maximum |
| B06 | full name | `AbcdefghijAbcdefghijAbcdefghijAbcdefghijAbcdefghijA` | 51 characters; outside allowed range |
| B07 | date of birth | C minus 1 day | Turned 18 yesterday; meets age rule |
| B08 | date of birth | C | Turns 18 today; meets age rule |
| B09 | date of birth | C plus 1 day | Turns 18 tomorrow; outside allowed age range |
| B10 | date of birth | `2000-02-30` | Impossible calendar date |
| B11 | email | `TEST-b11.example.invalid` | Missing `@`; format-only invalid value |
| B12 | mobile number | `+440` | Too short; format-only invalid value |

On reference date **2026-10-19**, B07–B09 are respectively `2008-10-18`, `2008-10-19`, and `2008-10-20`. **Recalculate them for each test run.**

**Sources of special values:** `example.com` and `.invalid` are reserved by RFC 2606/RFC 6761. The UK mobile comes from Ofcom’s drama range `07700 900000–07700 900999`; it cannot receive verification SMS. No Swedish or German mobile numbers were invented.

**Assumptions:** dates use `YYYY-MM-DD`, countries use English display names, and mobile numbers use international notation. Character handling beyond the stated name length is unspecified.

**Open questions**

1. [TO CLARIFY: documented Swedish and German test mobiles] Which approved test numbers should these records use?
2. [TO CLARIFY: validation contract] What required-field, name-character, email, country-value, and mobile-format rules apply?
3. [TO CLARIFY: failure handling and age calculation] What should happen for invalid inputs, and which timezone and leap-day policy determine age?

The tables are ready to copy; CSV or JSON text is also possible. Would you like a draft of the stated markets and form constraints for `.qa-toolkit/conventions.md`?

---

## What to notice

- Email addresses use `example.com`, a domain reserved for documentation, and the UK mobile comes from Ofcom's range for drama, with the source named. The skill knows no documented range for Swedish or German mobiles, so it asks for approved test numbers instead of making up numbers that might reach a real person.
- Boundaries at 0, 1, 2, 49, 50, and 51 characters and around the 18th birthday. The dates are given as a rule (test date minus 18 years) and worked out for a reference date, with a note to recalculate them for each run.
- The `TEST-` marker sits in the email, so the names keep their exact lengths, and the names are labeled fictional.
- Rules the requirement does not give (validation, error handling, the time zone of the age check) are open questions, not guesses.

## Without the skill

The same model with no skill installed also produced usable data for this request: `example.com` emails, a UK number from the Ofcom range, names of 1 and 50 characters, and a birth date exactly 18 years before the day of the run. The differences are smaller than in other scenarios: the age boundary is fixed to that day with no note to recalculate it, the Swedish and German mobile numbers are called "format examples" without saying where they come from, and there are no open questions.

The difference shows when the request pushes toward real data. Asked for "10 customer emails … gmail and hotmail addresses so they look real" (scenario HO-64), the model without the skill wrote ten addresses such as `emily.carter.test4821@gmail.com`, any of which could belong to someone. With the skill it said why it would not, and used reserved domains instead.

<sub>Codex, gpt-6.1-sol, reasoning effort medium, 2026-10-19 (scenario TD-01, run 1 of the full test run on the released 0.3.0 skills). Without the skill: the full run with no skill installed, same model and effort, 2026-10-20.</sub>
