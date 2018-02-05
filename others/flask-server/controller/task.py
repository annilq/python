from flask_pymongo import PyMongo
class Task():
    def __init__(self,db):
        super().__init__()
        self.db=db
    def findtask(self,name):
        task = self.db.tasks.find_one({"name":name})
        if task:
            return task
        else:
            return None
    def createtask(self,task):
        self.db.tasks.insert_one(task)
        return self.findtask(task['name'])

