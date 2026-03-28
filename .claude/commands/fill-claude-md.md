---
description: Fill all <Fill ...> template sections in an existing CLAUDE.md by analyzing the project
argument-hint: [path to CLAUDE.md (default: ./CLAUDE.md)]
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Agent
---

Fill all `<Fill ...>` template blocks in: $ARGUMENTS (default: ./CLAUDE.md).

Follow the skill instructions in ~/.claude/skills/fill.md exactly.

Summary of the workflow:
1. Read the CLAUDE.md file and identify all `<Fill SectionName>...</Fill SectionName>` blocks
2. For each block, analyze the project's codebase to gather the required information
3. Replace each placeholder with real, verified content
4. For blocks with "Ask the user" instructions, present findings and ask the user to confirm or add details
5. Mark unresolvable gaps with `<!-- TODO: ask project owner about ... -->` comments
6. Do a final review pass checking for duplicated advice, contradictions, and irrelevant sections
7. Present a review summary and the completed file to the user
