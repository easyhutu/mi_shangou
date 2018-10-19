"""
Author: Meng
Date: 2018/10/2
"""
import requests
from datetime import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer': 'https://www.mi.com/seckill/',
}


class Client:
    @staticmethod
    def get(url, params=None, **kwargs):
        html = requests.get(url, params, headers=header, verify=False, **kwargs)
        print('-' * 60)
        print(str(datetime.now()))
        print(html.content)
        print('-' * 60)
        return html
