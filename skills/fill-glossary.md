# Fill Glossary

You are an agent tasked with filling in the `<Glossary>` template section of a CLAUDE.md file.

## Instructions

1. Scan the codebase for domain-specific terminology:
   - Class names, module names, and constants that use project-specific jargon
   - Comments or docstrings that define terms
   - README sections that introduce concepts
2. Identify abbreviations and acronyms used in code, filenames, or docs
3. Look for terms whose meaning in this project differs from standard industry usage
4. Cross-reference with the Architecture section — don't repeat component descriptions, just define the names

## Output

Replace the `<Glossary>...</Glossary>` block in CLAUDE.md with filled-in content. Use this format:

```markdown
## Glossary

**<Term>**
: <Definition and relevant context.>

**<Term>**
: <Definition and relevant context.>
```

## Rules

- Only include terms that would confuse someone unfamiliar with the project
- Skip standard tech terms (API, ORM, CLI, etc.) unless they have a special meaning here
- Keep definitions to one or two sentences
- Sort alphabetically
- If the project has no meaningful jargon, write "No project-specific terminology beyond standard usage." and move on
