---
name: gemini
description: Official integration for Gemini CLI. Handles large-context code analysis, architectural reasoning, and web searches using Gemini 3 and 2.5 models.
---

# Gemini CLI Assistant

Use the `gemini` command when you need to analyze contexts larger than your current window, perform deep reasoning tasks, or access real-time information via Google Search.

## 1. Core Behavior & Rules

* **Context Strategy:** Use this for whole-project analysis, large refactors, or reading file sets >100KB.
* **Positional Arguments:** You must pass the prompt as the **last positional argument** enclosed in quotes.
* **Non-Interactive:** Always use the `-y` (YOLO) flag or ensure the prompt does not require follow-up questions, to prevent the agent from hanging.

## 2. Model Selection Strategy

You **must** specify a model using the `--model` (or `-m`) flag based on the user's intent.

| Use Case | Recommended Model | Flag | Notes |
| :--- | :--- | :--- | :--- |
| **Deep Reasoning & Architecture** | **Gemini 3 Pro** (Preview) | `-m gemini-3-pro-preview` | Default for complex code analysis. |
| **Speed & High Throughput** | Gemini 3 Flash (Preview) | `-m gemini-3-flash-preview` | Best for quick summaries of large files. |
| **Legacy / Stable Analysis** | Gemini 2.5 Pro | `-m gemini-2.5-pro` | Use if previews are unstable. |
| **Web Search & Lookups** | Gemini 2.5 Flash | `-m gemini-2.5-flash` | Optimized for `google_web_search`. |
| **Low Cost / Simple Tasks** | Gemini 2.5 Flash Lite | `-m gemini-2.5-flash-lite` | Minimal reasoning required. |

*Default Rule: If the user provides no specific constraint, use `gemini-3-pro-preview`.*

## 3. File & Directory Syntax

You can include context in two ways. Combining them is permitted.

### A. The `@` Syntax (In-Prompt)

Use this within your prompt string to point to specific files or folders relative to the current working directory.

* `"@src/main.ts"` -> Reads specific file.
* `"@src/components/"` -> Reads all files in directory.
* `"@./"` -> Reads the current directory (careful with size).

### B. The Directory Flag (Workspace Scope)

Use `--include-directories` to force the inclusion of specific paths into the workspace context if they are outside the standard execution scope.

* `--include-directories ./libs,./tests`

## 4. Google Web Search (`google_web_search`)

To use the search tool, you must explicitly instruct Gemini to use its tools in the prompt string.

* **Trigger:** "Search for...", "Find documentation on...", "Check current version of..."
* **Recommended Model:** `gemini-2.5-flash` (Fastest tool execution).

**Example:**

```bash
gemini -m gemini-2.5-flash "Check the latest news in UK about Tech" --allowed-tools google_web_search
```

## 5. Comprehensive Usage Examples

**Single file analysis:**

`gemini -p "@src/main.py Explain this file's purpose and structure"`

Multiple files:

`gemini -p "@package.json @src/index.js Analyze the dependencies used in the code"`

Entire directory:

`gemini -p "@src/ Summarize the architecture of this codebase"`

Multiple directories:

`gemini -p "@src/ @tests/ Analyze test coverage for the source code"`

Current directory and subdirectories:

`gemini -p "@./ Give me an overview of this entire project"`

## Implementation Verification Examples

Check if a feature is implemented:

`gemini -p "@src/ @lib/ Has dark mode been implemented in this codebase? Show me the relevant files and functions"`

Verify authentication implementation:

`gemini -p "@src/ @middleware/ Is JWT authentication implemented? List all auth-related endpoints and middleware"`

Check for specific patterns:

`gemini -p "@src/ Are there any React hooks that handle WebSocket connections? List them with file paths"`

Verify error handling:

`gemini -p "@src/ @api/ Is proper error handling implemented for all API endpoints? Show examples of try-catch blocks"`

Check for rate limiting:

`gemini -p "@backend/ @middleware/ Is rate limiting implemented for the API? Show the implementation details"`

Verify caching strategy:

`gemini -p "@src/ @lib/ @services/ Is Redis caching implemented? List all cache-related functions and their usage"`

Check for specific security measures:

`gemini -p "@src/ @api/ Are SQL injection protections implemented? Show how user inputs are sanitized"`

Verify test coverage for features:

`gemini -p "@src/payment/ @tests/ Is the payment processing module fully tested? List all test cases"`

## Gemini CLI Help Command

For a full list of options and flags, run:

```bash
gemini --help
```

This will provide you with the most up-to-date information on available commands and configurations.

### Important Notes

* Paths in @ syntax are relative to your current working directory when invoking gemini
* The CLI will include file contents directly in the context
* No need for --yolo flag for read-only analysis
* Gemini's context window can handle entire codebases that would overflow Claude's context
* When checking implementations, be specific about what you're looking for to get accurate results
