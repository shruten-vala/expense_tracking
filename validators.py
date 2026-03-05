
from datetime import datetime
def print_welcome():

    welcome_text = r"""
  ___                               _____               _             
 | __|_ ___ __ ___ _ _  ___ ___    |_   _| _ __ _  __| |_____ _ _ 
 | _|\ \ / '_ \/ -_) ' \(_-</ -_)     | || '_/ _` |/ _| / / -_) '_|
 |___/_\_\ .__/\___|_||_/__/\___|     |_||_| \__,_|\__|_\_\___|_|  
         |_|                                                      
    """
    print(welcome_text)
    print("=" * 65)
    print("           Welcome to your personal Expense Tracker!           ")
    print("=" * 65 + "\n")

def get_menu_choice():
    """Gathers the user's main menu selection."""
    print("\n1. View All Expenses")
    print("2. Add New Expense")
    print("3. Filter by Category")
    print("4. Category wise breakdown")
    print("5. Delete Expense")
    print("6. Exit")
    
    return input("\nSelect an option (1-6): ").strip()

from datetime import datetime

def get_expense_input():
    """Gathers data for one or more NEW expenses."""
    new_expenses = []
    
    while True:
        try:
            n = int(input("\nHow many expenses do you want to add? "))
            if n <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(n):
        print(f"\n--- Entering Expense {i+1} of {n} ---")
        
        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                valid_date = datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid format. Please use YYYY-MM-DD (e.g., 2026-03-03).")
                
        category = input("Enter category (e.g., Food, Travel): ").strip()
        
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                
        new_expenses.append({"date": date, "category": category, "amount": amount})
        
    return new_expenses

def get_category_choice():
    """Gathers a category name for filtering."""
    return input("\nEnter category to filter by: ").strip()

def get_index_to_delete():
    """Gathers the ID/Index for deletion."""
    while True:
        try:
            return int(input("\nEnter the ID of the record to delete: "))
        except ValueError:
            print("Invalid ID! Please enter a whole number.")






