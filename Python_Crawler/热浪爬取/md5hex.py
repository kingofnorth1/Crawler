import hashlib
import json

global cookie_name
cookie_name = 0

def getCookieName():
    cookie = ""
    global cookie_name
    with open("cookiesName.txt", "r") as f:
        cookie_list = f.readlines()
        if (cookie_name <= len(cookie_list)-1):
            for i in range(0, len(cookie_list)):
                if (i == cookie_name):
                    cookie_list[i] = cookie_list[i].strip("\n")
                    cookie = cookie_list[i]
        else:
            input("cookie已经消耗完毕！！！")
            quit()
    cookie_name += 1
    return cookie

def getH5Token(cookie):
    for StrList in cookie.split('; '):
        list = StrList.split('=')
        if (list[0] == "_m_h5_tk"):
            tempStr = list[1]
            tempStr = tempStr.split("_")
            print(tempStr[0])
            return tempStr[0]

def md5hex(cookie, nowt, appkey, data):
    h5_token = getH5Token(cookie)
    string = h5_token+"&"+nowt+"&"+appkey+"&"+data
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    print(hl.hexdigest())
    return (hl.hexdigest())

cookie = getCookieName()
# print(cookie)
md5hex(cookie,'1697957190078','12574478','{"pageNum":1,"pageSize":20,"keyword":"口红","priceSelect":"30","rankType":"2","recommendTabType":0}')