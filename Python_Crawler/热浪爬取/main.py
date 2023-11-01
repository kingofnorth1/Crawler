import sys
from loguru import logger
import requests as requests
from fake_useragent import UserAgent
import json
from urllib import parse
import hashlib
import time
from lxml import etree
import pandas as pd
import time
import os
import random
import signal

global num
num = 0

global repeatNum
repeatNum = 0

global cookie_num
cookie_num = 0

global cookie_name
cookie_name = 0

global cookie_temp_number
cookie_temp_number = ""


def getPhoneNum(
    itemIds,
    itemName,
    itemPrice,
    soldQuantity,
    itemShopId,
    itemShopName,
    userAgent,
    cookie,
    filePath,
    number,
    keyword,
):  # 获取hot.taobao.com电话
    if len(itemIds) == 0:
        return True
    flag = False
    for i in range(len(itemIds)):
        # print("是否重复："+str(removeRepeat(filePath, str(itemShopName[i]))))
        if not removeRepeat(filePath, str(itemShopName[i])):
            csrf = getCsrf(cookie)
            url = (
                "https://hot.taobao.com/alliance/search/item/phone.do?_csrf="
                + csrf
                + "&itemId="
                + str(itemIds[i])
            )
            logger.info(url)
            header = {
                "authority": "hot.taobao.com",
                "method": "GET",
                "path": url[21 : len(url)],
                "scheme": "https",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Bx-V": "2.5.3",
                "Cookie": cookie,
                "Referer": "https://hot.taobao.com/hw/union/hw-alliance/store?checkIcTags=0&hasSample=0&isDirect=0&keyword=%E5%8F%A3%E7%BA%A2&lowPrice=30&rankType=2",
                "User-Agent": userAgent,
                "X-Xsrf-Token": csrf,
            }
            tempItemId = [str(itemIds[i])]
            tempItemName = [str(itemName[i])]
            tempItemPrice = [str(itemPrice[i])]
            tempSoldQuantity = [str(soldQuantity[i])]
            # tempShopId = [str(itemShopId[i])]
            tempShopName = [str(itemShopName[i])]
            tempShopPhone = []
            numbers = [number]
            try:
                resp = requests.get(url=url, headers=header)
                page_text = resp.text
                data = json.loads(page_text)
                temp = str(data['data'])
                while (
                    "https://hot.taobao.com:443//alliance/search/item/phone.do/_____tmd_____/punish?x5secdata="
                    in temp
                ):
                    cookie_temp_number = getCookiePhone(keyword, number)
                    csrf = getCsrf(cookie_temp_number)
                    url = (
                        "https://hot.taobao.com/alliance/search/item/phone.do?_csrf="
                        + csrf
                        + "&itemId="
                        + str(itemIds[i])
                    )
                    logger.info(url)
                    header = {
                        "authority": "hot.taobao.com",
                        "method": "GET",
                        "path": url[21 : len(url)],
                        "scheme": "https",
                        "Accept": "application/json, text/plain, */*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                        "Bx-V": "2.5.3",
                        "Cookie": cookie_temp_number,
                        "Referer": "https://hot.taobao.com/hw/union/hw-alliance/store?checkIcTags=0&hasSample=0&isDirect=0&keyword=%E5%8F%A3%E7%BA%A2&lowPrice=30&rankType=2",
                        "User-Agent": userAgent,
                        "X-Xsrf-Token": csrf,
                    }
                    tempItemId = [str(itemIds[i])]
                    tempItemName = [str(itemName[i])]
                    tempItemPrice = [str(itemPrice[i])]
                    tempSoldQuantity = [str(soldQuantity[i])]
                    # tempShopId = [str(itemShopId[i])]
                    tempShopName = [str(itemShopName[i])]
                    tempShopPhone = []
                    numbers = [number]
                    resp = requests.get(url=url, headers=header)
                    page_text = resp.text
                    data = json.loads(page_text)
                    temp = str(data['data'])
                tempShopPhone.append(temp)
            except:
                temp = ""
                tempShopPhone.append(temp)
            global num
            logger.info(
                "第"
                + str(num)
                + "条数据  "
                + "商品id："
                + tempItemId[0]
                + "  商品名称："
                + tempItemName[0]
                + "  商品价格："
                + tempItemPrice[0]
                + "  商品销量："
                + tempSoldQuantity[0]
                + "  商店名称："
                + tempShopName[0]
                + "  商家电话："
                + tempShopPhone[0]
            )
            num += 1
            df = pd.DataFrame(
                {
                    "页数": numbers,
                    "商家id": tempItemId,
                    "商品名称": tempItemName,
                    "商品价格": tempItemPrice,
                    "商品销量": tempSoldQuantity,
                    "商家名称": tempShopName,
                    "商家电话": tempShopPhone,
                }
            )
            saveExcel(filePath, df)
            time.sleep(random.randint(15, 25) / 10)
        else:
            global repeatNum
            logger.info("重复：" + str(repeatNum))
            repeatNum += 1
            time.sleep(random.randint(5, 10) / 10)


