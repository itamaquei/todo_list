from typing import Union


class RunTaskList(tasklist_methods, tasklist_methods):

    def __init__(self, task_list: list[Union[str, Any]]) -> None:
        self.task_list = task_list

    # Here we call the setup class and the respective method
    def run_tasklist(self):
        pass

