# -*- coding: utf-8 -*-
import json

import requests

# r = requests.get(url='http://127.0.0.1:5000/book/search/我与地坛/1')
# r = requests.get(url='http://127.0.0.1:5000/book/search?q=我与地坛&page=1')
# r = requests.get(url='http://127.0.0.1:5000/book/search?q=我与&page=1', params={'q': '天', 'page': 2})
# r = requests.get(url='http://127.0.0.1:5000/book/search?q=我与&page=1&q=天&page=2')
r = requests.get(
    url='http://127.0.0.1:5000/book/search?q=我与&page=1&q=天&page=2',
    data=json.dumps({'q': '天天', 'page': 3}),
    headers={'Content-Type': 'application/json'}
)


print(r.text)
print(r.url)
