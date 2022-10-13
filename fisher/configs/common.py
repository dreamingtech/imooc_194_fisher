# -*- coding: utf-8 -*-
# common 中保存不涉及到敏感性的配置信息, 还保存生产和开发环境相同的信息

# 配置文件中的变量必须全部大写
# flask.config.Config.from_object
# if key.isupper(): 只有全部大写时才能正确读取

# 每页展示的数据量
PAGE_SIZE = 15

DEBUG = True

# SQLALCHEMY 数据库连接配置文件
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
# 注意: 因为是使用的 docker 运行的 mysql, 172.17.%.% 有权限访问. 172.17.0.1 是 docker0 网卡的地址.
# 否则会出现以下异常
# (1130, "172.17.0.1' is not allowed to connect to this MySQL server")
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flask:7CNH8MqTezH3jyr@localhost:33307/fisher"

# /home/ubuntu/.pyenv/versions/flask/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py:872:
# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled
# by default in the future.  Set it to True or False to suppress this warning.
#   warnings.warn(FSADeprecationWarning(
SQLALCHEMY_TRACK_MODIFICATIONS = True
