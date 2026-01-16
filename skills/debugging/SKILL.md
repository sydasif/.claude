---
name: debugging
description: Uses Gemini CLI to diagnose errors, analyze stack traces, explain cryptic error messages, and suggest code fixes. Use when encountering runtime errors, test failures, logic bugs, or performance issues.
---

# Code Debugging Assistant

Use Gemini CLI to isolate bugs, explain obscure error messages, diagnose logic issues, and propose targeted solutions.

## When to Use This Skill

Use this skill for debugging when you need:

### Error Analysis

- Parsing and interpreting stack traces or crash logs
- Explaining cryptic error messages or error codes
- Diagnosing CI/CD pipeline failures
- Understanding framework-specific errors

### Logic & Behavior Issues

- Code runs but produces incorrect results
- Identifying race conditions or concurrency bugs
- Tracing memory leaks or resource exhaustion
- Diagnosing performance bottlenecks in specific functions

### Code Quality Issues

- Fixing deprecation warnings
- Migrating legacy code patterns
- Resolving type errors or compilation issues
- Security vulnerability analysis

## Model Selection

Choose the appropriate model based on debugging complexity:

- **`gemini-3-pro-preview`** - Primary choice for debugging. Best for deep logic analysis, complex reasoning, and understanding subtle bugs
- **`gemini-2.5-pro`** - Fallback for standard logic issues if `gemini-3-pro-preview` is unavailable
- **`gemini-3-flash-preview`** - Use for quick lookups of specific error codes or checking latest API changes

## Context Injection

Effective debugging requires proper context. Scope your prompt to include only relevant files and error information.

### Single File with Error Message

```bash
gemini "@src/auth.ts Fix the 'Invalid Token' error in the login function" \
  --model gemini-3-pro-preview --output-format json
```

### Directory Scan for Logic Bugs

```bash
gemini "@src/utils/ Identify why dates are parsing incorrectly" \
  --model gemini-3-pro-preview --output-format json
```

### Stack Trace Analysis

```bash
gemini "@error.log @src/main.ts Explain this crash and suggest a fix" \
  --model gemini-3-pro-preview --output-format json
```

### Multiple Related Files

```bash
gemini "@src/types.ts @src/api.ts Fix the type mismatch error at line 42" \
  --model gemini-3-pro-preview --output-format json
```

## Common Debugging Commands

### 1. Fix Syntax or Logic Errors

Analyze a file and get a fix for a specific issue:

```bash
gemini "@src/api.ts Fix the async/await deadlock in getUserData" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 2. Analyze Stack Traces

Paste the stack trace directly into the prompt to find the root cause:

```bash
gemini "@src/app.tsx Stack trace: 'TypeError: Cannot read properties of undefined' at line 42. Explain the root cause and fix." \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 3. Security & Vulnerability Check

Review code for security issues before committing:

```bash
gemini "@src/db.ts Check for SQL injection vulnerabilities and suggest fixes" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 4. Performance Bottleneck Analysis

Identify performance issues in specific code sections:

```bash
gemini "@src/components/List.tsx Find performance bottlenecks causing slow renders" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### 5. Explain Cryptic Errors

Get detailed explanations of confusing error messages:

```bash
gemini "Explain this error: 'ECONNREFUSED 127.0.0.1:5432' in a Node.js PostgreSQL app" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

## Debugging Workflow

Follow this systematic approach for effective debugging:

### 1. Isolate Context

Identify the 1-3 files involved in the bug. Use `@path/to/file` syntax to include them in your prompt.

### 2. Describe the Symptom

Be specific about:

- The exact error message (not just "it doesn't work")
- The expected vs actual behavior
- Relevant log output or stack traces
- Steps to reproduce

### 3. Select the Right Model

- Use `gemini-3-pro-preview` for complex logic, subtle bugs, or security issues
- Use `gemini-3-flash-preview` for quick error code lookups or API documentation

### 4. Execute with JSON Output

Always use `--output-format json` to ensure clean separation of analysis and code suggestions:

```bash
gemini "@file.ts Your debugging prompt" \
  --model gemini-3-pro-preview \
  --output-format json | jq -r '.response'
```

### 5. Parse and Apply

Extract the suggested fix from the JSON response and apply it carefully, testing thoroughly.

## Output Processing

The JSON response contains the debugging analysis in the `.response` field:

```bash
# Extract just the debugging advice
gemini "@file.ts Debug this" --output-format json | jq -r '.response'

# Save analysis to file for reference
gemini "@file.ts Debug this" --output-format json | jq -r '.response' > debug-analysis.md

# Chain with further analysis
gemini "@file.ts Debug this" --output-format json | jq -r '.response' | \
  gemini "Simplify this fix for a junior developer" --output-format json
```

## Quick Tips for Effective Debugging

### Be Specific

- **Weak**: "Fix this"
- **Strong**: "Fix the NullPointerException at line 10 when user input is empty"

### Include Context

- Always provide the error message
- Include relevant stack traces
- Mention recent changes if applicable
- Note the runtime environment (Node version, browser, etc.)

### Use JSON Output

Always use `--output-format json` to:

- Ensure clean separation of reasoning and code blocks
- Enable reliable parsing and automation
- Handle special characters safely

### Iterate When Needed

If the first analysis doesn't solve the issue:

- Provide the attempted fix and new error
- Include additional context or related files
- Ask for alternative approaches

## Quick Reference

```bash
# Stack Trace Analysis
gemini "@file.ts @stack.log Analyze this crash" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Logic Error Fix
gemini "@src/calc.ts Fix incorrect calculation at line 23" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Security Audit
gemini "@src/auth.ts Check for authentication vulnerabilities" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Performance Debug
gemini "@src/query.ts Why is this database query slow?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Error Explanation
gemini "Explain error: CORS policy blocked fetch request" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

## Best Practices

- **Always specify the model explicitly** for consistent results
- **Use JSON output format** for reliable automation and parsing
- **Be very specific** about the error, including exact messages and line numbers
- **Include relevant files** using `@path/to/file` syntax
- **Provide context** about recent changes or environmental factors
- **Iterate systematically** if the first attempt doesn't solve the issue
- **Test fixes thoroughly** before considering the issue resolved
- **Save analysis** for documentation or team reference
