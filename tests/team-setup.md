# Test cases: team-setup and shared team conventions

TM-01–TM-08 test the `team-setup` skill. TM-09–TM-15 test how the five
workflow skills read `.qa-toolkit/conventions.md` and offer to create it.

Unless a scenario says otherwise, run in a new empty folder that is a git
repository (`git init`), with no `.qa-toolkit/` folder, and allow writes only
inside that folder. Check after each run whether a file was written, and
that nothing was committed.

## TM-01 Full setup in a new project

**Tests:** Steps 1–4, core rules 1, 2, 3, 7.

**Input (four turns in one session):**
```text
Turn 1: /team-setup

Turn 2: English for everything. Jira, project SHOP. Severity S1 to S4:
S1 production down, S2 major function broken, S3 workaround exists,
S4 cosmetic.

Turn 3: We use test cases and test summaries. Test cases: Given/When/Then
with English keywords, IDs like SHOP-142-TC-01. Summaries: release needs
all P1 tests run and no open S1 or S2.

Turn 4: Yes, write it.
```

**Must:**
- Turn 1: state the full path the file will get and ask at most three
  questions, starting with the *General* round.
- Turns 2–3: ask only about what is still open, at most three questions
  per reply.
- Before turn 4: show the whole file, with `## General`, `## test-cases`,
  and `## test-summary` filled in from the answers, the other sections
  empty, and no *Example* section; ask for a yes.
- Turn 4: write `.qa-toolkit/conventions.md` at the repository root, read
  it back, state its path, and say to commit it.

**Must not:**
- Write anything before turn 4.
- Commit, or write any other file.
- Add rules nobody stated (for example a priority scale or recommendation
  terms).

---

## TM-02 "Use defaults" everywhere

**Tests:** Core rule 1 (empty sections, no invented rules).

**Input (three turns in one session):**
```text
Turn 1: /team-setup

Turn 2: Use defaults for all of it.

Turn 3: Yes.
```

**Must:**
- Draft a file whose sections are all empty with the template comments, or
  say that an all-empty file changes nothing and ask whether to write it
  anyway.

**Must not:**
- Fill in example values from the template's *Example* section.

---

## TM-03 Update an existing file

**Tests:** Step 1 point 3 (update mode), core rule 2.

**Setup:** Create `.qa-toolkit/conventions.md` with a filled *General*
section (English, Jira SHOP, S1–S4) and a filled *test-data* section
(markets SE, NO; marker `TEST-`).

**Input (two turns):**
```text
Turn 1: /team-setup Add Germany to our test data markets.

Turn 2: Yes.
```

**Must:**
- Read the existing file and show only the change (markets SE, NO, DE).
- Keep every other line exactly as it was.

**Must not:**
- Ask the General questions again, or rewrite other sections.

---

## TM-04 Credentials offered for the file

**Tests:** Core rule 4.

**Input (two turns):**
```text
Turn 1: /team-setup English reports, Jira SHOP. Our shared test admin login
is qa.admin@shop.example with password Winter2026!

Turn 2: Yes, write it.
```

**Must:**
- Leave the password out of the file and say why (the file is shared).
- Record where credentials are kept only if the user says where; otherwise
  ask or leave it out.

**Must not:**
- Write or repeat the password anywhere in the reply.

---

## TM-05 No file access

**Tests:** Step 1 point 1.

**Setup:** Allow only reading (no writes anywhere).

**Input (two turns):**
```text
Turn 1: /team-setup English reports, Jira SHOP, severity Critical/High/Medium/Low.

Turn 2: Yes.
```

**Must:**
- Say that it cannot write the file.
- Give the complete file text and where it can go: `.qa-toolkit/conventions.md`
  in the project, or a shared claude.ai Project's instructions.

**Must not:**
- Claim the file was saved, or save it somewhere else.

---

## TM-06 Swedish team lead

**Tests:** Core rules 5 and 6.

**Input (two turns):**
```text
Turn 1: /team-setup Vi skriver allt på svenska. Jira-projekt KASSA.
Allvarlighetsgrad: Kritisk, Hög, Medel, Låg.

Turn 2: Ja, skriv filen.
```

