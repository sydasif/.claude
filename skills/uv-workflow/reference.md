# UV Command Reference

Complete command reference for Python projects.

## Essential Commands

```bash
# Project setup
uv init [path]                      # Initialize project
uv add <package>                    # Add dependency
uv add --dev <package>              # Add dev dependency
uv add --group <name> <package>     # Add to group
uv remove <package>                 # Remove dependency

# Environment sync
uv sync                             # Sync environment
uv sync --frozen                    # Reproducible (CI/CD)
uv sync --group <name>              # Include group
uv sync --no-dev                    # Production only

# Running code
uv run <command>                    # Run in environment
uvx <tool>                          # Run tool without install

# Python versions
uv python install 3.11              # Install Python
uv python list                      # List versions
echo "3.11" > .python-version       # Set version

# Maintenance
uv lock                             # Update lock file
uv export -o requirements.txt       # Export dependencies
uv cache clean                      # Clear cache
```

## Python Packages

```bash
# Web development
uv add flask                        # Web framework
uv add fastapi                      # Modern web framework
uv add django                       # Full-stack framework
uv add requests                     # HTTP library

# Data science
uv add pandas                       # Data manipulation
uv add numpy                        # Numerical computing
uv add matplotlib                   # Plotting library
uv add scikit-learn                # Machine learning

# Async
uv add httpx                        # Async HTTP client
uv add aiohttp                      # Async web client/server
uv add asyncio                      # Async standard library

# APIs and validation
uv add pydantic                     # Data validation
uv add aiohttp                      # Async HTTP client/server

# Development
uv add --dev pytest                 # Testing
uv add --dev pytest-mock            # Mocking
uv add --dev ruff                   # Linting
uv add --dev mypy                   # Type checking
uv add --dev ipython                # Interactive shell
```

## Project Configuration

```toml
# pyproject.toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.30.0",
    "pydantic>=2.0.0",
]

[dependency-groups]
dev = ["pytest>=7.4.0", "ruff>=0.1.0"]
web = ["flask>=2.0.0", "gunicorn>=20.0.0"]
data = ["pandas>=1.5.0", "numpy>=1.20.0"]
async = ["httpx>=0.25.0", "aiofiles>=23.0.0"]
```

## Environment Variables

```bash
UV_CACHE_DIR=/tmp/.uv              # Cache location
UV_NO_CACHE=true                   # Disable cache
UV_COMPILE_BYTECODE=1              # Compile (Docker)
UV_LINK_MODE=copy                  # Copy mode (Docker)
```

## CI/CD Patterns

### GitHub Actions

```yaml
steps:
  - uses: astral-sh/setup-uv@v5
    with:
      enable-cache: true
      cache-dependency-glob: "uv.lock"
  - run: uv python install
  - run: uv sync --frozen
  - run: uv run pytest
```

### GitLab CI

```yaml
variables:
  UV_CACHE_DIR: .uv-cache

cache:
  paths: [.uv-cache/, .venv/]

before_script:
  - curl -LsSf https://astral.sh/uv/install.sh | sh
  - export PATH="$HOME/.cargo/bin:$PATH"
  - uv sync --frozen
```

## Docker

```dockerfile
# Copy UV from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-cache

# Set environment
ENV PATH="/app/.venv/bin:$PATH"
```

## Version Constraints

```bash
uv add package                     # Latest
uv add package==1.2.3              # Exact
uv add 'package>=1.2.0'            # Minimum
uv add 'package<2.0.0'             # Maximum
uv add 'package>=1.2,<2.0'         # Range
```

## Troubleshooting

```bash
# Lock file issues
uv lock && uv sync

# Clear cache
uv cache clean

# Recreate environment
rm -rf .venv && uv sync

# Debug output
uv -vv sync
```
