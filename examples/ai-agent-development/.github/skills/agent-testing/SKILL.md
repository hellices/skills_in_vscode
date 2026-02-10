---
name: Test Agents
description: Comprehensive testing strategy for Microsoft Agent Framework agents
---

# Agent Testing Skill

Complete guide for testing agents in Microsoft Agent Framework.

## When to Use

- Creating new agents
- Modifying existing agents
- Testing agent interactions
- Validating communication patterns
- Performance testing

## Testing Layers

### 1. Unit Tests

Test individual agent methods in isolation.

```typescript
// src/agents/example/example.agent.test.ts

import { ExampleAgent } from './example.agent';
import { createMockMessage, createMockLogger } from '../../test-utils';

describe('ExampleAgent', () => {
  let agent: ExampleAgent;
  let mockLogger: jest.Mocked<Logger>;

  beforeEach(async () => {
    mockLogger = createMockLogger();
    agent = new ExampleAgent({ logger: mockLogger });
    await agent.initialize();
  });

  afterEach(async () => {
    await agent.shutdown();
  });

  describe('message processing', () => {
    it('should process valid messages', async () => {
      const message = createMockMessage({
        type: 'test_action',
        data: { value: 42 }
      });

      const response = await agent.process(message);

      expect(response.success).toBe(true);
      expect(response.data).toHaveProperty('result');
    });

    it('should validate message schema', async () => {
      const invalidMessage = createMockMessage({
        type: 'invalid_type',
        data: {}
      });

      const response = await agent.process(invalidMessage);

      expect(response.success).toBe(false);
      expect(response.error).toContain('Invalid message type');
    });

    it('should handle processing errors gracefully', async () => {
      const message = createMockMessage({
        type: 'error_prone_action',
        data: { causeError: true }
      });

      const response = await agent.process(message);

      expect(response.success).toBe(false);
      expect(response.error).toBeDefined();
      expect(mockLogger.error).toHaveBeenCalled();
    });
  });

  describe('initialization', () => {
    it('should initialize resources', async () => {
      const newAgent = new ExampleAgent({});
      await newAgent.initialize();

      expect(newAgent.isInitialized()).toBe(true);
    });

    it('should fail processing before initialization', async () => {
      const uninitializedAgent = new ExampleAgent({});
      const message = createMockMessage({ type: 'test_action' });

      await expect(uninitializedAgent.process(message))
        .rejects
        .toThrow('Agent not initialized');
    });
  });

  describe('shutdown', () => {
    it('should clean up resources', async () => {
      await agent.shutdown();

      expect(agent.isInitialized()).toBe(false);
    });
  });
});
```

### 2. Integration Tests

Test agent-to-agent communication.

```typescript
// tests/integration/agent-communication.test.ts

import { AgentSystem } from '@microsoft/agent-framework';
import { RedTeamAgent } from '../../src/agents/red-team/red-team.agent';
import { BlueTeamAgent } from '../../src/agents/blue-team/blue-team.agent';

describe('Red-Blue Team Communication', () => {
  let system: AgentSystem;
  let redTeam: RedTeamAgent;
  let blueTeam: BlueTeamAgent;

  beforeAll(async () => {
    system = new AgentSystem({
      messageTimeout: 30000,
      maxRetries: 3
    });

    redTeam = new RedTeamAgent({});
    blueTeam = new BlueTeamAgent({});

    await system.register(redTeam);
    await system.register(blueTeam);
    await system.start();
  });

  afterAll(async () => {
    await system.stop();
  });

  it('should detect and remediate vulnerabilities', async () => {
    // Red team finds vulnerability
    const vulnReport = await system.send({
      to: redTeam.id,
      action: 'analyze_code',
      data: {
        code: 'const query = `SELECT * FROM users WHERE id = ${userId}`;'
      }
    });

    expect(vulnReport.vulnerabilities).toHaveLength(1);
    expect(vulnReport.vulnerabilities[0].type).toBe('SQL_INJECTION');

    // Blue team receives and remediates
    const remediation = await system.send({
      to: blueTeam.id,
      action: 'remediate',
      data: { vulnerabilityId: vulnReport.vulnerabilities[0].id }
    });

    expect(remediation.status).toBe('FIXED');

    // Red team validates fix
    const validation = await system.send({
      to: redTeam.id,
      action: 'verify_fix',
      data: {
        vulnerabilityId: vulnReport.vulnerabilities[0].id,
        fixedCode: remediation.fix.code
      }
    });

    expect(validation.verified).toBe(true);
  });

  it('should handle communication timeouts', async () => {
    const slowAgent = new SlowRespondingAgent({});
    await system.register(slowAgent);

    await expect(
      system.send({
        to: slowAgent.id,
        action: 'slow_action',
        timeout: 1000
      })
    ).rejects.toThrow('Timeout');
  });

  it('should broadcast events to multiple agents', async () => {
    const messages: any[] = [];
    
    // Subscribe both agents to security events
    const unsubscribe1 = system.subscribe('security_alert', (msg) => {
      messages.push({ agent: 'red-team', message: msg });
    });
    
    const unsubscribe2 = system.subscribe('security_alert', (msg) => {
      messages.push({ agent: 'blue-team', message: msg });
    });

    // Broadcast security alert
    await system.broadcast({
      type: 'security_alert',
      data: { severity: 'HIGH', description: 'Suspicious activity detected' }
    });

    await waitFor(() => messages.length >= 2);

    expect(messages).toHaveLength(2);
    expect(messages[0].message.type).toBe('security_alert');

    unsubscribe1();
    unsubscribe2();
  });
});
```

