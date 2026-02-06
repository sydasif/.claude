# Python Testing Best Practices and Guidelines

This document contains centralized Python testing best practices to be referenced by various skills and agents.

## Modern Python Testing Standards (3.12+)

### Core Testing Framework

- Use **pytest** for all testing needs (the de facto standard as of 2026)
- Write **parametrized tests** to cover multiple scenarios efficiently
- Use **fixtures** for test setup/teardown and resource management
- Implement **property-based testing** with `hypothesis` for robust validation
- Maintain **high test coverage** with emphasis on branch coverage over line coverage

### Test Organization

- Place tests in `tests/` directory
- Mirror source structure: `src/module.py` → `tests/test_module.py`
- Use descriptive test names: `test_calculate_total_with_discount()`
- Group related tests in classes: `TestClassCalculator`
- Separate unit, integration, and end-to-end tests when appropriate

## Testing Standards and Requirements

### Test Coverage Requirements

**By Component Criticality:**

| Component Type | Branch Coverage | Rationale |
| --- | --- | --- |
| Business logic | 95%+ | Core value, high risk |
| API endpoints | 90%+ | User-facing |
| Data models/validation | 85%+ | Data integrity |
| CLI tools | 70%+ | Integration tests sufficient |
| Utilities | 80%+ | Pure functions |
| Config/constants | 60%+ | Low complexity |

**Use Branch Coverage, Not Line:**

For coverage commands, see [Tool Guidelines](~/.claude/shared/tools.md).

#### Don't Chase 100%

- Some code isn't worth testing (`__repr__`, simple getters, logging)
- Focus on **risk areas**, not percentage
- Use coverage to find **untested code**, not as a goal

### Test Patterns and Examples

#### Basic Unit Test

```python
def test_addition():
    """Test basic addition."""
    assert Calculator.add(2, 3) == 5
```

#### Parametrized Test

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_addition_parametrized(a, b, expected):
    """Test addition with multiple inputs."""
    assert Calculator.add(a, b) == expected
```

#### Property-Based Test

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    """Test that addition is commutative."""
    assert Calculator.add(a, b) == Calculator.add(b, a)
```

#### Test with Fixture

```python
@pytest.fixture
def calculator():
    """Provide a calculator instance."""
    return Calculator()

def test_calculator_initial_state(calculator):
    """Test calculator starts with zero."""
    assert calculator.memory == 0
```

#### Mock Test

```python
def test_save_to_database(mocker):
    """Test saving data to database."""
    mock_db_connection = mocker.patch('myapp.database.Connection')
    service = DataService(db_conn=mock_db_connection)
    result = service.save_data({"id": 1, "name": "Test"})

    mock_db_connection.insert.assert_called_once()
    assert result is True
```

## Advanced Testing Patterns

### Testing Classes

```python
class TestCalculator:
    def setup_method(self):
        """Setup for each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        result = self.calc.add(2, 3)
        assert result == 5

    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.multiply(3, 4)
        assert result == 12
```

### Testing Async Code

```python
import asyncio
import pytest

@pytest.mark.asyncio
async def test_async_api_call():
    """Test async API call."""
    api_client = ApiClient()
    result = await api_client.fetch_data("endpoint")

    assert isinstance(result, dict)
    assert "data" in result
```

### Testing Error Conditions

```python
def test_division_by_zero():
    """Test division by zero raises error."""
    calc = Calculator()

    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
```

## Integration Testing

### Database Integration Tests

```python
@pytest.fixture(scope="session")
def db_connection():
    """Create database connection for tests."""
    # Setup
    conn = create_test_database()
    yield conn
    # Teardown
    destroy_test_database(conn)

def test_create_user(db_connection):
    """Test creating a user in database."""
    user_service = UserService(db_connection)
    user = user_service.create_user("john@example.com", "John Doe")

    assert user.id is not None
    assert user.email == "john@example.com"
```

### API Integration Tests

