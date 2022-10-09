# -*- coding: utf-8 -*-

import requests

r = requests.get(url='http://127.0.0.1:5000/book/search/我与地坛/1')

print(r.text)
print(r.url)
