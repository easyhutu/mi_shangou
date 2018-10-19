"""
Author: Meng
Date: 2018/10/2
"""

from selenium.webdriver import Chrome, ChromeOptions
from settings import CHROME_DRIVER_PATH, LOGIN_URL, USERNAME, PWD, CHROME_OPTIONS_PATH
import time
import json


def login_get_cookie():
    try:
        print('正在打开浏览器')
        path = r'--user-data-dir={}'.format(CHROME_OPTIONS_PATH)
        print(path)
        option = ChromeOptions()
        option.add_argument(path)
        # option.add_argument('--incognito')
        # option.add_argument('--single-process')
        driver = Chrome(executable_path=CHROME_DRIVER_PATH, options=option)
        driver.set_page_load_timeout(10)
        print('打开登录页面')
        driver.get(LOGIN_URL)
        username = driver.find_element_by_id('username')
        username.send_keys(USERNAME)
        pwd = driver.find_element_by_id('pwd')
        pwd.send_keys(PWD)
        driver.find_element_by_id('login-button').submit()
        print('登录完成')
        time.sleep(3)
        cookies = driver.get_cookies()
        print('已获取cookies')
        driver.quit()
        new_co = {}
        for item in cookies:
            new_co[item.get('name')] = item.get('value')
        print(json.dumps(new_co))
        return new_co
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    login_get_cookie()
