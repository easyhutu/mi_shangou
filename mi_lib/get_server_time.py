"""
Author: Meng
Date: 2018/10/2
"""
url = 'https://time.hd.mi.com/gettimestamp'
from mi_lib.client import Client
import time


def server_time():
    html = Client.get(url)
    ti = html.content.decode()
    print(ti)
    ti = ti.split('=')[-1]
    return ti


def local_time(is_sp=False):
    ti = time.time()
    if is_sp:
        ti = str(ti).replace('.', '')
        return ti
    else:
        return str(int(ti))
