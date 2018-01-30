from flask import Flask, url_for
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

# connect to another MongoDB database on the same host
app.config['MONGO_DBNAME'] = 'react-todo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/react-todos'

MONGO = PyMongo(app)


@app.route('/')
def api_root():
    output = []
    users = get_users()
    # return json format
    return jsonify({'result': users})


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

# get users
def get_users():
    """当前方法只能在flask的上下文中运行，单独执行会报错"""
    output = []
    # return a collection cursor
    users = MONGO.db.users.find()
    # convert to list
    for user in users:
        print(user["name"])
        output.append({"name": user["name"], "email": user["email"]})
    return output


if __name__ == '__main__':
    app.run()