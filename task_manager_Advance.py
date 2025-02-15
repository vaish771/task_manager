import tkinter as tk
from tkinter import messagebox
import json
import os

# File for storing tasks
TASK_FILE = "tasks.json"

# Load tasks from JSON
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            loaded_tasks = json.load(file)
            # Ensure all tasks have "time"
            for task in loaded_tasks:
                task.setdefault("time", "00:00")  # Assign default if missing
            return loaded_tasks
    return []

# Save tasks to JSON
def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Update Task List Display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task.get("completed", False) else "❌"
        time = task.get("time", "00:00")  # Default time if missing
        task_listbox.insert(tk.END, f"{status} {time} - {task['task']}")

# Add Task
def add_task():
    task_text = task_entry.get()
    task_time = time_entry.get()
    if not task_text.strip():
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks.append({"task": task_text, "time": task_time, "completed": False})
    save_tasks()
    update_task_list()
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

# Delete Task
def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected!")
        return
    index = selected[0]
    del tasks[index]
    save_tasks()
    update_task_list()

# Mark Task as Completed
def complete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected!")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    save_tasks()
    update_task_list()

# Clear All Tasks
def clear_tasks():
    tasks.clear()
    save_tasks()
    update_task_list()

# Initialize Tkinter Window
root = tk.Tk()
root.title("Task Manager")
root.geometry("500x450")
root.configure(bg="#f4f4f4")

# Task Entry
tk.Label(root, text="Task:", font=("Arial", 12), bg="#f4f4f4").pack(pady=5)
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=5)

# Time Entry
tk.Label(root, text="Time (HH:MM):", font=("Arial", 12), bg="#f4f4f4").pack(pady=5)
time_entry = tk.Entry(root, width=15, font=("Arial", 12))
time_entry.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", font=("Arial", 10), command=add_task, width=12, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete Task", font=("Arial", 10), command=delete_task, width=12, bg="#f44336", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Mark Completed", font=("Arial", 10), command=complete_task, width=15, bg="#008CBA", fg="white").grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Clear All", font=("Arial", 10), command=clear_tasks, width=12, bg="#FF9800", fg="white").grid(row=0, column=3, padx=5, pady=5)

# Load Tasks on Start
tasks = load_tasks()
update_task_list()

# Run Tkinter Loop
root.mainloop()
