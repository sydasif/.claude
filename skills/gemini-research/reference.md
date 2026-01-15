# Gemini CLI Headless Mode Reference

This reference explains headless mode and the most useful options for using Gemini CLI programmatically in scripts, CI/CD, and automation tools.

For how Claude should decide when and how to use Gemini CLI, see [SKILL.md](SKILL.md).

## Overview

Headless mode provides a non‑interactive interface to Gemini CLI that:

- Accepts prompts via command‑line arguments or stdin
- Returns structured output (text or JSON)
- Supports file redirection and piping
- Is designed for scripting, automation, and CI/CD pipelines
- Provides consistent exit codes for error handling【turn0search0】

## Basic usage

### Direct prompts

Use `--prompt` (or `-p`) to run in headless mode:

```bash
gemini --prompt "What is machine learning?"
```

Short form:

```bash
gemini -p "What is machine learning?"
```

### Stdin input

Pipe input to Gemini CLI:

```bash
echo "Explain this code" | gemini
```

### Combining with file input

Read from files and pipe to Gemini:

```bash
cat README.md | gemini -p "Summarize this documentation"
```

## Output formats

### Text output (default)

Standard human‑readable text:

```bash
gemini -p "What is the capital of France?"
```

Example response:

```text
The capital of France is Paris.
```

### JSON output

For automation, use JSON output:

```bash
gemini -p "What is the capital of France?" --output-format json
```

Response structure (high‑level):

```json
{
  "response": "string",
  "stats": {
    "models": {
      "[model-name]": {
        "api": {
          "totalRequests": "number",
          "totalErrors": "number",
          "totalLatencyMs": "number"
        },
        "tokens": {
          "prompt": "number",
          "candidates": "number",
          "total": "number",
          "cached": "number",
          "thoughts": "number",
          "tool": "number"
        }
      }
    },
    "tools": {
      "totalCalls": "number",
      "totalSuccess": "number",
      "totalFail": "number",
      "totalDurationMs": "number",
      "totalDecisions": {
        "accept": "number",
        "reject": "number",
        "modify": "number",
        "auto_accept": "number"
      },
      "byName": {
        "[tool-name]": {
          "count": "number",
          "success": "number",
          "fail": "number",
          "durationMs": "number",
          "decisions": {
            "accept": "number",
            "reject": "number",
            "modify": "number",
            "auto_accept": "number"
          }
        }
      }
    },
    "files": {
      "totalLinesAdded": "number",
      "totalLinesRemoved": "number"
    }
  },
  "error": {
    "type": "string",
    "message": "string",
    "code": "number"
  }
}
```

The `error` object is present only when an error occurs.

### Streaming JSON output (stream-json)

For real‑time progress monitoring, event‑driven automation, or live UIs, use:

```bash
gemini --output-format stream-json --prompt "What is 2+2?"
```

Save events to a file:

```bash
gemini --output-format stream-json --prompt "Analyze this code" > events.jsonl
```

Parse event types with `jq`:

```bash
gemini --output-format stream-json --prompt "List files" | jq -r '.type'
```

#### Event types

The streaming JSONL format emits these event types:

- `init` — session starts; includes session_id and model
- `message` — user prompts and assistant messages
- `tool_use` — tool call requests with parameters
- `tool_result` — tool execution results (success or error)
- `error` — non‑fatal errors and warnings
- `result` — final session outcome with aggregated stats【turn0search0】

Each line is a complete JSON object.

### File redirection

Save output to files, append, or pipe to other commands:

```bash
# Save to file
gemini -p "Explain Docker" > docker-explanation.txt
gemini -p "Explain Docker" --output-format json > docker-explanation.json

# Append to file
gemini -p "Add more details" >> docker-explanation.txt

# Pipe to other tools
gemini -p "What is Kubernetes?" --output-format json | jq '.response'
gemini -p "Explain microservices" | wc -w
gemini -p "List programming languages" | grep -i "python"
```

## Key configuration options

| Option                  | Description                              | Example                                     |
| ----------------------- | ---------------------------------------- | ------------------------------------------- |
| `--prompt`, `-p`        | Run in headless mode                     | `gemini -p "query"`                         |
| `--output-format`       | Output format (text, json, stream-json)  | `gemini -p "query" --output-format json`    |
| `--model`, `-m`         | Choose the Gemini model                 | `gemini -p "query" -m gemini-2.5-flash`    |
| `--debug`, `-d`         | Enable debug mode                        | `gemini -p "query" --debug`                 |
| `--include-directories` | Include additional directories          | `gemini -p "query" --include-directories src,docs` |
| `--yolo`, `-y`          | Auto‑approve all actions                 | `gemini -p "query" --yolo`                 |
| `--approval-mode`       | Set approval mode                        | `gemini -p "query" --approval-mode auto_edit` |

For full configuration details (settings files, environment variables), see the official Gemini CLI configuration documentation.【turn0search11】【turn0search14】

## Related documentation

- [Gemini CLI Docs](https://geminicli.com/docs) — main documentation site
- [Headless mode](https://geminicli.com/docs/cli/headless) — detailed headless guide
