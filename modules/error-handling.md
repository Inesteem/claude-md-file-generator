---
name: Error Handling
type: static
tags: [errors, resilience]
order: 28
description: Rules for surfacing and communicating errors clearly
---
## Error Handling

- Never silently fail — surface errors clearly so the cause is immediately visible
- Use structured error output that includes at minimum an error type/category and a human-readable message
- Include both the error code and a plain-language summary when tool calls fail
- Never include credentials, internal paths, or raw stack traces in user-facing error output
- When context is insufficient to determine the correct behavior, fail explicitly with a descriptive error rather than falling back to a default assumption
