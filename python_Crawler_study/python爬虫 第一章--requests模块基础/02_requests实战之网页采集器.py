import requests
import os
#指定搜索关键字
word = input('enter a word you want to search:')
#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
#指定url
url = 'https://www.sogou.com/web'
#封装get请求参数
prams = {
    'query':word,
    'ie':'utf-8'
}
#发起请求
response = requests.get(url=url,params=prams,headers=headers)

#获取响应数据
page_text = response.text

with open('./sougou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

