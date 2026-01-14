# Development Standards

## Python Stack (Non-Negotiable)

- **Python**: 3.11+ only
- **Layout**: `src/` structure mandatory
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
uv sync --frozen         # CI/CD (locked)

# Tasks
uv run python -m pkg     # Run app
uv run pytest --cov=src --cov-fail-under=80  # Test
uv run ruff check . --fix && uv run ruff format .  # Lint + Format
uv run mypy src/ --strict                    # Type check
```

## Quality Gates (Pre-commit/CI)

```bash
# Validation pipeline (must pass)
uv run ruff check . --fix       # Auto-fix linting
uv run ruff format .            # Format (110 chars)
uv run mypy src/ --strict       # Type safety
uv run pytest --cov=src --cov-fail-under=80  # 80%+ coverage
grep -rn "api_key\|password\|token" src/ && exit 1  # No secrets
```

## Security Requirements

- **Secrets**: Environment variables only (never hardcode)
- **Validation**: Pydantic at all system boundaries
- **Errors**: Never expose internals in messages
- **Dependencies**: Pin versions, scan for CVEs
- **Input**: Validate/sanitize all external data

## Configuration Pattern

```python
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    db_url: str
    debug: bool = False

    class Config:
        env_file = ".env"

@lru_cache()  # Cache to avoid repeated file reads
def get_settings() -> Settings:
    return Settings()
```

## Documentation Rules

**Docstrings (Google-style):**

- Public APIs (always)
- Complex logic (complexity >7)
- Security-sensitive code

**README Structure:**

```markdown
# Project Name
Description (one line)

## Quick Start
```bash
uv sync && uv run python -m pkg
```

## Usage

```python
from pkg import main
main(args)
```

## Development

```bash
uv run pytest
```

```

**Tone**: Technical, concise, zero fluff.

## Type Safety Examples

```python
# Good: Full annotations
def process(data: dict[str, Any]) -> UserModel:
    return UserModel.model_validate(data)

# Bad: Missing types
def process(data):
    return UserModel(**data)
```

## Testing Standards

```python
# Good: Clear, AAA pattern (Arrange-Act-Assert)
def test_user_validation_rejects_invalid_email():
    """Reject user creation with invalid email format."""
    with pytest.raises(ValidationError, match="email"):
        User(email="invalid")

# Bad: Unclear intent
def test_user():
    try:
        User(email="bad")
        assert False
    except:
        pass

# Mocking with pytest-mock
def test_api_call(mocker):
    """Verify API client handles retries correctly."""
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200

    response = fetch_data("https://api.example.com")

    assert mock_get.call_count == 1
    assert response.ok
```

## Error Handling

```python
# Good: Specific exceptions with context
def load_config(path: Path) -> Config:
    """Load and validate configuration from file.

    Raises:
        FileNotFoundError: Config file doesn't exist
        ValidationError: Config fails schema validation
    """
    if not path.exists():
        raise FileNotFoundError(f"Config missing: {path}")

    raw_data = json.loads(path.read_text())
    return Config.model_validate(raw_data)

# Bad: Generic exceptions
def load_config(path):
    try:
        return Config(**json.load(open(path)))
    except Exception:
        raise Exception("Error")
```

## Project Structure

```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py      # Pydantic models
│       ├── config.py      # Settings with @lru_cache
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Shared fixtures
│   └── test_main.py
├── pyproject.toml
├── uv.lock
├── .env.example
└── README.md
```

## CI/CD Pipeline

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3

      - name: Install dependencies
        run: uv sync --frozen

      - name: Lint
        run: uv run ruff check .

      - name: Format check
        run: uv run ruff format --check .

      - name: Type check
        run: uv run mypy src/ --strict

      - name: Test
        run: uv run pytest --cov=src --cov-fail-under=80 --cov-report=xml

      - name: Security scan
        run: uv run bandit -r src/ -f json -o bandit-report.json

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
```

## Code Review Checklist

**Before submitting PR:**

- [ ] All tests pass locally
- [ ] Coverage ≥80%
- [ ] No ruff/mypy errors
- [ ] No hardcoded secrets (grep check)
- [ ] Docstrings on public APIs
- [ ] README updated if needed
- [ ] Migration plan for breaking changes

**Reviewer checks:**

- [ ] Logic correctness
- [ ] Error handling complete
- [ ] No SQL injection / XSS vectors
- [ ] Performance implications considered
- [ ] Tests cover edge cases
- [ ] No code duplication

## Common Patterns

### API Client with Retry

```python
from pydantic import BaseModel
from requests.adapters import HTTPAdapter, Retry

class APIClient:
    """HTTP client with automatic retries."""

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.session = requests.Session()

        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def get(self, endpoint: str) -> dict:
        response = self.session.get(
            f"{self.base_url}/{endpoint}",
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
```

### Database Connection with Context Manager

```python
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

@contextmanager
def get_db_session():
    """Provide transactional scope for database operations."""
    engine = create_engine(get_settings().db_url)
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage
with get_db_session() as db:
    user = db.query(User).filter_by(id=1).first()
```

### CLI with Rich Output

```python
import typer
from rich.console import Console
from rich.progress import track

app = typer.Typer()
console = Console()

@app.command()
def process(
    input_file: Path = typer.Argument(..., help="Input CSV file"),
    verbose: bool = typer.Option(False, "--verbose", "-v")
):
    """Process data from CSV file."""
    if not input_file.exists():
        console.print(f"[red]Error: {input_file} not found[/red]")
        raise typer.Exit(1)

    data = load_csv(input_file)

    for item in track(data, description="Processing..."):
        process_item(item)

    console.print("[green]✓ Processing complete[/green]")

if __name__ == "__main__":
    app()
```

## Performance Guidelines

- Use `@lru_cache` for expensive pure functions
- Batch database operations (avoid N+1 queries)
- Use `asyncio` for I/O-bound operations
- Profile before optimizing: `python -m cProfile`
- Consider pagination for large datasets

## Quick Reference

| Task | Command |
|------|---------|
| Add dependency | `uv add package` |
| Dev dependency | `uv add --dev package` |
| Run tests | `uv run pytest -v` |
| Watch tests | `uv run pytest-watch` |
| Lint + fix | `uv run ruff check . --fix` |
| Format | `uv run ruff format .` |
| Type check | `uv run mypy src/` |
| Coverage report | `uv run pytest --cov=src --cov-report=html` |
| Security scan | `uv run bandit -r src/` |
| Dependency audit | `uv pip audit` |
| Generate requirements | `uv pip compile pyproject.toml` |

## Troubleshooting

**Import errors after adding dependency:**

```bash
uv sync  # Ensure lock file updated
```

**Tests fail in CI but pass locally:**

```bash
uv sync --frozen  # Use exact locked versions
uv run pytest -v  # Check for environment differences
```

**Type errors from third-party packages:**

```bash
uv add --dev types-requests  # Add type stubs
```

**Coverage too low:**

```bash
uv run pytest --cov=src --cov-report=html
# Open htmlcov/index.html to see uncovered lines
```

**Golden Rule**: If it's not in `uv.lock`, it's not in production.
