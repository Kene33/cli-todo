from datetime import datetime 
from data import database

from colorama import init
init()
from colorama import Fore, Back, Style



class TaskManager:
    def __init__(self, name="None", id=int, status="todo", createdAt=int, updatedAt=int):
        self.name = name
        self.id = id
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt


    def add_task(self, name: str, id: int, status="todo"):
        now = datetime.now()
        current_time = now.strftime("%m-%d %H:%M")

        database.add_data(name, id, status, current_time, current_time)


    def update(self, name: str, id:int):
        now = datetime.now()
        updated_time = now.strftime("%m-%d %H:%M")

        database.update_data(name, id, updated_time)

    def delete(self, id: int):
        # Логика удаления задачи
        database.delete_data(id)
        # wtf i did

    def get_all_tasks(self, mark):
        tasks = database.get_tasks(mark)

        if not tasks:
            print("Tasks clean.")
        else:
            for task in tasks:
                if task[2] == "todo":
                    print(Fore.RED + f"ID: {task[0]} | Name: {task[1]} | Status: {task[2]} | Created: {task[3]} | Updated: {task[3]}\n")
                elif task[2] == "in-progress":
                    print(Fore.YELLOW + f"ID: {task[0]} | Name: {task[1]} | Status: {task[2]} | Created: {task[3]} | Updated: {task[3]}\n")
                else:
                    print(Fore.GREEN + f"ID: {task[0]} | Name: {task[1]} | Status: {task[2]} | Created: {task[3]} | Updated: {task[3]}\n")
                # i rly like shit coding 

    def mark_in_progress(self, status: str, id: int):
        database.mark_progress(status, id)