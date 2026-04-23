---
name: run-gemini
description: Use Gemini CLI for real-time info retrieval and code review.
---

# Gemini CLI

Use Gemini for real-time information and code analysis.

## Usage
`gemini -p "PROMPT" --model <MODEL> --output-format json`

## Models
- `gemini-3-flash-preview` (Deep analysis, complex reasoning)
- `gemini-3.1-flash-lite-preview` (Web search, fast queries)
- `gemini-2.5-flash` (Stable, general-purpose)
- `gemini-2.5-flash-lite` (Quick, simple tasks)

## Key Options
- `-m, --model <MODEL>`: Specify model
- `-o, --output-format <FORMAT>`: Output format (`text`, `json`, `stream-json`)
- `-s, --sandbox`: Run in sandbox mode
- `--approval-mode <MODE>`: Set approval mode (`default`, `auto_edit`, `yolo`, `plan`)
- `--include-directories <DIRS>`: Additional directories to include in the workspace

## Examples

### Information Retrieval
- `gemini -p "Latest React 19 features" --model gemini-3.1-flash-lite-preview`

### Code Analysis
- **Single File:** `gemini -p "@src/main.ts Review for bugs" --model gemini-3-flash-preview`
- **Directory:** `gemini -p "@src/components/ Find code smells" --model gemini-3-flash-preview`
- **Multi-Path:** `gemini -p "@src/ @tests/ Analyze coverage" --model gemini-3-flash-preview`

### Advanced Usage
- **Sandboxed Analysis:** `gemini -p "Review code" --sandbox --approval-mode plan`
- **With extra directories:** `gemini -p "Compare files" --include-directories "docs/,tests/"`

## Troubleshooting
- **Exit Codes:**
  - `0`: Success
  - `1`: API Failure
  - `42`: Input Error
  - `53`: Turn Limit Exceeded

*See [Gemini CLI docs](https://geminicli.com/docs/) for more.*
