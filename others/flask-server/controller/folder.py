from flask import session
from flask_pymongo import PyMongo


class Folder():
    def __init__(self, db):
        super().__init__()
        self.db = db

    def find_folder(self, name):
        folder = self.db.folders.find_one({"name": name})
        if folder:
            return folder
        else:
            return None

    def get_folders(self, foldertype):
        """当前方法只能在flask的上下文中运行，单独执行会报错"""
        output = []
        # return a collection cursor
        userId = session['uid']
        query = {"userId": userId}
        if foldertype:
            query["type"] = foldertype
        folders = self.db.folders.find(query)
        # convert to list
        for folder in folders:
            # convert objectId to string
            folder["_id"] = str(folder['_id'])
            output.append(folder)
        return output

    def createfolder(self, folder):
        self.db.folders.insert_one(folder)
        return self.find_folder(folder['name'])
