import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("📝 Ekta's To-Do List 💖")
root.geometry("400x500")
root.configure(bg="#ffe6f0")  # light pink background

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Enter a task first!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Oops!", "No task selected!")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index] = "✔️ " + tasks[index]
        update_listbox()
    except:
        messagebox.showwarning("Oops!", "No task selected!")

# GUI elements
label = tk.Label(root, text="💖 Your Tasks 💖", bg="#ffe6f0", font=("Comic Sans MS", 16))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, bg="#ffb3d9", font=("Arial", 12))
add_btn.pack(pady=5)

mark_btn = tk.Button(root, text="Mark as Done", command=mark_done, bg="#d98cb3", font=("Arial", 12))
mark_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, bg="#ff6666", font=("Arial", 12))
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10, bg="#fff0f5")
listbox.pack(pady=10)

root.mainloop()
