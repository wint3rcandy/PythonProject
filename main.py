from taskFunctions import addTasks, viewTasks, deleteTasks
from storage import saveTasks, loadTasks

def main():
    tasks = loadTasks()

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
            saveTasks(tasks)
            print("Tasks Saved.")
            print()
            break

        else:
            print()
            print("Please choose a valid option.")
            print()


main()