# Agent-Based Custom Instructions

This guide explores advanced usage of GitHub Copilot with agent-based configurations, allowing you to create specialized AI assistants for different aspects of your development workflow.

## What are Agent-Based Instructions?

Agent-based instructions allow you to configure multiple specialized "agents" within your project, each with specific knowledge domains, responsibilities, and behaviors. This is more advanced than simple custom instructions and enables:

- **Role-specific guidance**: Different instructions for frontend, backend, testing, etc.
- **Context-aware assistance**: Instructions that adapt based on the current file or task
- **Workflow automation**: Agents that guide through complex multi-step processes
- **Team collaboration**: Shared agent configurations across your team

## Creating Agent Configurations

### Directory Structure

```
.github/
└── copilot/
    ├── instructions.md              # Global instructions
    ├── agents/
    │   ├── frontend.md              # Frontend agent
    │   ├── backend.md               # Backend agent
    │   ├── testing.md               # Testing agent
    │   ├── security.md              # Security review agent
    │   └── documentation.md         # Documentation agent
    └── workflows/
        ├── new-feature.md           # Feature development workflow
        └── bug-fix.md               # Bug fixing workflow
```

## Example Agents

### 1. Frontend Development Agent

**File**: `.github/copilot/agents/frontend.md`

```markdown
# Frontend Development Agent

## Role
You are a frontend specialist focusing on React, TypeScript, and modern UI development.

## Responsibilities
- Component design and implementation
- State management
- UI/UX best practices
- Accessibility (WCAG compliance)
- Performance optimization

## Technology Stack
- React 18 with TypeScript
- Zustand for state management
- Tailwind CSS for styling
- React Query for data fetching
- Vitest + React Testing Library

## Component Guidelines

### Component Structure
```typescript
import { FC } from 'react';

interface UserProfileProps {
  userId: string;
  onUpdate?: (user: User) => void;
}

/**
 * Displays and manages user profile information.
 * @component
 */
export const UserProfile: FC<UserProfileProps> = ({ userId, onUpdate }) => {
  // Hooks first
  const { data: user, isLoading } = useUser(userId);
  const [isEditing, setIsEditing] = useState(false);
  
  // Event handlers
  const handleSave = () => {
    // implementation
  };
  
  // Render logic
  if (isLoading) return <LoadingSkeleton />;
  if (!user) return <NotFound />;
  
  return (
    <div className="user-profile">
      {/* JSX */}
    </div>
  );
};
```

### State Management Patterns
```typescript
// Zustand store
interface UserStore {
  currentUser: User | null;
  setUser: (user: User) => void;
  logout: () => void;
}

export const useUserStore = create<UserStore>((set) => ({
  currentUser: null,
  setUser: (user) => set({ currentUser: user }),
  logout: () => set({ currentUser: null })
}));
```

### Testing Requirements
- Unit tests for all components
- Integration tests for user flows
- Accessibility tests with jest-axe
- Visual regression tests for critical components

### Accessibility Checklist
- [ ] Semantic HTML elements
- [ ] ARIA labels where needed
- [ ] Keyboard navigation support
- [ ] Focus management
- [ ] Screen reader testing
- [ ] Color contrast ratios (WCAG AA)

## Code Review Focus
- Component reusability
- Props validation
- Error boundaries
- Loading states
- Performance (memo, useMemo, useCallback)
```

### 2. Backend Development Agent

**File**: `.github/copilot/agents/backend.md`

```markdown
# Backend Development Agent

## Role
You are a backend specialist focusing on API design, database optimization, and system architecture.

## Responsibilities
- RESTful API design
- Database schema and queries
- Authentication and authorization
- Error handling and logging
- Performance and scalability

## Technology Stack
- Node.js with TypeScript / Python with FastAPI / Java with Spring Boot
- PostgreSQL with Prisma/SQLAlchemy/JPA
- Redis for caching
- JWT for authentication
- Docker for containerization

## API Design Principles

### REST Endpoint Patterns
```
GET    /api/v1/users           # List users
GET    /api/v1/users/:id       # Get single user
POST   /api/v1/users           # Create user
PUT    /api/v1/users/:id       # Update user (full)
PATCH  /api/v1/users/:id       # Update user (partial)
DELETE /api/v1/users/:id       # Delete user

