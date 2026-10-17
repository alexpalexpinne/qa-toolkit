# Default test case format

Teams can replace this format through `team-conventions.md`. Headings are
shown in English; translate them into the output language, keeping the
structure.

## Step-table format (default)

```markdown
### TC-<number>: <feature or process> – <scenario or condition> – <expected outcome>

**Purpose:** <what the test proves, in one or two sentences>
**Priority:** High / Medium / Low
**Covers:** <acceptance criterion or requirement ID>
**Status:** Ready / Blocked: pending clarification (open question <n>)
**Preconditions:**
- <known starting state, as described in the requirement>

**Test data:**
- <fake values used across the test>

| # | Action | Data | Expected result |
|---|--------|------|-----------------|
| 1 | <one action> | <input values for this step, or empty> | <observable result, or "–" if nothing to check yet> |
| 2 | ... | ... | ... |
```

Leave out the *Data* column if no step needs input values. When
restructuring existing tests, add an *Original step* column.

### Placeholders

| Form | Meaning | Example |
|------|---------|---------|
| `[TO CLARIFY: …]` | Unknown; a person must provide it | `[TO CLARIFY: expected result]` |
| `{{…}}` | Chosen by the tester when running the test | `{{order number}}` |
| The team's own, e.g. `<ENV>` | Technical placeholder already in use | Keep exactly as it is |

## Data-driven format

Use when several cases differ only in input data.

```markdown
### TC-<number>: <feature> – <field> at boundaries – <outcome>

**Purpose:** <what the test proves>
**Priority:** Medium
**Covers:** <criterion>
**Status:** Ready / Blocked: pending clarification (open question <n>)
**Preconditions:** <...>

| # | Action | Expected result |
|---|--------|-----------------|
| 1 | Enter `<value>` in <field> | – |
| 2 | <submit action named in the requirement> | See table |

| Value | Why | Expected result |
|-------|-----|-----------------|
| (empty) | Below minimum | Error "<message from requirement>" |
| `A` (1 character) | Minimum | Saved |
| 50 characters | Maximum | Saved |
| 51 characters | Above maximum | Error "<message from requirement>" |
```

## Given/When/Then format

Use when the user or team prefers it.

```markdown
### TC-<number>: <feature or process> – <scenario or condition> – <expected outcome>

**Purpose:** <what the test proves, in one or two sentences>
**Priority:** High / Medium / Low
**Covers:** <criterion>
**Status:** Ready / Blocked: pending clarification (open question <n>)
**Test data:**
- <fake values used across the test>

Given <starting state: the preconditions>
And <more context>
When <one action>
Then <observable result>
And <more observable results>
```

## Report sections after the test cases

```markdown
## Coverage summary

| Criterion | Test cases | Status |
|-----------|------------|--------|
| AC1 | TC-1, TC-2 | Covered |
| AC2 | TC-3, TC-4 | Partly covered: TC-4 blocked (open question 1) |
| AC3 | TC-5 | Blocked: pending clarification (open question 2) |
| AC4 | – | Not covered: <reason> |

*Covered* means every part of the criterion (each condition, limit, and
outcome it states) has a case, and every case for it is *Ready*. If a
part has no case, the criterion is *Partly covered*; name the missing part.
A blocked case exists but cannot decide pass or fail, so it does not count
as coverage.

## Open questions
1. <each `[TO CLARIFY: …]` marker or assumption, and who could answer it>

## Further test ideas
- <condition left out because of the limit>
```

## Example

Every detail in the test cases below (the profile page, *Save*, the message,
what happens on success) comes from this requirement:

> AC1. Given I am logged in and on my profile page, when I enter a new
> display name of 1–50 characters and select *Save*, then the new name is
> shown on my profile.
>
> AC2. Given I enter an empty name or more than 50 characters, when I select
> *Save*, then the name is not saved and the message "Display name must be
> 1–50 characters" is shown under the field.

```markdown
### TC-3: Profile – display name at length boundaries – saved or rejected

**Purpose:** Verifies that display names of 1–50 characters are saved and
that empty or longer names are rejected with the required message.
**Priority:** Medium
**Covers:** AC1, AC2
**Status:** Ready
**Preconditions:** Logged in, on the profile page.

| # | Action | Expected result |
|---|--------|-----------------|
| 1 | Enter the value from the table below in *Display name* | – |
| 2 | Select *Save* | See table |

| Value | Why | Expected result |
|-------|-----|-----------------|
| (empty) | Below minimum | Not saved; message "Display name must be 1–50 characters" under the field |
| `A` | Minimum (1) | New name shown on profile |
| 50 × `a` | Maximum (50) | New name shown on profile |
| 51 × `a` | Above maximum (51) | Not saved; message "Display name must be 1–50 characters" under the field |

### TC-4: Profile – display name of only spaces – [TO CLARIFY: outcome]

**Purpose:** Verifies how a display name consisting only of spaces is
handled.
**Priority:** Low
**Covers:** AC2
**Status:** Blocked: pending clarification (open question 1)
**Preconditions:** Logged in, on the profile page.

| # | Action | Expected result |
|---|--------|-----------------|
| 1 | Enter three spaces in *Display name* | – |
| 2 | Select *Save* | [TO CLARIFY: expected result] |

## Open questions
1. Does a name of only spaces count as empty (AC2), or is it a valid name
   (AC1)? The requirement does not say. Product owner.
```
