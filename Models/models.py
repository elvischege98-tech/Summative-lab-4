class Person:
    def __init__(self, name):
        self._name = name  # protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    def __str__(self):     #prints Sam instead of <__main__.User object at 0x1234>
        return f"{self.name}"
    

class Task:
    _id_counter = 1  #A counter variable to assign unique IDs to tasks

    def __init__(self, title):
        self.id = Task._id_counter
        Task._id_counter += 1

        self._title = title
        self._completed = False #To show new tasks as incomplete by default

    @property
    def title(self):
        return self._title

    @property
    def completed(self):
        return self._completed

    def mark_complete(self):
        self._completed = True

    def __repr__(self): #Concerts to string when printed in lists, shows status and title instead of <__main__.Task object at 0x1234>
        status = "✔" if self.completed else "✘"
        return f"[{status}] Task({self.id}): {self.title}"
    

    def to_dict(self): #Converts to JSON(Javascript object notation) python does not understand
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
class Project:
    _id_counter = 1  #A counter variable to assign unique IDs to projects

    def __init__(self, title):
        self.id = Project._id_counter
        Project._id_counter += 1

        self._title = title
        self.tasks = []

    @property
    def title(self):
        return self._title

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def __repr__(self):
        return f"Project({self.id}): {self.title} | Tasks: {len(self.tasks)}"
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks]
        }


class User(Person):
    _id_counter = 1

    def __init__(self, name):
        super().__init__(name)

        self.id = User._id_counter
        User._id_counter += 1

        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_project(self, project_id):
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

    def __repr__(self):
        return f"User({self.id}): {self.name} | Projects: {len(self.projects)}"
    
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "projects": [project.to_dict() for project in self.projects]
        }
