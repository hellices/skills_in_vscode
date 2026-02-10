# Agent Skills Guide

Agent Skills are reusable, structured workflows that teach GitHub Copilot how to perform domain-specific tasks.

## What are Agent Skills?

Agent Skills are folders containing `SKILL.md` files that:
- Define step-by-step procedures
- Are automatically loaded when relevant
- Can be shared across projects
- Work with Copilot CLI, VS Code, and Coding Agent

## Quick Example

**Folder**: `.github/skills/write-tests/`

**File**: `.github/skills/write-tests/SKILL.md`
```markdown
---
name: Write Tests
description: Generate comprehensive test suites
---

When asked to write tests:

1. Identify the testing framework (pytest, Jest, JUnit)
2. Generate test structure:
   - Setup/teardown
   - Happy path tests
   - Edge cases
   - Error conditions
3. Use appropriate mocking
4. Follow project conventions from #file:.github/copilot-instructions.md
```

**Usage**: Automatically activated when discussing tests, or explicitly with `/skills write-tests`

## File Structure

```
.github/skills/
├── skill-name/
│   ├── SKILL.md              # Skill definition (required)
│   ├── examples/             # Optional examples
│   └── templates/            # Optional templates
```

## Skill Definition

```markdown
---
name: Skill Name
description: What this skill does
---

# Instructions

Step-by-step procedure for the skill:

1. First step
2. Second step
3. Final step

## Examples

```python
# Example code
```

## Notes
Additional context or tips
```

## Skill Types

### Code Generation Skills
```markdown
---
name: Generate API Endpoint
description: Create REST API endpoint with all boilerplate
---

Generate a complete API endpoint:
1. Route definition
2. Controller method
3. Service layer logic
4. Repository/data access
5. Input validation
6. Error handling
7. Tests
```

### Testing Skills
```markdown
---
name: Write Integration Tests
description: Create integration tests for API endpoints
---

Create integration tests that:
1. Set up test database
2. Make HTTP requests
3. Assert responses
4. Clean up after tests
```

### Deployment Skills
```markdown
---
name: Deploy to Production
description: Production deployment checklist
---

Before deploying:
1. Run all tests
2. Check environment variables
3. Review database migrations
4. Update documentation
5. Create deployment tag
```

## Complete Guide

For detailed documentation:
- [VS Code Agent Skills Documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [GitHub Docs: About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

## Differences from Anthropic Skills

| Feature | VS Code Agent Skills | Anthropic Skills (our docs) |
|---------|---------------------|----------------------------|
| **Provider** | GitHub Copilot native | Anthropic Claude API |
| **Location** | `.github/skills/` | `.vscode/skills.json` |
| **Format** | `SKILL.md` folders | JSON configuration |
| **Activation** | Auto-loaded | Manual trigger |
| **Cost** | Included with Copilot | API usage costs |
| **Integration** | Deep VS Code integration | Via Continue extension |

Both are valuable and can be used together!

## Resources

- [Overview](../overview.md)
- [Custom Instructions](../custom-instructions/README.md)
- [Prompt Files](../prompt-files/README.md)
- [Custom Agents](../custom-agents/README.md)
- [Anthropic Skills](../anthropic-skills/) (Alternative approach)
