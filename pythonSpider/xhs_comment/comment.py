import json
import time
import requests
from utils.sign import x_s, x_s_common
from utils.func import get_a1, read_config


def get_comment(node_id, cursor, root_comment_id, flag='main'):
    try:
        # 6563b84d0000000032032e9a
        url = f'/api/sns/web/v2/comment/page?note_id={node_id}&cursor={cursor}&top_comment_id=&image_formats=jpg,webp'
        if flag == 'sub':
            url = f'/api/sns/web/v2/comment/sub/page?note_id={node_id}&root_comment_id={root_comment_id}&num=10&cursor={cursor}&image_formats=jpg,webp,avif'
        full_url = "https://edith.xiaohongshu.com" + url

        config_data = read_config()
        cookie = config_data.get('cookie', '')
        a1 = get_a1(cookie)

        x_t_v = int(time.time() * 1000)
        x_s_v = x_s(a1, url, {}, 'GET', str(x_t_v))

        x_s_common_v = x_s_common({
            "s0": 5,
            "s1": "",
            "x0": "1",
            "x1": "3.6.8",
            "x2": "Windows",
            "x3": "xhs-pc-web",
            "x4": "3.19.3",
            "x5": a1,
            "x6": x_t_v,
            "x7": x_s_v,
            "x8": "I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeD9MDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR1QL+5Ii6sdnoeSfqYHqwl2qt5BfqJIvFbNLQ+ZPw7Ixdsxuwr4qtkIkrwIi/skZc3ICLdI3Oe0utl2ADZsL5eDSJsSPwXIEvsiVtJOPw8BuwfPpdeTDWOIx4VIiu6ZPwbJqt0IxHyoMAeVutWIvvs1PtnIi+KIEzaeo6s09G1e05sYuttrboe0FFWp9Ke0YqtIx/eDPwmIiJefqtAzZVVOsuwI3deTutA/Yve67zqIhTcIETJQoIkI3TJ8IYgIEhIBuwSIChV+/Kedp5e3qtuI36sja7s0fH4Ik5eirm5KqwfIiKsTove1SKs3PwPmeOedqwVI34LaU6eSqwkpfNsDPwoI3EnI3pkBVw+zPwnB0cnyMos0sosiutsIkKeSjdsVMc1IiAsjr6s3BhMIk/e1qt0IkHUPPwQtut1I3Oe1qtfIkNsVuwTIEosdqt9NVwgeqw7ICiCIxDn8nhY2ZNexPt7IhH8IiNeYuwQZbEqn00sjeHSIEYKPVwQsutaIv3exutW+LgeVldsVDkZIhOsxdJejPtPbVtoI3/sdqwIIigs1URN",
            "x9": -1389025093,
            "x10": 26
        })
        headers = {
            'Host': 'edith.xiaohongshu.com',
            'Cookie': cookie,
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'x-t': str(x_t_v),
            'x-b3-traceid': '804e4ac4598a0ca5',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'accept': 'application/json, text/plain, */*',
            'x-s-common': x_s_common_v,
            'x-s': x_s_v,
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.xiaohongshu.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.xiaohongshu.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }

        response = requests.request("GET", full_url, headers=headers)

        # print(response.text)
        return response.json()
    except Exception as e:
        print(f'请求评论错误：{e.args}')

# get_comment("6563b84d0000000032032e9a")