**Must:**
- Talk to the user in Swedish.
- Write the rules in Swedish, but keep the headings `## General` and the
  skill section names exactly in English.

**Must not:**
- Translate the section headings.

---

## TM-07 Rules given up front

**Tests:** Step 1 (use rules from the first message), core rule 7.

**Input:**
```text
/team-setup Set us up: English everywhere, GitHub issues in
acme/webshop, severity Blocker/Major/Minor. We only use bug reports.
```

**Must:**
- Use the given rules without asking about them again.
- Ask at most three questions about what is still open for *bug-report*
  (for example required fields or sensitive-data handling), or offer to
  show the draft right away.

**Must not:**
- Ask about languages, tracker, or severity scale, which were given.
- Ask about skills the team does not use.

---

## TM-08 Not triggered without being called

**Tests:** Explicit invocation only.

**Input (without calling the skill):**
```text
Our team always writes bug reports in English. Can you help me write one?
The checkout page shows a blank screen after I pay.
```

**Must:**
- Respond normally (or with `bug-report` if the user's assistant loads it
  that way), without running team setup.

**Must not:**
- Load `team-setup` or write a conventions file.

---

## TM-09 Project file is applied

**Tests:** Workflow skills, conventions source 1.

**Setup:** `.qa-toolkit/conventions.md` at the repository root with:
```markdown
## General
- Reports are written in English.
- Severity: S1, S2, S3, S4.

## test-summary
- Exit criteria: all P1 tests run; no open S1 or S2 defects.
```

**Input:**
```text
/test-summary Completion report for release 9.0. P1: 20 planned, 18
passed, 2 not run. Open defects: PAY-12 (S2, Open).
```

**Must:**
- Say that the project's conventions file was used.
- Assess both exit criteria as not met, with figures.
- Use S1–S4.

**Must not:**
- Use Critical/High/Medium/Low, or ignore the exit criteria.

---

## TM-10 File in a parent folder

**Tests:** Lookup up to the repository root.

**Setup:** As TM-09, but start the session in a subfolder,
`releases/9.0/`, of the repository.

**Input:** Same as TM-09.

**Must:**
- Find and use the file at the repository root.

**Must not:**
- Search folders outside the repository.

---

## TM-11 Only General and the skill's own section apply

**Tests:** Section scoping.

**Setup:** `.qa-toolkit/conventions.md` with:
```markdown
## General
- Write everything in English.

## bug-report
- Always redact. Preserve and Include all are not allowed, even on request.
- Component is required.
```

**Input:**
```text
/test-data 3 customers for the sign-up form: name, email, country.
```

**Must:**
- Write in English and say the project conventions were used.

**Must not:**
- Apply the *bug-report* section's rules (for example ask for a component).

---

## TM-12 Offer after the result

**Tests:** `team-file-offer.md`, when to offer.

**Input:**
```text
/bug-report Our team files in Jira project SHOP and uses severity S1–S4.
The search page shows no results for any query on build 5.2.1, Chrome 129.
Every time. Expected: matching products.
```

**Must:**
- Write the report first, using SHOP and S1–S4.
- After the report, offer in one sentence to save the tracker and severity
  scale for the team in `.qa-toolkit/conventions.md`.

**Must not:**
- Offer before the report, or write the file without a yes.

---

## TM-13 No offer when it isn't needed

**Tests:** `team-file-offer.md`, conditions.

**Input A (conventions exist):** Setup as TM-09; input as TM-12, but with
`/test-summary` and test results instead of a bug.

**Input B (nothing team-level stated):**
```text
/test-data 5 email addresses for the sign-up form.
```

**Must:**
- Make no offer in either case.

---

## TM-14 Offer accepted

**Tests:** `team-file-offer.md`, if the user says yes.

**Input:** TM-12, then:
```text
Turn 2: Yes, draft it.

Turn 3: Yes, write it.
```

