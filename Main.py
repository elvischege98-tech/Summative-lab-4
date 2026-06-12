import argparse
from Models.models import User, Project, Task
from Models.Storage import save_data, load_data

# In-memory storage
USERS = []

# Load existing data
USERS = load_data()

# ==========================
# User Actions
# ==========================

def add_user(name):
    user = User(name)
    USERS.append(user)
    save_data(USERS)
    print(f"User '{name}' created successfully.")


def list_users():
    if not USERS:
        print("No users found.")
        return

    for user in USERS:
        print(user)


# ==========================
# Project Actions
# ==========================

def add_project(user_name, title):
    for user in USERS:
        if user.name == user_name:
            project = Project(title)
            user.add_project(project)
            save_data(USERS)
            print(f"Project '{title}' added to {user_name}")
            return

    print("User not found.")


def list_projects(user_name):
    for user in USERS:
        if user.name == user_name:

            if not user.projects:
                print("No projects found.")
                return

            for project in user.projects:
                print(project)

            return

    print("User not found.")


# ==========================
# Task Actions
# ==========================

def add_task(user_name, project_title, task_title):

    for user in USERS:

        if user.name == user_name:

            for project in user.projects:

                if project.title == project_title:

                    task = Task(task_title)
                    project.add_task(task)

                    print(f"Task '{task_title}' added.")
                    save_data(USERS)
                    return

    print("Project not found.")


def list_tasks(user_name, project_title):

    for user in USERS:

        if user.name == user_name:

            for project in user.projects:

                if project.title == project_title:

                    if not project.tasks:
                        print("No tasks found.")
                        return

                    for task in project.tasks:
                        print(task)

                    return

    print("Project not found.")


def complete_task(user_name, project_title, task_id):

    for user in USERS:

        if user.name == user_name:

            for project in user.projects:

                if project.title == project_title:

                    task = project.get_task(task_id)

                    if task:
                        task.mark_complete()
                        save_data(USERS)
                        print("Task completed.")
                        return

                    print("Task not found.")
                    return

    print("Project not found.")


# ==========================
# CLI
# ==========================

def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---------- User Commands ----------

    add_user_cmd = subparsers.add_parser(
        "add-user",
        help="Add a new user"
    )
    add_user_cmd.add_argument(
        "--name",
        required=True,
        help="User name"
    )

    subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    # ---------- Project Commands ----------

    add_project_cmd = subparsers.add_parser(
        "add-project",
        help="Add a project"
    )
    add_project_cmd.add_argument(
        "--user",
        required=True,
        help="User name"
    )
    add_project_cmd.add_argument(
        "--title",
        required=True,
        help="Project title"
    )

    list_projects_cmd = subparsers.add_parser(
        "list-projects",
        help="List projects"
    )
    list_projects_cmd.add_argument(
        "--user",
        required=True,
        help="User name"
    )

    # ---------- Task Commands ----------

    add_task_cmd = subparsers.add_parser(
        "add-task",
        help="Add a task"
    )
    add_task_cmd.add_argument(
        "--user",
        required=True
    )
    add_task_cmd.add_argument(
        "--project",
        required=True
    )
    add_task_cmd.add_argument(
        "--title",
        required=True
    )

    list_tasks_cmd = subparsers.add_parser(
        "list-tasks",
        help="List tasks"
    )
    list_tasks_cmd.add_argument(
        "--user",
        required=True
    )
    list_tasks_cmd.add_argument(
        "--project",
        required=True
    )

    complete_task_cmd = subparsers.add_parser(
        "complete-task",
        help="Mark a task as complete"
    )
    complete_task_cmd.add_argument(
        "--user",
        required=True
    )
    complete_task_cmd.add_argument(
        "--project",
        required=True
    )
    complete_task_cmd.add_argument(
        "--id",
        type=int,
        required=True
    )

    args = parser.parse_args()

    # ---------- Command Router ----------

    if args.command == "add-user":
        add_user(args.name)

    elif args.command == "list-users":
        list_users()

    elif args.command == "add-project":
        add_project(args.user, args.title)

    elif args.command == "list-projects":
        list_projects(args.user)

    elif args.command == "add-task":
        add_task(args.user, args.project, args.title)

    elif args.command == "list-tasks":
        list_tasks(args.user, args.project)

    elif args.command == "complete-task":
        complete_task(args.user, args.project, args.id)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    