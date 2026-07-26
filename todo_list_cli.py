"""
To-Do List (CLI)
-----------------
A simple command-line to-do list app that saves tasks to a text file
so they persist between runs.
Demonstrates: lists, dicts, file I/O, functions, loops, OOP basics.
"""

import os

TASKS_FILE = "tasks.txt"


class ToDoList:
    """A simple to-do list backed by a plain text file."""

    def __init__(self, filename=TASKS_FILE):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    status, description = line.split("|", 1)
                    self.tasks.append({
                        "description": description,
                        "done": status == "1"
                    })

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                status = "1" if task["done"] else "0"
                f.write(f"{status}|{task['description']}\n")

    def add_task(self, description):
        self.tasks.append({"description": description, "done": False})
        self.save_tasks()
        print(f"Added: '{description}'")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()
            print(f"Marked as done: '{self.tasks[index]['description']}'")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted: '{removed['description']}'")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet. Add one!")
            return
        print("\nYour tasks:")
        for i, task in enumerate(self.tasks, start=1):
            box = "[x]" if task["done"] else "[ ]"
            print(f"  {i}. {box} {task['description']}")


def show_menu():
    print("\n===== To-Do List =====")
    print("  1. Add task")
    print("  2. View tasks")
    print("  3. Mark task as done")
    print("  4. Delete task")
    print("  5. Exit")


def main():
    todo = ToDoList()
    print("Welcome to the Week 1 CLI To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            if description:
                todo.add_task(description)
            else:
                print("Task description cannot be empty.")

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            todo.list_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            todo.list_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please select 1-5.")


if __name__ == "__main__":
    main()
