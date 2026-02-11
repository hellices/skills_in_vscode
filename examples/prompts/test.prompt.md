---
name: test
description: Generate comprehensive test suite
argument-hint: Test framework (auto-detected if not specified)
---

Generate a comprehensive test suite for:

${selectedText}

Requirements:
1. **Test Structure**: Use describe/it blocks (or language equivalent)
2. **Coverage**: Include happy path, edge cases, and error conditions
3. **Naming**: Descriptive test names (test_method_scenario_expected)
4. **Mocking**: Mock external dependencies appropriately
5. **Assertions**: Clear, specific assertions
6. **Setup/Teardown**: Proper test fixtures and cleanup

Current file: ${file}

Generate complete, runnable tests following project conventions from:
#file:.github/copilot-instructions.md
