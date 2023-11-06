import os

import pandas as pd
import numpy as np
from openpyxl import load_workbook

comment = [1,1,1]
name = ['a','b','c']
address = ['afds','fds','gsfd']
nameList = ['商家名称','商家评论','商家地址']
df = pd.DataFrame({
    "商家名称":name,
    "商家评论":comment,
    "商家地址":address
})
print(df)

file_path = "test.csv"
if not os.path.exists(file_path):
    df.to_csv("test.csv", index=False, header= False)
else:
    path = "test.csv"
    df.to_csv(file_path,mode="a",header=False,index=False)

    # df.to_excel(path,'Sheet1', startrow=3, index=False, header=False)
    # df_old = pd.DataFrame(pd.read_excel(path, sheet_name="Sheet1"))  # 读取原数据文件和表
    # writer = pd.ExcelWriter(path, engine='openpyxl')
    # book = load_workbook(path)
    # writer.book = book
    # writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    # df_rows = df_old.shape[0]  # 获取原数据的行数
    # df.to_excel(writer, sheet_name="Sheet1",
    #             startrow=df_rows + 1,  # 从下一行添加
    #             index=False,  # False
    #             header=False,
    #             encodings="GBK")  # 将数据写入excel中的data表,从第一个空行开始写
    # writer.save()  # 保存
    # book.close()
    # writer.close()



# if not os.path.exists(file_path):
#     df.to_excel(file_path, 'SelectData', index=False)
# else:
#     with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
#         df.to_excel(writer, 'new_sheet', index=False)
