# Technical Decisions & Tradeoffs

## Decision Log

### Decision 1: sys.argv vs argparse 🔤

**Date**: Month 1, Week 1
**Context**: Choosing argument parser for command line interface
**Options Considered:**

1. **sys.argv**: Simplest method. Returns command line arguments as a list.
    - Pros: Zero dependencies, full control.
    - Cons: Manual parsing, no validation, no help messages.

2. **argparse**: More robust. Fully featured command line parser.
    - Pros: Built-in, type validation, auto help, extensible.
    - Cons: More boilerplate, learning curve.

3. **getopt**: Usefull in handling flags, still requires sys,argv.
    - Pros: Handles flags well.
    - Cons: Harder to maintain.

**Decision**: argparse

**Reasoning:**

- **Complete features**: Don't have to build validation, help text, or type conversion from scratch.
- **Deep documentation**: Well-supported, lots of Stack Overflow answers.
- **Single, well-tested library**: Part of Python stdlib, won't break.
- **Future-proofing**: Easy to add subcommands later (e.g., `tracker add`, `tracker report`).
- **User experience**: Auto-generated help with `--help` flag.

**Tradeoffs Accepted:**

- Can't easily make unique CLI features or edit behavior of library.
- May be overkill for current simple use case (but app will grow).
- More verbose than sys.argv for basic cases.

**Outcome**:

- Less stress around the different CLI features I'd have to implement.
- Can focus on core logic instead of argument parsing.
- Better user experience with clear error messages.

**What I learned:**

- sys.argv is just a list - you parse everything yourself.
- argparse handles type conversion and validation automatically.
- Good libraries save time on boilerplate so you can focus on unique features.

**Would I make this choice again?** Yes. Even though it's more code upfront, the time saved on validation and help messages was worth it by Day 2.

---

### Decision 2: Python CSV Module vs Pandas Dataframes 📝

**Date**: Month 1, Week 1
**Context**: Choosing my csv read and write methods for data persistence.
**Options Considered:**

1. **CSV Module**: Reading to and writing from a python dictionary (or lists).
    - Pros: Zero dependencies, efficient read and write.
    - Cons: Manual data analysis, manual validation, list based (not intuitive).
2. **Pandas**: Reading to and writing from pandas Dataframe object.
    - Pros: Trusted library, built-in data analysis functionality.
    - Cons: New dependency, Medium learning curve.

**Decision**: Pandas

**Reasoning:**

- **Intuitive Dataframe Obj**: Dataframes are tabular, making future manipulation more intuitive.
- **Complete features**: Data agregation, manipulation and filtering is built in.
- **Future proofing**: Tabular data could be stored in databases and queried with sql in future.
- **Library Compatability**: Pandas is compatible with the data graphing libraries matplotlib and seaborn, which I will be using for the graphing functionality of this project.

**Tradeoffs Accepted:**

- Portability of program requires intallation of pandas to env.
- Dependencies must be updated (may break in future).
- New library to learn and understand (well documented with tutorials).

**Outcome**:

- No need to create search, data aggregation or data analysis algorithms.
- More consise, easily readable code
- May be overkill for project (but reduces posibility for human error)
- Extensive library allows me to focus on tracker functionality

**What I learned:**

- Use relative paths to ensure correct file retrieval
- Pandas throws a read error when the file is empty
- The interpreter should match your current command line env

**Would I make this choice again?** Yes. Pandas is a vital library in data analytics and is therefore used in professional settings as well. Exposure now will be beneficial long term.

---

### Decision 3: Entry ID's - Index based vs Hash Function

**Date**: Month 1, Week 1
**Context**: To allow for easier entry based search, entries should have a unique ID
**Options Considered:**

1. **Index-based custom ID column**: Separate 'id' column that increments
   - **Pros**: Persistent ID even after deletions, explicit and visible
   - **Cons**: Manual management, can have duplicates if not careful, extra column
2. **DateTime as ID**: Use timestamp as unique identifier  
   - **Pros**: Naturally unique per entry
   - **Cons**: Long string (2025-01-15T14:23:45), hard for users to type/remember
3. **Hash-based ID**: Hash the datetime or entry data
   - **Pros**: Short, collision-resistant
   - **Cons**: Complex implementation, potential collisions, overkill for small dataset
4. **DataFrame index** (discovered during implementation): Use Pandas built-in row index
   - **Pros**: Already exists, automatic, no extra column needed, simple deletion
   - **Cons**: Index changes when rows deleted (but this is fine for our use case)

