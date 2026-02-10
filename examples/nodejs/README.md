# Node.js Example Project

Example Node.js/TypeScript project with GitHub Copilot custom instructions and Anthropic skills.

## Setup

```bash
npm install
```

## Structure

```
nodejs-example/
├── src/
│   ├── models/
│   │   └── User.ts
│   └── services/
│       └── UserService.ts
├── .vscode/
│   ├── settings.json
│   └── skills.json
└── package.json
```

## Using Custom Instructions

Custom instructions are in `.github/copilot/javascript-instructions.md` and apply automatically.

## Available Skills

- **TypeScript Code Reviewer**: Review TypeScript code
- **Test Generator**: Generate Jest/Vitest tests
- **Documentation Generator**: Generate TSDoc comments

## Resources

- [Node.js Custom Instructions](../../docs/custom-instructions/nodejs.md)
- [Anthropic Skills](../../docs/anthropic-skills/)
