#!/usr/bin/env python3

import json
import re
import sys

PIP_PATTERNS = [
    re.compile(r"(^|\s)pip\s+install(\s|$)"),
    re.compile(r"(^|\s)pip3\s+install(\s|$)"),
    re.compile(r"(^|\s)pipenv\s+install(\s|$)"),
    re.compile(r"(^|\s)python\s+-m\s+pip\s+install(\s|$)"),
    re.compile(r"(^|\s)python3\s+-m\s+pip\s+install(\s|$)"),
]


def detect_pip(command):
    if not command:
        return False
    return any(p.search(command) for p in PIP_PATTERNS)


def main():
    try:
        hook_input = sys.stdin.read().strip()
        if not hook_input:
            sys.exit(0)

        data = json.loads(hook_input)
        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})

        if tool_name not in ["Bash", "ExecuteCommand"]:
            sys.exit(0)

        command = tool_input.get("command", tool_input.get("cmd", ""))

        if not detect_pip(command):
            sys.exit(0)

        error_message = (
            "BLOCKED: Use `uv` instead of `pip`\n"
            "\n"
            "This project uses uv for package management. "
            "Replace pip commands with:\n"
            "\n"
            "  uv add <package>     # instead of pip install <package>\n"
            "  uv sync              # instead of pip install -r requirements.txt\n"
            "  uv remove <package>  # instead of pip uninstall <package>\n"
            "  uv pip install ...   # if you must use pip syntax within uv\n"
        )
        print(error_message, file=sys.stderr)
        sys.exit(2)

    except (json.JSONDecodeError, KeyError):
        sys.exit(0)


if __name__ == "__main__":
    main()
