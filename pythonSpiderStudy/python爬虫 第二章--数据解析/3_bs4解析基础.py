from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    #将本地的html文档中html文档中的数据加载到该对象中
    url = 'https://www.shicimingju.com/shicimark'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    page = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(page,'lxml')
    #print(soup)
    #print(soup.a)
    #print(soup.div)
    #print(soup.find('div'))
    print(soup.find('div', class_="mark_card").text)
    #print(soup.select('.mark_card'))
    #print(soup.select('.mark_card > a > img')[0]['src'])

