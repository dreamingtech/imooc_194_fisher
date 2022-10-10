
慕课手记
http://www.imooc.com/t/4294850#Article


## 第2章 Flask的基本原理与核心知识

### 2-1 鱼书是一个什么样的产品

- 一句话概括产品的功能
  - 由简到繁，产品早期开发时，必须要围绕着一个核心点来做，在后期再围绕着这个核心点逐渐扩展

- 鱼书
  - http://yushu.talelin.com
  - 将自己不要的书，免费赠送给他人

- 鱼书核心功能
  - 搜索书籍
  - 选择要赠送的书籍 > 向他人赠送书籍
  - 选择自己想要的书籍 > 向他人索要书籍

- 建议
  - 学完课程后，完成一个类似的网站
  - 传音二手交易平台，赠送平台


### 2-3 使用官方推荐的pipenv创建虚拟环境

pipenv
https://github.com/pypa/pipenv
https://pipenv.pypa.io/en/latest/

https://docs.readthedocs.io/en/stable/tutorial/

安装 pipenv
推荐 pipenv 创建的虚拟环境和项目绑定

```shell

pip install pipenv

# pip is configured with locations that require TLS/SSL, 
# however the ssl module in Python is not available
# https://stackoverflow.com/questions/45954528/

# For Windows 10 if you want use pip in normal cmd, not only in Anaconda prompt. you need add 3 environment paths. like the followings:

# D:\Anaconda3 
# D:\Anaconda3\Scripts
# D:\Anaconda3\Library\bin 

# 把以上三个目录添加到环境变量中，如果使用的是 miniconda, 添加以下 3 个目录到环境变量

# C:\ProgramFiles\Miniconda3
# C:\ProgramFiles\Miniconda3\Scripts
# C:\ProgramFiles\Miniconda3\Library\bin 

pip install pipenv
# Defaulting to user installation because normal site-packages is not writeable
# Looking in indexes: https://pypi.douban.com/simple
# Collecting pipenv
#   Downloading https://pypi.doubanio.com/packages/43/14/fb9a7c9b104ffa64d631f6c3ab2dcb9b7ec7ec52d32f82466e9b785bbac0/pipenv-2022.9.24-py2.py3-none-any.whl (3.3 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 1.9 MB/s eta 0:00:00
# Collecting virtualenv
#   Downloading https://pypi.doubanio.com/packages/c1/23/9dc3c3fc959ad442397dd90cbc9ea2eca7c8a140d242c6e4222675ea9f86/virtualenv-20.16.5-py3-none-any.whl (8.8 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.8/8.8 MB 1.9 MB/s eta 0:00:00
# Requirement already satisfied: setuptools>=36.2.1 in c:\programfiles\miniconda3\lib\site-packages (from pipenv) (61.2.0)
# Requirement already satisfied: certifi in c:\programfiles\miniconda3\lib\site-packages (from pipenv) (2022.6.15)
# Collecting virtualenv-clone>=0.2.5
#   Downloading https://pypi.doubanio.com/packages/21/ac/e07058dc5a6c1b97f751d24f20d4b0ec14d735d77f4a1f78c471d6d13a43/virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
# Collecting distlib<1,>=0.3.5
#   Downloading https://pypi.doubanio.com/packages/76/cb/6bbd2b10170ed991cf64e8c8b85e01f2fb38f95d1bc77617569e0b0b26ac/distlib-0.3.6-py2.py3-none-any.whl (468 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.5/468.5 kB 1.8 MB/s eta 0:00:00
# Collecting platformdirs<3,>=2.4
#   Downloading https://pypi.doubanio.com/packages/ed/22/967181c94c3a4063fe64e15331b4cb366bdd7dfbf46fcb8ad89650026fec/platformdirs-2.5.2-py3-none-any.whl (14 kB)
# Collecting filelock<4,>=3.4.1
#   Using cached https://pypi.doubanio.com/packages/94/b3/ff2845971788613e646e667043fdb5f128e2e540aefa09a3c55be8290d6d/filelock-3.8.0-py3-none-any.whl (10 kB)
# Installing collected packages: distlib, virtualenv-clone, platformdirs, filelock, virtualenv, pipenv
#   WARNING: The script virtualenv-clone.exe is installed in 'C:\Users\zhiwei.wu\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#   WARNING: The script virtualenv.exe is installed in 'C:\Users\zhiwei.wu\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#   WARNING: The scripts pipenv-resolver.exe and pipenv.exe are installed in 'C:\Users\zhiwei.wu\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed distlib-0.3.6 filelock-3.8.0 pipenv-2022.9.24 platformdirs-2.5.2 virtualenv-20.16.5 virtualenv-clone-0.5.7

```

