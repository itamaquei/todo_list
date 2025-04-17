import os
from typing import Union, Any

#this is what we call when starting the task list
class SetupTasklist():
    def __init__(self, task_list: list[Union[str, Any]]) -> None:
        self.task_list = task_list

    # we set the directory containing the task lists here
    def set_dir(self):


    # we check if the directory already contains a file with tasks
    # if yes --> load all or only the first file we find; if no, create an empty file
    def check_dir_content(self):


    # this method should be called to create a task list. Should be a private method
    def create_tasklist(self):


    def check_extension(self):
        #we should only allow csv files for now, so we check if the task list file is of type csv

    # Gets called when closing the program and saves the tasklists and the respective tasks
    def safe_tasklist(self):
