# Migration Guide: Microsoft Agent Framework to Anthropic Skills

Complete guide for migrating from Microsoft Agent Framework (using Instructions/Prompts/Agents) to Anthropic Skills, or using both approaches together.

## Overview

This guide helps you migrate your AI agent development from Microsoft Agent Framework patterns to Anthropic Skills while maintaining the same functionality.

## Quick Comparison

| Feature | Microsoft Agent Framework | Anthropic Skills |
|---------|--------------------------|------------------|
| **Agent Definition** | `.agent.md` files | `.vscode/skills.json` |
| **Prompt Templates** | `.prompt.md` files | System prompts in JSON |
| **Instructions** | `.github/copilot-instructions.md` | System prompts |
| **Execution** | Built into VS Code Copilot | Via Continue/Claude Dev extension |
| **Communication** | Native VS Code | API calls to Anthropic |
| **Cost** | Free (with Copilot) | ~$3-15/month (API usage) |
| **Flexibility** | VS Code integrated | Full API control |

## Migration Strategies

### Strategy 1: Hybrid Approach (Recommended)

Use both together for maximum benefit:
- **Microsoft Framework**: For VS Code-integrated workflows
- **Anthropic Skills**: For advanced reasoning and analysis

```
Use Microsoft Agent Framework for:
✅ Development workflow automation
✅ Code generation with team standards
✅ VS Code integrated tasks
✅ Team-wide conventions

Use Anthropic Skills for:
✅ Deep code analysis
✅ Complex reasoning tasks
✅ Advanced security review
✅ Architectural decisions
```

### Strategy 2: Complete Migration

Full migration to Anthropic Skills for unified AI platform.

### Strategy 3: Gradual Migration

Migrate piece by piece while maintaining both systems.

## Migration Process

### Step 1: Analyze Current Setup

**What you have:**
```
.github/
├── copilot-instructions.md    # Development patterns
├── prompts/
│   ├── new-agent.prompt.md    # Agent scaffolding
│   └── agent-communication.prompt.md
└── agents/
    ├── red-team.agent.md      # Security testing
    └── blue-team.agent.md     # Security defense
```

**Map to Anthropic:**
- Instructions → System prompts in skills
- Prompt files → Individual skills
- Agent files → Specialized skills

### Step 2: Convert Instructions

**From: `.github/copilot-instructions.md`**
```markdown
# Development Patterns

## Agent Architecture
- Use modular agent design
- Implement message bus communication
- Each agent has single responsibility

## TypeScript Standards
- Use strict mode
- Define interfaces for messages
- Avoid `any` types
```

**To: Anthropic Skill**
```json
{
  "id": "agent-developer",
  "name": "Agent Developer",
  "description": "Develops agents following Microsoft Agent Framework patterns",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "config": {
    "temperature": 0.4,
    "maxTokens": 4096
  },
  "systemPrompt": "You are an expert in Microsoft Agent Framework development.\n\nDevelopment Patterns:\n- Use modular agent design with clear separation of concerns\n- Implement agents as independent services communicating via message bus\n- Each agent should have a single, well-defined responsibility\n- Use dependency injection for testability\n\nTypeScript Standards:\n- Use strict TypeScript mode\n- Define interfaces for all agent messages\n- Use branded types for IDs and sensitive data\n- Avoid `any` - use `unknown` for truly unknown types\n\nWhen generating code:\n1. Follow the agent interface pattern\n2. Include proper error handling\n3. Add comprehensive type definitions\n4. Write testable code with clear dependencies"
}
```

### Step 3: Convert Prompts

**From: `.github/prompts/new-agent.prompt.md`**
```markdown
---
name: new-agent
description: Create a new agent
---

Generate a complete agent implementation with boilerplate.
${selectedText}
```

