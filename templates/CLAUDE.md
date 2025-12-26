# Project Configuration

## Project Overview

Brief description of the project purpose, main functionality, and key features.

## Technology Stack

- **Language**: Python 3.11+
- **Management**: uv (Mandatory)
- **Validation**: Pydantic v2
- **Testing**: pytest, pytest-mock
- **Linting/Formatting**: Ruff (110 char limit)

## Project Structure

```
project-root/
├── src/                 # Source code (mandatory layout)
├── tests/               # Test files
├── docs/                # Documentation
├── pyproject.toml       # Configuration
└── README.md
```

## Setup & Installation

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest
```

## Development Standards

### Quality Gates

- **Coverage**: >80%
- **Linting**: `uv run ruff check . --fix`
- **Formatting**: `uv run ruff format .`

### Configuration

- Use `pydantic-settings` for all configuration.
- Wrap settings in `@lru_cache()`.
- No hard-coded secrets.

## Core Principles

- **Practical & Direct**: Solve efficiently; avoid ceremony.
- **Validation-First**: Always prefer `--check`, `--dry-run`, or `--validate` modes.
- **Safety**: Treat network changes as production-impacting. Idempotency is key.
