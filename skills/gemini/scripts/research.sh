#!/usr/bin/env bash
set -euo pipefail

GEMINI_BIN="${GEMINI_BIN:-gemini}"
FLAGS="-o text --debug=false"

QUERY="$*"
if [ -z "$QUERY" ]; then
  echo "No query provided"
  exit 1
fi

PROMPT="
Act as a research assistant.
Search the internet on your own and provide factual findings.
Research query:
$QUERY
"

$GEMINI_BIN $FLAGS "$PROMPT" 2>/dev/null
