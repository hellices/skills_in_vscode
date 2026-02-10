# Configuring Anthropic Skills

Once you've installed the necessary extensions, configure Anthropic skills to work seamlessly with your development workflow.

## Configuration Files

### Workspace Configuration

Create `.vscode/settings.json` in your project:

```json
{
  "anthropic.apiKey": "${env:ANTHROPIC_API_KEY}",
  "anthropic.model": "claude-3-sonnet-20240229",
  "anthropic.maxTokens": 4096,
  "anthropic.temperature": 0.7,
  
  "continue.telemetryEnabled": false,
  "continue.enableTabAutocomplete": true,
  
  "github.copilot.enable": {
    "*": true
  }
}
```

### Skills Definition

Create `.vscode/skills.json`:

```json
{
  "$schema": "https://example.com/skills-schema.json",
  "version": "1.0",
  "skills": [
    {
      "id": "code-reviewer",
      "name": "Code Reviewer",
      "description": "Analyzes code for quality, security, and best practices",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "config": {
        "temperature": 0.3,
        "maxTokens": 4096
      },
      "systemPrompt": "You are an expert code reviewer. Analyze code for:\n- Security vulnerabilities\n- Performance issues\n- Code style violations\n- Best practice adherence\n- Potential bugs\n\nProvide specific, actionable feedback.",
      "triggers": [
        "review",
        "check code",
        "analyze"
      ]
    },
    {
      "id": "test-generator",
      "name": "Test Generator",
      "description": "Generates comprehensive unit tests",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "config": {
        "temperature": 0.5,
        "maxTokens": 4096
      },
      "systemPrompt": "You are a testing expert. Generate unit tests that:\n- Cover main functionality\n- Test edge cases\n- Use appropriate assertions\n- Follow project testing conventions\n- Include setup and teardown\n- Are well-documented",
      "triggers": [
        "generate tests",
        "create tests",
        "test this"
      ]
    },
    {
      "id": "refactoring-assistant",
      "name": "Refactoring Assistant",
      "description": "Suggests code refactoring improvements",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "config": {
        "temperature": 0.4,
        "maxTokens": 4096
      },
      "systemPrompt": "You are a refactoring expert. Suggest improvements for:\n- Code readability\n- Performance optimization\n- Design patterns\n- SOLID principles\n- Code duplication\n\nExplain the benefits of each suggestion.",
      "triggers": [
        "refactor",
        "improve",
        "optimize"
      ]
    },
    {
      "id": "documentation-writer",
      "name": "Documentation Writer",
      "description": "Generates comprehensive documentation",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "config": {
        "temperature": 0.6,
        "maxTokens": 4096
      },
      "systemPrompt": "You are a technical writer. Create documentation that:\n- Explains what the code does\n- Includes usage examples\n- Documents parameters and return values\n- Describes edge cases\n- Is clear and concise\n- Follows documentation standards",
      "triggers": [
        "document",
        "add docs",
        "explain"
      ]
    },
    {
      "id": "bug-finder",
      "name": "Bug Finder",
      "description": "Identifies potential bugs and issues",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "config": {
        "temperature": 0.2,
        "maxTokens": 4096
      },
      "systemPrompt": "You are a bug detection expert. Look for:\n- Logic errors\n- Edge case handling\n- Null pointer exceptions\n- Race conditions\n- Memory leaks\n- Type errors\n\nExplain how each bug could occur and suggest fixes.",
      "triggers": [
        "find bugs",
        "debug",
        "what's wrong"
      ]
    }
  ]
}
```

## Language-Specific Configurations

### Python Projects

```json
{
  "skills": [
    {
      "id": "python-linter",
      "name": "Python Linter",
      "description": "Checks Python code against PEP 8 and best practices",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "Review Python code for PEP 8 compliance, type hints, docstrings, and Python best practices.",
      "filePatterns": ["**/*.py"]
    }
  ]
}
```

### JavaScript/TypeScript Projects

```json
{
  "skills": [
    {
      "id": "typescript-reviewer",
      "name": "TypeScript Reviewer",
      "description": "Reviews TypeScript for type safety and patterns",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "Review TypeScript code for type safety, best practices, and modern patterns. Check for: proper typing, null safety, async/await usage.",
      "filePatterns": ["**/*.ts", "**/*.tsx"]
    }
  ]
}
```

### Java Projects

```json
{
  "skills": [
    {
      "id": "java-reviewer",
      "name": "Java Reviewer",
      "description": "Reviews Java code for best practices and patterns",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "Review Java code for: SOLID principles, design patterns, Java best practices, Spring Boot conventions (if applicable).",
      "filePatterns": ["**/*.java"]
    }
  ]
}
```

## Environment Variables

Create a `.env` file (add to `.gitignore`):

```bash
# Anthropic Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here
ANTHROPIC_MODEL=claude-3-sonnet-20240229
ANTHROPIC_MAX_TOKENS=4096

# Optional: Rate Limiting
ANTHROPIC_RATE_LIMIT_RPM=50
ANTHROPIC_RATE_LIMIT_RETRY=60

# Optional: Logging
ANTHROPIC_LOG_LEVEL=info
ANTHROPIC_LOG_FILE=.logs/anthropic.log
```

Load in your shell configuration:

```bash
# ~/.bashrc or ~/.zshrc
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
fi
```

## Model Selection Guide

### Available Models

| Model | Best For | Speed | Cost |
|-------|----------|-------|------|
| claude-3-opus-20240229 | Complex reasoning, detailed analysis | Slower | Higher |
| claude-3-sonnet-20240229 | Balanced performance, general use | Medium | Medium |
| claude-3-haiku-20240307 | Quick responses, simple tasks | Faster | Lower |

