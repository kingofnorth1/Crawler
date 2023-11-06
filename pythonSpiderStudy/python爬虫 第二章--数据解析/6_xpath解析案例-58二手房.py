from datetime import time
from fake_useragent import UserAgent
from lxml import etree
import requests

#需求:爬取58二手房中的房源信息
if __name__ == '__main__':
    #爬取到页面源码数据
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    url = 'https://cd.58.com/ershoufang'
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    fp = open('58.txt','w',encoding='utf-8')
    for div in div_list:
        #局部解析
        title = div.xpath('./a//div[@class="property-content-title"]/h3/@title')[0]
        price = div.xpath('./a//p[@class="property-price-total"]//text()')[0]
        print(title)
        print(price)
        fp.write('价格:'+price+'万     口号:'+title+'\n')
