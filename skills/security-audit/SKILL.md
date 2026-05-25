---
name: security-audit
description: Run security scans on Python codebase after refactoring. Checks for vulnerabilities, dependency issues, and unsafe patterns. Use after refactor-code, before review-code.
---

# Security Audit Skill

Run comprehensive security scans on the codebase and block if critical issues are found.

## When to Use

- After `refactor-code` has modernized the code
- Before `review-code` final gate
- Any time you need a security health check

## Required Tools

- `bandit` – static security analysis
- `safety` – dependency vulnerability scan
- `uv-secure` – project dependency scanning

## Scan Commands

Run these from the project root:

```bash
uv run bandit -r src/ -f json -o bandit-report.json
uv run safety check --json > safety-report.json
uv run uv-secure scan --json > uv-secure-report.json
```

## Severity Rules

| Tool        | Blocking Condition               |
| ----------- | -------------------------------- |
| `bandit`    | HIGH severity OR HIGH confidence |
| `safety`    | Medium+ severity                 |
| `uv-secure` | Any vulnerability                |

## Non‑blocking Findings

Report but do not block:

- `bandit` MEDIUM/LOW severity with MEDIUM/LOW confidence
- `safety` Low severity

## Output Format

Produce a structured report:

```markdown
## Security Audit Report

### Bandit

- Total issues: X
- HIGH severity: Y (blocking if >0)
- MEDIUM severity: Z

### Safety

- Vulnerable packages: A (blocking if >0)
- Details: ...

### uv-secure

- Issues found: B (blocking if >0)

### Verdict

- PASS / FAIL (blocking issues found)
```

## Action on Block

If blocking issues found:

1. Report them clearly with file:line references
2. Suggest fixes (e.g., pin dependency, rewrite unsafe pattern)
3. Stop pipeline – do not proceed to `review-code`
4. Wait for user confirmation after fixes

## Integration

This skill is part of the pipeline: `cleanup-code` → `refactor-code` → `security-audit` → `review-code`