def getNameNum(dataList, userAgent, cookie, appkey, filePath, keyword, i):  # 获取h5api姓名
    header = {
        "authority": "h5api.m.taobao.com",
        "method": "GET",
        # "path": "/h5/mtop.taobao.content.ic.newstation.itemcenter.item.query/1.0/?jsv=2.7.0&appKey=12574478&t=1697867304999&sign=f52516cc248d7956ac9aa4a0a23d0b1b&api=mtop.taobao.content.ic.newstation.itemcenter.item.query&v=1.0&valueType=original&preventFallback=true&type=originaljsonp&dataType=jsonp&callback=mtopjsonp7&data=%7B%22pageNum%22%3A1%2C%22pageSize%22%3A20%2C%22keyword%22%3A%22%E5%8F%A3%E7%BA%A2%22%2C%22priceSelect%22%3A%2230%22%2C%22rankType%22%3A%222%22%2C%22recommendTabType%22%3A0%7D",
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Cookie": cookie,
        "Referer": "https://hot.taobao.com/",
        "Sec-Fetch-Mode": "no-cors",
        "User-Agent": userAgent,
    }
    t = time.time()
    t = str(int(round(t * 1000)))
    sign = signMd5Hex(cookie, t, appkey, dataList)
    dataList = parse.quote(dataList)
    url = (
        "https://h5api.m.taobao.com/h5/mtop.taobao.content.ic.newstation.itemcenter.item.query/1.0/?jsv=2.7.0&appKey="
        + appkey
        + "&t="
        + t
        + "&sign="
        + sign
        + "&api=mtop.taobao.content.ic.newstation.itemcenter.item.query&v=1.0&valueType=original&preventFallback=true&type=originaljsonp&dataType=jsonp&callback=mtopjsonp16&data="
        + dataList
    )
    logger.info(url)
    resp = requests.get(url=url, headers=header)
    resp.encoding = "utf-8"
    page_text = resp.text
    while "过期" in page_text:
        cookie_temp_number = getCookiePhone(keyword, i)
        header = {
            "authority": "h5api.m.taobao.com",
            "method": "GET",
            # "path": "/h5/mtop.taobao.content.ic.newstation.itemcenter.item.query/1.0/?jsv=2.7.0&appKey=12574478&t=1697867304999&sign=f52516cc248d7956ac9aa4a0a23d0b1b&api=mtop.taobao.content.ic.newstation.itemcenter.item.query&v=1.0&valueType=original&preventFallback=true&type=originaljsonp&dataType=jsonp&callback=mtopjsonp7&data=%7B%22pageNum%22%3A1%2C%22pageSize%22%3A20%2C%22keyword%22%3A%22%E5%8F%A3%E7%BA%A2%22%2C%22priceSelect%22%3A%2230%22%2C%22rankType%22%3A%222%22%2C%22recommendTabType%22%3A0%7D",
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate,br",
            "Cookie": cookie_temp_number,
            "Referer": "https://hot.taobao.com/",
            "Sec-Fetch-Mode": "no-cors",
            "User-Agent": userAgent,
        }
        t = time.time()
        t = str(int(round(t * 1000)))
        sign = signMd5Hex(cookie, t, appkey, dataList)
        dataList = parse.quote(dataList)
        url = (
            "https://h5api.m.taobao.com/h5/mtop.taobao.content.ic.newstation.itemcenter.item.query/1.0/?jsv=2.7.0&appKey="
            + appkey
            + "&t="
            + t
            + "&sign="
            + sign
            + "&api=mtop.taobao.content.ic.newstation.itemcenter.item.query&v=1.0&valueType=original&preventFallback=true&type=originaljsonp&dataType=jsonp&callback=mtopjsonp16&data="
            + dataList
        )
        logger.info(url)
        resp = requests.get(url=url, headers=header)
        resp.encoding = "utf-8"
        page_text = resp.text
    NameJson = page_text[page_text.find("{") : -1]
    data = json.loads(NameJson)
    itemId = []
    itemName = []
    itemPrice = []
    itemShopId = []
    itemShopName = []
    soldQuantity = []
    for i in range(len(data['data']['model']['list'])):
        shopName = data['data']['model']['list'][i]['extendVal']['shopInfo']['shopName']
        if shopName not in itemShopName:
            itemId.append(data['data']['model']['list'][i]['itemId'])
            itemName.append(data['data']['model']['list'][i]['itemName'])
            itemPrice.append(data['data']['model']['list'][i]['itemPrice'])
            soldQuantity.append(data['data']['model']['list'][i]['soldQuantity'])
            itemShopId.append(
                data['data']['model']['list'][i]['extendVal']['shopInfo']['safeShopId']
            )
            itemShopName.append(
                data['data']['model']['list'][i]['extendVal']['shopInfo']['shopName']
            )
    return itemId, itemName, itemPrice, soldQuantity, itemShopId, itemShopName


