---
name: code-quality
description: Enforce Python code quality with ruff, mypy, and modern best practices
user-invocable: false
---

# Python Code Quality Enforcer

This skill ensures Python code meets the highest quality standards using modern tools and best practices.

For comprehensive Python best practices, refer to: [Python Guidelines](~/.claude/rules/best-practices/python-guidelines.md)

For security guidelines, refer to: [Security Guidelines](~/.claude/rules/security-guidelines.md)

For tool usage guidelines, refer to: [Tool Guidelines](~/.claude/rules/tool-guidelines.md)

## Available Commands

For detailed command reference and all available options, see [Tool Guidelines](~/.claude/rules/tool-guidelines.md).

### Quick Reference

```bash
# Linting with Ruff
uv run ruff check src/
uv run ruff check --fix src/

# Type checking with MyPy
uv run mypy src/

# Formatting with Black
uv run black src/

# Security scanning
uv run safety check
```

## Integration with Development Workflow

### Pre-commit Hooks

```bash
# Run quality checks before committing
uv run ruff check src/
uv run mypy src/
uv run black --check src/
```

### CI/CD Pipeline

```yaml
# .github/workflows/python.yml
name: Python Quality Checks

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: uv sync

      - name: Run linting
        run: uv run ruff check src/

      - name: Run type checking
        run: uv run mypy src/

      - name: Run formatting check
        run: uv run black --check src/
```

## Performance Optimization

For comprehensive performance best practices, refer to: [Python Guidelines](~/.claude/rules/best-practices/python-guidelines.md)

### Avoid Common Pitfalls

```python
# ❌ Bad - Creates unnecessary list

squares = [x * x for x in range(1000000)]

# ✅ Good - Uses generator

squares = (x * x for x in range(1000000))
```

### Use Modern Python Features

```python
# ❌ Old style

file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()

# ✅ Modern with context manager

with open('data.txt', 'r') as file:
    content = file.read()
```

## Security Best Practices

For comprehensive security guidelines and code examples, refer to: [Security Guidelines](~/.claude/rules/security-guidelines.md) and [Python Guidelines](~/.claude/rules/best-practices/python-guidelines.md)

Key principles:
- Validate and sanitize all user inputs
- Use parameterized queries to prevent SQL injection
- Never hardcode secrets or API keys
- Use environment variables for configuration

---

## Integration with Other Skills

This skill works with:

- `dependency-manager` to ensure quality tools are installed
- `python-expert` for comprehensive code review
- Custom scripts for project-specific quality rules

Use this skill to maintain high code quality standards throughout your Python development workflow.