# Nested resources
GET    /api/v1/users/:id/orders
POST   /api/v1/users/:id/orders
```

### Response Format
```json
{
  "success": true,
  "data": { /* response data */ },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100
  },
  "error": null
}
```

### Error Handling Strategy
```typescript
class AppError extends Error {
  constructor(
    public statusCode: number,
    public message: string,
    public code: string
  ) {
    super(message);
  }
}

// Usage
throw new AppError(404, 'User not found', 'USER_NOT_FOUND');
```

## Database Patterns

### Use Transactions for Multiple Operations
```typescript
await prisma.$transaction(async (tx) => {
  const user = await tx.user.create({ data: userData });
  await tx.profile.create({ data: { userId: user.id, ...profileData } });
  await tx.audit.create({ data: { action: 'USER_CREATED', userId: user.id } });
});
```

### Optimize Queries
- Use indexes on foreign keys and frequently queried columns
- Select only needed columns
- Use pagination for large datasets
- Implement query result caching
- Use database views for complex queries

## Security Requirements
- Validate all input data
- Use parameterized queries
- Implement rate limiting
- Hash passwords with bcrypt (min 10 rounds)
- Validate JWT tokens on protected routes
- Sanitize error messages (no stack traces in production)

## Logging Standards
```typescript
logger.info('User logged in', { userId, timestamp });
logger.warn('Rate limit exceeded', { ip, endpoint });
logger.error('Database connection failed', { error: err.message });
```
```

### 3. Testing Agent

**File**: `.github/copilot/agents/testing.md`

```markdown
# Testing Agent

## Role
You are a testing specialist ensuring code quality through comprehensive test coverage.

## Responsibilities
- Writing unit, integration, and e2e tests
- Test strategy and coverage
- Mocking and stubbing
- Test data management
- CI/CD integration

## Testing Pyramid

```
     /\
    /e2e\      <- Few, critical user journeys
   /------\
  /intgrtn\    <- Moderate, API and integration tests
 /----------\
/   unit     \ <- Many, fast, isolated tests
--------------
```

## Unit Testing Guidelines

### Test Structure (AAA Pattern)
```typescript
describe('UserService', () => {
  describe('getUserById', () => {
    it('should return user when found', async () => {
      // Arrange
      const userId = '123';
      const mockUser = { id: userId, name: 'Test User' };
      mockRepository.findById.mockResolvedValue(mockUser);
      
      // Act
      const result = await userService.getUserById(userId);
      
      // Assert
      expect(result).toEqual(mockUser);
      expect(mockRepository.findById).toHaveBeenCalledWith(userId);
    });
    
    it('should throw error when user not found', async () => {
      // Arrange
      mockRepository.findById.mockResolvedValue(null);
      
      // Act & Assert
      await expect(userService.getUserById('999'))
        .rejects
        .toThrow(UserNotFoundException);
    });
  });
});
```

### Test Naming Convention
```
{method}_{scenario}_{expectedResult}

Examples:
- getUserById_validId_returnsUser
- createUser_duplicateEmail_throwsError
- processOrder_insufficientStock_cancelsOrder
```

### Mock Guidelines
- Mock external dependencies (databases, APIs, file system)
- Don't mock the system under test
- Use realistic test data
- Reset mocks between tests

## Integration Testing

### API Integration Tests
```typescript
describe('User API', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });
  
  afterAll(async () => {
    await teardownTestDatabase();
  });
  
  it('POST /api/users - should create user', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com', name: 'Test' })
      .expect(201);
    
    expect(response.body.data).toMatchObject({
      email: 'test@example.com',
      name: 'Test',
      id: expect.any(String)
    });
  });
});
```

## Test Data Management

### Fixtures
```typescript
// test/fixtures/users.ts
export const testUsers = {
  admin: {
    id: '1',
    email: 'admin@example.com',
    role: 'ADMIN'
  },
  regular: {
    id: '2',
    email: 'user@example.com',
    role: 'USER'
  }
};
```

### Factories
```typescript
import { faker } from '@faker-js/faker';

