from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@127.0.0.1/RESTful_API"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30))
    todo = db.Column(db.Text)
    done = db.Column(db.SmallInteger, default=0)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    finishtime = db.Column(db.DateTime)

    @property
    def __repr__(self):
        return '<Task %r>' % self.name


tasks = [
    {
        'user': u'Buy groceries',
        'todo': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'addtime': '',
        'finishtime': ''
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


#
@app.errorhandler(400)
def JsonError(error):
    return make_response(jsonify(
        {
            "status": 1,
            "message": u"请求不是json格式",
            "data": None
        }
    ), 400)


@app.errorhandler(401)
def JsonError(error):
    return make_response(jsonify(
        {
            "status": 2,
            "message": u"信息不完全",
            "data": None
        }
    ), 401)


#添加⼀条新的待办事项
@app.route("/todo/api/v1.0/posttask", methods=["POST"])
def PostTasks():
    try:
        temp = request.get_json(force=True)
    except:
        abort(400)
    print(temp)
    if temp['user'] == '' or temp['todo'] == '':
        abort(401)

    task = Task(
        user=temp["user"],
        todo=temp['todo'],
        finishtime=temp['finishtime']
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': temp}), 201




#查看所有事项
@app.route("/todo/api/v1.0/<name>/getalltasks")
def GetAllTasks(name):
    datas = Task.query.filter_by(
        user=name
    ).all()
    templist = []
    for data in datas:
        temp = {
            "user": data.user,
            "todo": data.todo,
            "addtime": data.addtime,
            "finishtime": data.finishtime
        }
        templist.append(temp)
    return jsonify({
        "status": 0,
        "message": "",
        "data": templist,
    })


#查看所有待办事项
@app.route("/todo/api/v1.0/<name>/gettodotasks")
def GetTodoTasks(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    templist = []
    for data in datas:
        temp = {
            "user": data.user,
            "todo": data.todo,
            "done": data.done,
            "addtime": data.addtime,
            "finishtime": data.finishtime
        }
        templist.append(temp)
    return jsonify({
        "status": 0,
        "message": "",
        "data": templist,
    })


#查看所有已完成事项
@app.route("/todo/api/v1.0/<name>/getdonetasks")
def GetDoneTasks(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    templist = []
    for data in datas:
        temp = {
            "user": data.user,
            "todo": data.todo,
            "done": data.done,
            "addtime": data.addtime,
            "finishtime": data.finishtime
        }
        templist.append(temp)
    return jsonify({
        "status": 0,
        "message": "",
        "data": templist,
    })


#删除一条事项
@app.route("/todo/api/v1.0/<name>/deletetask:<int:id>")
def DeleteTask(name, id):
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ). first()
    db.session.delete(data)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#删除所有事项
@app.route("/todo/api/v1.0/<name>/deletealltasks")
def DeleteAllTasks(name):
    datas = Task.query.filter(
        Task.user == name,
    ).all()
    for data in datas:
        db.session.delete(data)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#删除已完成事项
@app.route("/todo/api/v1.0/<name>/deletedonetasks")
def DeleteDoneTasks(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    for data in datas:
        db.session.delete(data)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#删除待完成事项
@app.route("/todo/api/v1.0/<name>/deletetodotasks")
def DeleteTodoTasks(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    for data in datas:
        db.session.delete(data)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#设置一条待办事项待办
@app.route("/todo/api/v1.0/<name>/settasktodo:<int:id>")
def SetTaskTodo(name, id):
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ). first()
    data.done = 0
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#设置所有待办事项待办
@app.route("/todo/api/v1.0/<name>/setalltaskstodo")
def SetAllTasksTodo(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    templist = []
    for data in datas:
        data.done = 0
        temp = {
            "user": data.user,
            "todo": data.todo,
            "done": data.done,
            "addtime": data.addtime,
            "finishtime": data.finishtime
        }
        templist.append(temp)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
        "data": templist,
    })


#设置一条已完成事项为已完成
@app.route("/todo/api/v1.0/<name>/settaskdone:<int:id>")
def SetTaskdone(name, id):
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ).first()
    data.done = 1
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
    })


#设置所有已完成事项为已完成
@app.route("/todo/api/v1.0/<name>/setalltasksdone")
def SetAllTasksDone(name):
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    templist = []
    for data in datas:
        data.done = 1
        temp = {
            "user": data.user,
            "todo": data.todo,
            "done": data.done,
            "addtime": data.addtime,
            "finishtime": data.finishtime
        }
        templist.append(temp)
    db.session.commit()
    return jsonify({
        "status": 0,
        "message": "",
        "data": templist,
    })


#获取所有事项的数量
app.route("/todo/api/v1.0/<name>/getalltasksnum")
def GetAllTasksNum(name):
    datanum = Task.query.filter(
        Task.user == name,
    ).count()
    return jsonify({
        "status": 0,
        "message": "",
        "data": datanum,
    })


#获取所有待办事项的数量
@app.route("/todo/api/v1.0/<name>/gettotasksnum")
def GetTodoTasksNum(name):
    datanum = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).count()
    return jsonify({
        "status": 0,
        "message": "",
        "data": datanum,
    })


# 获取所有已完成事项的数量
@app.route("/todo/api/v1.0/<name>/getdonetasksnum")
def GetDoneTasksNum(name):
    datanum = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).count()
    return jsonify({
        "status": 0,
        "message": "",
        "data": datanum,
    })

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)
