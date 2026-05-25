# Python Development Rules Index

This directory contains modular Python standards. Load individual files as needed, or load this index to see the full structure.

## Core

- [Core Style & Toolchain](./python/style-core.md) – `uv`, `ruff`, `mypy`, workflow, naming, imports, modern Python basics
- [Type Hints](./python/typing.md) – `mypy --strict`, protocols, generics, `TypedDict`, type checker selection
- [Docstrings](./python/docstrings.md) – Google‑style docstrings, `Args:`, `Returns:`, `Raises:`

## Safety & Correctness

- [Error Handling](./python/error-handling.md) – specific exceptions, `raise from`, context managers, logging
- [Security](./python/security.md) – secrets, `eval()`, SQL injection, `subprocess`, password hashing
- [Testing](./python/testing.md) – (separate file) AAA pattern, coverage, pytest

## Performance & Concurrency

- [Performance](./python/performance.md) – generators, `itertools`, `functools.lru_cache`, `set`, `heapq`, `str.join`
- [Async](./python/async.md) – `async`/`await`, `gather`, `TaskGroup`, `timeout`, `async with`

## Frameworks & Versioning

- [Framework Specifics](./python/frameworks.md) – FastAPI, Django, Flask
- [Python Version Policy](./python/version-policy.md) – minimum versions, feature tables, EOL policy
