# Technical Decisions & Tradeoffs

## Decision Log

### Decision 1: sys.argv vs argparse

**Date**: Month 1, Week 1
**Context**: Choosing choosing argument parser for command line interface
**Options Considered:**

1. **sys.argv**: Simplest method. Returns command line arguments as a list.
    - Pros: Zero dependencies, full control
    - Cons: Cons: Manual parsing, no validation, no help messages

2. **argparse**: More robust. Fully featured command line parser.
    - Pros: Built-in, type validation, auto help, extensible
    - Cons: More boilerplate, learning curve

3. **getopt**: Usefull in handling flags, still requires sys,argv.
    - Pros: Handles flags well
    - Cons: Harder to maintain

**Decision**: argparse

**Reasoning:**

- **Complete features**: Don't have to build validation, help text, or type conversion from scratch
- **Deep documentation**: Well-supported, lots of Stack Overflow answers
- **Single, well-tested library**: Part of Python stdlib, won't break
- **Future-proofing**: Easy to add subcommands later (e.g., `tracker add`, `tracker report`)
- **User experience**: Auto-generated help with `--help` flag

**Tradeoffs Accepted:**

- Can't easily make unique CLI features or edit behavior of library
- May be overkill for current simple use case (but app will grow)
- More verbose than sys.argv for basic cases

**Outcome**:

- Less stress around the different CLI features I'd have to implement.
- Can focus on core logic instead of argument parsing
- Better user experience with clear error messages

**What I learned:**

- sys.argv is just a list - you parse everything yourself
- argparse handles type conversion and validation automatically
- Good libraries save time on boilerplate so you can focus on unique features

**Would I make this choice again?** Yes. Even though it's more code upfront, the time saved on validation and help messages was worth it by Day 2.

---

### Decision 2

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
