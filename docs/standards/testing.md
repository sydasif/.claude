# Testing Standards

## Framework & Requirements

- **Framework**: `pytest` with TDD workflow
- **Coverage**: 80% minimum coverage required
- **Testing Approach**: TDD workflow - Write tests first -> Watch fail -> Implement -> Refactor
- **Mocks**: Use `pytest-mock` (mocker fixture). Prefer integration tests for database logic.

## Testing Strategy

- Respect existing tests
- Update or add tests only when behavior changes
- If tests are missing, state what should be tested
- Never claim tests were run unless they were
- Do not assume tests exist
- Add tests only when behavior changes

## Quality Assurance

- Tests should be updated or added when behavior changes
- Focus on meaningful function and variable names
- Ensure proper error handling and failure paths
- Identify obvious performance risks
