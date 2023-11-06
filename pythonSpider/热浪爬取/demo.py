import json
def getCsrfToken(csrf, itemId, userAgent, cookie):
    url = "https://hot.taobao.com/alliance/search/item/phone.do?_csrf="+csrf+"&itemId="+itemId
    print(url)

csrf = "417a80e9-3b41-4743-91bc-40a26226c7dc"
itemId = "668064473331"
getCsrfToken(csrf, itemId, 1,2)

import time
t = time.time()
print (int(round(t * 1000)))    #毫秒级时间戳

params = {
    "jsv": "2.7.0",
    "appKey": "12574478",
    "t": t,
    "sign": "abe9c09312ca49ae07f7d1d30fbd9c17",
    "api": "mtop.taobao.content.ic.newstation.itemcenter.item.query",
    "v": "1.0",
    "valueType": "original",
    "preventFallback": "true",
    "type": "originaljsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp7",
    "data": {"pageNum":1,"pageSize":20,"keyword":"口红","priceSelect":"30","rankType":"1","recommendTabType":0}
}
# params = """{
#     "jsv": "2.7.0",
#     "appKey": "12574478",
#     "t": "t",
#     "sign": "abe9c09312ca49ae07f7d1d30fbd9c17",
#     "api": "mtop.taobao.content.ic.newstation.itemcenter.item.query",
#     "v": "1.0",
#     "valueType": "original",
#     "preventFallback": "true",
#     "type": "originaljsonp",
#     "dataType": "jsonp",
#     "callback": "mtopjsonp7",
#     "data": {"pageNum":1,"pageSize":20,"keyword":"口红","priceSelect":"30","rankType":"1","recommendTabType":0}
# }"""
# st = str(params)
# temp = st.replace("\"", "\'")
# print(str(params))
params = {
    "sw": "123"
}
# st = str(params)
# temp = st.replace("\"", "\'")
# # print(temp)
# temp = json.loads(temp)
# print(type(temp))
print(params['sw'])

