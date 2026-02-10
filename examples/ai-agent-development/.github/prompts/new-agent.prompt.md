---
name: new-agent
description: Create a new agent with Microsoft Agent Framework boilerplate
argument-hint: Agent name and purpose
---

# Create New Agent

Generate a complete agent implementation with all required boilerplate.

## Agent Specification

${selectedText}

## Generate

Create the following files:

### 1. Agent Implementation

```typescript
// src/agents/{agent-name}/{agent-name}.agent.ts

import { Agent, AgentMessage, AgentResponse } from '@microsoft/agent-framework';
import { Logger } from '../common/logger';
import { z } from 'zod';

/**
 * {AgentName} Agent
 * 
 * Purpose: {Brief description}
 * 
 * Capabilities:
 * - {Capability 1}
 * - {Capability 2}
 */
export class {AgentName}Agent implements Agent {
  public readonly id: string;
  public readonly name: string;
  public readonly capabilities: string[];
  
  private logger: Logger;
  private isInitialized: boolean = false;

  constructor(config: {AgentName}Config) {
    this.id = config.id || generateAgentId();
    this.name = '{agent-name}';
    this.capabilities = ['{capability1}', '{capability2}'];
    this.logger = new Logger({ agent: this.name });
  }

  async initialize(): Promise<void> {
    this.logger.info('Initializing agent');
    
    // Initialize resources
    // Connect to services
    // Load configuration
    
    this.isInitialized = true;
    this.logger.info('Agent initialized successfully');
  }

  async process(message: AgentMessage): Promise<AgentResponse> {
    if (!this.isInitialized) {
      throw new Error('Agent not initialized');
    }

    this.logger.debug('Processing message', { messageId: message.id });

    try {
      // Validate message
      const validated = this.validateMessage(message);
      
      // Process based on message type
      const result = await this.handleMessage(validated);
      
      return {
        success: true,
        data: result,
        agentId: this.id,
        processingTime: Date.now() - message.timestamp.getTime()
      };
    } catch (error) {
      this.logger.error('Error processing message', { error, messageId: message.id });
      return this.handleError(error);
    }
  }

  async shutdown(): Promise<void> {
    this.logger.info('Shutting down agent');
    
    // Clean up resources
    // Close connections
    
    this.isInitialized = false;
  }

  private validateMessage(message: AgentMessage): ValidatedMessage {
    const schema = z.object({
      type: z.enum(['action1', 'action2']),
      data: z.unknown()
    });

    return schema.parse(message.content);
  }

  private async handleMessage(message: ValidatedMessage): Promise<unknown> {
    switch (message.type) {
      case 'action1':
        return this.handleAction1(message.data);
      case 'action2':
        return this.handleAction2(message.data);
      default:
        throw new Error(`Unknown message type: ${message.type}`);
    }
  }

  private async handleAction1(data: unknown): Promise<unknown> {
    // Implement action 1
    return { result: 'action1_completed' };
  }

  private async handleAction2(data: unknown): Promise<unknown> {
    // Implement action 2
    return { result: 'action2_completed' };
  }

  private handleError(error: unknown): AgentResponse {
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
      agentId: this.id
    };
  }
}
```

### 2. Agent Configuration

```typescript
// src/agents/{agent-name}/{agent-name}.config.ts

export interface {AgentName}Config {
  id?: string;
  // Add agent-specific configuration
  maxConcurrentTasks?: number;
  timeoutMs?: number;
}

export const default{AgentName}Config: {AgentName}Config = {
  maxConcurrentTasks: 5,
  timeoutMs: 30000
};
```

### 3. Unit Tests

```typescript
// src/agents/{agent-name}/{agent-name}.test.ts

import { {AgentName}Agent } from './{agent-name}.agent';
import { createMockMessage } from '../../common/test-utils';

describe('{AgentName}Agent', () => {
  let agent: {AgentName}Agent;

  beforeEach(async () => {
    agent = new {AgentName}Agent({});
    await agent.initialize();
  });

  afterEach(async () => {
    await agent.shutdown();
  });

  describe('initialization', () => {
    it('should initialize successfully', async () => {
      const newAgent = new {AgentName}Agent({});
      await expect(newAgent.initialize()).resolves.not.toThrow();
    });
  });

  describe('message processing', () => {
    it('should process action1 messages', async () => {
      const message = createMockMessage({
        type: 'action1',
        data: { test: true }
      });

      const response = await agent.process(message);

      expect(response.success).toBe(true);
      expect(response.data).toHaveProperty('result');
    });

    it('should handle errors gracefully', async () => {
      const message = createMockMessage({
        type: 'invalid',
        data: {}
      });

      const response = await agent.process(message);

      expect(response.success).toBe(false);
      expect(response.error).toBeDefined();
    });
  });
});
```

### 4. Integration Test

```typescript
// tests/integration/{agent-name}.integration.test.ts

import { AgentSystem } from '@microsoft/agent-framework';
import { {AgentName}Agent } from '../../src/agents/{agent-name}/{agent-name}.agent';

describe('{AgentName}Agent Integration', () => {
  let system: AgentSystem;
  let agent: {AgentName}Agent;

  beforeAll(async () => {
    system = new AgentSystem();
    agent = new {AgentName}Agent({});
    await system.register(agent);
    await system.start();
  });

  afterAll(async () => {
    await system.stop();
  });

  it('should communicate with other agents', async () => {
    const message = {
      to: agent.id,
      action: 'action1',
      data: { test: true }
    };

    const response = await system.send(message);

    expect(response.success).toBe(true);
  });
});
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

```typescript
{
  maxConcurrentTasks: 5,
  timeoutMs: 30000
}
```

## Usage

```typescript
const agent = new {AgentName}Agent({
  id: 'custom-id',
  maxConcurrentTasks: 10
});

await agent.initialize();

const response = await agent.process({
  type: 'action1',
  data: { ... }
});
```

## Testing

```bash
npm test -- {agent-name}
```

## Monitoring

- Metric: `{agent_name}_messages_processed`
- Metric: `{agent_name}_processing_time_ms`
- Metric: `{agent_name}_error_rate`
```

---

Follow project conventions: #file:.github/copilot-instructions.md

Ensure all files are properly typed, tested, and documented.
