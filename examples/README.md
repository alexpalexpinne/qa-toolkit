# Examples

Real outputs from test runs of the skills, one per skill, each with the
input, the output, and what to look for. Nothing here was written by hand
to look good: each page names the assistant, model, and date of the run.

| Skill | Example | What it shows |
|-------|---------|---------------|
| `review-requirements` | [Password reset story](review-requirements.md) | Vague criteria turned into concrete questions, with proposals that do not invent values |
| `test-cases` | [Restructuring a legacy test](test-cases.md) | A messy test cleaned up without guessing its missing expected results |
| `test-data` | [Sign-up form for three countries](test-data.md) | Boundaries and international names, with emails and phone numbers that cannot reach real people, and no made-up numbers where no safe range is documented |
| `test-summary` | [The "94 % pass rate" request](test-summary.md) | A headline number kept honest: what ran, what did not, and what is still unknown |
| `bug-report` | [Discount code not applied](bug-report.md) | A report a developer can act on, with only what the tester did not say asked at the end |

The runs were made in Codex with GPT-6.1-Sol (medium effort) on the
released 0.3.0 skills, on 2026-10-19 and 2026-10-20, as part of the full
test run. Each page names its scenario, which is defined in
[`tests/`](../tests/). All data in the examples is fictional.
