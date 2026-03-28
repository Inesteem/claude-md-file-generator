---
name: Forbidden Zones
type: template
tags: [safety, boundaries]
order: 9
description: Project-specific files and directories the agent must not modify (agent-filled, asks user)
---
<Fill Forbidden Zones>
Identify files and directories the agent should never modify directly:
- Generated files (and the command that regenerates them)
- Lock files (and the correct command to update them)
- Vendored or third-party code checked into the repo
- Files owned by another team or requiring a special review process
- Configuration files that must only be changed through a specific process

Verify: check for common generated file markers (auto-generated headers,
.gitattributes linguist-generated, codegen config files).

Ask the user:
- Are there any files or directories owned by another team?
- Are there config files that require a special process to change (e.g. infra-as-code)?
- Are there generated files that should never be hand-edited?
</Fill Forbidden Zones>
