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
    def createfolder(self,folder):
        self.db.folders.insert_one(folder)
        return self.findfolder(folder['name'])

