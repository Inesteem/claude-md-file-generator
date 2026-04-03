---
name: PII Protection
type: static
tags: [security, privacy]
order: 7
description: Prevent personal identifying information from entering the repository
---
## PII Protection

- This repository is public. No personal identifying information (PII) must enter the git history.
- Never commit real names, email addresses, phone numbers, physical addresses, or usernames beyond what is already public in git config.
- Never commit API keys, tokens, passwords, or credentials — use environment variables or secret managers.
- Keep `.env`, credentials files, and any file containing PII in `.gitignore`.
- Use placeholder values (e.g. `you@example.com`, `<YOUR_API_KEY>`) in config templates and documentation.
- Before pushing, review staged changes for accidental PII exposure: `git diff --cached`.
- If PII is accidentally committed, treat it as a security incident — rotate any exposed credentials immediately and consider rewriting git history.
