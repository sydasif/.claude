# Python Development Best Practices

This document contains centralized Python development best practices to be referenced by various skills and agents.

## Modern Python Standards (3.12+)

- Use **type hints** for all public function signatures and when clarity improves code understanding
- Prefer **f-strings** for string formatting
- Use **pathlib** for path manipulation
- Implement **async/await** patterns for I/O operations
- Use **dataclasses** for simple data structures
- Prefer **pydantic** for data validation

## Python Security Best Practices

For comprehensive security guidelines, refer to the centralized security guidelines at `rules/security-guidelines.md`.

## Security - Input Validation Requirements

### SQL Injection Prevention
```python
# ❌ NEVER - String concatenation
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)

# ✅ ALWAYS - Parameterized queries
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))

# ✅ ORM (safest)
user = User.objects.filter(id=user_id).first()
```

### Path Traversal Prevention

```python
# ❌ BAD
file_path = os.path.join(base_dir, user_input)

# ✅ GOOD
import os.path
safe_path = os.path.normpath(user_input)
if safe_path.startswith("..") or os.path.isabs(safe_path):
    raise ValueError("Path traversal attempt detected")
file_path = os.path.join(base_dir, safe_path)
```

### Command Injection Prevention

```python
# ❌ NEVER
import subprocess
subprocess.run(f"ls {user_dir}", shell=True)

# ✅ ALWAYS
subprocess.run(["ls", user_dir], shell=False)
```

### XSS Prevention (web contexts)

```python
from markupsafe import escape
safe_output = escape(user_input)
```

## Code Quality Requirements

### Type Hints - Pragmatic Approach

**REQUIRED:**
- Public API functions (in `__all__`)
- Functions with 2+ parameters
- Non-obvious return types
- Library/package code

**OPTIONAL:**
- Private functions with obvious signatures
- Lambda functions
- Simple property getters/setters
- `__init__` methods (use `@dataclass` instead)
- Script-level code

**Examples:**
```python
# ❌ Low value - obvious from name
def is_valid(email: str) -> bool:
    return "@" in email

# ✅ High value - complex signature
def transform_records(
    records: Iterable[Dict[str, Any]],
    filters: Optional[List[Callable[[Dict], bool]]] = None,
    limit: int = 100
) -> Iterator[ProcessedRecord]:
    ...
```

- **Documentation**: Use Google-style docstrings
- **Testing**: Include tests for all new functionality
- **Security**: No hardcoded secrets
- **Performance**: Avoid unnecessary memory usage

## Package Management Guidelines

### Dependency Management - Tool Selection

**Primary Recommendation: uv**
- Fastest package installer (10-100x faster than pip)
- Built-in Python version management
- Compatible with pip/PyPI
- Use for: New projects, speed-critical workflows

**Alternative: Poetry (if team already uses it)**
- Mature, stable, large ecosystem
- Excellent documentation
- Use for: Existing Poetry projects, team familiarity

**Alternative: PDM (PEP 582)**
- Standards-compliant
- Use for: Strict PEP adherence requirements

**Never Use:**
- Bare `pip` for project management (only for Docker/CI)
- `requirements.txt` without lock files

### Decision Tree:
```text
Starting new project? → uv
Team already uses Poetry? → Poetry
Must follow PEPs exactly? → PDM
Simple script/prototype? → uv
```

## Testing Standards

- Use **pytest** for all testing needs
- Write **parametrized tests** to cover multiple scenarios
- Use **fixtures** for test setup/teardown
- Implement **property-based testing** with `hypothesis`

### Test Coverage Requirements

**By Component Criticality:**

| Component Type | Branch Coverage | Rationale |
|---|---|---|
| Business logic | 95%+ | Core value, high risk |
| API endpoints | 90%+ | User-facing |
| Data models/validation | 85%+ | Data integrity |
| CLI tools | 70%+ | Integration tests sufficient |
| Utilities | 80%+ | Pure functions |
| Config/constants | 60%+ | Low complexity |

**Use Branch Coverage, Not Line:**
```bash
pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html
```

**Don't Chase 100%**
- Some code isn't worth testing (`__repr__`, simple getters)
- Focus on **risk areas**, not percentage
- Use coverage to find **untested code**, not as a goal

## Performance Best Practices

- Use generators for large datasets: `(x for x in items if condition)`
- Use `itertools` for efficient iteration patterns
- Consider `functools.lru_cache` for expensive pure functions
- Use `collections.defaultdict` to avoid repeated key checking

### Performance Testing Requirements

## Performance Testing Requirements

**Benchmark Critical Paths**

**Use pytest-benchmark:**
```python
def test_api_endpoint_performance(benchmark):
    result = benchmark(call_api, payload)
    assert result.status_code == 200
```

**pytest.ini configuration:**

```ini
[tool:pytest]
benchmark_min_rounds = 5
benchmark_warmup = true
benchmark_max_time = 1.0
```

**Load Testing**

**Required for:**

