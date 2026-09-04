def addTasks(tasks):
    while True:
        task = input("Enter a task or type 'exit' to stop: ")

        if task.lower() == "exit":
            break

        tasks.append(task)


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

    print(f"Deleted: {deletedTask}")
    print()


def main():
    tasks = []

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print()
            print("Please enter a valid number.")
            print()
            continue

        if choice == 1:
            addTasks(tasks)

        elif choice == 2:
            viewTasks(tasks)

        elif choice == 3:
            deleteTasks(tasks)

        elif choice == 4:
            break

        else:
            print()
            print("Please choose a valid option.")
            print()


main()