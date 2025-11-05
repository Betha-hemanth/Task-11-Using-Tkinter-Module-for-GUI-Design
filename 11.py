import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = a / b
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid numbers!")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

button_add = tk.Button(frame, text="+", width=5, command=lambda: calculate("+"))
button_add.grid(row=0, column=0)
button_sub = tk.Button(frame, text="-", width=5, command=lambda: calculate("-"))
button_sub.grid(row=0, column=1)
button_mul = tk.Button(frame, text="*", width=5, command=lambda: calculate("*"))
button_mul.grid(row=0, column=2)
button_div = tk.Button(frame, text="/", width=5, command=lambda: calculate("/"))
button_div.grid(row=0, column=3)

label_result = tk.Label(root, text="Result", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()

