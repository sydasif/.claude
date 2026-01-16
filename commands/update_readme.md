---
name: update-readme
description: Check README.md and update it based on recent git log changes
---

# Update README from Git Log

This command checks the README.md file and updates it to reflect recent changes from the git log.

## What it does

1. Reads the current README.md
2. Fetches recent git log entries
3. Analyzes what has changed since the last README update
4. Updates the README.md with:
   - New features added
   - Changes made
   - Fixes applied
   - Documentation updates
5. Maintains existing README structure
6. Adds a "Recent Updates" or "Changelog" section if needed

## Example workflow

When you run `/update-readme`, Claude will:

```bash
# Get recent commits
git log --oneline --since="30 days ago"

# Analyze README.md
cat README.md

# Generate updated README with recent changes
# Preserving existing content while adding new information
```

## Notes

- Preserves existing README structure
- Only adds information about changes not already documented
- Focuses on user-facing changes, not internal refactoring
- Can specify a custom time range if needed
