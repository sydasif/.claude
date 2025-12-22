# Unified Development Standards

## Python Standards

### Version Requirements

- **Python Version**: 3.11+ mandatory

### Framework & Libraries

- **Validation**: Pydantic v2 for data structures and configuration
- **Testing**: `pytest`; 80% minimum coverage required
- **Linting**: Ruff with 88-character line limit

### Best Practices

- Favor straightforward solutions over clever abstractions
- Do not implement features until required
- Robust validation at boundaries using Pydantic v2

## Testing Standards

### Requirements

- **Framework**: `pytest` with TDD workflow
- **Coverage**: 80% minimum required
- **Mocks**: Use `pytest-mock` (mocker fixture)

### Approach

- Update or add tests only when behavior changes
- Never claim tests were run unless they were

## Configuration Management

### Settings & Validation

- Use `Pydantic Settings` for environment variable validation
- Wrap settings in `@lru_cache()` to avoid repeated file system access
- Fail fast with Pydantic v2 validation at boundaries

### Secret Management

- Never commit sensitive values
- Use environment variables for credentials
- Enable SSH key-based authentication where possible

## Security Standards

### Security Checklist

- No hard-coded secrets, tokens, or credentials
- Input validation at system boundaries
- Proper error handling that doesn't expose sensitive information
- Validate all external inputs and data sources

### Security Testing

- Run security vulnerability scanning as part of development workflow
- Monitor for potential security issues in dependencies

## Network Safety Principles

### Change Approach

Treat all network-related changes as production-impacting by default.

- Prefer small, reversible changes
- Explain impact before suggesting changes
- Always consider rollback and failure scenarios
- Avoid guessing commands or syntax

### Automation Standards

- Prefer idempotent operations
- Fail clearly on errors
- Favor validation-first or dry-run approaches
- All scripts must be safe to run multiple times

### Boundaries

- Do not touch credentials or secrets
- Do not push configs to live devices without approval
- Treat all changes as production-impacting

## Code Quality Standards

### Linting

- **Tool**: Ruff for linting and formatting
- **Line Limit**: 88-character limit
- Commands: `ruff check . --fix` and `ruff format .`

### Quality Requirements

- Follow existing structure, style, and patterns
- Keep changes minimal and scoped
- Avoid unnecessary abstractions
- Prefer simple, proven solutions
- Prioritize correctness and maintainability
- Do not run destructive commands

## Documentation Standards

### Style

- **Tone**: Professional, direct, and concise (Technical/Engineering focus)
- **Format**: Markdown with clear headers
- **Updates**: Keep documentation close to code; update in the same PR

### Components

- **README**: Must include Setup, Usage, and minimal Examples
- **CLI**: Document all commands with arguments and example outputs
- **Docstrings**: Google-style or NumPy-style docstrings for complex functions
