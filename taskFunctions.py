from storage import saveTasks
def addTasks(tasks):
    while True:
        task = input("Enter a task or type 'exit' to stop: ")

        if task.lower() == "exit":
            break

        tasks.append(task)
        saveTasks(tasks)
def viewTasks(tasks):
    print("Your tasks are:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

    print()
def deleteTasks(tasks):
    if not tasks:
        print()
        print("There are no tasks to delete.")
        print()
        return

    print("Your tasks are:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

    print()

    try:
        num = int(input("What task would you like to delete? "))
    except ValueError:
        print("Please enter a number.")
        print()
        return

    if num < 1 or num > len(tasks):
        print("Please enter a valid task number.")
        print()
        return

    deletedTask = tasks.pop(num - 1)
    saveTasks(tasks)

    print(f"Deleted: {deletedTask}")
    print()
