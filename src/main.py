import tkinter as tk
import functions as f

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

    if str(key).isdigit():
        if len(expression_args) > 0 and str(expression_args[-1]).replace(".", "", 1).isdigit():
            expression_args[-1] = str(expression_args[-1]) + str(key)
        else:
            expression_args.append(str(key))

    elif key == ".":
        if len(expression_args) == 0:
            expression += "0"
            expression_args.append("0.")
        elif str(expression_args[-1]).replace(".", "", 1).isdigit():
            if "." not in str(expression_args[-1]):
                expression_args[-1] = str(expression_args[-1]) + "."
        else:
            expression_args.append("0.")

    elif key in ["+", "-", "*", "/"]:
        if len(expression_args) == 0:
            return

        if expression_args[-1] in ["+", "-", "*", "/"]:
            expression_args[-1] = key
            expression = expression[:-2] + key
            val.set(expression)
        else:
            expression_args.append(key)


def clear():
    global expression
    expression = ""
    val.set("")
    expression_args.clear()


def backspace():
    global expression

    if len(expression) > 0:
        expression = expression[:-1]
        val.set(expression)

    if len(expression_args) > 0:
        last = str(expression_args[-1])

        if len(last) > 1 and last not in ["+", "-", "*", "/"]:
            expression_args[-1] = last[:-1]
        else:
            expression_args.pop()


def percent():
    global expression

    if len(expression_args) == 0:
        return

    if expression_args[-1] in ["+", "-", "*", "/"]:
        return

    value = float(expression_args[-1]) / 100
    expression_args[-1] = str(value)

    parts = expression.split()
    expression = expression[:-len(str(parts[-1]))] + str(value) if parts else str(value)
    val.set(expression)


def calculate():
    global expression

    try:
        if len(expression_args) == 0:
            return

        if expression_args[-1] in ["+", "-", "*", "/"]:
            return

        result = f.calculate(expression_args)[0]

        if result == int(result):
            result = int(result)

        expression = str(result)
        expression_args.clear()
        expression_args.append(str(result))
        val.set(expression)

    except ZeroDivisionError:
        val.set("Sıfıra bölünmez")
        expression = ""
        expression_args.clear()

    except Exception:
        val.set("Hata")
        expression = ""
        expression_args.clear()


input_field = tk.Entry(
    window,
    textvariable=val,
    justify="right",
    font=("Arial", 18, "bold")
)
input_field.config(state="readonly")
input_field.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(6):
    window.rowconfigure(i, weight=1, uniform="row")


buttons = [
    ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
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
        action = percent
    else:
        action = lambda t=text: press(t)

    tk.Button(
        window,
        text=text,
        command=action,
        font=("Arial", 14)
    ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)


window.mainloop()