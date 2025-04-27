
import json
import uuid
from tabulate import tabulate
from storage import StorageManager
import colorama
from colorama import Fore, Back, Style
import pyfiglet
import time
from datetime import datetime

colorama.init()

# class blueprint of a Task Object
class Task:
    def __init__(self, title, description, due_date=None, status="pending"):
        self.title = title
        self.description = description
        self.status = status
        self.task_id = str(uuid.uuid1())
        self.due_date = due_date

    def __str__(self):
        return f"{self.task_id} - {self.title} - {self.description}"

    def __repr__(self):
        return self.__str__()


 # class methods for creating,reading,deleting and changing task status

class TasksController:
    @staticmethod
    def add_task(title, description, due_date=None, status="pending"):
        try:
            print(status)
            status_choices = ("pending", "in-progress", "completed")
            if status not in status_choices:
                raise ValueError(
                    "Status should be one of pending or in-progress or completed")
            if not datetime.strptime(due_date, "%d-%m-%Y"):
                raise ValueError("add due date in dd-mm-yyyy format")
            task = Task(title, description, due_date, status)
            print(f"\n{Fore.WHITE}Adding Task with title -->{Fore.YELLOW + Back.BLACK}{title} {Style.RESET_ALL}with status -->{Fore.YELLOW + Back.BLACK} {status if status else "pending"} {Style.RESET_ALL} and due date --> {Fore.YELLOW + Back.BLACK}{due_date if due_date else None} ")
            StorageManager.add_object(task)
            TasksController.defaut_formatting("Task added")
        except Exception as e:
            print(f" {Fore.RED} ERROR {e}")

    @staticmethod
    def get_task_index(task_number):
        StorageManager.get(task_number)

    @staticmethod
    def show_tasks():
        try:
            with open("./tasks.json", "r") as file:
                data = json.load(file)
                tasks = data.get("tasks", [])
                headers = ["Task Number", "Title",
                        "Description", "Status", "Task ID"]
                rows = [(task["task_number"], task["title"], task["description"],
                        task["status"], task["task_id"]) for task in tasks]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(e)


    @staticmethod
    def change_task_status(task_number, status):
        StorageManager.update_object(task_number, status)

    @staticmethod
    def delete_task(task_number):
        StorageManager.remove_objects(task_number)
        TasksController.defaut_formatting("Task Deleted")

    @staticmethod
    def defaut_formatting(text):
        time.sleep(0.5)
        ascii_text = pyfiglet.figlet_format(f"\n{text}\n")
        border = "+" + "-" * (len(ascii_text.splitlines()[0]) + 1) + "+"
        for line in ascii_text.splitlines():
            print(f"| {line} |")
        time.sleep(0.5)
        print(border)

    @staticmethod
    def check_stats():
        stats = StorageManager.json_stats()
        print(f'''"total_tasks":{stats.get("total_tasks")}, pending_tasks":{stats.get("pending_tasks")}"completed_tasks" : {stats.get("completed_tasks")},"in_progress_tasks" : {stats.get("in_progress_tasks")},\n''')