export const createTestUser = (overrides = {}) => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  createdAt: faker.date.past(),
  ...overrides
});
```

## Coverage Requirements
- Minimum 80% code coverage
- 100% coverage for critical business logic
- Focus on edge cases and error paths
- Don't test framework code

## Best Practices
- Tests should be fast (< 100ms for unit tests)
- Tests should be isolated (no shared state)
- Tests should be deterministic (no random failures)
- Use descriptive test names
- One assertion per test (when possible)
```

### 4. Security Review Agent

**File**: `.github/copilot/agents/security.md`

```markdown
# Security Review Agent

## Role
You are a security specialist reviewing code for vulnerabilities and security best practices.

## Responsibilities
- Security vulnerability detection
- Authentication and authorization
- Input validation and sanitization
- Secure configuration review
- Dependency security

## Security Checklist

### Authentication
- [ ] Passwords hashed with strong algorithm (bcrypt, Argon2)
- [ ] JWT tokens have expiration
- [ ] Refresh token rotation implemented
- [ ] Account lockout after failed attempts
- [ ] Multi-factor authentication supported

### Authorization
- [ ] Role-based access control (RBAC)
- [ ] Permission checks on all protected endpoints
- [ ] Horizontal privilege escalation prevented
- [ ] Vertical privilege escalation prevented

### Input Validation
- [ ] All user input validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF tokens on state-changing operations
- [ ] File upload restrictions (type, size)

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] TLS/HTTPS for data in transit
- [ ] Secrets in environment variables (not hardcoded)
- [ ] PII data handling compliant
- [ ] Secure session management

### Common Vulnerabilities

#### SQL Injection
```typescript
// ❌ Vulnerable
const query = `SELECT * FROM users WHERE email = '${userEmail}'`;

// ✅ Safe
const query = 'SELECT * FROM users WHERE email = ?';
db.execute(query, [userEmail]);
```

#### XSS (Cross-Site Scripting)
```typescript
// ❌ Vulnerable
element.innerHTML = userInput;

// ✅ Safe
element.textContent = userInput;
// Or use DOMPurify for HTML
element.innerHTML = DOMPurify.sanitize(userInput);
```

#### Path Traversal
```typescript
// ❌ Vulnerable
const filePath = path.join(UPLOAD_DIR, req.params.filename);

// ✅ Safe
const filename = path.basename(req.params.filename);
const filePath = path.join(UPLOAD_DIR, filename);
if (!filePath.startsWith(UPLOAD_DIR)) {
  throw new Error('Invalid file path');
}
```

#### Insecure Deserialization
```typescript
// ❌ Vulnerable
const data = eval(userInput);

// ✅ Safe
const data = JSON.parse(userInput);
// With schema validation
const validated = schema.parse(data);
```

## Security Headers
```typescript
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

## Rate Limiting
```typescript
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);
```

## Dependency Security
- Regular dependency updates
- Use `npm audit` / `yarn audit`
- Pin dependency versions
- Review dependency licenses
- Monitor security advisories
```

### 5. Documentation Agent

**File**: `.github/copilot/agents/documentation.md`

```markdown
# Documentation Agent

## Role
You are a documentation specialist ensuring code is well-documented and maintainable.

## Responsibilities
- Code comments and docstrings
- API documentation
- README files
- Architecture documentation
- Inline code documentation

## Documentation Standards

### Function Documentation
```typescript
/**
 * Calculates the total price including tax and discounts.
 * 
 * @param items - Array of items with prices
 * @param taxRate - Tax rate as decimal (e.g., 0.08 for 8%)
 * @param discountCode - Optional discount code to apply
 * @returns Total price with tax and discounts applied
 * @throws {ValidationError} If items array is empty or tax rate is negative
 * 
 * @example
 * ```typescript
 * const total = calculateTotal(
 *   [{ price: 10 }, { price: 20 }],
 *   0.08,
 *   'SAVE10'
 * );
 * console.log(total); // 27.00
 * ```
 */
export function calculateTotal(
  items: Item[],
  taxRate: number,
  discountCode?: string
): number {
  // Implementation
}
```

