---
name: bob
description: Uses for Web search, Fact-checking and verification, Code review, analysis and Information synthesis from multiple sources.
---

# Bob Enhanced Web Research and Analysis Skill

Use Gemini CLI `gemini` bash command as a primary tool for gathering real-time information, verifying facts, and researching topics, when the preferred models are unavailable due to rate `limits` use *fallback models* .

## Available Models (`with fallbacks`)

- `gemini-3-pro-preview` **Default** model for all tasks if no specific model is mentioned
- `gemini-3-flash-preview`  Use this for faster web search and fact-checking tasks
- `gemini-2.5-pro`  **Fallback** model for `gemini-3-pro-preview*` when rate-limited
- `gemini-2.5-flash`  **Fallback** model for `gemini-3-flash-preview*` when rate-limited
- `gemini-2.5-flash-lite` - Lightweight and faster version for basic tasks

## Usage

### Search Command

```bash
gemini "search query" --model gemini-3-pro-preview --allowed-tools GoogleSearch
```

### Stdin input

```bash
echo "explain this code" | gemini
```

### Combining with file input

```bash
cat README.md | gemini "Summarize this documentation"
```

### JSON output

```bash
gemini "What is the capital of France?" --output-format json
```

### Code review

```bash
cat src/auth.py | gemini "Review this authentication code for security issues" > security-review.txt
```

### Notes

- File redirection is supported as bash stdin input and output to files.
- JSON output is useful for integrating with other tools and scripts.
- Use `--help` flag with `gemini` command to explore more options and configurations.
