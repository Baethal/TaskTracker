# Creating a task tracker CLI app using python, json and other modules
# This will be the tasks dictionary that will hold the ID of the task, a short description and the status
# It will additionally display the time created and the time uppdated.

import datetime
import json
import baethal
import os


tasks: dict = {
    "null": {
        "id": "null",
        "description": "Example Task",
        "status": "In progress",
        "time_created": "Example Creation",
        "time_updated": "Example Update"
    }
}

def add_task():
    task_to_add: str = input("\nEnter a task to add: ")


def update_task():
    pass

def delete_task():
    pass

def mark_in_progress():
    pass

def mark_done():
    pass

def task_list():
    pass

def task_done():
    pass

def task_todo():
    pass

def task_in_progress():
    pass

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
    elif command == "list":
        return task_list()
    elif command == "list-done":
        return task_done()
    elif command == "list-todo":
        return task_todo()
    elif command == "list-in-progress":
        return task_in_progress()
    else:
        print("Invalid Command")
        return input_handler()

# The menu function will display my signature and a list of available commands to run
# This should also check if there's a json file already before running the print commands
# After the prints the input_handler function should be called to handle any user input and
# return to their specific functions

def file_check():
    file_name: str = "tasks.json"
    default_data: dict = {
            "null": {
                "id": "null",
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
            json.dump(default_data, file)
        print("""LOG: File: "tasks.json" has been created!""")
        print("LOG: Loading...\n")
        return menu()




def menu():
    print(f'\n{baethal.baethal}\n')
    print("""  _____ _   ___ _  __  _____ ___    _   ___ _  _____ ___ 
 |_   _/_\ / __| |/ / |_   _| _ \  /_\ / __| |/ / __| _ \\
   | |/ _ \\\__ \ ' <    | | |   / / _ \ (__| ' <| _||   /
   |_/_/ \_\___/_|\_\   |_| |_|_\/_/ \_\___|_|\_\___|_|_\\
                                                   
 <------- AVAILABLE COMMANDS ------->
    add:                    { Adds a Task and returns and ID }
    update <id>:            { Updates a Task using their ID }
    delete <id>:            { Deletes a Task using their ID }
    mark-in-progress <id>:  { Marks the status of a task as In Progress using their ID }
    mark-done <id>:         { Marks the status of a task as Done using their ID }
    list:                   { Lists all Tasks with their ID's }
    list-done:              { Lists all Done Tasks with their ID's }
    list-todo:              { Lists all In Progress Tasks with their ID's }
    list-in-progress:       { Lists all In Progress Tasks with their ID's }
    """)
    return input_handler()

def main():
    file_check()


if __name__ == '__main__':
    main()