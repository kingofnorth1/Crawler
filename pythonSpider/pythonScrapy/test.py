import json

import requests
# -*- coding: utf-8 -*-

# def
demo = """"'fdhdf[[\\u676f\\u5b50","https', '//srd.simba.taobao.com/rd?w=k2textlink&f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%E6%9D%AF%E5%AD%90%26catid%3D%26refpid%3D%26_input_charset%3Dut
f8&k=0a4878fe4c27888a&p=419780_1007&b=_1_1&pvid=0",0,"e2819379e6d6376c5d66940d2adbc7a1'"""

city = '\\u676f\\u5b50'
# print(city.encode(encoding='utf-8'))
print(demo[demo.find('['):])

def get_cookie_dist():
    cookie_str = 'viewed="35081743"; bid=wklddPTlkAo; ll="118318"; ap_v=0,6.0; dbcl2="250285709:Vh5Qlo1+4kw"; ck=bJiD; push_noty_num=0; push_doumail_num=0'
    cookie_dist = {}
    for item in cookie_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        if '"' in value:
            value = value[1:-1]
        cookie_dist[key] = value
    print(cookie_dist)
    return cookie_dist
print(get_cookie_dist())


