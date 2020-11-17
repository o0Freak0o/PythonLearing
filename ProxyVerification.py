# -*- codeing = utf-8 -*-
# @Time:2020/11/17 10:25
# @Author:Freak
# @File:ProxyVerification.py
# @Software:PyCharm

import requests
from bs4 import BeautifulSoup
import re
import random

ip_list = []

#https://www.kuaidaili.com/free/
baseurl='https://www.kuaidaili.com/free/'

id_find = re.compile(r'<td data-title="IP">(.*?)</td>')
port_find = re.compile(r'<td data-title="PORT">(.*?)</td>')

def judge(ip,port):
    proxy = {
        'http':ip+':'+port
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        res = requests.get('http://icanhazip.com',proxies=proxy,headers=headers)
    except Exception:
        print('该ip'+ip+'无效')
        return False
    if 200<=res.status_code<300:
        ip_list.append((ip,port))
        print('该ip' + ip + '有效')
        return True
    else:
        print('该ip'+ip+'无效')
        return False


def get_ip_list(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    req = requests.get(url,headers=headers)
    req = req.text
    res = BeautifulSoup(req,'html.parser')
    proxy_id_table = res.find('table',class_='table')
    proxy_id_table = str(proxy_id_table)
    proxy_id_list = re.findall(id_find,proxy_id_table)
    port_list = re.findall(port_find,proxy_id_table)
    for i in range(len(proxy_id_list)):
        judge(proxy_id_list[i],port_list[i])

def get_random_ip():
    ip,port = random.choice(ip_list)
    result = judge(ip,port)
    if result:
        return ip+':'+port
    else:
        ip_list.remove((ip,port))

if __name__ == '__main__':
    get_ip_list(baseurl)
    # present_valid_ip = get_random_ip()
    # print(present_valid_ip)