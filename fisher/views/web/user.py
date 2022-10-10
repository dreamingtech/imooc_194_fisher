# -*- coding: utf-8 -*-
from flask import jsonify

from . import bp_web


@bp_web.route('/user/register')
def register():
    return jsonify({"code": 200, "msg": "注册成功"})
