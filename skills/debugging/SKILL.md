---
name: debugging
description: Uses Gemini CLI to diagnose errors, analyze stack traces, and suggest code fixes.
---

# Code Debugging Assistant

Use Gemini CLI to isolate bugs, explain obscure error messages, and propose solutions.

## When to use

- **Error Analysis**
  - Parsing stack traces or crash logs
  - Explaining cryptic error messages or error codes
  - Debugging CI/CD failures

- **Logic & Behavior**
  - Code runs but produces incorrect results
  - Identifying race conditions or memory leaks
  - Performance bottlenecks in specific functions

- **Modernization**
  - Fixing deprecation warnings
  - migrating legacy code patterns

## Model Selection

- `gemini-3-pro-preview` - **Primary for debugging.** Best at logic, reasoning, and deep context.
- `gemini-2.5-pro` - **Fallback** for standard logic issues, if `gemini-3-pro-preview` is unavailable.
- `gemini-3-flash-preview` - Use for looking up specific error codes or latest API changes.

## Context Injection

Effective debugging requires context. Scope the prompt to relevant files.

```bash
# Specific file + Error message
gemini "@src/auth.ts Fix the 'Invalid Token' error in the login function"

# Directory scan for logic bugs
gemini "@src/utils/ Identify why dates are parsing incorrectly"

# Piping an error log (if file exists)
gemini "@error.log @src/main.ts Explain this crash"
```

## Common Commands

### 1. Fix Syntax or Logic Errors

Analyze a file and apply a fix for a specific issue.

```bash
gemini "@src/api.ts Fix the async/await deadlock in getUserData" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 2. Analyze Stack Traces

Paste the stack trace directly into the prompt to find the root cause.

```bash
gemini "@src/app.tsx Stack trace: 'TypeError: Cannot read properties of undefined' at line 42. Fix this." \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 3. Security & sanity check

Review code for vulnerabilities or bad practices before committing.

```bash
gemini "@src/db.ts Check for SQL injection vulnerabilities" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 4. Search for External Issues

If an error seems related to a library version or external service.

```bash
gemini "React 19 hydration error #418 workaround" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

## Debugging Workflow

1. **Isolate Context**: Identify the 1-3 files involved in the bug. Use `@path/to/file` to include them.
2. **Describe Symptom**: specific error message, unexpected behavior, or paste the log.
3. **Select Model**: Use `gemini-3-pro-preview` for deep logic, `flash` for external library errors.
4. **Execute**: Run with `--output-format json`.

## Quick Tips

- **Always include the error message**: "Fix this" is weak. "Fix the NullPointer at line 10" is strong.
- **Use JSON**: Always use `--output-format json` to ensure clean separation of reasoning and code blocks.
