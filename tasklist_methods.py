from typing import Any, Union, Optional
import os

#we should turn this into a class
# This task list comes from the tasklist_setup class and can have different instances
task_list: list[Union[str, Any]] = [] #Instead of a list, we can use a dict. Key-Value pair is more useful here

# issues to address if two task are in the list and you remove one it removes both of them fix it so the most recent on get deleted 

# without this function the other iife won't be able to find the file path
# We move this to tasklist_setup
@lambda _: _()
def pre_loader() -> None: 
    # use need to provide a file path
    filepath = "todo_list\\task.txt"
    with open(file=filepath, mode="a") as file:
        pass

# We move this to tasklist_setup and provide a safe_tasklist functionality
def save_task() -> Optional[Any]:
    filepath = "todo_list\\task.txt"
    #filepath = "file\\task.txt"
    with open(filepath, "w") as file:
        for current_task in task_list:
            file.write(f"{current_task}\n")


def check_if_task_exits(task) -> Union[int, Any]:
    if task in task_list:
        return -1 # return -1 means task is in list
    else:
        return 0 # return 0 means not in list

def add_task(task: str) -> Any:
    #os.system("cls") <-- remove this
    occur: int = 0
    for current_task in task_list:
        if current_task == task:
            occur += 1
    
    if occur > 2:
        print("you can't add task") #<-- Change to task already exists
    else:
        task_list.append(task)
        print(f"task added")

#This is duplicated. If a tasks can only be added once, why should there be a mechanism
#that removes a task that is duplicated
def remove_task() -> Any:
    try:
        #os.system("cls") <-- RRemove, no os commands
        # make sure every task in list only exits onces
        # display current task
        for index, value in enumerate(task_list):
            print(f"{index}, {value}")

        # task is being deleted based on it index
        print("Select task by number: ")
        task_to_delete: int = int(input("> "))
        
        del task_list[task_to_delete]
    except IndexError:
        print("\nTask does not exits\n")
    finally:
        return task_list

# the user should be able to update a task in the list
def update_task() -> Any:
    #os.system("cls")
    # clear the screen
    #os.system("cls")

    # load all task in a nice format
    for index, value in enumerate(task_list):
        print(f"{index}, {value}")
    
    task_usr_selected: str = input("Enter task you want to update: ")

    new_task: str = input("Enter new task: ")
    for index, value in enumerate(task_list):
        if value == task_usr_selected:
            task_list.remove(task_usr_selected)
            task_list.insert(index, new_task)
    
    return task_list

@lambda _: _() # <-- What is this?
#This should be part of the tasklist_setup class
def load_task() -> Optional[Any]:
    filepath = "todo_list\\task.txt"

    #filepath = "file\\task.txt"

    with open(file=filepath, mode="r") as file:
        data = file.readlines()
        for current_task in data:
            task_list.append(current_task.rstrip("\n"))


@lambda _: _()
#This should be part of the main.py class. There, we initate the task list
# and we provide the respective methods
def main():
    msg = """
[a]dd task
[r]emove task
[u]pdate task
[c]lear screen
[q]uit
[l]oad task
"""
    running: bool = True

    while running:
        print(msg)
        user_input: str = input("Enter command: ").lower().strip()

        match user_input:
            case "a":
                usr_task: str = input("Enter task: ")
                add_task(task=usr_task)
            case "r":
                print(remove_task())
            case "u":
                print(update_task())
            case "c":
                os.system("cls")
            case "l":
                os.system("cls")
                print(task_list)
            case "q":
                save_task()
                quit()
            case _:
                running =  False