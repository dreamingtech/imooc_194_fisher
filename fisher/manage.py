# -*- coding: utf-8 -*-

from applications import create_app
from views import bp_book

app = create_app()
app.register_blueprint(blueprint=bp_book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
