---
name: code-refactoring
description: Modernize legacy Python code with best practices, type hints, and efficient patterns.
---

# Python Refactoring Specialist

This skill transforms legacy Python code into modern, maintainable, and
efficient implementations following current best practices.

For comprehensive Python best practices, see [Python Guidelines](../../guidelines/python.md)

For security requirements, refer to: [Security Rules](../../rules/security.md)

For tool usage, refer to: [Tool Commands](../../rules/tools.md)

## Refactoring Process

### 1. Assessment

1. Identify legacy patterns in the code
2. Prioritize refactoring based on impact and risk
3. Check for existing tests (ensure they exist before refactoring)

### 2. Safe Refactoring Steps

1. Run existing tests to establish baseline
2. Apply one refactoring pattern at a time
3. Run tests after each change
4. Verify functionality remains the same

### 3. Modernization Checklist

- [ ] All string formatting uses f-strings
- [ ] Path operations use `pathlib`
- [ ] Function signatures use type hints
- [ ] Keyword-only arguments are used where appropriate
- [ ] Data classes replace simple classes
- [ ] Context managers handle resources
- [ ] Exception handling is specific
- [ ] Iterations use appropriate patterns (enumerate, comprehension)
- [ ] Lambda functions are moved to named functions if complex
- [ ] Imports are organized in standard groups

## Quality Assurance

For detailed tool commands, see [Tool Commands](../../rules/tools.md).

### Before Refactoring

Run type checking, linting, and tests to establish baseline.

### After Refactoring

Verify refactored code passes all checks:
- Type checking
- Linting  
- Unit tests
- Coverage analysis

## Common Refactoring Scenarios

### Scenario 1: Migrate to f-strings

```python
# Find all % formatting and .format() calls
# Replace with equivalent f-string expressions
# Preserve alignment and formatting options
```

### Scenario 2: Migrate to dataclasses

```python
# Identify simple classes with only attributes
# Add @dataclass decorator
# Add type hints to attributes
# Remove boilerplate methods (__init__, __repr__, __eq__)
```

### Scenario 3: Migrate to pathlib

```python
# Identify all os.path.* usage
# Replace with pathlib.Path equivalents
# Update path concatenation to use /
# Ensure cross-platform compatibility
```

---

Use this skill to modernize legacy Python code into clean, maintainable, and efficient implementations using contemporary Python features and best practices.