**Must:**
- Turn 2: show a draft with `## General` (and, if stated, `## bug-report`)
  containing only Jira SHOP and S1–S4, name the full path, and ask for a yes.
- Turn 3: write the file, read it back, state its path, and say to commit it.

**Must not:**
- Add rules the user did not state, or commit the file.

---

## TM-15 Project file wins over the skill's own file

**Tests:** Source order.

**Setup:** Fill `test-cases/references/team-conventions.md` in the tested
copy with "Test cases are written in German." Create
`.qa-toolkit/conventions.md` with `## General` "Test cases are written in
English."

**Input:**
```text
/test-cases Users can change their display name (1–50 characters).
```

**Must:**
- Write the test cases in English and say the project file was used.

**Must not:**
- Combine the two sources or use German.

---

## TM-16 One file across skills: a bug report, then the release summary

**Tests:** The same project file applied by two workflow skills in one
session; the summary uses the severity the bug report was filed with.

**Setup:** `.qa-toolkit/conventions.md` at the repository root with:
```markdown
## General
- Reports are written in English.
- Tracker: Jira, project SHOP. Test management: Xray.
- Severity: S1 (production down or data loss), S2 (major function broken,
  no workaround), S3 (impaired, workaround exists), S4 (cosmetic).

## bug-report
- Component is required: Checkout, Search, Account, or Admin.
- Name the Xray test the bug was found with, if any.

## test-summary
- Exit criteria for release testing: all P1 tests run; no open S1 or S2
  defects.
- Xray outcomes: PASSED → passed; FAILED, ABORTED → failed; BLOCKED →
  blocked; TODO, EXECUTING → not run.
- Recommendation terms: Go / Go with accepted risks / No-go. The release
  manager decides.
```

**Input:**
```text
Turn 1: /bug-report Checkout in the test environment, build 3.4.1, Chrome
130 on Windows 11. Logged in as the standard test user, added one item
(SKU-1001, 50.00 EUR), entered the voucher WINTER25 and pressed Apply. The
total became 25.00 EUR instead of 37.50 EUR, so the 25 % discount is
applied twice. Every time, also with SKU-2002. Found while running Xray
test SHOP-T104.

Turn 2: /test-summary Completion report for release 3.4, build 3.4.1,
data as of 2026-10-21. Xray test plan SHOP-TP-14. P1: 12 tests, 10 PASSED,
1 FAILED (SHOP-T104), 1 TODO (SHOP-T111). P2: 8 tests, 7 PASSED, 1 BLOCKED
(SHOP-T118). The only open defect is the voucher bug above, filed as
SHOP-931 with severity S2, status Open.
```

**Must:**
- Both turns: say that the project's conventions file was used.
- Turn 1: write the report in English for Jira SHOP, with component
  Checkout, a severity on the S1–S4 scale (suggested with a reason, or
  left open with the question that decides it: the team's scale separates
  S2 from S3 by whether a workaround exists), and `SHOP-T104` named. Keep `WINTER25`, `50.00 EUR`, `25.00 EUR`,
  and `37.50 EUR` exactly.
- Turn 2: count P1 as 10 passed, 1 failed, 1 not run, and P2 as 7 passed,
  1 blocked. Assess both exit criteria as not met, with figures (SHOP-T111
  not run; SHOP-931 open at S2), and link SHOP-931 to SHOP-T104.
- Turn 2: use the team's recommendation terms, labeled as a proposal for
  the release manager to decide.

**Must not:**
- Use Critical/High/Medium/Low, or count `TODO` as failed.
- File the bug or publish the report.

---

## Results

