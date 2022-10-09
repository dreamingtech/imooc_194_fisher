# -*- coding: utf-8 -*-
import requests


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
    def search_by_keyword(cls, keyword: str, start=0, count=15):
        url = cls.keyword_url.format(keyword, start, count)
        result = Http.get(url)
        return result
