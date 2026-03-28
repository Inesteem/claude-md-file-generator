---
name: Testing Patterns
type: static
tags: [testing, patterns]
order: 16
description: Advanced testing patterns beyond basic TDD
---
## Testing Patterns

- Split tests by dependency: keep unit tests free of I/O, network, and filesystem; isolate those into integration tests
- Use pytest fixtures to share setup and teardown; prefer function-scoped fixtures unless state is truly shareable
- Use `@pytest.mark.parametrize` for data-driven cases instead of loops inside tests
- Handle optional dependencies with skip decorators (`@pytest.mark.skipif`) rather than silent no-ops
- Label tests clearly so CI can run unit tests fast and integration tests separately
- Be aware of CI environment differences (temp dirs, available ports, env vars) and guard against them explicitly