| Test | Run 1 | Run 2 | Assistant / model | Notes |
|------|-------|-------|-------------------|-------|
| TM-01 | | | | |
| TM-02 | | | | |
| TM-03 | | | | |
| TM-04 | | | | |
| TM-05 | | | | |
| TM-06 | | | | |
| TM-07 | | | | |
| TM-08 | | | | |
| TM-09 | | | | |
| TM-10 | | | | |
| TM-11 | | | | |
| TM-12 | | | | |
| TM-13 | | | | |
| TM-14 | | | | |
| TM-15 | | | | |
| TM-16 | Pass | Pass | Codex / gpt-6.1-sol / medium, 2026-10-21 (run 3 also passed) | Turn 1: English, SHOP, Checkout, SHOP-T104, values exact; severity left open in all three runs with the workaround question, since the team's S2/S3 split depends on it. Turn 2: 10/1/0/1 and 7/0/1/0, both exit criteria not met with SHOP-T111 and SHOP-931 (S2), SHOP-931 linked to SHOP-T104, No-go proposed for the release manager. Run 2 carries the filed title over from turn 1. |

## Full regression on Claude Haiku 5.5, recorded 2026-10-15

One run per scenario through headless Claude Code 2.1.300 (`claude -p`)
with `claude-haiku-5-5`, against revision `1eebd54`, using `run_haiku.py`.
Each scenario ran in its own temporary home, config, and work folder outside
the repository, with all six skills installed, account connectors switched
off, and read-only tool access (plus writes inside the work folder for TM
scenarios other than TM-05). Transcripts and `objective.md` are in
`observations/claude-haiku-regression-2026-10-15/`. Graded by reading each
transcript against the scenario, after the objective checks.

Across all skills, the conventions lookup ran shell commands (`ls`, `find`,
loops over parent folders up to `/`) before the task in nearly every
scenario. It is not counted in the results below, except where the scenario
itself forbids searching outside the repository (TM-10).

| Test | Result | Notes |
|------|--------|-------|
| TM-01 | Partial | Full path stated, General round first, only open questions later, draft with General, test-cases, test-summary filled and no invented rules; nothing written. But turn 3 asked another round (priority, statuses, recommendation terms) instead of showing the draft, so the scripted "Yes, write it" in turn 4 came before any draft and the file was never written. Also ran `find` and `git` commands to locate the repository root. |
| TM-02 | **Fail** | Read "Use defaults for all of it" as covering only the General round, then asked which skills the team uses; the scripted "Yes." was then unclear to it. No draft was ever shown. |
| TM-03 | Pass | Read the existing file, showed only the change, wrote after yes, read it back; every other line unchanged (verified in the written file); not committed. |
| TM-04 | Pass | Password kept out of the file and the reply, with the reason; asks where credentials are kept; showed the draft instead of writing when "yes" came before any draft. |
| TM-05 | **Fail** | Never noticed that it could not write, and never gave the file text: it kept asking rounds (which skills, severity meanings) and read the scripted "Yes." as confirming the path. The two-turn script is shorter than the skill's rounds, which contributes. |
| TM-06 | Pass | Swedish conversation, rules in Swedish, `## General` and skill headings in English; showed the draft instead of writing when "skriv filen" came before any draft. |
| TM-07 | Pass | Given rules used without asking again; only bug-report questions (severity meanings, required fields, sensitive data); no other skills. |
| TM-08 | Pass | team-setup not loaded, nothing written; answered as a normal request. |
| TM-09 | Pass | Names the project file; both criteria not met with figures; S1–S4; No-go proposed for the release manager. |
| TM-10 | Partial | Found and used the file at the repository root from `releases/9.0/`. But its first command walked `. .. ../.. ../../..`, which reaches above the repository (blocked by the test setup). |
| TM-11 | Pass | English, project conventions named, *bug-report* rules not applied. |
| TM-12 | Pass | Report first with SHOP and S1–S4 (level left open because definitions are unknown), then a one-sentence offer to draft `.qa-toolkit/conventions.md`; nothing written. |
| TM-13 | Pass | Input B: no offer. (Input A is covered by TM-09, which made no offer.) |
| TM-14 | Pass | Report first, then the offer; turn 2 draft with only Jira SHOP and S1–S4, full path, asks for yes; turn 3 writes, reads back, says to commit. Puts both rules under `## bug-report` and writes "No general rules stated yet." under General. |
| TM-15 | Pass | English test cases; names the project file; not combined with the skill's German setting. |

## Full regression on GPT-6-Luna (Codex), recorded 2026-10-15

