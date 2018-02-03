from flask import Flask, url_for,redirect,jsonify,request
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
from user import User
app = Flask(__name__)

# connect to another MongoDB database on the same host
app.config['MONGO_DBNAME'] = 'react-todo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/react-todos'

MONGO = PyMongo(app)

@app.route('/')
def api_root():
    return 'welcome to this place'

@app.route('/api/users')
def api_users():
    users = get_users()
    # return json format
    return jsonify({'result': users})

@app.route('/api/tasks')
def api_tasks():
    tasks = get_tasks()
    return jsonify({'result': tasks})

@app.route('/api/folders')
def api_folders():
    folders = get_folders()
    return jsonify({'result': folders})

@app.route('/api/register',methods=['POST'])
def api_register():
    userDb=User(MONGO.db)    
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    user=userDb.findUser(name)
    if user:
        return jsonify({ "code": -1, "message": "该用户已经注册过了" })
    else:
        data={'name':name,"email":email}
        user=userDb.createUser(data)
        if user:
            print(type(user))
            # ObjectId('5a75c691e566330f9a86a052') is not JSON serializable不能序列化是个问题啊
            resp = app.make_response(dumps({ "code": 0,"data":user,"message": "注册成功" }))
            resp.headers['Content-Type'] = 'application/json'
            return resp
        else:
            jsonify({ code: -1, message: "注册失败" })

@app.route('/<path:path>')
def catch_all(path):
    return  redirect(url_for('api_root'))

# get users
def get_users():
    """当前方法只能在flask的上下文中运行，单独执行会报错"""
    output = []
    # return a collection cursor
    users = MONGO.db.users.find()
    # convert to list
    for user in users:
        output.append({"name": user["name"], "email": user["email"]})
    return output

def get_folders():
    """当前方法只能在flask的上下文中运行，单独执行会报错"""
    output = []
    # return a collection cursor
    folders = MONGO.db.folders.find()
    # convert to list
    for folder in folders:
        output.append({"userId":folder["userId"],"name":folder["name"]})
    return output

def get_tasks():
    """当前方法只能在flask的上下文中运行，单独执行会报错"""
    output = []
    # return a collection cursor
    tasks = MONGO.db.tasks.find()
    # convert to list
    for task in tasks:
        output.append({"userId":task["userId"],"name":task["name"]})
    return output


if __name__ == '__main__':
    app.run(debug=True)