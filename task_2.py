import csv
from datetime import datetime

# File to store expense data
EXPENSE_FILE = "expenses.csv"

# Function to initialize the expense file
def initialize_file():
    try:
        with open(EXPENSE_FILE, "x") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass

# Function to add an expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category (e.g., Food, Rent, Entertainment): ")
    description = input("Enter a brief description: ")
    try:
        amount = float(input("Enter amount: "))
        with open(EXPENSE_FILE, "a") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please try again.\n")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Function to output all expenses to a file
def output_expenses_to_file():
    output_file = "all_expenses_output.txt"
    try:
        with open(EXPENSE_FILE, "r") as infile, open(output_file, "w") as outfile:
            reader = csv.reader(infile)
            for row in reader:
                outfile.write(", ".join(row) + "\n")
        print(f"All expenses have been written to {output_file}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Function to view summary by category
def view_summary():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            summary = {}
            for row in reader:
                category = row[1]
                amount = float(row[3])
                summary[category] = summary.get(category, 0) + amount

            print("\nSummary by Category:")
            for category, total in summary.items():
                print(f"{category}: ${total:.2f}")
            print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary by Category")
        print("4. Output All Expenses to File")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            output_expenses_to_file()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
