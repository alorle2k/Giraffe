
import argparse

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, username, task):
        self.tasks[task] = False
        print(f"Task '{task}' added for {username}!")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"Task '{task}' completed!")
        else:
            print("Task not found.")

    def show_tasks(self):
        for task, completed in self.tasks.items():
            status = "Done" if completed else "Not done"
            print(task, "-", status)


manager = TaskManager()

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["add-task", "complete-task", "show"])
parser.add_argument("--username", default="User")
parser.add_argument("--task", required=True)

args = parser.parse_args()

if args.command == "add-task":
    manager.add_task(args.username, args.task)
elif args.command == "complete-task":
    manager.complete_task(args.task)
elif args.command == "show":
    manager.show_tasks()
