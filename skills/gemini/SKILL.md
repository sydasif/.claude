---
name: gemini
description: Uses for web search, fact-checking, information gathering and code review.
---

# Research Assistant

Use Gemini CLI `gemini` bash command as a primary tool for gathering real-time information, verifying facts, and researching topics.

## When to use

Use this skill when:

- **Web search is required**
- **Deep research needed**
- **Fact-checking and verification**
- **Code review and analysis**
- **Information synthesis from multiple sources**

## Usage

### Search Command

```bash
gemini "Your search query" --model gemini-3-pro-preview --allowed-tools GoogleSearch --output-format json
```

### Stdin input

```bash
echo "Explain this code" | gemini
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

### File redirection

```bash
gemini "Explain Docker" > docker-explanation.txt
gemini "Explain Docker" --output-format json > docker-explanation.json
gemini "Add more details" >> docker-explanation.txt
gemini "What is Kubernetes?" --output-format json | jq '.response'
gemini "Explain microservices" | wc -w
gemini "List programming languages" | grep -i "python"
```

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
