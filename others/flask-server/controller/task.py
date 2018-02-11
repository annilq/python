from flask import session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class Task():
    def __init__(self, db):
        super().__init__()
        self.db = db

    def find_task(self, id):
        task = self.db.tasks.find_one({"_id": ObjectId(id)})
        print(task)
        if task:
            task["_id"] = str(task['_id'])
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

    def post(self, folderId, name):
        task = {"userId": session['uid'], "folderId": folderId, "name": name}
        task = self.db.tasks.insert_one(task)
        return self.find_task(task.inserted_id)

    # update task
    def put(self, id, task):
        del task["_id"]
        task = self.db.tasks.update_one({
            "_id": ObjectId(id)
        }, {
            "$set": {
                **
                task
            }
        })
        print(task.upserted_id)
        return self.find_task(id)

    # delete task
    def delete(self, id):
        task = self.db.tasks.delete_one({"_id": ObjectId(id)})
        return task
