import pyfiglet
import argparse
from art import text2art
from task_manager import Task, TasksController
from inspirational_quotes import quote
import click
from colorama import Fore, Back, Style, init
import time

init(autoreset=True)


def main():
    # Greetings and motivational Quote
    quote_txt = quote()
    print(Fore.BLACK + "Hello & Welcome to Taskify")
    time.sleep(0.5)
    print(Fore.YELLOW + Back.BLACK +
          f"\nMotivational Quote: {Fore.YELLOW}{quote_txt.get("author")}: {Fore.CYAN} {quote_txt.get("quote")}")

    # PARSERS CONFIGS
    help_message = "Use these commands to use Taskify 👇\n"
    parser = argparse.ArgumentParser(
        prog="taskify", description="Commands for Taskify")
    subparser = parser.add_subparsers(dest="command", required=True)

    # parsers for adding tasks
    add_task_parser = subparser.add_parser(
        'addtask', help=f'''add a task with task title {Fore.YELLOW} EXAMPLE: py .\\main.py addtask "My Task" --description "This is a new task" --status "In Progress" --duedate 2025-12-01''')
    add_task_parser.add_argument(
        'taskname', nargs='+', type=str, help="add task name")
    add_task_parser.add_argument(
        '--description', nargs='+', type=str, help="add task description(OPTIONAL)")
    add_task_parser.add_argument(
        '--duedate', nargs='+', type=str, help="add duedate in dd-mm-yyyy format(OPTIONAL)")
    add_task_parser.add_argument(
        '--status', nargs='+', type=str, help="add status (OPTIONAL)")

    # parsers for showing tasks
    subparser.add_parser(
        "showtasks", help=f'''show all the tasks in the db/json {Fore.YELLOW} EXAMPLE: py .\\main.py showtasks''')

    # parsers for showing tasks
    subparser.add_parser("stats", help=f'''show stats''')

    # parsers for deleting tasks
    delete_task_parser = subparser.add_parser(
        "deletetask", help=f'''delete tasks commands {Fore.YELLOW} EXAMPLE: py .\\main.py deletetask 3''')
    delete_task_parser.add_argument(
        "task_number", type=int, help=f'''delete a particular task from the tasks db/json with the task number''')

    # parsers for changing status
    task_status_parser = subparser.add_parser(
        "updatestatus", help=f'''chaning tasks status commands {Fore.YELLOW} EXAMPLE: py .\\main.py updatestatus 3 completed ''')
    task_status_parser.add_argument(
        "task_number", type=int, help="task number for which status needs to be changed")
    task_status_parser.add_argument("new_status", help="add new status")

    args = parser.parse_args()
    # parser.print_help()
    if args.command == 'addtask':
        try:
            if ((len(args.taskname)) > 1 and (len(args.description)) > 1 and (len(args.duedate)) > 1 and (len(args.status)) > 1):
                for task, description, duedate, status in zip(args.taskname, args.description, args.duedate, args.status):
                    TasksController.add_task(
                        task, description, duedate, status or "pending")
            elif ((len(args.taskname)) == 1 and ((len(args.description)) == 1 or (len(args.duedate)) == 1 or (len(args.status)) == 1)):
                for task, description, duedate, status in zip(args.taskname, args.description, args.duedate, args.status):
                    TasksController.add_task(
                        task, description, duedate, status or "pending")

            show_tasks = input(
                Fore.BLUE + "want to see all tasks? press y for yes and n for no? ")
            if show_tasks == "y":
                TasksController.show_tasks()
            else:
                raise Exception
        except Exception as e:
            print(
                f"Please give more all properties when adding more than one task like name,status,desc,duedate ---- ERROR {e}")

    elif args.command == 'showtasks':
        TasksController.show_tasks()
    elif args.command == 'deletetask':
        TasksController.delete_task(args.task_number)
    elif args.command == 'updatestatus':
        TasksController.change_task_status(args.task_number, args.new_status)
    elif args.command == 'stats':
        TasksController.check_stats()


if __name__ == "__main__":
    main()
