---
name: uv-workflow
description: UV package manager workflow for Python. Use when creating projects, managing dependencies, adding libraries, or configuring CI/CD pipelines.
---

# UV Workflow

Expert guidance for managing Python projects with `uv`.

## Core Principles

1. **Structure**: Always use `src/` layout for applications.
2. **Dependencies**: Use `uv add` (never `pip install`).
3. **Validation**: Default to **Pydantic v2** for all data modeling.
4. **CI/CD**: Strict usage of `uv sync --frozen`.

## Quick Actions

```bash
uv init <name> --app          # New application (src layout)
uv add <package>              # Add dependency
uv run python src/main.py     # Run code
uv run pytest                 # Run tests
```

## Resources

- **Command Reference**: [reference.md](reference.md) (Full CLI flags and options)

## Configuration Rules

- **Python**: `3.11+`
- **Linting**: `ruff` (line-length 88)
- **Testing**: `pytest`
