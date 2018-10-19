"""
Author: Meng
Date: 2018/10/7
"""

from mi_lib.login_mi import login_get_cookie
import requests
import json
import time
from datetime import datetime
import sys
from settings import USERNAME

gurl = 'http://45.76.14.9/x/task/mi?task_name={}'.format(USERNAME)
purl = 'http://45.76.14.9/x/task/mi'


def get_ser_cookies():
    html = requests.get(gurl)
    cookies = html.json().get('data').get('cookies')
    if cookies:
        co = json.loads(cookies)

        return co
    else:
        return None


def get_ser_time():
    try:
        html = requests.get(gurl)
        ti = html.json().get('data')
        if ti:
            if ti.get('run_time'):

                return ti.get('run_time')

        return 0
    except:
        print('获取数据异常')
        return 0


def set_run_time(ti):
    params = dict(
        task_name=USERNAME,
        run_time=ti

    )
    html = requests.post(purl, json=params)
    print(html.content.decode())


def set_cookies():
    cookies = login_get_cookie()
    # cookies = {"mstuid": "1538450067925_7304",}

    params = dict(
        task_name=USERNAME,
        cookies=json.dumps(cookies)

    )
    html = requests.post(purl, json=params)
    print(html.content.decode())


def loop_set_cookies():
    while True:
        r_ti = get_ser_time()
        loc_ti = int(time.time())
        if r_ti - loc_ti > 0:
            if r_ti < loc_ti + 100:
                set_cookies()
                set_run_time(-1)
                time.sleep(2)
            sys.stdout.write('\r距离任务开始还有：{} S'.format(r_ti - loc_ti))
            sys.stdout.flush()

        else:
            sys.stdout.write('\rnot task {}'.format(str(datetime.now())))
            sys.stdout.flush()
        time.sleep(20)


if __name__ == '__main__':
    # set_cookies()
    # get_ser_cookies()
    # get_ser_time()
    loop_set_cookies()
    # set_run_time(1538888270)
