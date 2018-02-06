from flask_pymongo import PyMongo
class Folder():
    def __init__(self,db):
        super().__init__()
        self.db=db
    def findfolder(self,name):
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
            output.append({"type": folder["type"], "name": folder["name"]})
        return output
    def createfolder(self,folder):
        self.db.folders.insert_one(folder)
        return self.findfolder(folder['name'])

