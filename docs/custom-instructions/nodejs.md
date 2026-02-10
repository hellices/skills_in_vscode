# Node.js Custom Instructions

This guide provides Node.js and JavaScript/TypeScript-specific custom instructions for GitHub Copilot, focusing on modern practices and common patterns.

## Quick Start

Create `.github/copilot/javascript-instructions.md` in your repository:

```markdown
# Node.js Project Instructions

## Code Style
- Use TypeScript for type safety
- ESM modules (import/export)
- Async/await over callbacks
- Functional programming patterns preferred

## Project Setup
- Node.js version: 18+ LTS
- Package manager: pnpm
- Testing: Vitest
- Linting: ESLint with TypeScript
- Formatting: Prettier

## File Naming
- Components: PascalCase (UserProfile.tsx)
- Utilities: camelCase (formatDate.ts)
- Test files: *.test.ts or *.spec.ts
```

## Complete Example

Here's a comprehensive Node.js custom instructions file:

```markdown
# Node.js Development Guidelines

## Code Style & Conventions

### TypeScript Usage
Always use TypeScript with strict mode enabled:

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "esModuleInterop": true,
    "target": "ES2022",
    "module": "ESNext"
  }
}
```

### Naming Conventions
```typescript
// Interfaces and Types: PascalCase
interface UserProfile {
  id: string;
  email: string;
}

type ApiResponse<T> = {
  success: boolean;
  data: T;
  error?: string;
};

// Functions and Variables: camelCase
const getUserById = async (userId: string): Promise<User> => {
  // implementation
};

// Constants: UPPER_SNAKE_CASE
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = process.env.API_URL;

// Classes: PascalCase
class UserService {
  constructor(private repository: UserRepository) {}
}

// Files: kebab-case
// user-service.ts, api-client.ts
```

### Function Signatures
Use explicit types for all function parameters and returns:

```typescript
// Good
async function fetchUser(userId: string): Promise<User | null> {
  const response = await db.users.findUnique({
    where: { id: userId }
  });
  return response;
}

// Bad
async function fetchUser(userId) {
  return await db.users.findUnique({ where: { id: userId } });
}
```

## Project Structure

### Express API Layout
```
src/
├── index.ts                 # Application entry point
├── app.ts                   # Express app setup
├── config/
│   ├── database.ts          # Database configuration
│   └── env.ts               # Environment variables
├── controllers/             # Request handlers
│   └── user.controller.ts
├── services/                # Business logic
│   └── user.service.ts
├── repositories/            # Data access
│   └── user.repository.ts
├── models/                  # Type definitions
│   └── user.model.ts
├── middleware/              # Express middleware
│   ├── auth.middleware.ts
│   └── error.middleware.ts
├── routes/                  # Route definitions
│   └── user.routes.ts
└── utils/                   # Utility functions
    └── validation.ts
tests/
├── unit/
├── integration/
└── setup.ts
```

## Error Handling

### Custom Error Classes
```typescript
class AppError extends Error {
  constructor(
    public statusCode: number,
    public message: string,
    public isOperational = true
  ) {
    super(message);
    Object.setPrototypeOf(this, AppError.prototype);
  }
}

class NotFoundError extends AppError {
  constructor(resource: string) {
    super(404, `${resource} not found`);
  }
}

class ValidationError extends AppError {
  constructor(message: string) {
    super(400, message);
  }
}

// Usage
if (!user) {
  throw new NotFoundError('User');
}
```

### Global Error Handler
```typescript
import { Request, Response, NextFunction } from 'express';

const errorHandler = (
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      success: false,
      error: err.message
    });
  }

  // Log unexpected errors
  console.error('Unexpected error:', err);
  
  return res.status(500).json({
    success: false,
    error: 'Internal server error'
  });
};
```

### Async Error Wrapper
```typescript
type AsyncHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<any>;

const asyncHandler = (fn: AsyncHandler) => {
  return (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
};

// Usage
router.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await userService.findById(req.params.id);
  if (!user) {
    throw new NotFoundError('User');
  }
  res.json({ success: true, data: user });
}));
```

## Testing Guidelines

