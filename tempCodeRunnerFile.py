
            new_data_list = validators.get_expense_input()
            expenses.extend(new_data_list)
            storage.save_data(expenses)

            print(f"\n✅ {len(new_data_list)} expense(s) added successfully!")

        elif choice == '3':  # Filter by Category
            cat = validators.get_category_choice()
            filtered, total = services.filter_expenses(expenses, cat)
            display.show_filtered_report(filtered, cat, total)

        elif choice == '4':  # Category-Wise Breakdown
            totals_dict = services.get_category_wise_totals(expenses)
            display.show_category_wise_totals(totals_dict)

        elif choice == '5':  # Delete Expense
            total = services.calculate_total(expenses)
            display.show_total(expenses, total