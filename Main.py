import argparse
from Models.models import User, Project, Task
from Models.Storage import save_data, load_data
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

# In-memory storage
USERS = []

# Load existing data
USERS = load_data()

# User Actions

def add_user(name):
    user = User(name)
    USERS.append(user)
    save_data(USERS)
    print(f"User '{name}' created successfully.")

def list_users():
    if not USERS:
        console.print("[red]No users found.[/red]")
        return

    table = Table(title="Users", box=box.ROUNDED)

    table.add_column("Name", style="cyan")

    for user in USERS:
        table.add_row(user.name)

    console.print(table)

# Project Actions

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
                console.print("[red]No projects found.[/red]")
                return

            table = Table(title=f"Projects of {user_name}", box=box.ROUNDED)

            table.add_column("Title", style="yellow")

            for project in user.projects:
                table.add_row(project.title)

            console.print(table)
            return

    console.print("[red]User not found.[/red]")

# Task Actions

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
                        console.print("[red]No tasks found.[/red]")
                        return

                    table = Table(title=f"Tasks in {project_title}", box=box.SIMPLE_HEAVY)

                    table.add_column("ID", style="cyan", justify="right")
                    table.add_column("Task", style="white")
                    table.add_column("Status", style="green")

                    for i, task in enumerate(project.tasks):
                        status = "✔ Done" if getattr(task, "completed", False) else "✘ Pending"
                        table.add_row(str(i), task.title, status)

                    console.print(table)
                    return

    console.print("[red]Project not found.[/red]")

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

#View all users
# View / Display Actions

from rich.tree import Tree

def show_all():
    if not USERS:
        console.print("[red]No data found.[/red]")
        return

    tree = Tree("📦 [bold cyan]All Users[/bold cyan]")

    for user in USERS:
        user_branch = tree.add(f"👤 [bold]{user.name}[/bold]")

        if not user.projects:
            user_branch.add("[dim]No projects[/dim]")
            continue

        for project in user.projects:
            project_branch = user_branch.add(f"📁 [yellow]{project.title}[/yellow]")

            if not project.tasks:
                project_branch.add("[dim]No tasks[/dim]")
                continue

            for task in project.tasks:
                completed = getattr(task, "completed", False)
                status = "[green]✔[/green]" if completed else "[red]✘[/red]"
                project_branch.add(f"{status} {task.title}")

    console.print(tree)

# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    #  User Commands 

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

    #  Project Commands 

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

    # Task Commands 

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

    show_all_cmd = subparsers.add_parser(
        "show-all",
        help="Show all users, projects, and tasks"
    )

    args = parser.parse_args()

    #  Command Router 

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
    elif args.command == "show-all":
        show_all()    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    