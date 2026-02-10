# Creating Custom Anthropic Skills

Learn how to create your own custom skills for specific development tasks and workflows.

## Skill Anatomy

A skill consists of:

1. **Metadata**: ID, name, description
2. **Configuration**: Model, parameters
3. **System Prompt**: Instructions for the AI
4. **Triggers**: How the skill is activated
5. **Context**: What information is provided

## Basic Skill Structure

```json
{
  "id": "my-custom-skill",
  "name": "My Custom Skill",
  "description": "What this skill does",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.5,
    "maxTokens": 4096
  },
  "systemPrompt": "Your detailed instructions here",
  "triggers": ["keyword1", "keyword2"],
  "context": {
    "includeSelection": true,
    "includeFile": true,
    "includeWorkspace": false
  }
}
```

## Skill Creation Process

### 1. Define the Purpose

Identify what your skill should do:
- What problem does it solve?
- What inputs does it need?
- What outputs should it provide?
- Who will use it?

### 2. Write the System Prompt

The system prompt is crucial for skill behavior.

**Template:**

```markdown
You are a [ROLE] specialized in [DOMAIN].

Your task is to [MAIN OBJECTIVE].

Guidelines:
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]

Output Format:
[Describe expected output format]

Examples:
[Provide examples if helpful]
```

### 3. Configure Parameters

Choose appropriate model and parameters:

```json
{
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.5,
    "maxTokens": 4096,
    "topP": 0.9,
    "topK": 40
  }
}
```

**Parameter Guide:**

- **temperature**: 0.0-1.0 (lower = more deterministic)
- **maxTokens**: Maximum response length
- **topP**: Nucleus sampling (0.0-1.0)
- **topK**: Top-k sampling

## Example Skills

### 1. API Documentation Generator

```json
{
  "id": "api-doc-generator",
  "name": "API Documentation Generator",
  "description": "Generates OpenAPI/Swagger documentation for REST endpoints",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.4,
    "maxTokens": 4096
  },
  "systemPrompt": "You are an API documentation expert.\n\nAnalyze the provided code and generate OpenAPI 3.0 specification.\n\nInclude:\n- Endpoint paths and methods\n- Request/response schemas\n- Authentication requirements\n- Example requests and responses\n- Error codes and meanings\n\nFormat: YAML OpenAPI 3.0 specification",
  "triggers": ["document api", "generate openapi", "create swagger"],
  "filePatterns": ["**/*controller*.{ts,js,py,java}", "**/*route*.{ts,js,py,java}"],
  "context": {
    "includeSelection": true,
    "includeFile": true
  }
}
```

### 2. Database Schema Optimizer

```json
{
  "id": "schema-optimizer",
  "name": "Database Schema Optimizer",
  "description": "Analyzes and suggests optimizations for database schemas",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.3,
    "maxTokens": 4096
  },
  "systemPrompt": "You are a database optimization expert.\n\nAnalyze the database schema and provide:\n\n1. Index recommendations\n2. Normalization suggestions\n3. Performance optimization tips\n4. Query optimization strategies\n5. Potential bottlenecks\n\nFor each suggestion:\n- Explain the rationale\n- Show before/after examples\n- Estimate performance impact\n- Note any trade-offs",
  "triggers": ["optimize schema", "review database", "improve db"],
  "filePatterns": ["**/*.sql", "**/migrations/*.{ts,js,py}", "**/models/*.{ts,js,py,java}"],
  "context": {
    "includeFile": true,
    "includeRelatedFiles": true
  }
}
```

### 3. Security Vulnerability Scanner

```json
{
  "id": "security-scanner",
  "name": "Security Vulnerability Scanner",
  "description": "Scans code for common security vulnerabilities",
  "provider": "anthropic",
  "model": "claude-3-opus-20240229",
  "config": {
    "temperature": 0.2,
    "maxTokens": 4096
  },
  "systemPrompt": "You are a security expert specializing in OWASP Top 10 vulnerabilities.\n\nScan the code for:\n\n1. SQL Injection\n2. XSS (Cross-Site Scripting)\n3. CSRF (Cross-Site Request Forgery)\n4. Authentication flaws\n5. Authorization bypass\n6. Sensitive data exposure\n7. Insecure deserialization\n8. Path traversal\n9. Command injection\n10. Hardcoded secrets\n\nFor each vulnerability:\n- Severity: CRITICAL/HIGH/MEDIUM/LOW\n- Line number(s)\n- Explanation of the issue\n- Exploit scenario\n- Remediation steps\n- Code fix example",
  "triggers": ["security scan", "find vulnerabilities", "security review"],
  "context": {
    "includeSelection": true,
    "includeFile": true
  }
}
```

