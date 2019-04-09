"""
Author: Meng
Date: 2018/10/6
"""
secret = '0e288e41d1aca75267e53f8190ac6be4'
url = 'http://39.105.167.167/x/send_email'
import requests
from settings import IS_SEND_EMAIL, RECEIVER

def success_email(shop_name):
    title = '抢购成功-{}'.format(shop_name)
    content = '您抢购的《{}》,已成功加入购物车，请尽快前往小米商城购物车结算，超过15分钟将失效。'.format(shop_name)
    rec = RECEIVER
    pa = dict(
        title=title,
        content=content,
        key=secret,
        receiver=rec
    )
    if IS_SEND_EMAIL:
        html = requests.get(url, params=pa)
        print(html.content.decode())


def failed_email(shop_name):
    title = '抢购失败-{}'.format(shop_name)
    content = '您选择的《{}》抢购失败^-^'.format(shop_name)
    rec = '1711621009@qq.com'
    pa = dict(
        title=title,
        content=content,
        key=secret,
        receiver=rec
    )
    if IS_SEND_EMAIL:
        html = requests.get(url, params=pa)
        print(html.content.decode())


if __name__ == '__main__':
    # success_email('米兔定位电话 白色')
    failed_email('米兔定位电话 白色')
