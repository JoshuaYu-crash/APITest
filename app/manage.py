from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
            "status": 1001,
            "message": u"Wrong Json Type",
            "data": None
        }
    ), 400)


@app.errorhandler(406)
def InformationError(error):
    return make_response(jsonify(
        {
            "status": 1002,
            "message": u"Incomplete Information",
            "data": None
        }
    ), 406)


@app.errorhandler(500)
def DatabaseError(error):
    return make_response(jsonify(
        {
            "status": 1003,
            "message": u"Database Processing Failed",
            "data": None
        }
    ), 500)


@app.errorhandler(403)
def UserError(error):
    return make_response(jsonify(
        {
            "status": 1004,
            "message": u"User Does Not Exist",
            "data": None
        }
    ), 403)


# 添加⼀条新的待办事项
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
    try:
        db.session.add(task)
        db.session.commit()
    except:
        abort(402)
    return jsonify({'task': temp}), 201


# 查看所有事项
@app.route("/todo/api/v1.0/<name>/getalltasks")
def GetAllTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter_by(
        user=name
    ).all()
    templist = []
    for data in datas:
        temp = {
            "id": data.id,
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


# 查看所有待办事项
@app.route("/todo/api/v1.0/<name>/gettodotasks")
def GetTodoTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    templist = []
    for data in datas:
        temp = {
            "id": data.id,
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


# 查看所有已完成事项
@app.route("/todo/api/v1.0/<name>/getdonetasks")
def GetDoneTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    templist = []
    for data in datas:
        temp = {
            "id": data.id,
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


# 删除一条事项
@app.route("/todo/api/v1.0/<name>/deletetask:<int:id>")
def DeleteTask(name, id):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ).first()
    try:
        db.session.delete(data)
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 删除所有事项
@app.route("/todo/api/v1.0/<name>/deletealltasks")
def DeleteAllTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
    ).all()
    try:
        for data in datas:
            db.session.delete(data)
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 删除已完成事项
@app.route("/todo/api/v1.0/<name>/deletedonetasks")
def DeleteDoneTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    try:
        for data in datas:
            db.session.delete(data)
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 删除待完成事项
@app.route("/todo/api/v1.0/<name>/deletetodotasks")
def DeleteTodoTasks(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    try:
        for data in datas:
            db.session.delete(data)
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 设置一条待办事项待办
@app.route("/todo/api/v1.0/<name>/settasktodo:<int:id>")
def SetTaskTodo(name, id):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ).first()
    data.done = 0
    try:
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 设置所有事项待办事项
@app.route("/todo/api/v1.0/<name>/setalltaskstodo")
def SetAllTasksTodo(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 1
    ).all()
    for data in datas:
        data.done = 0
    try:
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": ""
    })


# 设置一条待办事项为已完成事项
@app.route("/todo/api/v1.0/<name>/settaskdone:<int:id>")
def SetTaskdone(name, id):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    data = Task.query.filter(
        Task.user == name,
        Task.id == id
    ).first()
    data.done = 1
    try:
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 设置所有事项为已完成事项
@app.route("/todo/api/v1.0/<name>/setalltasksdone")
def SetAllTasksDone(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datas = Task.query.filter(
        Task.user == name,
        Task.done == 0
    ).all()
    templist = []
    for data in datas:
        data.done = 1
    try:
        db.session.commit()
    except:
        abort(402)
    return jsonify({
        "status": 0,
        "message": "",
    })


# 获取所有事项的数量
@app.route("/todo/api/v1.0/<name>/getalltasksnum")
def GetAllTasksNum(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
    datanum = Task.query.filter(
        Task.user == name,
    ).count()
    return jsonify({
        "status": 0,
        "message": "",
        "data": datanum,
    })


# 获取所有待办事项的数量
@app.route("/todo/api/v1.0/<name>/gettodotasksnum")
def GetTodoTasksNum(name):
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
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
    if Task.query.filter_by(
        user=name
    ).count() == 0:
        abort(403)
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
    app.run()
