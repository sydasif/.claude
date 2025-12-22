---
name: gemini
description: Use Gemini CLI to perform internet research and code analysis to provide factual summaries and expert code feedback.
---

# Gemini Research & Code Analysis

- Use this skill when internet research or up-to-date factual information is required.
- Also use this skill when code quality assessment, security scanning, or code review is required.

**When invoked**:

1. **Determine user intent**:
   - Use `research.py` for general research questions, factual information, statistics, news, or explanations about concepts
   - Use `analyze_code.py` when analyzing code files, reviewing code quality, checking for security issues, or examining code structure

2. **For research queries**: Run the `scripts/research.py` helper with the query and optional parameters.

3. **For code analysis**: Run the `scripts/analyze_code.py` helper with the target path, analysis type, and optional parameters.

4. **Intent detection examples**:
   - **Research intent**: "What is the latest Python version?", "Find statistics about AI adoption", "Explain how neural networks work", "Research climate change policies"
   - **Code analysis intent**: "Analyze this Python code for security issues", "Review code quality", "Check for performance problems", "Suggest improvements for this function", "Find bugs in the provided code"

5. **Default behavior**: If the user intent is ambiguous, prefer `research.py` for general questions and `analyze_code.py` when code files or specific technical analysis is mentioned.

**Usage Examples**:

When the user requests:

- "Research the latest developments in AI"
- "Find current statistics about renewable energy adoption"
- "Search for recent news about climate change policies"

The script can be called directly with various options:

```bash
@skills/gemini/scripts/research.py "[specific query]"
@skills/gemini/scripts/research.py "[query]" --output-format json
@skills/gemini/scripts/research.py "[query]" --model gemini-2.5-flash
@skills/gemini/scripts/research.py "[query]" --debug
@skills/gemini/scripts/research.py "[query]" --include-directories src,docs
```

When the user requests code analysis:

- "Analyze the code quality of this project"
- "Review the security of these Python files"
- "Check for performance issues in this code"
- "Review code for best practices"
- "Suggest refactoring opportunities"

The script can be called directly with various options:

```bash
@skills/gemini/scripts/analyze_code.py [path] --type [analysis-type]
@skills/gemini/scripts/analyze_code.py [path] --type security --output-format json
@skills/gemini/scripts/analyze_code.py [path] --type performance --model gemini-2.5-pro
@skills/gemini/scripts/analyze_code.py [path] --type general --debug
@skills/gemini/scripts/analyze_code.py [path] --type best-practices --include-directories src,docs,tests
```

**Available Analysis Types**:

- `general` - Overall code quality and structure
- `security` - Security vulnerabilities and best practices
- `performance` - Performance bottlenecks and optimization
- `best-practices` - Coding standards and best practices
- `refactoring` - Code improvement opportunities

**Available Options**:

- `--output-format {text,json,stream-json}` - Specify output format (default: text)
- `--model MODEL` - Specify the Gemini model to use (e.g., gemini-2.5-flash, gemini-2.5-pro)
- `--debug` - Enable debug mode for troubleshooting
- `--include-directories INCLUDE_DIRECTORIES` - Include additional directories for context

**Expected Behavior**:

- For research: The skill will return factual, up-to-date information from internet research
- For code analysis: The skill will analyze provided code files or directories and provide expert feedback
- Both modes support JSON output for programmatic processing
- Both modes support model selection for specific capabilities
- Both modes support additional context through include-directories

**Notes**: Wait as needed for the scripts to complete before returning results to the user.
