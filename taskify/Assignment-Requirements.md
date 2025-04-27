Assignment Title: Task Tracker CLI

Objective:
Build a simple command-line based to-do list application using Python. This application should allow users to add, list, mark complete, and delete tasks. The tasks should persist using a local JSON file.

Requirements:
1. Add a Task - User can add a task by providing a title and an optional description. 
2. List Tasks - Display all tasks with their ID, title, description (if any), and status (Pending/Completed).
3. Mark Task as Completed - Allow the user to update the status of a task to 'Completed' using the task ID.
4. Delete Task - Allow the user to delete a task using its ID.
5. Data Persistence - Tasks should be stored and loaded from a local tasks.json file.

:file_folder: Expected Project Structure:
 task_tracker/
 │
 ├── main.py # CLI entry point
 ├── task_manager.py # Functions to add, delete, mark complete
 ├── storage.py # Functions to read/write JSON file
 ├── tasks.json # Stores task data
 └── README.md # Instructions & how to run

Bonus (Optional):
 Add support for due dates.
 Implement simple color-coded terminal output (e.g., using colorama).
 Sort tasks by due date.

No LLMs Allowed:
Any assignment that appears to be generated or assisted by a Large Language Model (LLM) will be rejected. Code style, comments, and problem-solving approach will be reviewed carefully to ensure originality.

Submission:
Submit a .zip file containing the entire task_tracker/ directory.
Include a README.md explaining how to run your code, what features are implemented, and any challenges faced.
Happy Coding!
