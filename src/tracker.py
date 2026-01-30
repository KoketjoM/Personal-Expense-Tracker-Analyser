"""
Tracker script containing core logic of expense tracker
"""

from datetime import datetime, date, time
import pandas as pd
from cli import create_cli


# import time
expenses = pd.read_csv("../data/expenses.csv")
cli = create_cli()


def main():
    """
    Main entry function for tracker
    - Handles conditional logic
    """
    if cli.expense is not None:
        add()
    if cli.remove is not None:
        remove(cli.remove)

    print("-" * 20)
    print("Current entries:")
    print(expenses)
    print("-" * 20)


def add():
    """
    Function to add an expense entry
    """
    if cli.category is not None:
        pos = len(expenses)
        # Create entry
        entry = {
            "date": date.today(),
            "time": datetime.now().time(),
            "value": cli.expense,
            "category": cli.category,
        }

        # Append entry to dataframe
        expenses.loc[pos] = entry
        # Update CSv
        expenses.to_csv("../data/expenses.csv", index=False)
    else:
        print("category required")


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


def entries():
    """
    Function to list entries
    - Can be modified by date or category flags
    """


def total():
    """
    Function to get the agregate sum of expenses
    - Can be modified by date or category
    """


if __name__ == "__main__":
    main()
