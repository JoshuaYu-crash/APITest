# APITest
西二第四轮考核接口代码和说明

### 如何部署

#### 1.安装MySQL

```
sudo apt-get update
```

更新已有的包，然后输入：

```
sudo apt-get install mysql-server
apt install mysql-client
apt install libmysqlclient-dev
```

安装MySQL服务，期间需要设置登录密码，自己设置并记住。输入

```
sudo netstat -tap | grep mysql
```

查看自己是否安装成功，接着输入

```
mysql -u root -p+密码
```

登录数据库并输入

```
create database RESTful_API
```

创建项目的数据库，等待后续导入数据。

#### 2.上传数据和代码

这里使用[Xftp](<https://www.netsarang.com/zh/xftp/>)来上传数据，首先上传项目到/var/www/目录下，使用cmd命令到自己本地MySQL数据库bin目录下，输入

```
mysqldump -uroot -p RESTful_API > 导出位置
```

然后一并上传到服务器/var/www/目录下，在服务器上打开创建的空白RESTful_API数据库，在其中输入

```
source /var/www/RESTful_API.sql
```

看到成功导入即可

#### 3.安装uwsgi

```
pip install uwsgi
```

在项目目录创建Flask_API_uwsgi.ini文件，在其中编辑

```python
[uwsgi]
#项目目录
base = /var/www/RESTful_API

#项目中Flask对象
app = manage
module = %(app)

#处理器数
processes = 4

#线程数
threads = 2

#socket的文件位置
socket = /var/www/demoapp/%n.sock

#随便设置一个认证码
chmod-socket    = 666

#项目中Flask对象
callable = app

```

然后再输入以下代码运行uwsgi

```
uwsgi --ini Flask_API_uwsgi.ini
```

观察代码是否能成功运行，如果可以，接着下一步

#### 4.安装nginx

安装并运行nginx

```
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```

删除nginx原本配置文件

```
sudo rm /etc/nginx/sites-enabled/default
```

再在项目目录添加Flask_API_nginx.conf配置文件并添加一下配置

```javascript
server {
    listen      80;
    server_name 127.0.0.1：0000;//服务器公网IP
    charset     utf-8;
    client_max_body_size 75M;

    location / { try_files $uri @yourapplication; }
    location @yourapplication {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/Flask_API/Flask_API_uwsgi.sock;
    }
}
```

访问该服务器IP观察是否有数据返回，完成部署！

### 接口使用

请参考API使用文档