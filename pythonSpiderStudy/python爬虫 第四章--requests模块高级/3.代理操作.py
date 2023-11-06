import requests

url = 'http://ip.293.net/'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
page_text = requests.get(url=url,headers=headers,proxies={"https":''}).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)