# -*- coding: utf-8 -*-

from applications import create_app

app = create_app()


if __name__ == '__main__':
    # werkzeug.serving.make_server
    # 不能同时开启多线程和多进程
    # app.run(host='0.0.0.0', port=5000, threaded=True, processes=3)
    app.run(host='0.0.0.0', port=5000, threaded=True)
    # app.run(host='0.0.0.0', port=5000, threaded=False, processes=3)
