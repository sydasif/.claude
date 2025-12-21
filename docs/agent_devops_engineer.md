# Comprehensive DevOps & UV Guide

## Containerization Standards

- **Base Images**: Use `debian-slim` or `distroless`. Never run as `root`; use `USER app` (UID 1000).
- **Multi-Stage Builds**:
    1. **Stage 1 (Builder)**: `uv sync --frozen --no-cache` to create `.venv`.
    2. **Stage 2 (Runtime)**: Copy `.venv` and application code.
- **Security**: Implement `HEALTHCHECK` and scan images for vulnerabilities.

## UV Tooling & Dependency Management

- **Workflow**: Use `uv init`, `uv add`, and `uv sync`.
- **Reproducibility**: Always use `uv sync --locked` or `--frozen` in CI/CD.
- **Workspace**: Manage monorepos using `[tool.uv.workspace]` in the root `pyproject.toml`.
- **Python Versioning**: Use `uv python install` and `.python-version` files.

## Configuration Management

- **Settings**: Use `Pydantic Settings` for env var validation.
- **Caching**: Wrap settings in `@lru_cache()` to avoid repeated file system access.
- **Environment**: Support `.env` for local and real env vars for production.
- **Secret Management**: Never commit sensitive values. Rotate secrets via environment configuration.

## CI/CD Recipes

- **GitHub Actions**: Use `astral-sh/setup-uv@v5` with `enable-cache: true`.
- **GitLab CI**: Cache `.uv-cache/` and `.venv/`. Use `JOB-TOKEN` for internal package registries.
