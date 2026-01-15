---
name: research-assistant
description: Handles code analysis, architectural reasoning, and web searches.
---

# Research Assistant

Use the `gemini` when you need to code-analysis, web-search, architecture, reasoning, perform deep reasoning tasks, or access real-time information via Google Search.

## Core Behavior & Rules

* **Context Strategy:** Use this for project analysis, refactors, or debugging etc.
* **Positional Arguments:** Pass the prompt as the **positional argument** enclosed in quotes.

## File & Directory Syntax

You can include context in two ways. Combining them is permitted.

### A. The `@` Syntax (In-Prompt)

Use this within your prompt string to point to specific files or folders relative to the current working directory.

* `"@src/main.ts"` -> Reads specific file.
* `"@src/components/"` -> Reads all files in directory.
* `"@./"` -> Reads the current directory (careful with size).

### B. The Directory Flag (Workspace Scope)

Use `--include-directories` to force the inclusion of specific paths into the workspace context if they are outside the standard execution scope.

* `--include-directories ./libs,./tests`

## Usage Examples

**Single file analysis:** `gemini "@src/main.py Explain this file's purpose and structure"`
**Multiple files:** `gemini "@package.json @src/index.js Analyze the dependencies used in the code"`
**Entire directory:** `gemini "@src/ Summarize the architecture of this codebase"`
**Multiple directories:** `gemini "@src/ @tests/ Analyze test coverage for the source code"`
**Current directory and subdirectories:** `gemini "@./ Give me an overview of this entire project"`

## Google Web Search (`google_web_search`)

To use the search tool, you must explicitly instruct Gemini to use its tools in the prompt string.

* **Trigger:** "Search for...", "Find documentation on...", "Check current version of..."
* **Recommended Model:** `gemini-2.5-flash` (Fastest tool execution).

**Example:**

```bash
gemini "Check the latest news in UK about Tech" -m gemini-2.5-flash --allowed-tools google_web_search
```

## Model Selection Strategy

You **may** specify a model using the `--model` (or `-m`) flag based on the user's intent.

| Use Case | Recommended Model | Flag Name | Notes |
| :--- | :--- | :--- | :--- |
| **Deep Reasoning & Architecture** | **Gemini 3 Pro** (Preview) | `gemini-3-pro-preview` | For complex code analysis. |
| **Speed & High Throughput** | Gemini 3 Flash (Preview) | `gemini-3-flash-preview` | Best for quick summaries of large files. |
| **Legacy / Stable Analysis** | Gemini 2.5 Pro | `gemini-2.5-pro` | Use if previews are unstable (errors). |
| **Web Search & Lookups** | Gemini 2.5 Flash | `gemini-2.5-flash` | Optimized for google search. |
| **Low Cost / Simple Tasks** | Gemini 2.5 Flash Lite | `gemini-2.5-flash-lite` | Minimal reasoning required. |

### Important Notes

* Paths in `@` syntax are relative to your current working directory when invoking gemini
* The CLI will include file contents directly in the context
* No need for `--yolo` flag for read-only analysis
* Gemini's context window can handle entire codebases that would overflow Claude's context
* When checking implementations, be specific about what you're looking for to get accurate results

## Gemini CLI Help Command

For a full list of options and flags, run: `gemini --help`

This will provide you with the most up-to-date information on available commands and configurations.

## Additional Resources

See [Gemini CLI Documentation](reference.md) for more details on using the Gemini CLI effectively.
