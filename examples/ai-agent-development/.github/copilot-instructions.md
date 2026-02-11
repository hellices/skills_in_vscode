# AI Agent Development with Microsoft Agent Framework

## Instructions

### Development Patterns

**Agent Architecture**
- Use modular agent design with clear separation of concerns
- Implement agents as independent services communicating via message bus
- Each agent should have a single, well-defined responsibility
- Use dependency injection for testability

**Code Organization**
```
src/
├── agents/           # Agent implementations
│   ├── coordinator/  # Orchestration agent
│   ├── analyst/      # Analysis agents
│   └── executor/     # Action-taking agents
├── common/          # Shared utilities
│   ├── messaging/   # Message bus implementation
│   ├── models/      # Data models
│   └── tools/       # Shared tools and functions
└── config/          # Configuration management
```

### Python Standards (Primary Language)

**Type Safety**
- Use Python 3.11+ with type hints
- Define dataclasses or Pydantic models for all agent messages
- Use Protocol for interface definitions
- Enable mypy strict mode

**Async Patterns**
- Use async/await with asyncio
- Handle exceptions with proper error boundaries
- Implement timeouts with asyncio.wait_for()
- Use asyncio.Task for long-running operations

**Example Agent Interface**
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Protocol

@dataclass
class AgentMessage:
    """Message passed between agents."""
    id: str
    timestamp: datetime
    sender: str
    recipient: str
    content: dict[str, Any]
    metadata: dict[str, Any] | None = None

@dataclass
class AgentResponse:
    """Response from agent processing."""
    success: bool
    data: dict[str, Any] | None = None
    error: str | None = None
    processing_time: float = 0.0

class Agent(Protocol):
    """Agent interface."""
    id: str
    name: str
    capabilities: list[str]
    
    async def process(self, message: AgentMessage) -> AgentResponse:
        """Process incoming message."""
        ...
    
    async def initialize(self) -> None:
        """Initialize agent resources."""
        ...
    
    async def shutdown(self) -> None:
        """Cleanup agent resources."""
        ...
```

### Microsoft Agent Framework Patterns

**Agent Registration**
```python
# Register agents with framework
agent_system = AgentSystem(
    message_timeout=30.0,
    max_retries=3
)

await agent_system.register(CoordinatorAgent())
await agent_system.register(RedTeamAgent())
await agent_system.register(BlueTeamAgent())
```

**Message Handling**
```python
from time import time

class BaseAgent:
    """Base agent implementation."""
    
    async def process(self, message: AgentMessage) -> AgentResponse:
        """Process message with error handling."""
        start_time = time()
        try:
            # Validate message
            validated = self.validate_message(message)
            
            # Process based on message type
            result = await self.handle_message(validated)
            
            # Return response
            return AgentResponse(
                success=True,
                data=result,
                processing_time=time() - start_time
            )
        except Exception as error:
            return self.handle_error(error, time() - start_time)
```

### Linting and Code Quality

**Ruff Configuration (pyproject.toml)**
```toml
[tool.ruff]
line-length = 88
target-version = "py311"
select = ["E", "F", "I", "N", "W", "UP", "ANN", "S", "B"]

[tool.ruff.per-file-ignores]
"tests/*" = ["S101"]  # Allow assert in tests

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
disallow_untyped_defs = true
```

**Required Checks**
- All agents must have unit tests (>80% coverage)
- Integration tests for agent communication
- Type checking with `mypy --strict`
- Linting with `ruff check`
- Security scan with `bandit`

### Testing Requirements

**Unit Tests**
```python
import pytest
from unittest.mock import AsyncMock, MagicMock
from agents.red_team import RedTeamAgent
from common.models import AgentMessage

@pytest.mark.asyncio
class TestRedTeamAgent:
    """Test suite for RedTeamAgent."""
    
    @pytest.fixture
    async def agent(self):
        """Create RedTeamAgent instance."""
        mock_message_bus = AsyncMock()
        agent = RedTeamAgent(mock_message_bus)
        await agent.initialize()
        yield agent
        await agent.shutdown()
    
    async def test_identify_security_vulnerabilities(self, agent):
        """Should identify hardcoded secrets."""
        message = AgentMessage(
            id="test-123",
            timestamp=datetime.now(),
            sender="test",
            recipient="red-team",
            content={
                "type": "analyze_code",
                "code": 'password = "hardcoded123"'
            }
        )
        
        response = await agent.process(message)
        
        assert response.success is True
        assert any(
            v["type"] == "hardcoded_secret" and v["severity"] == "HIGH"
            for v in response.data["vulnerabilities"]
        )
```

**Integration Tests**
```python
import pytest
from agent_system import AgentSystem

