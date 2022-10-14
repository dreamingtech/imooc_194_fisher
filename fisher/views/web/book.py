# -*- coding: utf-8 -*-
from flask import jsonify, request

from libs import is_isbn_or_key
from libs.httper import BookGetter
from validators.book import SearchValidator
from view_models.book import BookViewModel

from . import bp_web


@bp_web.route('/book/search', methods=['GET', 'POST'])
def search():
    """
    搜索图书
    /book/search?q=9787531324362&page=1
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
        p = validator.page.data
        # 视图函数是 flask 所有功能的入口, 不要写太长的逻辑, 而是使用函数封装功能
        # 阅读源码是分层次来看, 不用一上来就太关注细节. 如此视图函数, 第一次阅读时读取到这一句代码时,
        # 知道是区分 isbn 搜索还是普通搜索即可. 不用查看具体的细节代码.
        # 而不使用函数封装时, 就要强迫所有阅读此源码的人阅读具体的细节. 阅读体验会非常不好
        isbn_or_key = is_isbn_or_key(keyword=q)
        if isbn_or_key == 'isbn':
            books = BookGetter.search_by_isbn(isbn=q)
            books = BookViewModel.package_single(data=books, keyword=q)
        else:
            books = BookGetter.search_by_keyword(keyword=q, page=p)
            books = BookViewModel.package_collection(data=books, keyword=q)
        # 新版的 flask 可以直接返回一个字典, flask 甚至会自动加上 'Content-Type': 'application/json' 的响应头
        # {'Server': 'Werkzeug/2.2.2 Python/3.9.13', 'Date': 'Sun, 09 Oct 2022 08:58:56 GMT',
        # 'Content-Type': 'application/json', 'Content-Length': '997', 'Connection': 'close'}
        # return books
        return jsonify(books)
    # 使用 validator.errors 中的验证信息
    # {'q': ['Field must be between 1 and 30 characters long.']}
    return jsonify(validator.errors), 404