def getCookiePhone(keyword, numi):
    logger.debug("更换cookie")
    cookie = ""
    global cookie_num
    with open("cookiesPhone.txt", "r") as f:
        cookie_list = f.readlines()
        if cookie_num <= len(cookie_list) - 1:
            for i in range(0, len(cookie_list)):
                if i == cookie_num:
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            logger.error("cookiePhone已经消耗完毕！！！")
            writekeyword(keyword, 0, numi)
            logger.error("请回车退出")
            input("")
            pid = os.getpid()
            # 结束指定的进程
            target_pid = pid  # 替换为要结束的进程的ID
            os.kill(target_pid, signal.SIGTERM)
    cookie_num += 1
    return cookie


def getCookieName():
    cookie = ""
    global cookie_name
    with open("cookiesName.txt", "r") as f:
        cookie_list = f.readlines()
        if cookie_name <= len(cookie_list) - 1:
            for i in range(0, len(cookie_list)):
                if i == cookie_name:
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            logger.error("cookieName已经消耗完毕！！！")
            quit()
    cookie_name += 1
    return cookie


def getCsrf(token):
    for StrList in token.split('; '):
        list = StrList.split('=')
        if list[0] == "XSRF-TOKEN":
            tempStr = list[1]
            # print(tempStr)
            return tempStr


def saveExcel(filePath, dfFile):
    if not os.path.exists(filePath):
        dfFile.to_csv(filePath, index=False, header=True, encoding="utf_8_sig")
        # dfFile.to_csv(filePath, index=False, header=True, encoding="utf_8_sig")
    else:
        dfFile.to_csv(
            filePath, mode="a", header=False, index=False, encoding="utf_8_sig"
        )


def getH5Token(cookie):
    for StrList in cookie.split('; '):
        list = StrList.split('=')
        if list[0] == "_m_h5_tk":
            tempStr = list[1]
            tempStr = tempStr.split("_")
            return tempStr[0]


def signMd5Hex(cookie, nowt, appkey, data):
    h5_token = getH5Token(cookie)
    string = h5_token + "&" + nowt + "&" + appkey + "&" + data
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()


def removeRepeat(filePath, shopName):
    if not os.path.exists(filePath):
        df = pd.DataFrame(
            {
                "页数": [""],
                "商家id": [""],
                "商品名称": [""],
                "商品价格": [""],
                "商品销量": [""],
                "商家名称": [""],
                "商家电话": [""],
            }
        )
        saveExcel(filePath, df)
    df1 = pd.read_csv(filePath, header=None)
    return shopName in str(df1.iloc[:, 5].values)


