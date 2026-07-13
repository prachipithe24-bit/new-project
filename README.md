# 💰 Expense Tracker (CLI)

A command-line Python app to track daily expenses, categorize spending, and view summaries — all stored in a local CSV file.

## Features
- ➕ Add expenses with date, category, amount, and notes
- 📋 View all recorded expenses in a table
- 📊 View a spending summary grouped by category, with total
- 💾 Data saved in `expenses.csv` (easy to open in Excel too)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. Run the app:
   ```bash
   python expense_tracker.py
   ```

## Requirements
- Python 3.6 or higher (uses only built-in `csv`, `os`, and `datetime` modules)

## Example

```
==== EXPENSE TRACKER ====
1. Add expense
2. View all expenses
3. View summary by category
4. Exit
==========================
Choose an option (1-4): 1
Date (YYYY-MM-DD) [leave blank for today]: 
Category (e.g. Food, Travel, Bills): Food
Amount: 250
Note (optional): Lunch with friends
Expense added!
```

Summary output:
```
--- Expense Summary ---
Food           : 250.00
------------------------------
Total          : 250.00
```

## Future Improvements
- Filter expenses by date range or month
- Add a budget limit with alerts
- Export summary as a chart (using matplotlib)
- Build a web version with Flask

## Author
Prachi
