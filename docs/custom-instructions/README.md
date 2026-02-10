# GitHub Copilot Custom Instructions Guide

Custom instructions allow you to provide project-specific context and guidelines to GitHub Copilot, ensuring that code suggestions align with your team's practices and conventions.

## What are Custom Instructions?

Custom instructions are Markdown files that you place in your repository to guide Copilot's behavior. They can include:

- Coding standards and style guidelines
- Project-specific patterns and conventions
- Technology stack preferences
- Testing requirements
- Documentation standards
- Security considerations

## How Custom Instructions Work

When you use GitHub Copilot in VS Code, it automatically reads custom instruction files from:

1. **Repository root**: `.github/copilot/instructions.md`
2. **Language-specific**: `.github/copilot/{language}-instructions.md`
3. **Project-specific**: Any `.copilot-instructions.md` in the current directory

Instructions are applied hierarchically, with more specific instructions taking precedence.

## Creating Custom Instructions

### 1. Basic Structure

Create a file at `.github/copilot/instructions.md`:

```markdown
# Project Instructions

## Code Style
- Use descriptive variable names
- Keep functions under 50 lines
- Add docstrings to all public functions

## Testing
- Write unit tests for all new features
- Maintain test coverage above 80%

## Security
- Never hardcode credentials
- Validate all user inputs
- Use parameterized queries for database access
```

### 2. Language-Specific Instructions

Create language-specific files for targeted guidance:

- `.github/copilot/python-instructions.md`
- `.github/copilot/javascript-instructions.md`
- `.github/copilot/java-instructions.md`

### 3. Keep Instructions Concise

**Good**: Clear and actionable
```markdown
## Error Handling
- Use try-except blocks for file operations
- Log errors with context
- Return meaningful error messages
```

**Too Verbose**: Avoid lengthy explanations
```markdown
## Error Handling
In this project, we believe that proper error handling is crucial...
[10 more paragraphs]
```

## Best Practices

### ✅ Do

- **Be specific**: "Use PEP 8 naming conventions" vs "Follow Python standards"
- **Provide examples**: Show code snippets demonstrating patterns
- **Focus on project needs**: Include rules that matter for your codebase
- **Keep it updated**: Review and revise instructions regularly
- **Use sections**: Organize by topic (Style, Testing, Security, etc.)

### ❌ Don't

- Write novel-length instructions (aim for 100-300 lines)
- Include obvious or universal programming principles
- Duplicate language documentation
- Add rules that contradict linters/formatters
- Make instructions too restrictive

## Instruction Priority

Instructions are applied in this order (highest to lowest priority):

1. Workspace-specific (`.copilot-instructions.md` in current folder)
2. Language-specific (`.github/copilot/{language}-instructions.md`)
3. Repository root (`.github/copilot/instructions.md`)
4. User-level instructions (VS Code settings)

## Example Use Cases

### 1. Enforce Team Conventions

```markdown
## Naming Conventions
- React components: PascalCase (UserProfile.tsx)
- Utility functions: camelCase (formatDate.ts)
- Constants: UPPER_SNAKE_CASE (API_BASE_URL)
- Test files: *.test.ts or *.spec.ts
```

### 2. Technology Stack Guidance

```markdown
## Technology Stack
- Frontend: React 18 with TypeScript
- State Management: Zustand (not Redux)
- Styling: Tailwind CSS with custom theme
- Testing: Jest + React Testing Library
- API: GraphQL with Apollo Client
```

### 3. Project-Specific Patterns

```markdown
## Data Access Patterns
- Use repository pattern for database access
- All queries through UserRepository, OrderRepository, etc.
- Never use raw SQL in service layer
- Example:
  ```python
  # Good
  user = user_repository.find_by_id(user_id)
  
  # Bad
  user = db.execute("SELECT * FROM users WHERE id = ?", user_id)
  ```
```

### 4. Security Requirements

```markdown
## Security Guidelines
- Input Validation: Use Pydantic models for API inputs
- Authentication: All endpoints require JWT token
- Authorization: Check permissions using @require_permission decorator
- Sensitive Data: Never log user passwords or tokens
```

## Language-Specific Guides

For detailed examples and best practices for specific languages:

- [Python Custom Instructions](./python.md)
- [Node.js Custom Instructions](./nodejs.md)
- [Java Custom Instructions](./java.md)
- [Agent-Based Instructions](./agents.md)

## Testing Your Instructions

1. Create or modify instructions file
2. Open a file in VS Code
3. Start typing or use Copilot suggestions
4. Verify suggestions align with your instructions
5. Iterate based on results

## Common Patterns

### API Development

```markdown
## API Conventions
- REST endpoints: /api/v1/{resource}
- Use HTTP methods correctly (GET, POST, PUT, DELETE)
- Return JSON with consistent structure:
  {
    "success": boolean,
    "data": any,
    "error": string | null
  }
```

### Database Operations

```markdown
## Database Guidelines
- Use ORM (SQLAlchemy) for all database operations
- Apply migrations for schema changes
- Index foreign keys and frequently queried columns
- Use connection pooling for production
```

### Testing Standards

```markdown
## Testing Requirements
- Unit tests: Test business logic in isolation
- Integration tests: Test API endpoints end-to-end
- Fixture pattern: Use pytest fixtures for test data
- Naming: test_{function_name}_{scenario}_{expected_result}
```

## Troubleshooting

### Instructions Not Being Applied

1. Check file location: Must be in `.github/copilot/`
2. Verify file name: `instructions.md` or `{language}-instructions.md`
3. Check Markdown syntax: Must be valid Markdown
4. Reload VS Code window: Cmd/Ctrl + Shift + P → "Reload Window"

### Conflicting Instructions

If instructions conflict:
- More specific instructions override general ones
- Language-specific > repository root > user settings
- Consider splitting instructions into separate files

## Integration with Tools

Custom instructions work alongside:
- **Linters**: Copilot respects ESLint, Pylint, etc.
- **Formatters**: Works with Prettier, Black, etc.
- **Type Checkers**: Aligns with TypeScript, mypy
- **Git Hooks**: Pre-commit hooks still apply

## Resources

- [VS Code Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
- [Example Repositories](../../examples/)

## Next Steps

1. Choose your language and review the specific guide
2. Create basic instructions for your project
3. Test with real code examples
4. Iterate based on team feedback
5. Explore agent-based instructions for advanced use cases
