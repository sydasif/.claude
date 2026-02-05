---
name: python-dependency
description: Manage Python dependencies using uv for fast, reliable package management
user-invocable: false
---

# Python Dependency Manager

This skill provides comprehensive Python package management using `uv`, the modern replacement for `pip`.

For comprehensive tool usage guidelines, refer to: [Tool Guidelines](~/.claude/rules/tool-guidelines.md)

## Available Commands

> For complete command reference including all flags and options, see [Tool Guidelines](~/.claude/rules/tool-guidelines.md).

### Essential Commands

```bash
# Add dependencies
uv add package-name
uv add --dev pytest ruff mypy

# Remove dependencies
uv remove package-name

# Sync and update
uv sync
uv sync --reinstall

# List dependencies
uv pip list
```

## pyproject.toml Management

### Create New pyproject.toml

```bash
uv init my-project
cd my-project
```

### Add Dependencies to pyproject.toml

```bash
# Add runtime dependencies
uv add requests pandas
# Add development dependencies
uv add --dev pytest black mypy
```

### Update pyproject.toml

```bash
# Sync lock file after manual edits
uv lock
```

## Environment Management

### Create Virtual Environment

```bash
# uv automatically creates environments
# But you can specify manually
uv venv create
```

### Activate Environment

```bash
# uv manages this automatically
# Run commands directly with uv
uv run python script.py
```

## Best Practices

### Project Structure

```text
project-name/
├── pyproject.toml
├── README.md
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── module.py
├── tests/
└── .gitignore
```

### Dependency Organization

**Runtime Dependencies** (in [project] section):

- Core functionality
- Required for the application to run

**Development Dependencies** (in [tool] section):

- Testing frameworks
- Linters and formatters
- Documentation tools

### Security Considerations

- Never commit lock files to version control
- Use environment variables for API keys
- Regularly update dependencies
- Scan for vulnerabilities with `safety check`

## Troubleshooting

### Common Issues

**Permission Errors**:

```bash
# Run with appropriate permissions
uv add package-name
```

**Network Issues**:

```bash
# Check internet connection
ping pypi.org
# Use mirrors if needed
UV_INDEX_URL=https://example.com/index uv sync
```

**Python Version Mismatches**:

```bash
# Check Python version
python --version
# Install specific version
uv sync --python 3.12
```

## Examples

### Setting Up a New Project

```bash
# Initialize project
uv init data-analysis
cd data-analysis

# Add core dependencies
uv add pandas numpy matplotlib

# Add dev dependencies
uv add --dev pytest black mypy

# Create virtual environment
uv venv create

# Install dependencies
uv sync

# Run tests
uv run pytest
```

### Adding a New Dependency

```bash
# Add requests package
uv add requests

# Add with specific version
uv add requests==2.31.0

# Add with extras
uv add requests[security]

# Update lock file
uv lock
```

### Managing Development Dependencies

```bash
# Add testing framework
uv add --dev pytest pytest-cov

# Add linting tools
uv add --dev ruff black

# Add type checking
uv add --dev mypy

# Install all dev dependencies
uv sync --dev
```

---

## Integration with Other Skills

This skill integrates seamlessly with:

- `code-quality` for linting and type checking
- `python-expert` for comprehensive Python guidance
- `python-rules` for specific Python code review rules
- Custom scripts for project-specific workflows

Use this skill whenever you need to manage Python packages, set up new projects, or maintain dependency consistency across your Python development workflow.
