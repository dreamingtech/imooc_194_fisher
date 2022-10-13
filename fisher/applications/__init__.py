# -*- coding: utf-8 -*-
from flask import Flask

from models.book import db
from views.web import bp_web


def create_app():
    app = Flask(__name__)
    app.config.from_object('configs.common')
    app.config.from_object('configs.secure')

    # 注册 blueprint
    app.register_blueprint(blueprint=bp_web)

    # 初始化数据库连接
    db.init_app(app)
    # 生成数据表, 需要传入 app 参数, 否则就会报错
    # RuntimeError: No application found. Either work inside a view function or push an application context.
    # See http://flask-sqlalchemy.pocoo.org/contexts/.
    db.create_all(app=app)

    # with app.app_context():
    #     db.create_all()

    return app
