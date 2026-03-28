---
name: Type Checker Configuration
type: template
tags: [type-checking, tooling]
order: 23
description: Project-specific type checker setup and commands (agent-filled and verified)
---
<Fill Type Checker Configuration>
Identify the type checker used in this project and document:
- Which type checker is configured (e.g. pyright, mypy, tsc, flow)
- The exact command to run it
- Where the configuration lives (e.g. pyrightconfig.json, mypy.ini, tsconfig.json)
- Strictness level and any notable overrides
- Known type errors that are intentionally suppressed (and why)

Verify: run the type checker and confirm it works. Note any existing errors
and whether they are known/accepted or need fixing.
If no type checker is configured, state that explicitly.
</Fill Type Checker Configuration>
