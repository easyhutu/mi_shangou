"""
Author: Meng
Date: 2018/10/2
"""
import json
import random
from mi_lib.get_server_time import local_time


def to_json(html, jsoncallback):
    content = html.content.decode()
    co = content.replace(jsoncallback + '(', '')
    co = co.replace(');', '')
    co = co.replace(')', '')
    if co:
        data = json.loads(co)
        return data
    return None


def ram_jsoncallback(len=16):
    c = ''
    for index in range(len):
        c = c + str(random.randint(0, 9))
    return 'jQuery' + '11130' + c + '_' + local_time()