### 4. Performance Profiler

```json
{
  "id": "performance-profiler",
  "name": "Performance Profiler",
  "description": "Identifies performance bottlenecks and suggests optimizations",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.4,
    "maxTokens": 4096
  },
  "systemPrompt": "You are a performance optimization expert.\n\nAnalyze code for performance issues:\n\n1. Time Complexity: Identify O(n²) or worse algorithms\n2. Memory Usage: Find memory leaks or excessive allocations\n3. I/O Operations: Detect blocking I/O or unnecessary calls\n4. Database Queries: N+1 problems, missing indexes\n5. Caching Opportunities: What should be cached\n6. Async/Parallel: Where concurrency could help\n\nFor each issue:\n- Current implementation\n- Performance impact\n- Optimized solution\n- Expected improvement\n- Trade-offs to consider",
  "triggers": ["profile performance", "optimize code", "performance review"],
  "context": {
    "includeFile": true,
    "includeWorkspaceSymbols": true
  }
}
```

### 5. Migration Code Generator

```json
{
  "id": "migration-generator",
  "name": "Database Migration Generator",
  "description": "Generates database migration scripts from model changes",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.3,
    "maxTokens": 4096
  },
  "systemPrompt": "You are a database migration expert.\n\nGiven model/schema changes, generate migration scripts.\n\nInclude:\n1. Up migration (apply changes)\n2. Down migration (rollback)\n3. Data migration if needed\n4. Index creation/updates\n5. Constraint modifications\n\nConsiderations:\n- Backwards compatibility\n- Zero-downtime deployment\n- Data integrity\n- Rollback safety\n\nGenerate idempotent, safe migrations with proper error handling.",
  "triggers": ["generate migration", "create migration", "db migration"],
  "filePatterns": ["**/models/*.{ts,js,py,java}"],
  "context": {
    "includeSelection": true,
    "includeFile": true
  }
}
```

### 6. Code Translator

```json
{
  "id": "code-translator",
  "name": "Cross-Language Code Translator",
  "description": "Translates code between programming languages",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.5,
    "maxTokens": 4096
  },
  "systemPrompt": "You are a polyglot programmer expert in multiple languages.\n\nTranslate code to the target language while:\n\n1. Preserving functionality exactly\n2. Using idiomatic patterns in target language\n3. Maintaining code structure when possible\n4. Adding language-specific improvements\n5. Including necessary imports/dependencies\n6. Adding comments for non-obvious translations\n\nTarget language will be specified by the user.\n\nProvide:\n- Translated code\n- List of dependencies needed\n- Notes on any behavioral differences\n- Setup instructions if needed",
  "triggers": ["translate to", "convert to", "port to"],
  "context": {
    "includeSelection": true
  }
}
```

## Advanced Patterns

### Multi-Step Skills

Create skills that work in stages:

```json
{
  "id": "feature-builder",
  "name": "Full Feature Builder",
  "description": "Builds a complete feature from specification",
  "provider": "anthropic",
  "model": "claude-3-opus-20240229",
  "config": {
    "temperature": 0.5,
    "maxTokens": 4096
  },
  "steps": [
    {
      "name": "analyze",
      "prompt": "Analyze the feature requirements and create a technical specification"
    },
    {
      "name": "design",
      "prompt": "Design the API endpoints, data models, and architecture"
    },
    {
      "name": "implement",
      "prompt": "Generate the implementation code following the design"
    },
    {
      "name": "test",
      "prompt": "Generate comprehensive tests for the implementation"
    },
    {
      "name": "document",
      "prompt": "Create documentation for the feature"
    }
  ]
}
```

### Context-Aware Skills

Skills that adapt based on context:

```json
{
  "id": "smart-refactorer",
  "name": "Smart Refactoring Assistant",
  "description": "Context-aware refactoring suggestions",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "contextRules": [
    {
      "when": {"filePattern": "**/*.test.{ts,js}"},
      "systemPrompt": "Focus on test refactoring: reduce duplication, improve readability, add edge cases"
    },
    {
      "when": {"filePattern": "**/components/**/*.{tsx,jsx}"},
      "systemPrompt": "Focus on React component refactoring: extract hooks, improve props, optimize renders"
    },
    {
      "when": {"filePattern": "**/api/**/*.{ts,js,py}"},
      "systemPrompt": "Focus on API refactoring: improve error handling, add validation, optimize queries"
    }
  ]
}
```

