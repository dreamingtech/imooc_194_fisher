# -*- coding: utf-8 -*-

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchValidator(Form):
    # 对用户传递的请求参数进行验证
    # q 至少有1个字符, 且长度不能太长
    # 旧版的 wtforms 如果传入类似 'http://127.0.0.1:5000/book/search?q= &page=1' 的请求时
    # q 会被识别为通过校验, 可以通过添加 DataRequired 验证器来校验此类参数
    # 但在新版中, Length 校验器已经可以识别这种不合法的参数了
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

