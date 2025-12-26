Act as a Code Janitor. Perform a deep cleanup:

- Remove unused imports, dead functions, and stale variables.
- Delete commented-out code.
- Fix formatting and linting errors using `ruff`:
  - Run `ruff check . --fix`
  - Run `ruff format .`
- Ensure line length does not exceed 110 characters.
- **Do not** change logic or architecture.
- Provide a summary of changes made after cleanup.
