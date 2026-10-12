# Set up personal defaults

Use this flow when the user asks to set up or change their defaults, or
accepts the offer made after a report. A bug about an application's setup
page is a report, not a request to configure this skill.

Personal preferences are saved in `.config/bug-report/preferences.md` in the
user's home folder (`~/.config/bug-report/preferences.md` on macOS and
Linux, `%USERPROFILE%\.config\bug-report\preferences.md` on Windows). They
live outside the skill folder, so reinstalling or updating the skill keeps
them. Never write personal preferences into `team-conventions.md` or into a
project's repository; the team edits its conventions file by hand.

## Ask for preferences

Explain where the choices will be saved and that they are reused in future
conversations. Ask only for choices the user has not already made, in this
conversation or in the report just delivered. Ask numbered questions in the
normal chat reply, at most three per turn; if all four are missing, ask the
first three and ask about sensitive information after the user answers.
Skip a question when the team conventions already decide it, and tell the
user the team's setting applies.

1. Which language should reports use: a fixed language, or the language of
   the user's message? The conversation itself still follows the user's
   language.
2. Where will the reports be used: Jira, GitHub, Azure DevOps, or general
   Markdown? A default project may be included if the user supplies one.
3. How should reports be delivered: copy-paste text, a local file, or an
   offer to submit through an available tracker integration?
4. How should personal and customer data be handled: **Redact** (default),
   or **Preserve** in reports for the chosen destination? Preserve keeps
   only the data a report needs, such as an account email or order ID.
   Passwords, tokens, API keys, and other credentials are always masked.
   Enable Preserve only if the user chooses it; a remark that the tracker
   is internal is not a choice. Skip this question if the team conventions
   forbid Preserve.

If the user says "use defaults" or "don't ask again", save reports in the
user's language, general Markdown, copy-paste delivery, and Redact, so the
offer is not repeated in future conversations. If the user declines saving,
use the choices only in this conversation and say that a new conversation
will not remember them. Never treat silence as a choice.

## Save the choices

Asking for setup, or answering the setup questions after you explained where
they are saved, authorizes writing this file; no separate approval is
needed. Create the folder if it does not exist. If the file exists, change
only the choices the user asked to change and keep everything else.

Save the choices in plain language, for example:

```markdown
# Bug report preferences

## Report language
English.

## Destination
Jira. No default project.

## Delivery
Copy-paste into the Jira description.

## Sensitive information
Redact.
```

For Preserve, name the destination it applies to, for example "Preserve
personal and customer data needed in Jira reports. Credentials are always
masked." Save only the mode and its destination, never example values
mentioned while discussing setup.

Read the file back to check it, then tell the user what was saved and the
file's actual path. Saved preferences do not authorize publishing: core
rule 7 still applies, and a saved project is a suggestion, not permission
to submit there.

If writing is unavailable, give the user the file's text and path to save
themselves, and say the preferences have not been saved yet.

For a setup-only request, finish after reporting what was saved. If the user
also described a bug, continue with it using the new preferences, without
asking them to repeat details.
