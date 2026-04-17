"""GUI CLACULATOR
A fully functional calculator with Tkinter"""

import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        #Stor Calculation
        self.current = ""
        self.result_var = tk.StringVar()
        
        self.create_display()
        self.create_button()
        
    def create_display(self):
        """Create claculator display screen"""
        display = tk.Entry(
            self.window,
            textvariable=self.result_var,
            font=("Arial", 20),
            justify="right",
            bg="white",
            state="readonly"
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def create_button(self):
        """Create all calculation buttons"""
        #Button layout: (text, row, column)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)  #Clear button spans 4 columns
        ]
        
        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            
            button = tk.Button(
                self.window,
                text=text,
                bg="#7C7C7C",
                fg="white",
                font=("Arial", 14),
                command= lambda t=text: self.button_click(t)
            )
            button.grid(row=row, column=col, columnspan=colspan,
                        padx=5, pady=5, sticky="nsew")
            
        #Configure grid weights
        for i in range (6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range (4):
            self.window.grid_columnconfigure(i, weight=1)
    def button_click(self, value):
        """Handle button clicks"""
        if value == "C":
            self.current = ""
            self.result_var.set("")
        elif value == "=":
            try:
                #Replace display symbols with Python operators
                expression = self.current.replace('x', '*').replace('/', '/')
                result = eval(expression)
                self.result_var.set(result)
                self.current =str(result)
            except Exception:
                self.result_var.set("Error")
                self.current = ""
        else:
            self.current += value
            self.result_var.set(self.current)
            
    def run(self):
        self.window.mainloop()
        
#Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()