# -*- coding: utf-8 -*-
import requests
from flask import current_app


class Http(object):
    @staticmethod
    def get(url: str, return_json: bool = True):
        """
        大部分接口都是 restful 风格的, 要求返回的数据都是 json 格式的
        :param url:
        :param return_json:
        :return:
        """
        resp = requests.get(url)
        # 判断状态码
        # 搜索图书不存在时, 状态码会为 404
        if resp.status_code != 200:
            return {} if return_json else ''
        return resp.json() if return_json else resp.text


class BookGetter(object):
    """
    调用 api 获取图书信息
    """
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&start={}&count={}'
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'

    def __init__(self):
        """
        把图书搜索的结果保存到类属性中
        同时把两种不同格式的图书整理成一种格式, 替代 view_models.book.py 中的处理
        是否把查询的中间参数 如搜索关键词, 页码信息也保存在 Book 的实例属性中, 以方便 views 中使用?
        从编码的角度来考虑是没问题的, 但从类的内聚性上考虑, 这样会使这个类的职责变得不明确
        BookGetter 只是对获取图书这个过程的抽象, 隐藏了获取图书的具体过程, 一旦添加了一些中间参数,
        就会使这个类变得更加具体, 就脱离了 "获取图书" 这一职责, 也就不符合类的封装性和内聚性的特点
        """
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn: str):
        url = self.isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        """
        处理 isbn 搜索结果
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """
        处理 关键词 搜索结果
        :param data:
        :return:
        """
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword: str, page: int = 1):
        """
        talelin api 要求传入 start 和 count 参数, 但之前设计时, 用户需要传入的是 page 参数
        需要进行转换, 这个转换最好是放在本函数内部来进行.
        类具有封装性, 需要对外隐藏一些细节
        在 page > start + count 的转换中, 需要有 page_size 的参数, 可以使用类属性的方式定义
        但最好定义在配置文件中, 方便后继的修改
        二是逻辑计算最好不要直接放在本函数中, 而封装成一个单独的函数
        是否把功能代码封装成一个函数, 并不是由代码量或逻辑复杂度来决定的,
        函数本身不但具有封装性和利用性, 它本身还是一个自描述的对象, 可以很方便的通过函数名来知道函数的功能
        :param page:
        :param keyword:
        :return:
        """
        url = self.keyword_url.format(keyword, self.calculate_start(page), current_app.config.get('PAGE_SIZE', 20))
        result = Http.get(url)
        self.__fill_collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config.get('PAGE_SIZE', 20)
