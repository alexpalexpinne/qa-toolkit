#!/usr/bin/env python3
"""Run the scenarios in tests/*.md through headless Codex (`codex exec`).

The Codex counterpart of run_haiku.py, with the same scenarios, setup, and
transcript format, so grade_objective.py reads both. Each scenario runs in
its own temporary home and Codex config, outside the repository, with fresh
copies of all six skills in ~/.agents/skills. The user's config is ignored;
only the login (auth.json) is copied in. Connectors, plugins, web search,
browser and computer use, and sub-agents are turned off. Scenarios run in a
read-only sandbox, except TM scenarios that may write (workspace-write,
limited to the work folder). A leading `/skill` command becomes `$skill`,
Codex's way to invoke a skill by name.

Usage: run_codex.py <out-dir> [ID ...] [--model MODEL] [--effort EFFORT]
                    [--workers N] [--baseline] [--agents-md]
(no IDs = all scenarios)

--agents-md also writes the scenario's team conventions to AGENTS.md in the
working folder, where Codex reads them on its own. With --baseline, AGENTS.md
replaces the conventions file: what a team gets by writing its rules there
instead of using the skills.
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import time

from run_haiku import READ_ONLY_TM, RETIRED, SECS, baseline_prompt, prepare, revision, snapshot, team_rules, turns

AUTH = os.path.expanduser("~/.codex/auth.json")
DISABLED = ("apps", "plugins", "remote_plugin", "browser_use", "browser_use_external", "computer_use",
            "image_generation", "multi_agent", "tool_suggest", "skill_mcp_dependency_install")


def codex_prompt(prompt):
    """Turn a leading /skill or /qa-toolkit:skill command into $skill."""
    return re.sub(r"\A/(?:qa-toolkit:)?([a-z-]+)\b", r"$\1", prompt)


def unwrap(command):
    """Show the command the model wrote, without Codex's `bash -lc` wrapper."""
    try:
        argv = shlex.split(command)
    except ValueError:
        return command
    if len(argv) == 3 and os.path.basename(argv[0]) in ("bash", "sh", "zsh") and argv[1] in ("-c", "-lc"):
        return argv[2]
    return command


def describe(item):
    kind = item.get("type")
    if kind == "command_execution":
        call = [f"Shell {unwrap(item.get('command', ''))}"[:300]]
        if item.get("exit_code") not in (0, None):
            call.append(f"  -> error: exit {item['exit_code']}: {(item.get('aggregated_output') or '')[:160]}")
        return call
    if kind == "file_change":
        return ["Edit " + ", ".join(c.get("path", "") for c in item.get("changes", []))]
    if kind == "mcp_tool_call":
        return [f"MCP {item.get('server')}.{item.get('tool')} {json.dumps(item.get('arguments'), ensure_ascii=False)[:200]}"]
    if kind == "web_search":
        return [f"WebSearch {item.get('query', '')}"]
    if kind not in ("agent_message", "reasoning", "todo_list"):
        return [f"{kind} {json.dumps(item, ensure_ascii=False)[:200]}"]
    return []


