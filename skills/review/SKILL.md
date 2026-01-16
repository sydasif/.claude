---
name: review
description: Uses for code analysis, security auditing, refactoring suggestions, and test generation as peer review automation, finding subtle bugs, security vulnerabilities, and for code quality analysis.
---

# Code Review with Gemini CLI

This skill provides automated peer review and deep code analysis using Gemini CLI, acting as an AI-powered static analysis tool.

## When to Use This Skill

Use this skill for code review when you need:

### Analysis

- Finding subtle bugs, race conditions, or logic errors
- Security auditing (OWASP top 10, injection risks, authentication flaws)
- Performance bottleneck identification
- Complex algorithm analysis

### Refactoring

- Converting legacy code to modern syntax (e.g., Java to Kotlin, JS to TypeScript)
- Improving readability and maintainability
- Reducing technical debt
- Applying design patterns

## Basic Usage

Always use JSON output format for reliable parsing:

```bash
gemini "PROMPT" --output-format json
```

Review a specific file:

```bash
gemini "@src/main.ts Review for logic errors" --output-format json
```

## Model Selection

Choose the appropriate model based on your needs:

- **`gemini-3-pro-preview`** - Primary choice for code review. Best for deep reasoning, security analysis, and complex architecture review
- **`gemini-2.5-pro`** - Fallback for general code analysis if `gemini-3-pro-preview` is unavailable
- **`gemini-3-flash-preview`** - Good for quick syntax checks or generating boilerplate tests

## File Inclusion Patterns

### Single File Review

```bash
gemini "@src/auth.ts Review for security vulnerabilities" --output-format json
```

### Contextual Review (Multiple Files)

```bash
gemini "@src/types.d.ts @src/api.ts Ensure type safety between these files" --output-format json
```

### Full Module Review

```bash
gemini "@src/modules/payment/ Analyze architecture and separation of concerns" --output-format json
```

## Common Review Patterns

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

## Review Workflow

1. **Select Scope**
   - Identify the specific file(s) or directory needing review
   - Focus on modified modules rather than entire repository
   - Use `git diff` to identify recently changed files

2. **Define the Goal**
   - Be specific: bugs, security flaws, style issues, or tests?
   - Include requirements in your prompt

3. **Execute Review**

   ```bash
   gemini "@path/to/code Review prompt" --model gemini-3-pro-preview --output-format json
   ```

4. **Process Output**
   - Parse JSON response
   - Extract findings using `jq` or similar tools
   - Format for presentation or PR comments

## Key Principles

- **Context Matters**: Include interface/type definitions (`@types.ts`) when reviewing code that depends on them
- **Model Choice**: Always use `gemini-3-pro-preview` for security or complex logic reviews due to superior reasoning capabilities
- **Output Format**: Use `--output-format json` to handle special characters in code blocks safely and enable reliable parsing
- **Focused Reviews**: Don't dump entire repositories; focus on the modified module or component

## Output Processing

The JSON response contains the review in the `.response` field. Extract and format as needed:

```bash
# Extract just the review text
gemini "@file.ts Review code" --output-format json | jq -r '.response'

# Save to file for PR comment
gemini "@file.ts Review code" --output-format json | jq -r '.response' > review.md
```

## Quick Reference

```bash
# Security Check
gemini "@file Audit for security" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Performance Optimization
gemini "@file Optimize performance" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Generate Unit Tests
gemini "@file Write tests" --model gemini-3-flash-preview --output-format json | jq -r '.response'

# Type Safety Check
gemini "@types.ts @impl.ts Check type consistency" --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Best Practices

- Always specify the model explicitly for consistency
- Use JSON output format for reliable automation
- Include relevant context files (types, interfaces, schemas)
- Be specific about what you're looking for in the review
- Process output through `jq` for clean extraction
- Consider saving results for documentation or PR comments
