---
name: gemini-tool
description: Performs google web searches and research using the Gemini CLI to provide up-to-date factual summaries.
---

# Gemini Research Skill

Use this skill when you `user` need **real-time information**, or **factual verification** that requires web searches.

## usage

**Command**: `scripts/research.py`

**Arguments**:

1. **Query** (Positional, Required):
    - The search topic or question.
    - *Instruction*: Always wrap the query in quotes to prevent shell interpretation issues.

2. **`--output-format`** (Optional):
    - Choices: `text` (default), `json`
    - *Recommendation*: Use `text` for general summaries. Use `json` only if you need to programmatically parse the response.

3. **`--allowed-tools`** (Optional):
    - Default: `google_web_search`
    - *Instruction*: Rarely needs changing. Defaults to standard Google Search.

## Examples

> User: "What are the latest trends in AI industries?"

```bash
python scripts/research.py "latest trends in AI industries 2025"
```

## Constraints & Limitations

- The script prints the final research result to `stdout`.
- Status messages (e.g., "--- Researching: ... ---") are printed to `stderr`.
- The script may take longer to execute due to web search latency.
- Wait for the script to complete before using the output.
