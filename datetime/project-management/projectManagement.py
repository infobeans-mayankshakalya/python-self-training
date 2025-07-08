from datetime import *

class Project:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []
    def add_resource(self, resource):
        self.resources.append(resource)

class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

project = Project('AI', date(2021, 7, 18), date(2025, 8, 10))
task = Task('Create a bot', '5 days')
resource = Resource('John', 'React')
task.add_resource(resource)
project.add_task(task)

for eachTask in project.tasks:
    print('Task: ', eachTask.name, ', Duration: ', eachTask.duration)
    for res in eachTask.resources:
        print(res.name)
        print(res.skill)