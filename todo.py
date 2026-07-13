"""
Simple Command-Line To-Do List App
Author: Prachi
"""

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file, or return an empty list."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\nNo tasks yet! Add one.\n")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added!\n")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    menu = """
==== TO-DO LIST APP ====
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit
=========================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
