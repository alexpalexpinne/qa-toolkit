# Restructuring existing test cases

Rules for restructure mode (mode C), also used in review mode (mode B) to
spot problems. The goal is a test that is easier to run, review, and
maintain, while testing exactly the same thing as before.

## What is one test case?

A test case should verify one coherent behavior, rule, flow, or risk. It
normally has:

- one purpose
- one main trigger or flow
- one kind of expected outcome
- one clear reason to fail
- one execution context

Several steps are fine when they are needed to complete the same flow. Do
not treat each step as a separate test.

**Keep as one** when:

- One transaction runs from one trigger, through a fixed sequence, to one
  final outcome, even if it passes through several systems, services, or
  teams. Use checkpoints at important boundaries so a failure can be
  located, instead of splitting the test.
- A second way of reaching the same function (another menu, a shortcut) uses
  the same data and context and has no separate outcome. Mention it in the
  purpose rather than making a test that only proves a screen can be opened.

**Consider split** when:

- The test combines independent scenarios or variants that could each pass
  or fail on their own.
- Different business rules or outcome categories are mixed together.
- The same setup–action–result pattern repeats with meaningfully different
  conditions (for example different customer types or payment methods that
  follow different rules).
- A failure in one part has nothing to do with the rest of the test.

Variants that follow different rules or start from different states stay
separate, even if the screens look the same.

**Never split a test case yourself** unless the user explicitly asks.
Splitting affects execution history, coverage reports, ownership, and
attachments. Recommend it, and explain which steps would form which tests
and why they fail independently.

## Where content belongs

| Field | Contains | Does not contain |
|-------|----------|------------------|
| **Title** | Feature or process – scenario or condition – expected outcome | Step details, test data |
| **Purpose** | What the test proves, in one or two sentences | Parameters, scripts, long data |
| **Preconditions** | Required state before the test: environment, configuration, existing data, statuses, users and permissions, running services or jobs | Actions the tester performs |
| **Test data** (case level) | Values used across the test | Instructions |
| **Step action** | One instruction, starting with a verb | Expected results, long setup, scripts or parameters |
| **Step data** | Input values for this step: parameters, IDs, dates, paths, file names, scripts | Instructions, expected results, reviewer notes |
| **Step expected result** | What must be observably true after the action | Instructions, notes |
| **Notes** (case level) | Background, caveats, known limitations, references | Open questions (those go in *Open questions*) |

### Actions

- One executable instruction, starting with a verb: *Open*, *Select*,
  *Enter*, *Run*, *Upload*, *Check*.
- Use the exact label of a button or field when the source gives it, in
  quotes: `Select 'Confirm'.`
- Describe the interaction itself: `Select 'Confirm'.`, not `Confirm that
  the order should be cancelled.`
- A short sequence may stay in one step when the intermediate actions have
  no result of their own, for example entering a search term and selecting
  `'Search'`. Otherwise give each action its own step and result.
- Remove labels like `Step 1:`, `Description:`, `Expected:`.

### Step data

- Prefer `key: value` lines:
  ```text
  Job: nightly-order-export
  Order status before run: PAID
  Export date: <CURRENT_DATE>
  ```
- Leave it empty when the step has no input values. Do not repeat a value
  that is already explicit in the action.
- Keep stable starting state (environment, access, configuration) in
  preconditions, not in every step.
- State the scenario once, in the title, purpose, preconditions, or first
  step. Do not repeat the same scenario label in every step's data.
- Never write vague filler such as "valid test data" or "applicable
  environment". If a concrete value is missing, use `[TO CLARIFY: …]`.

### Expected results

- Observable: what is shown, stored, sent, changed, or blocked.
- Use bullets when there are several outcomes.
- If the source has no expected result for a step:
  - If outcome text is hidden in the action or data, move it to the
    expected result.
  - Otherwise write `[TO CLARIFY: expected result missing in the original
    test]` and mark the test *Blocked: pending clarification*.

## Steps: merging, splitting, and traceability

The number of steps may change. What must not change is traceability,
execution order, and the link between each action and its result.

- **Every new step names its original step or steps**, for example
  `(from original step 3)` or `(from original steps 4–5)`.
- **Merge** an original step that contains only an expected result, only
  setup, or only a note into the step it belongs to, when the relationship
  is clear. Setup usually moves to preconditions; notes to case-level notes.
- **Split** a step with several independent actions only when:
  - it has no attachments,
  - each new step can get its own clear expected result, and
  - the execution order stays the same.
