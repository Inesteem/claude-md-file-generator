---
name: Testing
type: static
tags: [testing, tdd, patterns]
order: 15
description: Test-driven development guidelines and testing patterns
---
## Testing

- Write tests before implementation when adding new functionality; write a failing test before writing the fix for bugs
- Run the full test suite and linter before committing
- Test edge cases and error paths, not just happy paths; include at least one test for each error a function can raise
- Use specific assertions (`assert result == expected`) over vague truthiness checks (`assert result`); include a message when the failure would be ambiguous
- Use descriptive test names that state the scenario and expected outcome (e.g. `test_parse_returns_empty_list_when_input_is_blank`)
- Prefer real implementations over mocks; use mocks only for external services, time-dependent logic, or code with side effects you cannot undo
- Split tests by dependency: keep unit tests free of I/O, network, and filesystem; isolate those into integration tests
- Use the test framework's fixture/setup mechanism for shared state; prefer per-test setup unless state is truly shareable
- Use parameterized tests for data-driven cases instead of loops inside test functions
- Handle optional dependencies with skip decorators rather than silent no-ops
- Label tests so CI can run unit tests fast and integration tests on a separate schedule
- Guard against CI environment differences explicitly: use temporary directories from the framework, avoid assuming specific ports are available
- Never delete or weaken a failing test to make it pass; fix the code under test or, if the test is genuinely wrong, fix the test and explain why in a comment
