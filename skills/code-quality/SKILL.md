---
name: code-quality
description: Enforce Python code quality with ruff, mypy, and modern best practices
user-invocable: false
---

# Python Code Quality Enforcer

This skill ensures Python code meets the highest quality standards using modern tools and best practices.

For comprehensive Python best practices, refer to: [Python Guidelines](../../rules/best-practices/python-guidelines.md)

For security guidelines, refer to: [Security Guidelines](../../rules/security-guidelines.md)

For tool usage guidelines, refer to: [Tool Guidelines](../../rules/tool-guidelines.md)

## Available Commands

### Linting with Ruff

```bash
# Check code for issues
uv run ruff check src/

# Auto-fix linting issues
uv run ruff check --fix src/

# Check specific files
uv run ruff check file.py

# Check with specific rules
uv run ruff check --select E,W src/
```

### Type Checking with MyPy

```bash
# Run type checking
uv run mypy src/

# Check specific files
uv run mypy file.py

# Show detailed error messages
uv run mypy --show-error-codes src/

# Ignore missing imports (for now)
uv run mypy --ignore-missing-imports src/
```

### Formatting with Black

```bash
# Format code
uv run black src/

# Check formatting without changing
uv run black --check src/

# Format specific file
uv run black file.py
```

### Security Scanning with Safety

```bash
# Scan dependencies for vulnerabilities
uv run safety check

# Check with JSON output
uv run safety check --json
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

For comprehensive performance best practices, refer to: [Python Guidelines](../../rules/best-practices/python-guidelines.md)

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

For comprehensive security guidelines, refer to: [Security Guidelines](../../rules/security-guidelines.md)

### Input Validation

```python
import re
from typing import Union

def validate_email(email: str) -> Union[str, None]:
    """Validate email address format.

    Args:
        email: Email address to validate.

    Returns:
        Validated email or None if invalid.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return email
    return None
```

### Safe Database Operations

```python
import sqlite3
from typing import List, Dict, Any

def get_users_by_age(min_age: int) -> List[Dict[str, Any]]:
    """Get users older than minimum age.

    Args:
        min_age: Minimum age to filter users.

    Returns:
        List of user dictionaries.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE age > ?"
    cursor.execute(query, (min_age,))

    results = cursor.fetchall()
    conn.close()

    return results
```

---

## Integration with Other Skills

This skill works with:

- `dependency-manager` to ensure quality tools are installed
- `python-expert` for comprehensive code review
- Custom scripts for project-specific quality rules

Use this skill to maintain high code quality standards throughout your Python development workflow.
