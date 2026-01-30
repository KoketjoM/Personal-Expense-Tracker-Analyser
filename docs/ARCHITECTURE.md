# Architecture Documentation

## System Overview

```markdown
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

---

### 5. Data Persistence & ID Management

**Purpose**: Store expenses and provide unique identifiers for operations

**File**: `src/tracker.py`

**ID Strategy**: DataFrame index (not custom ID column)

**Why?**:

- Pandas maintains index automatically
- Delete operation works on index: `df.drop(index)`
- User sees index when listing (0, 1, 2...)
- Sufficient for single-user application

**Considered alternatives**:

- Custom ID column (over-engineered for use case)
- DateTime ID (poor user experience)
- UUID (overkill for local app)

**Implementation**:

```python
# Adding preserves automatic indexing
expenses.loc[len(expenses)] = new_entry

# Deleting by index is simple
expenses.drop(index, inplace=True)
expenses.reset_index(drop=True, inplace=True)  # Keep index clean
```

**When this would change**:

- Multi-user system → Need persistent UUIDs
- Database migration → Use auto-increment primary keys
- Audit requirements → Need stable IDs that never reuse
