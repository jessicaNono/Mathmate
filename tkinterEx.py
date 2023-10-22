import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
import math


class CalculatorWithGraph(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator with Graph Plotting, Equation Solving, and Trigonometry')
        self.geometry("800x650")
        self.create_widgets()

    def create_widgets(self):
        OPTIONS = [
            "+", "-", "*", "÷", "^", "√", "%", "sin", "cos", "tan"
        ]

        self.operation = tk.StringVar(self)
        self.operation.set(OPTIONS[0])
        self.var = tk.StringVar()
        self.var.set('')
        self.memory = 0
        self.num1_var = tk.StringVar()

        ttk.Label(self, text="Number 1:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ttk.Entry(self, textvariable=self.num1_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Operation:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        ttk.Combobox(self, values=OPTIONS, state="readonly", textvariable=self.operation,
                     postcommand=self.adapt_design).grid(row=1, column=1, padx=10, pady=10)

        self.number2_label = ttk.Label(self, text="Number 2:")
        self.number2_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.e5 = ttk.Entry(self)
        self.e5.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self, text="=", command=self.calculatrice, width=10).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="Result:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.e9 = ttk.Entry(self)
        self.e9.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(self, textvariable=self.var, foreground="red").grid(row=5, column=1, padx=10, pady=10)
        ttk.Label(self, text="Memory Functions:").grid(row=6, column=0, padx=10, pady=10, sticky='w')

        ttk.Button(self, text="MC", command=self.memory_clear, width=3).grid(row=7, column=0, padx=5, pady=10)
        ttk.Button(self, text="M+", command=self.memory_add, width=3).grid(row=7, column=1, padx=5, pady=10)
        ttk.Button(self, text="M-", command=self.memory_subtract, width=3).grid(row=7, column=2, padx=5, pady=10)
        ttk.Button(self, text="MR", command=self.memory_recall, width=3).grid(row=7, column=3, padx=5, pady=10)

        ttk.Label(self, text="Equation (in terms of x):").grid(row=8, column=0, padx=10, pady=10, sticky='w')
        self.equation_entry = ttk.Entry(self)
        self.equation_entry.grid(row=8, column=1, padx=10, pady=10, columnspan=2, sticky='we')

        ttk.Button(self, text="Solve", command=self.solve_equation).grid(row=8, column=3, padx=10, pady=10)
        ttk.Button(self, text="Plot Graph", command=self.plot_graph).grid(row=9, column=1, columnspan=2, pady=20)

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)

    def adapt_design(self):
        if self.operation.get() in ["√", "sin", "cos", "tan"]:
            self.e5.config(state=tk.DISABLED)
            self.number2_label.config(state=tk.DISABLED)
        else:
            self.e5.config(state=tk.NORMAL)
            self.number2_label.config(state=tk.NORMAL)

    def calculatrice(self):
        num1 = float(self.num1_var.get())
        op = self.operation.get()

        if op not in ["√", "sin", "cos", "tan"]:
            num2 = float(self.e5.get())
        else:
            num2 = 0  # Placeholder for unary operations

        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "÷":
                if num2 == 0:
                    self.var.set("Division by 0")
                    return
                result = num1 / num2
            elif op == "^":
                result = num1 ** num2
            elif op == "√":
                result = math.sqrt(num1)
            elif op == "%":
                result = num1 % num2
            elif op == "sin":
                result = math.sin(num1)
            elif op == "cos":
                result = math.cos(num1)
            elif op == "tan":
                result = math.tan(num1)
            else:
                self.var.set("Invalid Operation")
                return

            self.e9.delete(0, tk.END)
            self.e9.insert(10, result)
            self.var.set("")
        except ValueError:
            self.var.set("error")

    def memory_clear(self):
        self.memory = 0

    def memory_add(self):
        try:
            self.memory += float(self.e9.get())
        except ValueError:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.e9.get())
        except ValueError:
            pass

    def memory_recall(self):
        self.e9.delete(0, tk.END)
        self.e9.insert(10, self.memory)

    def solve_equation(self):
        equation = self.equation_entry.get().replace('^', '**')
        x = sp.symbols('x')
        try:
            if not equation:
                raise ValueError("Please enter an equation.")
            solution = sp.solve(equation, x)
            messagebox.showinfo('Solution', f'The solutions are: {solution}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    
    def plot_graph(self):
        equation = self.equation_entry.get().replace('^', '**')
        if any(trig in equation for trig in ['sin', 'cos', 'tan']):
            x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        else:
            x = np.linspace(-10, 10, 400)
        y = eval(equation)

        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y)

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        # Adjusting the height of the GUI window during plotting
        current_width = self.winfo_width()
        current_height = self.winfo_height()
        increase_amount = 400  # amount by which to increase the height
        new_height = current_height + increase_amount
        self.geometry(f"{current_width}x{new_height}")

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")
        canvas.draw()



if __name__ == "__main__":
    app = CalculatorWithGraph()
    app.mainloop()
