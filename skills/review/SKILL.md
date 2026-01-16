---
name: code-review
description: Uses Gemini CLI for deep code analysis, security auditing, refactoring suggestions, and test generation. Use for peer review automation and code quality checks
---

# Code Reviewer with Gemini CLI

Use Gemini CLI as an automated peer reviewer and static analysis tool.

## When to use

Use Gemini CLI for code review when:

- **Deep Analysis is required**
  - Finding subtle bugs, race conditions, or logic errors
  - Security auditing (OWASP top 10, injection risks)
  - Performance bottleneck identification

- **Refactoring & Modernization**
  - Converting legacy code to modern syntax (e.g., Java to Kotlin, JS to TS)
  - Improving readability and maintainability
  - reducing technical debt

- **Test Generation**
  - Generating unit tests for complex functions
  - Identifying edge cases missing in current test suites

## Basic usage

```bash
# Always use JSON output for parsing
gemini "PROMPT" --output-format json

# Review a specific file
gemini "@src/main.ts Review for logic errors" --output-format json

# Or use the helper script
./scripts/run-gemini.sh "@src/main.ts Review this code"
```

## Model selection

- `gemini-3-pro-preview` - **Primary for Code Review**. Best for deep reasoning, security, and complex architecture.
- `gemini-2.5-pro` - **Fallback** for general code analysis. If `gemini-3-pro-preview` is unavailable.
- `gemini-3-flash-preview` - Good for quick syntax checks or generating boilerplate tests.

## File inclusion

```bash
# Single file review
gemini "@src/auth.ts Review for security vulnerabilities"

# Compare/Contextual review
gemini "@src/types.d.ts @src/api.ts Ensure type safety between these files"

# Full module review
gemini "@src/modules/payment/ Analyze architecture and separation of concerns"
```

## Common patterns

### Security Audit

```bash
gemini "@src/db/query.ts Check for SQL injection and proper parameter sanitization" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Performance Analysis

```bash
gemini "@src/components/List.tsx Identify re-render issues and memory leaks" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Refactoring Suggestions

```bash
gemini "@src/legacy/utils.js Convert to TypeScript and apply functional patterns" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Test Generation

```bash
gemini "@src/lib/calc.ts Generate Vitest test cases including edge cases" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

## Workflow

1. **Select Scope**
   - Identify the specific file(s) or directory needing review.
   - *Tip: Don't dump the whole repo; focus on the modified module.*

2. **Define the Goal**
   - Are you looking for *bugs*, *security flaws*, *style issues*, or *tests*?
   - Be specific in the prompt.

3. **Execute Review**

   ```bash
   gemini "@path/to/code Review prompt" --model gemini-3-pro-preview --output-format json
   ```

4. **Process Output**
   - The output will often contain markdown. Pipe to a viewer or save to a PR comment draft.

## Key points

- **Context Matters**: Include interface/type definitions (`@types.ts`) if reviewing code that depends on them.
- **Model Choice**: Always use `gemini-3-pro-preview` for security or logic reviews; it has significantly better reasoning capabilities.
- **Output**: Use `--output-format json` to handle special characters in code blocks safely.

## Quick reference

```bash
# Security Check
gemini "@file Audit for security" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Optimization
gemini "@file Optimize performance" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Unit Tests
gemini "@file Write tests" --model gemini-3-flash-preview --output-format json | jq -r '.response'
```
