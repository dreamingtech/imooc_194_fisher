# -*- coding: utf-8 -*-
# common 中保存不涉及到敏感性的配置信息, 还保存生产和开发环境相同的信息

# 配置文件中的变量必须全部大写
# flask.config.Config.from_object
# if key.isupper(): 只有全部大写时才能正确读取

# 每页展示的数据量
PAGE_SIZE = 15

DEBUG = True
