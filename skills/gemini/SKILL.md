---
name: research-with-gemini
description: Use Gemini CLI for web search, code analysis, architectural reasoning, and accessing real-time information. Complements Claude's capabilities with Google Search integration and alternative analysis perspective.
---

# Research Assistant with Gemini CLI

## When to Use This Skill

Gemini CLI is a **complementary tool** that you should use when:

### Primary Use Cases

- **Web search needed**: User asks about current events, latest versions, real-time data, or anything requiring up-to-date information
- **Alternative perspective**: Getting a second opinion on code analysis or architecture decisions
- **Specific research**: Deep-diving into documentation, best practices, or technical specifications
- **Verification**: Cross-checking assumptions or validating implementation approaches
- **Comparative analysis**: Understanding industry standards or comparing different approaches

### Think of Gemini As

A research assistant that can:

- Search the web for current information
- Analyze code from a different AI perspective
- Access Google Search directly for real-time data
- Provide architectural insights
- Help with debugging complex issues

## Command Syntax

Basic format: `gemini "PROMPT" [FLAGS]`

### File & Directory Inclusion

**In-prompt syntax (`@`):**

- `"@src/main.ts"` - Specific file
- `"@src/components/"` - Entire directory
- `"@./"` - Current directory and all subdirectories
- Can combine multiple: `"@file1.js @src/ @tests/"`

**Workspace scope flag:**

```bash
--include-directories ./libs,./tests
```

### Output Format (IMPORTANT)

**Always use JSON output for reliable parsing:**

```bash
gemini "PROMPT" --output-format json
```

The JSON response structure:

```json
{
  "response": "The actual answer to your prompt",
  "stats": { /* usage statistics */ },
  "error": { /* only present if error occurred */ }
}
```

**Extract the response:**

```bash
result=$(gemini "PROMPT" --output-format json)
echo "$result" | jq -r '.response'
```

## Model Selection

Choose the right model for the task:

| Model | Best For | Flag |
|-------|----------|------|
| `gemini-3-flash-preview` | **Web search, real-time info (DEFAULT)** | `--model gemini-3-flash-preview` |
| `gemini-3-pro-preview` | Deep code analysis, complex reasoning | `--model gemini-3-pro-preview` |
| `gemini-2.5-pro` | Stable fallback if previews error | `--model gemini-2.5-pro` |
| `gemini-2.5-flash` | Quick analysis, simple queries | `--model gemini-2.5-flash` |
| `gemini-2.5-flash-lite` | Very simple queries | `--model gemini-2.5-flash-lite` |

**Default recommendation**: Use `gemini-3-flash-preview` for most queries, especially web search.

## Common Usage Patterns

### 1. Web Search & Current Information

```bash
# Latest framework info
gemini "What are the latest features in React 19?" --model gemini-3-flash-preview --output-format json

# Current best practices
gemini "Current best practices for securing Node.js APIs in 2025" --model gemini-3-flash-preview --output-format json

# Package version checking
gemini "What is the latest stable version of TypeScript and what are the new features?" --model gemini-3-flash-preview --output-format json

# Technology comparisons
gemini "Compare Vite vs Webpack in 2025" --model gemini-3-flash-preview --output-format json
```

### 2. Code Analysis

```bash
# Single file review
gemini "@src/auth.ts Review this authentication implementation for security issues" --model gemini-3-pro-preview --output-format json

# Architecture analysis
gemini "@src/ Analyze the overall architecture and suggest improvements" --model gemini-3-pro-preview --output-format json

# Code quality check
gemini "@components/ Identify code smells and suggest refactoring opportunities" --model gemini-3-pro-preview --output-format json
```

### 3. Research & Documentation

```bash
# API best practices
gemini "Best practices for designing RESTful APIs with pagination and filtering" --model gemini-3-flash-preview --output-format json

# Implementation guidance
gemini "@config/ How should I structure environment configuration for this setup?" --model gemini-3-pro-preview --output-format json

# Debugging help
gemini "@src/database.js Why might this connection pooling cause memory leaks?" --model gemini-3-pro-preview --output-format json
```

