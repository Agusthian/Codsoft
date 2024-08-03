import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    """Remove a task by index."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks("crickek,football,hockey")
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