### 3. End-to-End Tests

Test complete workflows.

```typescript
// tests/e2e/security-workflow.test.ts

describe('Security Workflow E2E', () => {
  let system: AgentSystem;

  beforeAll(async () => {
    system = await setupCompleteSystem();
  });

  afterAll(async () => {
    await system.teardown();
  });

  it('should complete full security scan and remediation', async () => {
    // 1. Submit code for review
    const submission = await system.submitCodeReview({
      repository: 'test-repo',
      pullRequest: 123,
      files: ['src/api/users.ts']
    });

    expect(submission.status).toBe('ACCEPTED');

    // 2. Wait for red team analysis
    const analysis = await system.waitForEvent({
      type: 'analysis_complete',
      source: 'red-team',
      timeout: 60000
    });

    expect(analysis.vulnerabilities).toBeDefined();

    // 3. Blue team auto-remediates if possible
    if (analysis.autoFixable) {
      const fix = await system.waitForEvent({
        type: 'auto_fix_applied',
        source: 'blue-team',
        timeout: 60000
      });

      expect(fix.status).toBe('SUCCESS');
    }

    // 4. Verify final status
    const finalStatus = await system.getWorkflowStatus(submission.workflowId);

    expect(finalStatus.completed).toBe(true);
    expect(finalStatus.result).toBe('PASS');
  });
});
```

### 4. Performance Tests

Test agent scalability and performance.

```typescript
// tests/performance/agent-load.test.ts

describe('Agent Performance', () => {
  it('should handle high message volume', async () => {
    const system = await setupTestSystem();
    const agent = new TestAgent({});
    await system.register(agent);

    const messageCount = 1000;
    const startTime = Date.now();

    // Send many messages concurrently
    const promises = Array.from({ length: messageCount }, (_, i) =>
      system.send({
        to: agent.id,
        action: 'process',
        data: { index: i }
      })
    );

    const results = await Promise.all(promises);
    const endTime = Date.now();

    const successCount = results.filter(r => r.success).length;
    const avgLatency = (endTime - startTime) / messageCount;

    expect(successCount).toBe(messageCount);
    expect(avgLatency).toBeLessThan(100); // < 100ms per message
  });

  it('should not leak memory', async () => {
    const system = await setupTestSystem();
    const agent = new TestAgent({});
    await system.register(agent);

    const initialMemory = process.memoryUsage().heapUsed;

    // Process many messages
    for (let i = 0; i < 10000; i++) {
      await system.send({
        to: agent.id,
        action: 'process',
        data: { index: i }
      });
    }

    // Force garbage collection
    if (global.gc) global.gc();

    const finalMemory = process.memoryUsage().heapUsed;
    const memoryIncrease = (finalMemory - initialMemory) / 1024 / 1024; // MB

    expect(memoryIncrease).toBeLessThan(50); // < 50MB increase
  });
});
```