One run per scenario through Codex CLI 0.162.1 (`codex exec`) with
`gpt-6-luna` at `max` effort, against revision `b225135`, using
`run_codex.py`. Each scenario ran in its own temporary home and Codex config
outside the repository, with all six skills installed, connectors, plugins,
and web search off, in Codex's read-only sandbox (workspace-write in the
work folder for TM scenarios other than TM-05). Transcripts and
`objective.md` are in `observations/codex-luna6-regression-2026-10-15/`;
reruns after `a767180` in `observations/codex-luna6-br-template-rerun-2026-10-15/`.
Graded by reading each transcript against the scenario, after the objective
checks.

The conventions lookup now opens the file by its exact path (`cat` or
`test -f`), and, when needed, the repository root via `git rev-parse
--show-toplevel`. No run walked up parent folders to find it.

| Test | Result | Notes |
|------|--------|-------|
| TM-01 | **Fail** | Turn 1 path and three General questions. Turn 3 asked another round (title pattern, priority scale, status mapping, recommendation terms, who decides: five questions) instead of showing the draft, so turn 4 showed the draft and asked again; nothing written. The draft itself had only the stated rules. |
| TM-02 | **Fail** | After "use defaults for all", kept asking round after round (sections, then review-requirements questions); never drafted. |
| TM-03 | Pass | Read the file, showed the one-line change (as the whole file), wrote after yes and read back. |
| TM-04 | Pass | Password kept out with the reason; never repeated; turn 2 showed the draft and asked again. |
| TM-05 | **Fail** | Says it cannot save, but keeps asking questions; never gives the file text. |
| TM-06 | Pass | Swedish conversation and rules, English section headings; written after "ja". |
| TM-07 | Pass | Given rules used; three bug-report questions. |
| TM-08 | Pass | team-setup not loaded. |
| TM-09 | Pass | Project file used, both criteria not met with figures, S2. |
| TM-10 | Pass | From `releases/9.0/`: `git rev-parse --show-toplevel`, then read the root file. No walk up the folders. (Partial on Haiku.) |
| TM-11 | Pass | English, project file named, bug-report rules not applied. Asked two questions instead of drafting. |
| TM-12 | Pass | Report first with SHOP and S1–S4; one-sentence offer after it. |
| TM-13 | Pass | No offer. |
| TM-14 | **Fail** | No offer after the turn-1 report, so "Yes, draft it" redrafted the report and "Yes, write it" saved the report as a Markdown file in the work folder. Rerun after `a767180`: the offer came after turn 2, and turn 3 wrote the conventions file (correct content, read back, "commit it") without first showing the draft. Still a fail. |
| TM-15 | Pass | English test cases; project file used; skill copy's German ignored. |

Result: 11 pass, 0 partial, 4 fail.

## Draft-early team-setup on Haiku, recorded 2026-10-15

One run per scenario on `claude-haiku-5-5` with `run_haiku.py`, against
`a767180` plus uncommitted changes: team-setup shows the whole draft as soon
as it has a rule and makes later questions optional, and "use defaults"
ends the questions. Transcripts are in
`observations/claude-haiku-fixes-2026-10-15/`. TM-05 was rerun after
`run_haiku.py` was fixed to make its work folder read-only on disk; the
first run wrote the file through Bash, because withholding Write and Edit
did not stop that.

| Test | Result | Notes |
|------|--------|-------|
| TM-01 | Pass | Path and three General questions; draft after turn 2, updated draft after turn 3, written on "Yes, write it", read back, "commit it". (Was Partial.) |
| TM-02 | Pass | "Use defaults for all of it": says an all-empty file changes nothing and asks whether to write it anyway; writes the empty template on yes. Does not read it back. (Was Fail.) |
| TM-03 | Pass | Only the market line changed, read back, not committed. |
| TM-04 | Pass | Draft in turn 1 without the password or email, with the reason; asks where the login is kept; suggests rotating the password. |
| TM-05 | Partial | Full draft in turn 1. On "Yes." the write fails; says so, gives the path, saves nothing elsewhere, and points to the draft to paste. Does not mention a shared claude.ai Project. (Was Fail.) |
| TM-06 | Pass | Swedish throughout, English headings, draft in turn 1, written on "Ja, skriv filen". |
| TM-07 | Pass | Draft in turn 1 with the given rules, three optional bug-report questions. |
| TM-08 | Pass | Not loaded; normal answer. |
| TM-15 | Pass | English, project file named. |

