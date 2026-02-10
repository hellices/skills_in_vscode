# Complementary Usage: Custom Instructions + Anthropic Skills

Learn how to use custom instructions and Anthropic skills together for maximum effectiveness.

## The Complementary Approach

Using both tools together provides:
- **Foundation**: Custom instructions for consistent style
- **Power**: Skills for complex tasks
- **Flexibility**: Choose the right tool for each need
- **Efficiency**: Automate while maintaining standards

## Architecture

```
┌─────────────────────────────────────┐
│   GitHub Copilot (Base Layer)       │
│   - Autocomplete                     │
│   - Inline suggestions               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Custom Instructions (Style Layer) │
│   - Coding conventions               │
│   - File structure                   │
│   - Naming patterns                  │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Anthropic Skills (Task Layer)     │
│   - Code generation                  │
│   - Analysis & review                │
│   - Complex transformations          │
└─────────────────────────────────────┘
```

## Division of Responsibilities

### Custom Instructions Handle

1. **Coding Style**
   - Indentation, spacing
   - Naming conventions
   - Import organization
   - Comment style

2. **Project Structure**
   - Directory layout
   - File naming
   - Module organization

3. **Simple Rules**
   - Always-on guidelines
   - Static patterns
   - Quick reference

### Anthropic Skills Handle

1. **Code Generation**
   - Boilerplate code
   - Complex logic
   - Test suites
   - Documentation

2. **Analysis**
   - Code review
   - Security audit
   - Performance profiling
   - Bug detection

3. **Transformations**
   - Refactoring
   - Migration
   - Optimization
   - Translation

## Practical Integration Patterns

### Pattern 1: Style + Generation

**Custom Instructions**: Define style
```markdown
# JavaScript Style

## Naming
- Functions: camelCase
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE

## Structure
- One component per file
- Props interface above component
- Hooks before render logic
```

**Skill**: Generate following style
```json
{
  "id": "react-component-generator",
  "systemPrompt": "Generate React components following project style:\n- camelCase for functions\n- PascalCase for components\n- Props interface above component\n- Use TypeScript\n\n[Generate based on description]"
}
```

**Usage**:
```typescript
// Type in editor: "Create a UserProfile component"
// Copilot uses instructions for style
// Run skill for full component generation

@react-component-generator Create UserProfile component with name, email, avatar
```

**Result**: Component generated with perfect style compliance.

### Pattern 2: Standards + Review

**Custom Instructions**: Define standards
```markdown
# Security Standards

## Authentication
- JWT tokens for API auth
- HttpOnly cookies for session
- Tokens expire in 15 minutes

## Validation
- Validate all inputs
- Use Zod schemas
- Sanitize HTML output
```

**Skill**: Review against standards
```json
{
  "id": "security-reviewer",
  "systemPrompt": "Review code against security standards:\n- JWT authentication\n- Input validation with Zod\n- HTML sanitization\n- XSS prevention\n- SQL injection prevention\n\nFlag violations and suggest fixes."
}
```

**Usage**:
```typescript
// Write authentication code
// Copilot suggests patterns from instructions
// Run skill for comprehensive review

function login(email: string, password: string) {
  // ... implementation
}

// Select code, run: @security-reviewer
```

**Result**: Code follows standards, thoroughly reviewed.

### Pattern 3: Conventions + Testing

**Custom Instructions**: Define test conventions
```markdown
# Testing Conventions

## Structure
- Use describe/it blocks
- One assertion per test when possible
- Test files: *.test.ts

## Naming
- test_methodName_scenario_expected
- Descriptive test names

## Mocking
- Mock external dependencies
- Use fixtures for test data
```

**Skill**: Generate tests following conventions
```json
{
  "id": "test-generator",
  "systemPrompt": "Generate tests following conventions:\n- describe/it structure\n- Naming: test_methodName_scenario_expected\n- Mock external dependencies\n- Use fixtures\n- Cover happy path and edge cases"
}
```

**Usage**:
```typescript
// Write function
function calculateDiscount(price: number, code: string): number {
  // implementation
}

// Run: @test-generator Generate tests for calculateDiscount
```

**Result**: Complete test suite following all conventions.

### Pattern 4: Architecture + Refactoring

**Custom Instructions**: Define architecture
```markdown
# Architecture

## Layers
- Controllers: Handle HTTP requests
- Services: Business logic
- Repositories: Data access
- Models: Data structures

## Dependencies
- Controllers → Services
- Services → Repositories
- No circular dependencies
```

