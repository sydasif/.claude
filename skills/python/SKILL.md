---
name: python
description: Universal coding standards, best practices, and patterns for Python development including FastAPI, Django, Flask, and data science applications.
---

# Python Coding Standards & Best Practices

Universal coding standards applicable across all Python projects.

## Code Quality Principles

### 1. Readability First

- Code is read more than written
- Clear variable and function names
- Self-documenting code preferred over comments
- Follow PEP 8 style guide
- Consistent formatting with Black or similar

### 2. KISS (Keep It Simple, Stupid)

- Simplest solution that works
- Avoid over-engineering
- No premature optimization
- Pythonic code > clever code

### 3. DRY (Don't Repeat Yourself)

- Extract common logic into functions
- Create reusable modules and classes
- Share utilities across packages
- Avoid copy-paste programming

### 4. YAGNI (You Aren't Gonna Need It)

- Don't build features before they're needed
- Avoid speculative generality
- Add complexity only when required
- Start simple, refactor when needed

## Python Standards

### Variable Naming

```python
# ✅ GOOD: Descriptive names (snake_case)
market_search_query = "election"
is_user_authenticated = True
total_revenue = 1000.0

# ❌ BAD: Unclear names
q = "election"
flag = True
x = 1000
```

### Function Naming

```python
# ✅ GOOD: Verb-noun pattern (snake_case)
async def fetch_market_data(market_id: str) -> dict:
    pass

def calculate_similarity(a: list[float], b: list[float]) -> float:
    pass

def is_valid_email(email: str) -> bool:
    pass

# ❌ BAD: Unclear or CamelCase for functions
async def Market(id: str):
    pass

def Similarity(a, b):
    pass

def email(e):
    pass
```

### Immutability Pattern (CRITICAL)

```python
# ✅ ALWAYS create new objects, don't mutate
updated_user = {
    **user,
    "name": "New Name"
}

updated_list = [*items, new_item]

# For dataclasses, use replace()
from dataclasses import dataclass, replace

@dataclass
class User:
    name: str
    age: int

updated_user = replace(user, name="New Name")

# ❌ NEVER mutate directly unless explicitly needed
user["name"] = "New Name"  # BAD
items.append(new_item)     # BAD (unless intentional)
```

### Error Handling

```python
# ✅ GOOD: Comprehensive error handling
import httpx

async def fetch_data(url: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code}")
        raise ValueError(f"Failed to fetch data: {e}")
    except httpx.RequestError as e:
        print(f"Request failed: {e}")
        raise ConnectionError("Network error occurred")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

# ❌ BAD: No error handling or bare except
async def fetch_data(url):
    response = await client.get(url)
    return response.json()

# ❌ BAD: Bare except
try:
    risky_operation()
except:  # Never do this
    pass
```

### Async/Await Best Practices

```python
import asyncio

# ✅ GOOD: Parallel execution when possible
users, markets, stats = await asyncio.gather(
    fetch_users(),
    fetch_markets(),
    fetch_stats()
)

# ❌ BAD: Sequential when unnecessary
users = await fetch_users()
markets = await fetch_markets()
stats = await fetch_stats()
```

### Type Hints

```python
from typing import Literal
from datetime import datetime

# ✅ GOOD: Proper type hints
class Market:
    id: str
    name: str
    status: Literal["active", "resolved", "closed"]
    created_at: datetime

async def get_market(market_id: str) -> Market:
    # Implementation
    pass

# Using TypedDict for dictionaries
from typing import TypedDict

class MarketDict(TypedDict):
    id: str
    name: str
    status: Literal["active", "resolved", "closed"]

def process_market(market: MarketDict) -> None:
    pass

# ❌ BAD: No type hints
def get_market(id):
    # Implementation
    pass
```

## FastAPI/Web Framework Best Practices

### Route Structure

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ✅ GOOD: Pydantic models with validation
class CreateMarketRequest(BaseModel):
    name: str
    description: str
    end_date: datetime
    categories: list[str]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Election 2024",
                "description": "Presidential election outcome",
                "end_date": "2024-11-05T00:00:00Z",
                "categories": ["politics", "elections"]
            }
        }

class MarketResponse(BaseModel):
    id: str
    name: str
    status: str
    created_at: datetime

@app.post("/markets", response_model=MarketResponse)
async def create_market(request: CreateMarketRequest) -> MarketResponse:
    # Validation happens automatically via Pydantic
    market = await save_market(request)
    return market

# ❌ BAD: No validation, unclear types
@app.post("/markets")
async def create_market(request: dict):
    return await save_market(request)
```

### Dependency Injection

```python
from fastapi import Depends
from sqlalchemy.orm import Session

# ✅ GOOD: Use FastAPI dependencies
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/markets/{market_id}")
async def get_market(
    market_id: str,
    db: Session = Depends(get_db)
) -> MarketResponse:
    market = db.query(Market).filter(Market.id == market_id).first()
    if not market:
        raise HTTPException(status_code=404, detail="Market not found")
    return market
```

### Custom Exceptions

```python
# ✅ GOOD: Custom exception hierarchy
class AppException(Exception):
    """Base exception for application errors"""
    pass

