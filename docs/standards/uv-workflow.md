# UV Workflow Standards

## Dependency Management

```bash
uv init                    # Initialize
uv add <package>           # Add packages
uv sync --frozen           # Sync environment
```

## Package Management

- Use `uv` exclusively for packages, environments, and tool execution
- Always use `uv sync --locked` or `--frozen` in CI/CD
- Use `uv init`, `uv add`, and `uv sync` for workflow
- Use `uv python install` and `.python-version` files for Python versioning
- Manage monorepos using `[tool.uv.workspace]` in the root `pyproject.toml`

## Reproducibility

- Use `uv sync --frozen` to ensure reproducible environments
- In multi-stage Docker builds: Stage 1 (Builder): `uv sync --frozen --no-cache` to create `.venv`
- Cache `.uv-cache/` and `.venv/` in CI/CD systems
- Use `astral-sh/setup-uv@v5` with `enable-cache: true` for GitHub Actions

## Common Commands

```bash
uv sync                              # Build/Sync
uv run pytest                        # Run tests
ruff check . --fix && ruff format .  # Lint & fix
uv run pip-audit                     # Security check
```
