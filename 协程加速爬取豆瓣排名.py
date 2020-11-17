# -*- codeing = utf-8 -*-
# @Time:2020/11/6 12:39
# @Author:Freak
# @File:协程加速爬取豆瓣排名.py
# @Software:PyCharm

import bs4  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

from gevent import monkey
monkey.patch_all()
import gevent,csv
from gevent.queue import Queue

work = Queue()

Name_find = re.compile(r'<span class="title">(.*)</span>')
Rating_find = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
Inq_find = re.compile(r'<span class="inq">(.*)</span>')

for i in range(0,10):
    url = 'https://movie.douban.com/top250?start='
    url = url+str(i*25)
    work.put_nowait(url)
print(work)

datalist = []

def crawler():
    Header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    while not work.empty():
        url=work.get_nowait()
        req = urllib.request.Request(url=url,headers=Header)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = bs4.BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            # Serial = re.findall(Serial_find,item)
            # data.append(Serial[0])
            name = re.findall(Name_find, item)
            if (len(name) == 2):
                ctitle = name[0]
                data.append(ctitle)
                otitle = name[1].replace("/", "")
                data.append(otitle)
            elif (len(name) == 1):
                ctitle = name[0]
                data.append(ctitle)
                data.append(' ')
            rating = re.findall(Rating_find, item)[0]
            data.append(rating)
            inq = re.findall(Inq_find, item)
            if len(inq) != 0:
                inq = inq[0].replace("..", '')
                data.append(inq)
            else:
                data.append(' ')
            datalist.append(data)
    return datalist

def speed():
    tasks_list = []
    for x in range(5):
        task = gevent.spawn(crawler)
        tasks_list.append(task)
    gevent.joinall(tasks_list)

def savedata1(datalist):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet("豆瓣排行TOP250",cell_overwrite_ok=True)
    col = ["名字","英文名","排名","推荐语"]
    for i in range(0,4):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,4):
            sheet.write(i+1,j,data[j])
    book.save('douban9.xls')

if __name__ == '__main__':
    speed()
    savedata1(datalist)