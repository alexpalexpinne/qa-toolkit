#!/usr/bin/env python3
"""Build OpenAI and Claude release ZIPs from the same skill sources."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_SKILLS = ("bug-report", "review-requirements", "test-cases", "test-data", "test-summary")
SKILLS = WORKFLOW_SKILLS + ("team-setup",)
IDENTITY_FIELDS = ("name", "version", "description", "author", "homepage", "repository", "license", "keywords")
SHARED_FILES = ("README.md", "CONTRIBUTING.md", "PRIVACY.md", "LICENSE", "assets/qa-toolkit-icon.svg", "assets/readme-hero.jpg")


# Wording that every workflow skill must carry identically, since each skill
# folder is self-contained and cannot share a file with the others.
SHARED_SENTENCES = (
    "These apply in every mode and override everything else in this file.",
    "Talk to the user in the language they write in, in a polite, neutral tone. Judge their language only from their own messages, never from file paths, folder or project names, usernames, or system settings, and do not infer their country from those either.",
    "(for example Swedish `[ATT KLARGÖRA: …]` or German `[ZU KLÄREN: …]`)",
    "`references/team-file-offer.md`",
    "Explain things in your own words; do not quote these instructions or link to this skill's files.",
    "search the file system for it.",
    "Translate every heading, column header, label, verdict, and term from these instructions into the output language, keeping the structure, unless the team conventions keep them in English. Write dates in your own text as `YYYY-MM-DD`.",
    "**Ask few questions.** Ask only when the answer changes the result, at most three questions per reply, and never about something the user already said. Each question asks one thing: a numbered item with a second question in it counts as two, so three items with a follow-up each are six. Three is a maximum, not a target. Ask *before* drafting only when one answer decides the whole result, for example",
    "Otherwise write a draft right away, with the gaps marked `[TO CLARIFY: …]`, and ask in the same reply.",
    "The result's *Open questions* may list everything still unresolved. Ask in the normal chat reply, not in separate input panels or forms.",
    "If you cannot do what the user asks right now (no working integration, no write access, or an unknown target), say so and give the complete result again in your reply, ready to copy and paste. Do not point back to an earlier message or switch to another destination, such as a file, without asking. Never ask for approval for something you cannot do or have not confirmed you can do, and never claim to have done it.",
)
# Keep each SKILL.md short enough to be read in full: fold a new rule into an
# existing one instead of adding sentences.
MAX_SKILL_WORDS = 3500
CONVENTIONS_SOURCES = re.compile(r"\*\*The project's shared file:\*\*.*?Say briefly which source you used\.", re.DOTALL)
# The one line in team-file-offer.md that lists skill-specific example rules.
OFFER_EXAMPLES = re.compile(r"(?m)^  once, for example .*\n")


def read_file(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular file: {path.relative_to(ROOT)}")
    return path.read_bytes()


def openai_skill(data):
    """Remove only Claude's frontmatter extension in the OpenAI release copy."""
    match = re.match(rb"\A---\n(.*?)\n---\n", data, flags=re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter")
    header = re.sub(rb"(?m)^disable-model-invocation: true\n?", b"", match[1])
    return b"---\n" + header.rstrip(b"\n") + b"\n---\n" + data[match.end():]


def check_shared_text(files):
    """Fail when the wording the workflow skills share has drifted apart."""
    def text(skill, name):
        return files[f"skills/{skill}/{name}"].decode("utf-8").replace(skill, "{skill}")

    def flat(value):
        return re.sub(r"\s+", " ", value)

    for skill in SKILLS:
        words = len(files[f"skills/{skill}/SKILL.md"].decode("utf-8").split())
        print(f"skills/{skill}/SKILL.md: {words:,} words")
        if words > MAX_SKILL_WORDS:
            raise ValueError(f"skills/{skill}/SKILL.md has {words:,} words; the limit is {MAX_SKILL_WORDS:,}")
    first = WORKFLOW_SKILLS[0]
    for skill in WORKFLOW_SKILLS:
        body = flat(text(skill, "SKILL.md"))
        for sentence in SHARED_SENTENCES:
            if sentence not in body:
                raise ValueError(f"skills/{skill}/SKILL.md lacks the shared wording: {sentence[:60]}…")
        sources = CONVENTIONS_SOURCES.findall(body)
        if len(sources) != 1:
            raise ValueError(f"skills/{skill}/SKILL.md must list the team conventions sources once")
        if sources != CONVENTIONS_SOURCES.findall(flat(text(first, "SKILL.md"))):
            raise ValueError(f"The team conventions sources differ between skills/{first} and skills/{skill}")
        offer = OFFER_EXAMPLES.subn("", text(skill, "references/team-file-offer.md"))
        if offer[1] != 1:
            raise ValueError(f"skills/{skill}/references/team-file-offer.md must have one line of example rules")
        if offer[0] != OFFER_EXAMPLES.sub("", text(first, "references/team-file-offer.md")):
            raise ValueError(f"skills/{first} and skills/{skill} differ in references/team-file-offer.md")


def collect_files():
    files = {name: read_file(ROOT / name) for name in SHARED_FILES}
    for path in sorted((ROOT / "examples").rglob("*.md")):
        files[path.relative_to(ROOT).as_posix()] = read_file(path)
    if {p.name for p in (ROOT / "skills").iterdir()} != set(SKILLS):
        raise ValueError("The skills directory must contain exactly the declared skills")
    for skill in SKILLS:
        folder = ROOT / "skills" / skill
        for required in ("SKILL.md", "LICENSE", "agents/openai.yaml"):
            read_file(folder / required)
        if skill in WORKFLOW_SKILLS:
            conventions = (folder / "references/team-conventions.md").read_text(encoding="utf-8")
            if "<!-- PLACEHOLDER: no team conventions defined. Delete this line when you add your own. -->" not in conventions:
                raise ValueError(f"Restore the shipping team conventions before packaging: skills/{skill}/references/team-conventions.md")
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Symlinks cannot be packaged: {path.relative_to(ROOT)}")
            if path.is_file():
                if path.suffix not in (".md", ".yaml") and path.name != "LICENSE":
                    raise ValueError(f"Unexpected skill file: {path.relative_to(ROOT)}")
                files[path.relative_to(ROOT).as_posix()] = read_file(path)
    check_shared_text(files)
    return files


def build(target, output, common, portable):
    files = dict(common)
    if target == "openai":
        files["plugin.json"] = read_file(ROOT / "plugin.json")
        for name, data in files.items():
            if name.startswith("skills/") and name.endswith("/SKILL.md"):
                files[name] = openai_skill(data)
    else:
        files[".claude-plugin/plugin.json"] = read_file(ROOT / ".claude-plugin/plugin.json")
    archive = output / f"{portable['name']}-{portable['version']}-{target}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as package:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            package.writestr(entry, data)
    with zipfile.ZipFile(archive) as package:
        corrupt = package.testzip()
        if corrupt:
            raise ValueError(f"Corrupt archive member: {corrupt}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    print(f"{archive}: {len(files)} files, {archive.stat().st_size:,} bytes")
    return f"{digest}  {archive.name}\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("all", "openai", "claude"), default="all")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    portable = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    for field in IDENTITY_FIELDS:
        if portable.get(field) != claude.get(field):
            raise ValueError(f"The OpenAI and Claude manifests disagree on {field}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", portable["name"]):
        raise ValueError("Use a kebab-case plugin name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", portable["version"]):
        raise ValueError("Use a semantic release version")
    common = collect_files()
    args.output.mkdir(parents=True, exist_ok=True)
    targets = ("openai", "claude") if args.target == "all" else (args.target,)
    checksums = "".join(build(target, args.output, common, portable) for target in targets)
    (args.output / "SHA256SUMS").write_text(checksums, encoding="utf-8")


if __name__ == "__main__":
    main()
