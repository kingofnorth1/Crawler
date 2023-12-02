import scrapy
from scrapy.http import Response, Request
import json


class FirstPageSpider(scrapy.Spider):
    name = "firstPage"
    # allowed_domains = ["edith.xiaohongshu.com"]
    # start_urls = []

    def start_requests(self):
        note_id = "61f20d35000000000102e9b5"
        cursor = ""
        for i in range(1, 2):
            url = f"https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
            headers = {
                'authority': 'edith.xiaohongshu.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'no-cache',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'abRequestId=978748a7-11cb-511d-935c-dc8fc43824a7; xsecappid=xhs-pc-web; a1=18b8b7086d97we7juuqtljm9r785oejg02gah9tyu50000246607; webId=f74e61b31f5f66b3c372d9808ae3881e; gid=yYDYDW80Ji80yYDYDW8YKJj9fjWEdWV77A91kv7V6jFWY0282ldVkx888J4KK8W88fq2JiKK; web_session=040069b350603a121e5eeab364374b2a1df371; webBuild=3.15.8; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=f9ba15da-df5c-4698-a79f-5bd221e4d510; unread={%22ub%22:%22655161fa000000001100f12e%22%2C%22ue%22:%22653c9bab000000001f007ab5%22%2C%22uc%22:31}',
                'origin': 'https://www.xiaohongshu.com',
                'pragma': 'no-cache',
                'referer': 'https://www.xiaohongshu.com/',
                'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
                'x-b3-traceid': 'f0795778783b9015',
                'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjQ0NjNkMDAyMjgxODBjZDVhMDAyZjdkMWQ5Y2ExYTdiNzZmNzY4YjUxZmVkYzhhYWM2M2ZmMWI0ZjEwNGIwYzdkNjY4ZDYwZGExNjdlNzc5Y2VhNjQ5MGQ2ZmQyOWJjNWM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTdhMTMxNTUyOWFjNzA2MGRjOGQ0ZTk1MzQwYzJhMTAzMzIzMjM2MDI0ZGZjNmJhMjBlNjBhNmMwOTVhYjVmMGQ1ZmExYTI3MDBhMTY4MGFiYmJhNTAzZWRiMWI3ZGVhMjk1ZTcyODRlYzYxMWZlZTkzZDdkMDJjNzdiYWFlNjViZTlhOWRhMDU2YTkzZGM3Yzc0ZWI0NGQzZmE0ZDlhOTQzNWNiNTk0NGRkNjJiYmE2NjdlMjgwYjE2YmUzZGQ1MyJ9',
                'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0rhN0HjNsQh+aHCH0rhGArMGA+Y+/WFG9M1+/GAyBkly780+dr7qnb1qnEU4fuIJgp7qecE+/ZIPeZlPAPI+/rjNsQh+jHCP/qIP/cAP0HMP/DF+UIj2eqjwjQGnp4K8gSt2fbg8oppPMkMank6yLELznSPcFkCGp4D4p8HJo4yLFD9anEd2rSk49S8nrQ7LM4zyLRka0zYarMFGF4+4BcUpfSQyg4kGAQVJfQVnfl0JDEIG0HFyLRkagYQyg4kGF4B+nQownYycFD9ankzPrEx/fT+zrbE/nkd2rRrcfkyzb8i/Lzm2pkx8BT+pMrMn/Qb2bSL8BSw2SkT/dk8+bSxpgYyJp83ngkiybSg//Q+PSkT/p4QPbkxzg4wzFS7ngkDyFExn/zyzbS7nD4b2rEx8Blw2fPMn/QnyrExL/p+zMrUnfMz2LRgafkwpFFMnSzwypkTLfY+pMkinpzBJbSxy74yzBPInp4b2DMga/bwzFFA/nMwyFMoL/+wzF8i/gkByLELLfkw2DkxnD4ByDEr8Ap8yfl3npziySkLpflwzBYT/D4BJpSxJBY8PSkx//QnyrMxnfMyprQk/nk8PSSLnfSwzFEx//QwyLEL8BY+prMh/Szp2LRgzfkw2DrU/L4ayDRoL/mypBVl/gkz4MSCafY+prbC/gkQ2DMx//Q+zrDInD4yyDETafY+yDQV/fksyrET/g4Opb8innknJLMoL/byJLphnpzQPFMrcfY+pbDF/L4BypSTafYwprbCnS4ayLMga/+yzM8i/nk3PpkLG7SOzbQVngk82rMgnflypBTCnDzDyFMrafkw2fzknp4BJrExpfSypBli/M4ayrMrp/Q8pBTCnD4+PMSCGAmypFDI/D4z2SkTz/myzBli/Mzz2DEg/fSwpBVI/D4ayFExafS8JLLU/fkDJrMx8748yDLUnnMp2SkoL/b+2LiEHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafpDwLMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRSL98lnLYl49IUqgcMcf8laDS9zfQw/br3nSm7+FShPo+h4g4U+obFyFS3qd4QyaRAyMk0PFSe/BzQPFRSPopFJeQmzbkA/epSzb+tqM+c4MYQzg8Ayp8FaDRc4AYs4g4fLomD8pzrpFRQ2eznanSM+Skc49QtqgcIagYH2nR+cnpn4gzgag89qA8n4o+QyLMCanSiPd+f+d+/+9WMqSpOq98M4ezA//pSp7iFpDl6afp/p7poagYN8n8M4B+QynRAPop7p9QPynkc8omAa/+D8nSl4e+IpA4SPnq3PDSiyFlQzpHFL/4UPrDA/n4lpAWhanSC4LQn4MpQ4D4B+BL98nzj+np3pdzeagYmq98SP7PI8opyanWM8/+ryb+cqg4ranTOqA+sadP9L9pAygb7N7QDN9pr4g4xaL+Bz7kmJ9LIqg4V2fh6qM+M49QQPMQYa/+j+DQl47q64g4NJ7+n/DkIadPIyfpAy7pFcDS3J9p/G/+APnQBnLS38g+//e4A2eSQzDS38nL9qgz/anTUJo4n4MbzpdzBagY98/8M4bSQy9pApS87yFSb87+f4gz+/db7+Bpl4A4Q4DlDagYM20WE4p+NnjRS2opFzDSipAYQy/pSLMm7J9pgG9+IpLRAzo+34LSiLdSFLo472db7cLS38g+gqgzMqLSmqM8B+dPlanQPanSrOaHVHdWEH0ilw/W7+AP7PerMNsQhP/Zjw0P9P08R',
                'x-t': '1701432251947'
            }
            payload = {
                "image_scenes": "FD_PRV_WEBP,FD_WM_WEBP",
                "keyword": "口红",
                "note_type": 0,
                "page": 1,
                "page_size": 20,
                "search_id": "2cix4scu3jwjd6mccgfb5",
                "sort": "general",
            }
            jsonText = json.dumps(payload)
            print(jsonText)
            yield Request(url=url, method="post", headers=headers, body=jsonText, callback=self.parse)



    def parse(self, response, **kwargs):
        print(response.text)
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item



    # def start_requests(self):
    #     note_id = "61f20d35000000000102e9b5"
    #     cursor = ""
    #     for i in range(1, 2):
    #         url = f"https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={note_id}&cursor={cursor}&top_comment_id=&image_scenes=FD_WM_WEBP,CRD_WM_WEBP"
    #         headers = {
    #             'authority': 'edith.xiaohongshu.com',
    #             'accept': 'application/json, text/plain, */*',
    #             'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #             'cache-control': 'no-cache',
    #             # Requests sorts cookies= alphabetically
    #             # 'cookie': 'abRequestId=978748a7-11cb-511d-935c-dc8fc43824a7; xsecappid=xhs-pc-web; a1=18b8b7086d97we7juuqtljm9r785oejg02gah9tyu50000246607; webId=f74e61b31f5f66b3c372d9808ae3881e; gid=yYDYDW80Ji80yYDYDW8YKJj9fjWEdWV77A91kv7V6jFWY0282ldVkx888J4KK8W88fq2JiKK; web_session=040069b350603a121e5eeab364374b2a1df371; webBuild=3.15.8; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=f9ba15da-df5c-4698-a79f-5bd221e4d510; unread={%22ub%22:%22655161fa000000001100f12e%22%2C%22ue%22:%22653c9bab000000001f007ab5%22%2C%22uc%22:31}',
    #             'origin': 'https://www.xiaohongshu.com',
    #             'pragma': 'no-cache',
    #             'referer': 'https://www.xiaohongshu.com/',
    #             'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    #             'sec-ch-ua-mobile': '?0',
    #             'sec-ch-ua-platform': '"Windows"',
    #             'sec-fetch-dest': 'empty',
    #             'sec-fetch-mode': 'cors',
    #             'sec-fetch-site': 'same-site',
    #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    #             'x-b3-traceid': 'f0795778783b9015',
    #             'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjQ0NjNkMDAyMjgxODBjZDVhMDAyZjdkMWQ5Y2ExYTdiNzZmNzY4YjUxZmVkYzhhYWM2M2ZmMWI0ZjEwNGIwYzdkNjY4ZDYwZGExNjdlNzc5Y2VhNjQ5MGQ2ZmQyOWJjNWM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTdhMTMxNTUyOWFjNzA2MGRjOGQ0ZTk1MzQwYzJhMTAzMzIzMjM2MDI0ZGZjNmJhMjBlNjBhNmMwOTVhYjVmMGQ1ZmExYTI3MDBhMTY4MGFiYmJhNTAzZWRiMWI3ZGVhMjk1ZTcyODRlYzYxMWZlZTkzZDdkMDJjNzdiYWFlNjViZTlhOWRhMDU2YTkzZGM3Yzc0ZWI0NGQzZmE0ZDlhOTQzNWNiNTk0NGRkNjJiYmE2NjdlMjgwYjE2YmUzZGQ1MyJ9',
    #             'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0rhN0HjNsQh+aHCH0rhGArMGA+Y+/WFG9M1+/GAyBkly780+dr7qnb1qnEU4fuIJgp7qecE+/ZIPeZlPAPI+/rjNsQh+jHCP/qIP/cAP0HMP/DF+UIj2eqjwjQGnp4K8gSt2fbg8oppPMkMank6yLELznSPcFkCGp4D4p8HJo4yLFD9anEd2rSk49S8nrQ7LM4zyLRka0zYarMFGF4+4BcUpfSQyg4kGAQVJfQVnfl0JDEIG0HFyLRkagYQyg4kGF4B+nQownYycFD9ankzPrEx/fT+zrbE/nkd2rRrcfkyzb8i/Lzm2pkx8BT+pMrMn/Qb2bSL8BSw2SkT/dk8+bSxpgYyJp83ngkiybSg//Q+PSkT/p4QPbkxzg4wzFS7ngkDyFExn/zyzbS7nD4b2rEx8Blw2fPMn/QnyrExL/p+zMrUnfMz2LRgafkwpFFMnSzwypkTLfY+pMkinpzBJbSxy74yzBPInp4b2DMga/bwzFFA/nMwyFMoL/+wzF8i/gkByLELLfkw2DkxnD4ByDEr8Ap8yfl3npziySkLpflwzBYT/D4BJpSxJBY8PSkx//QnyrMxnfMyprQk/nk8PSSLnfSwzFEx//QwyLEL8BY+prMh/Szp2LRgzfkw2DrU/L4ayDRoL/mypBVl/gkz4MSCafY+prbC/gkQ2DMx//Q+zrDInD4yyDETafY+yDQV/fksyrET/g4Opb8innknJLMoL/byJLphnpzQPFMrcfY+pbDF/L4BypSTafYwprbCnS4ayLMga/+yzM8i/nk3PpkLG7SOzbQVngk82rMgnflypBTCnDzDyFMrafkw2fzknp4BJrExpfSypBli/M4ayrMrp/Q8pBTCnD4+PMSCGAmypFDI/D4z2SkTz/myzBli/Mzz2DEg/fSwpBVI/D4ayFExafS8JLLU/fkDJrMx8748yDLUnnMp2SkoL/b+2LiEHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafpDwLMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRSL98lnLYl49IUqgcMcf8laDS9zfQw/br3nSm7+FShPo+h4g4U+obFyFS3qd4QyaRAyMk0PFSe/BzQPFRSPopFJeQmzbkA/epSzb+tqM+c4MYQzg8Ayp8FaDRc4AYs4g4fLomD8pzrpFRQ2eznanSM+Skc49QtqgcIagYH2nR+cnpn4gzgag89qA8n4o+QyLMCanSiPd+f+d+/+9WMqSpOq98M4ezA//pSp7iFpDl6afp/p7poagYN8n8M4B+QynRAPop7p9QPynkc8omAa/+D8nSl4e+IpA4SPnq3PDSiyFlQzpHFL/4UPrDA/n4lpAWhanSC4LQn4MpQ4D4B+BL98nzj+np3pdzeagYmq98SP7PI8opyanWM8/+ryb+cqg4ranTOqA+sadP9L9pAygb7N7QDN9pr4g4xaL+Bz7kmJ9LIqg4V2fh6qM+M49QQPMQYa/+j+DQl47q64g4NJ7+n/DkIadPIyfpAy7pFcDS3J9p/G/+APnQBnLS38g+//e4A2eSQzDS38nL9qgz/anTUJo4n4MbzpdzBagY98/8M4bSQy9pApS87yFSb87+f4gz+/db7+Bpl4A4Q4DlDagYM20WE4p+NnjRS2opFzDSipAYQy/pSLMm7J9pgG9+IpLRAzo+34LSiLdSFLo472db7cLS38g+gqgzMqLSmqM8B+dPlanQPanSrOaHVHdWEH0ilw/W7+AP7PerMNsQhP/Zjw0P9P08R',
    #             'x-t': '1701432251947'
    #         }
    #         payload = {
    #             "image_scenes": "FD_PRV_WEBP,FD_WM_WEBP",
    #             "keyword": "口红",
    #             "note_type": 0,
    #             "page": 2,
    #             "page_size": 20,
    #             "search_id": "2cise94o8cky5wm6n7enw",
    #             "sort": "general",
    #         }
    #         jsonText = json.dumps(payload)
    #         print(jsonText)
    #         yield Request(url=url, method="get", headers=headers, callback=self.parse)