from fake_useragent import UserAgent
import requests
from lxml import etree
import os
#项目需求:解析出所有城市名称http://www.aqistudy.cn/historydata/

if __name__ == "__main__":
    # us = UserAgent()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    # }
    # url = "http://www.aqistudy.cn/historydata/"
    # page_text = requests.get(url=url,headers=headers).text
    #
    # #解析数据
    # tree = etree.HTML(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    #
    # #解析到了热门城市的城市名称
    # for li in host_li_list:
    #     host_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(host_city_name)
    #
    # #解析全部城市的名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    #
    # print(all_city_names,len(all_city_names))
    us = UserAgent()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    url = "http://www.aqistudy.cn/historydata/"
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a            热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a    全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))

