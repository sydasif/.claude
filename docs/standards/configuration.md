# Configuration Management Standards

## Settings & Validation

- **Settings Framework**: Use `Pydantic Settings` for environment variable validation
- **Caching**: Wrap settings in `@lru_cache()` to avoid repeated file system access
- **Validation**: Strict Pydantic v2 for data structures and configuration
- **Fail Fast**: Robust validation at boundaries using Pydantic v2

## Environment Management

- **Local Development**: Support `.env` files for local environment
- **Production**: Use real environment variables for production
- **Environment Variables**: Use for sensitive data and configuration values
- **Python Versioning**: Use `uv python install` and `.python-version` files

## Secret Management

- **No Hard-coded Values**: Never commit sensitive values
- **SSH Authentication**: Enable SSH key-based authentication where possible
- **Secret Rotation**: Rotate secrets via environment configuration
- **Security**: Use environment variables for credentials

## Configuration Patterns

- **Multi-Stage Builds**: In Docker - Stage 1 (Builder): `uv sync --frozen --no-cache` to create `.venv`, Stage 2 (Runtime): Copy `.venv` and application code
- **Workspace Management**: Manage monorepos using `[tool.uv.workspace]` in the root `pyproject.toml`
- **YAML Inventory**: Use hosts and groups structure for variable inheritance (for network automation)
- **Jinja2 Templates**: Generate configurations using standardized templates
