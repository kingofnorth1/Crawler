# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests
if __name__ == "__main__":
    #如何爬取图片数据
    url = "https://i0.hdslb.com/bfs/article/3a1f027f34f49289233edeb71596148ffc6771f5.jpg@942w_564h_progressive.webp"
    #content返回的是二进制形式的图片数据
    img_data = requests.get(url=url).content

    with open("./鬼刀.jpg",'wb') as fp:
        fp.write(img_data)

ex = '<div data-postdate="2021-11-22 17:00" id="idstpc" class><img src=".*?"data-url="(.*?)" border="0"><div>'



