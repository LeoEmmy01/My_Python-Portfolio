"""PERSONAL EXPENSE TRACKER
Track your daily spending with GUI"""

import tkinter as tk
from tkinter import messagebox
import json
import os

class ExpenseTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Expense Tracker")
        self.window.geometry("600x500")
        
        #Data storage
        self.expenses = []
        self.load_data()
        
        self.create_widgets()
        self.refresh_list()
        
    def load_data(self):
        """Load expense from file"""
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
    
    def save_data(self):
        """Save expenses to file"""
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)
            
    def create_widgets(self):
        """Create all GUI widgets"""
        #Title
        title = tk.Label(
            self.window,
            text="Personal Expenses Tracker", 
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)
        
        #Input frame
        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=10)
        
        #Desciption input
        tk.Label(input_frame, text="Description:").grid(row=0, column=0, padx=5)
        self.desc_entry = tk.Entry(input_frame, width=20)
        self.desc_entry.grid(row=0, column=1, padx=5)
        
        #Amount Input
        tk.Label(input_frame, text="Amount($): ").grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=0, column=3, padx=5)
        
        #Add Button
        add_btn = tk.Button(
            input_frame,
            text="Add Expense",
            command=self.add_expenses,
            bg="green",
            fg="white"
        )
        add_btn.grid(row=0, column=4, padx=10)
        
        #Expense list
        self.listbox = tk.Listbox(self.window, width=70, height=15)
        self.listbox.pack(pady=10)
        
        #Button frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)
        
        #Delete Button
        delete_btn = tk.Button(
            button_frame,
            text="Delete Selected",
            command=self.delete_expense,
            bg="red",
            fg="white"
        )
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        #ToTal Label
        self.total_label = tk.Label(
            self.window,
            text="Total: $0.00",
            font=("Arial", 14, "bold")
        )
        self.total_label.pack(pady=10)
    def add_expenses(self):
        """Add a new expense"""
        description = self.desc_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        
        #Validation
        if not description:
            messagebox.showerror("Error", "Please enter a description")
            return
        
        try:
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return
        
        #Add Expense
        expense = {
            "description": description,
            "amount": amount
        }
        self.expenses.append(expense)
        self.save_data()
        self.refresh_list()
        
        # Clear inputs
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"Added: {description} - ${amount:.2f}")
        
    def delete_expense(self):
        """Delete selected expense"""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an expense to delete")
            return
        
        #Confirm deletion
        if messagebox.askyesno("Confirm", "Delete the expense?"):
            index = selection[0]
            deleted = self.expenses.pop(index)
            self.save_data()
            self.refresh_list()
            messagebox.showinfo("Deleted", f"Deleted: {deleted['description']}")
            
    def refresh_list(self):
        """Refresh the expense list display"""
        self.listbox.delete(0, tk.END)
        
        total = 0
        for expense in self.expenses:
            desc = expense["description"]
            amount = expense["amount"]
            self.listbox.insert(tk.END, f"{desc}: ${amount:.2f}")
            total += amount
            
        self.total_label.config(text=f"Total: ${total:.2f}")
    def run(self):
        self.window.mainloop()
        
#Run the app
if __name__ == "__main__":
    app = ExpenseTracker()
    
    app.run()