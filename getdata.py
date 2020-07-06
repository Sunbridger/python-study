# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

os.system('clear')  # os.system('clear')


import urllib                    # 引入urllib.request
response =  urllib.urlopen('https://www.tangeche.com')            # 打开URL
html = response.read()            # 读取内容
html = html.decode('utf-8')            # 解码
print(html)