- **When in doubt, keep the step as it is** and add an open question.
- Resolve the structure in the draft. Do not leave notes like "reviewer
  should merge this later" unless the mapping is genuinely unclear.

## Exact technical content

If the source contains a script, command, query, message payload,
configuration block, request or response example, or file content:

- Keep it exactly as it is: no reformatting, correcting, shortening, or
  generalizing.
- Place it in step data. If it is too long to review there, you may
  suggest moving it to an attachment: label it as a *suggested
  attachment*, include only the exact content, keep it on the step that
  uses it, and say that it is not a real attachment in the team's tool
  until a person approves it.
- You may summarize *what it does* in the action, but the exact content must
  stay intact.
- Sensitive values are an exception: mask them as required by core rule 5,
  preserve the remaining text exactly, and describe the redaction by type
  only. If a runnable value was removed, mark the case *Blocked: pending
  clarification* and ask for safe replacement data. Never reproduce a
  sensitive value to keep a step unchanged.

## Attachments

Attachments are evidence or execution context.

- Keep test-level attachments at test level and step-level attachments on
  their step.
- Never delete, rename, or move attachments.
- An attachment named in the source (for example `[Attachment:
  invoice-reference.pdf]`) exists in the team's tool. Keep the reference;
  do not ask the user to supply the file, and do not block the test because
  you cannot see it.
- Never split, merge, reorder, or delete a step that has attachments
  automatically. If such a step contains several actions or checks that
  you would otherwise split, leave it as it is and add an open question
  saying that splitting it is a decision for a person, because of the
  attachment.
- One exception: a step that contains only an expected result may be
  merged into the step with the attachment that it belongs to. The
  attachment stays on that step, the step's action is not changed, and the
  change summary says so.

## Consistency with related test cases

When test cases from the same suite, folder, or test set are provided, check
whether the restructured test follows their pattern for:

- title naming, terminology, and abbreviations
- placeholder names
- preconditions wording
- level of detail in expected results
- size of the test
- overlap or duplication with neighbouring tests

Follow the group's pattern where it does not change meaning. If no related
tests were provided, state that consistency was not checked.

## Common problems to look for

- Missing expected result
- Vague expected result: "successful", "works", "as expected", "OK"
- Expected result hidden in the action
- Test data or preconditions hidden in the action
- Several independent actions in one step
- Labels such as `Step 1:` or `Expected:` inside the text
- Notes mixed into expected results
- A test that depends on another test having run first
- Several independent scenarios in one test
- Setup or reference material written as executable steps

## Checklist for a restructured test

- [ ] It tests the same thing as before: no expected result added, removed,
      or changed in meaning.
- [ ] Every new step names its original step or steps, and the order is
      unchanged.
- [ ] IDs, technical identifiers, and exact technical content are unchanged.
- [ ] Attachments are where they were, and steps with attachments were not
      split, merged, reordered, or deleted.
- [ ] Content is in the right fields (see *Where content belongs*).
- [ ] Missing information is marked `[TO CLARIFY: …]`, never filled with
      vague filler.
- [ ] The scope recommendation and change summary are included.
- [ ] Consistency with related tests is described, or stated as not checked.

## Example

**Original test (from a test management tool):**

```text
ORD-214  Export
Step 1: Make sure the export job is not running and there are paid orders.
        Run nightly-order-export for today. Orders should be exported.
Step 2: Expected: file is created in /data/export
Step 3: Check the database
```

**Restructured:**

```markdown
### ORD-214: Order export – nightly export of paid orders – export file created

**Purpose:** Verifies that the nightly export job exports paid orders to a file.
**Status:** Blocked: pending clarification (open question 1)
**Preconditions:** (from original step 1)
- The job `nightly-order-export` is not running.
- At least one order has the status paid.

| # | Action | Data | Expected result | Original step |
|---|--------|------|-----------------|---------------|
| 1 | Run the export job. | Job: `nightly-order-export`<br>Export date: today | • Orders are exported.<br>• A file is created in `/data/export`. | 1, 2 |
| 2 | Check the database. | – | [TO CLARIFY: expected result missing in the original test] | 3 |

**Scope:** Scope OK. One job, one flow, one outcome.

**Change summary:**
- Moved the starting conditions from step 1 to preconditions.
- Merged original step 2, which only contained an expected result, into
  step 1.
- Kept "Orders are exported" as written; it is vague but it is the original
  expected result.

**Open questions:**
1. Original step 3: what should the database show, and in which table?
2. "Orders are exported": which orders (all paid orders, or only today's),
   and what does the file contain?

Consistency with related tests: not checked; no related tests provided.
```
