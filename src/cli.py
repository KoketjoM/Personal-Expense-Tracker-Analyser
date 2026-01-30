"""
Command line interface
- Decided to use argparser for command line arguments
- Docs: https://docs.python.org/3/library/argparse.html
"""

import argparse


def create_cli():
    """
    Creates CLI including all related command line arguments for expense tracker app:
    - Adding an expense
    - Adding a category to entry
    - Adding a date to entry
    - Removing an expense entry
    - Search by month parameter
    - Listing entries by search parameter
    - Output expense balance

    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--expense", type=float, help="Adds an expense value")
    parser.add_argument("-c", "--category", type=str, help="Adds a label to the entry")
    parser.add_argument(
        "-d", "--date", type=str, help="Adds a date string (DD-MM-YYYY)"
    )

    parser.add_argument("--remove", type=int, help="Use entry ID to remove from CSV")
    parser.add_argument("--month", type=str, help="Search by month parameter")

    parser.add_argument("--list", help="Output search results")
    parser.add_argument("--total", help="Output expense balance")

    return parser.parse_args()


#  ---- Testing ----
if __name__ == "__main__":
    cli = create_cli()

    if cli.expense is not None:
        print(f"Expense added: {cli.expense}")
    if cli.category is not None:
        print(f"Category added: {cli.category}")
