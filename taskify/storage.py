import json
from colorama import Fore, Back, Style
import os
from datetime import datetime
file_path = "./tasks.json"


 # class methods for writing and reading to the json file
class StorageManager:
    
    # METHODS TO CREATE READ AND WRITE JSON
    @staticmethod
    def create_json(path):
        try:
            default_json = {"tasks": []}

            if not os.path.exists(path):
                with open(path, "w") as file:
                    json.dump(default_json, file, indent=4,
                            default=lambda obj: obj.__dict__)
            elif os.path.getsize(path) == 0:
                with open(path, "w") as file:
                    json.dump(default_json, file, indent=4,
                            default=lambda obj: obj.__dict__)
        except Exception as e:
            print(f"{Fore.RED}Error creating file: {e}")

    @staticmethod
    def read_json(path):
        try:

            StorageManager.create_json(path)
            with open(path, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f" {Fore.RED}FILE NOT FOUND")
            return {"tasks": []}

    @staticmethod
    def write_json(path, data):
        try:
            StorageManager.create_json(path)
            with open(path, "w") as file:

                json.dump(data, file, indent=4,
                          default=lambda obj: obj.__dict__)
        except FileNotFoundError:
            print(f" {Fore.RED}FILE NOT FOUND")
 
 # METHODS TO FOR THE TASK STRUCTURES ORE RETRIEVE FROM JSON
    @staticmethod
    def add_object(task):
        try:
            StorageManager.create_json(file_path)
            data = StorageManager.read_json(file_path)
            task_number = (len(data["tasks"]) + 1) if data["tasks"] else 1
            task.task_number = task_number
            if task.due_date:
                tasks_copy = data["tasks"][:]
                tasks_copy.append(task.__dict__)
                tasks_with_dates = list( filter(lambda task:task.get("due_date"),tasks_copy))
                sorted_tasks_with_dates =sorted(tasks_with_dates,key=lambda task: datetime.strptime(task['due_date'], "%d-%m-%Y"))
                tasks_without_dates = list(filter(lambda task:not task.get("due_date"),data["tasks"]))
                data["tasks"] = []
                data["tasks"].extend(sorted_tasks_with_dates)
                data["tasks"].extend(tasks_without_dates)
                
            else:
                data["tasks"].append(task.__dict__)
            StorageManager.write_json(file_path, data)
        except Exception as e:
            print(f" {Fore.RED}ERROR {e}")

    @staticmethod
    def remove_objects(task_number):
        try:
            counter = 1
            data = StorageManager.read_json(file_path)
            get_task = data["tasks"][task_number-1]
            data["tasks"].remove(get_task)
            for task in data["tasks"]:
                task["task_number"] = counter
                counter += 1
            StorageManager.write_json(file_path, data)
        except Exception as e:
            print(f" {Fore.RED}{e}")

    @staticmethod
    def update_object(task_number, status):
        try:
            data = StorageManager.read_json(file_path)
            get_task = data["tasks"][task_number-1]
            get_task["status"] = status
            StorageManager.write_json(file_path, data)
        except Exception as e:
            print(f" {Fore.RED}{e}")

    @staticmethod
    def json_stats():
        try:
            data = StorageManager.read_json(file_path)
            total_tasks = len(data["tasks"])
            pending_tasks = 0
            completed_tasks = 0
            in_progress_tasks = 0
            for task in data["tasks"]:
                if task.get("status") == "pending":
                    pending_tasks += 1
                if task.get("status") == "completed":
                    in_progress_tasks += 1

            return ({
                "total_tasks": total_tasks,
                "pending_tasks": pending_tasks,
                "completed_tasks": completed_tasks,
                "in_progress_tasks": in_progress_tasks,
            }
            )
        except Exception as e:
            print(f" {Fore.RED}{e}")
