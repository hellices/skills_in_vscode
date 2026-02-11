# Quick Start Guide

Get started with GitHub Copilot customization in VS Code.

## Choose Your Path

### Path 1: Instructions Only (Free, 2 minutes)
Basic coding standards and conventions.

```bash
# Copy instructions to your project
cp .github/copilot-instructions.md /your-project/.github/

# Start coding - Copilot follows your rules!
```

### Path 2: Add Prompt Files (Free, 5 minutes)
Reusable workflows with slash commands.

```bash
# Copy prompt files
mkdir -p /your-project/.github/prompts
cp examples/prompts/*.prompt.md /your-project/.github/prompts/

# Use in Copilot Chat: /review, /test, /component
```

### Path 3: Add Custom Agents (Free, 10 minutes)
Specialized AI personas for different roles.

```bash
# Copy agent files
mkdir -p /your-project/.github/agents
cp examples/agents/*.agent.md /your-project/.github/agents/

# Use in Copilot Chat: @security, @architect
```

### Path 4: Add Agent Skills (Free, 15 minutes)
Structured workflows for specific tasks.

```bash
# Copy skills
mkdir -p /your-project/.github/skills
cp -r examples/skills/* /your-project/.github/skills/

# Auto-loaded when relevant
```

### Path 5: Anthropic Integration (Paid, 20 minutes)
Add Claude AI capabilities via Continue extension.

```bash
# Install Continue extension
code --install-extension Continue.continue

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Configure
cp examples/python/.vscode/skills.json /your-project/.vscode/
```

## Language-Specific Quick Start

### Python

```bash
cd examples/python
pip install -r requirements.txt
code .
# Start coding - instructions active!
# Try: @code-reviewer or @test-generator
```

### Node.js/TypeScript

```bash
cd examples/nodejs
npm install
code .
# Start coding - instructions active!
# Try: @typescript-reviewer
```

### Java

```bash
cd examples/java
code .
# Start coding - instructions active!
```

## What You Get

### With Instructions ✅
- Automatic code style enforcement
- Naming convention guidance
- Project-specific patterns
- Zero cost, always active

### With Prompt Files ⚡
- Reusable workflows (`/review`, `/test`)
- Standardized team processes
- Zero cost, on-demand

### With Custom Agents 🤖
- Role-specific AI personas (`@security`, `@architect`)
- Specialized expertise
- Tool access control
- Zero cost, context-switching

### With Agent Skills 📚
- Structured task procedures
- Auto-loaded when relevant
- Shareable across projects
- Zero cost, intelligent

### With Anthropic Skills 🚀
- Claude AI capabilities
- Advanced reasoning
- Deep analysis
- ~$3-5/month for moderate use

## Next Steps

1. **Read the overview**: Start with [Customization Overview](./docs/overview.md)
2. **Pick your features**: 
   - [Instructions](./docs/custom-instructions/README.md)
   - [Prompt Files](./docs/prompt-files/README.md)
   - [Custom Agents](./docs/custom-agents/README.md)
   - [Agent Skills](./docs/agent-skills/README.md)
   - [Anthropic Skills](./docs/anthropic-skills/installation.md)
3. **Try examples**: Explore `examples/` directory
4. **Customize**: Edit files for your project needs
5. **Share**: Commit to Git for team collaboration

## Common Questions

**Q: What's the difference between all these options?**
A: 
- **Instructions**: Always-on coding rules
- **Prompt Files**: Reusable workflows (slash commands)
- **Custom Agents**: Role-specific personas
- **Agent Skills**: Structured procedures
- **Anthropic Skills**: Claude AI integration (paid)

**Q: Which should I start with?**
A: Start with Instructions (free, easy). Add others as needed.

**Q: Do I need all of them?**
A: No! Pick what fits your needs. Instructions alone are powerful.

**Q: How much does it cost?**
A: Instructions, Prompts, Agents, and Skills: Free (included with Copilot)
   Anthropic Skills: ~$3-15/month depending on usage

**Q: Can my team use this?**
A: Yes! All files can be shared via Git.

**Q: Which languages are supported?**
A: All languages. We provide examples for Python, Node.js, and Java.

## Help & Resources

- [Full Documentation](./README.md)
- [Custom Instructions Guide](./docs/custom-instructions/README.md)
- [Anthropic Skills Guide](./docs/anthropic-skills/installation.md)
- [Migration Strategy](./docs/migration/migration-strategy.md)
- [Comparison Guide](./docs/migration/comparison.md)

## Problems?

1. Instructions not working? → Reload VS Code window
2. Skills not working? → Check API key and extension installation
3. Need help? → Check troubleshooting sections in docs

---

**Ready?** Pick an option above and start coding smarter! 🚀
