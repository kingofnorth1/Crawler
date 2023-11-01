import requests
from lxml import etree
from fake_useragent import UserAgent

a=""
b=""
ua = UserAgent()
url = "http://httpbin.org/get"
header = {
    "User-Agent": ua.random
}
response = requests.get(url=url, headers=header).text
tree = etree.HTML(response)
a = tree.xpath("//div[@class='shop-list J_shop-list shop-all-list']/ul/li")
b = tree.xpath("//div[@class='shop-list J_shop-list shop-all-list']/ul/li")
print(a,b)
if (len(a)==0 & len(b)==0):
    print("输出")