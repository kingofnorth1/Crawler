import requests as requ
# import useragent as useragent
from lxml import etree
import time
import random
# from fake_useragent import UserAgent

def selectArea(city,choose):
    # ua = UserAgent()
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    url = "https://www.dianping.com/"+city+"/"+choose+""
    header = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding" : "gzip, deflate, br",
        "Referer" : "https://www.dianping.com/",
        "User-Agent" : userAgent,
        "Cookie" : "navCtgScroll=0; showNav=javascript:; navCtgScroll=0; showNav=#nav-tab|0|1; _lxsdk_cuid=18a5dced1d7c8-054c0d3839cd76-7f5d5470-144000-18a5dced1d7c8; _lxsdk=18a5dced1d7c8-054c0d3839cd76-7f5d5470-144000-18a5dced1d7c8; WEBDFPID=91x25v0503wx5955z3xu4w30101vv3uw81z4wxvw35597958zxx489v3-2009150951645-1693790950032YOWMMGWfd79fef3d01d5e9aadc18ccd4d0c95071977; _hc.v=bdaa5341-f24b-f4df-39ed-57588c82347f.1693790952; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1693791014; fspop=test; s_ViewType=10; cy=1; cye=shanghai; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; ctu=3f16fa93bd070d3472f95b8ec8b957d7a2a10594553e3e613971dac9abd7b1ec; qruuid=713a4e7b-6d33-4ccd-aa21-800d72dbb6a5; dper=3091e85f2b88fa84ecfa839f1c34d94ba92fce08e7d20af53493df80a2f37bc6943d407a516e8e4b436bc36e2dadcd68912787070d8a65cdb2259ee0949f52f0; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1693801190; _lxsdk_s=18a5e437ad7-387-4f8-376%7C%7C343"
    }
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
    return url_list[num]


if __name__ == "__main__":
    city = "chengdu"
    choose = 'ch10'
    print(selectArea(city,choose))
    time.sleep(100)