def addTasks(tasks):
    while True:
        task = input("Enter a task or type 'exit' to stop:")
        if task.lower() == "exit":
            break

        tasks.append(task)
def viewTasks(tasks):
    print("Your task are:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
    print()

def deleteTasks(tasks):
    print("Your task are:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
    print()
    num = int(input("What tasks would you like to delete?"))
    deletedTask = tasks.pop(num - 1)
    print(f"Deleted: {deletedTask}")
    print()

def main():
    tasks = []

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            addTasks(tasks)

        elif choice == 2:
            viewTasks(tasks)

        elif choice == 3:
            deleteTasks(tasks)

        elif choice == 4:
            break
main()
