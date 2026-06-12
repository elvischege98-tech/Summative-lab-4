##PROJECT: CLI PROJECT MANAGEMENT TOOL

--------------------------------------------------
DESCRIPTION
--------------------------------------------------
- CLI application
- Manage:
    -> Users
    -> Projects
    -> Tasks
- Uses:
    -> OOP (classes)
    -> JSON file storage
    -> argparse CLI
    -> Rich library for UI

--------------------------------------------------
SETUP STEPS
--------------------------------------------------

START

clone project
cd into project folder

create virtual environment
    python3 -m venv venv

activate venv
    source venv/bin/activate

install dependencies
    pip install rich

run project
    python3 Main.py <command>

END

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

Main.py
Models/
    User class
    Project class
    Task class
Storage module
data.json
venv/
requirements.txt

--------------------------------------------------
COMMANDS (CLI ACTIONS)
--------------------------------------------------

USER MANAGEMENT
    add-user --name NAME
    list-users

PROJECT MANAGEMENT
    add-project --user NAME --title TITLE
    list-projects --user NAME

TASK MANAGEMENT
    add-task --user NAME --project TITLE --title TASK
    list-tasks --user NAME --project TITLE
    complete-task --user NAME --project TITLE --id ID

--------------------------------------------------
DATA FLOW
--------------------------------------------------

User created
    -> stored in USERS list
    -> saved to JSON

Project created
    -> linked to User
    -> saved to JSON

Task created
    -> linked to Project
    -> saved to JSON

--------------------------------------------------
PERSISTENCE
--------------------------------------------------

on every change:
    save_data() → write to data.json

on startup:
    load_data() → rebuild objects

--------------------------------------------------
OUTPUT (RICH)
--------------------------------------------------

print users → table view
print tasks → colored status
print success messages → green
print errors → red

--------------------------------------------------
END
--------------------------------------------------