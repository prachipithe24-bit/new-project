"""
Expense Tracker (Command-Line App)
Author: Prachi
"""

import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "amount", "note"]


def init_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def add_expense():
    date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (e.g. Food, Travel, Bills): ").strip() or "Other"

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Expense not added.\n")
        return

    note = input("Note (optional): ").strip()

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({"date": date, "category": category, "amount": amount, "note": note})

    print("Expense added!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    print(f"{'Date':<12}{'Category':<15}{'Amount':<10}{'Note'}")
    print("-" * 50)
    for row in rows:
        print(f"{row['date']:<12}{row['category']:<15}{row['amount']:<10}{row['note']}")
    print()


def summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    total = 0
    by_category = {}

    for row in rows:
        amt = float(row["amount"])
        total += amt
        by_category[row["category"]] = by_category.get(row["category"], 0) + amt

    print("\n--- Expense Summary ---")
    for category, amt in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"{category:<15}: {amt:.2f}")
    print("-" * 30)
    print(f"{'Total':<15}: {total:.2f}\n")


def main():
    init_file()

    menu = """
==== EXPENSE TRACKER ====
1. Add expense
2. View all expenses
3. View summary by category
4. Exit
==========================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
