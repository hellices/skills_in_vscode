# Java Instructions

## Code Style
- Follow Google Java Style Guide
- Use Java 17+ features
- Maximum line length: 100 characters
- Use meaningful variable names

## Naming Conventions
- Classes/Interfaces: PascalCase (UserService, PaymentProcessor)
- Methods/Variables: camelCase (getUserById, firstName)
- Constants: UPPER_SNAKE_CASE (MAX_RETRIES, API_URL)
- Packages: lowercase (com.company.service)

## Modern Java Features
- Use records for DTOs (Java 16+)
- Use pattern matching (Java 17+)
- Use var for local variables when type is obvious
- Use Stream API for collections

## Spring Boot Patterns
- Use constructor injection (not field injection)
- Use @RequiredArgsConstructor from Lombok
- Service methods should be transactional when needed
- Use repository pattern for data access

## Error Handling
- Create custom exception classes
- Use @ControllerAdvice for global error handling
- Provide meaningful error messages
- Log exceptions appropriately

## Testing
- Use JUnit 5
- Use Mockito for mocking
- Name tests: methodName_scenario_expectedResult
- Use @DisplayName for readable test names

## Documentation
- Use Javadoc for public methods
- Include @param, @return, @throws tags
- Add class-level documentation
- Document complex algorithms

## Example Patterns
```java
@Service
@RequiredArgsConstructor
@Slf4j
public class UserService {
    private final UserRepository repository;
    
    public User getUserById(Long id) {
        return repository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
}
```
