import argparse

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # User commands
    subparsers.add_parser("add-user", help="Add a new user")
    subparsers.add_parser("list-users", help="List all users")

    # Project commands
    subparsers.add_parser("add-project", help="Add a new project")
    subparsers.add_parser("list-projects", help="List all projects")

    # Task commands
    subparsers.add_parser("add-task", help="Add a new task")
    subparsers.add_parser("complete-task", help="Mark a task as complete")

    args = parser.parse_args()

    print(f"Command received: {args.command}")

if __name__ == "__main__":
    main()