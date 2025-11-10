import tkinter as tk
from tkinter import messagebox
import random, string


# Password generation function

def genPassword():
    # Open and read the noun list
    with open("noun_list_1000.txt", "r") as file:
        nouns = [line.strip() for line in file]

    # Get 2 indexes for words
    first_noun_index = random.randint(0, len(nouns)-1)
    second_noun_index = random.randint(0, len(nouns)-1)

    # Make sure they aren't repeats
    while first_noun_index == second_noun_index:
        second_noun_index = random.randint(0, len(nouns)-1)

    # Give nouns word values
    first_noun = nouns[first_noun_index]
    second_noun = nouns[second_noun_index]

    # Get 3 digit number for password
    pass_number = random.randint(100, 999)

    special_char_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_"]
    pass_char = random.choice(special_char_list)

    password = first_noun + second_noun + str(pass_number) + pass_char
    return password


def strengthCheck(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"
    
# Tkinter GUI Functions

def show_password():
    password = genPassword()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard!")

def check_strength():
    pwd = strength_entry.get()
    if not pwd:
        messagebox.showwarning("No password", "Please enter a password to check.")
        return
    result = strengthCheck(pwd)
    messagebox.showinfo("Password strength", f"Strength: {result}")


# Tkinter GUI Setup

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Main frame
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(expand=True)

# Click to get password Label
label = tk.Label(frame, text="Click the button to generate a password:", 
                 font=("Helvetica", 14), bg="#ffffff")
label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Entry to display password
password_entry = tk.Entry(frame, width=40, font=("Courier", 12))
password_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Generate button
generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12, "bold"),
                            bg="#4CAF50", fg="white", padx=10, pady=5, command=show_password)
generate_button.grid(row=2, column=0, pady=15, sticky="ew", padx=(0, 10))

# Copy button
copy_button = tk.Button(frame, text="Copy to Clipboard", font=("Helvetica", 12, "bold"),
                        bg="#2196F3", fg="white", padx=10, pady=5, command=copy_to_clipboard)
copy_button.grid(row=2, column=1, pady=15, sticky="ew", padx=(10, 0))

#Password strength label
label = tk.Label(frame, text="Enter password to check strength:", 
                 font=("Helvetica", 14), bg="#ffffff")
label.grid(row=3, column=0, columnspan=2, pady=(0, 15))

#Password strength checker
strength_entry = tk.Entry(frame, width=40, font=("Courier", 12), show="*")
strength_entry.grid(row=4, column=0, columnspan=2, pady=5)

#Password strength button
check_button = tk.Button(frame, text="Check Strength", font=("Helvetica", 12, "bold"),
                         bg="#FF9800", fg="white", padx=10, pady=5, command=check_strength)
check_button.grid(row=5, column=0, columnspan=2, pady=(5, 0), sticky="ew")

# Expand columns equally
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

root.mainloop()