@pytest.mark.asyncio
class TestAgentCommunication:
    """Test agent-to-agent communication."""
    
    async def test_red_blue_team_coordination(self):
        """Red and blue teams should coordinate on vulnerabilities."""
        system = await setup_test_agent_system()
        
        # Red team finds vulnerability
        attack = await system.send({
            "to": "red-team",
            "action": "find_vulnerabilities",
            "target": test_code
        })
        
        # Blue team should receive alert and respond
        defense = await system.wait_for_message(
            from_agent="blue-team",
            in_response_to=attack["id"],
            timeout=5.0
        )
        
        assert defense["action"] == "patch_applied"
```

### Security Guidelines

**Sensitive Data**
- Never log agent messages containing user data
- Sanitize all outputs before logging
- Use encryption for agent-to-agent communication
- Implement authentication between agents

**Input Validation**
```python
from pydantic import BaseModel, Field, validator
from datetime import datetime

class AgentMessageSchema(BaseModel):
    """Validated agent message."""
    id: str = Field(..., regex=r'^[a-f0-9-]{36}$')
    timestamp: datetime
    sender: str = Field(..., min_length=1)
    recipient: str = Field(..., min_length=1)
    content: dict
    
    @validator('timestamp')
    def timestamp_not_future(cls, v):
        """Ensure timestamp is not in future."""
        if v > datetime.now():
            raise ValueError('Timestamp cannot be in future')
        return v

class MessageValidator:
    """Validate agent messages."""
    
    def validate(self, message: dict) -> AgentMessage:
        """Validate and return typed message."""
        validated = AgentMessageSchema(**message)
        return AgentMessage(
            id=validated.id,
            timestamp=validated.timestamp,
            sender=validated.sender,
            recipient=validated.recipient,
            content=validated.content
        )
```

### Error Handling

**Graceful Degradation**
- Agents should handle partial failures
- Implement circuit breakers for unreliable agents
- Provide meaningful error messages
- Log errors with context for debugging

**Retry Logic**
```python
import asyncio
from typing import TypeVar, Callable, Awaitable

T = TypeVar('T')

async def with_retry(
    fn: Callable[[], Awaitable[T]],
    max_retries: int = 3,
    delay: float = 1.0
) -> T:
    """Retry async function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return await fn()
        except Exception as error:
            if attempt == max_retries - 1:
                raise
            wait_time = delay * (2 ** attempt)
            await asyncio.sleep(wait_time)
    raise RuntimeError('Retry exhausted')
```

### Performance Considerations

**Message Processing**
- Process messages asynchronously with asyncio
- Implement message queuing for high load (e.g., asyncio.Queue)
- Use batching for bulk operations
- Monitor agent response times

**Resource Management**
- Limit concurrent agent instances with semaphores
- Implement memory limits per agent
- Clean up resources on shutdown
- Monitor CPU and memory usage with psutil

### Documentation Requirements

**Agent Documentation**
```python
class RedTeamAgent:
    """Red Team Agent - Security Testing.
    
    Responsibilities:
    - Identify security vulnerabilities in code
    - Simulate attack scenarios
    - Generate security reports
    
    Communication:
    - Receives: code_analysis_request, security_scan_request
    - Sends: vulnerability_report, attack_scenario
    
    Example:
        >>> agent = RedTeamAgent()
        >>> await agent.initialize()
        >>> result = await agent.process(AgentMessage(
        ...     type='security_scan',
        ...     target=source_code
        ... ))
    """
```

### Observability

**Logging**
```python
import structlog

logger = structlog.get_logger()

class RedTeamAgent:
    """Agent with structured logging."""
    
    async def process(self, message: AgentMessage) -> AgentResponse:
        """Process message with logging."""
        logger.info(
            "processing_message",
            agent=self.name,
            message_id=message.id,
            sender=message.sender
        )
        
        try:
            result = await self.handle_message(message)
            logger.info("message_processed", message_id=message.id)
            return result
        except Exception as error:
            logger.error(
                "processing_error",
                message_id=message.id,
                error=str(error),
                exc_info=True
            )
            raise
```

**Metrics**
- Track message processing time
- Monitor agent success/failure rates
- Measure inter-agent communication latency
- Alert on error rate thresholds

### Optional: TypeScript Implementation

For teams preferring TypeScript, the same patterns can be implemented:

```typescript
// TypeScript version available as an alternative
interface Agent {
  id: string;
  name: string;
  process(message: AgentMessage): Promise<AgentResponse>;
}

class BaseAgent implements Agent {
  async process(message: AgentMessage): Promise<AgentResponse> {
    // Implementation similar to Python version
  }
}
```

See TypeScript-specific documentation for full implementation details.
