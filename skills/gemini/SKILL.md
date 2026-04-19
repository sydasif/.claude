---
name: gemini-research
description: Gemini CLI for web search, code analysis, and second opinions.
---

# Gemini CLI Reference

Use Gemini as a complementary tool for real-time info and code review.

## 1. Core Command (Headless)

```bash
gemini -p "PROMPT" --model <model> --output-format json | jq -r '.response'
```

## 2. Model Guide

| Model                           | Best For                                 | Note                           |
| :------------------------------ | :--------------------------------------- | :----------------------------- |
| `gemini-3.1-flash-lite-preview` | Web search, current events, fast queries | Default for research           |
| `gemini-3-flash-preview`        | Deep code analysis, complex reasoning    | Best for architecture/security |
| `gemini-2.5-flash`              | Stable, general-purpose reasoning        | Fallback                       |
| `gemini-2.5-flash-lite`         | Quick, simple tasks                      | Lowest latency                 |

## 3. Usage Patterns

- **Web Search**: `gemini -p "Latest React 19 features" --model gemini-3-flash-preview`
- **Single File**: `gemini -p "@src/main.ts Review for bugs" --model gemini-3-pro-preview`
- **Directory**: `gemini -p "@src/components/ Find code smells" --model gemini-3-pro-preview`
- **Multi-Path**: `gemini -p "@src/ @tests/ Analyze coverage" --model gemini-3-pro-preview`

## 4. Pipeline & Automation

- **Piping (stdin)**: Pipe data directly into Gemini as context.
  - `Read logs.txt | gemini -p "Find the root cause of the error"`
  - `LS -R | gemini -p "Analyze this project structure"`
- **Dynamic Context**: Pipe command output for real-time analysis.
  - `git diff --cached | gemini -p "Write a concise git commit message"`
- **Bulk Processing**: Use shell loops for batch tasks.
  - `for f in *.py; do Read "$f" | gemini -p "Generate docstring" > "$f.docs"; done`

## 5. Reliability & Error Handling

- **JSON Schema**: `{ "response": "...", "stats": {...}, "error": {...} }`
- **Exit Codes**:
  - `0`: Success
  - `1`: General/API Failure
  - `42`: Input Error (invalid prompt/args)
  - `53`: Turn Limit Exceeded
- **Best Practices**:
  - **Always** use `--output-format json` and `-p` for automation.
  - **Verify** `.error` field before trusting `.response`.
  - **Limit** `@` scopes to avoid context overflow.
