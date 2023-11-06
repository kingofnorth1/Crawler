#编码流程:
#1.验证码的识别，获取验证码图片的文字数据
#2.对post请求进行发送（处理请求参数）
#3.对响应数据进行持久化存储

import requests
from lxml import etree
from chaojiying import Chaojiying_Client

#1.对验证码图片进行捕获和识别
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn' + tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]
code_img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(code_img_data)

#使用超级鹰提供的示例代码对验证码图片进行识别
chaojiying = Chaojiying_Client('northofking', '1314520', '928351')
im = open('code.jpg', 'rb').read()
code = chaojiying.PostPic(im, 1004)
print('验证码:',code)

#post请求的发送(模拟登录)
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE': 'VRfIsAVHt1rumfzGyupWFxJ445WeWJxnILmKmYX3zTEvZ9utO6bNHjJAcKC0HYMKBJ4GO7ckJsuH5MHyG9wtMIxyZHZVr7wKTOau+65g9ZG/yCmutkWvvWXEq4U=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '3441423164@qq.com',
    'pwd': '1314520hxt',
    'code': code,
    'denglu': '登录'
}
response = requests.post(url=login_url,headers=headers,data=data)
print(response.status_code)

login_page_text = response.text

with open('古诗文网.html','w',encoding='utf-8') as fp:
    fp.write(login_page_text)
    print('写入成功！')