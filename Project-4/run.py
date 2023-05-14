#! /usr/bin/env python3

import os
import json
import requests
import re


def readfiles(file_path):
    with open(file_path) as f:
        return f.readlines()


def text2dict(data, file_name):
    x = {
        "name": data[0].strip(),
        "weight": re.search('.*?(\d+)\s', data[1]).group(),
        'description': data[2].strip(),
        'image_name': f'{file_name}.jpeg',
    }
    return x


def send_requests(data):
    url = "http://34.135.227.3/fruits/"
    response = requests.post(
        url=url,
        data=data)
    print(response.content.decode('utf-8'))
    return response


if __name__ == "__main__":
    for file in os.listdir('supplier-data/descriptions'):
        if os.path.isfile('supplier-data/descriptions/' + file):
            send_requests(text2dict(readfiles('supplier-data/descriptions/' + file), os.path.splitext(file)[0]))
