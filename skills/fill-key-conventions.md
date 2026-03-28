# Fill Key Conventions

You are an agent tasked with filling in the `<Key Conventions>` template section of a CLAUDE.md file.

## Instructions

1. Analyze error handling patterns:
   - Does the project use exceptions, Result types, error codes, or HTTP statuses?
   - Is there a custom error hierarchy or base exception?
2. Check logging conventions:
   - Which logging library? What log levels are used and where?
   - Structured (JSON) or unstructured (text)?
3. Determine language/runtime constraints:
   - Minimum version specified in config?
   - Any syntax or features explicitly avoided?
4. Check naming conventions:
   - Do variable, function, or file names follow a project-specific pattern?
   - Any divergence from language defaults?
5. Examine import/module organization:
   - Is there a consistent import ordering?
   - Are there internal vs. external import groupings?
6. Look at testing conventions:
   - Test file naming pattern (test_*.py, *.test.ts, etc.)
   - Fixture patterns, factory functions, common test helpers
   - Mocking approach (what gets mocked, what doesn't)
7. Identify important config files and what they control
8. Look for "code smells" that are actually intentional — comments like "# noqa", "// nolint", "HACK:", "WORKAROUND:"

## Output

Replace the `<Key Conventions>...</Key Conventions>` block in CLAUDE.md with filled-in content. Use this format:

```markdown
## Key Conventions

### Error Handling
- <approach and any custom types>

### Logging
- <library, levels, format>

### Language Constraints
- <version, avoided features>

### Naming
- <any project-specific conventions>

### Imports
- <ordering rules>

### Testing
- <naming, fixtures, mocking approach>

### Configuration
- <key config files and what they control>

### Intentional Oddities
- <patterns that look wrong but are deliberate — explain why>
```

## Rules

- Only document conventions that are actually present in the code
- Omit subsections where the project just follows language defaults
- Be specific — "uses logging module" is useless; "uses `logging` with DEBUG for storage layer, INFO elsewhere" is useful
- For intentional oddities, always explain why — the whole point is preventing someone from "fixing" them
