---
name: gemini
description: Gemini CLI for web search, code analysis, and second opinions.
---

# Gemini CLI Reference

Use Gemini as a complementary tool for real-time info and code review.

## 1. Basic Command Structure

```bash
gemini -p "PROMPT" --model <model> --output-format json
```

## 2. Model Selection

| Model                           | Best For                                 |
| :------------------------------ | :--------------------------------------- |
| `gemini-3-flash-preview`        | Deep code analysis, complex reasoning    |
| `gemini-3.1-flash-lite-preview` | Web search, current events, fast queries |
| `gemini-2.5-flash`              | Stable, general-purpose reasoning        |
| `gemini-2.5-flash-lite`         | Quick, simple tasks                      |

## 3. Usage Examples

- **Web Search**: `gemini -p "Latest React 19 features" --model gemini-3.1-flash-lite-preview`
- **Single File**: `gemini -p "@src/main.ts Review for bugs" --model gemini-3-flash-preview`
- **Directory**: `gemini -p "@src/components/ Find code smells" --model gemini-3-flash-preview`
- **Multi-Path**: `gemini -p "@src/ @tests/ Analyze coverage" --model gemini-3-flash-preview`


## 5. Reliability & Error Handling

- **Exit Codes**:
  - `0`: Success
  - `1`: General/API Failure
  - `42`: Input Error (invalid prompt/args)
  - `53`: Turn Limit Exceeded

> See [Gemini CLI docs](https://developers.google.com/gemini/docs/cli) for detailed usage and troubleshooting.