## Test Utilities

### Mock Message Builder

```typescript
// src/test-utils/mock-message.ts

export function createMockMessage(
  content: Partial<AgentMessage['content']>
): AgentMessage {
  return {
    id: generateUUID(),
    timestamp: new Date(),
    sender: 'test-sender',
    recipient: 'test-recipient',
    content: {
      type: 'test_message',
      ...content
    },
    metadata: {}
  };
}
```

### Agent System Setup

```typescript
// src/test-utils/test-system.ts

export async function setupTestAgentSystem(): Promise<AgentSystem> {
  const system = new AgentSystem({
    messageTimeout: 5000,
    maxRetries: 1,
    logger: createTestLogger()
  });

  // Register test agents
  await system.register(new TestCoordinatorAgent());
  await system.start();

  return system;
}

export async function setupCompleteSystem(): Promise<AgentSystem> {
  const system = new AgentSystem();

  // Register all production agents
  await system.register(new CoordinatorAgent());
  await system.register(new RedTeamAgent());
  await system.register(new BlueTeamAgent());
  await system.start();

  return system;
}
```

### Wait Utilities

```typescript
// src/test-utils/wait-utils.ts

export async function waitFor(
  condition: () => boolean,
  timeout: number = 5000
): Promise<void> {
  const startTime = Date.now();
  
  while (!condition()) {
    if (Date.now() - startTime > timeout) {
      throw new Error('Timeout waiting for condition');
    }
    await sleep(100);
  }
}

export async function waitForMessage(
  system: AgentSystem,
  predicate: (msg: AgentMessage) => boolean,
  timeout: number = 5000
): Promise<AgentMessage> {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      unsubscribe();
      reject(new Error('Timeout waiting for message'));
    }, timeout);

    const unsubscribe = system.subscribeAll((msg) => {
      if (predicate(msg)) {
        clearTimeout(timer);
        unsubscribe();
        resolve(msg);
      }
    });
  });
}
```

## Best Practices

### Test Organization
```
tests/
├── unit/
│   ├── agents/
│   │   ├── red-team/
│   │   └── blue-team/
│   └── common/
├── integration/
│   ├── agent-communication/
│   └── message-flows/
├── e2e/
│   └── workflows/
└── performance/
    └── load-tests/
```

### Test Coverage Requirements
- Unit tests: >80% code coverage
- Integration tests: All agent interactions
- E2E tests: Critical workflows
- Performance tests: Key scenarios

### Test Data Management
```typescript
// Use factories for test data
export const AgentMessageFactory = {
  build: (overrides = {}) => ({
    id: faker.string.uuid(),
    timestamp: faker.date.recent(),
    sender: faker.string.alpha(10),
    recipient: faker.string.alpha(10),
    content: {},
    ...overrides
  })
};
```

## Continuous Testing

### Pre-commit Hooks
```json
{
  "scripts": {
    "test": "jest",
    "test:unit": "jest --testPathPattern=unit",
    "test:integration": "jest --testPathPattern=integration",
    "test:e2e": "jest --testPathPattern=e2e",
    "test:coverage": "jest --coverage"
  },
  "husky": {
    "hooks": {
      "pre-commit": "npm run test:unit",
      "pre-push": "npm run test:integration"
    }
  }
}
```

### CI/CD Integration
```yaml
# .github/workflows/test.yml
name: Test Agents

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm install
      - run: npm run test:unit
      - run: npm run test:integration
      - run: npm run test:coverage
```

## Debugging Tests

### Enable Debug Logging
```typescript
process.env.LOG_LEVEL = 'debug';
process.env.AGENT_DEBUG = 'true';
```

### Inspect Messages
```typescript
system.on('message', (msg) => {
  console.log('Message:', JSON.stringify(msg, null, 2));
});
```

### Breakpoint Testing
```typescript
it.only('debug this test', async () => {
  debugger; // Set breakpoint here
  const result = await agent.process(message);
  expect(result).toBeDefined();
});
```

## Resources

- Testing framework: Jest or Vitest
- Mocking: jest.mock() or Vitest mocks
- Test patterns: #file:.github/copilot-instructions.md
- CI/CD: GitHub Actions
