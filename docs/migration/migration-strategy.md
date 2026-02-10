# Migration Strategy: Custom Instructions to Anthropic Skills

This guide helps you migrate from GitHub Copilot custom instructions to Anthropic skills, or use both approaches together.

## Understanding the Difference

### Custom Instructions
- **What**: Markdown files that guide Copilot's behavior
- **Where**: `.github/copilot/*.md` files in your repository
- **Scope**: Repository-wide or language-specific
- **Activation**: Always active when files are present
- **Flexibility**: Static guidelines and patterns
- **Best for**: Project conventions, coding standards

### Anthropic Skills
- **What**: Configurable AI assistants with specific capabilities
- **Where**: `.vscode/skills.json` configuration
- **Scope**: Task-specific or workflow-specific
- **Activation**: Triggered on-demand or by keywords
- **Flexibility**: Dynamic, context-aware responses
- **Best for**: Complex tasks, analysis, generation

## Migration Decision Tree

```
Do you need static coding guidelines?
├─ Yes → Keep Custom Instructions
└─ No
    │
    Do you need dynamic, task-specific assistance?
    ├─ Yes → Use Anthropic Skills
    └─ No → Neither needed
    
Do you want both?
└─ Yes → Use Complementary Strategy (see below)
```

## Migration Approaches

### Approach 1: Complete Migration

Move entirely from custom instructions to skills.

**When to use:**
- Starting a new project
- Want more control over AI behavior
- Need task-specific workflows
- Want to share across projects

**Steps:**

1. **Inventory Existing Instructions**

```bash
# List all custom instruction files
find .github/copilot -name "*.md"
```

2. **Categorize by Purpose**

| Instruction Type | Migration Target |
|-----------------|------------------|
| Code style rules | Skill: code-reviewer |
| Testing guidelines | Skill: test-generator |
| Documentation standards | Skill: documentation-writer |
| Security checks | Skill: security-scanner |
| Architecture patterns | Skill: refactoring-assistant |

3. **Convert to Skills**

Example conversion:

**Before: `.github/copilot/python-instructions.md`**
```markdown
## Testing
- Use pytest for testing
- Name tests: test_{function}_{scenario}_{expected}
- Use fixtures for test data
- Mock external dependencies
```

**After: `.vscode/skills.json`**
```json
{
  "skills": [
    {
      "id": "python-test-generator",
      "name": "Python Test Generator",
      "description": "Generates pytest tests following project conventions",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "Generate pytest tests following these conventions:\n- Test naming: test_{function}_{scenario}_{expected}\n- Use pytest fixtures for test data\n- Mock external dependencies with pytest-mock\n- Include docstrings for test functions\n- Test both success and error cases",
      "filePatterns": ["**/*.py"],
      "triggers": ["generate tests", "create tests", "test this"]
    }
  ]
}
```

4. **Test Migration**

```bash
# Run skill on sample code
gh copilot skill run python-test-generator --file src/user.py

# Compare with previous Copilot suggestions
# Iterate on system prompt as needed
```

5. **Remove Old Instructions**

```bash
# Once satisfied, remove old files
git rm .github/copilot/python-instructions.md
```

### Approach 2: Gradual Migration

Incrementally adopt skills while keeping instructions.

**When to use:**
- Large existing codebase
- Team needs time to adapt
- Want to test skills first
- Maintaining backwards compatibility

**Steps:**

1. **Start with One Domain**

Begin with testing or documentation:

```json
{
  "skills": [
    {
      "id": "test-generator",
      "name": "Test Generator",
      "description": "Generate tests (experimental)",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "systemPrompt": "Generate comprehensive tests..."
    }
  ]
}
```

2. **Parallel Running**

Keep both active for comparison:
- Custom instructions continue guiding regular coding
- Skills handle specific tasks like test generation

3. **Gather Feedback**

Track which approach works better:
- Developer satisfaction
- Code quality metrics
- Time savings
- Error rates

4. **Expand Gradually**

Add more skills over time:
- Week 1: Test generation
- Week 2: Documentation
- Week 3: Code review
- Week 4: Refactoring