### Skill with External Tools

Integrate with external tools:

```json
{
  "id": "lint-and-fix",
  "name": "Lint and Auto-Fix",
  "description": "Runs linter and provides AI-powered fixes",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "preCommands": [
    {
      "command": "eslint ${file} --format json",
      "captureOutput": true
    }
  ],
  "systemPrompt": "You are a code quality expert.\n\nLinter output is provided in context.\n\nFor each error:\n1. Explain the issue\n2. Provide the fix\n3. Explain why the fix works\n4. Suggest prevention strategies",
  "postCommands": [
    {
      "command": "eslint ${file} --fix",
      "condition": "userApproves"
    }
  ]
}
```

## Sharing Skills

### Export Skill

Create a shareable skill file:

**`my-skill.json`**
```json
{
  "name": "My Awesome Skill",
  "version": "1.0.0",
  "author": "Your Name",
  "license": "MIT",
  "skill": {
    "id": "my-awesome-skill",
    "name": "My Awesome Skill",
    "description": "Does something awesome",
    "provider": "anthropic",
    "model": "claude-3-sonnet-20240229",
    "systemPrompt": "..."
  }
}
```

### Import Skill

```bash
# Import from file
code --install-skill ./my-skill.json

# Import from URL
code --install-skill https://example.com/skills/my-skill.json

# Import from marketplace
code --install-skill marketplace:my-awesome-skill
```

### Skill Registry

Create a `skills-registry.json` for your team:

```json
{
  "registry": "https://your-company.com/skills",
  "skills": [
    {
      "id": "company-code-reviewer",
      "source": "https://your-company.com/skills/code-reviewer.json",
      "version": "2.1.0"
    },
    {
      "id": "company-test-generator",
      "source": "https://your-company.com/skills/test-generator.json",
      "version": "1.5.0"
    }
  ]
}
```

## Testing Skills

### Skill Testing Framework

```json
{
  "id": "test-skill",
  "tests": [
    {
      "name": "handles_basic_input",
      "input": "function add(a, b) { return a + b; }",
      "expectedPattern": "test.*add.*should.*return.*sum",
      "timeout": 5000
    },
    {
      "name": "handles_edge_cases",
      "input": "function divide(a, b) { return a / b; }",
      "expectedPattern": "division.*by.*zero",
      "timeout": 5000
    }
  ]
}
```

### Manual Testing

```bash
# Test skill with sample input
gh copilot test-skill my-skill --input "sample code here"

# Test with file
gh copilot test-skill my-skill --file ./test-input.py

# Dry run (see what would be sent)
gh copilot test-skill my-skill --dry-run
```

## Best Practices

### System Prompt Writing

✅ **Do:**
- Be specific and detailed
- Provide examples
- Define output format clearly
- Include edge case handling
- Specify constraints

❌ **Don't:**
- Be vague or ambiguous
- Assume implicit knowledge
- Leave format open-ended
- Ignore error cases
- Make prompts too long (>2000 words)

### Model Selection

- **Haiku**: Fast, simple tasks, autocompletion
- **Sonnet**: Balanced, general development
- **Opus**: Complex reasoning, critical analysis

### Context Management

- Include only relevant context
- Use file patterns to filter
- Limit context size for performance
- Consider privacy/security

### Performance

- Cache common queries
- Use appropriate model for task
- Limit max tokens
- Implement rate limiting

## Troubleshooting

### Skill Not Triggering

1. Check trigger patterns
2. Verify file patterns match
3. Check skill is enabled
4. Reload VS Code

### Poor Quality Responses

1. Improve system prompt specificity
2. Provide better examples
3. Adjust temperature
4. Try different model
5. Add more context

### Rate Limiting Issues

1. Reduce concurrent requests
2. Implement caching
3. Use faster model
4. Batch requests

## Next Steps

1. [Configuration Guide](./configuration.md)
2. [Migration Strategy](../migration/migration-strategy.md)
3. [Example Projects](../../examples/)

## Resources

- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Claude Model Comparison](https://docs.anthropic.com/claude/docs/models-overview)
- [VS Code Extension API](https://code.visualstudio.com/api)
