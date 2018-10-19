"""
Author: Meng
Date: 2018/10/2
"""
from concurrent.futures import ThreadPoolExecutor
import time
from mi_lib.login_mi import login_get_cookie
import hashlib

if __name__ == '__main__':
    login_get_cookie()