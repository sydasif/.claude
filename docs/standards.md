# Python Development Standards

## Python Stack Overview

- **Python**: 3.11+
- **Package Manager**: `uv` (never `pip`)
- **Validation**: Pydantic v2 for all data/config
- **Testing**: `pytest` + `pytest-mock` (80% coverage minimum)
- **Linting**: Ruff (110 char limit)
- **Types**: `mypy --strict` on src/

## UV Workflow

```bash
# Dependencies
uv add requests pydantic                    # Runtime
uv add --dev pytest ruff mypy pytest-mock  # Dev tools

# Environment
uv sync                  # Local development

# Tasks
uv run ruff check . --fix && uv run ruff format .  # Lint + Format
```

## Security Requirements

- **Secrets**: Environment variables only (never hardcode)
- **Validation**: Pydantic at all system boundaries
- **Errors**: Never expose internals in messages
- **Dependencies**: Pin versions, scan for CVEs
- **Input**: Validate/sanitize all external data

## Documentation Rules

**Docstrings (Google-style):**

- Public APIs (always)
- Complex logic (complexity >7)
- Security-sensitive code

**Tone**: Technical, concise, zero fluff.

## Performance Guidelines

- Use `@lru_cache` for expensive pure functions
- Batch database operations (avoid N+1 queries)
- Use `asyncio` for I/O-bound operations
- Profile before optimizing: `python -m cProfile`
- Consider pagination for large datasets
