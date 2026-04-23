---
name: run-codex
description: Use Codex CLI for code generation, debugging, (bug, feature, refactor) and documentation.
---

# Codex CLI (Interactive Mode)

Use this skill to run Codex CLI in a guided, non-interactive way using `codex exec`.

## Workflow

### Step 1: Select Model

Use `AskUserQuestion` to let the user choose a model:

- `gpt-5.4` (Strong)
- `gpt-5.4-mini` (Fast)
- `gpt-5.3-codex` (Coding-optimized)
- `gpt-5.2` (Professional)

### Step 2: Select Reasoning Level

Use `AskUserQuestion` to let the user choose a reasoning effort:

- `Low`
- `Medium` (Default)
- `High`
- `xhigh`

### Step 3: Select Task Type

Use `AskUserQuestion` to let the user choose a task:

- **Code Review**: Inspect code for bugs, quality, and security.
- **Refactoring Suggestions**: Suggest improvements and cleaner patterns.
- **Code Editing**: Apply specific changes to the code.


### Step 4: Execute Task

Based on the task type, perform the following:

#### If Code Review:

1. Ask the user for the target directory or file.
2. Execute:
   `codex exec -c model="<model>" -c model_reasoning_effort="<level>" --sandbox read-only --ephemeral "Review the code in <target> for bugs, quality, and security."`
3. After Codex finishes, perform your own analysis of `<target>` and provide a summary comparison of your findings vs. Codex's output.

#### If Refactoring Suggestions:

1. Ask the user for the target directory or file.
2. Execute:
   `codex exec -c model="<model>" -c model_reasoning_effort="<level>" --sandbox read-only --ephemeral "Suggest improvements and refactoring for the code in <target>."`
3. After Codex finishes, summarize the key refactoring points and provide your own suggestions for the target.

#### If Code Editing:

1. Ask the user for the target directory or file.
2. Ask the user for specific instructions (e.g., "Add error handling to the auth module").
3. Execute:
   `codex exec -c model="<model>" -c model_reasoning_effort="<level>" --sandbox workspace-write --ephemeral "<instructions> in <target>"`

---

*Note: This skill is intended for automating Codex CLI workflows via Claude Code. For interactive sessions, use the Codex TUI directly.*
