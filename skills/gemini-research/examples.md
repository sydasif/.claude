# Gemini CLI Examples – Research & Automation

This file contains concrete, copy‑pasteable examples of using Gemini CLI in common workflows. For background on headless mode and flags, see [reference.md](reference.md). For when Claude should use Gemini, see [SKILL.md](SKILL.md).

In these examples:

- `--output-format json` is used by default for automation‑friendly output.
- `jq` extracts `.response` for the actual answer.
- Where relevant, `stats` are shown for tracking usage.

## Web search & current information

### Latest framework features

Latest features in React 19:

```bash
gemini "What are the new features and changes in React 19?" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

Current best practices for securing Node.js APIs in 2025:

```bash
gemini "Current best practices for securing Node.js APIs in 2025" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### Version checking

Latest stable TypeScript version and new features:

```bash
gemini "What is the latest stable version of TypeScript and what are the new features?" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### Technology comparisons

Vite vs Webpack in 2025:

```bash
gemini "Compare Vite vs Webpack in 2025" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

## Code analysis

### Single file security review

Review authentication code for security issues:

```bash
gemini "@src/auth.ts Review this authentication implementation for security issues and best practices" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Architecture review

Analyze the overall architecture of `src/`:

```bash
gemini "@src/ Analyze the overall architecture and suggest improvements" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Code quality & smells

Identify code smells and refactoring opportunities in `components/`:

```bash
gemini "@components/ Identify code smells and suggest refactoring opportunities" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Research & documentation

### API design best practices

Best practices for designing RESTful APIs with pagination and filtering:

```bash
gemini "Best practices for designing RESTful APIs with pagination and filtering" \
  --model gemini-3-flash-preview --output-format json | jq -r '.response'
```

### Configuration guidance

Suggest environment configuration structure:

```bash
gemini "@config/ How should I structure environment configuration for this setup?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Debugging help

Debug a potential memory leak in connection pooling:

```bash
gemini "@src/database.js Why might this connection pooling cause memory leaks?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Verification & second opinion

### Validate caching strategy

Check if a caching strategy is suitable for high traffic:

```bash
gemini "@src/cache.ts Is this caching strategy appropriate for high-traffic scenarios?" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Security review for an API surface

Check for common security vulnerabilities:

```bash
gemini "@src/api/ Check for common security vulnerabilities" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Performance bottlenecks

Identify performance bottlenecks in a data processing pipeline:

```bash
gemini "@src/processing/ Identify performance bottlenecks and optimization opportunities" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Testing & quality

### Test coverage analysis

Analyze test coverage for `src/` and `tests/`:

```bash
gemini "@src/ @tests/ Analyze test coverage and suggest missing test cases" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

### Edge‑case suggestions

Suggest edge cases to test for utility functions:

```bash
gemini "@src/utils.ts Suggest edge cases to test for these utility functions" \
  --model gemini-3-pro-preview --output-format json | jq -r '.response'
```

## Automation / CI patterns

### Code review (from a single file)

```bash
cat src/auth.py | gemini -p "Review this authentication code for security issues" \
  --output-format json | jq -r '.response' > security-review.txt
```

### Generate commit messages

```bash
result=$(git diff --cached | gemini -p "Write a concise commit message for these changes" --output-format json)
echo "$result" | jq -r '.response'
```

### API documentation: generate OpenAPI spec

```bash
result=$(cat api/routes.js | gemini -p "Generate OpenAPI spec for these routes" --output-format json)
echo "$result" | jq -r '.response' > openapi.json
```

### Batch code analysis

Analyze each Python file in `src/`:

```bash
mkdir -p reports
for file in src/*.py; do
  echo "Analyzing $file..."
  result=$(cat "$file" | gemini -p "Find potential bugs and suggest improvements" --output-format json)
  echo "$result" | jq -r '.response' > "reports/$(basename "$file").analysis"
  echo "Completed analysis for $(basename "$file")" >> reports/progress.log
done
```

### PR review from a diff

```bash
result=$(git diff origin/main...HEAD | gemini -p "Review these changes for bugs, security issues, and code quality" --output-format json)
echo "$result" | jq -r '.response' > pr-review.json
```

### Log analysis

```bash
grep "ERROR" /var/log/app.log | tail -20 | gemini -p "Analyze these errors and suggest root cause and fixes" > error-analysis.txt
```

### Release notes generation

```bash
result=$(git log --oneline v1.0.0..HEAD | gemini -p "Generate release notes from these commits" --output-format json)
response=$(echo "$result" | jq -r '.response')
echo "$response"
echo "$response" >> CHANGELOG.md
```

## Model & tool usage tracking

Track tokens, tool calls, and models used for a schema explanation:

```bash
result=$(gemini -p "Explain this database schema" --include-directories db --output-format json)

total_tokens=$(echo "$result" | jq -r '.stats.models // {} | to_entries | map(.value.tokens.total) | add // 0')
models_used=$(echo "$result" | jq -r '.stats.models // {} | keys | join(", ") | if . == "" then "none" else . end')
tool_calls=$(echo "$result" | jq -r '.stats.tools.totalCalls // 0')
tools_used=$(echo "$result" | jq -r '.stats.tools.byName // {} | keys | join(", ") | if . == "" then "none" else . end')

echo "$(date): $total_tokens tokens, $tool_calls tool calls ($tools_used) used with models: $models_used" >> usage.log
echo "$result" | jq -r '.response' > schema-docs.md
echo "Recent usage trends:"
tail -5 usage.log
```

## Tips for adapting these examples

- Adjust `--model` based on task complexity:
  - Use `gemini-3-flash-preview` for web and simple queries.
  - Use `gemini-3-pro-preview` or `gemini-2.5-pro` for complex code or architecture.
- Keep `@` scopes focused to avoid overloading context.
- In CI pipelines, always check `.error` before parsing `.response`.
- When logging or tracking, leverage `stats` fields for observability.
- Combine with other CLI tools (`grep`, `awk`, etc.) for custom workflows.
