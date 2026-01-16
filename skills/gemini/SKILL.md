---
name: gemini
description: Uses for **Web search**, **Fact-checking and verification**, **Code review and analysis** and **Information synthesis from multiple sources**.
---

# Gemini

Use Gemini CLI `gemini` bash command as a primary tool for gathering real-time information, verifying facts, and researching topics.
Use fallback models when the preferred models are unavailable due to rate `limits` or errors.

## Usage

### Search Command

```bash
gemini "search query" --model gemini-3-pro-preview --allowed-tools GoogleSearch --output-format json
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

This format is ideal for programmatic processing and automation scripts.

#### Code review

```bash
cat src/auth.py | gemini "Review this authentication code for security issues" > security-review.txt
```

## Available Models (`with fallbacks`)

- `gemini-3-pro-preview` **Default** model for all tasks if no specific model is mentioned
- `gemini-3-flash-preview`  Use this, if default is unavailable due to **rate limits or errors**
- `gemini-2.5-pro`  **Fallback** model if `gemini-3-*` models are unavailable due to **rate limits or errors**
- `gemini-2.5-flash`  Use this for faster responses when `gemini-2.5-pro` is rate-limited
- `gemini-2.5-flash-lite` - Lightweight for very short queries or low-latency needs

> File redirection is supported for input and output operations.
> Use `--help` flag with `gemini` command to explore more options and configurations.