pipenv

Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]
  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --three                         Use Python 3 when creating virtualenv.
                                  Deprecated
  --clear                         Clears caches (pipenv, pip).  [env var:
                                  PIPENV_CLEAR]
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  verify        Verify the hash in Pipfile.lock is up-to-date.


如果当前目录没有创建虚拟环境, 会给当前目录创建虚拟环境并绑定
如果已经创建虚拟环境, 会进入到虚拟环境中
pipenv shell

D:\projects_study\imooc_194_fisher>pipenv shell
Launching subshell in virtual environment...
Microsoft Windows [版本 10.0.19044.1766]
(c) Microsoft Corporation。保留所有权利。

(imooc_194_fisher-yaRaPKxN) D:\projects_study\imooc_194_fisher>pip list
Package    Version
---------- -------
pip        22.2.2
setuptools 65.3.0
wheel      0.37.1


pipenv install flask
Installing flask...
Adding flask to Pipfile's [packages]...
Installation Succeeded
Pipfile.lock (16c839) out of date, updating to (9536c4)...
Locking [packages] dependencies...
 Locking...Building requirements...
Resolving dependencies...
Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (9536c4)!
Installing dependencies from Pipfile.lock (9536c4)...

退出虚拟环境
exit

pipenv uninstall flask
pipenv install flask

查看包依赖
pipenv graph

Flask==2.2.2
  - click [required: >=8.0, installed: 8.1.3]
    - colorama [required: Any, installed: 0.4.5]
  - importlib-metadata [required: >=3.6.0, installed: 4.12.0]
    - zipp [required: >=0.5, installed: 3.8.1]
  - itsdangerous [required: >=2.0, installed: 2.1.2]
  - Jinja2 [required: >=3.0, installed: 3.1.2]
    - MarkupSafe [required: >=2.0, installed: 2.1.1]
  - Werkzeug [required: >=2.2.2, installed: 2.2.2]
    - MarkupSafe [required: >=2.1.1, installed: 2.1.1]


(imooc_194_fisher-yaRaPKxN) D:\projects_study\imooc_194_fisher>flask
Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.

Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  An application to load must be given with the '--app' option, 'FLASK_APP'
  environment variable, or with a 'wsgi.py' or 'app.py' file in the current
  directory.

Options:
  -e, --env-file FILE   Load environment variables from this file. python-
                        dotenv must be installed.
  -A, --app IMPORT      The Flask application or factory function to load, in
                        the form 'module:name'. Module can be a dotted import
                        or file path. Name is not required if it is 'app',
                        'application', 'create_app', or 'make_app', and can be
                        'name(args)' to pass arguments.
  --debug / --no-debug  Set debug mode.
  --version             Show the Flask version.
  --help                Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.

查看创建的虚拟环境保存的路径

pipenv --venv

C:\Users\dm\.virtualenvs\imooc_194_fisher-yaRaPKxN


### 2-4 开发工具推荐

- pycharm

- Xampp mysql

  - https://www.apachefriends.org/


- Navicat 数据库可视化管理工具


### 2-7 flask最小原型与唯一URL原则


```python

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


# flask 中的视图函数就是 MVC 中的 C(Controller)
@app.route("/hello")
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)


```

```shell

 * Serving Flask app 'applications'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.23:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 391-656-137

```


访问 http://127.0.0.1:5001/hello 可以获取数据

但访问 http://127.0.0.1:5001/hello/ 就会返回 404 NOT FOUND

修改 route 路由为 "/hello/", 就可以兼容 /hello 和 /hello/ 两种地址的访问了

但此时如果访问 http://127.0.0.1:5001/hello 时会 301 跳转到 http://127.0.0.1:5001/hello/ 中


### 2-8 路由的另一种注册方法

supervisor 监听文件改动，自动重启程序

```python

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


# 第一种注册路由的方式: 使用装饰器
# flask 中的视图函数就是 MVC 中的 C(Controller)
@app.route("/hello")
def hello():
    return 'Hello World!'


def hi():
    return 'Hi World!'


# 第二种注册路由的方式: 使用 add_url_rule
app.add_url_rule(rule='/hi/', view_func=hi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)

```

- 基于类的视图, 也称为 "即插视图"
  - 当使用基于类的视图时，只能使用 add_url_rule 的方法手动注册路由

