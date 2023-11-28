import tkinter as tk
class ToDoListGUI:
 def __init__(self, root):
 self.root = root
 self.root.title("To-Do List")
 self.tasks = []
 self.entry = tk.Entry(root)
 self.entry.pack()
 self.add_button = tk.Button(root, text="Add Task", 
command=self.add_task)
 self.add_button.pack()
 self.list_button = tk.Button(root, text="List Tasks", 
command=self.list_tasks)
 self.list_button.pack()
 self.remove_button = tk.Button(root, text="Remove Task", 
command=self.remove_task)
 self.remove_button.pack()
 self.tasks_label = tk.Label(root, text="Tasks will be listed 
here.")
 self.tasks_label.pack()
 def add_task(self):
 task = self.entry.get()
 if task:
 self.tasks.append(task)
 self.entry.delete(0, tk.END)
 def list_tasks(self):
 if self.tasks:
 tasks_text = "\n".join(self.tasks)
 self.tasks_label.config(text=tasks_text)
 else:
 self.tasks_label.config(text="No tasks in the list.")
 def remove_task(self):
 if self.tasks:
 task_index = len(self.tasks) - 1
 self.tasks.pop(task_index)
 self.list_tasks()
def main():
 root = tk.Tk()
 app = ToDoListGUI(root)
 root.mainloop()
if __name__ == "__main__":
 main(
