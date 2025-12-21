# Code Quality Standards

## Linting & Formatting

- **Tool**: Ruff for linting and formatting
- **Line Limit**: 88-character line limit
- **Commands**:

  ```bash
  ruff check . --fix         # Lint
  ruff format .              # Format
  ```

## Code Review Checklist

- Code clarity and readability
- Meaningful function and variable names
- No duplicated or unnecessary logic
- Proper error handling and failure paths
- Input validation where applicable
- Tests updated or added when behavior changes
- Obvious performance risks identified

## Quality Requirements

- Follow existing structure, style, and patterns
- Do not add new tools or libraries without need
- Keep changes minimal and scoped
- Avoid unnecessary abstractions
- Keep behavior explicit
- Do not hide errors or failures
- Prefer simple, proven solutions
- Prioritize correctness and maintainability

## Execution Quality

- Do not run destructive commands
- Do not assume OS, Python version, or runtime
- Do not make external calls without approval
- Favor validation or dry-run modes
- Cross-check outputs against expectations
- Question surprising success or failure
