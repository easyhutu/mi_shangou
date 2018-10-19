"""
Author: Meng
Date: 2018/10/2
"""
from mi_lib.get_server_time import server_time, local_time
import random
from mi_lib.client import Client
import json
import time
from datetime import datetime
from prettytable import PrettyTable

url = 'https://a.huodong.mi.com/flashsale/getlist'
params = dict(
    jsonpcallback='jQuery111308996532148481313_1538447442993',
    now_time='1538447441',
    size='15',
    page=1,
    _=''

)


def ram_ch(len=16):
    c = ''
    for index in range(len):
        c = c + str(random.randint(0, 9))
    return c


def make_params(params):
    params['jsonpcallback'] = 'jQuery' + '11130' + ram_ch() + '_' + local_time()
    params['now_time'] = server_time()
    params['_'] = local_time()
    return params


def get_shop_list():
    param = make_params(params)
    html = Client.get(url, params=param)
    content = html.content.decode()

    co = content.replace(param['jsonpcallback'] + '(', '')
    co = co.replace(');', '')
    data = json.loads(co)
    shop_list = data.get('data').get('data').get('list')
    show_shops(shop_list)
    all_shops = []
    for item in shop_list:
        start_time = item.get('start_time')
        end_time = item.get('end_time')
        for it in item.get('list'):
            all_shops.append({'name': it.get('goods_name'),
                              'start_time': start_time,
                              'st_time': strf_time(start_time),
                              'end_time': end_time,
                              'goods_id': it.get('goods_id')
                              })
    print('请浏览表格中的商品，选择需要秒杀的输入商品ID ^_^')
    return all_shops


def show_shops(shops):
    for sh in shops:
        print('*' * 80)
        st_time = sh.get('start_time')
        end_time = sh.get('end_time')
        print('秒杀开始时间:{}'.format(strf_time(st_time)))
        row = PrettyTable()
        row.field_names = ['名称', '原价', '秒杀价', '商品ID']
        for itme in sh.get('list'):
            goods_id = itme.get('goods_id')
            goods_name = itme.get('goods_name')
            goods_price = itme.get('goods_price')
            seckill_price = itme.get('seckill_price')
            row.add_row([goods_name, goods_price, seckill_price, goods_id])

        print(row)


def strf_time(ti):
    ti = time.localtime(ti)

    return time.strftime('%Y-%m-%d %H:%M:%S', ti)


if __name__ == '__main__':
    get_shop_list()
