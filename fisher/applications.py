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
