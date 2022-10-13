# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    # 装帧版本, 精装还是平装
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    # 出版时间
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    # 图书简介
    summary = Column(String(1000))
    # 图书图片
    image = Column(String(50))

    # MVC M Model 只有数据时 等价于 数据表
    # ORM 对象关系映射
    # Code First
