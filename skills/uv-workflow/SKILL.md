---
name: uv-workflow
description: UV package manager for Python projects. Use when setting up Python projects, managing dependencies, or setting up CI/CD for Python applications.
---

# UV Workflow for Python Projects

Fast Python dependency management for Python projects with common libraries and frameworks.

## Quick Commands

```bash
uv init                    # Initialize project
uv add requests flask      # Add dependencies
uv sync --frozen           # Reproducible sync (CI/CD)
uv run python script.py    # Run script
```

## Common Python Stack

```bash
# Web development
uv add flask fastapi django

# Data science
uv add pandas numpy matplotlib

# HTTP and APIs
uv add requests httpx aiohttp

# Development
uv add --dev pytest ruff
```

## Basic Workflow

```bash
# 1. Initialize
uv init my-project && cd my-project

# 2. Add libraries
uv add requests flask

# 3. Create script
cat > scripts/main.py << 'EOF'
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    data = fetch_data('https://api.github.com/users/octocat')
    print(data)
EOF

# 4. Run
uv run python scripts/main.py
```

## Project Structure

```text
my-project/
├── .python-version        # Python version
├── pyproject.toml         # Dependencies
├── uv.lock               # Lock file (commit to git!)
├── scripts/              # Python scripts
├── src/                  # Source code
├── templates/            # Jinja2 templates
└── tests/               # Tests
```

## Dependency Groups

```toml
[dependency-groups]
dev = ["pytest>=7.4.0", "ruff>=0.1.0"]
web = ["flask>=2.0.0", "gunicorn>=20.0.0"]
data = ["pandas>=1.5.0", "numpy>=1.20.0"]
async = ["httpx>=0.25.0", "aiofiles>=23.0.0"]
```

Install groups:

```bash
uv sync --group web
```

## CI/CD Integration

GitHub Actions:

```yaml
- uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
- run: uv sync --frozen
- run: uv run pytest
```

## Best Practices

- ✅ Use `uv sync --frozen` in CI/CD
- ✅ Commit `uv.lock` to version control
- ✅ Use dependency groups for organization
- ✅ Cache `.uv-cache/` and `.venv/` in CI

## Need More Details?

- For complete command reference: see [reference.md](reference.md)
- For real-world examples: see [examples.md](examples.md)
