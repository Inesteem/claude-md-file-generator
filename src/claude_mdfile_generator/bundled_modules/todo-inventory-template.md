---
name: TODO Inventory
type: template
tags: [workflow, todos]
order: 37
description: Current TODOs, FIXMEs, and technical debt in the codebase (agent-filled)
---
<Fill TODO Inventory>
Scan the codebase for TODO, FIXME, HACK, WORKAROUND, and XXX comments and document:
- Total count by category (TODO, FIXME, HACK, etc.)
- The most critical items (FIXMEs and HACKs) with file, line, and context
- Any patterns (e.g. "most TODOs are in the migration layer")
- Whether TODOs reference tickets/issues or are orphaned

Verify: run a grep for TODO/FIXME/HACK/XXX across the codebase.

Ask the user:
- Are any of these TODOs no longer relevant and should be cleaned up?
- Are there known technical debt items not captured by code comments?
</Fill TODO Inventory>
