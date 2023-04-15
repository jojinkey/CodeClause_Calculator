import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry widget to display input/output
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons for calculator
        self.buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "C", "/",
            "00", "sq", 
            "AC",
            "<--","sqrt"
        ]

        # Create and display buttons on the GUI
        row = 1
        col = 0
        for button in self.buttons:
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, padx=20, pady=10, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create button to calculate result
        equal_button = tk.Button(master, text="=", padx=20, pady=10, command=self.calculate)
        equal_button.grid(row=5, column=2)

    # Method to handle button clicks
    def button_click(self, symbol):
        if symbol == "C":
            self.entry.delete(0, tk.END)
        elif symbol == "AC":
            self.entry.delete(0, tk.END)
        elif symbol == "sq":
            current = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current**2)
        elif symbol == "sqrt":
            current = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, math.sqrt(current))
        elif symbol == "<--":
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(current) + str(symbol))

    # Method to evaluate input expression and display result
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

# Create the GUI window and Calculator object
root = tk.Tk()
calculator = Calculator(root)

# Run the main loop for the GUI
root.mainloop()
