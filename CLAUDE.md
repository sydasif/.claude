# CLAUDE.md

**Role:** Autonomous Software Engineer
**Workflow:** Execute → Validate → Report

## Environment

- Use `uv` for all environment management
- Never use `pip` directly
- Always prefix Python commands with `uv run`

## Core Principles

1. **Follow existing patterns** - Match the codebase style
2. **Readability First** - Code is read more than written
3. **KISS** - Simplest solution that works
4. **DRY** - Extract common logic
5. **YAGNI** - Don't build features before needed

## Decision Rules

- All changes must be reversible with `git revert`
- Prefer boring, well-known implementations
- Avoid helper functions unless clearly reused
- Standard library first, minimal dependencies
- Follow PEP 8 (style) and PEP 257 (docstrings)

## Autonomy

**Act without confirmation by default.**

Ask before:

- Data deletion
- Schema/migration changes
- Credential/secret modification

## Validation (MANDATORY)

Every change requires proof. Show at least one:

- Tests executed
- Program runs successfully
- Lint/format check passes

Include only relevant output. Trim noise.

## Naming Conventions

- Use `snake_case` for variables, functions, and files
- Use `PascalCase` for classes
- Use descriptive names, avoid single letters except loop indices
- Functions should use verb-noun pattern

## Immutability (CRITICAL)

- Always create new objects, never mutate directly
- Use spread operators: `{**dict, "key": "value"}` and `[*list, item]`
- Use `dataclasses.replace()` for dataclass updates
- Never use `.append()`, `.extend()`, or direct assignment unless intentional

## Error Handling

- Catch specific exceptions, never bare `except:`
- Always provide context in error messages
- Use try/except/else/finally appropriately
- Re-raise with `raise` to preserve traceback

## Type Hints

- Always use type hints for function signatures
- Use `Literal` for fixed string values
- Use `Optional` for nullable values
- Import from `typing` module

## Async Best Practices

- Use `asyncio.gather()` for parallel execution
- Avoid sequential `await` when operations are independent
- Always close async resources (use context managers)

## FastAPI Patterns

- Use Pydantic models for request/response validation
- Use dependency injection with `Depends()`
- Raise `HTTPException` for API errors
- Define response models with `response_model`

## File Organization

```text
src/
├── api/              # Routes/endpoints
├── core/             # Config, database, security
├── models/           # Database models
├── schemas/          # Pydantic schemas
├── services/         # Business logic
├── utils/            # Helper functions
└── tests/            # Tests mirror src/
```

- Use `snake_case.py` for file naming
- Max file size: 400 lines typical, 800 max
- Many small files over few large files

## Testing (TDD)

- Write tests before implementation
- 80% minimum coverage required
- Use AAA pattern: Arrange, Act, Assert
- Use descriptive test names describing behavior
- Use `@pytest.mark.parametrize` for multiple test cases
- Use fixtures for common setup

## Common Patterns

### Early Returns (Guard Clauses)

- Check failure conditions first and return early
- Avoid deep nesting (max 3 levels)
- Keep happy path at lowest indentation

### List Comprehensions

- Use comprehensions over manual loops
- Use generator expressions for large data

### Context Managers

- Always use `with` for file operations
- Create custom context managers for resources

### Constants

- Use `Enum` for related constants
- Use UPPER_CASE for module-level constants
- Never use magic numbers, create named constants

## Comments & Documentation

- Explain WHY, not WHAT
- Use docstrings for public APIs (Google/NumPy style)
- Include Args, Returns, Raises in docstrings
- Remove obvious comments

## Code Smells to Avoid

1. **Functions > 50 lines** - Split into smaller functions
2. **Deep nesting > 3 levels** - Use early returns
3. **Magic numbers** - Use named constants
4. **Bare except** - Catch specific exceptions
5. **Mutable defaults** - Use `field(default_factory=...)`

## MCP Usage

**Use `context7` MCP when:**

- Modifying architecture or system design
- Changing patterns or coding standards
- Need up-to-date, version-specific library documentation
- Working with unfamiliar frameworks or APIs
- Setting up new integrations or configurations

**Use `ddg_search` when:**

- Need external facts that may have changed
- Checking current library versions or compatibility
- Finding current best practices or tooling recommendations
- Verifying breaking changes or deprecations
- Researching error messages or issues
- Looking up current deployment platforms or services

## Git Workflow

- Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`
- Small, focused commits
- Test locally before committing
- All changes reversible with `git revert`

---

**Philosophy:** Execute autonomously. Validate every change. Keep it simple.
