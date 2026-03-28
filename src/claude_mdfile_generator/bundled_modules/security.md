---
name: Security
type: static
tags: [security]
order: 26
description: Security practices for handling credentials and sensitive operations
---
## Security

- Never output real API keys, credentials, or secrets in any response, generated file, or example
- When a secret must appear in output, use the placeholder format `<PLACEHOLDER_NAME>` (e.g. `<API_KEY>`, `<DB_PASSWORD>`, `Bearer <TOKEN>`)
- Ensure secrets are excluded from log output, debug traces, and error messages
- Refuse destructive production operations (e.g. DROP, DELETE, data wipes) without explicit confirmation
- Do not commit `.env` files or files containing credentials to version control
- Sanitize user-supplied input at all system boundaries before use
