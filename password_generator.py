import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ---------------- #

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length must be at least 4!"
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number!"
        )
        return

    chars = ""

    if letters_var.get():
        chars += string.ascii_letters

    if numbers_var.get():
        chars += string.digits

    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning(
            "Warning",
            "Select at least one character type!"
        )
        return

    password = "".join(
        random.choice(chars)
        for _ in range(length)
    )

    password_var.set(password)


def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

        messagebox.showinfo(
            "Success",
            "Password copied to clipboard!"
        )


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("700x550")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

# ---------------- Title ---------------- #

title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#1E1E1E"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Generate Strong & Secure Passwords",
    font=("Segoe UI", 11),
    fg="#B0B0B0",
    bg="#1E1E1E"
)
subtitle.pack()

# ---------------- Main Frame ---------------- #

frame = tk.Frame(
    root,
    bg="#2C2C2C",
    padx=30,
    pady=30
)
frame.pack(pady=20)

# Password Length

tk.Label(
    frame,
    text="Password Length",
    font=("Segoe UI", 13, "bold"),
    fg="white",
    bg="#2C2C2C"
).pack(anchor="w")

length_entry = tk.Entry(
    frame,
    font=("Segoe UI", 14),
    justify="center",
    width=10
)
length_entry.pack(pady=10)
length_entry.insert(0, "12")

# ---------------- Options ---------------- #

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    frame,
    text="Include Letters",
    variable=letters_var,
    bg="#2C2C2C",
    fg="white",
    activebackground="#2C2C2C",
    activeforeground="white",
    selectcolor="#2C2C2C",
    font=("Segoe UI", 12)
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Include Numbers",
    variable=numbers_var,
    bg="#2C2C2C",
    fg="white",
    activebackground="#2C2C2C",
    activeforeground="white",
    selectcolor="#2C2C2C",
    font=("Segoe UI", 12)
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Include Symbols",
    variable=symbols_var,
    bg="#2C2C2C",
    fg="white",
    activebackground="#2C2C2C",
    activeforeground="white",
    selectcolor="#2C2C2C",
    font=("Segoe UI", 12)
).pack(anchor="w")

# ---------------- Buttons ---------------- #

generate_btn = tk.Button(
    frame,
    text="Generate Password",
    command=generate_password,
    font=("Segoe UI", 12, "bold"),
    bg="#0078D7",
    fg="white",
    width=20,
    height=2,
    cursor="hand2"
)
generate_btn.pack(pady=20)

# ---------------- Password Display ---------------- #

password_var = tk.StringVar()

password_display = tk.Label(
    frame,
    textvariable=password_var,
    font=("Consolas", 22, "bold"),
    bg="white",
    fg="#0078D7",
    width=28,
    height=2,
    relief="ridge",
    bd=3
)
password_display.pack(pady=15)

# ---------------- Copy Button ---------------- #

copy_btn = tk.Button(
    frame,
    text="📋 Copy Password",
    command=copy_password,
    font=("Segoe UI", 12, "bold"),
    bg="#16A085",
    fg="white",
    width=20,
    height=2,
    cursor="hand2"
)
copy_btn.pack()

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="Secure • Fast • Modern",
    font=("Segoe UI", 10),
    fg="#B0B0B0",
    bg="#1E1E1E"
)
footer.pack(side="bottom", pady=15)

root.mainloop()