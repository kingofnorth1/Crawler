import os
import re
import requests
from random import random
from lxml import etree
from multiprocessing.dummy import Pool
#需求:爬取梨视频的视频数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
#原则:线程池处理的是阻塞且耗时的操作
data_path = './梨视频/'
if not os.path.exists(data_path):
    os.mkdir(data_path)

#对下述url发起请求解析出视频详情的url和视频名称
url = 'https://www.pearvideo.com/category_5'        #第一层url
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="listvideo-list clearfix"]/li')
urls = []  #存储所有视频的链接and名字

for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]        #第二层url
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    #对详情页的url发起请求
    session = requests.Session()
    detail_page_text = session.get(url=detail_url,headers=headers).text

    #从详情页中解析出视频的地址（url）
    detail_tree = etree.HTML(detail_page_text)
    video_number = detail_tree.xpath('//div[@class="video-main"]/div[2]/@data-cid')[0]

    #字典添加
    headers.update({'Referer': 'https://www.pearvideo.com/video_' + video_number})
    # while (video_detail_url == "") :s
    random_number = str(round(random(),16))         #小数点后16位随机数
    video_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + video_number + '&&mrd=' + random_number           #第三层url
    video_text = session.get(url=video_url, headers=headers).json()

    #获取视频url地址
    video_detail_url = video_text.get('videoInfo').get('videos').get('srcUrl')

    #正则替换
    str1 = '/cont-' + video_number + '-'
    video_detail_url = re.sub('/(\d)*-',str1,video_detail_url)
    dic = {
        'name':name,
        'url':video_detail_url
    }
    urls.append(dic)

#对视频链接发起请求获取视频的二进制数据,然后将视频进行返回
def get_video_data(dic):
    url = dic['url']
    name = dic['name']
    data = requests.get(url=url,headers=headers).content
    if (name=='理想的房子 x 卡门 | 愿你历尽相逢和离别，依然相信爱.mp4'):
        name='理想的房子 x 卡门  愿你历尽相逢和离别，依然相信爱.mp4'
    with open(data_path+name,'wb') as fp:
        fp.write(data)
        print(name,' 下载完毕！')


#使用线程池对视频数据进行请求(较为耗时的阻塞操作)
pool = Pool(4)
pool.map(get_video_data,urls)

pool.close()

    # 'https://video.pearvideo.com/mp4/third/20220209/cont-1751458-12033417-145907-hd.mp4'
    # 'https://video.pearvideo.com/mp4/third/20220209/1644508194268-12033417-145907-hd.mp4'
    # 'https://image.pearvideo.com/cont/20220209/12033417-151119-1.png'


