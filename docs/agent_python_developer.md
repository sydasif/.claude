# Comprehensive Python Developer Guide

## Core Technical Stack

- **Framework**: FastAPI 0.100+ (Python 3.11+).
- **ORM**: SQLAlchemy 2.0+ or equivalent with connection pooling.
- **Validation**: Pydantic v2 (Strict).

## API Design & REST Principles

- **URL Naming**: Plural nouns for collections (`/users`). Lowercase only. Hyphens for multi-word resources.
- **Parameters**: Use `snake_case` in curly braces for path parameters (e.g., `{user_id}`).
- **Responses**: Consistent JSON structure. `200 OK` (Success), `201 Created` (POST), `204 No Content` (DELETE), `422` (Validation Error).
- **Pagination/Sorting**: Standardized `?page=1&size=20` and `?sort=field:desc`.

## Database & Performance

- **Query Optimization**: Use `selectinload`/`joinedload` to prevent N+1 queries. Use `EXPLAIN` for complex joins.
- **Indexing**: Create indexes on frequently queried columns; monitor usage.
- **Asyncio**: Use `asyncio` for I/O-bound tasks.
- **Caching**: Use `functools.lru_cache` or Redis for expensive operations.
- **Serialization**: Use `msgspec` for performance-critical JSON; `Pydantic` for complex business logic.

## Error Handling & Logging

- **Custom Exceptions**: Create domain-specific exceptions (e.g., `PaymentError`).
- **Structured Logging**: Use JSON-formatted logs with timestamp, level, and context.
- **Fail Fast**: Implement validation at the earliest possible entry point.

## Testing Strategy

- **Framework**: Pytest with 80% minimum coverage.
- **Mocks**: Use `pytest-mock` (mocker fixture). Prefer integration tests for database logic.
- **TDD**: Write tests first -> Watch fail -> Implement -> Refactor.
