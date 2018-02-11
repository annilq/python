from flask import session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class Folder():
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.defalutFolder = [{
            "name": "home",
            "type": "home",
            "fixed": True
        }, {
            "name": "star",
            "type": "star",
            "fixed": True
        }, {
            "name": "done",
            "type": "done",
            "fixed": True
        }]

    def initfolders(self, uid):
        folders = []
        data = self.db.folders.find({"userId": uid})
        for folder in data:
            folders.append(folder)
        if len(folders) == 0:
            # 生成的folder
            output=[]
            for folder in self.defalutFolder:
                folder=self.post(folder["name"],folder["type"])
                output.append(folder)
            return output

    def find_folder(self, id):
        folder = self.db.folders.find_one({"_id": ObjectId(id)})
        if folder:
            folder["_id"] = str(folder['_id'])
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

    # 默认类型type为folder，这点其实不是很好
    def post(self, name, type="folder"):
        userId = session['uid']
        data = {"name": name, "userId": userId, "type": type}
        folder = self.db.folders.insert_one(data)
        return self.find_folder(folder.inserted_id)

    def put(self, id, folder):
        folder = self.db.folders.update_one({
            "_id": ObjectId(id)
        }, {
            "$set": {
                **
                folder
            }
        })
        print(folder.upserted_id)
        return self.find_folder(id)

    def delete(self, id):
        DeleteResult = self.db.folders.delete_one({"_id": ObjectId(id)})
        return DeleteResult
