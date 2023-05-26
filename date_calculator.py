import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def calculate_weeks_and_days():
    date_a = date_entry_a.get_date()
    date_b = date_entry_b.get_date() if date_entry_b.get() else datetime.datetime.now().date()
    days_difference = (date_b - date_a).days
    weeks = days_difference // 7
    days = days_difference % 7
    result_label.config(text=f"Weeks: {weeks}\nDays: {days}")

root = tk.Tk()
root.title("Date Calculator")

# Date A selection
label_a = ttk.Label(root, text="Date A:")
label_a.grid(row=0, column=0, padx=10, pady=10)

date_entry_a = DateEntry(root, width=12, background='darkblue',
                         foreground='white', borderwidth=2)
date_entry_a.grid(row=0, column=1, padx=10, pady=10)

# Date B selection
label_b = ttk.Label(root, text="Date B:")
label_b.grid(row=1, column=0, padx=10, pady=10)

date_entry_b = DateEntry(root, width=12, background='darkblue',
                         foreground='white', borderwidth=2)
date_entry_b.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_weeks_and_days)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Calculate the position to center the window
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
