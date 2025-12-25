expenses = []
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!\n")
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: ₹{expense['amount']}, "
              f"Category: {expense['category']}, "
              f"Date: {expense['date']}, "
              f"Note: {expense['note']}")
    print()

import csv
def save_expenses_to_file():
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["amount", "category", "date", "note"])  # header

        for expense in expenses:
            writer.writerow([
                expense["amount"],
                expense["category"],
                expense["date"],
                expense["note"]
            ])
def load_expenses_from_file():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"],
                    "note": row["note"]
                })
    except FileNotFoundError:
        pass  # file doesn't exist yet

def category_wise_summary():
    if not expenses:
        print("No expenses to analyze.\n")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nCategory-wise Spending:")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")

    print()

def highest_spending_category():
    if not expenses:
        print("No expenses to analyze.\n")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    highest_category = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_category]

    print(f"\nHighest spending category: {highest_category} (₹{highest_amount})\n")

def percentage_breakdown():
    if not expenses:
        print("No expenses to analyze.\n")
        return

    total_spent = sum(expense["amount"] for expense in expenses)
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nPercentage-wise Spending:")
    for category, amount in category_totals.items():
        percentage = (amount / total_spent) * 100
        print(f"{category}: {percentage:.2f}%")

    print()

def monthly_summary():
    if not expenses:
        print("No expenses recorded.\n")
        return

    month = input("Enter month (YYYY-MM): ")
    total = 0

    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]

    print(f"\nTotal expense for {month}: ₹{total}\n")


load_expenses_from_file()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category-wise Summary")
    print("4. Highest Spending Category")
    print("5. Percentage Breakdown")
    print("6. Monthly Summary")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_wise_summary()
    elif choice == "4":
        highest_spending_category()
    elif choice == "5":
        percentage_breakdown()
    elif choice == "6":
        monthly_summary()
    elif choice == "7":
        save_expenses_to_file()
        print("Expenses saved. Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")
