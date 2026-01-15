---
name: research-with-gemini
description: Code analysis, architectural reasoning, debugging, and latest web searches.
---

# Research Assistant

Use the `gemini` CLI when you need to code-analysis, web-search, architecture, reasoning, perform deep reasoning tasks, debugging or access real-time information via Google Search.

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

## Model Selection

You **may** specify a model using the `--model` (or `-m`) flag based on the user's intent.

| Flag Name | Notes |
| :--- | :--- |
| `gemini-3-pro-preview` | For code analysis. |
| `gemini-3-flash-preview` | Best for Web Search. |
| `gemini-2.5-pro` | Use if previews are unstable (errors). |
| `gemini-2.5-flash` | Good for quick reviews. |
| `gemini-2.5-flash-lite` | Minimal reasoning required. |

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
