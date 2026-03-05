import os
import csv

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(PROJECT_FOLDER, "expense.csv")

def load_data():
    """Reads the CSV and RETURNS the list of expenses."""
    if not os.path.exists(filename):
        return [] 

    expenses = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except Exception as e:
        print(f"Error loading data: {e}")
        
    return expenses

def save_data(expenses):
    """Takes the list from main.py and SAVES it to the CSV."""
    if not expenses:
        return 
        
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["date", "category", "amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(expenses)
    except Exception as e:
        print(f"Error saving data: {e}")