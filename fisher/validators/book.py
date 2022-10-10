# -*- coding: utf-8 -*-

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchValidator(Form):
    # 对用户传递的请求参数进行验证
    # q 至少有1个字符, 且长度不能太长
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

