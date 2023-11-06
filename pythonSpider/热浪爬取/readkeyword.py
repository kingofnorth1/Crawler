import os
import time
from loguru import logger


def readkeyword():
    fr = open("配置文件.txt", "r", encoding='utf-8')
    linelist = fr.readlines()
    fr.close()
    with open("关键词.txt", "r", encoding='utf-8') as temp:
        data = temp.readlines()
        for i in range(0, len(data)):
            keyData = data[i].split(",")
            line = linelist[i].split(",")
            if int(keyData[1]) == 0:
                # logger.debug(line[0] + line[1])
                return keyData[0], line[0], line[1]
            time.sleep(0.1)
        logger.error("关键词使用完毕")


def writekeyword(word, num, page):
    fr = open("关键词.txt", "r", encoding='utf-8')
    linelist = fr.readlines()
    fr.close()
    frp = open("配置文件.txt", "r", encoding='utf-8')
    pageList = frp.readlines()
    frp.close()
    fw = open("关键词.txt", "w", encoding='utf-8')
    fwp = open("配置文件.txt", "w", encoding='utf-8')
    for i in range(0, len(linelist)):
        keyData = linelist[i].split(",")
        if keyData[0] == word:
            # linelist[i] = linelist[i].replace("0", str(num))
            linelist[i] = linelist[i][0:pageList[i].find(",")]+","+str(num)+"\n"
            pageList[i] = pageList[i][0:pageList[i].find(",")]+","+str(page)+"\n"
            logger.error(pageList[i])
            fw.write(linelist[i])
            fwp.write(pageList[i])
        else:
            fw.write(linelist[i])
            fwp.write(pageList[i])
    fwp.close()
    fw.close()


def priceSelect():
    with open("配置文件.txt", "r", encoding='utf-8') as temp:
        data = temp.readline()
        print(data)


# print(type("0"))
# print(readkeyword())
writekeyword("灯泡", 1, 435435)



# while "i" in "i1534":
#     logger.error("test")


# while True:
#     logger.debug("test")
#     for i in range(0,100):
#         if i == 50:
#             logger.error("跳出")
#             break


# temp = "1416546501,10"
# print(temp.find(","))
# logger.info(temp[temp.find(",")+1:len(temp)])
# # temp = temp.replace(temp[temp.find(",")+1:len(temp)], "464", -1)
# logger.info(temp[0:temp.find(",")])
# logger.debug(temp[0:temp.find(",")]+","+"453465")

def temp(num):
    logger.error(1)


for i in range(0,10):
    cookies = 0
    if (i == 3):
        temp(i)
        cookies = i
    logger.debug(cookies)