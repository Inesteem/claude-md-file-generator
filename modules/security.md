---
name: Security
type: static
tags: [security]
order: 26
description: Security practices for handling credentials and sensitive operations
---
## Security

- Never output API keys, credentials, or secrets in any response or generated file
- Use placeholder tokens like `<REDACTED>` when a secret must be referenced in output
- Refuse destructive production operations (e.g. DROP, DELETE, data wipes) without explicit confirmation
- Do not commit `.env` files or files containing credentials to version control
- Sanitize user-supplied input at all system boundaries before use
