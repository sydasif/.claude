#!/usr/bin/env bash
# scripts/run-gemini.sh
#
# Helper script to call Gemini CLI in headless mode with JSON output,
# check for errors, and extract the response text.
#
# Usage:
#   ./scripts/run-gemini.sh "PROMPT" [EXTRA_GEMINI_ARGS...]
#
# Example:
#   ./scripts/run-gemini.sh "Explain this code" --model gemini-3-flash-preview

set -euo pipefail

prompt="$1"
shift

result=$(gemini -p "$prompt" --output-format json "$@")

if echo "$result" | jq -e '.error' > /dev/null 2>&1; then
  echo "Gemini error: $(echo "$result" | jq -r '.error.message')" >&2
  exit 1
fi

echo "$result" | jq -r '.response'
