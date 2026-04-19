# Claude CLI: Advanced Configuration & Customization Framework

This repository defines the core architecture for personalizing Claude Code across Python development workflows. It implements a tiered customization system designed to optimize context usage, enforce engineering standards, and automate domain-specific procedures.

## 1. System Architecture

The configuration follows a **Progressive Disclosure Strategy**, separating critical constraints from domain-specific reference material to maximize token efficiency.

### Tier 1: Always-On Constraints (Rules)

- **Path:** `~/.claude/rules/`
- **Behavior:** Automatically injected into every session.
- **Purpose:** Critical security, testing, and tool-chain requirements.
- **Key Files:** `security.md`, `testing.md`, `tools.md`.

### Tier 2: Domain-Specific Reference (Guidelines)

- **Path:** `~/.claude/guidelines/`
- **Behavior:** Manual loading via the `Read` tool as needed.
- **Purpose:** Best practices for specific technologies or patterns (e.g., Python, REST APIs).
- **Efficiency:** Reduces baseline context by 60-80% by avoiding unnecessary data loading.

### Tier 3: Actionable Workflows (Skills)

- **Path:** `~/.claude/skills/`
- **Behavior:** Triggered on-demand via intent detection or explicit activation.
- **Structure:** Markdown bundles with YAML metadata defining step-by-step procedures.
- **Example:** `code-refactor/SKILL.md` defines modernization sequences (Pathlib, Type Hints, etc.).

### Tier 4: Task Isolation (Subagents)

- **Path:** `~/.claude/agents/`
- **Behavior:** Spawned for deterministic, isolated subtasks.
- **Control:** Supports strict permissioning (e.g., read-only) and model-specific selection (Haiku vs. Sonnet).

---

## 2. Directory Structure

```text
~/.claude/
├── CLAUDE.md                # Core engineering mandates (auto-loaded)
├── rules/                   # TIER 1: Always-on critical constraints
│   ├── security.md          # Input validation, secret management
│   ├── testing.md           # Coverage thresholds & verification strategies
│   └── tools.md             # Standardized CLI command references
├── guidelines/              # TIER 2: On-demand domain knowledge
│   ├── python.md            # Idiomatic Python & async patterns
│   ├── api-design.md        # RESTful principles & schema standards
│   ├── database.md          # ORM optimization & migration workflows
│   └── documentation.md     # Documentation standards
├── skills/                  # TIER 3: Intent-based workflows
│   ├── code-refactor/       # Modernization & cleanup sequences
│   └── research/            # Structured discovery & analysis
└── agents/                  # TIER 4: Specialized subagents
    └── code-reviewer.md     # Read-only semantic analysis configuration
```

---

## 3. Configuration Hierarchy & Resolution

Claude resolves configurations using a specific priority order, allowing project-level overrides to supersede global defaults.

| Priority        | Scope       | Location                   | Usage                                              |
| :-------------- | :---------- | :------------------------- | :------------------------------------------------- |
| **1 (Highest)** | **Module**  | `path/to/module/CLAUDE.md` | Specific logic for a single service/package.       |
| **2**           | **Project** | `./CLAUDE.md`              | Tech stack, build commands, and local repo rules.  |
| **3**           | **Global**  | `~/.claude/CLAUDE.md`      | Personal style, safety rules, and global toolsets. |
| **4 (Lowest)**  | **System**  | Internal Defaults          | Default CLI behavior and safety guardrails.        |

---

## 4. Operational Workflows

### Loading Domain Context

To maintain a lean context window, only load guidelines relevant to the current task:

```bash
# For Python-centric feature development
Read ~/.claude/guidelines/python.md

# For API architectural planning
Read ~/.claude/guidelines/api-design.md
```

### Executing Specialized Reviews

Utilize the read-only Subagent for semantic verification without risk of unintended side effects:

```bash
# Request a structured review
Use the code-reviewer subagent to analyze the current diff for PEP-8 compliance.
```

---

## 5. Security & Engineering Standards

All contributions to this configuration must adhere to the **Security-First Mandate**:

1.  **Least Privilege:** Subagents should be restricted to the minimum tools required.
2.  **No Secrets:** Never store API keys or sensitive strings in any `.md` or YAML file.
3.  **Explicit Failure:** Skills must include error-handling steps for edge cases (e.g., network loss, malformed input).

---

## 6. Maintenance

- **License:** MIT
- **Version Tracking:** Configuration changes should be versioned alongside project code when possible.
- **Documentation:** Updates to `rules/` or `guidelines/` must be reflected in the corresponding reference file.
  nce file.