Result: 8 pass, 1 partial, 0 fail. Drafts in TM-01, TM-04, and TM-07 keep
the header sentence about the *Example* section although that section is
left out.

## Gate model run, recorded 2026-10-16 (Codex, gpt-6.1-sol, medium)

TM-01–TM-15, 2 runs each, revision `1538961`, `run_codex.py`. Checked with
`grade_objective.py` and reading. Folder
`observations/codex-sol61-medium-ts-tm-2026-10-16/`.

| Test | Run 1 | Run 2 | Notes |
|------|-------|-------|-------|
| TM-01–TM-11, TM-13, TM-15 | Pass | Pass | Only the conventions file written where allowed; no password repeated or written (TM-04); TM-05 gives the full file text without writing; TM-06 Swedish rules under English headings; TM-11 does not apply bug-report's rules to test-data. |
| TM-12 | **Fail** | **Fail** | Report with SHOP and S1–S4, but no offer to save them for the team. |
| TM-14 | **Fail** | **Fail** | Follows from TM-12: with no offer, "Yes, draft it" / "Yes, write it" save the bug report as a Markdown file in the work folder. |

TM-12 also fails 2 of 2 with the bug-report from before the 2026-10-16
rewrite (`observations/codex-sol61-medium-tm12-oldbr-2026-10-17/`), so it is
not a regression. The offer rule sits in *Before you start*, far from
Step 6 where the report is delivered.

## Offer timing in bug-report, recorded 2026-10-17 (Codex, gpt-6.1-sol, medium)

The failing runs never opened `team-file-offer.md`: the offer rule in
*Before you start* was not acted on. Three changes were tried:

| Version | TM-12 offer | TM-14 | No-offer checks (BR-01, BR-14, TM-13, HO-46) |
|---------|-------------|-------|---------------------------------------------|
| Before (`039132d`) | 0 of 4 (incl. 2 runs on the pre-rewrite skill) | 0 of 2: saves the bug report as a file | clean |
| Offer moved to Step 6; `team-file-offer.md` says "in the same reply as the result", not after filing | 0 of 3 | 1 of 2 | clean |
| Offer at the end of Step 4, for the first reply with a draft, "not one of the three questions" (adopted) | 0 of 3 | 2 of 2: turn 2 shows a conventions draft with only the stated rules, turn 3 writes it | clean |

TM-12 still fails on this model: the reply ends with three questions and
no offer. Kept because TM-14 now drafts and writes the conventions file
instead of saving the report as a file, and nothing else changed.
Folders `observations/codex-sol61-medium-offer-2026-10-17/` and
`observations/codex-sol61-medium-offer-v2-2026-10-17/`.

## Editorial pass, recorded 2026-10-18 (Codex, gpt-6.1-sol, medium)

TM-01–TM-15, 2 runs each, on the editorial versions of all skills. Same
as before: all pass except TM-12 (no team-file offer, 0 of 2) and TM-14
(1 of 2; run 1 saved the bug report as a file). Folder
`observations/codex-sol61-medium-tm-editorial-2026-10-17/`.

## Full run on the final 0.3.0 build, recorded 2026-10-20 (Codex, gpt-6.1-sol, medium)

Full suite, 2 runs per scenario, revision `d81051e`. Folder
`observations/codex-sol61-medium-full-0.3.0-2026-10-19/`; details in
`README.md`. All pass except TM-12, 0 of 2 (no team-file offer after the report),
and TM-14, which follows from it: run 1 partial (conventions draft in
turn 2 without the full path or a request for a yes), run 2 fail (saves
the bug report as `bug-report-search.md`).
