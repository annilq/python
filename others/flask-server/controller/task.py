from flask_pymongo import PyMongo


class Task():
    def __init__(self, db):
        super().__init__()
        self.db = db

    def findtask(self, name):
        task = self.db.tasks.find_one({"name": name})
        if task:
            return task
        else:
            return None

    def get_tasks(self):
        """当前方法只能在flask的上下文中运行，单独执行会报错"""
        output = []
        # return a collection cursor
        tasks = self.db.tasks.find()
        # convert to list
        for task in tasks:
            output.append({"userId": task["userId"], "name": task["name"]})
        return output

    def createtask(self, task):
        self.db.tasks.insert_one(task)
        return self.findtask(task['name'])