**To: Anthropic Skill**
```json
{
  "id": "generate-agent",
  "name": "Generate New Agent",
  "description": "Create complete agent with Microsoft Agent Framework boilerplate",
  "provider": "anthropic",
  "model": "claude-3-sonnet-20240229",
  "systemPrompt": "Generate a complete Microsoft Agent Framework agent implementation.\n\nInclude:\n1. Agent class with Agent interface\n2. Message validation with Zod schemas\n3. Error handling with proper logging\n4. Unit tests with Jest\n5. Integration test template\n6. README with usage examples\n\nAgent structure:\n- id, name, capabilities properties\n- initialize() method for setup\n- process(message) method for message handling\n- shutdown() method for cleanup\n\nEnsure all TypeScript types are properly defined.",
  "triggers": ["generate agent", "create agent", "new agent"]
}
```

### Step 4: Convert Agents

**From: `.github/agents/red-team.agent.md`**
```markdown
---
name: red-team
description: Offensive security agent
---

You are an offensive security specialist.

## Expertise
- OWASP Top 10
- Vulnerability discovery
- Attack simulation
```

**To: Anthropic Skill**
```json
{
  "id": "red-team-security",
  "name": "Red Team Security Analyst",
  "description": "Offensive security analysis for vulnerability discovery",
  "provider": "anthropic",
  "model": "claude-3-opus-20240229",
  "config": {
    "temperature": 0.2,
    "maxTokens": 4096
  },
  "systemPrompt": "You are an offensive security specialist (Red Team) focused on identifying vulnerabilities.\n\nExpertise:\n- OWASP Top 10 vulnerabilities\n- SQL injection, XSS, CSRF, authentication flaws\n- Code analysis for security issues\n- Attack scenario simulation\n- Threat modeling\n\nWhen analyzing code:\n1. Identify all input points\n2. Trace data flow through the application\n3. Find validation gaps and security weaknesses\n4. Document exploitability with proof-of-concept\n5. Provide severity ratings (CRITICAL/HIGH/MEDIUM/LOW)\n\nOutput format:\n{\n  \"vulnerability\": {\n    \"type\": \"SQL_INJECTION\",\n    \"severity\": \"HIGH\",\n    \"location\": \"file:line\",\n    \"description\": \"...\",\n    \"exploit\": \"...\",\n    \"remediation\": \"...\"\n  }\n}\n\nAlways provide clear remediation steps.",
  "triggers": ["security scan", "find vulnerabilities", "red team"]
}
```

### Step 5: Create Skills Configuration

Create `.vscode/skills.json` with all converted skills:

```json
{
  "skills": [
    {
      "id": "agent-developer",
      "name": "Agent Developer",
      "description": "Microsoft Agent Framework development expert",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "..."
    },
    {
      "id": "generate-agent",
      "name": "Generate New Agent",
      "description": "Create complete agent boilerplate",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "..."
    },
    {
      "id": "red-team-security",
      "name": "Red Team Security Analyst",
      "description": "Offensive security analysis",
      "provider": "anthropic",
      "model": "claude-3-opus-20240229",
      "systemPrompt": "..."
    },
    {
      "id": "blue-team-defense",
      "name": "Blue Team Defender",
      "description": "Defensive security and remediation",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "..."
    }
  ]
}
```

## Practical Example: Red/Blue Team Migration

### Before (Microsoft Agent Framework)

```
.github/
├── agents/
│   ├── red-team.agent.md
│   └── blue-team.agent.md
└── prompts/
    └── security-review.prompt.md
```

### After (Anthropic Skills)

```json
{
  "skills": [
    {
      "id": "security-pipeline",
      "name": "Security Analysis Pipeline",
      "description": "Complete security analysis with Red and Blue team coordination",
      "provider": "anthropic",
      "model": "claude-3-opus-20240229",
      "config": {
        "temperature": 0.2,
        "maxTokens": 8192
      },
      "systemPrompt": "You coordinate Red Team and Blue Team security analysis.\n\n**Red Team Phase:**\n1. Scan code for vulnerabilities (OWASP Top 10)\n2. Identify attack vectors\n3. Rate severity\n4. Create proof-of-concept exploits\n\n**Blue Team Phase:**\n1. Receive vulnerability reports\n2. Design secure fixes\n3. Implement remediations\n4. Write security tests\n5. Validate fixes\n\n**Output:**\n1. Vulnerability report with:\n   - Type, severity, location\n   - Exploitation method\n   - Impact analysis\n2. Remediation plan with:\n   - Fix implementation\n   - Security tests\n   - Validation results\n\nProvide both offensive findings and defensive solutions."
    }
  ]
}
```