- All API endpoints
- Database queries returning > 100 rows
- File operations > 10MB
- Algorithms with O(n²) or worse complexity

**Tools:**

- `locust` for HTTP load testing
- `k6` for modern load testing
- Set SLOs: p95 latency, error rate < 0.1%

**Example locust test**

```python
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_users(self):
        self.client.get("/api/users")
```

## Async Programming Patterns

- Use `async`/`await` syntax for asynchronous operations: `async def fetch_data():`
- Proper error handling with try/catch in async functions: Always handle potential exceptions from async operations
- Use `asyncio.gather()` for concurrent operations with proper error handling:
  ```python
  # Safe pattern - collect results and exceptions separately
  import asyncio

  async def safe_gather(*coroutines):
      results = await asyncio.gather(*coroutines, return_exceptions=True)
      for i, result in enumerate(results):
          if isinstance(result, Exception):
              print(f"Task {i} failed: {result}")
          else:
              print(f"Task {i} succeeded: {result}")

  # Example usage: await safe_gather(task1, task2)
  ```
- Use `asyncio.create_task()` to schedule concurrent tasks
- Use `asyncio.timeout()` (Python 3.11+) or `asyncio.wait_for()` for timeouts:
  ```python
  async def with_timeout():
      try:
          async with asyncio.timeout(5.0):  # 5 second timeout
              result = await some_async_operation()
          return result
      except TimeoutError:
          print("Operation timed out")
          raise
  ```
- Implement proper cleanup with async context managers: `async with`
- Avoid `asyncio.run()` in libraries; reserve for main entry points
- Use `asyncio.sleep()` instead of `time.sleep()` in async functions
- Handle cancellation gracefully with `asyncio.CancelledError` when needed
- Always use `asyncio.create_task()` with proper error propagation in concurrent scenarios

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

### Type Hint Complexity Guidelines

**When Type Hints Become Too Complex:**
- Use `TypeAlias` for complex type definitions:
  ```python
  from typing import TypeAlias

  Matrix: TypeAlias = list[list[float]]
  JsonData: TypeAlias = dict[str, str | int | float | list | dict]
  ```

**TypedDict for Dictionary Structures:**
```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str
```

**Protocol for Interface Definitions:**
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()
```

**Avoid overly complex type annotations that reduce readability. When type hints become longer than the function implementation, consider simplifying or using TypeAlias.**
```

### Async vs Sync Decision

## Async vs Sync - Quantitative Decision Matrix

**Use ASYNC when:**
- Handling **10+ concurrent** I/O operations
- Building web APIs/servers (FastAPI, Starlette)
- WebSocket/SSE long-lived connections
- Response time < 100ms required
- Integrating with async libraries (aiohttp, asyncpg)

**Use SYNC when:**
- Sequential processing (< 10 operations)
- Simple CLI scripts
- Batch jobs (not latency-sensitive)
- CPU-bound operations
- ORM doesn't support async (e.g., classic Django ORM)

**Examples:**

**Sequential file processing → SYNC:**
```python
for file in files[:5]:
    process_file(file)  # Simple, readable
```

**100+ concurrent API calls → ASYNC:**

```python
async with asyncio.TaskGroup() as tg:
    for url in urls:
        tg.create_task(fetch_url(url))
```

**Database queries:**

```python
# Simple CRUD → Sync is fine
user = User.objects.get(id=user_id)

# High-throughput API → Async
async with db.transaction():
    await User.async_get(id=user_id)
```

#### When to Use Async

```text
async def is better when:
├── I/O-bound operations (database, HTTP, file) - Quantitative: >5 concurrent ops
├── Many concurrent connections - Quantitative: >100 expected users
├── Real-time features - Quantitative: <100ms response time requirement
├── Microservices communication - Quantitative: >5 services interaction
└── FastAPI/Starlette/Django ASGI - Quantitative: When async infrastructure exists

def (sync) is better when:
├── CPU-bound operations - Quantitative: >80% CPU utilization expected
├── Simple scripts - Quantitative: <50 lines of code
├── Legacy codebase - Quantitative: When migration cost > benefit
├── Team unfamiliar with async - Quantitative: When training time > project timeline
└── Blocking libraries (no async version) - Quantitative: When 100% blocking dependencies
```

### Execution Patterns
- Always use `uv run`, `poetry run`, or `pdm run` to execute Python scripts and commands
- For ad-hoc Python execution, use `uv run python -c "your code"`, `poetry run python -c "your code"`, or `pdm run python -c "your code"`
- Use virtual environments for project isolation (automatic with `uv`, `Poetry`, and `PDM`)
- Use `pyproject.toml` for project configuration and dependency specifications
- Pin dependencies in lock files (`uv.lock`, `poetry.lock`, or `pdm.lock`)
- Scan dependencies for security vulnerabilities with `pip-audit`, `safety`, or similar tools
- Use `uv pip compile`, `poetry export`, or `pdm export` to generate requirements files for deployment
