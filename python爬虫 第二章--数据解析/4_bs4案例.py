#需求:爬取三国演义小说所有的章节标题和章节内容https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    #对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    page_text = requests.get(url=url,headers=headers)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers)
        detail_page_text.encoding = 'utf-8'
        detail_page_text = detail_page_text.text
        #解析出详情页相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(li.a.string+':'+content+'\n')
        print(li.a.string,'爬取成功！！！')

