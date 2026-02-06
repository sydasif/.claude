# Guidelines Loading Reference

This file defines when and how to load detailed guideline files from `~/.claude/shared/`.

## Why This Architecture?

The `~/.claude/shared/` folder contains detailed, domain-specific best practices that are **not auto-loaded**. This design:

- **Reduces context token consumption** - Only load what you need
- **Keeps CLAUDE.md lean** - High-level principles only
- **Enables modularity** - Load specific guidelines on demand
- **Scales better** - Won't hit context limits as domains expand

## Core Guidelines (Load at Session Start)

Load these files **at the beginning of every session** or when relevant:

### 1. Security Guidelines
**File**: `~/.claude/shared/security.md`  
**When to load**: 
- At session start (always)
- Before handling sensitive data
- Before authentication/authorization work
- Before reviewing code for security issues

**Contains**: Input validation, secret management, dependency security, secure coding practices

### 2. Testing Guidelines
**File**: `~/.claude/shared/testing.md`  
**When to load**:
- At session start (always)
- Before writing or modifying tests
- Before reviewing test coverage
- Before CI/CD configuration

**Contains**: Test organization, coverage requirements, test patterns, CI/CD integration

### 3. Tool Guidelines
**File**: `~/.claude/shared/tools.md`  
**When to load**:
- At session start (always)
- Before running build/test commands
- When setting up development environment
- When adding new tools to the project

**Contains**: uv, Poetry, Ruff, MyPy, Black, pytest, git commands

### 4. Documentation Guidelines
**File**: `~/.claude/shared/documentation.md`  
**When to load**:
- At session start
- Before writing documentation
- Before creating README files
- Before API documentation

**Contains**: README standards, docstring formats, inline comments

## Domain-Specific Guidelines (Load as Needed)

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
|-----------|------------------|
| **Session start** | security.md, testing.md, tools.md, documentation.md |
| **Python development** | python.md + session start files |
| **Database work** | database.md + session start files |
| **API development** | api-design.md + session start files |
| **Code review** | All relevant domain files |
| **Security audit** | security.md (priority) + others as needed |

## How to Load

Always use the Read tool:

```
Read ~/.claude/shared/security.md
Read ~/.claude/shared/python.md
```

## Priority Notes

- **Auto-loaded rules** (this directory): High priority, loaded every session
- **CLAUDE.md**: High priority, loaded every session  
- **~/.claude/shared/ files**: On-demand, load only when needed
- **Skills**: Medium priority, on-demand when triggered

This architecture ensures Claude has exactly the context needed - no more, no less.
