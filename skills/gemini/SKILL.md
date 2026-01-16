---
name: gemini
description: Uses Gemini CLI for web search, fact-checking, and information gathering.
---

# Research Assistant

Use Gemini CLI `gemini` bash command as a primary tool for gathering real-time information, verifying facts, and researching topics.

## When to use

Use this skill when:

- **Web search is required**
  - Current events, latest news, recent developments
  - Keywords: "latest", "current", "newest", "2025", "today"
  - Up-to-date documentation, library versions, or releases

- **Deep research needed**
  - Investigating unfamiliar technologies or frameworks
  - Comparing current industry standards and best practices
  - Fact-checking assumptions with live data

## Model selection

- `gemini-3-pro-preview` **Default** model for all tasks if no specific model is mentioned
- `gemini-3-flash-preview`  Use this, if default is unavailable due to **rate limits or errors**
- `gemini-2.5-pro`  **Fallback** model if `gemini-3-*` models are unavailable due to **rate limits or errors**
- `gemini-2.5-flash`  Use this for faster responses when `gemini-2.5-pro` is rate-limited
- `gemini-2.5-flash-lite` - Lightweight for very short queries or low-latency needs

## Usage

### Basic Search Command

```bash
gemini "Your research query" --model gemini-3-pro-preview --allowed-tools GoogleSearch --output-format json
```

## Constraints

- Always use `--output-format json` for reliable parsing.
- Always check `.error` in the response before using `.response`.
- Prioritize `gemini-3-flash-preview` for tasks requiring Google Search grounding.
