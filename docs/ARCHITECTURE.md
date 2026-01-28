# Architecture Documentation

## System Overview

[High-level architecture diagram]

## Component Design

### 1. Command Line Interface

**Purpose**: Take user input and perform operations

**Flow**: Command line text input → conditional function call based on flag
**Key Decisions:**

- **argparser**: used `add_argument` to add flag based arguments
  - Why: I can call specific functions based on flags added to cli
