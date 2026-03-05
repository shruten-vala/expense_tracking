🚀 Personal Expense Tracker
<p align="center"> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=26&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Personal+Expense+Tracker;Python+CLI+Application;Track+and+Manage+Your+Expenses+Effortlessly" /> </p> <p align="center">








</p>

📖 About the Project

A modular command-line application built in Python that allows users to track daily expenses efficiently.

This tool enables you to:

Log expenses

Analyze category-wise spending

Filter expense records

Maintain persistent data storage using CSV

All functionality is implemented with clean modular architecture, making the code easy to maintain and extend.


✨ Features

✔ Add new expenses with validation
✔ View all expense records
✔ Filter expenses by category
✔ Category-wise spending breakdown
✔ Delete expense records
✔ Persistent storage using CSV


🎥 CLI Demo
Example terminal interaction:
==== Personal Expense Tracker ====

1. Add Expense
2. View All Expenses
3. Filter by Category
4. Category Breakdown
5. Delete Expense
6. Exit
![Demo](demo.gif)


expense-tracker/
│
├── main.py
├── services.py
├── storage.py
├── validators.py
├── display.py
├── expense.csv
└── README.md

🧩 Module Responsibilities

| Module          | Responsibility                           |
| --------------- | ---------------------------------------- |
| `main.py`       | Application entry point and menu routing |
| `services.py`   | Business logic and calculations          |
| `storage.py`    | Reading and writing expense data         |
| `validators.py` | Input validation and interaction         |
| `display.py`    | Formatting tables and CLI output         |


⚙️ Installation

Clone the repository
git clone https://github.com/YOUR_USERNAME/expense-tracker.git

Navigate into the project
cd expense-tracker

Run the application
python3 main.py


🏗 Application Flow
User Input
    │
    ▼
validators.py
    │
    ▼
main.py (Menu Routing)
    │
    ▼
services.py (Business Logic)
    │
    ▼
storage.py (CSV Handling)
    │
    ▼
expense.csv

<details>
<summary>📌 Click to see implementation details</summary>

### Architecture Explanation

- **validators.py** → handles user input validation  
- **services.py** → contains business logic  
- **storage.py** → reads and writes CSV data  
- **display.py** → formats terminal output  

### Why Modular Design?

This architecture improves:

- maintainability
- readability
- scalability

</details>


🧠 Concepts Practiced

This project demonstrates:

Python modular programming

CLI application design

CSV file handling

Input validation

Data filtering and aggregation

Clean separation of concerns


🔮 Future Improvements

Data visualization

Monthly reports

SQLite database support

GUI version

Web dashboard


📊 GitHub Stats

<p align="center"> <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=tokyonight" /> <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=tokyonight" /> </p>

⭐ Support

If you found this project helpful, consider starring the repository ⭐




