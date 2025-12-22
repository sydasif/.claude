# UV Project Examples

Production-ready patterns using Pydantic v2 and proper project layout.

## 1. Data Processing Script (Flat Layout)

Use for simple, single-file tasks.

```bash
uv init data-processor && cd data-processor
uv add pandas
```

```python
# hello.py
import pandas as pd
from pathlib import Path

def process(input_path: Path):
    df = pd.read_csv(input_path)
    print(f"Processed {len(df)} rows")

if __name__ == "__main__":
    process(Path("data.csv"))
```

## 2. API Client (Pydantic v2)

**Requirement**: Use `model_validate`, `model_dump`, and `field_validator`.

```python
from pydantic import BaseModel, Field, ConfigDict, field_validator
import requests

class User(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    username: str
    email: str

    @field_validator('username')
    @classmethod
    def validate_user(cls, v):
        if not v.isalnum():
            raise ValueError('Must be alphanumeric')
        return v

def get_user(user_id: int) -> User:
    resp = requests.get(f"https://api.example.com/users/{user_id}")
    resp.raise_for_status()
    # Pydantic v2 syntax
    return User.model_validate(resp.json())
```

## 3. Full Application (Src Layout)

**Use this for all "projects" or "apps".**

```bash
uv init my-app --app
uv add fastapi pydantic uvicorn
uv add --dev pytest ruff
```

**Structure:**

```text
my-app/
├── pyproject.toml
├── src/
│   └── my_app/
│       ├── __init__.py
│       └── main.py
└── tests/
```

**Code:**

```python
# src/my_app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```
