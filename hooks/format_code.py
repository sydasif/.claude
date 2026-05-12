#!/usr/bin/env python3

import os
import sys
import subprocess
import json
from pathlib import Path


def get_file_extension(file_path):
    """Get the file extension from a file path."""
    return Path(file_path).suffix.lower()


def format_python(file_path):
    """Format Python files using ruff."""
    try:
        subprocess.run(["ruff", "format", file_path], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def format_rust(file_path):
    """Format Rust files using rustfmt."""
    try:
        subprocess.run(["rustfmt", file_path], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def format_go(file_path):
    """Format Go files using gofmt."""
    try:
        subprocess.run(["gofmt", "-w", file_path], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def format_javascript_typescript(file_path):
    """Format JS/TS files using prettier if available, fallback to built-in tools."""
    # Try prettier first
    try:
        subprocess.run(
            ["prettier", "--write", file_path], check=True, capture_output=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Fallback to eslint --fix if available
    try:
        subprocess.run(["eslint", "--fix", file_path], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def should_format_file(file_path, tool_name):
    """Check if file should be formatted based on tool name."""
    if not os.path.exists(file_path):
        return False
    # Only format if the file was actually modified by Write, Edit, or MultiEdit tools
    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        return False
    return True


def main():
    """Main formatting function."""
    # Read tool data from stdin
    hook_input = sys.stdin.read().strip()
    if not hook_input:
        sys.exit(0)

    try:
        hook_data = json.loads(hook_input)
        tool_name = hook_data.get("tool_name", "")
        tool_input = hook_data.get("tool_input", {})
        file_path = tool_input.get("file_path")

        if not file_path or not should_format_file(file_path, tool_name):
            sys.exit(0)

        extension = get_file_extension(file_path)
        formatted = False
        if extension == ".py":
            formatted = format_python(file_path)
        elif extension == ".rs":
            formatted = format_rust(file_path)
        elif extension == ".go":
            formatted = format_go(file_path)
        elif extension in [".js", ".ts", ".jsx", ".tsx"]:
            formatted = format_javascript_typescript(file_path)

        if formatted:
            print(f"Formatted {file_path}")
    except (json.JSONDecodeError, KeyError):
        # Silently ignore if we can't parse tool args
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
