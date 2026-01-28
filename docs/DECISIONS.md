# Technical Decisions & Tradeoffs

## Decision Log

### Decision 1: sys.argv vs argparse

**Date**: Month 1, Week 1
**Context**: Choosing choosing argument parser for command line interface
**Options Considered:**

1. sys.argv - Simplest method. Returns command line arguments as a list.
2. argparse - More robust. Fully featured command line parser.
3. getopt - Usefull in handling flags, still requires sys,argv.

**Decision**: argparse
**Reasoning:**

- Complete features (don't have to build out features from scratch)
- Deep documentation
- Single, well tested library

**Tradeoffs Accepted:**

- Can't easily make unique CLI features or edit behaviour of library

**Outcome**: Less stress around the different CLI features I'd have to implement.

---

### Decision 2

**Date**: Month _, Week_
**Context**:

**Options Considered:**

1. Option - features, requirements
2. Option - features, requirements
3. Option - features, requirements

**Decision**:
**Reasoning:**

- Reason
- Reason
- Reason

**Tradeoffs Accepted:**

- Tradeoff
- Tradeoff
- Tradeoff

**What I'd do differently**: Explanation

---

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
