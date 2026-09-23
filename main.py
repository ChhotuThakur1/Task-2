from tracker import ExpenseTracker


def display_menu():
    print("\n" + "=" * 30)
    print("      EXPENSE TRACKER")
    print("=" * 30)
    print("1. Add an Expense")
    print("2. View Total Spent")
    print("3. View Breakdown by Category")
    print("4. Exit")
    print("=" * 30)


def prompt_add_expense(tracker: ExpenseTracker):
    raw_amount = input("Enter expense amount (e.g., 50.00): ").strip()
    try:
        amount = float(raw_amount)
    except ValueError:
        print("Invalid number. Operation cancelled.")
        return

    category = input("Enter category (optional, default 'General'): ").strip()
    if not category:
        category = "General"

    try:
        tracker.add_expense(amount, category)
        print(f"Added ${amount:.2f} to '{category}'.")
        print(f"Current Total Spent: ${tracker.total_spent:.2f}")
    except ValueError as err:
        print(f"Error: {err}")


def prompt_view_breakdown(tracker: ExpenseTracker):
    summary = tracker.get_summary()
    if not summary:
        print("No expenses recorded yet.")
        return

    print("\nSpending Breakdown:")
    for category, total in summary.items():
        print(f" - {category}: ${total:.2f}")
    print(f"\nFinal Total Spent: ${tracker.total_spent:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            prompt_add_expense(tracker)
        elif choice == "2":
            print(f"\nTotal Spent: ${tracker.total_spent:.2f}")
        elif choice == "3":
            prompt_view_breakdown(tracker)
        elif choice == "4":
            print(f"\nExiting. Total Spent: ${tracker.total_spent:.2f}. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
