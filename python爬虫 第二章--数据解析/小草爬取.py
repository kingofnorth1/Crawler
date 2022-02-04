# 开发人员：&杜乾坤
# 开发工具：&pycharm
# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests
from bs4 import BeautifulSoup
import os

def func(sum):
    # 创建一个文件夹,保存所有的图片
    if not os.path.exists('./小草'):
        os.mkdir('./小草')
    url = 'https://cle2e479b78947ca.xyz/read.php?tid=707576&inapp=1&isnative=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }

    # 使用通用爬虫对url对应一整页面进行爬取
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    img = soup.select('.idstpc > br')

    # 使用聚焦爬虫对页面解析
    fp = open('./小草/草图','wb')

