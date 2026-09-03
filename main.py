def addTasks(tasks):
    while True:
        task = input("Enter a task or type 'exit' to stop:")
        if task.lower() == "exit":
            break

        tasks.append(task)
def viewTasks(tasks):
    print("Your task are:")
    for task in tasks:
        print(task)

tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        addTasks(tasks)

    elif choice == 2:
        viewTasks(tasks)

    elif choice == 3:
        break