host='0.0.0.0'

ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:37ff:fec0:9a52  prefixlen 64  scopeid 0x20<link>
        ether 02:42:37:c0:9a:52  txqueuelen 0  (Ethernet)
        RX packets 54447  bytes 49318791 (49.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 57570  bytes 47192179 (47.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.23  netmask 255.255.255.0  broadcast 10.0.0.255
        inet6 fe80::5054:ff:feaf:4389  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:af:43:89  txqueuelen 1000  (Ethernet)
        RX packets 13470601  bytes 6577124290 (6.5 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 14596435  bytes 6163312665 (6.1 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 260288  bytes 31057449 (31.0 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 260288  bytes 31057449 (31.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

默认 host 为 127.0.0.1, 只能在本机通过 localhost:5000/hello/ 或 127.0.0.1:5000/hello 访问

如果绑定 10.0.0.23, 则所有内网机器都能通过 http://10.0.0.23:5000/hello/ 来访问
但本机就不能再通过 localhost:5000/hello/ 或 127.0.0.1:5000/hello 访问

绑定的是某一块网卡对应的地址，所以也可以说是绑定某块网卡

绑定 0.0.0.0 时, 访问任意一块网卡的地址都可以访问到 web 服务


为什么访问以下地址也可以 ??

http://127.0.0.0:5000/hi/
http://127.0.0.3:5000/hi/


部署的最基本原则是保证开发环境的源码和生产环境的源码是镜像关系



### 配置文件的使用

在 application.py 所在根目录中新建 config.py

config.py

```python
# -*- coding: utf-8 -*-

# 配置文件中的变量必须全部大写
# flask.config.Config.from_object
# if key.isupper(): 只有全部大写时才能正确读取
DEBUG = True

SERVER_NAME = '0.0.0.0:5002'

```

修改 applications.py, 使用配置文件

```python

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# 导入配置文件方法 1
app.config.from_pyfile('config.py')
# 导入配置文件方法 2
# from_object + 模块的路径
# app.config.from_object('config')


# 第一种注册路由的方式: 使用装饰器
# flask 中的视图函数就是 MVC 中的 C(Controller)
@app.route("/hello")
def hello():
    return 'Hello World!'


def hi():
    return 'Hi World!'


# 第二种注册路由的方式: 使用 add_url_rule
app.add_url_rule(rule='/hi/', view_func=hi)

if __name__ == '__main__':
    app.run()

```
运行服务时会有如下 warning
/home/ubuntu/.pyenv/versions/flask/lib/python3.9/site-packages/flask/app.py:2218: UserWarning: Current server name '127.0.0.1:5002' doesn't match configured server name '0.0.0.0:5002'
  return self.url_map.bind_to_environ(

且此时访问任何网址都是 404

```

curl http://127.0.0.1:5002/hello
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

```

原因：
config 中配置了 SERVER_NAME = '0.0.0.0:5002' 后就会出现上面的问题，参考以下答案。
结论是：
**不要在 config 中配置 SERVER_NAME 属性**

https://icode.best/i/31321039924483
https://blog.csdn.net/XC_SunnyBoy/article/details/115676135
https://www.4k8k.xyz/article/XC_SunnyBoy/115676135
https://stackoverflow.com/questions/47002617/flasks-built-in-server-always-404-with-server-name-set


生产环境一般使用 nginx + uwsgi 来运行 flask 应用。 不再使用 flask 自带的服务 app.run 来运行 flask 服务

nginx 作为前置服务，接收浏览器/用户发送的请求，再把请求转发给 uwsgi, uwsgi 加载 fisher 模块来启动服务

视图函数

如果设置 status 为 301，同时设置 headers 中的 location 为 http://www.bing.com 就会自动重定向到 bing.com

content-type: text/plain
content-type: text/html
content-type: application/json

### 返回响应的方式和响应状态码

```python

# -*- coding: utf-8 -*-

from flask import Flask, make_response

app = Flask(__name__)

# 导入配置文件方法 1
# app.config.from_pyfile('config.py')
# 导入配置文件方法 2
# from_object + 模块的路径
app.config.from_object('config')


# 第一种注册路由的方式: 使用装饰器
# flask 中的视图函数就是 MVC 中的 C(Controller)
@app.route("/hello")
def hello():
    # 视图函数除了返回自定义的字符串外, 还会对字符串进行进一步的封装.
    # 1. 把自定义的文本进行渲染后再返回
    # 2. 还会返回 status code,
    # 3. 在 response headers 中添加 Content-Type, 默认为 text/html
    # 返回响应 1
    return 'Hello World!'
    # 返回响应 2
    return 'Hello World', 200, {'Content-Type': 'text/html'}
    # 返回响应 3
    # 以 text/html 返回时会把返回的 html 文本内容渲染为 html 标签
    return '<html></html>', 200, {'Content-Type': 'text/html'}
    # 以 text/plain 返回时会把返回的 html 文本内容渲染为 纯文本内容
    # 返回响应 4
    return '<html></html>', 200, {'Content-Type': 'text/plain'}
    # 301 状态码和 location
    return '<html></html>', 301, {'Content-Type': 'text/plain', 'Location': 'https://www.bing.com'}
    # 返回响应 5
    response = make_response('Hello World', 200)
    # 设置 headers 方式1, 推荐
    response.headers['Content-Type'] = 'text/html'
    # 设置 headers 方式2, 不推荐, 会覆盖 response 中 flask 自动设置的 headers 项
    response.headers = {
        'Content-Type': 'text/html'
    }
    return response


def hi():
    return 'Hi World!'


# 第二种注册路由的方式: 使用 add_url_rule
app.add_url_rule(rule='/hi/', view_func=hi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


```

### 3-1 搜索而不是拍照上传


- 鱼书功能
  - 搜索书籍
  - 选择要赠送的书籍
    - 向他人赠送书籍
  - 选择自己想要的书籍
    - 向他人索要书籍

- 不知道如何开始做一个项目。
  - 从项目最核心的需求开始，本项目的核心需求是 "向他人赠送书籍"
  - 需求 > 数据 > 页面 > 实现


向他人赠送书籍，首先要有书籍信息，但是不需要做电商一样的商品管理功能

可以根据书名，作者，isbn 来搜索图书

### 3-2 书籍搜索与查询 1-数据API

- 关键字搜索
  - http://t.talelin.com/v2/book/search?q={}&start={}&count={}
  - http://t.talelin.com/v2/book/search?q=我与

- isbn 搜索
  - http://t.talelin.com/v2/book/isbn/{isbn}
  - http://t.talelin.com/v2/book/isbn/9787531324362

```json

{
    "author": [
        "史铁生"
    ],
    "binding": "平装",
    "category": "散文",
    "id": 12248,
    "image": "https://img1.doubanio.com/lpic/s1151479.jpg",
    "images": {
        "large": "https://img1.doubanio.com/lpic/s1151479.jpg"
    },
    "isbn": "9787531324362",
    "pages": "399",
    "price": "25.00元",
    "pubdate": "2002-5",
    "publisher": "春风文艺出版社",
    "subtitle": "史铁生代表作",
    "summary": "收有“午餐半小时”、“我的遥远的清平湾”、“命若琴弦”、“第一人称”、“两个故事”等15篇史铁生的代表作。",
    "title": "我与地坛",
    "translator": []
}

```

  - 图书不存在时, status code = 404
  - http://t.talelin.com/v2/book/isbn/9787531324363

```json

{
    "msg": "book not found",
    "code": 2000
}

```

- 豆瓣API
  - https://api.douban.com/v2/book

### 3-3 书籍搜索与查询 2-搜索关键字

http://yushu.talelin.com/book/search?q=%E5%A4%A9%E4%B8%8B

http://localhost:5002/book/search/天下/1
http://t.

taobao 的搜索需要用户选择是商品搜索还是店铺搜索, 但鱼书不需要用户区分是 关键字搜索还是 isbn 搜索
可以在代码中根据用户的输入进行判断

q: 关键字搜索
start 开始
count 每页数据量
isbn isbn 搜索

4个参数简化
q: 关键字搜索 + isbn 搜索
page: 合并 start + count


修改 applications.py


```python
# applications.py
# -*- coding: utf-8 -*-

from flask import Flask, make_response

from libs import is_isbn_or_key

app = Flask(__name__)

# app.config.from_pyfile('config.py')
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    return 'Hello Fisher'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

新建 libs 模块, 新建 libs.is_isbn_or_key 函数, 判断用户的输入是 isbn 搜索还是普通关键词搜索

```python
# libs.__init__.py

# -*- coding: utf-8 -*-

def is_isbn_or_key(keyword: str):
    """
    区分用户输入的搜索关键字是 普通搜索还是关键词搜索
    isbn13: 13个0到9的数字组成
    isbn10: 老的标准, 10个0到9的数字组成, 含有一些 '-'
    :param keyword:
    :return:
    """
    isbn_or_key = 'key'
    # 把大概率出现假的条件放在最前面
    # 把需要 io 操作的判断放在后面, 如查询数据库, 读取文件等
    if len(keyword) == 13 and keyword.isdigit():
        isbn_or_key = 'isbn'
    if '-' in keyword and len(keyword.replace('-', '')) == 10 and keyword.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


```

### 3-7 从API获取数据

新建 libs/httper.py, 完成调用接口返回数据的工作

```python

# -*- coding: utf-8 -*-
import requests


class Http(object):
    @staticmethod
    def get(url: str, return_json: bool = True):
        """
        大部分接口都是 restful 风格的, 要求返回的数据都是 json 格式的
        :param url:
        :param return_json:
        :return:
        """
        resp = requests.get(url)
        # 判断状态码
        # 搜索图书不存在时, 状态码会为 404
        if resp.status_code != 200:
            return {} if return_json else ''
        return resp.json() if return_json else resp.text


class BookGetter(object):
    """
    调用 api 获取图书信息
    """
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&start={}&count={}'
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'

    @classmethod
    def search_by_isbn(cls, isbn: str):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword: str, start=0, count=15):
        url = cls.keyword_url.format(keyword, start, count)
        result = Http.get(url)
        return result

```

修改 applications.py, 获取并返回数据

```python

# -*- coding: utf-8 -*-

from flask import Flask, make_response, jsonify

from libs import is_isbn_or_key
from libs.httper import BookGetter

app = Flask(__name__)

# app.config.from_pyfile('config.py')
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
    # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
    # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
    # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
    isbn_or_key = is_isbn_or_key(keyword=q)
    if isbn_or_key == 'isbn':
        books = BookGetter.search_by_isbn(isbn=q)
    else:
        books = BookGetter.search_by_keyword(keyword=q)
    # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
    # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
    # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
    # return books
    return jsonify(books)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

http://127.0.0.1:5000/book/search/9787531324362/1
http://127.0.0.1:5000/book/search/我与地坛/1
必须使用 urlencoded 地址才能正确获取数据
http://127.0.0.1:5000/book/search/%E6%88%91%E4%B8%8E%E5%9C%B0%E5%9D%9B/1


写 api 的难点不是代码实现, 而是路由的设计, 如何设计才能更好的表达数据和资源

API + JS (单页面, NG, VUE, React) 前后端分离 SEO
TP5 + 小程序 webview
多页面网站 ajax


### 3-9 将视图函数拆分到单独的文件中

不推荐把所有视图函数都放在一个文件中

- 1. 函数太多, 代码太长, 不利于后期维护
- 2. 不同的业务模型对应的视图函数要放在不同的文件中
  - search 是图书相关的, 单独所以放在一个 book 的视图文件中
  - 与用户相关的注册, 登录, 修改密码等, 可以放在 user 的视图文件中

新建 views 模块，保存所有的视图文件

新建 views/book.py

```python

# views/book.py

# -*- coding: utf-8 -*-
from flask import jsonify

from applications import app
from libs import is_isbn_or_key
from libs.httper import BookGetter


@app.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
    # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
    # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
    # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
    isbn_or_key = is_isbn_or_key(keyword=q)
    if isbn_or_key == 'isbn':
        books = BookGetter.search_by_isbn(isbn=q)
    else:
        books = BookGetter.search_by_keyword(keyword=q)
    # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
    # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
    # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
    # return books
    return jsonify(books)

```

修改 applications.py, 引入视图文件

```python

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# app.config.from_pyfile('config.py')
app.config.from_object('config')

# 必须要在入口文件中引入视图文件才能执行视图
from views import book


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

运行 flask 服务，测试请求

```shell

curl http://127.0.0.1:5000/book/search/%E6%88%91%E4%B8%8E%E5%9C%B0%E5%9D%9B/1

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>


```

```shell

ssh://ubuntu@162.62.134.181:22/home/ubuntu/.pyenv/versions/flask/bin/python -u /data/dev/fisher/applications.py
 * Serving Flask app 'applications'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.23:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 912-315-642
127.0.0.1 - - [09/Oct/2022 18:53:22] "GET /book/search/我与地坛/1 HTTP/1.1" 404 -

```

出现 404 的原因： 循环引入


### 3-10 深入了解flask路由


客户端(浏览器) > http://yushu.im/book/search > 视图函数 search

url1 ----(endpoint)----> search1

url2 ----(endpoint)----> search2

url3 ----(endpoint)----> search3

每一个/种 url 对应一个 endpoint 和 视图函数

在通过视图反向构建 url 时, endpoint 的用处就体现出来了


在 flask.scaffold.Scaffold.route 中 `endpoint = options.pop("endpoint", None)` 和 `return f` 中打上断点，使用调试模式运行 flask 应用

进入到 flask.app.Flask.add_url_rule 函数中


endpoint 参数可以省略，此时 flask 会把 view_func 的函数名作为 endpoint 的值
app.add_url_rule(rule='url', view_func=func, endpoint='')


flask.app.Flask.add_url_rule

```python


    @setupmethod
    def add_url_rule(
        self,
        rule: str,
        endpoint: t.Optional[str] = None,
        view_func: t.Optional[ft.RouteCallable] = None,
        provide_automatic_options: t.Optional[bool] = None,
        **options: t.Any,
    ) -> None:
        if endpoint is None:
            endpoint = _endpoint_from_view_func(view_func)  # type: ignore
        options["endpoint"] = endpoint
        methods = options.pop("methods", None)

        # if the methods are not given and the view_func object knows its
        # methods we can use that instead.  If neither exists, we go with
        # a tuple of only ``GET`` as default.
        if methods is None:
            methods = getattr(view_func, "methods", None) or ("GET",)
        if isinstance(methods, str):
            raise TypeError(
                "Allowed methods must be a list of strings, for"
                ' example: @app.route(..., methods=["POST"])'
            )
        methods = {item.upper() for item in methods}

        # Methods that should always be added
        required_methods = set(getattr(view_func, "required_methods", ()))

        # starting with Flask 0.8 the view_func object can disable and
        # force-enable the automatic options handling.
        if provide_automatic_options is None:
            provide_automatic_options = getattr(
                view_func, "provide_automatic_options", None
            )

        if provide_automatic_options is None:
            if "OPTIONS" not in methods:
                provide_automatic_options = True
                required_methods.add("OPTIONS")
            else:
                provide_automatic_options = False

        # Add the required methods now.
        methods |= required_methods

        rule = self.url_rule_class(rule, methods=methods, **options)
        rule.provide_automatic_options = provide_automatic_options  # type: ignore

        self.url_map.add(rule)
        if view_func is not None:
            old_func = self.view_functions.get(endpoint)
            if old_func is not None and old_func != view_func:
                raise AssertionError(
                    "View function mapping is overwriting an existing"
                    f" endpoint function: {endpoint}"
                )
            self.view_functions[endpoint] = view_func

```

self.url_map.add(rule)， rule 规则是保存在 url_map 中的

self.view_functions[endpoint] = view_func，视图函数是保存在 view_functions 中的

self 就是所运行的 flask 应用

```

<Flask 'applications'>

```
self.url_map 中保存的值

```

Map([<Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
 <Rule '/book/search/<q>/<page>' (HEAD, GET, OPTIONS) -> search>])

```

self.view_functions 中保存的值

```

{'static': <function Flask.__init__.<locals>.<lambda> at 0x7f56677b7ee0>, 'search': <function search at 0x7f56675f4700>}

```

也就是说，路由想要成功注册，self.url_map 中必须保存有 路由到 视图函数的对应关系， self.view_functions 中也必须要有 endpoint 为 key, 视图函数为 值的对应关系

flask 接收到一个请求时，由 url_map 通过 rule 查找到视图函数名称，再由 view_functions 查找到对应的视图函数，才能调用视图函数处理请求

修改 applications.py 和 book.py, 打印 app 的 id

applications.py

```python

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

print('id in application', id(app))

# app.config.from_pyfile('config.py')
app.config.from_object('config')

# 必须要在入口文件中引入视图文件才能执行视图
from views import book


if __name__ == '__main__':
    print('id in main', id(app))
    app.run(host='0.0.0.0', port=5000)

```

book.py

```python

# -*- coding: utf-8 -*-
from flask import jsonify

from applications import app
from libs import is_isbn_or_key
from libs.httper import BookGetter

print('id in book', id(app))


@app.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
    # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
    # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
    # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
    isbn_or_key = is_isbn_or_key(keyword=q)
    if isbn_or_key == 'isbn':
        books = BookGetter.search_by_isbn(isbn=q)
    else:
        books = BookGetter.search_by_keyword(keyword=q)
    # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
    # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
    # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
    # return books
    return jsonify(books)

```

运行 app

```

ssh://ubuntu@162.62.134.181:22/home/ubuntu/.pyenv/versions/flask/bin/python -u /data/dev/fisher/applications.py
id 为 140352383539904 的 app 实例化
id 为 140352364328128 的 app 实例化
id 为 140352364328128 的 app 注册路由
id 为 140352383539904 的 app 运行
 * Serving Flask app 'applications'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.23:5000
Press CTRL+C to quit
 * Restarting with stat
id 为 140195674786592 的 app 实例化
id 为 140195655587056 的 app 实例化
id 为 140195655587056 的 app 注册路由
id 为 140195674786592 的 app 运行
 * Debugger is active!
 * Debugger PIN: 912-315-642

```

**Restarting with stat** 关闭 debug 模式, 因为 debug 模式下 flask 会自动重新启动一次

```

ssh://ubuntu@162.62.134.181:22/home/ubuntu/.pyenv/versions/flask/bin/python -u /data/dev/fisher/applications.py
id 为 140659671620288 的 app 实例化
id 为 140659652412896 的 app 实例化
id 为 140659652412896 的 app 注册路由
id 为 140659671620288 的 app 运行
 * Serving Flask app 'applications'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.23:5000
Press CTRL+C to quit

```

单步调试 step over

运行 applicaions.py 时，会先生成一个 Flask app, 执行到导入 book.py 时，会跳转到执行 book.py 导入, 而在 book.py 中又通过 `from applicaions import app`导入了 app, 此时会再次运行 applications.py, 再次生成一个新的 Flask app，并导致到 book.py 中使用，在 book.py 中导入 app 时，因为 applications.py 中的 `__name__ == '__main__'` 的条件不成立，此时不会执行 app.run() 中的代码， 而是会返回 book.py 中运行，才会执行注册路由的操作。 book.py 运行结束后会返回 applications.py 中继续执行，但此时在 applications.py 中执行的还是 生成的第一个 Flask app, 但第一个 app 并未绑定视图函数，所以就导致了请求时的 404

即运行的 app 和 注册路由的 app 不是同一个 Flask 对象


### 4-1 应用、蓝图与视图函数

第一层    app

第二层   蓝图1   蓝图2    蓝图3

第三层  蓝图1的静态文件  蓝图1的视图函数  蓝图1的模板 ...


第一层的 Flask 核心 app 类似一个插座，可以插入各种插件，实现更多的功能

把视图函数注册到蓝图中，再把蓝图注册到核心 app 上，从而实现分层与分业务

__init__.py 把一个目录变成 python 的包, 还兼负着一个包初始化的代码，可以把包的初始化代码写在 __init__.py 文件中


新建 applications 模块，把 create_app 的功能从原来的 applications.py 文件中提取出来


applications.__init__.py

```python

# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    return app

```

新建 views 模块

新建 views.book.py

```python

# -*- coding: utf-8 -*-
from flask import jsonify, Blueprint

from libs import is_isbn_or_key
from libs.httper import BookGetter

bp_book = Blueprint(name='book', import_name=__name__)


@bp_book.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
    # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
    # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
    # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
    isbn_or_key = is_isbn_or_key(keyword=q)
    if isbn_or_key == 'isbn':
        books = BookGetter.search_by_isbn(isbn=q)
    else:
        books = BookGetter.search_by_keyword(keyword=q)
    # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
    # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
    # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
    # return books
    return jsonify(books)


```

修改 views.__init__.py


```python

# -*- coding: utf-8 -*-

from .book import bp_book

```

新建 manage.py, 做为项目的入口文件

```python

# -*- coding: utf-8 -*-

from applications import create_app
from views import bp_book

app = create_app()
app.register_blueprint(blueprint=bp_book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

项目结构如下

fisher/
├── applications
│   └── __init__.py
├── config.py
├── __init__.py
├── libs
│   ├── httper.py
│   └── __init__.py
├── manage.py
├── test
│   └── test_search_keyword.py
└── views
    ├── book.py
    ├── __init__.py
    └── user.py


BluePrint 不是用来拆分文件的，而是用来在大型项目中拆分业务模块的，如网站相关的业务逻辑放在 web 蓝图中, api 对外接口, cms 内容管理 也做为单独的蓝图。如果只对 book，user 创建单独的蓝图，有点小题大做了。

新建 views.web 模块，views.api 模块，views.cms 模块

在 views.web.__init__.py 文件中创建 web 蓝图


```python

# -*- coding: utf-8 -*-
from flask import Blueprint

bp_web = Blueprint(name='bp_web', import_name=__name__)

```

把 book.py 和 user.py 移动到 views.web 中并使用 bp_web

views.web.book.py

```python

# -*- coding: utf-8 -*-
from flask import jsonify

from libs import is_isbn_or_key
from libs.httper import BookGetter

from . import bp_web


@bp_web.route('/book/search/<q>/<page>')
def search(q: str, page: str):
    """
    搜索图书
    :param q:
    :param page:
    :return:
    """
    # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
    # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
    # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
    # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
    isbn_or_key = is_isbn_or_key(keyword=q)
    if isbn_or_key == 'isbn':
        books = BookGetter.search_by_isbn(isbn=q)
    else:
        books = BookGetter.search_by_keyword(keyword=q)
    # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
    # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
    # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
    # return books
    return jsonify(books)

```

views.web.user.py


```python

# -*- coding: utf-8 -*-
from flask import jsonify

from . import bp_web


@bp_web.route('/user/register')
def register():
    return jsonify({"code": 200, "msg": "注册成功"})

```

此时执行以下命令测试依然会得到 404 的响应，是因为 book.py 和 user.py 未被执行，定义的路由并没有注册到视图函数上

curl http://127.0.0.1:5000/user/register
curl http://127.0.0.1:5000/book/search/%E6%88%91%E4%B8%8E%E5%9C%B0%E5%9D%9B/1

修改 views.web.__init__.py 文件

```python

# -*- coding: utf-8 -*-
from flask import Blueprint

bp_web = Blueprint(name='web', import_name=__name__)

# 执行导入 book 和 user 的操作, 把路由注册到蓝图上
from views.web import book
from views.web import user

```

但是这里是一个循环导入, book 和 user 中会导入 bp_web，而这里又导入 book 和 user, 因为 book 和 user 只会导入一次，所以代码也不会报错，但从逻辑上来讲还是难以接受的。

可以把 from views.web import book, user 的操作放在 views.__init__.py 文件中

views.__init__.py

```python

# -*- coding: utf-8 -*-
# 执行导入 book 和 user 的操作, 把路由注册到蓝图上
from .web import book, user

```

也可以把 bp_web 的实例化放在其它文件中，而不是 __init__.py 文件中，这样也能避免循环导入



修改 manage.py, 注册 bp_web 蓝图

```python
# -*- coding: utf-8 -*-

from applications import create_app
from views.web import bp_web

app = create_app()
app.register_blueprint(blueprint=bp_web)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

fisher/
├── applications
│   └── __init__.py
├── config.py
├── __init__.py
├── libs
│   ├── httper.py
│   └── __init__.py
├── manage.py
├── test
│   └── test_search_keyword.py
└── views
    ├── __init__.py
    ├── web
    │   └── __init__.py
    └── webs
        ├── book.py
        ├── __init__.py
        └── user.py

此时在 manage.py 中 if __name__ == '__main__' 处打上断点，查看 app 中的 url_map 和 view_functions, 可见对应的函数变成了 web.search, 如果是使用蓝图注册的视图函数，就会显示为 `蓝图名.函数名`

```

Map([<Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>,
 <Rule '/book/search/<q>/<page>' (GET, HEAD, OPTIONS) -> bp_web.search>,
 <Rule '/user/register' (GET, HEAD, OPTIONS) -> bp_web.register>])

{'static': <function Flask.__init__.<locals>.<lambda> at 0x7fdbcda883a0>, 'bp_web.search': <function search at 0x7fdbcda9b0d0>, 'bp_web.register': <function register at 0x7fdbcd8a4670>}

```

#### todo 这三种导入方式的不同

from . web import book
from .web import book
from web import book

from web import book 会报错

ssh://ubuntu@162.62.134.181:22/home/ubuntu/.pyenv/versions/flask/bin/python -u /data/dev/fisher/manage.py
Traceback (most recent call last):
  File "/data/dev/fisher/manage.py", line 4, in <module>
    from views.web import bp_web
  File "/data/dev/fisher/views/__init__.py", line 3, in <module>
    from web import book
ModuleNotFoundError: No module named 'web'

from . web import book
from .web import book

都能正常导入

### 4-4 request 对象

不使用 url 位置参数, 而是通过请求参数传递 q 和 page

http://10.0.0.23:5000/book/search/9787531324362/1

http://10.0.0.23:5000/book/search?q=9787531324362&page=1

获取参数
request.args.get()
request.values.get()

```python

# 获取请求参数的两种方法
# 1. values.get
q = request.values.get('q')
page = request.values.get('page')
# 2. args.get
q = request.args.get('q')
page = request.args.get('page')

request.args.to_dict()
request.values.to_dict()
request.form.to_dict()

```

request.values
CombinedMultiDict([ImmutableMultiDict([('q', '9787531324362')])])

request.args
ImmutableMultiDict([('q', '9787531324362')])

request.form
ImmutableMultiDict([])

不可变字典
werkzeug.datastructures.ImmutableMultiDict

验证参数, 使用 WTForms 对用户的输入进行验证
https://github.com/wtforms/wtforms
https://pypi.org/project/WTForms/

pipenv install WTForms

添加一个验证层, Validation layers, 对用户的输入进行验证

pycharm ctrl + p 查看函数参数


学习优秀框架时, 关注框架的实现和思想. 如 wtforms 对参数进行验证时, 就不是写函数, 在函数中写一堆 if...else...的判断. 而是把功能封装成对象和模块, 模块对外提供接口或方法供用户使用. 

新建 validators 模块, 新建 validators/book.py

```python
# validators/book.py
# -*- coding: utf-8 -*-

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchValidator(Form):
    # 对用户传递的请求参数进行验证
    # q 至少有1个字符, 且长度不能太长
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

```

修改 book 视图函数, 对用户的输入进行验证

view/web/book.py

```python

# -*- coding: utf-8 -*-
from flask import jsonify, request

from libs import is_isbn_or_key
from libs.httper import BookGetter
from validators.book import SearchValidator

from . import bp_web


@bp_web.route('/book/search')
def search():
    """
    搜索图书
    /book/search?q=9787531324362&page=1
    :return:
    """
    # <Request 'http://10.0.0.23:5000/book/search?q=9787531324362' [GET]>
    # 只有当 request 是由 http 请求来触发的, 或者说是由视图函数触发的, 或者说在 flask 上下文环境中时, request 才能代表用户的请求,
    # 否则 request 的类型是 LocalProxy
    validator = SearchValidator(request.args)
    if validator.validate():
        # 从 validator 中取出来 q 的值, 而不是从 args 或 values 中获取
        q = validator.q.data.strip()
        # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
        # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
        # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
        # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
        isbn_or_key = is_isbn_or_key(keyword=q)
        if isbn_or_key == 'isbn':
            books = BookGetter.search_by_isbn(isbn=q)
        else:
            books = BookGetter.search_by_keyword(keyword=q)
        # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
        # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
        # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
        # return books
        return jsonify(books)
    return jsonify({'code': 404, 'msg': '参数校验失效'}), 404

```

