expenses = []

def add_expense(amount, description):
    expenses.append({"amount": amount, "description": description})
    print("Expense added successfully.")

def view_summary():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount spent: $"))
                description = input("Enter a brief description: ")
                add_expense(amount, description)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
