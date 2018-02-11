from flask import session
from flask_pymongo import PyMongo


class Task():
    def __init__(self, db):
        super().__init__()
        self.db = db

    def find_task(self, name):
        task = self.db.tasks.find_one({"name": name})
        if task:
            return task
        else:
            return None

    def get_tasks(self, param):
        """当前方法只能在flask的上下文中运行，单独执行会报错"""
        output = []
        # return a collection cursor
        query = {"userId": session['uid']}
        query = {**query, **param}
        tasks = self.db.tasks.find(query)
        # convert to list
        for task in tasks:
            task["_id"] = str(task['_id'])
            output.append(task)
        return output

    def createtask(self, task):
        self.db.tasks.insert_one(task)
        return self.find_task(task['name'])
