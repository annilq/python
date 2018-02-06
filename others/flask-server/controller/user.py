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

    def get_users(self):
        """当前方法只能在flask的上下文中运行，单独执行会报错"""
        output = []
        # return a collection cursor
        users = self.db.users.find()
        # convert to list
        for user in users:
            output.append({"name": user["name"], "email": user["email"]})
        return output

    def createUser(self,user):
        self.db.users.insert_one(user)
        return self.findUser(user['name'])

