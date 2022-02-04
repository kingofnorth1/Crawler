# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests
import re
import os

def func(sum):
    # 创建一个文件夹,保存所有的图片
    if not os.path.exists('./4k高清美女'):
        os.mkdir('./4k高清美女')
    url = 'https://pic.netbian.com/4kmeinv/' + 'index_' + sum + '.html'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }

    # 使用通用爬虫对url对应一整页面进行爬取
    page_text = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫对页面解析
    ex = '<li>.*?<img src="(.*?)" alt.*?>.*?</li>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for str in img_src_list:
        # 拼接出一个完整的图片url
        str = 'https://pic.netbian.com/' + str
        # 请求到图片的二进制数据
        img_data = requests.get(url=str, headers=headers).content
        # 生成图片名称
        img_name = str.split('/')[-1]
        # 图片储存的路径
        imgPath = './4k高清美女/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！')

if __name__ == "__main__":
    sum = int(input("请输入需要遍历的页数:"))
    sum += 1
    for n in range(1, sum):
        n = str(n)
        func(n)
