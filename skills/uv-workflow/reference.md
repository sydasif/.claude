# UV Command Reference

## Dependency Management

| Command | Action |
|---------|--------|
| `uv add <pkg>` | Add package to `pyproject.toml` |
| `uv add --dev <pkg>` | Add to dev dependencies |
| `uv remove <pkg>` | Uninstall package |
| `uv sync` | Sync environment with lock file |
| `uv sync --frozen` | CI/CD mode (fails if lock outdated) |
| `uv tree` | View dependency graph |

## Python Versioning

```bash
uv python install 3.12      # Install specific version
uv python pin 3.12          # Pin project to 3.12
```

## Tool Running

```bash
uv run <cmd>                # Run inside venv (e.g., uv run pytest)
uvx <tool>                  # Run ephemeral tool (e.g., uvx ruff check)
```

## Docker Optimization

Use these env vars in Dockerfiles for caching:

```dockerfile
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
RUN uv sync --frozen --no-dev
```
