import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.todo_list = []
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.prompt_label = tk.Label(self.root, text="Write your task here:", font=("Arial", 12))
        self.prompt_label.pack(pady=5)

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.done_button = tk.Button(self.root, text="Mark as Done", width=20, command=self.mark_done)
        self.done_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", width=20, command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.todo_list.append({"task": task, "done": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.todo_list[selected_task_index]
            task["done"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            status = "Done" if task["done"] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
