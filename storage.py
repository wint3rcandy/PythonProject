import json
import json


def saveTasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []