# Creating a task tracker CLI app using python, json and other modules
# This will be the tasks dictionary that will hold the ID of the task, a short description and the status
# It will additionally display the time created and the time uppdated.

import datetime
import json
import baethal
import os

file_name = "tasks.json"

# Adds any task
def add_task():
    task_to_add: str = input("\nEnter a task to add: ")
    if task_to_add == "":
        print("Invalid Task: Please enter a task")
        return add_task()

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            id = len(data) - 1
            data[id] = {
                "description": task_to_add,
                "status": "Todo",
                "time_created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "time_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(file_name, "w") as f:
                json.dump(data, f, indent=4)
                print(f'Task {task_to_add} has been added with ID: {id}')
    except FileNotFoundError:
        print("File not found, restarting...")
        return file_check()
    except json.JSONDecodeError:
        print("File is empty, restarting...")
        return file_check()

    return input_handler()

# Updates any task
def update_task():
    task_id: int = input("\nEnter the ID of the task to update: ")
    with open(file_name, "r") as file:
        tasks: dict = json.load(file)

        if task_id not in tasks:
            print("Invalid ID: Please enter a valid ID")
            return update_task()

        task_to_update: str = input("\nEnter a task to update: ")

        if task_to_update == "":
            print("Invalid Task: Please enter a task")
            return update_task()

        tasks[task_id]["description"] = task_to_update
        tasks[task_id]["time_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f'Task {task_to_update} has been updated with ID: {task_id}')
    return input_handler()

# Deletes any task
def delete_task():
    task_delete: int = input("\nEnter the ID of the task to delete: ")
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)

        if task_delete not in tasks:
            print("Invalid ID: Please enter a valid ID")
            return delete_task()

        del tasks[task_delete]

        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f'Task with ID: {task_delete} has been deleted')
    return input_handler()

# Marks any task as in progress
def mark_in_progress():
    marked_progress = input("\nEnter the ID of the task to mark in progress: ")
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)

        if marked_progress not in tasks:
            print("Invalid ID: Please enter a valid ID")
            return mark_in_progress()

        tasks[marked_progress]["status"] = "In Progress"
        tasks[marked_progress]["time_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f'Task with ID: {marked_progress} has been marked in progress')
    return input_handler()

# Gives a list of all tasks that are marked as done
def mark_done():
    marked_done = input("\nEnter the ID of the task to mark done: ")
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)

        if marked_done not in tasks:
            print("Invalid ID: Please enter a valid ID")
            return mark_done()

        tasks[marked_done]["status"] = "Done"
        tasks[marked_done]["time_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f'Task with ID: {marked_done} has been marked done')
    return input_handler()

# Gives a list of all tasks that are marked as todo
def mark_todo():
    marked_todo = input("\nEnter the ID of the task to mark todo: ")
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)

        if marked_todo not in tasks:
            print("Invalid ID: Please enter a valid ID")
            return mark_todo()

        tasks[marked_todo]["status"] = "Todo"
        tasks[marked_todo]["time_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f'Task with ID: {marked_todo} has been marked todo')
    return input_handler()

# Gives a list of all tasks
def tasks_list():
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)
        print(f"--- Your current tasks are: ---\n\n")
        for i in tasks:
            print(f" ID: {i} \n"
                  f"   Description: {tasks[i]['description']} \n"
                  f"   Status: {tasks[i]['status']} \n"
                  f"   Time Created: {tasks[i]['time_created']} \n"
                  f"   Time Updated: {tasks[i]['time_updated']}\n\n")

    return input_handler()

# Marks any task as done
def tasks_done():
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)
        print(f"--- The following tasks are done: ---\n\n")
        for i in tasks:
            if tasks[i]["status"] == "Done":
                print(f" ID: {i} \n"
                      f"   Description: {tasks[i]['description']} \n"
                      f"   Status: {tasks[i]['status']} \n"
                      f"   Time Created: {tasks[i]['time_created']} \n"
                      f"   Time Updated: {tasks[i]['time_updated']}\n\n")

    return input_handler()

