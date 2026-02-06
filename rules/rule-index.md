# Guidelines Reference

This file defines when and how to load detailed guideline files from `~/.claude/shared/`.

## Core Guidelines

Load these files when relevant:

### 1. Security Guidelines

**File**: `~/.claude/shared/security.md`

**When to load**:

- Before handling sensitive data
- Before authentication/authorization work
- Before reviewing code for security issues

**Contains**: Input validation, secret management, dependency security, secure coding practices

### 2. Testing Guidelines

**File**: `~/.claude/shared/testing.md`

**When to load**:

- Before writing or modifying tests
- Before reviewing test coverage
- Before CI/CD configuration

**Contains**: Test organization, coverage requirements, test patterns, CI/CD integration

### 3. Tool Guidelines

**File**: `~/.claude/shared/tools.md`

**When to load**:

- Before running build/test commands
- When setting up development environment
- When adding new tools to the project

**Contains**: uv, Poetry, Ruff, MyPy, Black, pytest, git commands

### 4. Documentation Guidelines

**File**: `~/.claude/shared/documentation.md`

**When to load**:

- Before writing documentation
- Before creating README files
- Before API documentation

**Contains**: README standards, docstring formats, inline comments

## Domain-Specific Guidelines

### 5. Python Guidelines

**File**: `~/.claude/shared/python.md`

**When to load**:

- Before Python development work
- Before code review of Python files
- Before refactoring Python code
- When working with `.py` files

**Contains**: Python 3.12+ standards, type hints, async patterns, framework selection

### 6. Database Guidelines

**File**: `~/.claude/shared/database.md`

**When to load**:

- Before database work
- Before writing SQL queries
- Before ORM configuration
- Before migration work
- When working with `src/db/`, `models/`, or `migrations/`

**Contains**: Connection management, ORM patterns, query optimization, migrations

### 7. API Design Guidelines

**File**: `~/.claude/shared/api-design.md`

**When to load**:

- Before API development
- Before designing endpoints
- Before API documentation
- When working with `src/api/` or `routes/`

**Contains**: RESTful design, GraphQL patterns, error handling, versioning

## Quick Reference Map

| Task Type | Load These Files |
| ----------- | ------------------ |
| **Session start** | security.md, testing.md, tools.md, documentation.md |
| **Python development** | python.md + session start files |
| **Database work** | database.md + session start files |
| **API development** | api-design.md + session start files |
| **Code review** | All relevant domain files |
| **Security audit** | security.md (priority) + others as needed |

## How to Load

Always use the Read tool:

```text
Read ~/.claude/shared/security.md
Read ~/.claude/shared/python.md
```

This architecture ensures Claude code **(YOU)** has exactly the context needed - no more, no less.