**Skill**: Refactor to architecture
```json
{
  "id": "architecture-refactor",
  "systemPrompt": "Refactor code to follow layered architecture:\n- Extract business logic to services\n- Move data access to repositories\n- Controllers handle only HTTP\n- Follow dependency rules\n\nProvide step-by-step refactoring plan."
}
```

**Usage**:
```typescript
// Messy code with everything in controller
@Controller()
class UserController {
  // Database queries, business logic, HTTP handling all mixed
}

// Run: @architecture-refactor
```

**Result**: Clean, properly layered architecture.

## Workflow Examples

### Workflow 1: New Feature Development

1. **Design** (Manual)
   - Define requirements
   - Plan implementation

2. **Generate Boilerplate** (Skill)
   ```bash
   @feature-generator Create user profile feature with CRUD operations
   ```

3. **Style Compliance** (Custom Instructions)
   - Copilot auto-formats as you type
   - Follows naming conventions automatically

4. **Implementation** (Copilot + Instructions)
   - Copilot suggests code
   - Instructions guide patterns

5. **Generate Tests** (Skill)
   ```bash
   @test-generator Generate tests for UserProfileService
   ```

6. **Code Review** (Skill)
   ```bash
   @code-reviewer Review UserProfileService implementation
   ```

7. **Documentation** (Skill)
   ```bash
   @document Generate API documentation for user profile endpoints
   ```

### Workflow 2: Bug Fixing

1. **Identify Issue** (Manual)
   - Understand the bug
   - Locate problematic code

2. **Analyze** (Skill)
   ```bash
   @bug-finder Analyze this function for potential issues
   ```

3. **Fix** (Copilot + Instructions)
   - Implement fix
   - Copilot suggests code following instructions

4. **Test** (Skill)
   ```bash
   @test-generator Generate regression tests for this bug fix
   ```

5. **Review** (Skill)
   ```bash
   @code-reviewer Review the bug fix for any issues
   ```

### Workflow 3: Code Review

1. **Initial Review** (Skill)
   ```bash
   @code-reviewer Review this pull request
   ```

2. **Security Check** (Skill)
   ```bash
   @security-scanner Scan for vulnerabilities
   ```

3. **Performance** (Skill)
   ```bash
   @performance-profiler Check for performance issues
   ```

4. **Style Check** (Custom Instructions)
   - Automatically checked by Copilot
   - Highlighted in real-time

5. **Improvements** (Copilot + Instructions)
   - Apply suggested changes
   - Copilot maintains style consistency

## Team Collaboration

### Shared Configuration

**Repository** (version controlled):
```
.github/
└── copilot/
    ├── instructions.md          # Shared coding standards
    ├── python-instructions.md   # Language-specific
    └── README.md                # Team guidelines

.vscode/
└── skills.json                  # Shared skills
```

**Personal** (not version controlled):
```
.vscode/
└── settings.local.json          # Personal preferences
```

### Team Workflow

1. **Onboarding**
   - New developers clone repo
   - Instructions automatically available
   - Skills pre-configured

2. **Standards Updates**
   ```bash
   # Update instructions
   git pull origin main
   
   # Reload VS Code
   # Changes apply immediately
   ```

3. **Skill Improvements**
   ```bash
   # Team member improves skill
   git add .vscode/skills.json
   git commit -m "Improve test-generator skill"
   git push
   
   # Others pull changes
   # Better skills available to all
   ```

## Configuration Strategy

### Layered Configuration

**Level 1: Repository Instructions** (`.github/copilot/instructions.md`)
```markdown
# Universal coding standards for all contributors
- Follow language style guides
- Write tests for new features
- Document public APIs
```

**Level 2: Language Instructions** (`.github/copilot/python-instructions.md`)
```markdown
# Python-specific standards
- Use PEP 8
- Type hints required
- pytest for testing
```

**Level 3: Workspace Skills** (`.vscode/skills.json`)
```json
{
  "skills": [
    {
      "id": "project-specific-skill",
      "description": "Handles project-specific patterns"
    }
  ]
}
```

**Level 4: User Settings** (User settings.json)
```json
{
  "anthropic.personalPreferences": {
    "verboseOutput": true
  }
}
```

### Priority Order

