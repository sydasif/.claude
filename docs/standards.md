# Unified Development Standards

## Python Environment

### Version & Layout

- **Python Version**: 3.11+ mandatory.
- **Structure**: Always use `src/` layout for proper package isolation.

### Framework & Libraries

- **Validation**: Pydantic v2 for all data structures, settings, and configuration.
- **Testing**: `pytest` with `pytest-mock` (mocker fixture).
- **Linting/Formatting**: Ruff (88-character line limit).
- **Management**: `uv` (Mandatory. Do not use `pip`).

### Commands (UV Workflow)

```bash
# Dependency Management
uv add requests pydantic          # Runtime dependencies
uv add --dev pytest ruff mypy    # Development dependencies

# Execution & Sync
uv sync                           # Development environment
uv sync --frozen                  # CI/CD (strict lockfile)

# Running Tasks
uv run python -m package_name     # Run application
uv run pytest                     # Run tests
uv run ruff check . --fix         # Lint
uv run ruff format .              # Format
```

## Quality Gates

### Testing

- **Coverage**: Minimum 80% required.
- **Workflow**: Tests must pass before merging.
- **Mocking**: Use `pytest-mock` exclusively.

### Linting

- **Tool**: Ruff for both linting and formatting.
- **Rules**:
  - Line limit: 110 characters.
  - Commands: `ruff check . --fix` and `ruff format .`.

## Configuration & Security

### Settings

- **Library**: `Pydantic Settings`.
- **Optimization**: Wrap settings in `@lru_cache()` to prevent repeated file system access.
- **Validation**: Strict Pydantic v2 validation at system boundaries.

### Security Checklist

- No hard-coded secrets, tokens, or credentials in code.
- Credentials must use environment variables.
- Input validation required at all system boundaries.
- Error handling must not expose sensitive information.
- Security scanning must be part of the CI workflow.

## Documentation

- **Tone**: Technical, direct, and concise.
- **Format**: Markdown with clear headers.
- **Requirements**:
  - README must include Setup, Usage, and Examples.
  - CLI commands must document arguments and example outputs.
  - Complex functions require Google-style or NumPy-style docstrings.
