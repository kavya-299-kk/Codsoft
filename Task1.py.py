import tkinter as tk
from tkinter import messagebox

#Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Please Enter a Task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter updated task!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        if not task.endswith(" (Done)"):
            listbox.delete(selected)
            listbox.insert(selected, task + " (Done)")
    except:
        messagebox.showwarning("Warning", "Please select a task to mark done!")


root =tk.Tk()

root.title("Simple TO-DO List")
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=1, padx=5)

update_btn = tk.Button(root, text="Update Task", width=12, command=update_task)
update_btn.grid(row=1, column=1, padx=5)

delete_btn = tk.Button(root, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=2, column=1, padx=5)

done_btn = tk.Button(root, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=3, column=1, padx=5)

listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.grid(row=1, column=0, rowspan=4, padx=10, pady=10)

root.mainloop()