1. User settings (highest)
2. Workspace skills
3. Language-specific instructions
4. Repository instructions (lowest)

More specific overrides more general.

## Advanced Integration

### Context Sharing

Skills can reference custom instructions:

```json
{
  "id": "smart-generator",
  "systemPrompt": "Generate code following the custom instructions in .github/copilot/.\n\nAdditionally, ensure:\n- Comprehensive error handling\n- Performance optimization\n- Security best practices"
}
```

### Conditional Skills

Skills that adapt to instructions:

```json
{
  "id": "adaptive-refactor",
  "preProcess": {
    "loadInstructions": true
  },
  "systemPrompt": "Read the custom instructions for this project.\n\nRefactor the code to:\n1. Follow all instructions\n2. Improve code quality\n3. Add missing patterns from instructions"
}
```

### Skill Chains with Instructions

```json
{
  "id": "full-feature-pipeline",
  "steps": [
    {
      "name": "generate",
      "skill": "feature-generator",
      "note": "Generates feature following instructions"
    },
    {
      "name": "style",
      "skill": "style-checker",
      "note": "Validates against instructions"
    },
    {
      "name": "test",
      "skill": "test-generator",
      "note": "Tests following test instructions"
    }
  ]
}
```

## Best Practices

### ✅ Do

1. **Keep Instructions Concise**
   - Focus on what's unique to your project
   - Don't repeat universal programming principles

2. **Make Skills Specific**
   - Each skill has one clear purpose
   - Detailed system prompts

3. **Update Both Together**
   - When standards change, update instructions
   - Update related skills to match

4. **Document Integration**
   - Explain which tool does what
   - Guide team on usage

5. **Test Integration**
   - Verify skills follow instructions
   - Check for conflicts

### ❌ Don't

1. **Duplicate Information**
   - Don't repeat instruction content in skills
   - Skills should enhance, not duplicate

2. **Create Conflicts**
   - Ensure skills and instructions align
   - Resolve contradictions

3. **Overload Either Tool**
   - Don't put everything in instructions
   - Don't create one giant skill

4. **Ignore Feedback**
   - Monitor what works
   - Adjust based on team input

5. **Forget Updates**
   - Keep both updated
   - Deprecate outdated patterns

## Monitoring Effectiveness

### Metrics

**Custom Instructions:**
- Style consistency score
- Convention violation rate
- Code review comment reduction

**Anthropic Skills:**
- Usage frequency per skill
- Time saved per task
- Generated code acceptance rate

**Combined:**
- Overall code quality
- Developer velocity
- Team satisfaction

### Feedback Loop

```
Observe Usage
    ↓
Collect Feedback
    ↓
Analyze Metrics
    ↓
Adjust Instructions/Skills
    ↓
Deploy Updates
    ↓
Observe Usage (repeat)
```

## Troubleshooting

### Issue: Skills ignore instructions

**Solution**: Include key instructions in skill prompt
```json
{
  "systemPrompt": "Follow project conventions:\n- [Key conventions from instructions]\n\nAdditionally: [Skill-specific guidance]"
}
```

### Issue: Too much overlap

**Solution**: Clarify responsibilities
- Instructions: What code should look like
- Skills: How to generate/analyze code

### Issue: Conflicts between tools

**Solution**: Establish clear hierarchy
1. Security rules: Strict
2. Style rules: From instructions
3. Generation rules: From skills

## Examples by Use Case

### Use Case 1: API Development

**Instructions**: REST conventions
**Skills**: 
- `api-generator`: Creates endpoints
- `api-documenter`: Generates OpenAPI specs
- `api-tester`: Creates integration tests

### Use Case 2: Frontend Development

**Instructions**: React/component patterns
**Skills**:
- `component-generator`: Creates components
- `state-refactorer`: Optimizes state management
- `a11y-checker`: Validates accessibility

### Use Case 3: Database Work

**Instructions**: Schema conventions
**Skills**:
- `migration-generator`: Creates migrations
- `query-optimizer`: Improves queries
- `schema-validator`: Checks design

## Next Steps

1. [Migration Strategy](./migration-strategy.md)
2. [Comparison Guide](./comparison.md)
3. [Example Projects](../../examples/)

## Resources

- [Custom Instructions Guide](../custom-instructions/README.md)
- [Creating Skills Guide](../anthropic-skills/creating-skills.md)
- [Configuration Guide](../anthropic-skills/configuration.md)
