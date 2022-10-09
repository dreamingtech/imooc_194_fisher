# -*- coding: utf-8 -*-

def is_isbn_or_key(keyword: str):
    """
    区分用户输入的搜索关键字是 普通搜索还是关键词搜索
    isbn13: 13个0到9的数字组成
    isbn10: 老的标准, 10个0到9的数字组成, 含有一些 '-'
    :param keyword:
    :return:
    """
    isbn_or_key = 'key'
    # 把大概率出现假的条件放在最前面
    # 把需要 io 操作的判断放在后面, 如查询数据库, 读取文件等
    if len(keyword) == 13 and keyword.isdigit():
        isbn_or_key = 'isbn'
    if '-' in keyword and len(keyword.replace('-', '')) == 10 and keyword.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

