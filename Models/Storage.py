import json
from Models import User, Project, Task

DATA_FILE = "data.json"

def save_data(users):
    data = {
        "users": [user.to_dict() for user in users]
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": []}

    # SAFETY CHECK (IMPORTANT)
    if "users" not in data:
        data["users"] = []

    users = []

    for user_data in data["users"]:
        user = User(user_data["name"])
        user.id = user_data["id"]

        for project_data in user_data.get("projects", []):
            project = Project(project_data["title"])
            project.id = project_data["id"]

            for task_data in project_data.get("tasks", []):
                task = Task(task_data["title"])
                task.id = task_data["id"]

                if task_data.get("completed"):
                    task.mark_complete()

                project.add_task(task)

            user.add_project(project)

        users.append(user)

    return users