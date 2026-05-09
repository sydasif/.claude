#!/usr/bin/env bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

if [[ "$file_path" != *.py ]] && [[ -f "$file_path" ]]; then
  if ! command -v npx &>/dev/null; then
    echo "prettier-after-edit: npx not found, skipping prettier" >&2
    exit 0
  fi
  npx prettier --write "$file_path" 2>/dev/null || \
    echo "prettier-after-edit: prettier failed on $file_path" >&2
fi
exit 0