**Initial Decision**: Custom ID column (Option 1)

**Initial Reasoning**:

- Wanted IDs to persist even after deletions
- Thought I needed to manually track: `entry_id = int(expenses["id"].iloc[-1]) + 1`
- Worried about duplicate IDs if using simple index

**Implementation Attempt**:

```python
# What I first tried - custom ID column
if cli.category is not None:
    pos = len(expenses)
    entry_id = int(expenses["id"].iloc[-1]) + 1 if pos > 0 else 0
    
    entry = {
        "id": entry_id,
        "date": date.today(),
        "time": datetime.now().time(),
        "value": cli.expense,
        "category": cli.category,
    }
    
    expenses.loc[pos] = entry
    expenses.to_csv("../data/expenses.csv", index=False)

# Attempted removal with custom ID
rows = expenses.loc[expenses["id"] == cli.remove]
if len(rows) > 0:
    print(f"{rows} entries found")
    expenses.drop(cli.remove, inplace=True)  # This doesn't work right!
    print(f"Entry {cli.remove} was removed")
```

**What I Discovered**:

- DataFrame `.drop()` works on **index**, not column values
- To delete by custom ID, I'd need: `expenses = expenses[expenses['id'] != cli.remove]`
- DataFrame already maintains unique index automatically
- For simple expense tracker, index is sufficient (we're not doing complex operations)

**Revised Decision**: Use DataFrame index (Option 4)

**Revised Reasoning**:

- **Simpler**: No extra column to manage, no manual ID generation
- **Built-in**: Pandas handles index automatically
- **Sufficient**: For delete operation, index works perfectly
- **User experience**: User sees row numbers when listing expenses (0, 1, 2...)
- **No complexity**: Deletion is one line: `df.drop(index, inplace=True)`

```python
# Final remove function
def remove(index):
    """Remove an expense entry by index"""
    try:
        # Drop for dataframe
        expenses.drop(index, inplace=True)
        # Reset index to keep it clean
        expenses.reset_index(drop=True, inplace=True)
        # Update expenses CSV
        expenses.to_csv("../data/expenses.csv", index=False)
        print(f"Entry {index} removed successfully")
    except KeyError:
        print(f"Entry {index} not found")

```

**Tradeoffs Accepted**:

- Index numbers change after deletion (row 5 becomes row 4 if row 3 deleted)
  - **Why this is OK**: User sees current state when they list expenses
  - **When this would be a problem**: Multi-user system, need persistent IDs
        - No historical record of deleted entries
  - **Why this is OK**: Simple personal tracker, not audit system
  - **When this would be a problem**: Business expense tracking, need audit trail

**What I Learned**:

**DataFrame fundamentals**:

- `.drop()` operates on index, not arbitrary columns
- Index is automatically maintained (0, 1, 2, 3...)
- After dropping row 2: index becomes [0, 1, 3, 4] (gap exists)
- Can reset index with `df.reset_index(drop=True)` if needed

**When to use custom IDs**:

- ✅ Multi-user systems (need stable references)
- ✅ Database-backed apps (foreign key relationships)
- ✅ Audit requirements (track what was deleted when)
- ❌ Simple single-user tracker (index is fine)

**Would I make this choice again?**

Yes - for this project scope. The index-based approach is:

- Simpler (less code to maintain)
- Sufficient (meets all current requirements)  
- Pythonic (uses DataFrame as intended)

**However**, if requirements changed to:

- Multi-user access → Would need UUID or database-generated IDs
- Audit trail needed → Would need persistent IDs that never reuse
- API for external apps → Would need stable, persistent identifiers

Then I'd revisit and implement proper ID column or move to SQLite with auto-increment primary keys.

**Key Insight**: Don't over-engineer for hypothetical future needs. Build what solves today's problem, refactor if requirements change. This saved ~30 minutes of unnecessary ID management code.

---

## Anti-Patterns I Avoided

### ❌ Pattern

**Temptation**:
**Reality**:
**Example**:

---

## Lessons Learned

### Technical

1. **Start simple, add complexity**: Started with basic implementation, then refactored for design
2. **Monitor everything**: Can't improve what you don't measure
3. **Fail fast**: Good error messages save hours of debugging
4. **Automate repetition**: If you do it twice, script it

### Process

1. **Document as you go**: Future you will forget why you did things
2. **Test early and often**: Test every new feature before adding onto it
3. **Just In Time Information**: Its better to get information when needed instead of falling into tutorial hell
