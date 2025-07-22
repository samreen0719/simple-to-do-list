# To-Do List Console Application

A simple console-based To-Do List application written in Python. This program allows users to manage their tasks by adding, viewing, removing, and marking tasks as done. The tasks are stored in a JSON file, ensuring that they persist between sessions.

## Features

- View current tasks
- Add new tasks
- Remove existing tasks
- Mark tasks as done
- Data persistence using JSON file

## Requirements

- Python 3.x

## Usage

Once the application is running, you will see a menu with the following options:

View Tasks: Displays the current tasks with their IDs and status (done or not done).
Add Task: Prompts you to enter a task title and adds it to the list.
Remove Task: Prompts you to enter the task ID to remove it from the list.
Mark Task as Done: Prompts you to enter the task ID to mark it as completed.
Exit: Exits the program.

## File handling

The tasks are stored in a JSON file named tasks.json. When the program starts, it loads existing tasks from this file, and any changes made to the tasks are saved back to the file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

Inspired by various task management applications.
Thanks to the Python community for their support and resource
