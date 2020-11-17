# -*- codeing = utf-8 -*-
# @Time:2020/11/9 8:38
# @Author:Freak
# @File:ygdy8网站爬虫.py
# @Software:PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
from urllib.parse import quote# 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import requests

a_find = re.compile(r'<a href="(.*?)"')
movie = input("请输入你想看的电影名:\n")
Base_url = 'https://www.ygdy8.com'
Target_url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+quote(movie.encode('gbk'))
res = requests.get(Target_url)
res.encoding=res.apparent_encoding
soup = BeautifulSoup(res.text,'html.parser')
item = soup.find('div',class_='co_content8')
item = str(item)
stretch_url = re.findall(a_find,item)[0]
print(stretch_url)
Final_url = Base_url+stretch_url
res1 = requests.get(Final_url)
res1.encoding = res1.apparent_encoding
soup1 = BeautifulSoup(res1.text,'html.parser')
item1 = soup1.find('div',id='Zoom').find('span').find('table').find('a').text
print(item1)


