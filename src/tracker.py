"""
Tracker script containing core logic of expense tracker
"""

import pandas as pd
from cli import create_cli

# import time


def main():
    """
    Main entry function for tracker
    - Creates cli instance
    """
    expenses = pd.read_csv("../data/expenses.csv")
    cli = create_cli()

    if cli.expense is not None:
        print(f"Expense added: {cli.expense}")
    if cli.category is not None:
        print(f"Category added: {cli.category}")


if __name__ == "__main__":
    main()
