# API文档

## 序言

这是一个接口示例文档

## 修改记录

| 日期     | 修改人 | 修改接口 | 修改内容 |
| -------- | ------ | -------- | -------- |
| 2020/3/6 | yjs    | 全部     | 编写文档 |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |
|          |        |          |          |

## 全局错误码

| 错误码 | 错误描述       |
| ------ | -------------- |
| 1001   | 非Json格式     |
| 1002   | 关键信息缺失   |
| 1003   | 数据库处理出错 |
| 1004   | 查无此人       |

## 接口示例

### 新增待办事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/posttask

**请求方式：**

- POST

**参数：**

| 参数名     | 必选 | 类型     | 说明     |
| ---------- | ---- | -------- | -------- |
| user       | 是   | String   | 用户名   |
| todo       | 是   | Text     | 事项     |
| finishtime | 否   | Datetime | 结束时间 |

**返回示例：**

```json
{
    "task":{
        "finishtime":"2020-03-06 23:00:28",
        "todo":"test",
        "user":"joshuayu"
	}
}
```

**备注：**

- 需要以json格式请求

### 查看所有事项

**请求URL：**

- http://101.200.157.252//todo/api/v1.0/name/getalltasks

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": [
        {
            "addtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "done": 1,
            "finishtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "id": 2,
            "todo": "hello",
            "user": "yjs"
        },
        {
            "addtime": "Fri, 28 Feb 2020 21:40:51 GMT",
            "done": 0,
            "finishtime": "Fri, 28 Feb 2020 21:40:50 GMT",
            "id": 3,
            "todo": "hello",
            "user": "yjs"
        }
    ],
    "message": "",
    "status": 0
}
```

**备注：**name为所请求用户名

### 查看所有待办事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/gettodotasks

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": [
        {
            "addtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "done": 0,
            "finishtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "id": 2,
            "todo": "hello",
            "user": "yjs"
        },
        {
            "addtime": "Fri, 28 Feb 2020 21:40:51 GMT",
            "done": 0,
            "finishtime": "Fri, 28 Feb 2020 21:40:50 GMT",
            "id": 3,
            "todo": "hello",
            "user": "yjs"
        }
    ],
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 查看所有已完成事项

**请求URL：**

- http://101.200.157.252

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": [
        {
            "addtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "done": 1,
            "finishtime": "Fri, 28 Feb 2020 21:40:49 GMT",
            "id": 2,
            "todo": "hello",
            "user": "yjs"
        },
        {
            "addtime": "Fri, 28 Feb 2020 21:40:51 GMT",
            "done": 1,
            "finishtime": "Fri, 28 Feb 2020 21:40:50 GMT",
            "id": 3,
            "todo": "hello",
            "user": "yjs"
        }
    ],
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 删除一条事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/deletetask:<int:id>

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名，id为所选删除事项的id

### 删除所有事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/deletealltasks

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 删除已完成事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/deletedonetasks

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 删除待办事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/deletetodotasks

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 设置一条事项为待办事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/settasktodo:<int:id>

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名，id为所选设置事项的id

### 设置所有事项为待办事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/setalltaskstodo

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名，

### 设置一条事项为已完成事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/settaskdone:<int:id>

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名，id为所选设置事项的id

### 设置所有事项为已完成事项

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/setalltasksdone

**请求方式：**

- GET

**返回示例：**

```json
{
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 获取所有事项的数量

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/getalltasksnum

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": 6,
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 获取所有待办事项的数量

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/gettodotasksnum

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": 4,
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

### 获取所有已完成事项的数量

**请求URL：**

- http://101.200.157.252/todo/api/v1.0/name/getdonetasksnum

**请求方式：**

- GET

**返回示例：**

```json
{
    "data": 3,
    "message": "",
    "status": 0
}
```

**备注：**

- name为所请求用户名

## 数据库模型

- 事项表，储存事项信息

| 字段       | 类型        | 空   | 默认 | 注释         |
| ---------- | ----------- | ---- | ---- | ------------ |
| id         | int(11)     | 否   | 是   | 事项id       |
| user       | varchar(30) | 是   | 否   | 用户名       |
| todo       | text        | 是   | 否   | 事项内容     |
| done       | smallint(6) | 是   | 否   | 事项是否完成 |
| addtime    | datetime    | 是   | 是   | 添加时间     |
| finishtime | datetime    | 是   | 否   | 完成时间     |

