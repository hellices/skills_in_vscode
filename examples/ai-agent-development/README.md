# AI Agent Development with Microsoft Agent Framework

Complete, immediately usable example for developing AI agents using Microsoft Agent Framework in VS Code with **Python** (TypeScript optional).

## Quick Start

```bash
# 1. Copy this example to your project
cp -r examples/ai-agent-development /your-project/

# 2. Open in VS Code
code /your-project/ai-agent-development

# 3. Start developing agents in Python!
# - Custom instructions active automatically
# - Use /new-agent to create agents
# - Use @red-team or @blue-team for security analysis
```

## What's Included

### ✅ Custom Instructions (`.github/copilot-instructions.md`)

Development patterns for Microsoft Agent Framework with **Python**:
- Agent architecture guidelines
- Python 3.11+ standards with type hints
- Async/await patterns with asyncio
- Testing requirements (pytest)
- Security best practices
- Error handling patterns
- Performance considerations

**Always active** - influences all Copilot suggestions

**Note**: TypeScript patterns available as optional alternative

### ✅ Prompt Files (`.github/prompts/`)

Reusable workflows for Python:
- `/new-agent` - Generate complete Python agent with boilerplate
- `/agent-communication` - Design message patterns between agents

**Usage**: Type `/prompt-name` in Copilot Chat

### ✅ Custom Agents (`.github/agents/`)

Specialized AI personas:
- `@red-team` - Offensive security testing
  - Vulnerability discovery
  - Attack simulation
  - Threat modeling
  
- `@blue-team` - Defensive security
  - Remediation planning
  - Security controls implementation
  - Fix validation

**Usage**: Type `@agent-name` in Copilot Chat

### ✅ Agent Skills (`.github/skills/`)

Structured procedures:
- `agent-testing` - Comprehensive testing strategy
  - Unit tests with pytest
  - Integration tests
  - E2E tests
  - Performance tests

**Auto-loaded** when relevant context is detected

### ✅ Migration Guide (`MIGRATION.md`)

Complete guide for:
- Migrating to Anthropic Skills
- Using both approaches together
- Cost optimization strategies
- Practical examples

## Practical Examples

### Example 1: Create New Security Agent (Python)

```bash
# 1. Select this specification:
"""
Create a security monitoring agent that:
- Monitors API requests for suspicious patterns
- Detects potential DDoS attempts
- Alerts on anomalous behavior
- Logs security events
"""

# 2. Use the prompt:
/new-agent

# 3. Get complete implementation:
# - Agent class with full interface
# - Message validation
# - Unit tests
# - Integration tests
# - Documentation
```

### Example 2: Security Analysis Workflow

```python
# 1. Write potentially vulnerable code
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)

# 2. Ask Red Team for analysis
# @red-team Analyze this code for security vulnerabilities

# 3. Get vulnerability report:
# {
#   "type": "SQL_INJECTION",
#   "severity": "HIGH",
#   "exploit": "user_id = '1 OR 1=1'",
#   "remediation": "Use parameterized queries"
# }

# 4. Ask Blue Team for fix
# @blue-team Remediate the SQL injection vulnerability

# 5. Get secure implementation:
def get_user_data(user_id: int) -> dict:
    query = "SELECT * FROM users WHERE id = ?"
    return db.execute(query, (user_id,))
```

### Example 3: Design Agent Communication

```bash
# 1. Describe interaction:
"""
Design communication between:
- Monitoring Agent: Detects threats
- Alert Agent: Sends notifications
- Response Agent: Takes defensive actions
"""

# 2. Use the prompt:
/agent-communication

# 3. Get complete design:
# - Message schemas
# - Communication handlers
# - Sequence diagrams
# - Integration tests
```

## Project Structure

```
ai-agent-development/
├── .github/
│   ├── copilot-instructions.md    # Development patterns & standards
│   ├── prompts/
│   │   ├── new-agent.prompt.md           # Agent scaffolding
│   │   └── agent-communication.prompt.md # Message design
│   ├── agents/
│   │   ├── red-team.agent.md    # Security testing
│   │   └── blue-team.agent.md   # Security defense
│   └── skills/
│       └── agent-testing/
│           └── SKILL.md         # Testing procedures
├── MIGRATION.md                 # Anthropic Skills migration guide
└── README.md                    # This file
```

## Usage Workflows

### Workflow 1: New Agent Development

```
1. Design → /new-agent Create authentication agent
2. Review → @red-team Review security
3. Enhance → Implement feedback
4. Test → Use agent-testing skill
5. Deploy → Ready for production
```

### Workflow 2: Security Hardening

```
1. Scan → @red-team Full security audit
2. Prioritize → Review findings
3. Fix → @blue-team Remediate HIGH severity issues
4. Validate → @red-team Verify fixes
5. Document → Update security docs
```

### Workflow 3: Communication Design

```
1. Specify → /agent-communication Describe interaction
2. Implement → Generate message handlers
3. Test → Create integration tests
4. Monitor → Add observability
```

## Red Team / Blue Team Example

### Red Team: Finding Vulnerabilities

```python
# Code to analyze
class AuthService:
    """Authentication service."""
    
    def login(self, username: str, password: str):
        """Login user."""
        user = db.query(f"""
            SELECT * FROM users 
            WHERE username = '{username}' 
            AND password = '{password}'
        """)
        return generate_token(user) if user else None

# Ask Red Team
# @red-team Perform security analysis

# Red Team finds:
# 1. SQL Injection in username/password
# 2. Plaintext password comparison
# 3. No rate limiting
# 4. Missing input validation
```