# Marks any task as to do
def tasks_todo():
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)
        print(f"--- These tasks are todo: ---\n\n")
        for i in tasks:
            if tasks[i]["status"] == "Todo":
                print(f" ID: {i} \n"
                      f"   Description: {tasks[i]['description']} \n"
                      f"   Status: {tasks[i]['status']} \n"
                      f"   Time Created: {tasks[i]['time_created']} \n"
                      f"   Time Updated: {tasks[i]['time_updated']}\n\n")

    return input_handler()

# Marks any task as in progress
def tasks_in_progress():
    with open(file_name, "r") as f:
        tasks: dict = json.load(f)
        print(f"--- The following tasks are in progress: ---\n\n")
        for i in tasks:
            if tasks[i]["status"] == "In Progress":
                print(f" ID: {i} \n"
                      f"   Description: {tasks[i]['description']} \n"
                      f"   Status: {tasks[i]['status']} \n"
                      f"   Time Created: {tasks[i]['time_created']} \n"
                      f"   Time Updated: {tasks[i]['time_updated']}\n\n")

    return input_handler()

    # Input handler Distrubutes user input to their specific functions
def input_handler():
    command = input("Enter your commands here: ")
    if command == "add":
        return add_task()
    elif command == "update":
        return update_task()
    elif command == "delete":
        return delete_task()
    elif command == "mark-in-progress":
        return mark_in_progress()
    elif command == "mark-done":
        return mark_done()
    elif command == "mark-todo":
        return mark_todo()
    elif command == "list":
        return tasks_list()
    elif command == "list-done":
        return tasks_done()
    elif command == "list-todo":
        return tasks_todo()
    elif command == "list-in-progress":
        return tasks_in_progress()
    elif command == "menu":
        return menu()
    elif command == "refresh file":
        return file_check()
    else:
        print("Invalid Command")
        return input_handler()

    # The menu function will display my signature and a list of available commands to run
    # This should also check if there's a json file already before running the print commands
    # After the prints the input_handler function should be called to handle any user input and
    # return to their specific functions


def menu():
    print(f'\n{baethal.baethal}\n')
    print("""  _____ _   ___ _  __  _____ ___    _   ___ _  _____ ___ 
 |_   _/_\ / __| |/ / |_   _| _ \  /_\ / __| |/ / __| _ \\
   | |/ _ \\\__ \ ' <    | | |   / / _ \ (__| ' <| _||   /
   |_/_/ \_\___/_|\_\   |_| |_|_\/_/ \_\___|_|\_\___|_|_\\
                                                   
 <------- AVAILABLE COMMANDS ------->
    add:                    { Adds a Task and returns and ID }
    update:                 { Updates a Task using their ID }
    delete:                 { Deletes a Task using their ID }
    mark-in-progress:       { Marks the status of a task as In Progress using their ID }
    mark-done:              { Marks the status of a task as Done using their ID }
    mark-todo               { Marks the status of a task as Todo using their ID }
    list:                   { Lists all Tasks with their ID's }
    list-done:              { Lists all Done Tasks with their ID's }
    list-todo:              { Lists all In Progress Tasks with their ID's }
    list-in-progress:       { Lists all In Progress Tasks with their ID's }
    menu:                   { Returns to the Menu }
    refresh file:           { Refreshes the File }
    """)
    return input_handler()

def file_check():
    default_data: dict = {
            "id": {
                "description": "Example Task",
                "status": "In progress",
                "time_created": "Example Creation",
                "time_updated": "Example Update"
            }
        }
    print("LOG: Checking if tasks.json exists...")
    if os.path.exists(file_name):
        print("""LOG: File: "tasks.json" has been found!""")
        print("LOG: Loading...\n")
        return menu()
    else:
        print("""LOG: File: "tasks.json" has not been found!""")
        print("""LOG: Creating file: "tasks.json"... """)
        with open(file_name, "w") as file:
            json.dump(default_data, file, indent=4)
        print("""LOG: File: "tasks.json" has been created!""")
        print("LOG: Loading...\n")
        return menu()

def main():
    file_check()


if __name__ == '__main__':
    main()