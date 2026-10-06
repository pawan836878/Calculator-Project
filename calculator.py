import tkinter as tk

# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    bg="#252526",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(fill="both", padx=15, pady=20, ipady=15)


def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        clear()
        display.insert(0, str(result))
    except:
        clear()
        display.insert(0, "Error")


# Button layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "⌫"]
]


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=10)

    for button in row:

        if button == "C":
            command = clear
            color = "#d9534f"

        elif button == "=":
            command = calculate
            color = "#28a745"

        elif button == "⌫":
            command = backspace
            color = "#f0ad4e"

        elif button in "+-*/":
            command = lambda x=button: click(x)
            color = "#007acc"

        else:
            command = lambda x=button: click(x)
            color = "#333333"

        tk.Button(
            frame,
            text=button,
            command=command,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            bd=0
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=5,
            pady=5
        )


root.mainloop()
