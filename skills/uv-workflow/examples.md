# Python Project Examples

Production-ready examples for Python projects with UV.

## 1. Data Processing Script

```bash
# Setup
uv init data-processor && cd data-processor
uv add pandas pyyaml
```

```python
# scripts/process_data.py
import pandas as pd
from pathlib import Path
from datetime import datetime
import yaml

def process_csv(input_file, output_dir):
    df = pd.read_csv(input_file)

    # Perform some data transformations
    processed_df = df.fillna(0)  # Fill missing values
    summary = processed_df.describe()

    # Save processed data
    output_path = Path(output_dir) / f"processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(output_path, index=False)

    # Save summary
    summary_path = Path(output_dir) / "summary.txt"
    with open(summary_path, 'w') as f:
        f.write(str(summary))

    return f'Processed {len(df)} rows, saved to {output_path}'

if __name__ == '__main__':
    # Example usage
    import io
    # Create sample data for demonstration
    sample_data = """name,age,score
    Alice,25,85
    Bob,30,92
    Charlie,35,78
    """
    Path('data').mkdir(exist_ok=True)
    Path('data/sample.csv').write_text(sample_data)

    result = process_csv('data/sample.csv', 'output')
    print(result)
```

Run: `uv run python scripts/process_data.py`

---

## 2. Flask Web Application

```bash
# Setup
uv init flask-app && cd flask-app
uv add flask requests
```

```python
# app.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Flask app!'})

@app.route('/api/data')
def get_data():
    # Example API call
    try:
        response = requests.get('https://api.github.com/users/octocat')
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({
        'message': 'User created',
        'user': data
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Run: `uv run python app.py`

---

## 3. API Client with Pydantic

```bash
# Setup
uv init api-client && cd api-client
uv add requests pydantic httpx
```

```python
# client.py
import requests
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    public_repos: int

class GitHubClient:
    def __init__(self, base_url: str = "https://api.github.com"):
        self.base_url = base_url

    def get_user(self, username: str) -> User:
        response = requests.get(f"{self.base_url}/users/{username}")
        response.raise_for_status()
        return User(**response.json())

    def search_users(self, query: str) -> List[User]:
        response = requests.get(f"{self.base_url}/search/users", params={"q": query})
        response.raise_for_status()
        users_data = response.json()["items"]
        return [User(**user_data) for user_data in users_data[:5]]  # Limit to 5 results

if __name__ == "__main__":
    client = GitHubClient()

    # Get specific user
    user = client.get_user("octocat")
    print(f"User: {user.name} (@{user.login}) has {user.public_repos} public repos")

    # Search users
    results = client.search_users("python")
    print(f"Found {len(results)} users")
    for user in results:
        print(f"  - {user.login} ({user.public_repos} repos)")
```

Run: `uv run python client.py`

---

## 4. Async Web Scraping

```bash
# Setup
uv init async-scraper && cd async-scraper
uv add --group async httpx aiofiles beautifulsoup4
```

```python
# scraper.py
import asyncio
import httpx
from bs4 import BeautifulSoup
from pathlib import Path

async def fetch_page(client, url):
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.text
    except httpx.RequestError as e:
        print(f"Error fetching {url}: {e}")
        return None

async def scrape_url(session, url, index):
    html = await fetch_page(session, url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')
        title_text = title.get_text() if title else "No title"

        # Save content to file
        filename = f"page_{index}.html"
        filepath = Path("scraped_pages") / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(html, encoding='utf-8')

        return f"Scraped {url} - Title: {title_text[:50]}..."
    return f"Failed to scrape {url}"

async def main():
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://example.com"
    ]

    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [scrape_url(client, url, i) for i, url in enumerate(urls)]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

Run: `uv sync --group async && uv run python scraper.py`

---

## 5. CLI Tool with Typer

```bash
# Setup
uv init cli-tool && cd cli-tool
uv add typer rich
```

```python
# cli.py
import typer
from pathlib import Path
from typing import Optional
import json

app = typer.Typer()

@app.command()
def greet(name: str, greeting: str = "Hello", excited: bool = False):
    """Greet someone with a personalized message."""
    punctuation = "!" if excited else "."
    message = f"{greeting} {name}{punctuation}"
    typer.echo(message)

@app.command()
def count_words(file_path: Path, output: Optional[Path] = None):
    """Count words in a text file and optionally save results."""
    if not file_path.exists():
        typer.echo(f"Error: File {file_path} does not exist", err=True)
        raise typer.Exit(code=1)

    content = file_path.read_text()
    word_count = len(content.split())
    char_count = len(content)
    line_count = len(content.splitlines())

    result = {
        "file": str(file_path),
        "words": word_count,
        "characters": char_count,
        "lines": line_count
    }

    if output:
        output.write_text(json.dumps(result, indent=2))
        typer.echo(f"Results saved to {output}")
    else:
        typer.echo(f"File: {file_path}")
        typer.echo(f"Words: {word_count}")
        typer.echo(f"Characters: {char_count}")
        typer.echo(f"Lines: {line_count}")

@app.command()
def generate_password(length: int = 12, include_symbols: bool = True):
    """Generate a random password."""
    import secrets
    import string

    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += "!@#$%^&*"

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    typer.echo(password)

if __name__ == "__main__":
    app()
```