def run(sid, out, model, effort, rev, baseline=False, agents_md=False):
    dest = f"{out}/{sid}"
    if os.path.exists(f"{dest}/transcript.md"):
        return f"{sid}: skipped (exists)"
    # A folder without a transcript is an interrupted run: start it again.
    shutil.rmtree(dest, ignore_errors=True)
    base = tempfile.mkdtemp(prefix=f"qa-{sid}-")
    home, work, cwd = prepare(sid, base, baseline, skills_dir=".agents/skills")
    if agents_md:
        if baseline:
            shutil.rmtree(f"{work}/.qa-toolkit", ignore_errors=True)
        rules = team_rules(sid)
        if rules:
            with open(f"{cwd}/AGENTS.md", "w", encoding="utf-8") as f:
                f.write("# Team conventions for testing work\n\n" + rules.strip() + "\n")
    os.makedirs(f"{home}/.codex", exist_ok=True)
    shutil.copy(AUTH, f"{home}/.codex/auth.json")
    internal = {f"{home}/.codex", f"{home}/.cache"}
    before = {"home": snapshot(home, internal), "work": snapshot(work, set())}
    env = {**os.environ, "HOME": home, "CODEX_HOME": f"{home}/.codex"}
    writable = sid[:2] == "TM" and sid not in READ_ONLY_TM
    config = [f'model_reasoning_effort="{effort}"', 'web_search="disabled"',
              f'sandbox_mode="{"workspace-write" if writable else "read-only"}"']
    if writable:
        config += [f"sandbox_workspace_write.writable_roots={json.dumps([work])}",
                   "sandbox_workspace_write.exclude_slash_tmp=true",
                   "sandbox_workspace_write.exclude_tmpdir_env_var=true"]
    flags = ["--json", "--ignore-user-config", "--skip-git-repo-check", "-m", model]
    for c in config:
        flags += ["-c", c]
    for feature in DISABLED:
        flags += ["--disable", feature]
    os.makedirs(dest)
    thread, log = None, []
    t0 = time.time()
    prompts = [baseline_prompt(p) for p in turns(sid)] if baseline else [codex_prompt(p) for p in turns(sid)]
    for n, prompt in enumerate(prompts, 1):
        cmd = ["codex", "exec", "resume", thread, *flags, "-"] if thread else ["codex", "exec", *flags, "-"]
        with open(f"{dest}/turn{n}.jsonl", "w") as ev, open(f"{dest}/turn{n}.stderr", "w") as er:
            try:
                code = subprocess.run(cmd, cwd=cwd, env=env, stdout=ev, stderr=er,
                                      input=prompt, text=True, timeout=1800).returncode
            except subprocess.TimeoutExpired:
                er.write("\nTIMEOUT\n")
                code = "timeout"
        messages, tools, completed, failure = [], [], False, None
        with open(f"{dest}/turn{n}.jsonl") as ev:
            for line in ev:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("type") == "thread.started":
                    thread = thread or e.get("thread_id")
                if e.get("type") == "item.completed":
                    item = e.get("item", {})
                    if item.get("type") == "agent_message":
                        messages.append(item.get("text", ""))
                    tools += describe(item)
                if e.get("type") == "turn.completed":
                    completed = True
                if e.get("type") == "turn.failed":
                    completed = False
                    failure = (e.get("error") or {}).get("message", "turn failed")
        # Only a turn that ran to the end is a result (not a usage limit, a
        # crash, or a timeout): drop the scenario so a rerun picks it up again.
        if code != 0 or not completed:
            reason = failure or f"exit {code}, turn not completed"
            shutil.rmtree(base, ignore_errors=True)
            shutil.rmtree(dest, ignore_errors=True)
            return f"{sid}: FAILED in turn {n}: {reason[:120]}"
        log.append((prompt, tools, "\n\n".join(messages)))
    after = {"home": snapshot(home, internal), "work": snapshot(work, set())}
    written = [(root, path) for root in ("home", "work") for path, mtime in sorted(after[root].items())
               if before[root].get(path) != mtime]
    with open(f"{dest}/transcript.md", "w", encoding="utf-8") as f:
        f.write(f"# {sid} — Codex, {model} ({effort}), {time.strftime('%Y-%m-%d')}\n\n")
        setup = "baseline, no skills installed" if baseline else f"skill revision {rev}"
        if agents_md:
            setup += ", team conventions in AGENTS.md"
        f.write(f"Configuration: {setup}. Working folder: `{os.path.relpath(cwd, base)}`. "
                "Every agent message of a turn is shown under its answer.\n\n")
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
                    content = text.read()
                    f.write("```\n" + content[:20000] + "\n```\n\n")
                    if len(content) > 20000:
                        f.write(f"(Preview: first 20,000 of {len(content):,} characters. "
                                "The complete file is under files/ and is what the grader scans.)\n\n")
            except (UnicodeDecodeError, OSError):
                f.write("(not a text file)\n\n")
            os.makedirs(os.path.dirname(f"{dest}/files/{root}/{path}"), exist_ok=True)
            shutil.copy(source, f"{dest}/files/{root}/{path}")
    shutil.rmtree(base, ignore_errors=True)
    return f"{sid}: done in {time.time() - t0:.0f}s, {len(log)} turn(s), {len(written)} file(s) written"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("out")
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--model", default="gpt-6-luna")
    parser.add_argument("--effort", default="max")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--baseline", action="store_true", help="run without the skills")
    parser.add_argument("--agents-md", action="store_true",
                        help="also write the team conventions to AGENTS.md")
    args = parser.parse_intermixed_args()
    os.makedirs(args.out, exist_ok=True)
    ids = args.ids or sorted((s for s in SECS if s not in RETIRED), key=lambda s: (s[:2], int(s[3:])))
    unknown = [i for i in ids if i not in SECS]
    if unknown:
        parser.error(f"unknown scenario: {', '.join(unknown)}")
    rev = revision()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for msg in pool.map(lambda s: run(s, args.out, args.model, args.effort, rev, args.baseline, args.agents_md), ids):
            print(msg, flush=True)


if __name__ == "__main__":
    main()
