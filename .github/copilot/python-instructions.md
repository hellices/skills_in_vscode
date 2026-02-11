# Python Instructions

## Code Style
- Follow PEP 8 style guide
- Use type hints for function signatures
- Maximum line length: 88 characters
- Use f-strings for string formatting

## Naming Conventions
- Classes: PascalCase (UserService, DataProcessor)
- Functions/Methods: snake_case (get_user, process_data)
- Constants: UPPER_SNAKE_CASE (MAX_RETRIES, API_URL)
- Private members: _leading_underscore

## Imports
- Standard library first
- Third-party packages second
- Local imports last
- Use absolute imports from project root

## Docstrings
Use Google-style docstrings:

```python
def calculate_total(items: list[float], tax_rate: float) -> float:
    """Calculate total price including tax.
    
    Args:
        items: List of item prices
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
        
    Returns:
        Total price with tax applied
        
    Raises:
        ValueError: If tax_rate is negative
    """
    pass
```

## Error Handling
- Use specific exception types
- Provide meaningful error messages
- Use context managers for resources
- Don't use bare except clauses

## Testing
- Use pytest for testing
- Name tests: test_{function}_{scenario}_{expected}
- Use fixtures for test data
- Mock external dependencies

## Common Patterns
- Use list comprehensions over loops when readable
- Use generators for large datasets
- Prefer async/await for I/O operations
- Use dataclasses or Pydantic for data models
