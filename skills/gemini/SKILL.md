---
name: gemini
description: Use Gemini CLI to perform internet research and code analysis to provide factual summaries and expert code feedback.
---

# Gemini Research & Code Analysis

- Use this skill when internet research or up-to-date factual information is required.
- Also use this skill when code quality assessment, security scanning, or code review is required.

**When invoked**:

1. Determine if the user needs internet research or code analysis.
2. For research: Run the `scripts/research.sh` helper with the query.
3. For code analysis: Run the `scripts/analyze-code.sh` helper with the target path and analysis type.

**Usage Examples**:

When the user requests:

- "Research the latest developments in AI"
- "Find current statistics about renewable energy adoption"
- "Search for recent news about climate change policies"

The script can be called directly: `@skills/gemini-research/scripts/research.sh "[specific query]"`

When the user requests code analysis:

- "Analyze the code quality of this project"
- "Review the security of these Python files"
- "Check for performance issues in this code"
- "Review code for best practices"
- "Suggest refactoring opportunities"

The script can be called directly: `@skills/gemini-research/scripts/analyze-code.sh [path] --type [analysis-type]`

**Expected Behavior**:

- For research: The skill will return factual, up-to-date information from internet research
- For code analysis: The skill will analyze provided code files or directories and provide expert feedback
