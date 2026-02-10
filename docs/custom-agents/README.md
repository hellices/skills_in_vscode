# Custom Agents Guide

Custom agents are specialized AI personas for GitHub Copilot that you can create for specific roles and workflows.

## What are Custom Agents?

Custom agents (`.agent.md` files) allow you to:
- Define AI personas with specific expertise
- Restrict tool access for different roles
- Create multi-step workflows with agent handoffs
- Switch between specialized contexts

## Quick Example

**File**: `.github/agents/security.agent.md`
```markdown
---
name: security
description: Security-focused code reviewer
---

You are a security expert specializing in:
- OWASP Top 10 vulnerabilities
- Secure coding practices
- Authentication and authorization
- Data protection

When reviewing code, focus on security implications.
```

**Usage**: In Copilot Chat → `@security review this code`

## File Structure

```markdown
---
name: agent-name
description: Agent role and purpose
tools: [list, of, allowed, tools]
---

# Agent Instructions

Define the agent's:
- Expertise and knowledge domain
- Review criteria or goals
- Output format
- Restrictions or guidelines
```

## Agent Types

### Read-Only Agents
For analysis without code changes:
```yaml
---
name: analyzer
tools: [read-files, search]
---
```

### Full-Access Agents
For implementation:
```yaml
---
name: implementer
tools: [read-files, write-files, search, terminal]
---
```

## Complete Guide

For detailed documentation and examples:
- [VS Code Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Agent Handoffs and Workflows](https://code.visualstudio.com/docs/copilot/customization/custom-agents#agent-handoffs)

## Resources

- [Overview](../overview.md)
- [Custom Instructions](../custom-instructions/README.md)
- [Prompt Files](../prompt-files/README.md)
- [Agent Skills](../agent-skills/README.md)
