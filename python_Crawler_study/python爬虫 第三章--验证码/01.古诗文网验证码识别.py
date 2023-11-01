import requests
from lxml import etree
from chaojiying import Chaojiying_Client

#将验证码图片下载到本地
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = requests.get(url=url,headers=headers).text
#解析验证码图片img中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn' + tree.xpath('//div[@class="mainreg2"]/img/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)

#调用打码平台的示例程序进行验证码图片数据识别
chaojiying = Chaojiying_Client('northofking', '1314520', '928351')	#用户中心>>软件ID 生成一个替换 96001
im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
data = chaojiying.PostPic(im, 1004)
print ('识别结果为:',data)


