from flask_pymongo import PyMongo
from bson.json_util import dumps

class Folder():
    def __init__(self,db):
        super().__init__()
        self.db=db
    def find_folder(self,name):
        folder = self.db.folders.find_one({"name":name})
        if folder:
            return folder
        else:
            return None
    def get_folders(self):
        """当前方法只能在flask的上下文中运行，单独执行会报错"""
        output = []
        # return a collection cursor
        folders = self.db.folders.find()
        # convert to list
        for folder in folders:
            output.append(folder)
        return output
    def createfolder(self,folder):
        self.db.folders.insert_one(folder)
        return self.find_folder(folder['name'])

