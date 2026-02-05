# Tool Guidelines

This document contains centralized tool usage guidelines to be referenced by various skills and agents.

## Python Development Tools

### uv (Universal Virtual Environment)
- Use `uv` for fast dependency management and execution (recommended)
- Faster alternative to `pip` and `virtualenv`
- Compatible with `pyproject.toml`, `requirements.txt`, and `setup.py`

#### Common uv Commands:
```bash
# Initialize a new project
uv init my-project

# Add dependencies
uv add package-name
uv add package-name==1.2.3
uv add --dev pytest black mypy

# Sync dependencies from pyproject.toml
uv sync

# Run commands in the environment
uv run python script.py
uv run pytest
uv run black .
```

### Ruff (Fast Python Linter)
- Blazingly fast Python linter and formatter
- Drop-in replacement for multiple tools
- Supports most common linting rules

#### Common Ruff Commands:
```bash
# Check code for issues
uv run ruff check src/

# Auto-fix issues
uv run ruff check --fix src/

# Format code (like Black)
uv run ruff format src/
```

### MyPy (Static Type Checker)
- Static type checker for Python
- Catches type-related errors before runtime

#### Common MyPy Commands:
```bash
# Run type checking
uv run mypy src/

# Show detailed error messages
uv run mypy --show-error-codes src/
```

### Black (Code Formatter)
- Opinionated code formatter
- Ensures consistent code style

#### Common Black Commands:
```bash
# Format code
uv run black src/

# Check formatting without changing
uv run black --check src/
```

### PyTest (Testing Framework)
- Feature-rich testing framework
- Supports simple unit tests and complex functional testing

#### Common PyTest Commands:
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test file
uv run pytest tests/test_example.py

# Run with verbose output
uv run pytest -v
```

## Git Best Practices

### Commit Messages
- Use imperative mood: "Add feature" not "Added feature"
- Start with capital letter
- Don't end with period
- Limit subject line to 50 characters
- Separate subject from body with blank line
- Wrap body at 72 characters

### Branch Naming
- Use lowercase with hyphens
- Prefix with type: `feat/`, `bugfix/`, `chore/`, `docs/`
- Example: `feat/add-user-authentication`

## Docker Guidelines

### Dockerfile Best Practices
- Use specific base image tags
- Multi-stage builds for smaller final images
- RUN apt-get update && apt-get install together
- Use .dockerignore to exclude unnecessary files

## Package Management Tools

### Poetry
- Dependency management and packaging tool
- Handles virtual environments automatically
- Uses poetry.lock for reproducible builds

### PDM
- Modern Python package manager
- Uses PEP 582 approach (no virtual env required)
- Fast dependency resolution

## Code Quality Tools

### Safety
- Scans dependencies for known security vulnerabilities
```bash
uv run safety check
```

### Bandit
- Security-oriented static analysis tool for Python
```bash
uv run bandit -r src/
```

### Pre-commit Hooks
- Automate code quality checks
- Configure in `.pre-commit-config.yaml`
- Run checks before commits

## Development Environment Setup

### IDE Configuration
- Configure auto-formatters to run on save
- Set up linters with proper configuration
- Use virtual environments consistently
- Enable type checking in the editor