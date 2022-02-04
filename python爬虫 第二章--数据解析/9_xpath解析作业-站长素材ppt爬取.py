#需求:站长素材ppt爬取
import os
import requests
from lxml import etree

def func(sum):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
    }
    if sum==1:
        url = 'https://sc.chinaz.com/ppt/free.html'
    else:
        url = 'https://sc.chinaz.com/ppt/free_' + str(sum) + '.html'
    response = requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text

    #解析数据
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="container clearfix"]/div[5]/div')

    for div in div_list:
        ppt_src = 'https://sc.chinaz.com' + div.xpath('./div[2]/a/@href')[0]
        ppt_names = div.xpath('./div[2]/a/text()')[0]

        #下载解析
        ppt_text = requests.get(url=ppt_src,headers=headers).text
        tree = etree.HTML(ppt_text)
        src = tree.xpath('//div[@class="download-url"]/a/@href')[0]
        ppt_data = requests.get(url=src,headers=headers).content

        if not os.path.exists('./ppt素材'):
            os.mkdir('./ppt素材')
        title = './ppt素材/' + ppt_names + '.rar'
        with open(title,'wb') as fp:
            fp.write(ppt_data)
            print(ppt_names,'下载成功！')

if __name__ == "__main__":
    sum = int(input("请输入需要下载的页数:"))
    for i in range(1,sum+1):
        func(i)
