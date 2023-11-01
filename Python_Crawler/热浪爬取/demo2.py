import requests as requests
from fake_useragent import UserAgent
import json
import time
from lxml import etree
import pandas as pd
import time
import os
import random
global cookie_num
cookie_num = 0

def getCookie():
    cookie = ""
    global cookie_num
    with open("cookiesPhone.txt", "r") as f:
        cookie_list = f.readlines()
        if (cookie_num <= len(cookie_list)-1):
            for i in range(0, len(cookie_list)):
                if (i == cookie_num):
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            input("cookie已经消耗完毕！！！")
            quit()
    cookie_num += 1
    return cookie

def getCsrf(token):
    for StrList in token.split('; '):
        list = StrList.split('=')
        if (list[0] == "XSRF-TOKEN"):
            tempStr = list[1]
            # print(tempStr)
            return tempStr

def getPhoneNum(itemIds, itemNames, userAgent, cookie):         #获取hot.taobao.com电话
    phoneNum = []
    # for i in range(len(itemIds)):
    csrf = getCsrf(cookie)
    url = "https://hot.taobao.com/alliance/search/item/phone.do?_csrf="+str(csrf)+"&itemId="+itemIds[0]
    print(url)
    header = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Referer": "https://www.dianping.com/",
        "authority": "hot.taobao.com",
        "method": "GET",
        "path": url[21:-0],
        "scheme": "https",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Bx-V": "2.5.3",
        "Cookie": cookie,
        "Referer": "https://hot.taobao.com/hw/union/hw-alliance/store?checkIcTags=0&hasSample=0&isDirect=0&keyword=%E5%8F%A3%E7%BA%A2&lowPrice=30&rankType=2",
        "User-Agent": userAgent,
        "X-Xsrf-Token": csrf
    }
    temp = ""
    # try :
    resp = requests.get(url=url, headers=header)
    page_text = resp.text
    print(page_text)
    # data = json.loads(page_text)
    # temp = str(data['data'])
    # phoneNum.append(temp)
    # except :
    #     temp = ""
    #     phoneNum.append(temp)
    # time.sleep(random.randint(20, 30) / 10)
    # print("商品id："+str(itemIds[i])+"  商家名称："+str(itemNames[i])+"  商家电话："+temp)
    # df = pd.DataFrame({
    #     # "商品id": itemIds,
    #     "商家名称": itemNames,
    #     "商家电话": phoneNum
    # })
    # print(df)
    # return df

if __name__ == "__main__":
    cookie = getCookie()
    ua = UserAgent()
    itemId = ["668064473331"]
    itemName = ["0."]
    userAgent = ua.random
    getPhoneNum(itemId,itemName,userAgent,cookie)