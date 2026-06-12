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

    def __str__(self):
        return f"{self.name}"
    

class Task:
    _id_counter = 1

    def __init__(self, title):
        self.id = Task._id_counter
        Task._id_counter += 1

        self._title = title
        self._completed = False

    @property
    def title(self):
        return self._title

    @property
    def completed(self):
        return self._completed

    def mark_complete(self):
        self._completed = True

    def __repr__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] Task({self.id}): {self.title}"
    
class Project:
    _id_counter = 1

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
