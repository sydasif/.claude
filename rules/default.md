# Default Rules

General code quality rules applied to all file types that don't have language-specific rules. These rules represent universal software engineering best practices.

## Available Commands

There are no direct commands for this skill. It provides rules that are applied by other agents like the code-reviewer.

## Rules

### 1. Code Documentation and Comments

- All public functions/methods must have docstrings
- Complex logic should be explained with inline comments
- Remove commented-out code before committing
- Use clear, descriptive names that reduce need for comments

### 2. Error Handling

## Error Handling Standards

### Requirements

- Use specific exception types
- Log at appropriate level (debug/info/warning/error/critical)
- Take explicit action (return default, retry, raise, fallback)
- Include context in log messages

#### ❌ VIOLATIONS

**Silent failure:**

```python
try:
    critical_operation()
except:  # Too broad
    pass  # No logging, no action
```

**Wrong log level:**

```python
try:
    save_to_database()
except DatabaseError as e:
    logger.debug(f"Save failed: {e}")  # Should be error/critical
    return None  # Hiding critical failure
```

#### ✅ CORRECT PATTERNS

**Specific exception, logged, action taken:**

```python
try:
    process_payment(amount)
except ValueError as e:
    logger.warning(f"Invalid payment amount: {e}")
    return {"error": "Invalid amount", "details": str(e)}
except PaymentProviderError as e:
    logger.error(f"Payment provider failed: {e}")
    raise  # Re-raise critical errors
```

**With recovery:**

```python
try:
    data = fetch_from_cache()
except CacheTimeout:
    logger.info("Cache timeout, falling back to database")
    data = fetch_from_database()
```

### 3. Code Organization

- Keep functions small and focused on a single responsibility
- Limit function length to reasonable size (typically < 50 lines)
- Group related functionality together
- Use consistent indentation and formatting

### 4. Naming Conventions

- Use descriptive, meaningful names
- Follow language-specific naming conventions
- Avoid abbreviations that aren't widely understood
- Use consistent naming patterns throughout the codebase

### 5. Performance Considerations

- Avoid unnecessary computation in loops
- Use efficient algorithms and data structures
- Be mindful of memory usage
- Optimize for readability first, performance second

### 6. Security Best Practices

- Validate all user inputs
- Never hardcode secrets or credentials
- Use parameterized queries to prevent injection attacks
- Follow principle of least privilege

### 7. Testing

- Write testable code
- Cover edge cases in tests
- Use meaningful test names
- Keep tests independent and deterministic

### 8. Maintainability

- Avoid deep nesting levels (prefer < 3 levels)
- Remove dead code and unused imports
- Keep dependencies minimal and up-to-date
- Write code that others can easily understand and modify

## Usage Guidelines

Apply these rules to all file types that don't have specific language rules configured. These serve as baseline quality standards that complement language-specific rules.

## Best Practices

- Use these as baseline requirements in addition to language-specific rules
- Prioritize readability and maintainability
- Ensure consistent application across all code types
- Balance with project-specific requirements

## Security Considerations

- Validate all inputs regardless of source
- Never store secrets in code
- Use secure coding patterns consistently
- Follow the principle of least privilege

> Use this skill as a foundation for code quality assessment.
