#! /usr/bin/env python3

import os
import json
import requests


def readfiles(file_path):
    with open(file_path) as f:
        return f.readlines()


def text2dict(data):
    x = {
        "title": data[0].strip(),
        "name": data[1].strip(),
        'date': data[2].strip(),
        'feedback': data[3].strip()
    }
    return x


def send_requests(data):
    url = "http://34.173.218.54/feedback/"
    response = requests.post(
        url=url,
        data=data)
    print(response.content.decode('utf-8'))
    return response


if __name__ == "__main__":
    for file in os.listdir('feedkack'):
        if os.path.isfile('feedkack/' + file):
            send_requests(text2dict(readfiles('feedkack/' + file)))
