"""
Author: Meng
Date: 2018/10/6
"""
from mi_lib.login_mi import login_get_cookie
from mi_lib.callback_json import ram_jsoncallback, to_json
from mi_lib.get_server_time import local_time
import time
import sys
from mi_lib.client import Client

add_url = 'https://cart.mi.com/cart/add/{}'


def qianggou_req():
    goods = input_goods_id()
    ti = input_time()

    while True:
        s_time = ti
        l_time = time.time()
        if s_time > l_time + 30:
            csx = s_time - l_time
            m = int(csx / 60) % 60
            h = int(csx / (60 * 60))
            s = int(csx % 60)
            stf_ti = '{:02}:{:02}:{:02}'.format(h, m, s)
            sys.stdout.write('\r距秒杀《{}》开始还有 {}'.format(goods, stf_ti))
            sys.stdout.flush()
            time.sleep(1)
        else:
            print('还有半分钟就开始秒杀-{},进行秒杀前准备工作'.format(goods))
            # 调用selenium登录小米获取cookie
            cookie = login_get_cookie()
            while True:
                l_ti = time.time()
                # 距离开始抢购1.2秒时进入抢购环节
                if s_time > l_ti + 1.2:
                    sys.stdout.write('\r距秒杀《{}》开始还有 {}'.format(goods, s_time - l_ti))
                    sys.stdout.flush()
                    time.sleep(0.1)
                else:
                    req(goods, cookie)
                    exit()


def req(goods_id, cookie):
    params = dict(
        jsonpcallback='',
        _=''
    )
    for index in range(100):
        params['jsonpcallback'] = ram_jsoncallback()
        params['_'] = local_time()
        url = add_url.format(goods_id)
        html = Client.get(url, params=params, cookies=cookie)
        data = to_json(html, params['jsonpcallback'])
        if data.get('code') == 1:
            print('抢购成功')
            break
        else:
            print(data)
            print('失败，重新尝试')


def input_goods_id():
    while True:
        goods_id = input('请输入商品ID：')
        if goods_id:
            return goods_id


def input_time():
    while True:
        ti = input('请输入开始抢购时间(格式：%Y-%m-%d %H:%M:%S)：')
        if ti:
            try:
                strp_ti = time.strptime(ti, '%Y-%m-%d %H:%M:%S')

                return time.mktime(strp_ti)
            except Exception as e:
                print('时间输入有误！')


if __name__ == '__main__':
    qianggou_req()
