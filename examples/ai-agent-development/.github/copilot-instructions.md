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

### TypeScript Standards

**Type Safety**
- Use strict TypeScript mode
- Define interfaces for all agent messages
- Use branded types for IDs and sensitive data
- Avoid `any` - use `unknown` for truly unknown types

**Async Patterns**
- Use async/await consistently
- Handle promise rejections with proper error boundaries
- Implement timeouts for all external calls
- Use cancellation tokens for long-running operations

**Example Agent Interface**
```typescript
interface Agent {
  id: string;
  name: string;
  capabilities: string[];
  process(message: AgentMessage): Promise<AgentResponse>;
  initialize(): Promise<void>;
  shutdown(): Promise<void>;
}

interface AgentMessage {
  id: string;
  timestamp: Date;
  sender: string;
  recipient: string;
  content: unknown;
  metadata?: Record<string, unknown>;
}
```

### Microsoft Agent Framework Patterns

**Agent Registration**
```typescript
// Register agents with framework
const agentSystem = new AgentSystem({
  messageTimeout: 30000,
  maxRetries: 3
});

await agentSystem.register(new CoordinatorAgent());
await agentSystem.register(new RedTeamAgent());
await agentSystem.register(new BlueTeamAgent());
```

**Message Handling**
```typescript
class BaseAgent implements Agent {
  async process(message: AgentMessage): Promise<AgentResponse> {
    try {
      // Validate message
      const validated = this.validateMessage(message);
      
      // Process based on message type
      const result = await this.handleMessage(validated);
      
      // Return response
      return {
        success: true,
        data: result,
        processingTime: Date.now() - message.timestamp.getTime()
      };
    } catch (error) {
      return this.handleError(error);
    }
  }
}
```

### Linting and Code Quality

**ESLint Configuration**
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking"
  ],
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-floating-promises": "error",
    "no-console": ["error", { "allow": ["warn", "error"] }],
    "max-lines-per-function": ["warn", 50]
  }
}
```

**Required Checks**
- All agents must have unit tests (>80% coverage)
- Integration tests for agent communication
- Type checking with `tsc --noEmit`
- Linting with no errors
- Security scan with npm audit

### Testing Requirements

**Unit Tests**
```typescript
describe('RedTeamAgent', () => {
  let agent: RedTeamAgent;
  let mockMessageBus: jest.Mocked<MessageBus>;

  beforeEach(() => {
    mockMessageBus = createMockMessageBus();
    agent = new RedTeamAgent(mockMessageBus);
  });

  it('should identify security vulnerabilities', async () => {
    const message = createTestMessage({
      type: 'analyze_code',
      code: 'const password = "hardcoded123";'
    });

    const response = await agent.process(message);

    expect(response.success).toBe(true);
    expect(response.vulnerabilities).toContainEqual(
      expect.objectContaining({
        type: 'hardcoded_secret',
        severity: 'HIGH'
      })
    );
  });
});
```

**Integration Tests**
```typescript
describe('Agent Communication', () => {
  it('should coordinate between red and blue teams', async () => {
    const system = await setupTestAgentSystem();
    
    // Red team finds vulnerability
    const attack = await system.send({
      to: 'red-team',
      action: 'find_vulnerabilities',
      target: testCode
    });

    // Blue team should receive alert and respond
    const defense = await system.waitForMessage({
      from: 'blue-team',
      inResponseTo: attack.id
    });

    expect(defense.action).toBe('patch_applied');
  });
});
```

### Security Guidelines

**Sensitive Data**
- Never log agent messages containing user data
- Sanitize all outputs before logging
- Use encryption for agent-to-agent communication
- Implement authentication between agents

**Input Validation**
```typescript
class MessageValidator {
  validate(message: unknown): AgentMessage {
    const schema = z.object({
      id: z.string().uuid(),
      timestamp: z.date(),
      sender: z.string().min(1),
      recipient: z.string().min(1),
      content: z.unknown()
    });

    return schema.parse(message);
  }
}
```

### Error Handling

**Graceful Degradation**
- Agents should handle partial failures
- Implement circuit breakers for unreliable agents
- Provide meaningful error messages
- Log errors with context for debugging

**Retry Logic**
```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  delay: number = 1000
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await sleep(delay * Math.pow(2, i));
    }
  }
  throw new Error('Retry exhausted');
}
```

### Performance Considerations

**Message Processing**
- Process messages asynchronously
- Implement message queuing for high load
- Use batching for bulk operations
- Monitor agent response times

**Resource Management**
- Limit concurrent agent instances
- Implement memory limits per agent
- Clean up resources on shutdown
- Monitor CPU and memory usage

### Documentation Requirements

**Agent Documentation**
```typescript
/**
 * Red Team Agent - Security Testing
 * 
 * Responsibilities:
 * - Identify security vulnerabilities in code
 * - Simulate attack scenarios
 * - Generate security reports
 * 
 * Communication:
 * - Receives: code_analysis_request, security_scan_request
 * - Sends: vulnerability_report, attack_scenario
 * 
 * @example
 * const agent = new RedTeamAgent();
 * const result = await agent.process({
 *   type: 'security_scan',
 *   target: sourceCode
 * });
 */
```

### Observability

**Logging**
```typescript
import { Logger } from '@microsoft/agent-framework';

const logger = new Logger({
  agent: 'red-team',
  level: 'info'
});

logger.info('Processing message', {
  messageId: message.id,
  sender: message.sender
});
```

**Metrics**
- Track message processing time
- Monitor agent success/failure rates
- Measure inter-agent communication latency
- Alert on error rate thresholds
