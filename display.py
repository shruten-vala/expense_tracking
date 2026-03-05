

def show_filtered_report(filtered_list, category, total_amt):
    """It receives ready data. It does not filter or calculate."""
    if not filtered_list:
        print(f"\n--- No records found for: {category} ---")
        return

    print(f"\n~~~~~~~~~~~~ Filtering: {category.upper()} ~~~~~~~~~~~~")
    print(f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount'}")
    print("-" * 53)

    for i, exp in enumerate(filtered_list):
        print(f"{i+1:<4} | {exp['date']:<12} | {exp['category']:<15} | ${exp['amount']:>8.2f}")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"TOTAL FOR {category.upper()}: ${total_amt:>25.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def show_total(expenses, total):
    """It receives ready data. It does not calculate."""
    print("\n~~~~~~~~~~~~~~~~~~~ Expense Summary ~~~~~~~~~~~~~~~~~~~")

    print(f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount'}")
    print("-" * 53)

    for i, exp in enumerate(expenses):
        print(f"{i+1:<4} | {exp['date']:<12} | {exp['category']:<15} | ${exp['amount']:>8.2f}")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"GRAND TOTAL: ${total:>37.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def show_delete_result(success, item):
    """It receives ready data. It does not delete."""
    if success and item:
        print("\n~~~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~~~")
        print(f"DELETED: {item['date']} | {item['category']} | ${item['amount']:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("\n!!!!!!!!!!!!!!!! Error !!!!!!!!!!!!!!!!")
        print("Invalid ID. No item was removed.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def show_category_wise_totals(category_totals):
    """Prints the dictionary of category totals in a formatted table."""
    if not category_totals:
        print("\nNo expenses to summarize yet.")
        return
        
    print("\n~~~~ Category-Wise Breakdown ~~~~")
    print(f"{'Category':<15} | {'Total Amount'}")
    print("-" * 33)
    
    for cat, total in category_totals.items():
        print(f"{cat:<15} | ${total:>12.2f}")
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")