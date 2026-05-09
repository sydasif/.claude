#!/usr/bin/env bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

if [[ "$file_path" == *.py ]] && [[ -f "$file_path" ]]; then
  if ! command -v uv &>/dev/null; then
    echo "ruff-after-edit: uv not found, skipping ruff" >&2
    exit 0
  fi
  uv run ruff check --fix --quiet "$file_path" 2>/dev/null || \
    echo "ruff-after-edit: ruff check failed on $file_path" >&2
  uv run ruff format --quiet "$file_path" 2>/dev/null || \
    echo "ruff-after-edit: ruff format failed on $file_path" >&2
fi
exit 0