# Python Custom Instructions

This guide provides Python-specific custom instructions for GitHub Copilot, focusing on modern Python best practices and common patterns.

## Quick Start

Create `.github/copilot/python-instructions.md` in your repository:

```markdown
# Python Project Instructions

## Code Style
- Follow PEP 8 naming conventions
- Use type hints for function signatures
- Maximum line length: 88 characters (Black formatter)
- Use f-strings for string formatting

## Project Setup
- Python version: 3.11+
- Package manager: Poetry
- Testing: pytest with pytest-cov
- Linting: ruff
- Formatting: black + isort

## Imports
- Standard library imports first
- Third-party imports second
- Local imports last
- Use absolute imports from project root
```

## Complete Example

Here's a comprehensive Python custom instructions file:

```markdown
# Python Development Guidelines

## Code Style & Conventions

### Naming
- Classes: PascalCase (UserService, DatabaseConnection)
- Functions/Methods: snake_case (get_user, process_data)
- Constants: UPPER_SNAKE_CASE (MAX_RETRIES, API_KEY)
- Private members: _leading_underscore (_internal_method)
- Module names: lowercase with underscores (user_service.py)

### Type Hints
Always use type hints for function signatures:

```python
from typing import Optional, List, Dict

def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Fetch user by ID."""
    pass

def process_items(items: List[str], max_count: int = 10) -> List[str]:
    """Process a list of items."""
    pass
```

### Docstrings
Use Google-style docstrings for all public functions and classes:

```python
def calculate_total(items: List[float], tax_rate: float) -> float:
    """Calculate total price including tax.
    
    Args:
        items: List of item prices
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
        
    Returns:
        Total price with tax applied
        
    Raises:
        ValueError: If tax_rate is negative
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return sum(items) * (1 + tax_rate)
```

## Project Structure

### Application Layout
```
src/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration management
│   ├── models/              # Data models
│   ├── services/            # Business logic
│   ├── repositories/        # Data access layer
│   └── utils/               # Utility functions
tests/
├── unit/
├── integration/
└── conftest.py              # Pytest fixtures
```

### Import Organization
```python
# Standard library
import os
import sys
from datetime import datetime
from pathlib import Path

# Third-party
import pandas as pd
import requests
from pydantic import BaseModel

# Local
from app.config import settings
from app.models import User
from app.services import UserService
```

## Error Handling

### Use Specific Exceptions
```python
# Good
def get_user(user_id: int) -> User:
    if user_id <= 0:
        raise ValueError(f"Invalid user ID: {user_id}")
    
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise UserNotFoundError(f"User {user_id} not found")
    
    return user

# Bad
def get_user(user_id: int) -> User:
    try:
        return db.query(User).filter_by(id=user_id).first()
    except:
        return None
```

### Context Managers for Resources
```python
# Always use context managers for files, connections
with open('data.json', 'r') as f:
    data = json.load(f)

with DatabaseConnection() as db:
    db.execute(query)
```

## Testing Guidelines

### Test Structure
```python
import pytest
from app.services import UserService

class TestUserService:
    """Test suite for UserService."""
    
    @pytest.fixture
    def user_service(self):
        """Create UserService instance for testing."""
        return UserService()
    
    def test_create_user_success(self, user_service):
        """Test successful user creation."""
        user = user_service.create_user("test@example.com")
        assert user.email == "test@example.com"
        assert user.id is not None
    
    def test_create_user_invalid_email(self, user_service):
        """Test user creation with invalid email."""
        with pytest.raises(ValueError):
            user_service.create_user("invalid-email")
```

### Use Fixtures for Test Data
```python
@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return User(
        id=1,
        email="test@example.com",
        name="Test User"
    )

@pytest.fixture
def mock_database(mocker):
    """Mock database connection."""
    return mocker.patch('app.database.get_connection')
```

## Data Validation

### Use Pydantic for Models
```python
from pydantic import BaseModel, EmailStr, Field, validator

