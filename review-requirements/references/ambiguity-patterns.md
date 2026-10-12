# Ambiguity patterns

Wording that often hides an unanswered question. The examples are in
English; look for equivalent wording in any language.

Not every occurrence is a problem. Flag it when two reasonable people could
build or test it differently.

| Pattern | Examples | Ask |
|---------|----------|-----|
| **Unmeasured quality** | fast, quickly, responsive, efficient, scalable | "How fast, measured how, under what load?" |
| **Subjective quality** | user-friendly, intuitive, simple, clean, modern, nice | "What would a user be able to do, or see, that shows this is met?" |
| **Unclear obligation** | should, may, might, could, ideally, preferably, if possible (see *Obligation words* below) | "Is this required or optional? What happens if it is not done?" |
| **Vague frequency** | usually, normally, often, sometimes, rarely, in most cases | "What happens in the other cases?" |
| **Vague quantity** | some, several, many, few, large, small, a lot | "What is the number or the limit?" |
| **Open-ended list** | etc., and so on, such as, including, and more | "What is the complete list?" |
| **Unclear reference** | it, this, they, the data, the system, the user | "Which one exactly?" |
| **Unclear actor** | "is sent", "is updated", "will be notified" (passive voice) | "Who or what does it, and who receives it?" |
| **Unclear timing** | immediately, soon, real-time, regularly, periodically, later | "Within what time? How often?" |
| **Absolute claim** | always, never, all, every, none | "Are there really no exceptions? What about `<edge case>`?" |
| **Undefined state** | appropriate, relevant, valid, correct, proper, as needed | "What exactly counts as valid/appropriate here?" |
| **Comparison without baseline** | better, improved, faster than before, more secure | "Compared to what, and by how much?" |
| **Hidden condition** | if necessary, when applicable, where possible, as required | "When exactly is it necessary, and who decides?" |
| **Undefined error handling** | "shows an error", "handles errors gracefully", "fails safely" | "Which message, what can the user do next, and what happens to their data?" |

## Obligation words

Whether a word means "required" or "optional" depends on the language and on
the organization. A literal translation of "should" can be the mandatory
form in another language's conventions. Do not rely on a fixed word list.
Instead, in this order:

1. **Team conventions.** If `team-conventions.md` defines obligation words,
   follow it.
2. **The document's own definitions.** If the requirement or its parent
   specification defines its terms (for example "MUST, SHOULD, and MAY as
   defined in RFC 2119", or a glossary), follow those definitions and do not
   flag correctly used terms.
3. **Consistency.** If neither exists, look at how the document expresses
   obligation. Flag it when several forms are mixed without a clear
   difference (for example "must", "should", and "is expected to" for
   similar things), or when one criterion's obligation is unclear in
   context.
4. **Ask, don't guess.** If you are unsure what a word means in this
   language or organization, ask whether the item is required or optional.
   Never classify an item as optional or mandatory based on an assumption
   about the language.

## Example

> The system should quickly notify the user when their export is ready.

- **"should"** (unclear obligation): is the notification required?
- **"quickly"** (unmeasured): within how many seconds or minutes?
- **"notify"** (unclear channel): in the app, by email, push notification?
- **"the user"** (unclear reference): only the user who started the export,
  or everyone with access?
- **Missing:** what happens if the export fails?
