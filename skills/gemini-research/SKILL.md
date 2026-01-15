---
name: gemini-research
description: Uses Gemini CLI for web search, code analysis, architectural reasoning, and real-time information. Use when the user needs current information, web search, code review, architecture advice, or a second opinion on implementation decisions.
---

# Research Assistant with Gemini CLI

This skill tells Claude when and how to use Gemini CLI as a complementary research and analysis tool.

## When to use this skill

Prefer Gemini CLI when any of the following are true:

- Web search or real-time information is required
  - Questions about current events, latest versions, releases, or recent changes
  - Queries with words like “latest”, “current”, “newest”, “2025”, “recent”, “today”
  - Requests for up‑to‑date best practices, standards, or comparisons

- A second AI perspective would be valuable
  - Code analysis, security reviews, or architecture decisions
  - Cross‑checking assumptions or verifying implementation approaches

- Deep research or documentation diving is needed
  - Understanding unfamiliar libraries, frameworks, or APIs
  - Investigating best practices, patterns, or trade‑offs

Treat Gemini CLI as a research assistant that:

- Performs web searches with Google Search integration
- Reads and analyzes code from a different AI perspective
- Provides architectural and implementation guidance
- Helps debug complex issues by exploring code and docs

## Command syntax

Basic format:

```bash
gemini "PROMPT" [FLAGS]
```

For anything automated or parsed, always use JSON output:

```bash
gemini "PROMPT" --output-format json
```

JSON response structure (main fields):

```json
{
  "response": "The actual answer to your prompt",
  "stats": {
    "models": { /* per‑model API & token usage */ },
    "tools":  { /* tool usage stats */ },
    "files":  { /* file modification stats */ }
  },
  "error": { /* only present if an error occurred */ }
}
```

Extract the answer and handle errors safely (bash pattern):

```bash
result=$(gemini -p "Your prompt" --output-format json)

if echo "$result" | jq -e '.error' > /dev/null 2>&1; then
  echo "Gemini error: $(echo "$result" | jq -r '.error.message')" >&2
  exit 1
fi

echo "$result" | jq -r '.response'
```

When available, use the helper script:

```bash
./scripts/run-gemini.sh "Your prompt" [EXTRA_GEMINI_ARGS...]
```

## Model selection

Choose a model appropriate for the task:

- `gemini-3-flash-preview`
  - Best for: web search, real‑time information, quick answers (default preference)
- `gemini-3-pro-preview`
  - Best for: deep code analysis, complex reasoning, architecture
- `gemini-2.5-pro`
  - Best for: stable fallback when preview models are unavailable or error
- `gemini-2.5-flash`
  - Best for: quick analysis, simple queries, lower latency
- `gemini-2.5-flash-lite`
  - Best for: very simple queries where speed/cost matter more than depth

Defaults:

- For web search or current information: prefer `gemini-3-flash-preview`.
- For deep code/architecture tasks: prefer `gemini-3-pro-preview` or `gemini-2.5-pro`.

## File and directory inclusion

In‑prompt `@` syntax:

- `"@src/main.ts"` — specific file
- `"@src/components/"` — entire directory
- `"@./"` — current directory and all subdirectories
- Combine multiple: `"@file1.js @src/ @tests/"`

Workspace scope flag:

```bash
--include-directories ./libs,./tests
```

Paths are relative to the current working directory. Use forward slashes consistently.

## Output handling

For automation:

- Always use `--output-format json`.
- Always:
  - Check `.error` and surface error messages
  - Extract `.response` for the actual answer
  - Use `.stats.models` and `.stats.tools` for usage tracking when useful

For long‑running operations or event‑driven use:

- Use `--output-format stream-json` and process JSONL events (init, message, tool_use, tool_result, error, result). See [reference.md](reference.md) for details.

## Common usage patterns

### Web search & current information

- Latest framework features or release notes
- Current best practices or security recommendations
- Version checking and comparisons
- Technology or tool comparisons

Example:

```bash
gemini "What are the latest features in React 19?" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### Code analysis

- Single file review (security, correctness, style)
- Architecture analysis for a module or codebase
- Code smell or refactoring opportunities across a directory

Example:

```bash
gemini "@src/auth.ts Review this authentication implementation for security issues" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Research & documentation

- API design guidance (pagination, filtering, error handling)
- Configuration and environment layout
- Debugging help (why this code might fail, leak, or stall)

Example:

```bash
gemini "@config/ How should I structure environment configuration for this setup?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Verification & second opinion

- Validate approach choices (caching, batching, retries)
- Security and performance audits
- Cross‑checking Claude’s analysis

Example:

```bash
gemini "@src/cache.ts Is this caching strategy appropriate for high-traffic scenarios?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Testing & quality

- Test coverage analysis and missing test suggestions
- Edge‑case brainstorms for utilities and APIs

Example:

```bash
gemini "@src/ @tests/ Analyze test coverage and suggest missing test cases" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Integration workflow

When the user asks a question:

1) Decide if web search or current information is needed
   - Look for keywords like “latest”, “current”, “newest”, “2025”, “recent”, “today”.
   - Questions about versions, releases, updates.
   - Requests for current best practices or standards.

2) For web search → use Gemini CLI immediately

   ```bash
   gemini "User's question" --model gemini-3-flash-preview --output-format json | jq -r '.response'
   ```

3) For code analysis → consider using Gemini CLI
   - As a primary tool for an alternative perspective.
   - As a verification step to validate Claude’s own analysis.
   - For comprehensive reviews where different models may catch different issues.

4) Present results clearly
   - Cite that information came from Gemini CLI + web search.
   - Include relevant URLs when Gemini provides them.
   - Summarize key findings and how they apply to the user’s codebase or situation.

## Important notes

- All `@` syntax paths are relative to the current working directory.
- For analysis tasks (no writes), you do not need `--yolo`; read‑only is sufficient.
- Always parse JSON output and use the `.response` field for the actual answer.
- Use Gemini CLI as a complement to Claude, not a wholesale replacement.
- Leverage Gemini’s built‑in Google Search integration for real‑time queries.
- Be mindful of context window: keep `@` scopes focused and avoid unnecessary duplication.
- Multiple perspectives (Claude + Gemini) are helpful for cross‑validation.

## Quick reference

- Web search (most common)

  ```bash
  gemini "search query" --model gemini-3-flash-preview --output-format json | jq -r '.response'
  ```

- Code analysis

  ```bash
  gemini "@path/to/code prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'
  ```

- Full codebase analysis

  ```bash
  gemini "@./ prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'
  ```

- Multiple paths

  ```bash
  gemini "@src/ @tests/ prompt" --model gemini-3-pro-preview --output-format json | jq -r '.response'
  ```

## Related docs in this skill

- [reference.md](reference.md) — detailed Gemini CLI headless reference (flags, output formats, JSON schema).
- [examples.md](examples.md) — concrete, copy‑pasteable scenarios and automation patterns.
- [scripts/run-gemini.sh](scripts/run-gemini.sh) — helper for safe JSON parsing and error handling.
