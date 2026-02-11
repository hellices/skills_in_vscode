---
name: new-agent
description: Create a new agent with Microsoft Agent Framework boilerplate (Python)
argument-hint: Agent name and purpose
---

# Create New Agent

Generate a complete Python agent implementation with all required boilerplate.

## Agent Specification

${selectedText}

## Generate

Create the following files:

### 1. Agent Implementation

```python
# src/agents/{agent_name}/{agent_name}_agent.py

from dataclasses import dataclass
from datetime import datetime
from typing import Any
import structlog
from common.models import Agent, AgentMessage, AgentResponse
from common.logger import get_logger

logger = get_logger(__name__)

@dataclass
class {AgentName}Config:
    """Configuration for {AgentName}Agent."""
    id: str | None = None
    max_concurrent_tasks: int = 5
    timeout_seconds: float = 30.0

class {AgentName}Agent(Agent):
    """{AgentName} Agent.
    
    Purpose: {Brief description}
    
    Capabilities:
    - {Capability 1}
    - {Capability 2}
    """
    
    def __init__(self, config: {AgentName}Config | None = None):
        """Initialize agent."""
        config = config or {AgentName}Config()
        self.id = config.id or self._generate_agent_id()
        self.name = "{agent_name}"
        self.capabilities = ["{capability1}", "{capability2}"]
        self.config = config
        self._initialized = False
        self.logger = logger.bind(agent=self.name, agent_id=self.id)
    
    async def initialize(self) -> None:
        """Initialize agent resources."""
        self.logger.info("initializing_agent")
        
        # Initialize resources
        # Connect to services
        # Load configuration
        
        self._initialized = True
        self.logger.info("agent_initialized")
    
    async def process(self, message: AgentMessage) -> AgentResponse:
        """Process incoming message."""
        if not self._initialized:
            raise RuntimeError("Agent not initialized")
        
        self.logger.debug("processing_message", message_id=message.id)
        
        start_time = datetime.now()
        try:
            # Validate message
            validated = self._validate_message(message)
            
            # Process based on message type
            result = await self._handle_message(validated)
            
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return AgentResponse(
                success=True,
                data=result,
                processing_time=processing_time
            )
        except Exception as error:
            self.logger.error(
                "processing_error",
                message_id=message.id,
                error=str(error),
                exc_info=True
            )
            return self._handle_error(error, start_time)
    
    async def shutdown(self) -> None:
        """Cleanup agent resources."""
        self.logger.info("shutting_down_agent")
        
        # Clean up resources
        # Close connections
        
        self._initialized = False
        self.logger.info("agent_shutdown_complete")
    
    def _validate_message(self, message: AgentMessage) -> dict[str, Any]:
        """Validate message content."""
        from pydantic import BaseModel, Field
        
        class MessageSchema(BaseModel):
            type: str = Field(..., pattern="^(action1|action2)$")
            data: dict[str, Any]
        
        validated = MessageSchema(**message.content)
        return validated.dict()
    
    async def _handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """Handle validated message."""
        message_type = message["type"]
        
        if message_type == "action1":
            return await self._handle_action1(message["data"])
        elif message_type == "action2":
            return await self._handle_action2(message["data"])
        else:
            raise ValueError(f"Unknown message type: {message_type}")
    
    async def _handle_action1(self, data: dict[str, Any]) -> dict[str, Any]:
        """Handle action1."""
        # Implement action 1
        return {"result": "action1_completed"}
    
    async def _handle_action2(self, data: dict[str, Any]) -> dict[str, Any]:
        """Handle action2."""
        # Implement action 2
        return {"result": "action2_completed"}
    
    def _handle_error(
        self,
        error: Exception,
        start_time: datetime
    ) -> AgentResponse:
        """Handle processing error."""
        processing_time = (datetime.now() - start_time).total_seconds()
        return AgentResponse(
            success=False,
            error=str(error),
            processing_time=processing_time
        )
    
    @staticmethod
    def _generate_agent_id() -> str:
        """Generate unique agent ID."""
        import uuid
        return str(uuid.uuid4())
```

