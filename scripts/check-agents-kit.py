#!/usr/bin/env python3
"""Static checks for the AGENTS instruction kit."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "instructions/coding.md",
    "instructions/review.md",
    "instructions/research.md",
    "instructions/personal-assistant.md",
    "instructions/ops-and-automation.md",
    "instructions/security-and-privacy.md",
    "instructions/skills-and-harnesses.md",
    "instructions/computer-use.md",
    "workflows/generate-evaluate-repair.md",
    "workflows/verification.md",
    "workflows/subagents.md",
    "workflows/handoff-and-state.md",
    "workflows/repository-docs.md",
    "workflows/review-and-roast.md",
    "rubrics/code-review.md",
    "rubrics/agent-harness-eval.md",
    "rubrics/plan-quality.md",
    "rubrics/security-safety.md",
    "rubrics/research-signal.md",
    "templates/AGENTS.md",
    "templates/CONTEXT.md",
    "templates/STYLE.md",
    "templates/HANDOFF.md",
    "templates/PLAN.md",
    "templates/REVIEW.md",
    "examples/minimal-repo/AGENTS.md",
    "examples/software-project/AGENTS.md",
    "examples/software-project/CONTEXT.md",
    "examples/software-project/STYLE.md",
    "examples/assistant-ops-repo/AGENTS.md",
    "examples/assistant-ops-repo/CONTEXT.md",
    "examples/assistant-ops-repo/STYLE.md",
]

ROOT_LINKS = [
    "instructions/coding.md",
    "instructions/review.md",
    "instructions/research.md",
    "instructions/personal-assistant.md",
    "instructions/ops-and-automation.md",
    "instructions/security-and-privacy.md",
    "instructions/skills-and-harnesses.md",
    "instructions/computer-use.md",
    "workflows/generate-evaluate-repair.md",
    "workflows/verification.md",
    "workflows/subagents.md",
    "workflows/handoff-and-state.md",
    "workflows/repository-docs.md",
    "workflows/review-and-roast.md",
    "rubrics/code-review.md",
    "rubrics/agent-harness-eval.md",
    "rubrics/plan-quality.md",
    "rubrics/research-signal.md",
    "rubrics/security-safety.md",
]

EXPECTED_REFERENCES = {
    "README.md": [
        "templates/AGENTS.md",
        "templates/CONTEXT.md",
        "templates/STYLE.md",
                    ],
    "examples/assistant-ops-repo/AGENTS.md": [
        "../../instructions/personal-assistant.md",
        "../../instructions/ops-and-automation.md",
        "../../instructions/security-and-privacy.md",
        "../../rubrics/agent-harness-eval.md",
    ],
}

FORBIDDEN_PATTERNS = {
    "private key header": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    "github token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    "generic api key assignment": re.compile(
        r"(?i)(api[_-]?key|token|secret|password)\s*=\s*['\"]?[A-Za-z0-9_./+-]{24,}"
    ),
    "private unix home path": re.compile(r"/home/[a-z][a-z0-9_-]{0,31}/"),
    "private macos home path": re.compile(r"/Users/[A-Za-z][A-Za-z0-9_-]{0,31}/"),
}

ALLOWED_PRIVATE_WORD_FILES = {
    "examples/assistant-ops-repo/AGENTS.md",
    "examples/assistant-ops-repo/CONTEXT.md",
    "examples/assistant-ops-repo/STYLE.md",
    "instructions/personal-assistant.md",
}

PRIVATE_NAME_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(name) for name in ["I" + "an", "K" + "im", "Sh" + "im"]) + r")\b"
)

TEXT_SUFFIXES = {
    ".md",
    ".mdc",
    ".py",
    ".sh",
    ".bash",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".txt",
    ".gitignore",
}


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_text_file(path: Path) -> bool:
    if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
        return False
    return path.suffix in TEXT_SUFFIXES or path.name in {"AGENTS.md", ".gitignore"}


def read_text(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{rel(path)}: expected text file is not valid UTF-8", failures)
        return ""


def main() -> int:
    failures: list[str] = []

    for item in REQUIRED_FILES:
        if not (ROOT / item).is_file():
            fail(f"missing required file: {item}", failures)

    root_path = ROOT / "AGENTS.md"
    root_text = read_text(root_path, failures) if root_path.is_file() else ""
    if root_text:
        for item in ROOT_LINKS:
            if item not in root_text:
                fail(f"AGENTS.md does not reference {item}", failures)

        line_count = len(root_text.splitlines())
        if line_count > 180:
            fail(f"AGENTS.md is too long for an entry point ({line_count} lines > 180)", failures)

    for path in ROOT.rglob("*"):
        if not is_text_file(path):
            continue
        item = rel(path)
        text = read_text(path, failures)
        for name, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                fail(f"{item}: forbidden pattern detected ({name})", failures)
        if item not in ALLOWED_PRIVATE_WORD_FILES and PRIVATE_NAME_PATTERN.search(text):
            fail(f"{item}: contains private/example-specific name outside allowed assistant examples", failures)

    for item, references in EXPECTED_REFERENCES.items():
        path = ROOT / item
        if not path.is_file():
            continue
        text = read_text(path, failures)
        for reference in references:
            if reference not in text:
                fail(f"{item}: missing expected reference {reference}", failures)
            elif not (path.parent / reference).resolve().is_file():
                fail(f"{item}: reference does not resolve: {reference}", failures)

    if failures:
        print("AGENTS kit checks failed:\n", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print(f"AGENTS kit checks passed ({len(REQUIRED_FILES)} required files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
