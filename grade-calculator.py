import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        marks_input = entry.get().strip()
        name = name_entry.get().strip()

        print(f"DEBUG - name: '{name}' | marks_input: '{marks_input}'")

        if name == "":
            result.set("Enter student name")
            return

        if marks_input == "":
            result.set("Enter marks")
            return

        # Convert to float
        marks = float(marks_input)

        # Grade Logic
        if marks < 0 or marks > 100:
            grade = "Unknown"
        elif marks >= 90:
            grade = "Grade A"
        elif marks >= 70:
            grade = "Grade B"
        elif marks >= 50:
            grade = "Grade C"
        elif marks >= 35:
            grade = "Grade D"
        else:
            grade = "Fail"

        result.set(f"{name} scored {grade}")

        with open("grades.txt", "a") as file:
           file.write(f"{name} - {marks} -> {grade}\n")

        messagebox.showinfo("Saved", f"Result saved for {name}.")

    except ValueError as e:
        print("DEBUG - Exception:", e)
        result.set("Invalid input")

def clear_fields():
    name_entry.delete(0, tk.END)
    entry.delete(0, tk.END)
    result.set("")

def exit_app():
    root.destroy()

# GUI Window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("350x400")
root.config(bg="#f0f0f0")

# Student Name
tk.Label(root, text="Enter Student Name:", bg="#f0f0f0").pack(pady=5)
name_entry = tk.Entry(root, width=25, font=("Arial", 12))
name_entry.pack()

# Marks Input
tk.Label(root, text="Enter Marks (0–100):", bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack()

# Result Display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue", bg="#f0f0f0").pack(pady=10)

# Buttons
tk.Button(root, text="Check Grade", command=calculate_grade).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, fg="white", bg="red").pack(pady=5)

# Start GUI
root.mainloop()
