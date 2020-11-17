# -*- codeing = utf-8 -*-
# @Time:2020/11/10 15:47
# @Author:Freak
# @File:扇贝单词.py
# @Software:PyCharm

import bs4  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import requests

base_url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
base_Headers = {

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',

}

def choose():
    lin = requests.get(url=base_url,headers=base_Headers)
    js_link = lin.json()
    bianhao = int(input('请输入编号'))
    ciku = js_link['data'][bianhao-1][0]
    return ciku
def test(ciku):
    Second_url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku
    test = requests.get(url=Second_url,headers=base_Headers)
    words = test.json()
    return words

def count(words):
    danci = []
    words_know = []
    words_unkonw = []
    for i in range(0,50):
        print("第"+str(i+1)+'个'+words['data'][i]['content'])
        answer = input("你认识吗？认识输入Y，不认识输入N")
        if answer == 'Y':
            words_know.append(words['data'][i]['content'])
        else:
            words_unkonw.append(words['data'][i]['content'])
    print("50个单词中你以为你会"+str(len(words_know))+"个"+"不会"+str(len(words_unkonw))+"个")


def delicate_read(words):
    words_real_know=[]
    print("接下来测试你真正掌握了多少")
    for i in range(0,50):
        print("第"+str(i+1)+"个"+words['data'][i]['content'])
        print('A.'+words['data'][i]['definition_choices'][0]['definition'])
        print('B.' + words['data'][i]['definition_choices'][1]['definition'])
        print('C.' + words['data'][i]['definition_choices'][2]['definition'])
        print('D.' + words['data'][i]['definition_choices'][3]['definition'])
        choice = input("请输入你的选择")
        choice_rank = {
            'A': words['data'][i]['definition_choices'][0]['rank'],
            'B': words['data'][i]['definition_choices'][1]['rank'],
            'C': words['data'][i]['definition_choices'][2]['rank'],
            'D': words['data'][i]['definition_choices'][3]['rank']
        }
        if choice_rank[choice] == words['data'][i]['rank']:
            words_real_know.append(words['data'][i])
    print("你真正掌握的单词数量为"+str(len(words_real_know)))

if __name__ == '__main__':
    ciku = choose()
    words = test(ciku)
    count(words)
    delicate_read(words)
