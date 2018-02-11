from flask import Flask, url_for, redirect, jsonify, request, session, send_from_directory
from flask_pymongo import PyMongo
from flask_session import Session
from flask_bcrypt import Bcrypt

from util import get_json_response
from controller.user import User
from controller.folder import Folder
from controller.task import Task

app = Flask(__name__, static_url_path='/static')
# session config
SESSION_TYPE = 'mongodb'
app.config.from_object(__name__)
Session(app)

# connect to another MongoDB database on the same host
app.config['MONGO_DBNAME'] = 'react-todo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/react-todos'

MONGO = PyMongo(app)

# 加密
bcrypt = Bcrypt(app)


@app.route('/api/users')
def api_users():
    userDb = User(MONGO.db)
    users = userDb.get_users()
    # return json format
    return jsonify({'result': users})


@app.route('/api/tasks')
def api_tasks():
    taskDb = Task(MONGO.db)
    # convert args todict
    query=request.args.to_dict()
    if query.get("star","")=="true":
        query['star']=True
    if query.get("status","")=="1":
        query['status']=True
    tasks = taskDb.get_tasks(query)
    return get_json_response(app, data=tasks)


@app.route('/api/folders')
def api_folders():
    folderDb = Folder(MONGO.db)
    foldertype = request.args.get('type',"")
    folders = folderDb.get_folders(foldertype)
    return get_json_response(app, data=folders)

# 注册接口
@app.route('/api/register', methods=['POST'])
def api_register():
    userDb = User(MONGO.db)
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = userDb.find_user(name)
    if user:
        return jsonify({"code": -1, "message": "该用户已经注册过了"})
    else:
        data = {'name': name, "email": email, 'password': pw_hash}
        user = userDb.createUser(data)
        if user:
            print(type(user))
            # ObjectId('5a75c691e566330f9a86a052') is not JSON serializable不能序列化是个问题啊
            resp = get_json_response(app, data=user, message="注册成功")
            return resp
        else:
            return jsonify({"code": -1, "message": "注册失败"})

# 登陆接口
@app.route('/api/login', methods=['POST'])
def api_login():
    userDb = User(MONGO.db)
    name = request.json['name']
    password = request.json['password']
    user = userDb.find_user(name)
    if user:
        if bcrypt.check_password_hash(user['password'], password):
            resp = get_json_response(app, data=user, message="登陆成功")
            session['uid'] = str(user["_id"])
            return resp
        else:
            return jsonify({"code": -1, "message": "用户名或密码错误"})
    else:
        return jsonify({"code": -1, "message": "用户不存在"})

# 退出登录接口
@app.route('/api/logout')
def api_logout():
    session.pop('username', None)
    return jsonify({"code": 0, "message": "退出成功"})


# before_request hook


@app.before_request
def before_action():
    if '/api/' in request.path:
        if '/api/login' not in request.path:
            if 'userId' not in session:
                return jsonify({"code": -1, "message": "登陆过期"})


@app.route('/')
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('', 'index.html')


app.secret_key = 'annilq'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
