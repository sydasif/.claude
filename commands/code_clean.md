Execute comprehensive cleanup following project standards:

## Pre-flight Checks

```bash
# Verify git status is clean or changes are stashed
git status --short
```

## Cleanup Pipeline

### Phase 1: Automated Fixes

```bash
# Remove unused imports and fix linting
uv run ruff check . --fix --select F401,I001,UP

# Apply formatting (110 char limit per standards.md)
uv run ruff format .
```

### Phase 2: Dead Code Detection

```bash
# Find unused functions (requires vulture)
uv run vulture src/ --min-confidence 80
```

Manual review for:

- Commented code blocks (`#` followed by code patterns)
- Unused imports after auto-fix
- Variables assigned but never read
- Functions with no callers

### Phase 3: Type Safety

```bash
# Run type checker
uv run mypy src/ --strict
```

### Phase 4: Validation

```bash
# Ensure tests still pass
uv run pytest

# Verify no ruff errors remain
uv run ruff check .
```

## Summary Template

After completion, report:

- Lines of code removed
- Imports cleaned
- Formatting fixes applied
- Dead code locations (manual review needed)
- Type errors found/fixed
- Test status: PASS/FAIL

**Note:** Never modify business logic. Only cleanup presentation.
