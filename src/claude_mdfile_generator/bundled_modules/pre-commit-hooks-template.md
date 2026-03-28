---
name: Pre-commit Hooks
type: template
tags: [hooks, tooling, automation]
order: 27
description: Pre-commit hook configuration (agent-filled and verified)
---
<Fill Pre-commit Hooks>
Identify any pre-commit hooks configured in this project and document:
- Which framework is used (e.g. pre-commit, husky, lefthook, lint-staged)
- Where the config lives (e.g. .pre-commit-config.yaml, .husky/, package.json)
- What hooks run (lint, format, type check, test, commit message validation, etc.)
- The order hooks execute in
- How to install/activate the hooks locally
- How to bypass hooks when necessary (and when that is acceptable)

Verify: read the hook config and confirm the hooks are correctly configured.
If no pre-commit hooks are set up, state that explicitly.
</Fill Pre-commit Hooks>