class ValidationError(AppException):
    """Raised when validation fails"""
    pass

class NotFoundError(AppException):
    """Raised when resource not found"""
    pass

class AuthenticationError(AppException):
    """Raised when authentication fails"""
    pass

# Usage
def get_user(user_id: str) -> User:
    user = db.get(user_id)
    if not user:
        raise NotFoundError(f"User {user_id} not found")
    return user
```

## Data Classes and Models

### Dataclasses

```python
from dataclasses import dataclass, field
from datetime import datetime

# ✅ GOOD: Dataclass with defaults and validation
@dataclass
class Market:
    id: str
    name: str
    status: Literal["active", "resolved", "closed"] = "active"
    created_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        if len(self.name) > 200:
            raise ValueError("Market name too long")

# ✅ GOOD: Frozen dataclass for immutability
@dataclass(frozen=True)
class User:
    id: str
    email: str
    created_at: datetime

# ❌ BAD: Mutable default arguments
@dataclass
class Market:
    id: str
    metadata: dict = {}  # DANGEROUS! Shared across instances
```

### Pydantic Models

```python
from pydantic import BaseModel, Field, field_validator

# ✅ GOOD: Pydantic for validation
class Market(BaseModel):
    id: str
    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=2000)
    end_date: datetime
    categories: list[str] = Field(..., min_length=1)

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, v):
        if len(v) > 10:
            raise ValueError("Too many categories")
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "123",
                "name": "Election 2024",
                "description": "Presidential election",
                "end_date": "2024-11-05T00:00:00Z",
                "categories": ["politics"]
            }
        }
    }
```

## API Design Standards

### REST API Conventions

```terminal
GET    /api/markets              # List all markets
GET    /api/markets/{id}         # Get specific market
POST   /api/markets              # Create new market
PUT    /api/markets/{id}         # Update market (full)
PATCH  /api/markets/{id}         # Update market (partial)
DELETE /api/markets/{id}         # Delete market

# Query parameters for filtering
GET /api/markets?status=active&limit=10&offset=0
```

### Response Format

```python
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

# ✅ GOOD: Consistent response structure
class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
    meta: Optional[dict] = None

class PaginationMeta(BaseModel):
    total: int
    page: int
    limit: int

# Success response
from fastapi.responses import JSONResponse

@app.get("/markets")
async def list_markets():
    markets = await fetch_markets()
    return ApiResponse(
        success=True,
        data=markets,
        meta=PaginationMeta(total=100, page=1, limit=10).model_dump()
    )

# Error response
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=ApiResponse(
            success=False,
            error=str(exc)
        ).model_dump()
    )
```

## File Organization

### Project Structure

```terminal
src/
├── api/                    # API routes/endpoints
│   ├── routes/            # Route handlers
│   ├── dependencies.py    # FastAPI dependencies
│   └── middleware.py      # Custom middleware
├── core/                  # Core application
│   ├── config.py         # Configuration
│   ├── database.py       # Database setup
│   └── security.py       # Auth/security
├── models/               # Database models
│   ├── user.py
│   └── market.py
├── schemas/              # Pydantic schemas
│   ├── user.py
│   └── market.py
├── services/             # Business logic
│   ├── market_service.py
│   └── user_service.py
├── utils/                # Utility functions
│   ├── helpers.py
│   └── validators.py
├── tests/                # Test files
│   ├── test_api.py
│   └── test_services.py
└── main.py              # Application entry point
```

## Comments & Documentation

### When to Comment

```python
# ✅ GOOD: Explain WHY, not WHAT
# Use exponential backoff to avoid overwhelming the API during outages
delay = min(1000 * (2 ** retry_count), 30000)

# Deliberately using mutation here for performance with large arrays
items.append(new_item)

# ❌ BAD: Stating the obvious
# Increment counter by 1
count += 1

# Set name to user's name
name = user.name
```

### Docstrings for Public APIs

```python
def search_markets(query: str, limit: int = 10) -> list[Market]:
    """
    Search markets using semantic similarity.

    Args:
        query: Natural language search query
        limit: Maximum number of results (default: 10)

    Returns:
        List of markets sorted by similarity score

    Raises:
        ValueError: If query is empty
        ConnectionError: If OpenAI API fails or Redis unavailable

    Example:
        >>> results = search_markets("election", 5)
        >>> print(results[0].name)
        'Trump vs Biden'
    """
    # Implementation
    pass
```

## Performance Best Practices

### List Comprehensions

```python
# ✅ GOOD: List comprehension (faster)
squared = [x**2 for x in range(100)]

# Filter with condition
active_markets = [m for m in markets if m.status == "active"]

# ❌ BAD: Manual loop when comprehension works
squared = []
for x in range(100):
    squared.append(x**2)
```

### Generator Expressions

```python
# ✅ GOOD: Generator for memory efficiency
total = sum(x**2 for x in range(1000000))

# Process large file
def process_large_file(filename: str):
    with open(filename) as f:
        for line in f:  # Generator, doesn't load all into memory
            yield process_line(line)

