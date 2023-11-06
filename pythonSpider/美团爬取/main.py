import os
import requests as requ
from lxml import etree
import pandas as pd
# from openpyxl import load_workbook
import time
import random
from fake_useragent import UserAgent

global cookie_num
cookie_num = 0
global ip_num
ip_num = 0
# try:
def requestMeiTuan(area_url,num,cookie,userAgent):
    # ua = UserAgent()
    # userAgent = ua.random
    # url = "https://www.dianping.com/" + city + "/"+choose+"/p" + str(num)
    url = area_url+"p"+str(num)
    header = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding" : "gzip, deflate, br",
        "Referer" : area_url+"p"+str(num-1),
        "User-Agent" : userAgent,
        "Cookie" : cookie
    }
    time.sleep(random.randint(10, 20)/10)
    resp = requ.get(url=url, headers=header)
    if (resp.status_code == 403):
        if (readport() != ""):
            for i in range(0,5):
                proxy = {
                    'http': readport()
                }
                resp = requ.get(url=url, headers=header, proxies=proxy, verify=False)
                if (resp.status_code == requ.codes.ok):
                    break
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": area_url + "p" + str(num - 1),
                "User-Agent": userAgent,
                "Cookie": readCookie()
            }
            resp = requ.get(url=url, headers=header)
            if (resp.status_code != requ.codes.ok):
                global cookie_num
                input("第1个到第"+cookie_num+"个cookie全部失效，请重新查找cookie！！！(任意键结束)")
                quit()
        else:
            input("需要登录网络手动验证！！！(任意键结束)")
            quit()
    resp.encoding = "utf-8"
    page_text = resp.text

    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class='shop-list J_shop-list shop-all-list']/ul/li")
    if (len(li_list) == 0):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": area_url + "p" + str(num - 1),
            "User-Agent": userAgent,
            "Cookie": readCookie()
        }
        resp = requ.get(url=url, headers=header)
        resp.encoding = "utf-8"
        page_text = resp.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath("//div[@class='shop-list J_shop-list shop-all-list']/ul/li")
    title_list = []
    comment_list = []
    address_list = []
    phone_list = []
    for li in li_list:
        # time.sleep(random.randint(5,20)/10)
        phone_url = li.xpath('./div[2]/div[1]/a/@href')[0]
        phone_number, address = phone_get(phone_url,url,cookie)
        print(phone_number, address)
        phone_list.append(phone_number)
        address_list.append(address)
        title_list.append(li.xpath('./div[2]/div[1]/a/h4/text()')[0])
        comment_list.append(li.xpath('./div[2]/div[2]/a/b/text()')[0])

    df = pd.DataFrame({
        "商家名称": title_list,
        "商家评论": comment_list,
        "商家地址": address_list,
        "商家电话": phone_list,
    })
    print(df)
    return df

def saveExcel(filePath,dfFile):
    if not os.path.exists(filePath):
        dfFile.to_csv(filePath, index=False, header=False, encoding="utf_8_sig")
    else:
        dfFile.to_csv(filePath, mode="a", header=False, index=False, encoding="utf_8_sig")



def phone_get(phone_url,url,cookie):
    ua = UserAgent()
    userAgent = ua.random
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie": cookie,
        "Host": "www.dianping.com",
        "Referer": url,
        "Sec-Ch-Ua":'"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Windows",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent": userAgent,
    }
    time.sleep(random.randint(50, 65) / 10)
    resp = requ.get(url=phone_url, headers=header)
    if (resp.status_code == 403):
        if (readport() != ""):
            for i in range(0,5):
                proxy = {
                    'http': readport()
                }
                resp = requ.get(url=url, headers=header, proxies=proxy, verify=False)
                if (resp.status_code == requ.codes.ok):
                    break
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": readCookie(),
                "Host": "www.dianping.com",
                "Referer": url,
                "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "Windows",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": userAgent,
            }
            resp = requ.get(url=url, headers=header)
            if (resp.status_code != requ.codes.ok):
                global cookie_num
                input("第1个到第"+cookie_num+"个cookie全部失效，请重新查找cookie！！！(任意键结束)")
                quit()
        else:
            input("需要登录网络手动验证！！！(任意键结束)")
            quit()
    resp.encoding = "utf-8"
    page_text = resp.text
    # print(page_text)
    tree = etree.HTML(page_text)
    phone_number = tree.xpath("//div[@id='basic-info']/p//text()")[2]
    address = tree.xpath("//div[@class='expand-info address']/div/span/text()")[0]
    if (len(phone_number) == 0 & len(address) == 0):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": readCookie(),
            "Host": "www.dianping.com",
            "Referer": url,
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": userAgent,
        }
        resp = requ.get(url=url, headers=header)
        resp.encoding = "utf-8"
        page_text = resp.text
        tree = etree.HTML(page_text)
        phone_number = tree.xpath("//div[@id='basic-info']/p//text()")[2]
        address = tree.xpath("//div[@class='expand-info address']/div/span/text()")[0]

    return phone_number, address


