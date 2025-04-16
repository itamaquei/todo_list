from typing import Any
import os
task_list: list[str| Any] = []

# issues to address if two task are in the list and you remove one it removes both of them fix it so the most recent on get deleted 

# without this function the other iife won't be able to find the file path
@lambda _: _()
def pre_loader() -> None: 
    # use need to provide a file path
    filepath = ""
    with open(file=filepath, mode="a") as file:
        pass

def save_task() -> Any | None:
    filepath = ""
    #filepath = "file\\task.txt"
    with open(filepath, "w") as file:
        for current_task in task_list:
            file.write(f"{current_task}\n")


def check_if_task_exits(task) -> int | Any:
    if task in task_list:
        return -1 # return -1 means task is in list
    else:
        return 0 # return 0 means not in list

def add_task(task: str) -> Any:
    os.system("cls")
    occur: int = 0
    for current_task in task_list:
        if current_task == task:
            occur += 1
    
    if occur > 2:
        print("you can't add task")
    else:
        task_list.append(task)
        print(f"task added")

def remove_task(task_to_remove: str) -> Any:
    os.system("cls")
    # make sure every task in list only exits onces
    occur: int = 0
    for current_task in task_list:
        if current_task == task_to_remove:
            occur += 1
    
    if occur > 1:
        for index, value in enumerate(task_list[:-1]):
            if task_to_remove == value:
                del task_list[index]
                print('Tasked removed')
    else:
        for index, value in enumerate(task_list):
            if task_to_remove == value:
                del task_list[index]
                print("Tasked remove")
        
    return task_list

# the user should be able to update a task in the list
def update_task() -> Any:
    os.system("cls")
    # clear the screen
    os.system("cls")

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

@lambda _: _()
def load_task() -> Any | None:
    filepath = ""

    #filepath = "file\\task.txt"

    with open(file=filepath, mode="r") as file:
        data = file.readlines()
        for current_task in data:
            task_list.append(current_task.rstrip("\n"))


@lambda _: _()
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
                remove_task_input: str = input("Enter task to remove: ")
                print(remove_task(remove_task_input))
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