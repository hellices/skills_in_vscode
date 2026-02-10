# Quick Start Guide

Get started with GitHub Copilot custom instructions and Anthropic skills in 5 minutes.

## For Impatient Developers

### Option 1: Just Use Custom Instructions (0 cost, 2 minutes)

```bash
# 1. Copy instructions to your project
cp -r .github/copilot /your-project/.github/

# 2. Open VS Code in your project
code /your-project

# 3. Start coding - Copilot now follows your instructions!
```

### Option 2: Full Power Mode (small cost, 5 minutes)

```bash
# 1. Copy custom instructions
cp -r .github/copilot /your-project/.github/

# 2. Copy skills configuration
cp -r .vscode /your-project/

# 3. Set your Anthropic API key
export ANTHROPIC_API_KEY="your-key-here"

# 4. Install Continue extension in VS Code
code --install-extension Continue.continue

# 5. Open your project
code /your-project

# 6. Use skills with Ctrl+I or Command Palette
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

## What Do I Get?

### With Custom Instructions ✅
- Automatic code style enforcement
- Naming convention guidance
- Project-specific patterns
- Zero additional cost
- Always active

### With Anthropic Skills ⚡
- Generate complete test suites
- Deep code analysis
- Security scanning
- Complex refactoring
- Documentation generation
- ~$3-5/month for moderate use

## Next Steps

1. **Read the docs**: Start with [README.md](./README.md)
2. **Try examples**: Explore `examples/` directory
3. **Customize**: Edit `.github/copilot/instructions.md` for your needs
4. **Create skills**: See [Creating Skills Guide](./docs/anthropic-skills/creating-skills.md)
5. **Share with team**: Commit files to your repository

## Common Questions

**Q: Do I need both?**
A: No. Start with custom instructions (free). Add skills later if you need advanced features.

**Q: How much does it cost?**
A: Custom instructions: $0. Anthropic skills: ~$3-15/month depending on usage.

**Q: Which languages are supported?**
A: Both work with any language. We provide examples for Python, Node.js, and Java.

**Q: Can my team use this?**
A: Yes! Custom instructions are shared via Git. Skills need individual API keys.

**Q: Is it hard to set up?**
A: Custom instructions: Very easy (copy files). Skills: Medium (install extension + API key).

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
