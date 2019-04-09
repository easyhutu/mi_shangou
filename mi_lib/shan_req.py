"""
Author: Meng
Date: 2018/10/2
"""
from mi_lib.client import Client
from mi_lib.login_mi import login_get_cookie
from urllib.parse import unquote_plus, urlparse, urlencode
from mi_lib.get_server_time import local_time, server_time
from mi_lib.callback_json import to_json
import random
from concurrent.futures import ThreadPoolExecutor
from mi_lib.send_email import success_email, failed_email
from queue import Queue
import string
import hashlib
import json

qus = Queue()

hdinfo_url = 'https://tp2.hd.mi.com/hdinfo/cn'

hdget_url = 'https://tp2.hd.mi.com/hdget/cn'

add_url = 'https://cart.mi.com/cart/add/{}'


def ram_str(len=10):
    ran_str = ''
    for index in range(len):
        ran_str = ran_str + ''.join(random.sample(string.ascii_letters + string.digits + '+/', 1))
    print(ran_str)
    return ran_str


def hdinfo_make_params(shop: dict, cookie):
    params = dict(
        jsonpcallback='hdinfo',
        sitename='cn',
        start=shop.get('start_time'),
        source='flashsale',
        m=1,
        _=local_time()
    )
    html = Client.get(hdinfo_url, params=params, cookies=cookie)
    data = to_json(html, params['jsonpcallback'])
    return data.get('status')


def make_ctr1():
    h = hashlib.sha1()
    h.update(local_time().encode())
    shs = h.hexdigest()
    return '1807535409_0196475409{}'.format(shs[:37])


def hdget_make_params(shop: dict, salt, cookie):
    params = dict(
        jsonpcallback='cn2181000027',
        source='flashsale',
        product='2181000027',
        salt=salt,
        m=1,
        addcart=1,
        # cstr1='1807535409_0189525479660bbd4b2c96361039ac0d9b558665e5adacf',
        cstr1=make_ctr1(),
        # cstr2='ZHXgu8noD5UHzYOe4O%2FpjfrHdYBYDKRx2nLAlH0EJhEnQCKc5T%2FWl4d7VZnGQWQYtpQwN%2FxxsPw%3D',
        cstr2='{}='.format(ram_str(75)),
        _=local_time()
    )
    params['jsonpcallback'] = 'cn' + shop.get('goods_id')
    params['product'] = shop.get('goods_id')

    html = Client.get(hdget_url, params=params, cookies=cookie)
    data = to_json(html, params['jsonpcallback'])
    if data:
        st = data.get('status')
        if st:
            token = st.get(shop.get('goods_id')).get('hdurl')
            if token:
                return token
    return None


def ram_ch(len=16):
    c = ''
    for index in range(len):
        c = c + str(random.randint(0, 9))
    return c


def add_make_params(shop: dict, token: str, cookie):
    params = dict(
        jsonpcallback='jQuery111301636100507708247_1538481692013',
        product_id=2181000027,
        source='bigtap_flash',
        token='9fd054a48725c2459d295a512d5d7ba598e%2C637160660%2C2181000027%2C1538481699%2C1%2C1%2C000%2Cflashsale%2C',
        _=1538481692018
    )
    params['jsonpcallback'] = 'jQuery' + '11130' + ram_ch() + '_' + local_time()
    params['product_id'] = shop.get('goods_id')
    #params['extend_field[end_time]'] = shop.get('end_time')
    params['extend_field'] = json.dumps({'start_time': shop.get('start_time'), 'end_time': shop.get('end_time')})
    params['token'] = token
    params['_'] = local_time()
    url = add_url.format(shop.get('goods_id'))
    html = Client.get(url, params=params, cookies=cookie)
    data = to_json(html, params['jsonpcallback'])
    print(data)
    return data


def get_salt(shop, cookie):
    for i in range(10):
        hd_info = hdinfo_make_params(shop, cookie)
        salt = hd_info.get(shop.get('goods_id')).get('salt')

        if salt:
            return salt
    return '96c6e69f2ef9749e'


def get_goods_info(shop, cookie):
    infos = {}
    for i in range(1000):
        hd_info = hdinfo_make_params(shop, cookie)
        salt = hd_info.get(shop.get('goods_id'))
        if salt.get('salt'):
            infos = salt
            break
    return infos


def shangou_request(shop: dict, cookie):
    # salt = get_salt(shop, cookie)
    global is_shop
    is_shop = False
    info = get_goods_info(shop, cookie)
    salt = info.get('salt')
    shop['end_time'] = info.get('endtime')
    shop['start_time'] = info.get('starttime')
    if salt:

        hd_token = hdget_make_params(shop, salt, cookie)
        if hd_token:
            worker = 5
            with ThreadPoolExecutor(max_workers=worker) as executor:
                for item in range(worker):
                    executor.submit(large_ex, shop, hd_token, cookie)
                    print(item)
            if qus.empty():
                failed_email(shop.get('name'))
            return True

        else:
            print('获取抢购资格失败，重新尝试')

    else:
        print('获取秒杀商品信息失败！')
        return False


def shangou_request_one(shop: dict, cookie):
    info = get_goods_info(shop, cookie)
    salt = info.get('salt')
    shop['end_time'] = info.get('endtime')
    shop['start_time'] = info.get('starttime')
    if salt:

        hd_token = hdget_make_params(shop, salt, cookie)
        if hd_token:
            stat = large_ex(shop, hd_token, cookie)
            if stat is False:
                failed_email(shop.get('name'))

        else:
            print('获取抢购资格失败，重新尝试')
            failed_email(shop.get('name'))

    else:
        failed_email(shop.get('name'))
        print('获取秒杀商品信息失败！')
        return False


def large_ex(shop, hd_token, cookie):
    status = add_make_params(shop, hd_token, cookie)
    if status:
        if status.get('code') == 1:
            print('秒杀成功，请前往购物车结算！')
            qus.put('ok')
            success_email(shop.get('name'))

            return True
        else:

            print('添加到购物车失败')
            return False


if __name__ == '__main__':
    shop = {
        'start_time': '1538481600',

        'end_time': '1538483220',
        'goods_id': '2181000027'
    }
    ram_str(75)
    print(make_ctr1())
    # hdget_make_params(shop, '2k23s23', {})
    # hdinfo_make_params(shop, {})
