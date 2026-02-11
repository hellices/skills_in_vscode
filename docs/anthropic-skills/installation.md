# Installing Anthropic Skills in VS Code

This guide walks you through installing and configuring Anthropic Claude skills in Visual Studio Code using the Copilot CLI.

## Prerequisites

Before you begin, ensure you have:

- Visual Studio Code (version 1.80 or later)
- GitHub Copilot subscription
- Node.js (version 18 or later)
- Git installed and configured
- An Anthropic API key (if using Claude directly)

## Installation Steps

### 1. Install GitHub Copilot CLI

The GitHub Copilot CLI provides command-line tools for managing Copilot features.

```bash
# Install globally using npm
npm install -g @github/copilot-cli

# Verify installation
gh copilot --version
```

**Alternative: Using GitHub CLI**

If you have GitHub CLI installed:

```bash
# Install gh CLI if not already installed
# macOS
brew install gh

# Windows (using winget)
winget install GitHub.cli

# Authenticate with GitHub
gh auth login

# Install Copilot CLI extension
gh extension install github/gh-copilot
```

### 2. Configure Copilot CLI for VS Code

Set VS Code as your default editor:

```bash
# Set editor preference
gh copilot config set editor vscode

# Verify configuration
gh copilot config get editor
```

### 3. Install Anthropic Skills Extension

**Note**: As of early 2024, native Anthropic skills integration is evolving. Current approaches include:

#### Option A: Using Anthropic's Continue Extension

Continue is a popular VS Code extension that integrates Claude and other LLMs:

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "Continue"
4. Click Install
5. Configure with your Anthropic API key

```json
// settings.json configuration
{
  "continue.apiKey": "${ANTHROPIC_API_KEY}",
  "continue.model": "claude-3-sonnet-20240229",
  "continue.provider": "anthropic"
}
```

#### Option B: Using Claude Dev Extension

1. Open VS Code Extensions
2. Search for "Claude Dev" or "Anthropic Claude"
3. Install the extension
4. Configure API credentials

### 4. Configure Anthropic API Key

Store your API key securely:

**Using Environment Variables (Recommended)**

```bash
# Linux/macOS - Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="your-api-key-here"

# Windows PowerShell - Add to profile
$env:ANTHROPIC_API_KEY = "your-api-key-here"

# Or use VS Code settings
code ~/.config/Code/User/settings.json
```

**VS Code Settings Configuration**

```json
{
  "anthropic.apiKey": "${env:ANTHROPIC_API_KEY}",
  "anthropic.model": "claude-3-sonnet-20240229",
  "anthropic.maxTokens": 4096,
  "anthropic.temperature": 0.7
}
```

### 5. Install Required VS Code Extensions

For the best experience, install these complementary extensions:

```bash
# Using code command
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension Continue.continue

# Or search in VS Code Extensions marketplace:
# - GitHub Copilot
# - GitHub Copilot Chat
# - Continue (for Claude integration)
```

## Verification

### Test GitHub Copilot

1. Open a code file in VS Code
2. Start typing a function
3. Verify Copilot suggestions appear
4. Use Copilot Chat (Ctrl+I / Cmd+I)

### Test Anthropic Integration

1. Open Continue sidebar (if using Continue extension)
2. Ask a question: "Explain this code"
3. Verify Claude responds
4. Try code generation

## Configuration Options

### Copilot Settings

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": true,
    "plaintext": false,
    "markdown": true
  },
  "github.copilot.advanced": {
    "debug.overrideEngine": "claude-3-sonnet",
    "debug.testOverrideProxyUrl": "http://localhost:3000"
  }
}
```

### Continue Extension Settings

```json
{
  "continue.telemetryEnabled": false,
  "continue.enableTabAutocomplete": true,
  "continue.models": [
    {
      "title": "Claude 3 Sonnet",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "apiKey": "${ANTHROPIC_API_KEY}"
    },
    {
      "title": "Claude 3 Opus",
      "provider": "anthropic",
      "model": "claude-3-opus-20240229",
      "apiKey": "${ANTHROPIC_API_KEY}"
    }
  ]
}
```

### Skills Configuration

Create a skills configuration file:

**`.vscode/skills.json`**

```json
{
  "skills": [
    {
      "name": "code-review",
      "description": "Review code for best practices and issues",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "prompts": {
        "system": "You are a code reviewer. Focus on: security, performance, readability, and best practices."
      }
    },
    {
      "name": "test-generation",
      "description": "Generate unit tests for code",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "prompts": {
        "system": "Generate comprehensive unit tests using the project's testing framework."
      }
    },
    {
      "name": "documentation",
      "description": "Generate documentation for code",
      "provider": "anthropic",
      "model": "claude-3-sonnet-20240229",
      "prompts": {
        "system": "Generate clear, concise documentation with examples."
      }
    }
  ]
}
```

## Using Copilot CLI Commands

### Common Commands

```bash
# Explain code or command
gh copilot explain "git rebase -i HEAD~3"

# Suggest a command
gh copilot suggest "list all files modified in the last 7 days"

# Get help with error messages
gh copilot fix "npm ERR! code ENOENT"

# Interactive chat
gh copilot chat
```

### Skills-Specific Commands

```bash
# Run a specific skill
gh copilot skill run code-review --file src/app.ts

# List available skills
gh copilot skill list

# Create a new skill
gh copilot skill create --name custom-skill
```

## Keyboard Shortcuts

Configure useful shortcuts in VS Code:

**`keybindings.json`**

```json
[
  {
    "key": "ctrl+shift+a",
    "command": "github.copilot.chat.open",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+e",
    "command": "github.copilot.explain",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+t",
    "command": "continue.continueGUIView.focus",
    "when": "editorTextFocus"
  }
]
```

## Troubleshooting

### Copilot Not Working

```bash
# Check Copilot status
gh copilot status

# Re-authenticate
gh auth refresh

# Check VS Code extension
code --list-extensions | grep copilot
```

### Anthropic API Issues

```bash
# Test API key
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

### Extension Conflicts

If you have multiple AI coding assistants:

1. Disable conflicting extensions temporarily
2. Configure priorities in settings
3. Use specific keyboard shortcuts for each

### Common Issues

**Issue: API Key Not Found**
```bash
# Solution: Verify environment variable
echo $ANTHROPIC_API_KEY

# Reload VS Code
code --reload
```

**Issue: Extension Not Activating**
```bash
# Solution: Check extension logs
# View > Output > Select extension from dropdown
```

**Issue: Rate Limiting**
```json
{
  "anthropic.rateLimiting": {
    "requestsPerMinute": 50,
    "retryAfter": 60
  }
}
```

## Next Steps

1. [Configure Anthropic Skills](./configuration.md)
2. [Create Custom Skills](./creating-skills.md)
3. [Migrate from Custom Instructions](../migration/migration-strategy.md)

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Continue Extension Docs](https://continue.dev/docs)
- [VS Code Extension API](https://code.visualstudio.com/api)

## Getting Help

- GitHub Copilot: [Support](https://support.github.com/)
- Anthropic: [Community Discord](https://anthropic.com/discord)
- VS Code: [Community Forum](https://github.com/microsoft/vscode/discussions)
