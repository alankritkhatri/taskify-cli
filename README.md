<!-- INTRO -->
- Taskify is a command line tool to manage a TodoList
- Users can add,delete tasks
- Tasks can have properties like title,description,status,due_date
- Title is mandatory and rest is optional


<!-- how to run -->
2 Ways to run

1) Using pip - Link - https://pypi.org/project/heytaskify/
    - pip install heytaskify
    - usage is simple -> heytaskify addtask "Task Title" --description "task description" --status "pending" --duedate "22-3-2014"

2)  Using this zip file 
    Step 1 : Unzip the file
    Step 3 : Activate the venv by using
                Windows: .\.venv\Scripts\activate 
                Mac: source .venv/bin/activate
    Step 3 : cd into Taskify
    Step 4 : Run py .\main.py <COMMAND_NAME>


<!-- COMMANDS -->
# Commands

**if using PIP theh just run ocmmand using heytaskify command example=> heytaskify addtask "Task Title" --description "task description" --status "pending**


1. Add Task
py .\main.py addtask "Task Title" --description "task description" --status "pending" --duedate "22-3-2014"


to create multiple tasks at once use this . Basically adding more arguments to each flag
py .\main.py addtask "Task Title" "Task 2 Title" --description "task description" "task 2  description" --status "pending"  "pending" --duedate "22-3-2014" "22-3-2014"

2. Show Tasks
py .\main.py showtasks

3. Show Stats
py .\main.py stats

4. Delete Task
py .\main.py deletetask <task_number>

5. Update Status
py .\main.py updatestatus <task_number> <new_status>

<!-- CODE -->

FLOW - main.py calls-> taskmanger.py to create an instance of the Task or use the class methods which calls-> Storage.py to read and write the json files
which writes the operation into tasks.JSON and maintains the json structure

Main.py
    - main function which is the entry point to our application
    - args parser and the arguments are initiated in this file and the respective method is called at the end to execute the task

task_manager.py
    - Task Class which is the blueprint of a task 
    - Task Manger Class has methods to create the tasks or do any operation related to the tasks like show stats or show tasks ,etc. the methods in this class communicate with the methods in the StorageManger class in storage.py to work with the tasks.JSON file

storage.py
 -methods to Interact with the JSON file
 - Specifically 3 methods to read/write/create the json
 - Other methods to do particular operations from the json which leverage the reading/writing methods to operate


