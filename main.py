import argparse

from data import database
from manager import TaskManager

database.create_data()

parser = argparse.ArgumentParser(
    prog="task-cli",
    usage='%(prog)s [add,update,delete,list] [options]',
    description='Task management: add, update, delete and restore task list.',
    epilog="github.com/kene33"
)



# Create subcommands
subparsers = parser.add_subparsers(dest="command", required=True)

# Subcommand for adding a task
add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("name", help="Name of the task to add")

# Subcommand for updating a task
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id", help="ID of the task to update")
update_parser.add_argument("new_name", help="New name for the task")

# Subcommand for deleting a task
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", help="ID of the task to delete")

# Subcommand for getting the list of tasks
list_parser = subparsers.add_parser("list", help="Get the list of tasks")
list_parser.add_argument("mark", nargs='?', default=None, help="List all tasks with status (todo, done, in-progress)")

# Subcommand for marking tasks
mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark the task as in progress")
mark_in_progress_parser.add_argument("id", help="ID of the task to mark")

mark_done_parser = subparsers.add_parser("mark-done", help="Mark the task as done")
mark_done_parser.add_argument("id", help="ID of the task to mark")


args = parser.parse_args()

def main():
    manager = TaskManager() # dont know why I'm using classes in this project -_-

    if args.command == "add":
        id = database.get_id()
        manager.add_task(args.name, id)
        print(f"Task added successfully (ID: {id})")

    elif args.command == "update":
        id = args.id
        new_name = args.new_name

        manager.update(new_name, id)
        print(f"Task {id} updated.")

    elif args.command == "delete":
        id = args.id
        manager.delete(id)
        print(f"Task {id} deleted.")
        # wtf

    elif args.command == "list":
        manager.get_all_tasks(args.mark)


    elif args.command == "mark-in-progress":

        id = args.id
        manager.mark_in_progress("in-progress", id)
        print(f"Task {id} mark in-progress")

    elif args.command == "mark-done":
        id = args.id
        manager.mark_in_progress("done", id)
        print(f"Task {id} mark done")

if __name__ == "__main__":
    main()