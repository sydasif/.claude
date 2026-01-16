---
name: research
description: Uses Gemini CLI for web search, fact-checking, and real-time information gathering.
---

# Research Assistant with Gemini CLI

Use Gemini CLI as a primary tool for gathering real-time information, verifying facts, and researching topics.

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

- `gemini-3-flash-preview` - **Primary model for web search and current info**
- `gemini-2.5-flash` - **Fallback** for general research tasks, if `gemini-3-flash-preview` is unavailable
- `gemini-2.5-flash-lite` - Lightweight for very short queries

## Usage

### Basic Search Command

```bash
gemini "Your research query" --model gemini-3-flash-preview --output-format json
```

### Research Workflow

1. **Identify Information Gap:**
    - Is the information time-sensitive?
    - Is the internal knowledge cutoff outdated?

2. **Execute Search:**
    - Formulate a clear, keyword-rich query.
    - Run the command using the `gemini-3-flash-preview` model.

3. **Synthesize:**
    - Parse the JSON output.
    - Cite the findings.
    - Integrate the new information into the response.

## Examples

**Finding latest documentation:**

```bash
gemini "What are the breaking changes in Next.js 15?" \
  --model gemini-3-flash-preview --output-format json
```

**Market research / Trends:**

```bash
gemini "Current trends in AI agent architecture 2025" \
  --model gemini-3-flash-preview --output-format json
```

**Technical comparison:**

```bash
gemini "Compare Bun vs Node.js performance benchmarks 2025" \
  --model gemini-3-flash-preview --output-format json
```

## Constraints

- Always use `--output-format json` for reliable parsing.
- Always check `.error` in the response before using `.response`.
- Prioritize `gemini-3-flash-preview` for tasks requiring Google Search grounding.
