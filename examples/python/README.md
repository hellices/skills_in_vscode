# Python Example Project

This is an example Python project demonstrating GitHub Copilot custom instructions and Anthropic skills integration.

## Project Structure

```
python-example/
├── .github/
│   └── copilot/
│       └── python-instructions.md   # Custom instructions
├── .vscode/
│   ├── settings.json               # VS Code configuration
│   └── skills.json                 # Anthropic skills
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── models/
│       ├── __init__.py
│       └── user.py
├── tests/
│   ├── __init__.py
│   └── test_user_service.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure VS Code

The `.vscode/settings.json` is pre-configured with:
- Python interpreter settings
- Linting and formatting tools
- Anthropic API configuration

### 3. Set Up API Key (for Anthropic Skills)

```bash
# Add to your environment
export ANTHROPIC_API_KEY="your-api-key-here"

# Or create .env file
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

## Using Custom Instructions

Custom instructions are automatically applied when you use GitHub Copilot in this project.

**Try this:**

1. Create a new Python file
2. Start typing a function
3. Notice Copilot suggestions follow PEP 8 and project conventions

## Using Anthropic Skills

### Code Review

1. Select code in a Python file
2. Open Command Palette (Ctrl+Shift+P)
3. Type "Anthropic: Run Skill"
4. Select "Python Code Reviewer"

### Test Generation

1. Open `src/services/user_service.py`
2. Select the `UserService` class
3. Run skill: "Python Test Generator"
4. Tests will be generated in `tests/`

### Documentation

1. Select a function
2. Run skill: "Python Documentation Generator"
3. Google-style docstring will be added

## Example Code

### User Model (`src/models/user.py`)

```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class User:
    """User model representing a system user.
    
    Attributes:
        id: Unique user identifier
        email: User's email address
        name: User's full name
        created_at: Timestamp of user creation
    """
    id: int
    email: str
    name: str
    created_at: datetime
    
    def __post_init__(self):
        """Validate user data after initialization."""
        if not self.email:
            raise ValueError("Email is required")
        if "@" not in self.email:
            raise ValueError("Invalid email format")
```

### User Service (`src/services/user_service.py`)

```python
from typing import Optional, List
from ..models.user import User


class UserService:
    """Service for managing user operations.
    
    This service handles user-related business logic including
    creation, retrieval, and validation.
    """
    
    def __init__(self):
        self._users: List[User] = []
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID.
        
        Args:
            user_id: The unique identifier of the user
            
        Returns:
            User object if found, None otherwise
            
        Example:
            >>> service = UserService()
            >>> user = service.get_user_by_id(1)
        """
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def create_user(self, email: str, name: str) -> User:
        """Create a new user.
        
        Args:
            email: User's email address
            name: User's full name
            
        Returns:
            Newly created User object
            
        Raises:
            ValueError: If email or name is invalid
        """
        from datetime import datetime
        
        user_id = len(self._users) + 1
        user = User(
            id=user_id,
            email=email,
            name=name,
            created_at=datetime.now()
        )
        self._users.append(user)
        return user
```

### Tests (`tests/test_user_service.py`)

```python
import pytest
from datetime import datetime
from src.models.user import User
from src.services.user_service import UserService


class TestUserService:
    """Test suite for UserService."""
    
    @pytest.fixture
    def service(self):
        """Create a UserService instance for testing."""
        return UserService()
    
    def test_create_user_success(self, service):
        """Test successful user creation."""
        user = service.create_user("test@example.com", "Test User")
        
        assert user.id == 1
        assert user.email == "test@example.com"
        assert user.name == "Test User"
        assert isinstance(user.created_at, datetime)
    
    def test_get_user_by_id_found(self, service):
        """Test retrieving an existing user by ID."""
        created_user = service.create_user("test@example.com", "Test User")
        
        found_user = service.get_user_by_id(created_user.id)
        
        assert found_user is not None
        assert found_user.id == created_user.id
        assert found_user.email == created_user.email
    
    def test_get_user_by_id_not_found(self, service):
        """Test retrieving a non-existent user by ID."""
        user = service.get_user_by_id(999)
        
        assert user is None
    
    def test_create_user_invalid_email(self):
        """Test user creation with invalid email."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User(id=1, email="invalid", name="Test", created_at=datetime.now())
```

## Available Skills

### 1. Python Code Reviewer
- Checks PEP 8 compliance
- Validates type hints
- Reviews error handling
- Suggests improvements

### 2. Python Test Generator
- Creates pytest tests
- Follows naming conventions
- Uses fixtures
- Covers edge cases

### 3. Python Documentation Generator
- Generates Google-style docstrings
- Includes examples
- Documents parameters and returns
- Adds type information

### 4. Python Refactorer
- Suggests code improvements
- Identifies performance issues
- Recommends design patterns
- Reduces complexity

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_user_service.py::TestUserService::test_create_user_success
```

## Linting and Formatting

```bash
# Format code with black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Lint with ruff
ruff check src/ tests/

# Type check with mypy
mypy src/
```

## Tips

1. **Let Copilot help**: Start typing and let it suggest based on instructions
2. **Use skills for complex tasks**: Test generation, refactoring, documentation
3. **Keep instructions updated**: Modify `.github/copilot/python-instructions.md` as needed
4. **Share with team**: Commit instruction and skill files to Git

## Next Steps

1. Explore the custom instructions in `.github/copilot/python-instructions.md`
2. Try generating tests with Anthropic skills
3. Create your own custom skills in `.vscode/skills.json`
4. Read the [Python Custom Instructions Guide](../../docs/custom-instructions/python.md)

## Resources

- [Python Custom Instructions](../../docs/custom-instructions/python.md)
- [Anthropic Skills Configuration](../../docs/anthropic-skills/configuration.md)
- [Creating Custom Skills](../../docs/anthropic-skills/creating-skills.md)
