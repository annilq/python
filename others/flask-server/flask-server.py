from flask import Flask, url_for, redirect, jsonify, request, render_template,send_from_directory
from flask_pymongo import PyMongo
from bson.json_util import dumps
from controller.user import User
from controller.folder import Folder
from controller.task import Task

app = Flask(__name__,static_url_path='/static')

# connect to another MongoDB database on the same host
app.config['MONGO_DBNAME'] = 'react-todo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/react-todos'

MONGO = PyMongo(app)


@app.route('/')
def api_root():
    return send_from_directory('','index.html')

@app.route('/api/users')
def api_users():
    userDb = User(MONGO.db)
    users = userDb.get_users()
    # return json format
    return jsonify({'result': users})


@app.route('/api/tasks')
def api_tasks():
    taskDb = Task(MONGO.db)
    tasks = taskDb.get_tasks()
    return jsonify({'result': tasks})


@app.route('/api/folders')
def api_folders():
    folderDb = Folder(MONGO.db)
    folders = folderDb.get_folders()
    return jsonify({'result': folders})


@app.route('/api/register', methods=['POST'])
def api_register():
    userDb = User(MONGO.db)
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    user = userDb.findUser(name)
    if user:
        return jsonify({"code": -1, "message": "该用户已经注册过了"})
    else:
        data = {'name': name, "email": email}
        user = userDb.createUser(data)
        if user:
            print(type(user))
            # ObjectId('5a75c691e566330f9a86a052') is not JSON serializable不能序列化是个问题啊
            resp = app.make_response(
                dumps({
                    "code": 0,
                    "data": user,
                    "message": "注册成功"
                }))
            resp.headers['Content-Type'] = 'application/json'
            return resp
        else:
            jsonify({"code": -1, "message": "注册失败"})


@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('api_root'))


if __name__ == '__main__':
    app.run(debug=True,port=8080)