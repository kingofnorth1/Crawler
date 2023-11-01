import requests
from fake_useragent import UserAgent
from lxml import etree
import pandas as pd
from openpyxl import load_workbook
import time
import random

def getIp(num):
    ua = UserAgent()
    userAgent = ua.random
    url = "https://www.kuaidaili.com/free/inha/"+str(num)+"/"
    # print(url)
    header = {
        "User-Agent": userAgent,
        "cookie": "channelid=0; sid=1693800232053748; _gcl_au=1.1.1588400466.1693800234; __51vcke__K3h4gFH3WOf3aJqX=bdeef225-f2c0-5dfc-a307-68f1a334cbb2; __51vuft__K3h4gFH3WOf3aJqX=1693800233764; _gid=GA1.2.1844623222.1693800239; sessionid=b4a9ba969cc3c2400bcb4a11b3e2da4a; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1693887987; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1693904704; __51uvsct__K3h4gFH3WOf3aJqX=5; _ga_DC1XM0P4JL=GS1.1.1693904706.7.1.1693904711.55.0.0; _ga=GA1.2.18022577.1644411460; __vtins__K3h4gFH3WOf3aJqX=%7B%22sid%22%3A%20%2212ac114a-229c-5a8b-9f36-ff3939eabce8%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%204392%2C%20%22dr%22%3A%203372%2C%20%22expires%22%3A%201693906511196%2C%20%22ct%22%3A%201693904711196%7D",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer": "https://www.kuaidaili.com/free/inha/"+str(num-1)+"/",
    }
    response = requests.get(url=url, headers=header)
    # if (response.status_code == 403):
    response.encoding = "utf-8"
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//*[@id="list"]/div[1]/table/tbody/tr')
    ip_list = []
    port_list = []
    for tr in tr_list:
        ip = tr.xpath("./td[1]/text()")[0]
        port = tr.xpath("./td[2]/text()")[0]
        ip_list.append(ip)
        port_list.append(port)
        print("爬取的ip",ip,port)
    # print(ip_list)
    with open("ipPort.txt","a") as f:
        for i in range(0,len(ip_list)):
            f.write(ip_list[i]+" "+port_list[i]+"\n")

if __name__ ==  '__main__':
    # number = int(input("请问需要多少条IP?\n"))
    start = int(input("请问从第几页开始？\n"))
    ent = int(input("请问到第几页结束?\n"))
    # numbers = int(number/12)+1
    for num in range(start,ent):
    # for num in range(1,numbers+1):
        # print(num)
        getIp(num)
        time.sleep(random.randint(10,50)/10)
    input("请输入任意键继续")
