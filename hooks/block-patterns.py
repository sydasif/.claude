#!/usr/bin/env python3
import json
import re
import sys

DANGEROUS_PATTERNS = [
    # Obfuscation & Remote Payloads
    r"(curl|wget).*\s+\|\s*(bash|sh|python|perl|php|ruby|node)",  # Pipe to shell
    r"base64\s+-[di].*\|\s*(bash|sh|python|perl|php)",  # Obfuscated execution
    # Reverse Shells & Persistence
    r"nc\s+.*-e\s+",  # Netcat reverse shell
    r"bash\s+-i\s+>&",  # Interactive bash reverse shell
    r"python.*\s+-c\s+.*import\s+socket",  # Python reverse shell
    # Command Injection & Chaining
    # Catches things like: ls ; rm -rf /
    r"[;&|]\s*(rm|sudo|curl|wget|nc|bash|sh|python|perl|chmod|chown|mkfs|dd)",
    # Nested Execution (Command Substitution)
    # Catches things like: ls $(whoami)
    r"\$\(.*\)",
    r"`.*`",
    # Denial of Service
    r":[()]{.*:\|:&.*};",  # Classic fork bomb
]

input_data = json.load(sys.stdin)
if input_data.get("tool_name") == "Bash":
    command = input_data.get("tool_input", {}).get("command", "")
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            print("BLOCKED: Dangerous pattern", file=sys.stderr)
            sys.exit(2)

sys.exit(0)
