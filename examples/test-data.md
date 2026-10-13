# Example: test-data

Sign-up form data for three countries, with a length limit and an age limit.

## What the user typed

```text
$test-data I need test data for our sign-up form, for Sweden, Germany and
the UK. Fields: full name (1–50 characters), email, date of birth (must be
18 or older), country, mobile number.
```

## What came back

> Real output, unedited except that its headings are shifted down two levels to fit this page.

---

Here is a safe, copy-pasteable set. The `test.signup` email prefix is the cleanup marker. Dates use `YYYY-MM-DD`; reference date is **2026-10-13**.

| Purpose | full name | email | date of birth | country | mobile number |
|---|---|---|---|---|---|
| Valid typical; Swedish character | `Åsa Solvind` | `test.signup.se.asa@example.org` | `1989-04-21` | `Sweden` | `+46701740635` |
| Valid typical; German diacritic | `Mila Kovačević` | `test.signup.de.mila@example.org` | `1994-09-08` | `Germany` | `+4915228817386` |
| Valid typical; apostrophe | `Rhys O'Harper` | `test.signup.uk.rhys@example.org` | `2000-12-31` | `United Kingdom` | `+447700900000` |
| Full name empty, 0 characters — outside range; [TO CLARIFY: handling/message] | `""` | `test.signup.name-empty@example.org` | `1990-03-10` | `Sweden` | `+46701740636` |
| Full name minimum, 1 character | `A` | `test.signup.name-min@example.org` | `1990-03-11` | `Sweden` | `+46701740637` |
| Full name maximum, 50 characters | `Alexandra Elisabeth Kovačević van Linden-Sundström` | `test.signup.name-max@example.org` | `1982-01-12` | `Germany` | `+491713920001` |
| Full name 51 characters — outside range; [TO CLARIFY: handling/message] | `Alexandra Elisabeth Kovačević van Linden-Sundströms` | `test.signup.name-over@example.org` | `1982-01-13` | `United Kingdom` | `+447700900001` |
| Exactly 18 years old on reference date | `Linnea Varg` | `test.signup.age-exact18@example.org` | `2008-10-13` | `Sweden` | `+46701740638` |
| Just inside age limit, 18 years + 1 day | `Emre Sommer` | `test.signup.age-inside@example.org` | `2008-10-12` | `Germany` | `+491713920002` |
| Just outside age limit, 17 years 364 days — [TO CLARIFY: handling/message] | `Sana Mercer` | `test.signup.age-under18@example.org` | `2008-10-14` | `United Kingdom` | `+447700900002` |
| Email format probe, missing `@` — [TO CLARIFY: validation/handling] | `Nora Faye` | `test.signup.invalid-email.example.org` | `1987-02-14` | `Germany` | `+4915228895456` |
| Mobile format probe, contains a letter — [TO CLARIFY: validation/handling] | `Jonas Vale` | `test.signup.mobile-format@example.org` | `1988-05-05` | `Sweden` | `+4670174063X` |

Special values are fictional/reserved: `example.org` is a documentation domain; Swedish numbers come from [PTS](https://www.pts.se/internet-och-telefoni/telefonnummer-och-adressering/telefonnummer-till-bocker-och-filmer/), German numbers from the [Bundesnetzagentur](https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Nummerierung/DramaNumbers/artikel.html), and UK numbers from [Ofcom](https://www.ofcom.org.uk/phones-and-broadband/phone-numbers/numbers-for-drama).

Assumptions: mobile numbers use E.164 format, and the country value is `United Kingdom` rather than `UK`. These numbers cannot receive SMS; use team/provider sandbox numbers for OTP tests.

---

## What to notice

- Email addresses use `example.org`, a domain reserved for documentation, and every phone number comes from a range the national regulator sets aside for films and books, with the source linked. None of it can reach a real person.
- Boundaries at 0, 1, 50, and 51 characters and around the 18th birthday, with the reference date stated so the ages can be recalculated.
- How the form should react to invalid values is marked `[TO CLARIFY: …]`, because the requirement does not say.

<sub>Codex, gpt-5.6-luna, reasoning effort max, 2026-10-13 (scenario TD-01). The skills have changed since some of these runs, so current output may differ in detail.</sub>
