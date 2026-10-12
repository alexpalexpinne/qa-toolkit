# Requirements review checklist

Go through every area. Most requirements will only have findings in a few of
them. Do not report an area just because it is not mentioned: report it when
its absence matters for this requirement.

## 1. Clarity

- Is every criterion specific enough that two people would test it the same
  way?
- Are there vague words? See `ambiguity-patterns.md`.
- Are domain terms used consistently? (The same thing should not be called
  "customer", "client", and "account" in different places.)
- Is it clear which criteria are required and which are optional? Follow the
  *Obligation words* method in `ambiguity-patterns.md`.
- Are abbreviations and domain terms defined or commonly understood by the
  team?

## 2. Testability

- Does each criterion describe an **observable** result: something visible
  on screen, in data, in a message, or in a log?
- Can a pass/fail decision be made without asking someone?
- Are measurable qualities given numbers? ("Loads quickly" → "loads within
  `<n>` seconds on `<conditions>`")

## 3. Completeness

| Area | Questions to ask |
|------|------------------|
| **Users and permissions** | Who can do this? What happens for users who are not allowed? |
| **Inputs** | What are valid values, formats, lengths, ranges? Which fields are required? |
| **Boundaries** | What happens at minimum, maximum, empty, zero, and just outside the limits? |
| **Errors** | What does the user see when input is invalid, a service is down, or a timeout occurs? |
| **States** | What happens if the item is in another state (draft, locked, deleted, expired)? |
| **Data** | Where is data stored, for how long, and who can see it? What happens to existing data? |
| **Concurrency** | What if two users change the same thing at the same time? What if the user double-clicks? |
| **Integrations** | Which other systems are involved, and what happens if one of them fails? |
| **Non-functional** | Performance, security, accessibility, and privacy requirements, if relevant |
| **Locale** | Languages, date/number/currency formats, time zones, right-to-left scripts, character sets |
| **Out of scope** | Is it stated what this requirement deliberately does *not* cover? |

## 4. Consistency

- Do any criteria contradict each other?
- Does the requirement contradict existing behavior, other requirements, or
  the design (if provided)?
- In mode B (several items): do items overlap, conflict, or leave a gap
  between them? Are the same rules defined differently in different items?

## 5. Size and focus

- Does the item describe one feature, or several that should be split?
- Is the "why" (the user's goal) stated? Without it, the team cannot judge
  edge cases sensibly.
- Does it prescribe a technical solution where it should describe a need?
  (Flag gently: sometimes this is intentional.)
