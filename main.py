import tkinter as tk
from tkinter import ttk
import spacy

class ExpenseManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Manager")
        self.geometry("400x300")
        self.expenses = []

        # Load spaCy model for English language
        self.nlp = spacy.load("en_core_web_sm")

        self.create_widgets()

    def create_widgets(self):
        # Expense Input Section
        expense_frame = ttk.LabelFrame(self, text="Expense Input")
        expense_frame.pack(padx=20, pady=20)

        date_label = ttk.Label(expense_frame, text="Date:")
        date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(expense_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        amount_label = ttk.Label(expense_frame, text="Amount:")
        amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(expense_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        description_label = ttk.Label(expense_frame, text="Description:")
        description_label.grid(row=2, column=0, padx=5, pady=5)
        self.description_entry = ttk.Entry(expense_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = ttk.Button(expense_frame, text="Add Expense", command=self.add_expense)
        add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Expense Analysis Section
        analysis_frame = ttk.LabelFrame(self, text="Expense Analysis")
        analysis_frame.pack(padx=20, pady=20)

        analyze_button = ttk.Button(analysis_frame, text="Analyze Expenses", command=self.analyze_expenses)
        analyze_button.pack(padx=5, pady=5)

        self.result_text = tk.Text(analysis_frame, height=10, width=40)
        self.result_text.pack(padx=5, pady=5)

    def add_expense(self):
        date = self.date_entry.get()
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()

        expense = {
            "date": date,
            "amount": amount,
            "description": description
        }

        self.expenses.append(expense)

        self.date_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def analyze_expenses(self):
        if not self.expenses:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "No expenses to analyze.")
            return

        self.result_text.delete(1.0, tk.END)

        self.categorize_expenses()
        self.generate_insights()

    def categorize_expenses(self):
        self.result_text.insert(tk.END, "Categorized Expenses:\n")

        for expense in self.expenses:
            description = expense["description"]
            doc = self.nlp(description)

            # Customize the categorization logic based on your requirements
            category = "Other"
            for token in doc:
                if token.text in ["grocery", "food", "dining"]:
                    category = "Food"
                elif token.text in ["taxi", "car", "transport"]:
                    category = "Transportation"
                elif token.text in ["rent", "mortgage", "utilities"]:
                    category = "Housing"
                elif token.text in ["movies", "games", "entertainment"]:
                    category = "Entertainment"
                elif token.text in ["clothes", "electronics"]:
                    category = "Shopping"

            expense["category"] = category
            self.result_text.insert(tk.END, f"Description: {description}, Category: {category}\n")

    def generate_insights(self):
        self.result_text.insert(tk.END, "\nExpense Insights:\n")

        # Add your expense analysis and insights generation logic here

if __name__ == "__main__":
    app = ExpenseManagerApp()
    app.mainloop()