def selectArea(city,choose,cookie,userAgent):
    # ua = UserAgent()
    # userAgent = ua.random
    # userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    url = "https://www.dianping.com/"+city+"/"+choose+""
    header = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding" : "gzip, deflate, br",
        "Referer" : "https://www.dianping.com/",
        "User-Agent" : userAgent,
        "Cookie" : cookie
    }
    time.sleep(random.randint(10, 50) / 10)
    resp = requ.get(url=url, headers=header)
    resp.encoding = "utf-8"
    page_text = resp.text
    # print(page_text)
    tree = etree.HTML(page_text)
    a_list = tree.xpath("//div[@id='region-nav']/a")
    name_list = []
    url_list = []
    for a in a_list:
        name = a.xpath("./span/text()")[0]
        url = a.xpath("./@href")[0]
        name_list.append(name)
        url_list.append(url)
    for i in range(0, len(name_list)):
        print(i, name_list[i])
    num = int(input("请输入所需要爬取的地区的编号\n"))
    print(url_list[num])
    return url_list[num]

def fileMaxPage(area_url,cookie,userAgent):
    # ua = UserAgent()
    # userAgent = ua.random
    # userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    url = area_url
    header = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding" : "gzip, deflate, br",
        "Referer" : "https://www.dianping.com/",
        "User-Agent" : userAgent,
        "Cookie" : cookie
    }
    time.sleep(random.randint(10, 50) / 10)
    resp = requ.get(url=url, headers=header)
    resp.encoding = "utf-8"
    page_text = resp.text
    # print(page_text)
    tree = etree.HTML(page_text)
    maxPage = tree.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/a[last()-1]/text()")[0]
    return maxPage

def readport():
    global ip_num
    with open("ipPort.txt","r") as f:
        # for line in f.readlines():
        line = f.readlines(ip_num)
        line = line.strip("\n")
        ip = line.split(" ")[0]
        port = line.split(" ")[1]
    ip_port = ip+":"+port
    ip_num +=1
    return ip_port

def readCookie():
    cookie = ""
    global cookie_num
    with open("cookies.txt", "r") as f:
        cookie_list = f.readlines()
        if (cookie_num<=len(cookie_list)-1):
            for i in range(0, len(cookie_list)):
                if (i == cookie_num):
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            input("cookie已经消耗完毕！！！")
            quit()
    cookie_num += 1
    return cookie


if __name__ ==  '__main__':
    # try:
        # sheetName = 'Sheet1'
        choose = 'ch10'
        city = input("请输入所需的城市(拼音):\n")
        filePath = input("请输入所需保存的文件名称:\n")+".csv"
        start_number = int(input("请输入需要从第几页开始:\n"))
        # end_number = int(input("请输入需要到第几页结束:\n"))
        # print(selectArea(city, choose))
        cookie = input("请输入cookie(不填可以使用默认的):\n")
        if (cookie == ""):
            cookie = readCookie()
        ua = UserAgent()
        userAgent = ua.random
        area_url = selectArea(city, choose, cookie, userAgent)
        end_number = int(fileMaxPage(area_url, cookie, userAgent))
        # print(end_number)
        # time.sleep(1000)
        for i in range(start_number,end_number+1):
            print("*****************************************************************************")
            print("                         开始爬取第"+str(i)+"页                                  ")
            dfFile = requestMeiTuan(area_url, i, cookie, userAgent)
            saveExcel(filePath, dfFile)
            time.sleep(random.randint(50,100)/10)
            print("*****************************************************************************")
            print("                       第"+str(i)+"页已经爬取完毕                                ")
        # print("爬取结束，请查看数据")
        input("爬取结束，请查看数据（输入任意键结束）")
    # except Exception:
    #     input("爬取结束，请查看数据（输入任意键结束）")
    #     exit()


