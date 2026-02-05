# Python Development Best Practices

This document contains centralized Python development best practices to be referenced by various skills and agents.

## Modern Python Standards (3.12+)

- Use **type hints** for all function signatures
- Prefer **f-strings** for string formatting
- Use **pathlib** for path manipulation
- Implement **async/await** patterns for I/O operations
- Use **dataclasses** for simple data structures
- Prefer **pydantic** for data validation

## Python Security Best Practices

- Never commit secrets or API keys
- Use environment variables for configuration
- Validate all user inputs
- Use parameterized queries for database operations
- Keep dependencies updated

## Code Quality Requirements

- **Type Hints**: All public functions must have type annotations
- **Documentation**: Use Google-style docstrings
- **Testing**: Include tests for all new functionality
- **Security**: No hardcoded secrets
- **Performance**: Avoid unnecessary memory usage

## Package Management Guidelines

- Prefer `uv` over `pip` for speed and reliability
- Use `pyproject.toml` instead of `requirements.txt`
- Pin exact versions in lock files
- Regularly update dependencies

## Testing Standards

- Use **pytest** for all testing needs
- Write **parametrized tests** to cover multiple scenarios
- Use **fixtures** for test setup/teardown
- Implement **property-based testing** with `hypothesis`
- Maintain **high test coverage** (90%+ preferred)

## Performance Best Practices

- Use generators for large datasets: `(x for x in items if condition)`
- Use `itertools` for efficient iteration patterns
- Consider `functools.lru_cache` for expensive pure functions
- Use `collections.defaultdict` to avoid repeated key checking

## Async Programming Patterns

- Use `async`/`await` syntax for asynchronous operations: `async def fetch_data():`
- Proper error handling with try/catch in async functions
- Use `asyncio.gather()` for concurrent operations: `await asyncio.gather(task1, task2)`
- Use `asyncio.create_task()` to schedule concurrent tasks
- Use `asyncio.timeout()` (Python 3.11+) or `asyncio.wait_for()` for timeouts
- Implement proper cleanup with async context managers: `async with`
- Avoid `asyncio.run()` in libraries; reserve for main entry points
- Use `asyncio.sleep()` instead of `time.sleep()` in async functions

## Framework Selection Guidelines

### Decision Tree

```text
What are you building?
│
├── API-first / Microservices
│   └── FastAPI (async, modern, fast)
│
├── Full-stack web / CMS / Admin
│   └── Django (batteries-included)
│
├── Simple / Script / Learning
│   └── Flask (minimal, flexible)
│
├── AI/ML API serving
│   └── FastAPI (Pydantic, async, uvicorn)
│
└── Background workers
    └── Celery + any framework
```

### Async vs Sync Decision

#### When to Use Async

```text
async def is better when:
├── I/O-bound operations (database, HTTP, file)
├── Many concurrent connections
├── Real-time features
├── Microservices communication
└── FastAPI/Starlette/Django ASGI

def (sync) is better when:
├── CPU-bound operations
├── Simple scripts
├── Legacy codebase
├── Team unfamiliar with async
└── Blocking libraries (no async version)
```

## Dependency Management

Always use modern, reproducible dependency management and execution patterns.

- Use `uv` for fast dependency management and execution (recommended)
- Use `Poetry` or `PDM` for project dependency management with lock files
- Always use `uv run` or `poetry run` to execute Python scripts and commands
- For ad-hoc Python execution, use `uv run python -c "your code"` or `poetry run python -c "your code"`
- Use virtual environments for project isolation
- Use `pyproject.toml` for project configuration and dependency specifications
- Pin dependencies in lock files (`uv.lock`, `poetry.lock`, or `pdm.lock`)
- Scan dependencies for security vulnerabilities with `pip-audit`, `safety`, or similar tools
- Use `uv pip compile` or `poetry export` to generate requirements files for deployment
