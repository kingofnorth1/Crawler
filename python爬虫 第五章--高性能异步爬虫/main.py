# string = {'1':'a','2':'b'}
# print(type(string['1']))
import re

str1='https://video.pearvideo.com/mp4/third/20220209/cont-1751458-12033417-145907-hd.mp4'
str2='https://video.pearvideo.com/mp4/third/20220209/1644508194268-12033417-145907-hd.mp4'
num = '1751458'
str3 = '/cont-'+num+'-'

str2 = re.sub('/(\d)*-',str3,str2)

print(str2)