# GitHub Copilot Customization Guide

Complete guide to customizing GitHub Copilot in VS Code with custom instructions, prompt files, custom agents, and skills.

## 📚 Table of Contents

1. [Overview](#overview)
2. [GitHub Copilot Customization](#github-copilot-customization)
3. [Anthropic Skills Integration](#anthropic-skills-integration)
4. [Migration & Complementary Strategies](#migration--complementary-strategies)
5. [Quick Start](#quick-start)

## Overview

VS Code provides multiple ways to customize GitHub Copilot:

- **[Instructions](./docs/custom-instructions/README.md)**: Always-on coding standards and conventions
- **[Prompt Files](./docs/prompt-files/README.md)**: Reusable prompt templates with slash commands
- **[Custom Agents](./docs/custom-agents/README.md)**: Specialized AI personas for different roles
- **[Agent Skills](./docs/agent-skills/README.md)**: Structured workflows for specific tasks

📖 **Start here**: [Customization Overview](./docs/overview.md)

## GitHub Copilot Customization

### 1. Custom Instructions

Define project-specific coding standards that influence all Copilot suggestions.

**Documentation:**
- [📖 Custom Instructions Guide](./docs/custom-instructions/README.md) - Main guide and overview
- [🐍 Python Instructions](./docs/custom-instructions/python.md) - Python-specific examples
- [📦 Node.js Instructions](./docs/custom-instructions/nodejs.md) - Node.js/JavaScript examples
- [☕ Java Instructions](./docs/custom-instructions/java.md) - Java-specific examples
- [🤖 Agent-Based Instructions](./docs/custom-instructions/agents.md) - Advanced patterns

**Quick Example:**
```markdown
# .github/copilot-instructions.md
- Use TypeScript strict mode
- Follow ESLint rules
- Write tests for new features
```

### 2. Prompt Files

Create reusable workflows invokable with `/command` in Copilot Chat.

**Documentation:**
- [📝 Prompt Files Guide](./docs/prompt-files/README.md)

**Quick Example:**
```markdown
<!-- .github/prompts/review.prompt.md -->
---
name: review
description: Code review
---
Review for: security, performance, best practices
${selectedText}
```

### 3. Custom Agents

Define specialized AI personas with specific expertise and tool access.

**Documentation:**
- [🤖 Custom Agents Guide](./docs/custom-agents/README.md)

**Quick Example:**
```markdown
<!-- .github/agents/security.agent.md -->
---
name: security
description: Security reviewer
---
You are a security expert focusing on OWASP Top 10.
```

### 4. Agent Skills

Teach Copilot domain-specific procedures that are auto-loaded when relevant.

**Documentation:**
- [⚡ Agent Skills Guide](./docs/agent-skills/README.md)

**Quick Example:**
```markdown
<!-- .github/skills/test-gen/SKILL.md -->
---
name: Generate Tests
description: Create test suites
---
1. Detect testing framework
2. Generate test structure
3. Cover edge cases
```

### Example Projects

- [`examples/python/`](./examples/python/) - Python project with custom instructions
- [`examples/nodejs/`](./examples/nodejs/) - Node.js project with custom instructions
- [`examples/java/`](./examples/java/) - Java project with custom instructions
- [`examples/ai-agent-development/`](./examples/ai-agent-development/) - **AI agent development with Microsoft Agent Framework (Python)** - Red/Blue team security workflows

### Example Files

- [`examples/prompts/`](./examples/prompts/) - Prompt file examples (`.prompt.md`)
- [`examples/agents/`](./examples/agents/) - Custom agent examples (`.agent.md`)
- [`examples/skills/`](./examples/skills/) - Agent skill examples (`SKILL.md`)

## Anthropic Skills Integration

Learn how to install and configure Anthropic skills plugins in VS Code using Copilot CLI.

### Documentation

- [🔌 Installation Guide](./docs/anthropic-skills/installation.md) - Step-by-step plugin installation
- [⚙️ Configuration](./docs/anthropic-skills/configuration.md) - Configuration and setup
- [🛠️ Creating Skills](./docs/anthropic-skills/creating-skills.md) - Build your own skills

## Migration & Complementary Strategies

Understand how to migrate from custom instructions to Anthropic skills, or use both together.

- [🔄 Migration Strategy](./docs/migration/migration-strategy.md) - Moving from custom instructions to skills
- [🤝 Complementary Usage](./docs/migration/complementary-usage.md) - Using both approaches together
- [📊 Comparison](./docs/migration/comparison.md) - Feature comparison and decision guide

## Quick Start

### 1. Set Up Custom Instructions

```bash
# Copy custom instructions to your project
cp -r .github/copilot/instructions .github/copilot/

# Or create manually in VS Code
# Create .github/copilot/instructions.md in your project root
```

### 2. Install Anthropic Skills Plugin

```bash
# Install Copilot CLI (if not already installed)
npm install -g @github/copilot-cli

# Configure for Anthropic skills
gh copilot config set editor vscode
```

See the [installation guide](./docs/anthropic-skills/installation.md) for detailed steps.

### 3. Choose Your Approach

- **Custom Instructions**: Best for project-specific coding guidelines and conventions
- **Anthropic Skills**: Best for reusable, shareable capabilities across projects
- **Both**: Use custom instructions for project rules and skills for utilities

## Structure

```
skills_in_vscode/
├── .github/
│   └── copilot/
│       ├── instructions.md          # Root-level custom instructions
│       ├── python-instructions.md   # Python-specific instructions
│       ├── nodejs-instructions.md   # Node.js-specific instructions
│       └── java-instructions.md     # Java-specific instructions
├── docs/
│   ├── overview.md                  # Customization overview
│   ├── custom-instructions/         # Custom instructions documentation
│   ├── prompt-files/                # Prompt files documentation
│   ├── custom-agents/               # Custom agents documentation
│   ├── agent-skills/                # Agent skills documentation
│   ├── anthropic-skills/            # Anthropic skills documentation
│   └── migration/                   # Migration and comparison guides
├── examples/
│   ├── python/                      # Python example project
│   ├── nodejs/                      # Node.js example project
│   ├── java/                        # Java example project
│   ├── prompts/                     # Example .prompt.md files
│   ├── agents/                      # Example .agent.md files
│   └── skills/                      # Example SKILL.md files
└── skills/
    └── anthropic/                   # Anthropic skill definitions
```

## Resources

### VS Code Documentation
- [Customization Overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

### GitHub Documentation
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

### Anthropic
- [Anthropic Claude Documentation](https://docs.anthropic.com/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use these examples in your projects.