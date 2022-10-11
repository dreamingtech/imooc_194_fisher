# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('configs.common')
    app.config.from_object('configs.secure')

    return app
