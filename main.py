import services
import validators
import storage
import display


def main():
    # Load data ONCE and store in memory
    expenses = storage.load_data()

    # Show welcome screen
    validators.print_welcome()

    while True:
        # Get user choice
        choice = validators.get_menu_choice()

        if choice == '1':  # View All
            total = services.calculate_total(expenses)
            display.show_total(expenses, total)

        elif choice == '2':  # Add Expense
            new_data_list = validators.get_expense_input()
            expenses.extend(new_data_list)
            storage.save_data(expenses)

            print(f"\n✅ {len(new_data_list)} expense(s) added successfully!")

        elif choice == '3':  # Filter by Category
            cat = validators.get_category_choice()
            filtered, total = services.filter_expenses(expenses, cat)
            display.show_filtered_report(filtered, cat, total)

        elif choice == '4':  # Category-Wise Breakdown￼

            totals_dict = services.get_category_wise_totals(expenses)
            display.show_category_wise_totals(totals_dict)

        elif choice == '5':  # Delete Expense
            total = services.calculate_total(expenses)
            display.show_total(expenses, total)

            idx = validators.get_index_to_delete()
            success, item = services.delete_expense(expenses, idx)

            display.show_delete_result(success, item)

            if success:
                storage.save_data(expenses)


        elif choice == '6':  # Exit
            storage.save_data(expenses)
            print("Thank you for using Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()