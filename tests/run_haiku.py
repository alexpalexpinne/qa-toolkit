#!/usr/bin/env python3
"""Run the scenarios in tests/*.md through headless Claude Code.

Each scenario runs in its own temporary home, Claude config, and work folder,
outside the repository, with fresh copies of all six skills (as the plugin
installs them) and the scenario's conventions in place. Nothing touches the
user's real configuration. Transcripts, and every file the session wrote,
are copied to <out-dir>/<ID>/.

With --baseline, no skills are installed and each `/skill` command is
replaced by a plain request in English (BASELINE_REQUEST), so the same
scenario shows what the model does without the skill. Use it only with
scenarios whose input is in English.

Usage: run_haiku.py <out-dir> [ID ...] [--model MODEL] [--workers N] [--baseline]
(no IDs = all scenarios)
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import tempfile
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS = os.path.expanduser("~/.claude/.credentials.json")
SKILLS = ("bug-report", "review-requirements", "test-cases", "test-data", "test-summary", "team-setup")
FILES = {"BR": "bug-report", "RR": "review-requirements", "TC": "test-cases",
         "TD": "test-data", "TS": "test-summary", "TM": "team-setup", "HO": "held-out"}
BASELINE_REQUEST = {"bug-report": "Help me write a bug report.",
                    "review-requirements": "Review this requirement for testability.",
                    "test-cases": "Write test cases for this.",
                    "test-data": "Create test data for this.",
                    "test-summary": "Write a test report.",
                    "team-setup": "Help us set up our team's QA conventions."}
# The skill a TM scenario exercises, where it is not team-setup itself.
TM_SKILL = {"TM-09": "test-summary", "TM-10": "test-summary", "TM-11": "test-data",
            "TM-12": "bug-report", "TM-13": "test-data", "TM-14": "bug-report",
            "TM-15": "test-cases"}

# The skill's own references/team-conventions.md: filled with its example, or
# with the block in the scenario's setup.
FILL_EXAMPLE = {"BR-09", "RR-05", "TC-06", "TD-11", "TS-06", "TS-15"}
FILL_CUSTOM = {"RR-13"}
FILL_TEXT = {"TM-15": "Test cases are written in German."}
# The project's .qa-toolkit/conventions.md: the block in the scenario's setup
# (or the named scenario's), or the given text.
PROJECT_FROM = {"BR-21": "BR-21", "BR-23": "BR-21", "BR-24": "BR-24",
                "TM-09": "TM-09", "TM-10": "TM-09", "TM-11": "TM-11", "HO-13": "HO-13",
                "HO-41": "HO-41", "HO-46": "HO-46", "HO-61": "HO-61", "HO-77": "HO-77"}
PROJECT_TEXT = {
    "TM-03": "## General\n- Reports are written in English.\n- Tracker: Jira, project SHOP.\n"
             "- Severity: S1, S2, S3, S4.\n\n## review-requirements\n\n## test-cases\n\n"
             "## test-data\n- Markets: SE, NO.\n- Test data marker: `TEST-`.\n\n"
             "## bug-report\n\n## test-summary\n",
    "TM-15": "## General\n- Test cases are written in English.\n",
}
FIXTURES = {"TC-21": ["xray-tests-export.csv"],
            "TS-14": ["xray-test-plan-export.csv", "jira-open-bugs-export.csv"],
            "TS-15": ["xray-test-plan-export.csv", "jira-open-bugs-export.csv"]}
CODE_PROJECT = {"BR-11", "BR-13", "TC-10", "TD-14", "TS-16"}
SUBFOLDER = {"TM-10": "releases/9.0"}
# TM scenarios run in a git repository and may write inside it, except TM-05.
READ_ONLY_TM = {"TM-05"}
# TM-13 input A needs a hand-made input; its no-offer check is covered by the
# TM-09 run. Only input B runs here.
INPUT_B = {"TM-13"}


def load_sections():
    secs = {}
    for prefix, name in FILES.items():
        sid, body, fence = None, [], False
        with open(f"{REPO}/tests/{name}.md", encoding="utf-8") as f:
            lines = f.read().split("\n") + ["## END"]
        for line in lines:
            if line.startswith("```"):
                fence = not fence
            if not fence and line.startswith("## "):
                text = "\n".join(body)
                if sid and "**Input" in text and sid not in secs:
                    secs[sid] = text
                m = re.match(r"## ([A-Z]{2}-\d+) ", line)
                sid, body = (m.group(1) if m else None), []
                continue
            body.append(line)
    return secs


SECS = load_sections()
# Held-out scenarios that informed a fix: kept for history, run only by name.
RETIRED = {"HO-33", "HO-41", "HO-62"}


def first_block(s):
    return re.search(r"```[a-z]*\n(.*?)\n```", s, re.S).group(1)


def split_turns(block):
    if re.search(r"^Turn \d+:", block, re.M):
        parts = re.split(r"^Turn \d+: ?", block, flags=re.M)
        return [p.strip() for p in parts if p.strip()]
    return [block]


def turns(sid):
    body = SECS[sid]
    if sid in INPUT_B:
        return [first_block(body[body.index("**Input B"):])]
    m = re.search(r"\*\*Input[^*]*\*\*([^\n]*)\n(.*)", body, re.S)
    header, rest = m.group(1).strip(), m.group(2)
    ref = re.search(r"(?:Complete|The|Same as) ([A-Z]{2}-\d+)", header)
    if ref and "with this line added before the log" in header:
        base = turns(ref.group(1))[0]
        return [base.replace("Here is the log:", first_block(rest) + "\nHere is the log:", 1)]
    then = re.match(r"([A-Z]{2}-\d+), then:", header)
    if then:
        return turns(then.group(1)) + split_turns(first_block(rest))
    if ref and header.startswith("Complete"):
        return turns(ref.group(1)) + [first_block(rest)]
    if ref:
        return turns(ref.group(1))
    return split_turns(first_block(rest))


def setup_block(sid):
    setup = re.search(r"\*\*Setup:\*\*(.*?)\n\*\*", SECS[sid], re.S).group(1)
    return first_block(setup)


def make_code_project(work):
    os.makedirs(f"{work}/tests", exist_ok=True)
    with open(f"{work}/discount.py", "w") as f:
        f.write("def apply_discount(total, percent):\n    return round(total * (1 - percent / 100), 2)\n")
    with open(f"{work}/tests/test_discount.py", "w") as f:
        f.write("from discount import apply_discount\n\n\ndef test_ten_percent():\n"
                "    assert apply_discount(100, 10) == 90\n")
    with open(f"{work}/ci.log", "w") as f:
        f.write("FAILED tests/test_discount.py::test_rounding - assert 33.33 == 33.34\n"
                "1 failed, 1 passed in 0.12s\n")


def tested_skill(sid):
    if sid[:2] == "HO":
        return re.search(r"\*\*Skill:\*\* `([a-z-]+)`", SECS[sid]).group(1)
    return TM_SKILL.get(sid, FILES[sid[:2]])


def baseline_prompt(prompt):
    """Replace a leading /skill command with a plain request."""
    m = re.match(r"/(?:qa-toolkit:)?([a-z-]+)\b[ \t]*\n?", prompt)
    if not m or m.group(1) not in BASELINE_REQUEST:
        return prompt
    rest = prompt[m.end():]
    return BASELINE_REQUEST[m.group(1)] + ("\n" + rest if rest else "")


def prepare(sid, base, baseline=False, skills_dir=".claude/skills"):
    """Set up the home and work folders; skills_dir is where the host finds user skills."""
    home, work = f"{base}/home", f"{base}/work"
    os.makedirs(f"{home}/{skills_dir}", exist_ok=True)
    os.makedirs(work, exist_ok=True)
    if skills_dir == ".claude/skills":
        os.symlink(CREDS, f"{home}/.claude/.credentials.json")
    if not baseline:
        for skill in SKILLS:
            shutil.copytree(f"{REPO}/skills/{skill}", f"{home}/{skills_dir}/{skill}")
    if not baseline and (sid in FILL_EXAMPLE or sid in FILL_CUSTOM or sid in FILL_TEXT):
        conv = f"{home}/{skills_dir}/{tested_skill(sid)}/references/team-conventions.md"
        with open(conv, encoding="utf-8") as f:
            s = f.read()
        if sid in FILL_EXAMPLE:
            fill = re.search(r"```markdown\n(.*?)\n```", s, re.S).group(1)
        else:
            fill = FILL_TEXT.get(sid) or setup_block(sid)
        s = re.sub(r"<!-- PLACEHOLDER:.*?-->", lambda _: fill, s)
        with open(conv, "w", encoding="utf-8") as f:
            f.write(s)
    project = PROJECT_TEXT.get(sid) or (setup_block(PROJECT_FROM[sid]) if sid in PROJECT_FROM else None)
    if project:
        os.makedirs(f"{work}/.qa-toolkit", exist_ok=True)
        with open(f"{work}/.qa-toolkit/conventions.md", "w", encoding="utf-8") as f:
            f.write("# QA Toolkit team conventions\n\n" + project.strip() + "\n")
    for name in FIXTURES.get(sid, []):
        shutil.copy(f"{REPO}/tests/fixtures/{name}", work)
    if sid in CODE_PROJECT:
        make_code_project(work)
    if sid in CODE_PROJECT or sid[:2] == "TM":
        subprocess.run(["git", "init", "-q", work], check=True)
    cwd = f"{work}/{SUBFOLDER[sid]}" if sid in SUBFOLDER else work
    os.makedirs(cwd, exist_ok=True)
    return home, work, cwd


def snapshot(root, skip):
    found = {}
    for folder, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if os.path.join(folder, d) not in skip and d != ".git"]
        for name in names:
            path = os.path.join(folder, name)
            if not os.path.islink(path):
                found[os.path.relpath(path, root)] = os.path.getmtime(path)
    return found


def revision():
    sha = subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                         capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--", "skills"],
                           capture_output=True, text=True).stdout.strip()
    return f"{sha} with uncommitted skill changes" if dirty else sha


def set_writable(top, writable):
    """Add or remove write permission on every folder under top."""
    for path in [top] + [os.path.join(d, n) for d, names, _ in os.walk(top) for n in names]:
        mode = os.stat(path).st_mode
        os.chmod(path, mode | 0o200 if writable else mode & ~0o222)


def run(sid, out, model, rev, baseline=False):
    dest = f"{out}/{sid}"
    if os.path.exists(f"{dest}/transcript.md"):
        return f"{sid}: skipped (exists)"
    # A folder without a transcript is an interrupted run: start it again.
    shutil.rmtree(dest, ignore_errors=True)
    base = tempfile.mkdtemp(prefix=f"qa-{sid}-")
    home, work, cwd = prepare(sid, base, baseline)
    internal = {f"{home}/.claude", f"{home}/.cache"}
    before = {"home": snapshot(home, internal), "work": snapshot(work, set())}
    env = {**os.environ, "HOME": home, "CLAUDE_CONFIG_DIR": f"{home}/.claude"}
    allowed = ["Read"]
    if sid[:2] == "TM" and sid not in READ_ONLY_TM:
        allowed += [f"Write(/{work}/**)", f"Edit(/{work}/**)"]
    # Withholding Write and Edit is not enough: Bash can still write files.
    read_only = sid in READ_ONLY_TM
    if read_only:
        set_writable(work, False)
    real_home = os.path.expanduser("~")
    denied = [f"{t}(/{real_home}/{d}/**)" for t in ("Read", "Write", "Edit") for d in (".config", ".claude")]
    denied += [f"{t}(/{REPO}/**)" for t in ("Write", "Edit")]
    os.makedirs(dest)
    session, log = None, []
    t0 = time.time()
    prompts = [baseline_prompt(p) for p in turns(sid)] if baseline else turns(sid)
    for n, prompt in enumerate(prompts, 1):
        # --strict-mcp-config without --mcp-config: no connectors from the account.
        cmd = ["claude", "-p", "--model", model, "--output-format", "stream-json", "--verbose",
               "--strict-mcp-config", "--allowedTools", *allowed, "--disallowedTools", *denied]
        if session:
            cmd += ["--resume", session]
        with open(f"{dest}/turn{n}.jsonl", "w") as ev, open(f"{dest}/turn{n}.stderr", "w") as er:
            try:
                code = subprocess.run(cmd, cwd=cwd, env=env, stdout=ev, stderr=er,
                                      input=prompt, text=True, timeout=900).returncode
            except subprocess.TimeoutExpired:
                code = "timeout"
        texts, tools, final = [], [], None
        with open(f"{dest}/turn{n}.jsonl") as ev:
            for line in ev:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("type") == "assistant":
                    for c in e["message"].get("content", []):
                        if c.get("type") == "tool_use":
                            tools.append(f"{c['name']} {json.dumps(c['input'], ensure_ascii=False)[:200]}")
                        if c.get("type") == "text" and c.get("text", "").strip():
                            texts.append(c["text"])
                if e.get("type") == "user" and isinstance(e["message"].get("content"), list):
                    for c in e["message"]["content"]:
                        if c.get("type") == "tool_result" and c.get("is_error"):
                            tools.append(f"  -> error: {str(c.get('content'))[:160]}")
                if e.get("type") == "result":
                    final, session = e, e.get("session_id")
        # Only a turn that ran to the end is a result; anything else is rerun.
        if code != 0 or not final or final.get("subtype") != "success" or final.get("is_error"):
            reason = (final or {}).get("result") or (final or {}).get("subtype") or f"exit {code}, no result"
            if read_only:
                set_writable(work, True)
            shutil.rmtree(base, ignore_errors=True)
            shutil.rmtree(dest, ignore_errors=True)
            return f"{sid}: FAILED in turn {n}: {str(reason)[:120]}"
        # Grade every assistant message of the turn, not only the last one:
        # a value leaked in an intermediate message is still in the reply.
        result = "\n\n".join(texts) or final.get("result") or ""
        log.append((prompt, tools, result))
    after = {"home": snapshot(home, internal), "work": snapshot(work, set())}
    written = [(root, path) for root in ("home", "work") for path, mtime in sorted(after[root].items())
               if before[root].get(path) != mtime]
    with open(f"{dest}/transcript.md", "w", encoding="utf-8") as f:
        f.write(f"# {sid} — Claude Code, {model}, {time.strftime('%Y-%m-%d')}\n\n")
        setup = "baseline, no skills installed" if baseline else f"skill revision {rev}"
        f.write(f"Configuration: {setup}. Working folder: `{os.path.relpath(cwd, base)}`. "
                "Every assistant message of a turn is shown under its answer.\n\n")
        for n, (prompt, tools, result) in enumerate(log, 1):
            f.write(f"## Turn {n}: prompt\n```\n{prompt}\n```\n\n")
            f.write("### Tool calls\n" + ("\n".join(f"- `{t}`" for t in tools) or "- none") + "\n\n")
            f.write(f"### Answer\n\n{result}\n\n")
        f.write("## Files written or changed during the run\n\n")
        if not written:
            f.write("None.\n")
        for root, path in written:
            source = f"{home if root == 'home' else work}/{path}"
            f.write(f"### `{root}/{path}`\n\n")
            try:
                with open(source, encoding="utf-8") as text:
                    f.write("```\n" + text.read()[:20000] + "\n```\n\n")
            except (UnicodeDecodeError, OSError):
                f.write("(not a text file)\n\n")
            os.makedirs(os.path.dirname(f"{dest}/files/{root}/{path}"), exist_ok=True)
            shutil.copy(source, f"{dest}/files/{root}/{path}")
    if read_only:
        set_writable(work, True)
    shutil.rmtree(base, ignore_errors=True)
    return f"{sid}: done in {time.time() - t0:.0f}s, {len(log)} turn(s), {len(written)} file(s) written"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("out")
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--model", default="claude-haiku-5-5")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--baseline", action="store_true", help="run without the skills")
    args = parser.parse_intermixed_args()
    os.makedirs(args.out, exist_ok=True)
    ids = args.ids or sorted((s for s in SECS if s not in RETIRED), key=lambda s: (s[:2], int(s[3:])))
    unknown = [i for i in ids if i not in SECS]
    if unknown:
        parser.error(f"unknown scenario: {', '.join(unknown)}")
    rev = revision()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for msg in pool.map(lambda s: run(s, args.out, args.model, rev, args.baseline), ids):
            print(msg, flush=True)


if __name__ == "__main__":
    main()
