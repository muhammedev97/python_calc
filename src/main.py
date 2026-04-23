import tkinter as tk

window = tk.Tk()
window.title("Zaur & Muhammed Kalkulyator")
window.geometry("300x400")
window.resizable(False, False)

val = tk.StringVar()
expression = ""
expression_args = []

def press(key):
    global expression
    expression += str(key)
    val.set(expression)
    expression_args.append(key)
def clear():
    global expression
    expression = ""
    val.set("")
    expression_args.clear()

def backspace():
    global expression
    expression = expression[:-1]
    val.set(expression)
    expression_args.pop()

def calculate():
    global expression_args
    # try:
    #     result = str(eval(expression))
    #     val.set(result)
    #     expression = result
    # except:
    #     val.set("Error")
    #     expression = ""

    print(expression_args)

input_field = tk.Entry(window, textvariable=val, justify="right", font=("Arial", 18, "bold"))
input_field.config(state="readonly")
input_field.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(6):  
    window.rowconfigure(i, weight=1, uniform="row")

buttons = [
    ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    elif text == "CE":
        action = clear
    elif text == "⌫":
        action = backspace
    elif text == "%":
        action = lambda: press("/100")
    else:
        action = lambda t=text: press(t)

    tk.Button(window, text=text, command=action, font=("Arial", 14))\
        .grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

tk.Button(window, text="=", command=calculate, font=("Arial", 14))\
    .grid(row=5, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)

window.mainloop()