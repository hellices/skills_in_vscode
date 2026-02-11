# Anthropic Skills Examples

This directory contains example Anthropic skill definitions that can be imported into your VS Code workspace.

## Available Skills

### 1. Code Reviewer (`code-reviewer.json`)
Comprehensive code review skill for multiple languages

### 2. Test Generator (`test-generator.json`)
Generates tests following project conventions

### 3. Documentation Generator (`documentation-generator.json`)
Creates comprehensive documentation

### 4. Security Scanner (`security-scanner.json`)
Scans for security vulnerabilities

### 5. Refactoring Assistant (`refactoring-assistant.json`)
Suggests code improvements and refactoring

## Usage

### Import a Single Skill

Copy the skill definition to your `.vscode/skills.json`:

```bash
# Copy code reviewer skill
cat skills/anthropic/code-reviewer.json >> .vscode/skills.json
```

### Import All Skills

```bash
# Merge all skills into your configuration
cat skills/anthropic/*.json > .vscode/skills.json
```

### Custom Configuration

Edit the skill files to match your project:
- Adjust `systemPrompt` for your conventions
- Change `model` based on needs
- Update `filePatterns` for your file types
- Modify `temperature` and `maxTokens` for different behavior

## Skill Descriptions

See individual JSON files for detailed configurations and usage instructions.
