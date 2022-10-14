# -*- coding: utf-8 -*-


class BookViewModel:
    # 描述特征 （类变量、实例变量）
    # 行为 （方法）
    # 面向过程
    @classmethod
    def package_single(cls, data, keyword):
        """
        处理 isbn 搜索接口返回一种图书的情况
        编程思维: 对单项的数据单独定义一个处理方法，对多项数据处理时就可以利用单项数据的处理方法了
        最好不要直接对多项数据定义一个方法处理
        :param data:
        :param keyword:
        :return:
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """
        处理 关键词 搜索接口返回多本图书的情况
        :param data:
        :param keyword:
        :return:
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            # pages 处理. isbn 搜索结果中 pages 和 summary 可能为空, 此时渲染可能会出现异常.
            'pages': data['pages'] or '',
            # 如果前端使用 ajax 处理请求，可以直接把列表形式的 author 返回给前端
            # 如果是使用模板渲染的方法，最好是处理之后再传递给模板
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
