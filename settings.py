"""
Author: Meng
Date: 2018/10/2
"""
import os


ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DRIVER_PATH = os.path.join(ROOT_PATH, 'driver')
LOGIN_URL = 'https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Fseckill%252F%26sign%3DOGU1NTc1NzcwNjIxZWQ3YjE5YmIzMTQ1YWQzNGE4ODdjNjk2M2IxMQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180'
# chrome driver路径
CHROME_DRIVER_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')

# 谷歌浏览器个人配置路径
CHROME_OPTIONS_PATH = r'C:\Users\mengjianhua\AppData\Local\Google\Chrome\User Data'

# 小米登录用户名密码
USERNAME = ''
PWD = ''

# 闪购结果提醒邮件配置
# 是否开启邮件提醒
IS_SEND_EMAIL = True
# 接收邮件提醒的邮箱
RECEIVER = '1711621009@qq.com'