Run: `uv run python cli.py --help`

---

## 6. Data Validation with Pydantic

```bash
# Setup
uv init data-validator && cd data-validator
uv add pydantic email-validator
```

```python
# validator.py
from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List, Optional
from datetime import datetime
import json

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    signup_date: datetime
    is_active: bool = True
    tags: List[str] = []

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty or whitespace')
        return v.strip()

class UserDatabase:
    def __init__(self):
        self.users = []

    def add_user(self, user_data: dict) -> User:
        """Add a user after validating the data."""
        try:
            user = User(**user_data)
            self.users.append(user)
            return user
        except ValidationError as e:
            print(f"Validation error: {e}")
            raise

    def find_user_by_email(self, email: str) -> Optional[User]:
        """Find a user by email address."""
        for user in self.users:
            if user.email == email:
                return user
        return None

    def export_users(self, filename: str):
        """Export all users to a JSON file."""
        with open(filename, 'w') as f:
            json.dump([user.dict() for user in self.users], f, indent=2, default=str)

if __name__ == "__main__":
    db = UserDatabase()

    # Valid user
    valid_user_data = {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "age": 30,
        "signup_date": datetime.now(),
        "is_active": True,
        "tags": ["admin", "premium"]
    }

    try:
        user = db.add_user(valid_user_data)
        print(f"Added user: {user.name} ({user.email})")
    except ValidationError:
        print("Failed to add user due to validation errors")

    # Invalid user (negative age)
    invalid_user_data = {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "age": -5,  # Invalid: negative age
        "signup_date": datetime.now(),
        "is_active": True
    }

    try:
        db.add_user(invalid_user_data)
    except ValidationError:
        print("Correctly rejected invalid user data")
```

Run: `uv run python validator.py`

---

## 7. Testing with Pytest

```bash
# Setup
uv init test-project && cd test-project
uv add requests
uv add --dev pytest pytest-mock pytest-cov
```

```python
# calculator.py
"""Simple calculator module for testing examples."""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide two numbers, raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def fetch_user_data(user_id: int) -> dict:
    """Simulate fetching user data from an API."""
    # In a real application, this would make an API call
    import requests
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    response.raise_for_status()
    return response.json()
```

```python
# tests/test_calculator.py
import pytest
from calculator import add, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, 1, 0),
    (10.5, 2.5, 13),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

Run: `uv run pytest -v`

---

## 8. Complete Python Project Structure

```bash
# Setup
uv init my-python-project && cd my-python-project
uv add requests pydantic
uv add --dev pytest black mypy ruff
```

```toml
# pyproject.toml
[project]
name = "my-python-project"
version = "0.1.0"
description = "A complete Python project example"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28.0",
    "pydantic>=2.0.0",
]

[dependency-groups]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "mypy>=1.0.0",
    "ruff>=0.1.0",
]

[project.scripts]
my-app = "src.main:main"

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "mypy>=1.0.0",
    "ruff>=0.1.0",
]
```

```python
# src/main.py
"""Main application entry point."""

from typing import Optional
import requests
from pydantic import BaseModel

class Quote(BaseModel):
    text: str
    author: str
    tags: list[str]

def get_random_quote() -> Optional[Quote]:
    """Get a random quote from an API."""
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return Quote(
            text=data["content"],
            author=data["author"],
            tags=data.get("tags", [])
        )
    except requests.RequestException:
        return None

def main():
    """Main application function."""
    print("Random Quote Generator")
    print("-" * 20)

    quote = get_random_quote()
    if quote:
        print(f'"{quote.text}"')
        print(f"  — {quote.author}")
        if quote.tags:
            print(f"  Tags: {', '.join(quote.tags)}")
    else:
        print("Could not fetch a quote. Check your internet connection.")

if __name__ == "__main__":
    main()
```

Run: `uv run python src/main.py`

## Running Tests and Linting

```bash
# Run tests
uv run pytest

# Run linters
uv run ruff check .
uv run black --check .
uv run mypy .
```
