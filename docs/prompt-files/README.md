# Prompt Files Guide

Prompt files allow you to create reusable prompt templates that can be invoked with slash commands in GitHub Copilot Chat.

## What are Prompt Files?

Prompt files (`.prompt.md`) are reusable templates that:
- Standardize common workflows
- Reduce repetitive prompting
- Share best practices across teams
- Can be invoked with `/prompt-name` in Copilot Chat

## Quick Example

**File**: `.github/prompts/review.prompt.md`
```markdown
---
name: review
description: Code review with security focus
---

Review this code for:
- Security vulnerabilities
- Performance issues
- Best practices

${selectedText}
```

**Usage**: Select code → Copilot Chat → `/review`

## File Structure

```markdown
---
name: command-name
description: What this prompt does
argument-hint: (Optional) Expected input
---

Your prompt template with:
- ${selectedText} for current selection
- ${file} for file path
- #file:path to reference files
```

## Complete Guide

For detailed documentation, examples, and best practices, see:
- [Full Prompt Files Documentation](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Example Prompts](../../examples/prompts/)

## Resources

- [Overview](../overview.md)
- [Custom Instructions](../custom-instructions/README.md)
- [VS Code Documentation](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
