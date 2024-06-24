import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import random

# Define stages with minimum and maximum durations in days
stages = [
    {"stage": "Process 1.", "min_duration": 0, "max_duration": 1},
    {"stage": "Process 2.", "min_duration": 2, "max_duration": 3},
    {"stage": "Process 3.", "min_duration": 3, "max_duration": 4},
    {"stage": "Process 4.", "min_duration": 4, "max_duration": 5},
    {"stage": "Process 5.", "min_duration": 5, "max_duration": 6},
    {"stage": "Process 6.", "min_duration": 6, "max_duration": 7},
]

def process_status(start_date_str, current_date_str):
    # Convert start_date and current_date strings to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    
    # Calculate the number of days elapsed
    elapsed_days = (current_date - start_date).days
    
    # Determine current stage
    total_days = 0
    current_stage = None
    for stage_info in stages:
        stage_duration = random.randint(stage_info["min_duration"], stage_info["max_duration"])
        total_days += stage_duration
        if elapsed_days < total_days:
            current_stage = stage_info["stage"]
            break
    
    # Calculate predicted end date
    total_duration = sum(random.randint(stage_info["min_duration"], stage_info["max_duration"]) for stage_info in stages)
    predicted_end_date = start_date + timedelta(days=total_duration)
    
    return current_stage, predicted_end_date.strftime("%Y-%m-%d")

def on_submit():
    start_date_input = start_date_entry.get()
    current_date_input = current_date_entry.get()
    try:
        current_stage, predicted_end_date = process_status(start_date_input, current_date_input)
        result_label.config(text=f"Current Stage: {current_stage}\nPredicted End Date: {predicted_end_date}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main application window
root = tk.Tk()
root.title("Process Status Checker")

# Create and place the widgets
tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Current Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
current_date_entry = tk.Entry(root)
current_date_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
