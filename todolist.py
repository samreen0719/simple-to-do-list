import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    """Display the current tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nCurrent Tasks:")
    for task_id, task in tasks.items():
        print(f"{task_id}: {task['title']} - {'Done' if task['done'] else 'Not Done'}")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter the task title: ")
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {'title': title, 'done': False}
    print(f"Task '{title}' added with ID {task_id}.")

def remove_task(tasks):
    """Remove a task by ID."""
    task_id = input("Enter the task ID to remove: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} removed.")
    else:
        print("Task ID not found.")

def mark_task_done(tasks):
    """Mark a task as done."""
    task_id = input("Enter the task ID to mark as done: ")
    if task_id in tasks:
        tasks[task_id]['done'] = True
        print(f"Task ID {task_id} marked as done.")
    else:
        print("Task ID not found.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
