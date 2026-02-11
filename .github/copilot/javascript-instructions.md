# JavaScript/TypeScript Instructions

## Code Style
- Use TypeScript for type safety
- Use ESM modules (import/export)
- Prefer const over let, avoid var
- Use async/await over callbacks

## Naming Conventions
- Interfaces/Types: PascalCase (UserProfile, ApiResponse)
- Functions/Variables: camelCase (getUserById, isValid)
- Constants: UPPER_SNAKE_CASE (MAX_RETRY, API_URL)
- Components: PascalCase (UserProfile, Button)
- Files: kebab-case (user-service.ts, api-client.ts)

## TypeScript
- Always use explicit types
- Enable strict mode
- Use type inference when obvious
- Avoid any, use unknown instead

## Functions
```typescript
async function fetchUser(userId: string): Promise<User | null> {
  const response = await api.get(`/users/${userId}`);
  return response.data;
}
```

## Error Handling
- Use try-catch for async operations
- Create custom error classes
- Provide meaningful error messages
- Use global error handlers in Express/Next

## Testing
- Use Vitest or Jest
- Test file naming: *.test.ts or *.spec.ts
- Use describe/it blocks
- Mock external dependencies

## React Patterns (if applicable)
- Functional components with hooks
- Use TypeScript for props
- Extract custom hooks for reusable logic
- Use memo/useMemo for performance

## Common Patterns
- Use optional chaining: user?.email
- Use nullish coalescing: value ?? defaultValue
- Destructure objects and arrays
- Use array methods: map, filter, reduce
