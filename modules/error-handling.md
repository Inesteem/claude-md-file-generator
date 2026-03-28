---
name: Error Handling
type: static
tags: [errors, resilience]
order: 28
description: Rules for surfacing and communicating errors clearly
---
## Error Handling

- Never silently fail — surface errors clearly so the cause is immediately visible
- Use structured error output that includes both an error type and a human-readable message
- Include both the error code and a plain-language summary when tool calls fail
- Ask a clarifying question before guessing on missing context — do not invent assumptions silently