def readkeyword():
    fr = open("配置文件.txt", "r", encoding='utf-8')
    linelist = fr.readlines()
    fr.close()
    with open("关键词.txt", "r", encoding='utf-8') as temp:
        data = temp.readlines()
        for i in range(0, len(data)):
            keyData = data[i].split(",")
            line = linelist[i].split(",")
            if int(keyData[1]) == 0:
                # logger.debug(line[0] + line[1])
                return keyData[0], line[0], line[1]
            time.sleep(0.1)
        logger.error("关键词使用完毕")


def writekeyword(word, numbers, page):
    fr = open("关键词.txt", "r", encoding='utf-8')
    linelist = fr.readlines()
    fr.close()
    frp = open("配置文件.txt", "r", encoding='utf-8')
    pageList = frp.readlines()
    frp.close()
    fw = open("关键词.txt", "w", encoding='utf-8')
    fwp = open("配置文件.txt", "w", encoding='utf-8')
    for i in range(0, len(linelist)):
        keyData = linelist[i].split(",")
        if keyData[0] == word:
            linelist[i] = (
                linelist[i][0 : linelist[i].find(",")] + "," + str(numbers) + "\n"
            )
            pageList[i] = (
                pageList[i][0 : pageList[i].find(",")] + "," + str(page) + "\n"
            )
            logger.error(pageList[i])
            fw.write(linelist[i])
            fwp.write(pageList[i])
        else:
            fw.write(linelist[i])
            fwp.write(pageList[i])
    fwp.close()
    fw.close()


if __name__ == '__main__':
    temp = True
    try:
        while True:
            num = 0
            repeatNum = 0
            cookie_num = 0
            cookie_name = 0
            keyword, priceSelect, pageNum = readkeyword()
            # cookiephone = getCookiePhone(keyword, 1)
            if temp:
                temp = False
                cookie_temp_number = getCookiePhone(keyword, 1)
            ua = UserAgent()
            userAgent = ua.random
            rankType = "2"
            recommendTabType = 0

            filePath = keyword + ".csv"
            end_number = 100
            appkey = str(12574478)
            for i in range(int(pageNum), end_number + 1):
                print(
                    "*****************************************************************************"
                )
                print(
                    "                         开始爬取第"
                    + str(i)
                    + "页                                  "
                )
                logger.debug("开始爬取" + keyword + "关键字！！！")
                dataList = (
                    '{"pageNum":'
                    + str(i)
                    + ',"pageSize":20,"keyword":"'
                    + keyword
                    + '","priceSelect":"'
                    + priceSelect
                    + '","rankType":"'
                    + rankType
                    + '","recommendTabType":'
                    + str(recommendTabType)
                    + '}'
                )
                (
                    itemId,
                    itemName,
                    itemPrice,
                    soldQuantity,
                    itemShopId,
                    itemShopName,
                ) = getNameNum(
                    dataList,
                    userAgent,
                    cookie_temp_number,
                    appkey,
                    filePath,
                    keyword,
                    i,
                )
                time.sleep(random.randint(20, 30) / 10)
                dfFile = getPhoneNum(
                    itemId,
                    itemName,
                    itemPrice,
                    soldQuantity,
                    itemShopId,
                    itemShopName,
                    userAgent,
                    cookie_temp_number,
                    filePath,
                    str(i),
                    keyword,
                )
                if dfFile:
                    writekeyword(keyword, 1, i)
                    break
                time.sleep(random.randint(40, 70) / 10)
                writekeyword(keyword, 0, i + 1)
                print(
                    "*****************************************************************************"
                )
                print(
                    "                       第"
                    + str(i)
                    + "页已经爬取完毕                                "
                )
                logger.info(
                    "已经爬取" + str(num) + "条数据", "爬取的重复数据：" + str(repeatNum) + "条数据"
                )
            # writekeyword(keyword, 1, num)
            logger.error(keyword + "关键字已经爬取结束，请查看数据")
    except:
        logger.error("请回车退出！")
        input("")