### Unit Tests with Vitest
```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { UserService } from './user.service';

describe('UserService', () => {
  let userService: UserService;
  let mockRepository: any;

  beforeEach(() => {
    mockRepository = {
      findById: vi.fn(),
      create: vi.fn()
    };
    userService = new UserService(mockRepository);
  });

  it('should find user by id', async () => {
    const mockUser = { id: '1', email: 'test@example.com' };
    mockRepository.findById.mockResolvedValue(mockUser);

    const result = await userService.getUserById('1');

    expect(result).toEqual(mockUser);
    expect(mockRepository.findById).toHaveBeenCalledWith('1');
  });

  it('should throw error when user not found', async () => {
    mockRepository.findById.mockResolvedValue(null);

    await expect(userService.getUserById('1')).rejects.toThrow(NotFoundError);
  });
});
```

### Integration Tests
```typescript
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import request from 'supertest';
import { app } from '../app';
import { setupTestDatabase, teardownTestDatabase } from './setup';

describe('User API', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

  it('GET /api/users/:id - should return user', async () => {
    const response = await request(app)
      .get('/api/users/1')
      .expect(200);

    expect(response.body).toMatchObject({
      success: true,
      data: {
        id: '1',
        email: expect.any(String)
      }
    });
  });

  it('POST /api/users - should create user', async () => {
    const newUser = {
      email: 'new@example.com',
      name: 'New User'
    };

    const response = await request(app)
      .post('/api/users')
      .send(newUser)
      .expect(201);

    expect(response.body.data).toMatchObject(newUser);
  });
});
```

## Validation

### Use Zod for Runtime Validation
```typescript
import { z } from 'zod';

// Define schema
const UserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().positive().max(150).optional()
});

type User = z.infer<typeof UserSchema>;

// Validation middleware
const validateBody = (schema: z.ZodSchema) => {
  return (req: Request, res: Response, next: NextFunction) => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({
          success: false,
          error: 'Validation failed',
          details: error.errors
        });
      }
      next(error);
    }
  };
};

// Usage
router.post('/users', validateBody(UserSchema), asyncHandler(async (req, res) => {
  const user = await userService.create(req.body);
  res.status(201).json({ success: true, data: user });
}));
```

## Async Patterns

### Prefer Async/Await
```typescript
// Good - Async/await
async function fetchUserData(userId: string) {
  const user = await userRepository.findById(userId);
  const orders = await orderRepository.findByUserId(userId);
  return { user, orders };
}

// Avoid - Callbacks
function fetchUserData(userId: string, callback: Function) {
  userRepository.findById(userId, (err, user) => {
    if (err) return callback(err);
    orderRepository.findByUserId(userId, (err, orders) => {
      if (err) return callback(err);
      callback(null, { user, orders });
    });
  });
}
```

### Parallel Execution
```typescript
// Sequential - slower
async function getData(userId: string) {
  const user = await userRepository.findById(userId);
  const orders = await orderRepository.findByUserId(userId);
  const preferences = await preferenceRepository.findByUserId(userId);
  return { user, orders, preferences };
}

// Parallel - faster
async function getData(userId: string) {
  const [user, orders, preferences] = await Promise.all([
    userRepository.findById(userId),
    orderRepository.findByUserId(userId),
    preferenceRepository.findByUserId(userId)
  ]);
  return { user, orders, preferences };
}
```

## Database Patterns

### Prisma ORM
```typescript
// schema.prisma
model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String
  createdAt DateTime @default(now())
  orders    Order[]
}

model Order {
  id        String   @id @default(cuid())
  userId    String
  user      User     @relation(fields: [userId], references: [id])
  total     Float
  createdAt DateTime @default(now())
}

// Repository pattern
class UserRepository {
  constructor(private prisma: PrismaClient) {}

  async findById(id: string): Promise<User | null> {
    return this.prisma.user.findUnique({
      where: { id },
      include: { orders: true }
    });
  }

  async create(data: CreateUserDto): Promise<User> {
    return this.prisma.user.create({
      data
    });
  }

  async update(id: string, data: UpdateUserDto): Promise<User> {
    return this.prisma.user.update({
      where: { id },
      data
    });
  }
}
```

## API Response Format

### Consistent Response Structure
```typescript
interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  meta?: {
    page?: number;
    limit?: number;
    total?: number;
  };
}

// Success response
const successResponse = <T>(data: T, meta?: any): ApiResponse<T> => ({
  success: true,
  data,
  meta
});

// Error response
const errorResponse = (message: string): ApiResponse => ({
  success: false,
  error: message
});

// Usage
res.json(successResponse(user));
res.status(404).json(errorResponse('User not found'));
```

