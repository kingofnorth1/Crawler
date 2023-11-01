import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
urls = {
    'https://www.cnblogs.com/12580s/p/9332803.html',
    'https://www.baidu.com/s?wd=%E9%BB%84%E8%8A%AF%E6%A1%90&rsv_spt=1&rsv_iqid=0xf1c2a742000a86d0&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=16&rsv_sug1=15&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=11353&rsv_sug4=14545',
    'https://www.bilibili.com/video/BV1Yh411o7Sz?p=39'
}
def get_content(url):
    print('正在爬取:',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print('响应数据的长度为:',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)

