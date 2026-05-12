#!/usr/bin/env python3

import json

import sys

from pathlib import Path


def main():

    try:
        # Read and parse the hook input from stdin

        hook_input = sys.stdin.read()

        data = json.loads(hook_input)

        # Get the file path from the tool input

        file_path_str = data.get("tool_input", {}).get("file_path", "")

        if not file_path_str:
            sys.exit(0)  # Nothing to check

        file_path = Path(file_path_str)

        # Define the list of sensitive file extensions

        sensitive_extensions = [
            ".env",
            ".pem",
            ".key",
            ".credential",
            ".token",
            ".p12",
            ".pfx",
            ".crt",
            ".cer",
            ".secret",
            ".config",
        ]

        # Check if the file path has a sensitive extension

        if file_path.suffix.lower() in sensitive_extensions:
            # This is a sensitive file, block the action

            # Construct a clear, helpful error message for Claude

            error_message = (
                f"SECURITY_POLICY_VIOLATION: Access to the sensitive file '{file_path.name}' is blocked. "
                f"Reason: Files with extensions like {', '.join(sensitive_extensions)} contain credentials and should not be accessed or modified by the AI. "
                "Please use environment variables or a secure secret management tool instead."
            )

            # Print the error message to stderr

            print(error_message, file=sys.stderr)

            # Exit with code 2 to block the action and feed the error to Claude

            sys.exit(2)

    except (json.JSONDecodeError, KeyError):
        # Fail silently if input is malformed

        sys.exit(0)

    # If no sensitive file is detected, exit with 0 to allow the action

    sys.exit(0)


if __name__ == "__main__":
    main()
