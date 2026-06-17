import tkinter as tk
import math
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.configure(bg="#1E1E1E")
expression = ""
angle_mode = "DEG"

equation = tk.StringVar()
equation.set("0")

mode_text = tk.StringVar()
mode_text.set("DEG")

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression.replace('^', '**').replace('π', 'math.pi').replace('e', 'math.e')))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("0")

def backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        equation.set("0")
    else:
        equation.set(expression)

def toggle_mode():
    global angle_mode
    if angle_mode == "DEG":
        angle_mode = "RAD"
    else:
        angle_mode = "DEG"
    mode_text.set(angle_mode)

def press_sin():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        if angle_mode == "DEG":
            val = math.radians(val)
        res = math.sin(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def press_cos():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        if angle_mode == "DEG":
            val = math.radians(val)
        res = math.cos(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def press_tan():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        if angle_mode == "DEG":
            val = math.radians(val)
        res = math.tan(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def deg_to_rad():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        res = math.radians(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def rad_to_deg():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        res = math.degrees(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def press_sqrt():
    global expression
    try:
        val = float(eval(expression.replace('π', 'math.pi').replace('e', 'math.e')))
        res = math.sqrt(val)
        expression = str(res)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def press_pi():
    global expression
    expression = expression + "π"
    equation.set(expression)

display_frame = tk.Frame(root, bg="#121212")
display_frame.pack(fill="both", expand=True, padx=10, pady=10)

mode_label = tk.Label(
    display_frame,
    textvariable=mode_text,
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="#FF9F0A"
)
mode_label.pack(anchor="nw", padx=10, pady=5)

display_entry = tk.Label(
    display_frame,
    textvariable=equation,
    font=("Arial", 28, "bold"),
    bg="#121212",
    fg="#FFFFFF",
    anchor="e"
)
display_entry.pack(fill="both", expand=True, padx=10, pady=10)

keypad_frame = tk.Frame(root, bg="#1E1E1E")
keypad_frame.pack(fill="both", expand=True, padx=10, pady=10)

for i in range(5):
    keypad_frame.grid_columnconfigure(i, weight=1)
for i in range(6):
    keypad_frame.grid_rowconfigure(i, weight=1)

buttons = [
    ("C", 0, 0, clear),
    ("⌫", 0, 1, backspace),
    ("(", 0, 2, lambda: press("(")),
    (")", 0, 3, lambda: press(")")),
    ("DEG/RAD", 0, 4, toggle_mode),
    
    ("sin", 1, 0, press_sin),
    ("cos", 1, 1, press_cos),
    ("tan", 1, 2, press_tan),
    ("deg→rad", 1, 3, deg_to_rad),
    ("rad→deg", 1, 4, rad_to_deg),
    
    ("7", 2, 0, lambda: press("7")),
    ("8", 2, 1, lambda: press("8")),
    ("9", 2, 2, lambda: press("9")),
    ("/", 2, 3, lambda: press("/")),
    ("sqrt", 2, 4, press_sqrt),
    
    ("4", 3, 0, lambda: press("4")),
    ("5", 3, 1, lambda: press("5")),
    ("6", 3, 2, lambda: press("6")),
    ("*", 3, 3, lambda: press("*")),
    ("^", 3, 4, lambda: press("^")),
    
    ("1", 4, 0, lambda: press("1")),
    ("2", 4, 1, lambda: press("2")),
    ("3", 4, 2, lambda: press("3")),
    ("-", 4, 3, lambda: press("-")),
    ("π", 4, 4, press_pi),
    
    ("0", 5, 0, lambda: press("0")),
    (".", 5, 1, lambda: press(".")),
    ("+", 5, 2, lambda: press("+")),
    ("=", 5, 3, equalpress)
]

for text, r, c, cmd in buttons:
    if text == "0":
        btn = tk.Button(keypad_frame, text=text, font=("Arial", 14, "bold"), bg="#2C2C2E", fg="#FFFFFF", bd=0, activebackground="#3A3A3C", activeforeground="#FFFFFF", command=cmd)
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
    elif text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        btn = tk.Button(keypad_frame, text=text, font=("Arial", 14, "bold"), bg="#2C2C2E", fg="#FFFFFF", bd=0, activebackground="#3A3A3C", activeforeground="#FFFFFF", command=cmd)
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
    elif text in ["+", "-", "*", "/", "="]:
        bg_color = "#FF9F0A"
        active_bg = "#FFB340"
        if text == "=":
            btn = tk.Button(keypad_frame, text=text, font=("Arial", 14, "bold"), bg=bg_color, fg="#FFFFFF", bd=0, activebackground=active_bg, activeforeground="#FFFFFF", command=cmd)
            btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=3, pady=3)
        else:
            btn = tk.Button(keypad_frame, text=text, font=("Arial", 14, "bold"), bg=bg_color, fg="#FFFFFF", bd=0, activebackground=active_bg, activeforeground="#FFFFFF", command=cmd)
            btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
    elif text in ["C", "⌫"]:
        btn = tk.Button(keypad_frame, text=text, font=("Arial", 14, "bold"), bg="#48484A", fg="#FF453A", bd=0, activebackground="#545456", activeforeground="#FF453A", command=cmd)
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
    else:
        btn = tk.Button(keypad_frame, text=text, font=("Arial", 12, "bold"), bg="#3A3A3C", fg="#F2F2F7", bd=0, activebackground="#48484A", activeforeground="#F2F2F7", command=cmd)
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

if __name__ == "__main__":
    root.mainloop()
