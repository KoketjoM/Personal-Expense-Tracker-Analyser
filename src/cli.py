# Decided to use argparser for command line arguments
# Docs: https://docs.python.org/3/library/argparse.html
import argparse

# import time

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--expense", type=float, help="Adds an expense value")
parser.add_argument("-i", "--income", type=float, help="Adds an income value")
parser.add_argument("-c", "--category", type=str, help="Adds a label to the entry")
parser.add_argument("-r", "--remove", type=int, help="Use entry ID to remove from CSV")

args = parser.parse_args()

if args.expense is not None:
    print(f"Expense added: {args.expense}")
if args.income is not None:
    print(f"Income added: {args.income}")
if args.category is not None:
    print(f"Category added: {args.category}")
