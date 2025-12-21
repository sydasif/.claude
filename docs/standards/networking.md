# Network Safety Principles

## Change Approach

Treat all network-related changes as production-impacting by default.

- Verify syntax and behavior from existing configs
- Avoid assumptions about topology or platform
- Prefer small, reversible changes
- Explain impact before suggesting changes
- Always consider rollback and failure scenarios
- Respect vendor-specific behavior
- Avoid guessing commands or syntax

## Automation Standards

Automation must be safe and predictable.

- Prefer idempotent operations
- Avoid one-off or fragile scripts
- Fail clearly on errors
- Keep inputs and outputs explicit
- Do not hide side effects
- Keep automation repeatable
- Favor validation-first or dry-run approaches
- Treat configs as production-sensitive
- Prefer incremental edits

## Configuration Safety

- Do not guess vendor syntax or behavior
- Respect vendor-specific limitations
- Avoid irreversible changes
- Implement timeout controls (SSH Connect 60s, Auth 30s, Command Execute 120s, Global 300s)
- Implement retry logic with exponential backoff
- All automation scripts must be safe to run multiple times (idempotency)

## Validation & Safety

- Favor dry-run or validation-first workflows
- Call out risks clearly
- Explain intent of config changes
- Note rollback considerations
- Highlight dependencies or prerequisites
- Use the `READ_ONLY_COMMANDS` list for all non-destructive discovery
- Always create a configuration checkpoint/backup before major changes

## Boundaries

- Do not touch credentials or secrets
- Do not push configs to live devices without approval
- Do not assume topology, platform, or OS
- Act as a cautious network engineer
- Treat all changes as production-impacting
- Avoid assumptions
