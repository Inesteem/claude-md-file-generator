---
name: Testing Configuration
type: template
tags: [testing, tooling]
order: 15
description: Project-specific test framework, structure, and coverage (agent-filled and verified)
---
<Fill Testing Configuration>
Identify the testing setup for this project and document:
- Test framework(s) and runner command (e.g. pytest, vitest, go test, cargo test)
- Test directory structure and file naming convention
- How to run the full suite, a single file, and a single test
- Coverage tool and minimum threshold (if configured)
- Test database or fixture/seed setup (if applicable)
- Mocking approach: what gets mocked, what libraries are used
- CI test command (if different from local)

Verify: run the test suite and confirm it passes. Note any failing tests
and whether they are known/accepted.

Ask the user:
- Is there a minimum coverage requirement?
- Are there tests that are known-flaky or intentionally skipped?
</Fill Testing Configuration>
