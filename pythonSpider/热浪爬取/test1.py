from urllib import parse
import os
import pandas as pd
from loguru import logger

s = """https://h5api.m.taobao.com/h5/mtop.taobao.content.ic.newstation.itemcenter.item.query/1.0/?jsv=2.7.0&appKey=12574478&t=1697885764509&sign=138d02075a244f560268e92047363373&api=mtop.taobao.content.ic.newstation.itemcenter.item.query&v=1.0&valueType=original&preventFallback=true&type=originaljsonp&dataType=jsonp&callback=mtopjsonp7&data={"pageNum":1,"pageSize":20,"keyword":"口红","priceSelect":"30","rankType":"2","recommendTabType":0}"""
# u = s.decode("UTF-8" )
print(s[336:len(s)])
test = parse.quote(s[336:len(s)])
print(test)

params = {
    "jsv": "2.7.0",
    "appKey": "12574478",
    "t": "1697898927616",
    "sign": "138d02075a244f560268e92047363373",
    "api": "mtop.taobao.content.ic.newstation.itemcenter.item.query",
    "v": "1.0",
    "valueType": "original",
    "preventFallback": "true",
    "type": "originaljsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp7",
    "data": '{"pageNum":1,"pageSize":20,"keyword":"口红","priceSelect":"30","rankType":"2","recommendTabType":0}'
}
pageNum = 1
keyword = "口红"
priceSelect = "30"
rankType = "2"
recommendTabType = 0
dataList = '{"pageNum":' + str(
    pageNum) + ',"pageSize":20,"keyword":"' + keyword + '","priceSelect":"' + priceSelect + '","rankType":"' + rankType + '","recommendTabType":' + str(
    recommendTabType) + '}'
print(dataList)
dataList = parse.quote(dataList)
print(dataList)


def saveExcel(filePath, dfFile):
    if not os.path.exists(filePath):
        dfFile.to_csv(filePath, index=False, header=False, encoding="utf_8_sig")
    else:
        dfFile.to_csv(filePath, mode="a", header=False, index=False, encoding="utf_8_sig")


itemIds = []
itemShopId = []
itemShopName = []
shopPhoneNum = []
df = pd.DataFrame({
    "商家id": itemIds,
    "商店id": itemShopId,
    "商家名称": itemShopName,
    "商家电话": shopPhoneNum
})
saveExcel("demo.csv", df)


def removeRepeat(filePath, shopName):
    if not os.path.exists(filePath):
        df = pd.DataFrame({
            "商家id": [""],
            "商店id": [""],
            "商家名称": [""],
            "商家电话": [""]
        })
        saveExcel(filePath, df)
    df1 = pd.read_csv(filePath, header=None)
    # print(df1)
    # print(df1.iloc[:,2])
    print(type(shopName), type(df1.iloc[:, 5].values))
    print(shopName, df1.iloc[:, 2].values)
    return shopName in str(df1.iloc[:, 5].values)

# while True:
#     # print(removeRepeat("吹风机.csv", "天天特卖工厂店"))
#     # if (removeRepeat("吹风机.csv", "天天特卖工厂店")):
#     #     print("tests")
#     if ("{" in "{fdsfsdfsd"):
#         logger.error("cookie已经消耗完毕！！！")
#         # input("test")

with open("cookiesName.txt", "a", encoding="utf-8") as fp:
    fp.write("\n"+"test")