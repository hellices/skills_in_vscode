---
name: Generate Tests
description: Generate comprehensive test suites for code
---

# Test Generation Skill

This skill helps generate comprehensive tests following project conventions.

## When to Use

Use this skill when:
- Creating tests for new code
- Adding missing test coverage
- Refactoring existing tests
- Learning testing patterns

## Process

### 1. Analyze Code
- Identify the code to test
- Understand inputs and outputs
- Note edge cases and error conditions
- Check existing test patterns

### 2. Determine Test Framework

**Python**: pytest, unittest
**JavaScript/TypeScript**: Jest, Vitest, Mocha
**Java**: JUnit 5, TestNG
**Go**: testing package

### 3. Generate Test Structure

```python
# Python example
import pytest
from module import function

class TestFunction:
    """Test suite for function."""
    
    @pytest.fixture
    def setup_data(self):
        """Create test data."""
        return {"key": "value"}
    
    def test_happy_path(self, setup_data):
        """Test normal operation."""
        result = function(setup_data)
        assert result == expected
    
    def test_edge_case(self):
        """Test edge case."""
        result = function(edge_input)
        assert result == edge_expected
    
    def test_error_condition(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            function(invalid_input)
```

### 4. Include Test Types

**Unit Tests**: Test individual functions/methods in isolation

**Integration Tests**: Test component interactions

**Edge Cases**: 
- Empty inputs
- Null/undefined values
- Maximum/minimum values
- Invalid types

**Error Conditions**:
- Expected exceptions
- Error messages
- Graceful degradation

### 5. Best Practices

- **One concept per test**: Each test should verify one thing
- **AAA Pattern**: Arrange, Act, Assert
- **Descriptive names**: `test_method_scenario_expected`
- **Mock dependencies**: Use mocks for external services
- **Clean up**: Proper teardown and resource cleanup

## Examples

### Testing a User Service

```typescript
// TypeScript with Jest
describe('UserService', () => {
  let service: UserService;
  let mockRepository: jest.Mocked<UserRepository>;

  beforeEach(() => {
    mockRepository = {
      findById: jest.fn(),
      save: jest.fn()
    } as any;
    service = new UserService(mockRepository);
  });

  describe('getUserById', () => {
    it('should return user when found', async () => {
      const mockUser = { id: '1', name: 'Test' };
      mockRepository.findById.mockResolvedValue(mockUser);

      const result = await service.getUserById('1');

      expect(result).toEqual(mockUser);
      expect(mockRepository.findById).toHaveBeenCalledWith('1');
    });

    it('should throw error when not found', async () => {
      mockRepository.findById.mockResolvedValue(null);

      await expect(service.getUserById('999'))
        .rejects
        .toThrow('User not found');
    });
  });
});
```

### Testing API Endpoints

```python
# Python with pytest
def test_get_user_endpoint(client, test_db):
    """Test GET /users/:id endpoint."""
    # Arrange
    user = create_test_user(test_db)
    
    # Act
    response = client.get(f'/users/{user.id}')
    
    # Assert
    assert response.status_code == 200
    assert response.json()['id'] == user.id
    assert response.json()['email'] == user.email

def test_get_user_not_found(client):
    """Test GET /users/:id with invalid ID."""
    response = client.get('/users/999')
    
    assert response.status_code == 404
    assert 'error' in response.json()
```

## Common Patterns

### Fixtures and Test Data

```python
@pytest.fixture
def sample_user():
    """Create sample user for testing."""
    return User(
        id=1,
        email="test@example.com",
        name="Test User"
    )

@pytest.fixture
def user_factory():
    """Factory for creating test users."""
    def _create(email=None, name=None):
        return User(
            email=email or f"test{uuid.uuid4()}@example.com",
            name=name or "Test User"
        )
    return _create
```

### Parameterized Tests

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("", ""),
])
def test_uppercase(input, expected):
    """Test uppercase function with various inputs."""
    assert uppercase(input) == expected
```

## Integration with Project

Always check and follow:
- Project testing conventions: #file:.github/copilot-instructions.md
- Existing test patterns: #file:tests/
- Test configuration: #file:pytest.ini or #file:jest.config.js

## Tips

1. **Start simple**: Write basic happy path test first
2. **Add edge cases**: Then cover boundary conditions
3. **Test errors**: Verify error handling
4. **Refactor**: Clean up tests after they pass
5. **Run tests**: Ensure they pass before committing
