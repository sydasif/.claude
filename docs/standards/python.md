# Python Standards

## Version Requirements

- **Python Version**: 3.11+ mandatory
- **Package Manager**: `uv` exclusively for packages, environments, and tool execution

## Framework & Libraries

- **Validation**: Strict Pydantic v2 for data structures and configuration
- **Testing**: `pytest` with TDD workflow; 80% minimum coverage required
- **Linting & Style**: Ruff (88-character line limit)

## Best Practices

- Write clear and readable code
- Avoid unnecessary abstractions
- Keep behavior explicit
- Do not hide errors or failures
- Favor straightforward solutions over clever abstractions
- Do not implement features until required
- Robust validation at boundaries using Pydantic v2
