#### 项目说明
一个由后端由flask 与 mongodb提供restful接口，前端由react创建的todo app项目
1. 前端 [项目地址](https://github.com/annilq/react-todos)
    ```javascript
    git clone https://github.com/annilq/react-todos
    npm i
    npm start
    ```
2. flask只提供restful风格的数据接口
    1. code说明
        1. 0 成功
        2. -1 错误
        3. -2 过期 

#### 创建虚拟环境
1. 创建虚拟环境flask-server
```python
python3 -m venv flask-server
```
2. 进入python-todo-server并在当前目录激活环境(退出环境命令<code>deactivate</code>)
```python
source ./bin/activate
```
[用venv安装虚拟环境](https://docs.python.org/3/library/venv.html)

#### 安装项目依赖

1. 首先安装mongodb
参考[mongodb小记](https://annilq.github.io/2016/04/18/mongoDb/)

2. 安装依赖
```python
pip install Flask
pip install Flask-PyMongo
pip install Flask-Session
pip install Flask-Bcrypt
## 记录第三方模块
pip freeze > requirements.txt
## 安装txt文件里所记录的所有第三方模块
pip install -r requirements.txt

```
#### 项目注意事项
1. mongodb查询的返回值是bson数据结构,不能直接用<code>flask</code>的<code>jsonify</code>直接返回
    1. 需要自定义一个自定义一个方法将数据返回 [参考链接](https://github.com/annilq/python/blob/master/others/flask-server/util.py)
    2. 将查询数据中的<code>_id</code>由<code>ObjectId</code>格式转成<code>str</code>格式返回
#### 参考文档
1. [pymongo](http://api.mongodb.com/python/current/tutorial.html)
2. [flask-pymongo](http://flask-pymongo.readthedocs.io/en/latest/#flask_pymongo.PyMongo)
3. [Flask-Session](https://pythonhosted.org/Flask-Session/)
4. [Flask-Bcrypt](http://flask-bcrypt.readthedocs.io/en/latest/)

#### 项目地址
[flask-server](https://github.com/annilq/python/tree/master/others/flask-server)
