# GitHub Copilot Custom Instructions & Anthropic Skills Integration

This repository demonstrates how to use GitHub Copilot custom instructions, integrate Anthropic skills in VS Code, and migrate between the two approaches.

## 📚 Table of Contents

1. [GitHub Copilot Custom Instructions](#github-copilot-custom-instructions)
2. [Anthropic Skills Integration](#anthropic-skills-integration)
3. [Migration & Complementary Strategies](#migration--complementary-strategies)
4. [Quick Start](#quick-start)

## GitHub Copilot Custom Instructions

Custom instructions allow you to define project-specific guidance for GitHub Copilot, improving code suggestions and consistency across your team.

### Documentation

- [📖 Custom Instructions Guide](./docs/custom-instructions/README.md) - Main guide and overview
- [🐍 Python Instructions](./docs/custom-instructions/python.md) - Python-specific examples
- [📦 Node.js Instructions](./docs/custom-instructions/nodejs.md) - Node.js/JavaScript examples
- [☕ Java Instructions](./docs/custom-instructions/java.md) - Java-specific examples
- [🤖 Agent-Based Instructions](./docs/custom-instructions/agents.md) - Advanced agent configurations

### Example Projects

- [`examples/python/`](./examples/python/) - Python project with custom instructions
- [`examples/nodejs/`](./examples/nodejs/) - Node.js project with custom instructions
- [`examples/java/`](./examples/java/) - Java project with custom instructions

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
│   ├── custom-instructions/         # Custom instructions documentation
│   ├── anthropic-skills/            # Anthropic skills documentation
│   └── migration/                   # Migration and comparison guides
├── examples/
│   ├── python/                      # Python example project
│   ├── nodejs/                      # Node.js example project
│   └── java/                        # Java example project
└── skills/
    └── anthropic/                   # Anthropic skill definitions
```

## Resources

- [VS Code Copilot Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Anthropic Claude Skills](https://docs.anthropic.com/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use these examples in your projects.