## Usage Comparison

### Microsoft Agent Framework

```typescript
// In VS Code, type slash command
/new-agent Create a security monitoring agent

// Or use agent mention
@red-team Analyze this code for vulnerabilities
```

### Anthropic Skills

```typescript
// In Continue extension chat
Use the red-team-security skill to analyze this code

// Or via API
const result = await anthropic.messages.create({
  model: "claude-3-opus-20240229",
  system: skills.find(s => s.id === 'red-team-security').systemPrompt,
  messages: [{ role: "user", content: codeToAnalyze }]
});
```

## Hybrid Usage Example

Use both for comprehensive development:

```typescript
// 1. Generate agent structure with Microsoft Agent Framework
// Type in VS Code: /new-agent Security monitoring agent

// 2. Enhance with Anthropic deep analysis
// Use Continue: "Use agent-developer skill to add advanced 
//  threat detection with machine learning patterns"

// 3. Security review with both
// Microsoft: @red-team Quick scan
// Anthropic: "Use security-pipeline skill for comprehensive analysis"

// 4. Implementation with Microsoft
// Type: /agent-communication Design message flow between monitor and alert

// 5. Testing with Anthropic
// Continue: "Use agent-developer skill to generate comprehensive test suite"
```

## Cost Considerations

### Microsoft Agent Framework
- **Cost**: $0 (included with GitHub Copilot subscription)
- **Limits**: VS Code integration limits

### Anthropic Skills
- **Cost**: Pay per API call
  - Claude 3 Haiku: ~$0.25 per million input tokens
  - Claude 3 Sonnet: ~$3 per million input tokens
  - Claude 3 Opus: ~$15 per million input tokens
- **Estimate**: ~$3-15/month for moderate usage

### Hybrid Approach
- Use Microsoft for frequent, simple tasks (free)
- Use Anthropic for complex analysis (paid, but targeted)
- **Estimated cost**: ~$5-10/month

## Migration Checklist

- [ ] Inventory all `.github/copilot-instructions.md` content
- [ ] List all `.prompt.md` files
- [ ] Document all `.agent.md` files
- [ ] Create `.vscode/skills.json` structure
- [ ] Convert instructions to system prompts
- [ ] Convert prompts to skills
- [ ] Convert agents to specialized skills
- [ ] Install Continue or Claude Dev extension
- [ ] Set up Anthropic API key
- [ ] Test each skill individually
- [ ] Document usage for team
- [ ] Train team on new workflow
- [ ] Monitor API usage and costs

## Troubleshooting

### Skills Not Working
```bash
# Check API key
echo $ANTHROPIC_API_KEY

# Test API connection
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"model":"claude-3-sonnet-20240229","messages":[{"role":"user","content":"test"}],"max_tokens":10}'
```

### Skills Not Loading
- Verify `.vscode/skills.json` syntax
- Check file location
- Restart VS Code
- Check Continue extension logs

## Best Practices

### For Hybrid Approach

1. **Use Microsoft for:**
   - Quick code generation
   - Template scaffolding
   - Team conventions
   - Simple transformations

2. **Use Anthropic for:**
   - Deep analysis
   - Security reviews
   - Architecture decisions
   - Complex reasoning

3. **Workflow:**
   ```
   Generate (Microsoft) → Analyze (Anthropic) → Refine (Microsoft) → Validate (Anthropic)
   ```

## Complete Example Repository

See `/examples/ai-agent-development/` for:
- Microsoft Agent Framework setup
- Anthropic Skills configuration
- Hybrid usage examples
- Migration templates

## Resources

- [Microsoft Agent Framework Docs](../docs/custom-agents/README.md)
- [Anthropic Skills Guide](../docs/anthropic-skills/)
- [Continue Extension](https://continue.dev)
- [Anthropic API Docs](https://docs.anthropic.com/)