## Environment Configuration

### Type-Safe Environment Variables
```typescript
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.string().transform(Number),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  API_KEY: z.string()
});

type Env = z.infer<typeof envSchema>;

const env: Env = envSchema.parse(process.env);

export default env;
```

## Security Best Practices

### Input Sanitization
```typescript
import validator from 'validator';

function sanitizeInput(input: string): string {
  return validator.escape(validator.trim(input));
}

function isValidEmail(email: string): boolean {
  return validator.isEmail(email);
}
```

### JWT Authentication
```typescript
import jwt from 'jsonwebtoken';

interface TokenPayload {
  userId: string;
  email: string;
}

export const generateToken = (payload: TokenPayload): string => {
  return jwt.sign(payload, env.JWT_SECRET, {
    expiresIn: '7d'
  });
};

export const verifyToken = (token: string): TokenPayload => {
  return jwt.verify(token, env.JWT_SECRET) as TokenPayload;
};

// Middleware
export const authMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  if (!token) {
    return res.status(401).json(errorResponse('No token provided'));
  }

  try {
    const decoded = verifyToken(token);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(401).json(errorResponse('Invalid token'));
  }
};
```

### Password Hashing
```typescript
import bcrypt from 'bcrypt';

const SALT_ROUNDS = 10;

export async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

export async function comparePassword(
  password: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(password, hash);
}
```

## Logging

### Structured Logging with Pino
```typescript
import pino from 'pino';

const logger = pino({
  level: env.NODE_ENV === 'production' ? 'info' : 'debug',
  transport: env.NODE_ENV === 'development'
    ? { target: 'pino-pretty' }
    : undefined
});

// Usage
logger.info({ userId: '123' }, 'User logged in');
logger.error({ err, userId: '123' }, 'Failed to process order');

// HTTP request logging
import pinoHttp from 'pino-http';

app.use(pinoHttp({ logger }));
```

## Performance Optimization

### Caching with Redis
```typescript
import { createClient } from 'redis';

const redis = createClient({
  url: env.REDIS_URL
});

await redis.connect();

// Cache decorator
function Cache(ttl: number = 3600) {
  return function (
    target: any,
    propertyName: string,
    descriptor: PropertyDescriptor
  ) {
    const original = descriptor.value;

    descriptor.value = async function (...args: any[]) {
      const key = `cache:${propertyName}:${JSON.stringify(args)}`;
      
      const cached = await redis.get(key);
      if (cached) {
        return JSON.parse(cached);
      }

      const result = await original.apply(this, args);
      await redis.setEx(key, ttl, JSON.stringify(result));
      
      return result;
    };

    return descriptor;
  };
}

// Usage
class UserService {
  @Cache(3600)
  async getUserById(userId: string) {
    return this.repository.findById(userId);
  }
}
```

## Common Anti-Patterns to Avoid

### ❌ Callback Hell
```typescript
// Bad
function processUser(userId, callback) {
  getUser(userId, (err, user) => {
    if (err) return callback(err);
    getOrders(user.id, (err, orders) => {
      if (err) return callback(err);
      // More nesting...
    });
  });
}

// Good
async function processUser(userId: string) {
  const user = await getUser(userId);
  const orders = await getOrders(user.id);
  return { user, orders };
}
```

### ❌ Unhandled Promise Rejections
```typescript
// Bad
app.get('/users/:id', (req, res) => {
  getUserById(req.params.id).then(user => {
    res.json(user);
  });
  // Missing .catch()
});

// Good
app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await getUserById(req.params.id);
  res.json(user);
}));
```

## Tools Integration

### Required Development Tools
```json
{
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/node": "^20.0.0",
    "tsx": "^3.12.0",
    "vitest": "^0.34.0",
    "eslint": "^8.50.0",
    "@typescript-eslint/parser": "^6.0.0",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "prettier": "^3.0.0"
  }
}
```

### ESLint Configuration
```javascript
// .eslintrc.js
module.exports = {
  parser: '@typescript-eslint/parser',
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier'
  ],
  rules: {
    '@typescript-eslint/explicit-function-return-type': 'warn',
    '@typescript-eslint/no-explicit-any': 'error',
    'no-console': ['warn', { allow: ['warn', 'error'] }]
  }
};
```

## Additional Resources

- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Express.js Best Practices](https://expressjs.com/en/advanced/best-practice-security.html)
