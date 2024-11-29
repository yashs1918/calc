import tkinter as tk
from tkinter import messagebox

def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the current equation
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons and add to the window
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 18), bg="lightgray",
                       command=lambda text=button_text: click(text))
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
