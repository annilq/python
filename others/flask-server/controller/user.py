from flask_pymongo import PyMongo
class User():
    def __init__(self,db):
        super().__init__()
        self.db=db
    def findUser(self,name):
        user = self.db.users.find_one({"name":name})
        if user:
            return user
        else:
            return None
    def createUser(self,user):
        self.db.users.insert_one(user)
        return self.findUser(user['name'])

