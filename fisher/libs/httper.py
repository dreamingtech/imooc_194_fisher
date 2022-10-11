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

    @classmethod
    def search_by_isbn(cls, isbn: str):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword: str, page: int = 1):
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
        url = cls.keyword_url.format(keyword, cls.calculate_start(page), current_app.config.get('PAGE_SIZE', 20))
        result = Http.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config.get('PAGE_SIZE', 20)
