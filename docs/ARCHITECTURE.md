# Architecture Documentation

## System Overview

```
┌─────────────┐
│   User      │
└──────┬──────┘
       │ CLI commands
       ▼
┌─────────────────┐
│  CLI Interface  │ ← argparse
│   (cli.py)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Expense Tracker │ ← Core logic (Week 2)
│  (tracker.py)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CSV Storage    │ ← Data persistence (Week 2)
│ (expenses.csv)  │
└─────────────────┘
```

## Component Design

### 1. Command Line Interface

**Purpose**: Parse user input and route to appropriate operations

**File**: `src/cli.py`

**Flow**: User types command → argparse parses → validate input → call tracker method → display result

**Implementation**:

```bash
# Current commands (to be extended later):
python cli.py --expense --amount 45.50 --category groceries --date 2025-01-15
python cli.py --list --month january
python cli.py --total --category groceries
```

**Key Decisions**:

- **Library choice**: argparse
  - Why: Built-in validation, type conversion, auto-help generation
  - Alternative considered: sys.argv (too manual), getopt (less Pythonic)
  - See DECISIONS.md for full comparison

- **Command structure**: Flag-based arguments (`--amount`) vs positional
  - Why: More explicit, easier to extend, order doesn't matter
  - Example: `--amount 45.50` vs just `45.50`

- **Validation**: Type checking at argparse level
  - Why: Fail fast with clear error messages
  - Example: `type=float` ensures amount is numeric before reaching core logic
