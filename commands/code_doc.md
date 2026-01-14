Generate production-grade documentation following project conventions.

## Scope Priority

1. Public API functions/classes (user-facing)
2. Complex algorithms (cognitive complexity > 7)
3. Data models and validators
4. Configuration and settings classes

## Documentation Format

### Google-Style Docstrings

```python
def process_data(input_path: Path, validate: bool = True) -> pd.DataFrame:
    """Load and validate data from CSV file.

    Args:
        input_path: Path to CSV file containing raw data
        validate: Whether to run Pydantic validation on loaded data

    Returns:
        Validated DataFrame with standardized column names

    Raises:
        ValidationError: If validate=True and data fails schema checks
        FileNotFoundError: If input_path does not exist

    Example:
        >>> df = process_data(Path("data.csv"))
        >>> assert df.shape[0] > 0
    """
```

### Class Documentation

```python
class DataProcessor:
    """Handles ETL pipeline for customer data.

    Responsibilities:
    - Load CSV/JSON sources
    - Apply Pydantic validation
    - Transform to standard schema
    - Export to database

    Attributes:
        schema: Pydantic model for validation
        batch_size: Records per database commit

    Example:
        processor = DataProcessor(schema=CustomerModel)
        processor.process(Path("customers.csv"))
    """
```

## Rules

- First line: One-sentence summary (imperative mood: "Load data" not "Loads data")
- Args/Returns: Be specific about types beyond type hints
- Examples: Show actual usage, not pseudo-code
- Raises: Document expected exceptions only
- Avoid: "This function...", "This class...", filler words

## Automation

```bash
# Generate stubs for missing docs
uv run interrogate src/ -v

# Validate docstring coverage
uv run interrogate src/ --fail-under 80
```

Only document what adds value. Skip obvious getters/setters.