5. **Deprecate Instructions**

Once skills prove effective, phase out instructions.

### Approach 3: Hybrid (Recommended)

Use both approaches for different purposes.

**When to use:**
- Want best of both worlds
- Different needs for different tasks
- Team has mixed preferences

## Complementary Strategy

### Division of Responsibilities

**Custom Instructions for:**
- Coding style and formatting
- Naming conventions
- Import organization
- File structure
- Simple, consistent rules
- Always-on guidance

**Anthropic Skills for:**
- Complex code generation
- Code analysis and review
- Test generation
- Documentation creation
- Refactoring suggestions
- On-demand assistance

### Example Setup

**`.github/copilot/instructions.md`**
```markdown
# General Coding Guidelines

## Style
- Follow language-specific style guides
- Use meaningful variable names
- Keep functions small and focused

## Comments
- Add comments for complex logic only
- Use docstrings for public APIs
- Keep comments up to date

## Error Handling
- Use specific exception types
- Provide meaningful error messages
- Log errors with context
```

**`.vscode/skills.json`**
```json
{
  "skills": [
    {
      "id": "code-reviewer",
      "name": "Code Reviewer",
      "description": "Deep code analysis beyond style",
      "systemPrompt": "Review code for:\n- Logic errors\n- Security vulnerabilities\n- Performance issues\n- Design pattern violations\n- Edge cases\n\nProvide specific, actionable feedback."
    },
    {
      "id": "test-generator",
      "name": "Test Generator",
      "description": "Generate comprehensive test suites",
      "systemPrompt": "Generate tests covering:\n- Happy path scenarios\n- Edge cases\n- Error conditions\n- Integration points\n\nFollow project testing conventions."
    }
  ]
}
```

## Migration Patterns by Language

### Python Migration

**Custom Instructions** (keep):
```markdown
- Use PEP 8
- Type hints required
- Docstrings required
```

**Skills** (add):
```json
{
  "id": "python-analyzer",
  "systemPrompt": "Analyze Python code for:\n- Type safety issues\n- Performance bottlenecks\n- Security vulnerabilities\n- Best practice violations"
}
```

### JavaScript/TypeScript Migration

**Custom Instructions** (keep):
```markdown
- TypeScript strict mode
- ESLint + Prettier
- Functional patterns preferred
```

**Skills** (add):
```json
{
  "id": "ts-refactorer",
  "systemPrompt": "Refactor TypeScript for:\n- Better type safety\n- Performance improvements\n- Modern patterns (async/await, optional chaining)\n- Reduced complexity"
}
```

### Java Migration

**Custom Instructions** (keep):
```markdown
- Java 17+ features
- Spring Boot conventions
- Lombok for boilerplate
```

**Skills** (add):
```json
{
  "id": "java-optimizer",
  "systemPrompt": "Optimize Java code for:\n- Stream API usage\n- Record classes\n- Pattern matching\n- Spring Boot best practices"
}
```

## Practical Examples

### Example 1: Test Generation

**Before (Custom Instructions only):**
```markdown
# Testing Guidelines
- Use JUnit 5
- Test naming: methodName_scenario_expected
- Use @DisplayName for readability
- Mock with Mockito
```

Developer manually writes tests following guidelines.

**After (With Skills):**
```bash
# Select method, run skill
@test-generator Generate tests for this method

# Skill generates:
# - Happy path test
# - Edge case tests  
# - Error condition tests
# - Following all conventions from system prompt
```

**Result**: Tests are generated automatically, following conventions, saving time.

### Example 2: Code Review

**Before (Custom Instructions only):**
```markdown
# Code Review Checklist
- Check error handling
- Verify input validation
- Review security
- Check performance
```

Developer manually reviews code against checklist.

**After (With Skills):**
```bash
# Select code, run skill
@code-reviewer Review this code

# Skill provides:
# - Specific issues found
# - Severity ratings
# - Fix suggestions
# - Code examples
```

**Result**: Automated, thorough review with actionable feedback.

### Example 3: Documentation

