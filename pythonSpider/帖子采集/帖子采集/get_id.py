import json
import re
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_xhs_params(i):
    url = "http://127.0.0.1:8000/get?project_name=xhs"
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url=url, headers=headers, json=i, verify=False).json()
    return resp


def get_data(x_s, data):
    cookies = {
        'abRequestId': '65f0cc8e-f23b-578b-b365-d2e53c63cada',
        'xsecappid': 'xhs-pc-web',
        'a1': '18c15c3a584cmn563hjqkvc6q7qanqnrvo0muwp4950000133051',
        'webId': '41ba17d09438474ff276f3508f6df38c',
        'gid': 'yYSy2SqDyJhSyYSy2Sq02lEUY4S6I2KqxVAT84jhSKAWA6280IAIF7888yqq82y8dDS4jqf0',
        'webBuild': '3.18.3',
        'websectiga': '7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4',
        'sec_poison_id': '89198134-a293-47bc-9ba3-b3c1e1ad5095',
        'web_session': '040069b0e8138e12dbecf9ba52374b516591b5',
        'unread': '{%22ub%22:%2265706c2b0000000006021de0%22%2C%22ue%22:%22656be275000000003802f9aa%22%2C%22uc%22:29}',
    }
    headers = {
        # 'x-t': f'{x_s["X-t"]}',
        'x-t': f'1701964826627',
        'x-s': f'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjY1Y2VkMTgzODQwYjJlYjgyYWM5NGZkNDRlNjdkY2VmMjhhYzBmYmMwODZlN2Q2NmU1ZDBhY2JjYWY2NzBiNDEzNjRiYWFjYWJkZGJjNjFkOTQyOTBmZDg5MDYwNGQwM2M5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTdhMTMxNTUyOWFjNzA2MGRjOGQ0ZTk1MzQwYzJhMTAzMzIzMjM2MDI0ZGZjNmJhMjBlNjBhNmMwOTVhYjVmMGQ1ZmExYTI3MDBhMTY4MGFiYmJhNTAzZWRiMWI3ZGVhMjk1ZTcyODRlYzYxMWZlZTkzZDdkMDJjNzdiYWFlNjViZTlhOWRhMDU2YTkzZGM3Yzc0ZWI0NGQzZmE0ZDlhOTQ3ZWY0YWExNmEwZTIxYzhmOTYwMDNiMDViZGI1YTY1ZCJ9',
        'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0rEN0PjNsQh+aHCH0rhGArMGA+Y+/WFG9M1+/GAyBkly780+dr7qnb1qnEU4fuIJgp7qecE+/ZIPeZlPAPI+/rjNsQh+jHCP/qIP/D9+eWU+0GU+UIj2eqjwjQGnp4K8gSt2fbg8oppPMkMank6yLELznSPcFkCGp4D4p8HJo4yLFD9anEd2rSk49S8nrQ7LM4zyLRka0zYarMFGF4+4BcUpfSQyg4kGAQVJfQVnfl0JDEIG0HFyLRkagYQyg4kGF4B+nQownYycFD9ank8PpDUpfT+pB4C/Fzz4MSxafl8yf4Enp4++LEonfTwzbQV/fkDyMDUpfM+yfYingksJpST/g4OzbkV/0QzPDETp/byzrQin/QtySSgn/Qw2DQk/Dzb2DExLfS8pF8xnp4tyMkoafkwyD83/Mzz2LRLcfMyzBqM/Lz84FEoLg4+PDFMnSzwypkTLfY+pMkinpzBJbSxy74yzBPInp4b2DMga/bwzFFA/nMwyFMoL/+wzF8i/gkByLELLfkw2DkxnD4ByDEr8Ap8yfl3npziySkLpflwzBYT/D4BJpSxJBY8PSkx//QnyrMxnfMyprQk/nk8PSSLnfSwzFEx//QwyLEL8BY+prMh/Szp2LRgzfkw2DrU/L4ayDRoL/mypBVl/gkz4MSCafY+prbC/gkQ2DMx//Q+zrDInD4yyDETafY+yDQV/fksyrET/g4Opb8innknJLMoL/byJLphnpzQPFMrcfY+pbDF/L4BypSTafYwprbCnS4ayLMga/+yzM8i/nk3PpkLG7SOzbQVngk82rMgnflypBTCnDzDyFMrafkw2fzknp4BJrExpfSypBli/M4ayrMrp/Q8pBTCnD4+PMSCGAmypFDI/D4z2SkTz/myzBli/MzayrMCnfSOzb8V/gk02DELLgY+pF8knpzd+pkgnfSyprE3/p48PrExyBT8yLiEHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/JDMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRSL98lnLYl49IUqgcMcf8laDS9zfQw/br3nSm7+FShPo+h4g4U+obFyFS3qd4QyaRAyMk0PFSe/BzQPFRSPopFJeQmzbkA/epSzb+tqM+c4MYQzg8Ayp8FaDRc4AYs4g4fLomD8pzrpFRQ2eznanSM+Skc49QtqgcIagYH2nR+cnpn4gzgag89qA8c4rQQyLMCanSiPd+f+d+/+9WMqSpOq98M4ezA//pSp7iFpDl6afp/p7poagYN8n8M4B+QynRAPop7p9QPynkc8omAa/+D8nSl4e+IpA4SPnq3PDSiyAYQznVULn4QyDDALAzla/WhanSC4LQn4MpQ4D4B+BL98nzj+np3pdzeagYmq98SP7PI8opyanWM8/+ryb+cqg4ranTOqA+sadP9L9pAygb7N7QDN9pr4g4xaL+Bz7kmJ9LIqg4V2fh6qM+M49QQPMQNa/+CpDQM49L6qg4dcfkQ/DkIadPIyfpA2b8F8LS3/fp/pLTAPp+PPFS3J7+//e4A2eSQzDS3+9LlLozfanTc4g4c49MwLozeagY98/8M4bSQy9pApS87zrSb8g+fLoc7abm7a9Mc4FbQ4SmDagYM20WE4nDUGFTS2obFzLSiyn+Qy/4SLMm7J9pgG9+IpLRAzo+34LSiLdSFLo472db7cLS38g+gqgzMqLSmqM8B+dPlanQPanSrOaHVHdWEH0ilweWh+ArA+eGFNsQhP/Zjw0ql+7F=',
        'authority': 'edith.xiaohongshu.com',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.xiaohongshu.com',
        'pragma': 'no-cache',
        'referer': 'https://www.xiaohongshu.com/',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-b3-traceid': 'f21ad9da7c6f843a',
    }
    print(headers['x-s'])
    id_list = []
    response = requests.post(
        'https://edith.xiaohongshu.com/api/sns/web/v1/search/notes',
        cookies=cookies,
        headers=headers,
        data=json.dumps(json_data, ensure_ascii=False, separators=(',', ':')).encode())

    with open('xhs.txt', mode='wb') as f:
        f.write(response.content)
    print(response.text)

    data1 = re.findall(r'"id":(.*?),', response.text)
    with open(f'{key_word}_id.txt', mode='w', encoding='utf8') as f:
        for i in data1:
            matches = re.findall(r'"([0-9a-fA-F]+)"', i)
            for match in matches:
                print(match)
                f.write(match + '\n')


if __name__ == '__main__':
    key_word = input('输入搜索的关键词:::')
    json_data = {
        'keyword': f'{key_word}',
        'page': 1,
        'page_size': 20,
        'search_id': '2cjupd9d9ynx6d36c8iir',
        'sort': 'general',
        'note_type': 0,
        'image_scenes': 'FD_PRV_WEBP,FD_WM_WEBP',
    }
    # data = get_xhs_params(i=json_data)
    data = "fdsf"
    get_data(x_s=data, data=json_data)
