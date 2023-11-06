from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

class Spider:
    def __init__(self, url, header, cookie):
        self.url = url
        self.header = header
        self.cookie = cookie
    def parse(self):
        reponse = requests.get(url=self.url, headers=self.header)
        reponse.encoding = "utf-8"
        page_text = reponse.text
        Soup = BeautifulSoup(page_text, 'lxml')
        select = Soup.select("img")
        logger.debug(select)
        findAll = Soup.find_all("img")
        logger.debug(findAll)
        logger.debug(Soup.find_all(attrs={"class": "nav"}))
        # prettify = Soup.prettify()  #将数据显示
        # logger.debug(prettify)

if __name__ == "__main__":
    url = "http://www.bige3.cc/"
    useragent = UserAgent().random
    logger.debug(useragent)
    header = {
        "User-Agent": useragent
    }
    cookie = {
        "Cookie": "BAIDUID=85A36BB34D3A19F3286739BE1AFD599D:FG=1; BIDUPSID=85A36BB34D3A19F3286739BE1AFD599D; PSTM=1698857028; BD_UPN=13314752; COOKIE_SESSION=0_0_1_0_0_1_1_0_1_1_0_0_0_0_0_0_0_0_1698857037%7C1%230_0_1698857037%7C1; baikeVisitId=961a4515-9250-4ebd-bb19-068ee8d72f22; BA_HECTOR=8h0h2g85800g208g8404akah1ik50541q; ZFY=s8z3O2hQq28XHzhRiA7ZTGura5Witc1l5UEv5X50gWo:C"
    }
    Spider(url, header, cookie).parse()
