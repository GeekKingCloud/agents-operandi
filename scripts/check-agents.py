#!/usr/bin/env python3
"""Check the structure, routing, and public-data safety of this AGENTS baseline."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "AGENTS.md",
    "README.md",
    "instructions/computer-use.md",
    "instructions/development.md",
    "instructions/operations.md",
    "instructions/personal-assistant.md",
    "instructions/research.md",
    "instructions/security-and-privacy.md",
    "instructions/skills.md",
    "workflows/handoff.md",
    "workflows/implementation-finish.md",
    "workflows/repository-guidance.md",
    "workflows/subagents.md",
    "workflows/verification.md",
    "templates/HANDOFF.md",
    "templates/PLAN.md",
    "templates/TASK-BRIEF.md",
    "scripts/check-agents.py",
}

ROOT_ROUTES = {
    "instructions/computer-use.md",
    "instructions/development.md",
    "instructions/operations.md",
    "instructions/personal-assistant.md",
    "instructions/research.md",
    "instructions/security-and-privacy.md",
    "instructions/skills.md",
    "workflows/handoff.md",
    "workflows/repository-guidance.md",
    "workflows/subagents.md",
    "workflows/verification.md",
    "templates/TASK-BRIEF.md",
    "templates/PLAN.md",
}

POLICY_SMOKE_MARKERS = {
    "README.md": ["commit `0e98352`", "Substring markers catch accidental deletion"],
    "AGENTS.md": [
        "When a row matches, read those files before acting",
        "Skills Are the Procedure Layer",
        "Never push, create or update a pull request",
        "exact repository/worktree path, branch, commits",
        "Push back briefly when a request is more complex than needed",
    ],
    "instructions/development.md": [
        "native harness is the default",
        "lumber-hack",
        "atoshell",
        "g8ldfish",
        "implementation finish workflow",
        "Never push, create or update a pull request",
    ],
    "workflows/implementation-finish.md": [
        "Remove Unjustified Machinery",
        "Keep Tests and Explanations Durable",
        "Never remove authentication",
        "rerun every affected check",
    ],
    "instructions/skills.md": [
        "default procedure layer",
        "Crucible",
        "Roast",
        "ask to install or make it available",
        "read its nearest `AGENTS.md`",
        "Do not copy, install, vendor, or sync skills elsewhere",
    ],
    "workflows/subagents.md": [
        "Proposer",
        "Skeptic",
        "Goal steward",
        "Verifier",
        "Specialist",
        "Do not vote, average opinions",
        "Never silently substitute self-review",
        "wait briefly, harvest and close completed threads, then retry once",
    ],
    "workflows/verification.md": [
        "Verified",
        "Inferred",
        "Not checked",
        "Blocked",
        "fresh",
        "reviewer-backed",
    ],
    "instructions/operations.md": ["stall rule", "root-cause pass before retrying"],
}

FORBIDDEN_PATHS = {"examples", "rubrics", "scripts/check-agents-kit.py"}

FORBIDDEN_PHRASES = {
    "How To Use This Kit",
    "Adoption patterns",
    "optional companion skills",
    "copy the downstream starter",
}

FORBIDDEN_PATTERNS = {
    "private key header": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    "github token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "github fine-grained pat": re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    "aws access key id": re.compile(r"AKIA[0-9A-Z]{16}"),
    "slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    "generic secret assignment": re.compile(
        r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{24,}"
    ),
    "private unix home": re.compile(r"/home/[a-z][a-z0-9_-]{0,31}(?![A-Za-z0-9_-])"),
    "private macos home": re.compile(
        r"/Users/(?!Shared\b|Guest\b)[A-Za-z][A-Za-z0-9_-]{0,31}(?![A-Za-z0-9_-])"
    ),
    "private windows home": re.compile(
        r"(?i)[A-Za-z]:[\\/]+Users[\\/]+(?!Public\b|Default\b)[A-Za-z][A-Za-z0-9 ._-]{0,63}"
    ),
}

PATTERN_SELF_TESTS = [
    ("private key header", True, "-----BEGIN RSA PRIVATE" + " KEY-----"),
    ("github token", True, "ghp" + "_" + "a" * 24),
    ("github fine-grained pat", True, "github_pat" + "_" + "a" * 30),
    ("aws access key id", True, "AKIA" + "0" * 16),
    ("slack token", True, "xoxb" + "-" + "0" * 24),
    ("generic secret assignment", True, "api_key" + " = \"" + "A" * 30 + "\""),
    ("private unix home", True, "/home/" + "alice/project"),
    ("private unix home", False, "/home/" + "<username>/project"),
    ("private macos home", True, "/Users/" + "alice/project"),
    ("private macos home", False, "/Users/" + "Shared/media"),
    ("private windows home", True, "C:" + "\\Users\\" + "alice"),
    ("private windows home", False, "C:" + "\\Users\\" + "Public\\shared"),
]

TEXT_SUFFIXES = {
    ".bash",
    ".cfg",
    ".conf",
    ".ini",
    ".json",
    ".md",
    ".mdc",
    ".properties",
    ".ps1",
    ".psd1",
    ".psm1",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
SPECIAL_TEXT_NAMES = {".env", ".gitignore", "Dockerfile", "Makefile"}
FILE_SELECTION_SELF_TESTS = [
    ("policy.mdc", True),
    ("check.sh", True),
    ("check.bash", True),
    ("check.ps1", True),
    (".gitignore", True),
    (".env", True),
    (".env.example", True),
    ("asset.png", False),
]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        failures.append(f"{path.relative_to(ROOT).as_posix()}: not valid UTF-8")
        return ""


def is_scannable_name(path: Path) -> bool:
    return (
        path.suffix in TEXT_SUFFIXES
        or path.name in SPECIAL_TEXT_NAMES
        or path.name.startswith(".env.")
    )


def is_inside_root(path: Path) -> bool:
    try:
        path.relative_to(ROOT)
    except ValueError:
        return False
    return True


def missing_markers(text: str, markers: list[str]) -> list[str]:
    return [marker for marker in markers if marker not in text]


def check_local_links(path: Path, text: str, failures: list[str]) -> None:
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        resolved = (path.parent / target).resolve()
        rel = path.relative_to(ROOT).as_posix()
        if not is_inside_root(resolved):
            failures.append(f"{rel}: local link escapes repository: {raw_target}")
        elif not resolved.is_file():
            failures.append(f"{rel}: broken local link {raw_target}")


def main() -> int:
    failures: list[str] = []

    for name, expected, sample in PATTERN_SELF_TESTS:
        if bool(FORBIDDEN_PATTERNS[name].search(sample)) != expected:
            failures.append(f"privacy pattern self-test failed: {name}")

    for name, expected in FILE_SELECTION_SELF_TESTS:
        if is_scannable_name(Path(name)) != expected:
            failures.append(f"file-selection self-test failed: {name}")

    if missing_markers("required policy", ["required policy"]):
        failures.append("policy-marker positive self-test failed")
    if missing_markers("unrelated text", ["required policy"]) != ["required policy"]:
        failures.append("policy-marker negative self-test failed")
    if not is_inside_root(ROOT / "AGENTS.md") or is_inside_root(ROOT.parent / "private.md"):
        failures.append("repository-boundary self-test failed")

    for item in sorted(REQUIRED_FILES):
        if not (ROOT / item).is_file():
            failures.append(f"missing required file: {item}")

    for item in sorted(FORBIDDEN_PATHS):
        path = ROOT / item
        remains = path.is_file() or (path.is_dir() and any(child.is_file() for child in path.rglob("*")))
        if remains:
            failures.append(f"legacy generic-kit path must stay removed: {item}")

    root_path = ROOT / "AGENTS.md"
    root_text = read(root_path, failures) if root_path.is_file() else ""
    if root_text:
        lines = len(root_text.splitlines())
        words = len(root_text.split())
        size = len(root_text.encode("utf-8"))
        if lines > 90 or words > 900 or size > 7_000:
            failures.append(
                f"AGENTS.md exceeds entry-point budget: {lines} lines, {words} words, {size} bytes"
            )
        for route in sorted(ROOT_ROUTES):
            if route not in root_text:
                failures.append(f"AGENTS.md does not route to {route}")

    for item, markers in POLICY_SMOKE_MARKERS.items():
        path = ROOT / item
        if not path.is_file():
            continue
        text = read(path, failures)
        for marker in missing_markers(text, markers):
            failures.append(f"{item}: missing policy smoke marker: {marker}")

    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or ".git" in path.parts
            or not is_scannable_name(path)
        ):
            continue
        text = read(path, failures)
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix == ".md":
            check_local_links(path, text, failures)
            for phrase in FORBIDDEN_PHRASES:
                if phrase.lower() in text.lower():
                    failures.append(f"{rel}: obsolete adoption language: {phrase}")
        for name, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"{rel}: forbidden public-data pattern: {name}")

    if failures:
        print("AGENTS checks failed:\n", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"AGENTS checks passed ({len(REQUIRED_FILES)} core files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