### Blue Team: Implementing Fixes

```python
# Ask Blue Team
# @blue-team Fix the identified vulnerabilities

# Blue Team provides secure implementation:
import bcrypt
from pydantic import BaseModel, Field, validator
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

class LoginSchema(BaseModel):
    """Login request validation."""
    username: str = Field(..., min_length=3, max_length=50, regex=r'^[a-zA-Z0-9_]+$')
    password: str = Field(..., min_length=8)

class AuthService:
    """Secure authentication service."""
    
    async def login(self, username: str, password: str) -> dict | None:
        """Login user with secure implementation."""
        # Validate input
        validated = LoginSchema(username=username, password=password)
        
        # Use parameterized query
        user = await db.query(
            "SELECT * FROM users WHERE username = ?",
            (validated.username,)
        )
        
        if not user:
            return None
        
        # Compare hashed password
        is_valid = bcrypt.checkpw(
            validated.password.encode(),
            user.password_hash.encode()
        )
        
        return generate_token(user) if is_valid else None

# Apply rate limiting
@app.post('/login')
@limiter.limit("5/15minutes")
async def login_endpoint(request: LoginRequest):
    # ... login logic
```

## Testing Your Agents

Use the agent-testing skill:

```python
# Generate comprehensive tests
# Use agent-testing skill to create tests for AuthService

# Result: Complete pytest test suite
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestAuthService:
    """Test suite for AuthService."""
    
    async def test_reject_sql_injection(self):
        """Should reject SQL injection attempts."""
        auth_service = AuthService()
        malicious_input = "admin' OR '1'='1"
        
        with pytest.raises(ValueError, match="Invalid username"):
            await auth_service.login(malicious_input, "password")
    
    async def test_rate_limiting(self, client):
        """Should enforce rate limiting."""
        # Attempt 6 logins in quick succession
        for _ in range(6):
            await client.post('/login', json={
                "username": "test",
                "password": "password"
            })
        
        # 7th attempt should be rate limited
        response = await client.post('/login', json={
            "username": "test",
            "password": "password"
        })
        
        assert response.status_code == 429
```

## Anthropic Skills Alternative

Want more advanced AI capabilities? See `MIGRATION.md` for:
- Converting to Anthropic Skills
- Hybrid approach (use both)
- Cost optimization
- Complete examples

### Quick Anthropic Setup

```bash
# 1. Install Continue extension
code --install-extension Continue.continue

# 2. Set API key
export ANTHROPIC_API_KEY="your-key-here"

# 3. Use in Continue chat
"Use red-team-security skill to analyze this code"
```

## Tips & Best Practices

### 1. Use the Right Tool

- **Slash commands** (`/new-agent`) - Quick generation
- **Agent mentions** (`@red-team`) - Specialized analysis
- **Skills** (auto-loaded) - Structured procedures

### 2. Iterative Development

```
Generate → Review → Refine → Test → Deploy
  ↓         ↓         ↓        ↓       ↓
/prompt  @agent   Edit   Skill    Push
```

### 3. Security First

Always run security analysis:
```
1. Write code
2. @red-team Analyze
3. @blue-team Fix
4. @red-team Verify
```

### 4. Test Everything

Use agent-testing skill for:
- Unit tests (required)
- Integration tests (required)
- E2E tests (critical paths)
- Performance tests (key operations)

## Team Collaboration

### Sharing with Team

```bash
# Commit to Git
git add .github/
git commit -m "Add AI agent development framework"
git push

# Team members get automatically:
# ✅ Custom instructions
# ✅ Prompt files
# ✅ Agent personas
# ✅ Testing skills
```

### Team Standards

All team members now:
- Follow same agent patterns
- Use same security practices
- Generate consistent code
- Apply same testing standards

## Advanced Usage

### Chaining Agents

```python
# Complex workflow
# 1. @red-team Analyze security
# 2. Review findings
# 3. @blue-team Implement top 3 fixes
# 4. @red-team Validate fixes
# 5. Document changes
```

### Custom Combinations

```python
# Generate + Secure + Test
# /new-agent Create payment processor
# @blue-team Add security controls
# Generate comprehensive tests for payment processor
```

## Troubleshooting

### Prompts Not Working

```bash
# Check location
ls -la .github/prompts/

# Verify syntax (YAML frontmatter required)
head -5 .github/prompts/new-agent.prompt.md

# Reload VS Code
# Cmd/Ctrl + Shift + P → "Reload Window"
```

### Agents Not Responding

```bash
# Check diagnostics
# View > Output > GitHub Copilot

# Verify file extension
ls .github/agents/*.agent.md

# Check frontmatter
head -5 .github/agents/red-team.agent.md
```

## Next Steps

1. ✅ **Try the examples** - Follow the workflows above
2. ✅ **Create your agents** - Use `/new-agent`
3. ✅ **Run security analysis** - Use `@red-team` and `@blue-team`
4. ✅ **Generate tests** - Let the testing skill help
5. ✅ **Consider Anthropic** - Read `MIGRATION.md` for advanced features

## Resources

- [Microsoft Agent Framework Docs](../../docs/custom-agents/README.md)
- [Prompt Files Guide](../../docs/prompt-files/README.md)
- [Agent Skills Guide](../../docs/agent-skills/README.md)
- [Anthropic Migration](./MIGRATION.md)
- [Main Repository](../../README.md)

## Support

- **Issues**: Open issue in repository
- **Questions**: Check documentation
- **Contributions**: PRs welcome!

---

**Ready to build AI agents?** Start with `/new-agent`! 🚀
