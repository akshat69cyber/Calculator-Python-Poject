import tkinter as tk

# main window
root = tk.Tk()
root.title("Calculator")

# entry widget
entry_box = tk.Entry(root, width=25, borderwidth=4, font=("Arial", 14))
entry_box.grid(row=0, column=0, columnspan=4)

expression = ""

# function to add value in entry
def add_to_expression(value):
    global expression
    expression += str(value)
    entry_box.delete(0, tk.END)
    entry_box.insert(0, expression)

# function to clear entry
def clear_screen():
    global expression
    expression = ""
    entry_box.delete(0, tk.END)

# function to calculate
def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_box.delete(0, tk.END)
        entry_box.insert(0, result)
        expression = result
    except:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")
        expression = ""

# list of buttons (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# create buttons using loop
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: add_to_expression(t)).grid(row=row, column=col)

# clear button
tk.Button(root, text="C", width=22, height=2, command=clear_screen).grid(row=5, column=0, columnspan=4)

# run the main loop
root.mainloop()