### Configuration Examples

**High-Quality Code Reviews**
```json
{
  "model": "claude-3-opus-20240229",
  "temperature": 0.2,
  "maxTokens": 4096
}
```

**Fast Autocomplete**
```json
{
  "model": "claude-3-haiku-20240307",
  "temperature": 0.5,
  "maxTokens": 1024
}
```

**Balanced Development**
```json
{
  "model": "claude-3-sonnet-20240229",
  "temperature": 0.4,
  "maxTokens": 2048
}
```

## Advanced Configuration

### Context Window Management

```json
{
  "anthropic.context": {
    "includeOpenFiles": true,
    "includeWorkspaceSymbols": true,
    "maxFilesInContext": 5,
    "maxLinesPerFile": 500
  }
}
```

### Custom Triggers

```json
{
  "anthropic.triggers": {
    "codeReview": {
      "pattern": "^(review|check|analyze)\\s+",
      "skill": "code-reviewer"
    },
    "testGen": {
      "pattern": "^(test|spec)\\s+",
      "skill": "test-generator"
    },
    "docs": {
      "pattern": "^(doc|document|explain)\\s+",
      "skill": "documentation-writer"
    }
  }
}
```

### Skill Chains

Configure skills to work in sequence:

```json
{
  "anthropic.skillChains": [
    {
      "name": "full-review",
      "description": "Complete code review pipeline",
      "steps": [
        {
          "skill": "code-reviewer",
          "description": "Initial code review"
        },
        {
          "skill": "bug-finder",
          "description": "Bug detection"
        },
        {
          "skill": "refactoring-assistant",
          "description": "Refactoring suggestions"
        },
        {
          "skill": "test-generator",
          "description": "Generate missing tests"
        }
      ]
    }
  ]
}
```

## Keyboard Shortcuts

Configure in `.vscode/keybindings.json`:

```json
[
  {
    "key": "ctrl+alt+r",
    "command": "anthropic.runSkill",
    "args": { "skillId": "code-reviewer" },
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+alt+t",
    "command": "anthropic.runSkill",
    "args": { "skillId": "test-generator" },
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+alt+d",
    "command": "anthropic.runSkill",
    "args": { "skillId": "documentation-writer" },
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+alt+f",
    "command": "anthropic.runSkill",
    "args": { "skillId": "bug-finder" },
    "when": "editorTextFocus"
  }
]
```

## Usage Examples

### Command Palette

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Anthropic: Run Skill"
3. Select desired skill
4. Skill executes on current selection or file

### Inline Chat

```typescript
// Select code, then type in chat:
// @code-reviewer Check this function for issues

function processUser(user) {
  return user.name + " " + user.email;
}
```

### Automatic Triggers

Configure automatic skill execution:

```json
{
  "anthropic.autoRun": {
    "onSave": [
      {
        "filePattern": "**/*.py",
        "skill": "python-linter"
      }
    ],
    "onPaste": [
      {
        "filePattern": "**/*.ts",
        "skill": "typescript-reviewer"
      }
    ]
  }
}
```

## Performance Tuning

### Caching

```json
{
  "anthropic.cache": {
    "enabled": true,
    "ttl": 3600,
    "maxSize": "100MB",
    "location": ".vscode/cache/anthropic"
  }
}
```

### Parallel Execution

```json
{
  "anthropic.parallel": {
    "enabled": true,
    "maxConcurrent": 3
  }
}
```

## Monitoring and Logging

### Enable Detailed Logging

```json
{
  "anthropic.logging": {
    "level": "debug",
    "file": ".logs/anthropic.log",
    "console": true,
    "includeTimestamp": true
  }
}
```

### Usage Tracking

```json
{
  "anthropic.tracking": {
    "enabled": true,
    "metrics": {
      "tokensUsed": true,
      "requestCount": true,
      "averageLatency": true
    },
    "outputFile": ".logs/usage.json"
  }
}
```

## Team Collaboration

### Shared Configuration

Commit `.vscode/skills.json` to version control:

```bash
git add .vscode/skills.json
git commit -m "Add team Anthropic skills configuration"
```

### User-Specific Overrides

Create `.vscode/settings.local.json` (add to `.gitignore`):

```json
{
  "anthropic.apiKey": "${env:ANTHROPIC_API_KEY}",
  "anthropic.model": "claude-3-opus-20240229",
  "anthropic.customPreferences": {
    "preferVerboseOutput": true
  }
}
```

## Troubleshooting

### Verify Configuration

```bash
# Check if API key is set
echo $ANTHROPIC_API_KEY

# Test API connection
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"model": "claude-3-sonnet-20240229", "messages": [{"role":"user","content":"test"}], "max_tokens": 10}'
```

### Common Issues

**Skills Not Loading**
- Check JSON syntax in skills.json
- Verify file location (.vscode/skills.json)
- Reload VS Code window

**API Rate Limiting**
- Reduce concurrent requests
- Implement request queuing
- Consider caching responses

**Performance Issues**
- Reduce max tokens
- Use faster model (Haiku)
- Limit context size

## Next Steps

1. [Create Custom Skills](./creating-skills.md)
2. [Migration Strategy](../migration/migration-strategy.md)
3. [Example Projects](../../examples/)

## Resources

- [Anthropic API Docs](https://docs.anthropic.com/)
- [VS Code Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Continue Extension Docs](https://continue.dev/docs)
