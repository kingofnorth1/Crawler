# -*- coding: utf-8 -*-
import execjs
 

def x_s(a1, url, data_body, method, time_now):
    # 读取 JavaScript 文件内容
    with open('./utils/x_s/x_s_sign.js', 'r', encoding='utf-8') as file:
        x_s_js_code = file.read()

    # 创建一个运行 JavaScript 的环境
    ctx = execjs.compile(x_s_js_code)

    # 调用 JavaScript 函数
    result = ctx.call('x_s_sign', a1, url, data_body, method, time_now)
    # print(result)
    return result


def x_s_common(t):
    with open('./utils/x_s_common/x_s_common_analysis.js', 'r', encoding='utf-8') as file:
        x_s_js_code = file.read()
    ctx = execjs.compile(x_s_js_code)
    result = ctx.call('x_s_common_encode', t)
    return result

# x-s测试
# time_now_ = int(time.time())
# aa = '18c052c8e11b6stqsy8ca1k9cowfzf2oc4untklud50000306503'
# dd = {"keyword": "穿搭", "page": 1, "page_size": 20, "search_id": "2cjxuvvbdja8e8kb3tgzu", "sort": "general",
#       "note_type": 0, "image_formats": ["jpg", "webp"]}
# uu = '/api/sns/web/v1/search/notes'
# x_Sss = x_s(aa, uu, dd, 'POST', time_now_)
#
# # x-s-common 测试
#
# t_c = {
#     "s0": 5,
#     "s1": "",
#     "x0": "1",
#     "x1": "3.6.8",
#     "x2": "Windows",
#     "x3": "xhs-pc-web",
#     "x4": "3.19.3",
#     "x5": aa,
#     "x6": time_now_,
#     "x7": x_Sss,
#     "x8": "I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeD9MDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR1QL+5Ii6sdnoeSfqYHqwl2qt5BfqJIvFbNLQ+ZPw7Ixdsxuwr4qtkIkrwIi/skZc3ICLdI3Oe0utl2ADZsL5eDSJsSPwXIEvsiVtJOPw8BuwfPpdeTDWOIx4VIiu6ZPwbJqt0IxHyoMAeVutWIvvs1PtnIi+KIEzaeo6s09G1e05sYuttrboe0FFWp9Ke0YqtIx/eDPwmIiJefqtAzZVVOsuwI3deTutA/Yve67zqIhTcIETJQoIkI3TJ8IYgIEhIBuwSIChV+/Kedp5e3qtuI36sja7s0fH4Ik5eirm5KqwfIiKsTove1SKs3PwPmeOedqwVI34LaU6eSqwkpfNsDPwoI3EnI3pkBVw+zPwnB0cnyMos0sosiutsIkKeSjdsVMc1IiAsjr6s3BhMIk/e1qt0IkHUPPwQtut1I3Oe1qtfIkNsVuwTIEosdqt9NVwgeqw7ICiCIxDn8nhY2ZNexPt7IhH8IiNeYuwQZbEqn00sjeHSIEYKPVwQsutaIv3exutW+LgeVldsVDkZIhOsxdJejPtPbVtoI3/sdqwIIigs1URN",
#     "x9": -1389025093,
#     "x10": 26
# }
#
# x_s_c = x_s_common(t_c)
# print(x_s_c)
