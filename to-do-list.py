import json
import os

FILE = "tasks.json"  

def loadTasks():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return []

def saveTasks(tasks):
    with open(FILE,"w") as f:
        json.dump(tasks, f, indent=2)

def addTasks(tasks):
    title = input("Task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added")

def listTasks(tasks):
    if not tasks:
        print("No task found")
        return
    for i, task in enumerate(tasks):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{i+1}.{task['title']}") 

def deleteTasks(tasks):
    listTasks(tasks)
    try:
        d = int(input("Enter the task number to delete: ")) - 1
        if 0 <= d < len(tasks):
            tasks.pop(d)
            print("Task deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def completeTask(tasks):
    listTasks(tasks)
    try:
        c = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= c <len(tasks):
            tasks[c]["completed"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def main():
    tasks = loadTasks()
    while True:
        print("To-Do List")
        print("1. Add Task\n2. List Tasks\n3. Delete Tasks\n4. Complete Task\n5. Exit")   
        choice = input("Choose an option: ")
        if choice == "1":
            addTasks(tasks)
        elif choice == "2":
            listTasks(tasks)
        elif choice == "3":
            deleteTasks(tasks)
        elif choice == "4":
            completeTask(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option")

main()