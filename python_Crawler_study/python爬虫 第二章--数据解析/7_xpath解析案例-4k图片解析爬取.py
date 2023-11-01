 #需求:解析下载图片数据 http://pic.netbian.com/4kmeinv/
from fake_useragent import UserAgent
import requests
from lxml import etree
import os

def img(sum):
    us = UserAgent()
    headers = {
        'UserAgent': us.random
    }
    url = "https://pic.netbian.com/4kmeinv" + '/index_' + sum + '.html'
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text

    # 数据解析:src的属性值  alt属性
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')

    # 创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src = "https://pic.netbian.com" + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用处理中文乱码的解决方法
        # img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name,img_src)

        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功!')

if __name__ == "__main__":
    sum = int(input("请输入需要遍历的页数:"))
    sum += 1
    for n in range(1, sum):
        n = str(n)
        img(n)

