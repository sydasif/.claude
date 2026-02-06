# Testing Rules (Always-On)

Testing requirements and verification standards that must always be followed.

## Core Requirements

### Before Any Code Change
- Run existing tests to establish baseline
- Ensure tests pass before modifying code
- Never commit broken tests

### Coverage Requirements

| Component Type | Branch Coverage | Rationale |
|----------------|-----------------|-----------|
| Business logic | 95%+ | Core value, high risk |
| API endpoints | 90%+ | User-facing |
| Data models/validation | 85%+ | Data integrity |
| CLI tools | 70%+ | Integration tests sufficient |
| Utilities | 80%+ | Pure functions |
| Config/constants | 60%+ | Low complexity |

**Use Branch Coverage, not Line Coverage.**

## Verification Pyramid (Required)

For every change, you MUST verify:

- [ ] **Static**: Linter/Type-checker passes
- [ ] **Positive**: Test case for expected behavior passes
- [ ] **Negative**: Test case for bad input/error handling passes
- [ ] **Regression**: Existing tests still pass
- [ ] **Rollback**: Rollback procedure tested

## Test Quality Standards

### Test Isolation
- Each test must be independent
- Use fixtures for setup/teardown
- Clean up after tests (no side effects)
- Avoid shared mutable state

### Test Naming
- Use `test_` prefix
- Pattern: `test_[functionality]_[scenario]_[expected]`
- Example: `test_calculate_total_with_discount()`

### AAA Pattern (Arrange, Act, Assert)
1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute function under test
3. **Assert**: Verify expected outcome

## Anti-Patterns to Avoid

### 1. Test Chaining (FORBIDDEN)

```python
# ❌ NEVER - Tests depending on each other
def test_create_user():
    pass  # Creates user for next test

def test_update_user():
    pass  # Depends on test_create_user

# ✅ ALWAYS - Independent tests
def test_create_user():
    # Self-contained
    pass

def test_update_user():
    # Sets up its own prerequisites
    pass
```

### 2. Over-Mocking

```python
# ❌ DON'T - Testing the mock, not the code
def test_calculator_add(mocker):
    calc_mock = mocker.Mock()
    calc_mock.add.return_value = 5
    assert calc_mock.add(2, 3) == 5
```

### 3. Flaky Tests
- Avoid tests that sometimes pass/fail
- Don't depend on external services without mocking
- Avoid timing-dependent tests

## Pre-Commit Requirements

```bash
# Run before every commit
pytest
pytest --cov=src --cov-fail-under=90
```

## When Testing Is Complete

You are not "done" until:
- All verification pyramid items checked
- Static analysis passes
- Coverage meets minimum thresholds
- No flaky tests introduced