### 4. Verification & Second Opinion

```bash
# Verify approach
gemini "@src/cache.ts Is this caching strategy appropriate for high-traffic scenarios?" --model gemini-3-pro-preview --output-format json

# Security review
gemini "@src/api/ Check for common security vulnerabilities" --model gemini-3-pro-preview --output-format json

# Performance analysis
gemini "@src/processing/ Identify performance bottlenecks in this data processing pipeline" --model gemini-3-pro-preview --output-format json
```

### 5. Testing & Quality

```bash
# Test coverage
gemini "@src/ @tests/ Analyze test coverage and suggest missing test cases" --model gemini-3-pro-preview --output-format json

# Test generation ideas
gemini "@src/utils.ts Suggest edge cases to test for these utility functions" --model gemini-3-pro-preview --output-format json
```

## Processing Gemini's Output

### Extract Response

```bash
result=$(gemini "Your prompt" --output-format json)
response=$(echo "$result" | jq -r '.response')
echo "$response"
```

### Check for Errors

```bash
if echo "$result" | jq -e '.error' > /dev/null 2>&1; then
    error_msg=$(echo "$result" | jq -r '.error.message')
    echo "Gemini error: $error_msg"
else
    echo "$result" | jq -r '.response'
fi
```

### Get Usage Statistics

```bash
total_tokens=$(echo "$result" | jq -r '.stats.models | to_entries | map(.value.tokens.total) | add // 0')
echo "Used $total_tokens tokens"
```

## Integration Workflow

### When User Asks a Question

1. **Identify if web search needed**:
   - Keywords: "latest", "current", "newest", "2025", "recent", "today"
   - Questions about versions, releases, updates
   - Requests for current best practices or standards

2. **For web search → Use Gemini immediately**:

   ```bash
   gemini "User's question" --model gemini-3-flash-preview --output-format json | jq -r '.response'
   ```

3. **For code analysis → Consider using Gemini**:
   - As primary tool: For alternative perspective
   - As verification: To validate Claude's analysis
   - For comprehensive review: Different AI might catch different issues

4. **Present results clearly**:
   - Always cite that information came from Gemini + web search
   - Include relevant URLs if Gemini found them
   - Summarize key findings

## Examples by Scenario

### User: "What's new in Next.js 15?"

```bash
gemini "What are the new features and changes in Next.js 15?" --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### User: "Review this authentication code"

```bash
# Option 1: Use Gemini for review
gemini "@src/auth.ts Review for security vulnerabilities and best practices" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Option 2: Use both Claude + Gemini for comprehensive review
# (Claude does initial review, then verify with Gemini)
```

### User: "How should I implement caching here?"

```bash
# Get current best practices
gemini "Best practices for implementing caching in Node.js applications 2025" --model gemini-3-flash-preview --output-format json | jq -r '.response'

# Then analyze their specific code
gemini "@src/api/ Given this API structure, suggest appropriate caching strategy" --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### User: "Is this React pattern still recommended?"

```bash
gemini "@src/components/UserList.tsx Is this React pattern still considered best practice in 2025?" --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### User: "Find performance issues in my code"

```bash
gemini "@src/ Analyze for performance bottlenecks and optimization opportunities" --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Important Notes

- **Paths are relative**: All `@` syntax paths are relative to current working directory
- **Read-only analysis**: No `--yolo` flag needed for analysis tasks
- **Always parse JSON**: Extract `.response` field for the actual answer
- **Combine with Claude**: Use Gemini as complement, not replacement
- **Web search advantage**: Gemini has direct Google Search integration
- **Context window**: Gemini can handle large codebases in single context
- **Multiple perspectives**: Different AI models catch different issues

## Quick Reference

```bash
# Web search (most common)
gemini "search query" --model gemini-3-flash-preview --output-format json | jq -r '.response'

# Code analysis
gemini "@path/to/code prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Full codebase analysis
gemini "@./ prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'

# Multiple paths
gemini "@src/ @tests/ prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## For More Information

Run `gemini --help` for full CLI reference or see [reference.md](reference.md) for complete documentation.
