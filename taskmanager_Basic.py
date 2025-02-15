import sys

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Added task: {task}')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f'Deleted task: {removed_task["task"]}')
    except IndexError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{i + 1}. {task["task"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        print("Invalid task number")

def show_help():
    print("""
    Available commands:
    1. add <task>: Add a new task
    2. delete <task_number>: Delete a task by its number
    3. view: View all tasks
    4. complete <task_number>: Mark a task as completed
    5. help: Show this help message
    6. exit: Exit the application
    """)

def main():
    print("Task Manager Application")
    show_help()
    while True:
        command = input("Enter command number: ").strip().split()
        if not command:
            continue
        if command[0] == "1":
            task = input("Enter task: ").strip()
            add_task(task)
        elif command[0] == "2":
            task_number = input("Enter task number to delete: ").strip()
            if task_number.isdigit():
                delete_task(int(task_number) - 1)
            else:
                print("Invalid command")
        elif command[0] == "3":
            view_tasks()
        elif command[0] == "4":
            task_number = input("Enter task number to complete: ").strip()
            if task_number.isdigit():
                mark_task_completed(int(task_number) - 1)
            else:
                print("Invalid command")
        elif command[0] == "5":
            show_help()
        elif command[0] == "6":
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Type '5' to see available commands.")

if __name__ == "__main__":
    main()