# ❌ BAD: Loading everything into memory
lines = open(filename).readlines()  # Loads entire file
```

### Dictionary Operations

```python
# ✅ GOOD: Dictionary comprehension
market_lookup = {m.id: m for m in markets}

# ✅ GOOD: get() with default
value = user_data.get("name", "Unknown")

# ❌ BAD: KeyError risk
value = user_data["name"]  # Raises KeyError if missing
```

### Database Queries (SQLAlchemy)

```python
from sqlalchemy import select

# ✅ GOOD: Select only needed columns
stmt = select(Market.id, Market.name, Market.status).limit(10)
results = await session.execute(stmt)

# ✅ GOOD: Use joins efficiently
stmt = (
    select(Market)
    .join(Market.categories)
    .options(joinedload(Market.categories))
    .limit(10)
)

# ❌ BAD: N+1 query problem
markets = await session.execute(select(Market))
for market in markets:
    categories = market.categories  # Triggers separate query each time
```

## Testing Standards

### Test Structure (AAA Pattern)

```python
import pytest

def test_calculates_similarity_correctly():
    # Arrange
    vector1 = [1.0, 0.0, 0.0]
    vector2 = [0.0, 1.0, 0.0]

    # Act
    similarity = calculate_cosine_similarity(vector1, vector2)

    # Assert
    assert similarity == 0.0


# ✅ GOOD: Parametrize for multiple cases
@pytest.mark.parametrize("vector1,vector2,expected", [
    ([1, 0, 0], [1, 0, 0], 1.0),
    ([1, 0, 0], [0, 1, 0], 0.0),
    ([1, 1, 0], [1, 1, 0], 1.0),
])
def test_similarity_calculations(vector1, vector2, expected):
    assert calculate_cosine_similarity(vector1, vector2) == expected
```

### Test Naming

```python
# ✅ GOOD: Descriptive test names
def test_returns_empty_list_when_no_markets_match_query():
    pass

def test_raises_error_when_openai_api_key_missing():
    pass

def test_falls_back_to_substring_search_when_redis_unavailable():
    pass

# ❌ BAD: Vague test names
def test_works():
    pass

def test_search():
    pass
```

### Fixtures and Mocking

```python
import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
async def mock_db():
    """Provide a mock database session"""
    db = AsyncMock()
    yield db
    await db.close()

@pytest.mark.asyncio
async def test_create_market(mock_db):
    # Arrange
    market_data = {"name": "Test Market", "status": "active"}

    # Act
    with patch("services.market_service.save_to_db") as mock_save:
        mock_save.return_value = market_data
        result = await create_market(market_data, mock_db)

    # Assert
    assert result["name"] == "Test Market"
    mock_save.assert_called_once()
```

## Code Smell Detection

### 1. Long Functions

```python
# ❌ BAD: Function > 50 lines
def process_market_data():
    # 100 lines of code
    pass

# ✅ GOOD: Split into smaller functions
def process_market_data():
    validated = validate_data()
    transformed = transform_data(validated)
    return save_data(transformed)
```

### 2. Deep Nesting

```python
# ❌ BAD: 5+ levels of nesting
if user:
    if user.is_admin:
        if market:
            if market.is_active:
                if has_permission:
                    # Do something
                    pass

# ✅ GOOD: Early returns (guard clauses)
if not user:
    return
if not user.is_admin:
    return
if not market:
    return
if not market.is_active:
    return
if not has_permission:
    return

# Do something
```

### 3. Magic Numbers

```python
# ❌ BAD: Unexplained numbers
if retry_count > 3:
    pass
await asyncio.sleep(0.5)

# ✅ GOOD: Named constants
MAX_RETRIES = 3
DEBOUNCE_DELAY_SECONDS = 0.5

if retry_count > MAX_RETRIES:
    pass
await asyncio.sleep(DEBOUNCE_DELAY_SECONDS)
```

## Python-Specific Best Practices

### Context Managers

```python
# ✅ GOOD: Use context managers for resources
with open("file.txt", "r") as f:
    content = f.read()

# Custom context manager
from contextlib import asynccontextmanager

@asynccontextmanager
async def database_transaction():
    transaction = await db.begin()
    try:
        yield transaction
        await transaction.commit()
    except Exception:
        await transaction.rollback()
        raise
```

### Pathlib for File Operations

```python
from pathlib import Path

# ✅ GOOD: Use pathlib
config_path = Path("config") / "settings.json"
if config_path.exists():
    content = config_path.read_text()

# ❌ BAD: String concatenation
import os
config_path = os.path.join("config", "settings.json")
```

### Enums for Constants

```python
from enum import Enum

# ✅ GOOD: Use Enum for related constants
class MarketStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    CLOSED = "closed"

# Usage with type safety
def get_active_markets(status: MarketStatus = MarketStatus.ACTIVE):
    pass

# ❌ BAD: String constants
ACTIVE = "active"
RESOLVED = "resolved"
CLOSED = "closed"
```

**Remember**: Code quality is not negotiable. Clear, maintainable, Pythonic code enables rapid development and confident refactoring.
