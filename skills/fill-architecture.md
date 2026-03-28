# Fill Architecture

You are an agent tasked with filling in the `<Architecture>` template section of a CLAUDE.md file.

## Instructions

1. Map the directory structure:
   - List top-level directories/packages and their purpose
   - Note where source, tests, config, and assets live
2. Identify main components by reading source files:
   - Models/data layer
   - Business logic / core
   - UI / API / CLI layer
   - Storage / persistence
3. Trace the primary data flow(s) — what happens when the user does the main thing
4. Find external integrations (databases, APIs, file systems, caches, message queues)
5. Determine where state lives (database, config files, in-memory, environment)
6. Note important design decisions visible in the code (patterns chosen, trade-offs made)

## Output

Replace the `<Architecture>...</Architecture>` block in CLAUDE.md with filled-in content. Use this format:

```markdown
## Architecture

### Directory Structure
- `src/` — <purpose>
- `tests/` — <purpose>
- `<dir>/` — <purpose>

### Components
- **<Component>** (`path/`) — <responsibility>
- **<Component>** (`path/`) — <responsibility>

### Data Flow
<describe the primary flow in 2-4 sentences or a numbered list>

### External Integrations
- <database, API, filesystem, etc. — or "None" if self-contained>

### State
- <where persistent and transient state lives>

### Design Decisions
- <key trade-off or pattern choice and why>
```

## Rules

- Derive everything from the actual code — don't invent or assume
- Keep each component description to one line
- Focus on what helps a new contributor navigate the codebase
- Omit subsections that don't apply (e.g. no External Integrations for a pure library)