### 2. Agent Configuration

```python
# src/agents/{agent_name}/config.py

from dataclasses import dataclass

@dataclass
class {AgentName}Config:
    """Configuration for {AgentName}Agent."""
    id: str | None = None
    # Add agent-specific configuration
    max_concurrent_tasks: int = 5
    timeout_seconds: float = 30.0

# Default configuration
DEFAULT_{AGENT_NAME}_CONFIG = {AgentName}Config(
    max_concurrent_tasks=5,
    timeout_seconds=30.0
)
```

### 3. Unit Tests

```python
# tests/agents/{agent_name}/test_{agent_name}_agent.py

import pytest
from datetime import datetime
from agents.{agent_name}.{agent_name}_agent import {AgentName}Agent
from common.models import AgentMessage

@pytest.mark.asyncio
class Test{AgentName}Agent:
    """Test suite for {AgentName}Agent."""
    
    @pytest.fixture
    async def agent(self):
        """Create agent instance for testing."""
        agent = {AgentName}Agent()
        await agent.initialize()
        yield agent
        await agent.shutdown()
    
    async def test_initialization(self):
        """Agent should initialize successfully."""
        agent = {AgentName}Agent()
        await agent.initialize()
        assert agent._initialized is True
        await agent.shutdown()
    
    async def test_process_action1_message(self, agent):
        """Should process action1 messages."""
        message = AgentMessage(
            id="test-123",
            timestamp=datetime.now(),
            sender="test",
            recipient=agent.id,
            content={
                "type": "action1",
                "data": {"test": True}
            }
        )
        
        response = await agent.process(message)
        
        assert response.success is True
        assert "result" in response.data
    
    async def test_handle_invalid_message(self, agent):
        """Should handle invalid messages gracefully."""
        message = AgentMessage(
            id="test-456",
            timestamp=datetime.now(),
            sender="test",
            recipient=agent.id,
            content={
                "type": "invalid",
                "data": {}
            }
        )
        
        response = await agent.process(message)
        
        assert response.success is False
        assert response.error is not None
```

### 4. Integration Test

```python
# tests/integration/test_{agent_name}_integration.py

import pytest
from agent_system import AgentSystem
from agents.{agent_name}.{agent_name}_agent import {AgentName}Agent

@pytest.mark.asyncio
class Test{AgentName}Integration:
    """Integration tests for {AgentName}Agent."""
    
    @pytest.fixture
    async def system(self):
        """Create agent system for testing."""
        system = AgentSystem()
        agent = {AgentName}Agent()
        await system.register(agent)
        await system.start()
        yield system
        await system.stop()
    
    async def test_agent_communication(self, system):
        """Agent should communicate with system."""
        message = {
            "to": "{agent_name}",
            "action": "action1",
            "data": {"test": True}
        }
        
        response = await system.send(message)
        
        assert response["success"] is True
```

### 5. README

```markdown
# {AgentName} Agent

## Purpose

{Brief description of what this agent does}

## Capabilities

- {Capability 1}
- {Capability 2}
- {Capability 3}

## Message Types

### Input Messages

- `action1`: {Description}
- `action2`: {Description}

### Output Messages

- `result`: {Description}
- `error`: {Description}

## Configuration

```python
{AgentName}Config(
    max_concurrent_tasks=5,
    timeout_seconds=30.0
)
```

## Usage

```python
from agents.{agent_name}.{agent_name}_agent import {AgentName}Agent

agent = {AgentName}Agent()
await agent.initialize()

response = await agent.process(AgentMessage(
    type="action1",
    data={...}
))

await agent.shutdown()
```

## Testing

```bash
pytest tests/agents/{agent_name}/
```

## Monitoring

- Metric: `{agent_name}_messages_processed`
- Metric: `{agent_name}_processing_time_seconds`
- Metric: `{agent_name}_error_rate`
```

---

Follow project conventions: #file:.github/copilot-instructions.md

Ensure all files are properly typed, tested, and documented.

### Optional: TypeScript Version

For TypeScript implementation, see TypeScript-specific prompt file.