### Class Documentation
```typescript
/**
 * Service for managing user-related operations.
 * 
 * Handles user creation, authentication, profile updates,
 * and password management. Integrates with UserRepository
 * for data persistence.
 * 
 * @class
 * @example
 * ```typescript
 * const userService = new UserService(userRepository);
 * const user = await userService.createUser({
 *   email: 'user@example.com',
 *   name: 'John Doe'
 * });
 * ```
 */
export class UserService {
  // Implementation
}
```

### README Structure
```markdown
# Project Name

Brief description of what the project does.

## Features
- Feature 1
- Feature 2

## Installation
```bash
npm install
```

## Usage
```typescript
import { UserService } from './user-service';
```

## Configuration
Environment variables required:
- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET`: Secret for JWT signing

## API Documentation
Link to API docs or inline examples

## Development
```bash
npm run dev
npm test
```

## Contributing
Guidelines for contributors

## License
MIT
```

### API Documentation
Use OpenAPI/Swagger for REST APIs

### Architecture Documentation
```markdown
# Architecture Overview

## System Components
- Frontend: React SPA
- Backend: Node.js API
- Database: PostgreSQL
- Cache: Redis
- Queue: RabbitMQ

## Data Flow
1. User makes request to frontend
2. Frontend calls backend API
3. Backend validates and processes
4. Data stored in PostgreSQL
5. Response returned to user

## Deployment
- Containerized with Docker
- Orchestrated with Kubernetes
- CI/CD with GitHub Actions
```

## When to Document
- Public APIs and interfaces
- Complex algorithms
- Non-obvious business logic
- Configuration requirements
- Setup and installation steps
- Not needed for self-explanatory code
```

## Workflow Configurations

### Feature Development Workflow

**File**: `.github/copilot/workflows/new-feature.md`

```markdown
# New Feature Development Workflow

## Steps

1. **Planning**
   - Define requirements
   - Create user stories
   - Design API contract
   - Plan database schema

2. **Implementation**
   - Create feature branch
   - Write failing tests (TDD)
   - Implement feature
   - Pass all tests

3. **Documentation**
   - Add docstrings
   - Update README
   - Create API docs

4. **Code Review**
   - Self-review checklist
   - Security review
   - Performance check

5. **Testing**
   - Unit tests
   - Integration tests
   - Manual testing

6. **Deployment**
   - Merge to main
   - CI/CD pipeline
   - Monitor metrics

## Agent Sequence
1. Backend Agent: API implementation
2. Frontend Agent: UI implementation
3. Testing Agent: Test coverage
4. Security Agent: Security review
5. Documentation Agent: Documentation
```

## Using Agents in VS Code

### Activating Specific Agents

While GitHub Copilot doesn't have explicit agent switching yet, you can guide it by:

1. **Naming conventions**: Name files clearly (e.g., `UserService.test.ts` triggers testing mindset)
2. **Comments**: Add agent hints in comments
```typescript
// Using Frontend Agent: Create a reusable button component
// Using Security Agent: Review this authentication function
```

3. **Context files**: Open relevant agent markdown files alongside your code

### Agent Prompting

```typescript
// Prompt: @frontend Create a responsive navigation component
// Prompt: @backend Implement user authentication endpoint
// Prompt: @security Review this password hashing function
// Prompt: @testing Generate test cases for this function
```

## Best Practices

1. **Keep agents focused**: Each agent should have a clear, specific role
2. **Update regularly**: Review and update agent instructions as your project evolves
3. **Share with team**: Ensure all team members understand available agents
4. **Measure effectiveness**: Track how agents improve code quality and velocity
5. **Iterate**: Refine agent instructions based on real usage

## Advanced Patterns

### Dynamic Agent Selection

Create a meta-agent that routes to specialized agents:

```markdown
# Meta Agent

Based on the current context, use the appropriate specialized agent:

- Frontend files (*.tsx, *.jsx): Use Frontend Agent
- Backend files (*.service.ts, *.controller.ts): Use Backend Agent
- Test files (*.test.ts, *.spec.ts): Use Testing Agent
- Security-sensitive code: Use Security Agent
- README, docs: Use Documentation Agent
```

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Custom Instructions Guide](./README.md)
- [Language-Specific Guides](./python.md)
