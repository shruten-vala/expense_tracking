# adding the expense to the list
def add_expense(expenses, date, category, amount):
    expenses.append(
        {
            "date": date,
            "category": category,
            "amount": amount
        }
    )

# return filtered expenses + total for that category
def filter_expenses(expenses, category):
    filtered = []
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            filtered.append(expense)
            total += expense["amount"]

    return filtered, total

# calculate total of all expenses
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]

    return total

# delete expense by index (0-based index)
def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        return True, deleted
    else:
        return False, None
    
# category wise breakdown
def get_category_wise_totals(expenses):
    if not expenses:
        return {}
    category_totals = {}
    for expense in expenses:
        cat = expense.get("category", "Unknown").strip().title()
        amount = float(expense.get("amount", 0))

        if cat in category_totals:
            category_totals[cat] += amount
        else:
            category_totals[cat] = amount
            
    return category_totals

