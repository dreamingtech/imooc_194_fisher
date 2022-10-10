# -*- coding: utf-8 -*-

from applications import create_app
from views.web import bp_web

app = create_app()
app.register_blueprint(blueprint=bp_web)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
