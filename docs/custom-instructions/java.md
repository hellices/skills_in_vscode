# Java Custom Instructions

This guide provides Java-specific custom instructions for GitHub Copilot, focusing on modern Java practices and enterprise patterns.

## Quick Start

Create `.github/copilot/java-instructions.md` in your repository:

```markdown
# Java Project Instructions

## Code Style
- Follow Google Java Style Guide
- Use Java 17+ features
- Prefer records for DTOs
- Use Stream API for collections

## Project Setup
- Java version: 17 LTS or 21 LTS
- Build tool: Maven or Gradle
- Testing: JUnit 5 + Mockito
- Framework: Spring Boot 3.x

## Naming Conventions
- Classes: PascalCase (UserService, OrderRepository)
- Methods: camelCase (getUserById, processOrder)
- Constants: UPPER_SNAKE_CASE (MAX_RETRIES, API_URL)
- Packages: lowercase (com.company.service)
```

## Complete Example

Here's a comprehensive Java custom instructions file:

```markdown
# Java Development Guidelines

## Code Style & Conventions

### Class Structure
```java
/**
 * Service for managing user operations.
 * 
 * @author Your Team
 * @since 1.0
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class UserService {
    
    // Constants first
    private static final int MAX_RETRIES = 3;
    
    // Dependencies (injected)
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    // Public methods
    public User getUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    // Private methods
    private void validateUser(User user) {
        // validation logic
    }
}
```

### Naming Conventions
```java
// Classes and Interfaces: PascalCase
public class UserService {}
public interface PaymentProcessor {}

// Methods and Variables: camelCase
public User getUserById(Long userId) {}
private String firstName;

// Constants: UPPER_SNAKE_CASE
public static final String API_BASE_URL = "https://api.example.com";
private static final int MAX_RETRY_ATTEMPTS = 3;

// Packages: lowercase with dots
package com.company.service;
package com.company.repository;

// Enums: PascalCase for type, UPPER_SNAKE_CASE for values
public enum OrderStatus {
    PENDING,
    PROCESSING,
    COMPLETED,
    CANCELLED
}
```

## Project Structure

### Spring Boot Application Layout
```
src/
├── main/
│   ├── java/
│   │   └── com/company/app/
│   │       ├── Application.java              # Main entry point
│   │       ├── config/                       # Configuration classes
│   │       │   ├── DatabaseConfig.java
│   │       │   └── SecurityConfig.java
│   │       ├── controller/                   # REST controllers
│   │       │   └── UserController.java
│   │       ├── service/                      # Business logic
│   │       │   ├── UserService.java
│   │       │   └── impl/
│   │       │       └── UserServiceImpl.java
│   │       ├── repository/                   # Data access
│   │       │   └── UserRepository.java
│   │       ├── model/                        # Domain entities
│   │       │   └── User.java
│   │       ├── dto/                          # Data transfer objects
│   │       │   ├── UserRequest.java
│   │       │   └── UserResponse.java
│   │       ├── exception/                    # Custom exceptions
│   │       │   └── UserNotFoundException.java
│   │       └── util/                         # Utility classes
│   │           └── ValidationUtil.java
│   └── resources/
│       ├── application.yml
│       ├── application-dev.yml
│       └── application-prod.yml
└── test/
    └── java/
        └── com/company/app/
            ├── service/
            │   └── UserServiceTest.java
            └── controller/
                └── UserControllerTest.java
```

## Modern Java Features

### Records for DTOs (Java 16+)
```java
// Instead of boilerplate POJO
public record UserRequest(
    @NotBlank String email,
    @NotBlank String name,
    @Min(18) Integer age
) {
    // Compact constructor for validation
    public UserRequest {
        email = email.trim().toLowerCase();
    }
}

public record UserResponse(
    Long id,
    String email,
    String name,
    LocalDateTime createdAt
) {}
```

### Pattern Matching (Java 17+)
```java
// Switch expressions with pattern matching
public String getStatusMessage(Order order) {
    return switch (order.status()) {
        case PENDING -> "Order is being processed";
        case PROCESSING -> "Order is on the way";
        case COMPLETED -> "Order delivered";
        case CANCELLED -> "Order was cancelled";
    };
}

// Pattern matching with instanceof
public double calculateArea(Shape shape) {
    if (shape instanceof Circle c) {
        return Math.PI * c.radius() * c.radius();
    } else if (shape instanceof Rectangle r) {
        return r.width() * r.height();
    }
    throw new IllegalArgumentException("Unknown shape");
}
```

### Sealed Classes (Java 17+)
```java
public sealed interface Shape
    permits Circle, Rectangle, Triangle {
}

public final record Circle(double radius) implements Shape {}
public final record Rectangle(double width, double height) implements Shape {}
public final record Triangle(double base, double height) implements Shape {}
```

## Spring Boot Patterns

### REST Controller
```java
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
@Validated
@Tag(name = "User", description = "User management APIs")
public class UserController {
    
    private final UserService userService;
    
    @GetMapping("/{id}")
    @Operation(summary = "Get user by ID")
    public ResponseEntity<ApiResponse<UserResponse>> getUser(
            @PathVariable @Positive Long id) {
        
        UserResponse user = userService.getUserById(id);
        return ResponseEntity.ok(
            ApiResponse.success(user)
        );
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Create new user")
    public ApiResponse<UserResponse> createUser(
            @RequestBody @Valid UserRequest request) {
        
        UserResponse user = userService.createUser(request);
        return ApiResponse.success(user);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<UserResponse>> updateUser(
            @PathVariable @Positive Long id,
            @RequestBody @Valid UserRequest request) {
        
        UserResponse user = userService.updateUser(id, request);
        return ResponseEntity.ok(
            ApiResponse.success(user)
        );
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable @Positive Long id) {
        userService.deleteUser(id);
    }
}
```

### Service Layer
```java
@Service
@RequiredArgsConstructor
@Slf4j
@Transactional(readOnly = true)
public class UserService {
    
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    
    public UserResponse getUserById(Long id) {
        log.debug("Fetching user with id: {}", id);
        
        return userRepository.findById(id)
            .map(userMapper::toResponse)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    @Transactional
    public UserResponse createUser(UserRequest request) {
        log.info("Creating new user: {}", request.email());
        
        if (userRepository.existsByEmail(request.email())) {
            throw new DuplicateEmailException(request.email());
        }
        
        User user = userMapper.toEntity(request);
        User savedUser = userRepository.save(user);
        
        log.info("User created with id: {}", savedUser.getId());
        return userMapper.toResponse(savedUser);
    }
    
    @Transactional
    public UserResponse updateUser(Long id, UserRequest request) {
        User user = userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
        
        userMapper.updateEntity(user, request);
        User updatedUser = userRepository.save(user);
        
        return userMapper.toResponse(updatedUser);
    }
    
    @Transactional
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new UserNotFoundException(id);
        }
        userRepository.deleteById(id);
        log.info("User deleted: {}", id);
    }
}
```

### Repository Layer
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    Optional<User> findByEmail(String email);
    
    boolean existsByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.createdAt >= :date")
    List<User> findRecentUsers(@Param("date") LocalDateTime date);
    
    @Query("""
        SELECT u FROM User u 
        WHERE u.active = true 
        AND u.email LIKE %:search%
        ORDER BY u.createdAt DESC
    """)
    Page<User> searchActiveUsers(
        @Param("search") String search,
        Pageable pageable
    );
}
```

## Exception Handling

### Custom Exceptions
```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(Long id) {
        super("User not found with id: " + id);
    }
}

public class DuplicateEmailException extends RuntimeException {
    public DuplicateEmailException(String email) {
        super("Email already exists: " + email);
    }
}
```

### Global Exception Handler
```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ApiResponse<Void> handleUserNotFound(UserNotFoundException ex) {
        log.warn("User not found: {}", ex.getMessage());
        return ApiResponse.error(ex.getMessage());
    }
    
    @ExceptionHandler(DuplicateEmailException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public ApiResponse<Void> handleDuplicateEmail(DuplicateEmailException ex) {
        log.warn("Duplicate email: {}", ex.getMessage());
        return ApiResponse.error(ex.getMessage());
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Map<String, String>> handleValidationErrors(
            MethodArgumentNotValidException ex) {
        
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(
                FieldError::getField,
                error -> Objects.requireNonNullElse(
                    error.getDefaultMessage(), "Invalid value"
                )
            ));
        
        return ApiResponse.error("Validation failed", errors);
    }
    
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ApiResponse<Void> handleGenericException(Exception ex) {
        log.error("Unexpected error", ex);
        return ApiResponse.error("An unexpected error occurred");
    }
}
```

## Validation

### Bean Validation (Jakarta)
```java
public record CreateOrderRequest(
    @NotNull(message = "User ID is required")
    Long userId,
    
    @NotEmpty(message = "Items cannot be empty")
    @Size(min = 1, max = 100, message = "Order must have 1-100 items")
    List<@Valid OrderItemRequest> items,
    
    @NotNull
    @DecimalMin(value = "0.01", message = "Total must be positive")
    BigDecimal total,
    
    @Email(message = "Invalid email format")
    String contactEmail
) {}

// Custom validator
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = PhoneNumberValidator.class)
public @interface ValidPhoneNumber {
    String message() default "Invalid phone number";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class PhoneNumberValidator 
        implements ConstraintValidator<ValidPhoneNumber, String> {
    
    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        if (value == null) return true;
        return value.matches("^\\+?[1-9]\\d{1,14}$");
    }
}
```

## Testing

### JUnit 5 Unit Tests
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private UserMapper userMapper;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    @DisplayName("Should return user when found")
    void getUserById_WhenUserExists_ReturnsUser() {
        // Given
        Long userId = 1L;
        User user = new User(userId, "test@example.com", "Test User");
        UserResponse expected = new UserResponse(
            userId, "test@example.com", "Test User", LocalDateTime.now()
        );
        
        when(userRepository.findById(userId))
            .thenReturn(Optional.of(user));
        when(userMapper.toResponse(user))
            .thenReturn(expected);
        
        // When
        UserResponse actual = userService.getUserById(userId);
        
        // Then
        assertThat(actual).isEqualTo(expected);
        verify(userRepository).findById(userId);
        verify(userMapper).toResponse(user);
    }
    
    @Test
    @DisplayName("Should throw exception when user not found")
    void getUserById_WhenUserNotFound_ThrowsException() {
        // Given
        Long userId = 1L;
        when(userRepository.findById(userId))
            .thenReturn(Optional.empty());
        
        // When & Then
        assertThatThrownBy(() -> userService.getUserById(userId))
            .isInstanceOf(UserNotFoundException.class)
            .hasMessageContaining("User not found with id: 1");
    }
}
```

### Integration Tests
```java
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
@Sql(scripts = "/test-data.sql", executionPhase = BEFORE_TEST_METHOD)
@Sql(scripts = "/cleanup.sql", executionPhase = AFTER_TEST_METHOD)
class UserControllerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private ObjectMapper objectMapper;
    
    @Test
    void createUser_WithValidData_ReturnsCreated() throws Exception {
        // Given
        UserRequest request = new UserRequest(
            "newuser@example.com",
            "New User",
            25
        );
        
        // When & Then
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.success").value(true))
            .andExpect(jsonPath("$.data.email").value("newuser@example.com"))
            .andExpect(jsonPath("$.data.id").exists());
    }
    
    @Test
    void getUser_WhenNotFound_Returns404() throws Exception {
        mockMvc.perform(get("/api/users/999"))
            .andExpect(status().isNotFound())
            .andExpect(jsonPath("$.success").value(false))
            .andExpect(jsonPath("$.error").exists());
    }
}
```

## MapStruct for Object Mapping

```java
@Mapper(componentModel = "spring")
public interface UserMapper {
    
    UserResponse toResponse(User user);
    
    User toEntity(UserRequest request);
    
    @Mapping(target = "id", ignore = true)
    @Mapping(target = "createdAt", ignore = true)
    void updateEntity(@MappingTarget User user, UserRequest request);
    
    List<UserResponse> toResponseList(List<User> users);
}
```

## Configuration

### Application Properties (YAML)
```yaml
# application.yml
spring:
  application:
    name: user-service
  
  datasource:
    url: ${DATABASE_URL:jdbc:postgresql://localhost:5432/userdb}
    username: ${DATABASE_USER:postgres}
    password: ${DATABASE_PASSWORD:postgres}
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
      connection-timeout: 30000
  
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        format_sql: true
        dialect: org.hibernate.dialect.PostgreSQLDialect
  
  flyway:
    enabled: true
    locations: classpath:db/migration

logging:
  level:
    root: INFO
    com.company.app: DEBUG
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
```

### Type-Safe Configuration
```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
public record AppConfig(
    @NotBlank String name,
    @NotBlank String version,
    @Valid ApiConfig api,
    @Valid SecurityConfig security
) {
    public record ApiConfig(
        @Min(1) int maxRequestsPerMinute,
        @NotBlank String baseUrl
    ) {}
    
    public record SecurityConfig(
        @NotBlank String jwtSecret,
        @Min(60) long jwtExpirationSeconds
    ) {}
}
```

## Logging

### SLF4J with Lombok
```java
@Service
@Slf4j
public class OrderService {
    
    public Order processOrder(OrderRequest request) {
        log.info("Processing order for user: {}", request.userId());
        
        try {
            Order order = createOrder(request);
            log.debug("Order created: {}", order.getId());
            return order;
        } catch (Exception e) {
            log.error("Failed to process order", e);
            throw new OrderProcessingException("Order processing failed", e);
        }
    }
}
```

## Performance Optimization

### Caching with Spring
```java
@Configuration
@EnableCaching
public class CacheConfig {
    
    @Bean
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager("users", "orders");
    }
}

@Service
public class UserService {
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
    
    @CachePut(value = "users", key = "#result.id")
    public User updateUser(Long id, UserRequest request) {
        // update logic
    }
}
```

## Security

### JWT Authentication
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .addFilterBefore(jwtAuthFilter, 
                UsernamePasswordAuthenticationFilter.class)
            .build();
    }
}
```

## Tools Integration

### Maven Configuration
```xml
<properties>
    <java.version>17</java.version>
    <spring-boot.version>3.2.0</spring-boot.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
</dependencies>
```

## Additional Resources

- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Java Language Guide](https://docs.oracle.com/en/java/javase/17/)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
