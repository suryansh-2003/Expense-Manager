# Expense Manager

Expense Manager is a Python-based application that helps you keep track of your expenses and provides categorization and analysis features. It allows you to add expenses with details like date, amount, and description, and then categorizes them based on the description using spaCy. The application also provides basic expense analysis and insights.


## Features

- Add expenses with date, amount, and description
- Categorize expenses based on description using spaCy
- Generate basic expense analysis and insights
- Simple and intuitive user interface

## Requirements

- Python 3.x
- spaCy library and the English language model (`en_core_web_sm`)

## Installation

1. Clone the repository
2. Install the required dependencies:
    pip install spacy
    python -m spacy download en_core_web_sm 


## Usage
1. Navigate to the project directory:
    cd expense-manager
2. Run the application:
    python expense_manager.py
3. Enter the expense details in the provided fields and click "Add Expense" to add an expense.

4. Click "Analyze Expenses" to categorize and analyze the expenses.

5. View the categorized expenses and generated insights in the application window.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.

## Acknowledgements


Tkinter - Python GUI library
spaCy - Natural Language Processing library
