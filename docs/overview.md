# Overview: GitHub Copilot Customization

This overview explains all the customization options available in VS Code for GitHub Copilot.

## Customization Options

VS Code provides several ways to customize GitHub Copilot's behavior:

### 1. [Instructions](./custom-instructions/README.md)
Custom instructions help you encode your team's coding standards and project-specific guidelines. They are always active and influence all Copilot suggestions.

**Use for:**
- Coding standards and style guidelines
- Project conventions and patterns
- Technology stack preferences
- Security and quality requirements

**File locations:**
- `.github/copilot-instructions.md` - Project-wide instructions
- `.github/copilot/instructions.md` - Alternative location
- `.github/copilot/{language}-instructions.md` - Language-specific rules

### 2. [Prompt Files](./prompt-files/README.md)
Prompt files are reusable prompt templates that you can invoke with slash commands in Copilot Chat. They standardize common workflows across your team.

**Use for:**
- Code review templates
- Component scaffolding
- Documentation generation
- Testing workflows
- Common refactoring patterns

**File locations:**
- `.github/prompts/*.prompt.md` - Workspace prompts
- `~/.vscode/prompts/*.prompt.md` - Personal prompts

### 3. [Custom Agents](./custom-agents/README.md)
Custom agents are specialized AI personas with specific roles, tools, and instructions. You can switch between agents for different tasks.

**Use for:**
- Role-specific workflows (architect, reviewer, implementer)
- Multi-step workflows with handoffs
- Restricted tool access for specific tasks
- Domain-specific expertise

**File locations:**
- `.github/agents/*.agent.md` - Project agents
- `~/.vscode/agents/*.agent.md` - Personal agents

### 4. [Skills](./agent-skills/README.md)
Skills are reusable, structured workflows that teach Copilot how to perform domain-specific or repetitive tasks. They are automatically loaded when relevant.

**Use for:**
- Test generation patterns
- Deployment procedures
- Code migration workflows
- Project-specific tooling

**File locations:**
- `.github/skills/*/SKILL.md` - Project skills
- `~/.copilot/skills/*/SKILL.md` - Personal skills

## Comparison Matrix

| Feature | Scope | Activation | Best For | File Type |
|---------|-------|------------|----------|-----------|
| **Instructions** | Always-on | Automatic | Coding standards, conventions | `.md` |
| **Prompt Files** | On-demand | `/prompt-name` | Reusable workflows | `.prompt.md` |
| **Custom Agents** | Session-based | `@agent-name` | Role-specific tasks | `.agent.md` |
| **Skills** | Auto-loaded | When relevant | Specialized procedures | `SKILL.md` |

## Getting Started

### Quick Start: Instructions Only (Easiest)

```bash
# Create basic instructions
mkdir -p .github
cat > .github/copilot-instructions.md << 'EOF'
# Project Instructions

## Code Style
- Use TypeScript strict mode
- Follow ESLint rules
- Write tests for new features

## Naming Conventions
- Components: PascalCase
- Functions: camelCase
- Constants: UPPER_SNAKE_CASE
EOF
```

### Full Setup: All Features

```bash
# Create directory structure
mkdir -p .github/{prompts,agents,skills}

# Add instructions
cp examples/.github/copilot-instructions.md .github/

# Add prompt files
cp examples/.github/prompts/*.prompt.md .github/prompts/

# Add custom agents
cp examples/.github/agents/*.agent.md .github/agents/

# Add skills
cp -r examples/.github/skills/* .github/skills/
```

## Hierarchy and Precedence

When multiple customizations apply, they work together:

1. **Instructions** provide the foundation (coding standards)
2. **Skills** add specialized knowledge (how to do specific tasks)
3. **Agents** apply role-specific perspective (who is doing the task)
4. **Prompts** orchestrate workflows (what sequence of steps)

Example workflow:
1. Base coding style from **instructions**
2. Test generation skill from **skills**
3. Security-focused review from **agent**
4. Pull request workflow from **prompt file**

## Best Practices

### Start Simple
1. Begin with basic instructions
2. Add prompt files for common tasks
3. Create agents for specialized roles
4. Build skills for complex workflows

### Keep It Focused
- **Instructions**: General rules only (< 300 lines)
- **Prompts**: Single-purpose workflows
- **Agents**: Clear, distinct roles
- **Skills**: Specific, reusable procedures

### Share with Team
```bash
# Commit customizations to Git
git add .github/
git commit -m "Add Copilot customizations"
git push
```

Team members automatically get:
- ✅ Instructions
- ✅ Prompt files
- ✅ Custom agents
- ✅ Skills

## Migration Path

### From Nothing → Full Setup

**Week 1**: Add basic instructions
```bash
# Start with coding standards
echo "# Use TypeScript strict mode" > .github/copilot-instructions.md
```

**Week 2**: Add your first prompt file
```bash
# Create code review prompt
mkdir -p .github/prompts
cat > .github/prompts/review.prompt.md << 'EOF'
---
name: Code Review
description: Comprehensive code review
---

Review this code for:
- Security vulnerabilities
- Performance issues
- Best practices
- Test coverage
EOF
```

**Week 3**: Create a custom agent
```bash
# Security reviewer agent
mkdir -p .github/agents
cat > .github/agents/security.agent.md << 'EOF'
---
name: Security Reviewer
description: Security-focused code review
---

You are a security expert. Review code for:
- SQL injection
- XSS vulnerabilities
- Authentication issues
- Data exposure
EOF
```

**Week 4**: Add your first skill
```bash
# Test generation skill
mkdir -p .github/skills/test-gen
cat > .github/skills/test-gen/SKILL.md << 'EOF'
---
name: Generate Tests
description: Create comprehensive test suites
---

Generate tests that cover:
1. Happy path scenarios
2. Edge cases
3. Error conditions
4. Integration points
EOF
```

## Examples by Use Case

### Startup / Small Team
- ✅ Instructions: Basic coding standards
- ✅ Prompts: 2-3 common workflows
- ❌ Agents: Not needed yet
- ❌ Skills: Too complex for now

### Growing Team (10-50 developers)
- ✅ Instructions: Comprehensive standards
- ✅ Prompts: 5-10 standardized workflows
- ✅ Agents: 2-3 specialized roles
- ⚠️ Skills: 1-2 critical procedures

### Enterprise (50+ developers)
- ✅ Instructions: Detailed standards
- ✅ Prompts: 20+ workflows
- ✅ Agents: 5+ specialized roles
- ✅ Skills: 10+ domain procedures

## Troubleshooting

### Instructions not applied
- Check file location: `.github/copilot-instructions.md`
- Verify Markdown syntax
- Reload VS Code window

### Prompts not appearing
- Check file extension: `.prompt.md`
- Verify YAML frontmatter
- Look in Command Palette: "GitHub Copilot: Chat"

### Agents not loading
- Check diagnostics: View > Output > GitHub Copilot
- Verify `.agent.md` extension
- Check YAML frontmatter syntax

### Skills not working
- Ensure SKILL.md in folder: `.github/skills/{skill-name}/SKILL.md`
- Check YAML frontmatter
- Restart VS Code

## Resources

- [Custom Instructions Guide](./custom-instructions/README.md)
- [Prompt Files Guide](./prompt-files/README.md)
- [Custom Agents Guide](./custom-agents/README.md)
- [Agent Skills Guide](./agent-skills/README.md)
- [VS Code Documentation](https://code.visualstudio.com/docs/copilot/customization/overview)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)

## Next Steps

1. Choose your starting point based on team size
2. Review the specific guides for each feature
3. Try the examples in this repository
4. Customize for your project
5. Share with your team
