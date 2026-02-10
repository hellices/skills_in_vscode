---
name: component
description: Generate React/Vue component with boilerplate
argument-hint: Component name and description
---

Create a component for:

${selectedText}

Include:

1. **TypeScript Interface** for props
```typescript
interface ComponentProps {
  // prop definitions
}
```

2. **Component Implementation**
- Functional component with hooks
- PropTypes or Zod validation
- Proper TypeScript types

3. **Styling**
- CSS module or styled-components
- Responsive design considerations

4. **Documentation**
- JSDoc with usage example
- Props documentation

5. **Test File**
- Basic render test
- Props validation test
- User interaction tests

Follow project conventions: #file:.github/copilot-instructions.md
