#!/usr/bin/env python3
import requests
import os

url = "http://34.135.227.3/upload/"

for img in os.listdir('supplier-data/images'):
    if img.endswith('.jpeg'):
        with open(f'supplier-data/images/{img}', 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.content.decode('utf-8'))