```python
@pytest.fixture
def api_client():
    """Create test API client."""
    app = create_app()
    with TestClient(app) as client:
        yield client

def test_get_user_endpoint(api_client):
    """Test GET /users/{id} endpoint."""
    response = api_client.get("/users/1")

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
```

## Performance and Load Testing

### Benchmark Tests

```python
import pytest_benchmark

def test_heavy_calculation_performance(benchmark):
    """Benchmark heavy calculation."""
    def run_calc():
        return HeavyCalculator().perform_calculation(large_dataset)

    result = benchmark(run_calc)
    assert result is not None
```

### Load Testing Preparation

```python
# Prepare test data for load testing
@pytest.fixture
def sample_users():
    """Generate sample users for testing."""
    return [
        {"name": f"user_{i}", "email": f"user_{i}@example.com"}
        for i in range(1000)
    ]
```

## Security Testing

### Input Validation Tests

```python
def test_sql_injection_prevention():
    """Test that SQL injection attempts are prevented."""
    db_service = DatabaseService()

    malicious_input = "'; DROP TABLE users; --"
    result = db_service.get_user_by_name(malicious_input)

    # Should handle malicious input safely
    assert result is None or isinstance(result, list) and len(result) == 0
```

### Authentication Tests

```python
def test_unauthorized_access():
    """Test that unauthorized access is prevented."""
    client = TestClient(create_app())

    response = client.get("/admin/dashboard")

    assert response.status_code == 401  # Unauthorized
```

## Test Quality Standards

### AAA Pattern (Arrange, Act, Assert)

1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute the function or method under test
3. **Assert**: Verify the expected outcome

### Test Isolation

- Each test should be independent and not rely on others
- Use fixtures for setup/teardown
- Clean up after tests to avoid side effects
- Avoid shared mutable state between tests

### Test Documentation

- Include meaningful docstrings for complex test cases
- Document the purpose and expected behavior
- Explain why certain edge cases are important to test

## Continuous Integration and Delivery

### Pre-commit Checks

For testing commands, see [Tool Guidelines](~/.claude/shared/tools.md).

```bash
# Run tests before committing
pytest
# With coverage (see tools.md for full command examples)
pytest --cov=src --cov-fail-under=90
```

### CI/CD Pipeline Example

```yaml
name: Python Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']

    steps:
      - uses: actions/checkout@v3

      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --dev

      - name: Run type checking
        run: uv run mypy src/

      - name: Run linting
        run: uv run ruff check src/

      - name: Run tests with coverage
        run: uv run pytest --cov=src --cov-report=xml
```

## Test Naming Conventions

- Use `test_` prefix for all test functions
- Make names descriptive and include expected outcome
- Follow the pattern: `test_[functionality]_[scenario]_[expected_result]`
- Group related tests in classes with `Test` prefix

## Testing Anti-Patterns to Avoid

### 1. Test Chaining

```python
# ❌ DON'T: Tests depending on each other
def test_create_user():
    # Creates user for next test
    pass

def test_update_user():
    # Depends on test_create_user running first
    pass
```

```python
# ✅ DO: Independent tests
def test_create_user():
    # Self-contained test
    pass

def test_update_user():
    # Sets up its own prerequisites
    pass
```

### 2. Over-Mocking

```python
# ❌ DON'T: Mock everything
def test_calculator_add(mocker):
    calc_mock = mocker.Mock()
    calc_mock.add.return_value = 5
    assert calc_mock.add(2, 3) == 5  # Testing the mock, not the code
```

### 3. Flaky Tests

- Avoid tests that sometimes pass and sometimes fail
- Don't depend on external services without proper mocking
- Avoid relying on timing or ordering when possible

## Performance Considerations

### Fast Tests

- Keep individual tests under 100ms when possible
- Use fixtures to share expensive setup
- Separate slow integration tests from fast unit tests
- Consider using pytest markers to run subsets of tests

### Resource Management

- Use fixtures with proper teardown for resource cleanup
- Close file handles, database connections, and network resources
- Consider using `tmp_path` fixture for temporary files

---

**Note**: This document should be referenced by testing-related skills and agents to ensure consistent testing practices across projects.
