# Skill Components

Reusable components and templates for creating consistent Claude Code skills.

## Standard Skill Template

```markdown
---
name: {skill-name}
description: {skill-description}
user-invocable: false
---

# {Skill Title}

{Skill description and purpose}

## Available Commands

{List of available commands}

## Usage Guidelines

{How to use the skill effectively}

## Best Practices

{Relevant best practices}

## Security Considerations

{Security guidelines specific to this skill}

## Troubleshooting

{Common issues and solutions}

## Integration with Other Skills

This skill works with:

- `{other-skill-1}` for {purpose}
- `{other-skill-2}` for {purpose}
- {other relevant skills}

Use this skill to {primary purpose}.
```

## Standard Sections

### Common Command Patterns

#### Linting Commands:
```bash
# Check code for issues
uv run ruff check src/

# Auto-fix linting issues
uv run ruff check --fix src/
```

#### Type Checking Commands:
```bash
# Run type checking
uv run mypy src/
```

#### Formatting Commands:
```bash
# Format code
uv run black src/

# Check formatting without changing
uv run black --check src/
```

#### Testing Commands:
```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src
```

#### Dependency Commands:
```bash
# Add a dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Sync dependencies
uv sync
```

### Common Security Guidelines

- Never commit secrets or API keys
- Use environment variables for configuration
- Validate all user inputs
- Use parameterized queries for database operations
- Keep dependencies updated

### Common Quality Requirements

- Type Hints: All public functions must have type annotations
- Documentation: Use Google-style docstrings
- Testing: Include tests for all new functionality
- Security: No hardcoded secrets
- Performance: Avoid unnecessary memory usage

### Common Modern Standards

- Use type hints for all function signatures
- Prefer f-strings for string formatting
- Use pathlib for path manipulation
- Implement async/await patterns for I/O operations
- Use dataclasses for simple data structures

### Common Project Context Checks

- Check for project configuration files (pyproject.toml, package.json, etc.)
- Identify the language/framework version being used
- Look for existing patterns and conventions
- Verify appropriate virtual environment setup

### Common Workflow Guidelines

- Analyze code structure before making changes
- Apply modern practices appropriate for the language
- Follow established project conventions
- Ensure proper error handling
- Write maintainable and readable code

## Skill Integration Patterns

### Referencing Shared Resources

Skills should reference shared resources where possible:

- For Python best practices: `[Python Guidelines](../shared/best-practices/python-guidelines.md)`
- For security practices: `[Security Guidelines](../shared/security-guidelines.md)`
- For tool usage: `[Tool Guidelines](../shared/tool-guidelines.md)`

### Cross-Skill Communication

Skills should clearly document how they work with other skills:

```
## Integration with Other Skills

This skill works with:

- `dependency-manager` for package management
- `code-quality` for linting and type checking
- `test-engineer` for test coverage verification
```

## Quality Standards for Skills

### Content Quality
- Clear, concise instructions
- Relevant examples for common use cases
- Proper formatting and structure
- Accurate and up-to-date information

### Technical Accuracy
- Valid command examples
- Correct syntax for code samples
- Working integration with actual tools
- Consistent with current best practices

### Usability
- Logical organization of content
- Clear section headings and hierarchy
- Actionable guidance
- Helpful troubleshooting tips