tasks = []

def show_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def add_task(task):
    tasks.append(task)

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid index")

while True:
    action = input("Enter command (add, remove, show, quit): ").strip().lower()
    if action == 'add':
        task = input("Enter task: ")
        add_task(task)
    elif action == 'remove':
        index = int(input("Enter task index to remove: ")) - 1
        remove_task(index)
    elif action == 'show':
        show_tasks()
    elif action == 'quit':
        break
    else:
        print("Unknown command")
