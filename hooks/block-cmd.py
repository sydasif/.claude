#!/usr/bin/env python3
import json
import re
import sys

DANGEROUS_PATTERNS = [
    r"\brm\s+.*-[a-z]*r[a-z]*f",
    r"sudo\s+rm",
    r"chmod\s+777",
    r"git\s+push\s+--force.*main",
]

input_data = json.load(sys.stdin)
if input_data.get("tool_name") == "Bash":
    command = input_data.get("tool_input", {}).get("command", "")
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            print("BLOCKED: Dangerous pattern", file=sys.stderr)
            sys.exit(2)

sys.exit(0)
