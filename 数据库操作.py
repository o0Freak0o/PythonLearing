# -*- codeing = utf-8 -*-
# @Time:2020/11/5 9:06
# @Author:Freak
# @File:数据库操作.py
# @Software:PyCharm

import bs4  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import sqlite3
# conn = sqlite3.connect("test.db")
# print("Open database successfully")
# c = conn.cursor()#获取游标
# sql = '''
#     create table company
#           (id int primary key not null,
#           name text not null,
#           age int not null,
#           address char(50),
#           salary real);
# '''
# c.execute(sql)
# conn.commit()
# conn.close()
# print("成功建表")


conn = sqlite3.connect("test.db")
print("Open database successfully")
c = conn.cursor()#获取游标
sql1 = '''
    insert into company(id,name,age,salary)
    values (1,'张三',"成都",8000)
'''
sql2 = '''
    insert into company(id,name,age,salary)
    values (2,'李四',"成都",8000)
'''
sql = '''
     select id,name,address,salary from company
'''
cursor = c.execute(sql)
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary=",row[3])
c.execute(sql1)
c.execute(sql2)
conn.commit()
conn.close()
print("成功建表")