class UserCreate(BaseModel):
    """User creation schema."""
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        """Validate name is not just whitespace."""
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
```

## Async Patterns

### Use asyncio for I/O Operations
```python
import asyncio
import aiohttp
from typing import List

async def fetch_user(session: aiohttp.ClientSession, user_id: int) -> dict:
    """Fetch single user asynchronously."""
    async with session.get(f"{API_URL}/users/{user_id}") as response:
        return await response.json()

async def fetch_multiple_users(user_ids: List[int]) -> List[dict]:
    """Fetch multiple users concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, uid) for uid in user_ids]
        return await asyncio.gather(*tasks)
```

## Database Patterns

### Use SQLAlchemy ORM
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
```

### Repository Pattern
```python
from typing import Optional, List
from sqlalchemy.orm import Session

class UserRepository:
    """Repository for User operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        """Find user by ID."""
        return self.db.query(User).filter_by(id=user_id).first()
    
    def find_all(self, limit: int = 100) -> List[User]:
        """Get all users with optional limit."""
        return self.db.query(User).limit(limit).all()
    
    def create(self, user_data: UserCreate) -> User:
        """Create new user."""
        user = User(**user_data.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
```

## Logging

### Use Structured Logging
```python
import logging
import structlog

# Configure structured logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()

# Usage
logger.info("user_created", user_id=user.id, email=user.email)
logger.error("database_error", error=str(e), query=query)
```

## Configuration Management

### Use Environment Variables with Pydantic Settings
```python
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """Application settings."""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = Field(..., env="DATABASE_URL")
    api_key: str = Field(..., env="API_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

## Security Best Practices

### Never Hardcode Secrets
```python
# Good - Use environment variables
import os
API_KEY = os.getenv("API_KEY")

# Bad - Hardcoded
API_KEY = "sk_live_abc123..."  # NEVER DO THIS
```

### Validate User Input
```python
from pydantic import BaseModel, validator

class SearchQuery(BaseModel):
    """Search query validation."""
    query: str
    limit: int = 10
    
    @validator('query')
    def sanitize_query(cls, v):
        """Remove potentially harmful characters."""
        # Remove SQL injection attempts
        dangerous_chars = [';', '--', '/*', '*/']
        for char in dangerous_chars:
            if char in v:
                raise ValueError("Invalid characters in query")
        return v.strip()
```

### Use Parameterized Queries
```python
# Good - Parameterized
user = db.execute(
    "SELECT * FROM users WHERE email = :email",
    {"email": user_email}
).first()

# Bad - String interpolation
user = db.execute(
    f"SELECT * FROM users WHERE email = '{user_email}'"
).first()  # SQL injection risk!
```

## Performance Optimization

### Use List Comprehensions
```python
# Good - List comprehension
squares = [x**2 for x in range(100)]

# Less efficient - Loop with append
squares = []
for x in range(100):
    squares.append(x**2)
```

### Use Generators for Large Datasets
```python
def read_large_file(file_path: str):
    """Read large file line by line."""
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Process without loading entire file into memory
for line in read_large_file('huge_file.txt'):
    process(line)
```

## Common Anti-Patterns to Avoid

### ❌ Mutable Default Arguments
```python
# Bad
def add_item(item, items=[]):
    items.append(item)
    return items

# Good
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### ❌ Bare Except Clauses
```python
# Bad
try:
    risky_operation()
except:
    pass

# Good
try:
    risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

## Tools Integration

### Required Development Tools
- **Black**: Code formatting (line length 88)
- **isort**: Import sorting
- **ruff**: Fast linting (replaces flake8, pylint)
- **mypy**: Static type checking
- **pytest**: Testing framework
- **coverage**: Code coverage reporting

### Pre-commit Configuration
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.270
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
```

## Additional Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [pytest Documentation](https://docs.pytest.org/)