**Before (Custom Instructions only):**
```markdown
# Documentation Standards
- Use Google-style docstrings
- Include examples
- Document parameters and returns
```

Developer writes documentation following standards.

**After (With Skills):**
```bash
# Select function, run skill
@document Generate documentation

# Skill generates:
# - Complete docstring
# - Usage examples
# - Parameter descriptions
# - Following documentation standards
```

**Result**: Comprehensive documentation generated instantly.

## Team Rollout Plan

### Phase 1: Preparation (Week 1)

1. **Audit Current Instructions**
   - Document all existing custom instructions
   - Categorize by purpose
   - Identify candidates for skills

2. **Set Up Infrastructure**
   - Install Anthropic extensions
   - Configure API keys
   - Create initial skills.json

3. **Train Core Team**
   - Introduction to skills
   - Hands-on workshop
   - Document best practices

### Phase 2: Pilot (Weeks 2-3)

1. **Select Pilot Skills**
   - Start with 2-3 skills
   - Choose high-value use cases
   - Keep custom instructions active

2. **Pilot Group**
   - 3-5 early adopters
   - Provide support channel
   - Gather feedback daily

3. **Iterate**
   - Adjust system prompts
   - Fix issues quickly
   - Document learnings

### Phase 3: Expansion (Weeks 4-6)

1. **Expand to Full Team**
   - Share success stories
   - Provide training sessions
   - Update documentation

2. **Add More Skills**
   - Based on team feedback
   - Create custom skills for team needs
   - Share in skill registry

3. **Monitor Usage**
   - Track adoption metrics
   - Measure impact
   - Collect feedback

### Phase 4: Optimization (Ongoing)

1. **Refine Skills**
   - Update system prompts
   - Optimize performance
   - Add new capabilities

2. **Deprecate Instructions**
   - Remove redundant instructions
   - Keep essential ones
   - Document migration

3. **Share Knowledge**
   - Create skill library
   - Document patterns
   - Train new team members

## Measuring Success

### Metrics to Track

**Quantitative:**
- Lines of code generated
- Time saved per developer
- Test coverage improvement
- Code review time reduction
- Bug reduction rate

**Qualitative:**
- Developer satisfaction
- Code quality perception
- Learning curve feedback
- Team collaboration improvement

### Success Criteria

**Custom Instructions:**
- ✓ Code style consistency
- ✓ Convention adherence
- ✓ Onboarding speed

**Anthropic Skills:**
- ✓ Task completion time
- ✓ Code quality
- ✓ Feature richness
- ✓ Flexibility

## Troubleshooting Migration

### Common Issues

**Issue 1: Skills override instructions**
- **Solution**: Make instructions more general, skills more specific
- **Example**: Instructions say "use camelCase", skill doesn't need to repeat this

**Issue 2: Confusion about which to use**
- **Solution**: Create clear guidelines
- **Example**: "Use skills for generation, instructions for style"

**Issue 3: Skills don't follow instructions**
- **Solution**: Include key instructions in skill system prompts
- **Example**: Add "Follow PEP 8" to Python skill prompts

**Issue 4: Team resistance**
- **Solution**: Start small, show value, provide training
- **Example**: Demo time savings with test generation skill

## Rollback Plan

If migration doesn't work:

1. **Immediate Rollback**
   ```bash
   # Deactivate skills
   mv .vscode/skills.json .vscode/skills.json.backup
   
   # Restore instructions
   git checkout .github/copilot/
   ```

2. **Partial Rollback**
   - Keep working skills
   - Remove problematic ones
   - Restore relevant instructions

3. **Learn and Retry**
   - Analyze what went wrong
   - Adjust approach
   - Try again with improvements

## Next Steps

1. [Complementary Usage Guide](./complementary-usage.md)
2. [Comparison Guide](./comparison.md)
3. [Example Projects](../../examples/)

## Resources

- [Custom Instructions Guide](../custom-instructions/README.md)
- [Creating Skills Guide](../anthropic-skills/creating-skills.md)
- [Configuration Guide](../anthropic-skills/configuration.md)
