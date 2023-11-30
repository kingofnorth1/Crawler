import scrapy
from scrapy.http import Response, Request
import json


class FirstPageSpider(scrapy.Spider):
    name = "firstPage"
    # allowed_domains = ["edith.xiaohongshu.com"]
    # start_urls = []

    def start_requests(self):
        for i in range(1, 2):
            url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Content-Type': 'application/json;charset=utf-8',
                "Origin": "https://www.xiaohongshu.com",
                'Referer': 'https://www.xiaohongshu.com/',
                'X-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImZjNzY3ZmRiMzUyMzM1MmQxZTUwYzc3NGU0MjAxNjM2N2ZkYmFhZmZmMWE2NzlmMzI3NmZmNGQ4ZjQ3NWY2NzViNTYyNzMzMjE2YjJhZDJiNDAxMDcyOTlmYjI0Y2Q1ZWM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTdhMTMxNTUyOWFjNzA2MGRjOGQ0ZTk1MzQwYzJhMTAzMzIzMjM2MDI0ZGZjNmJhMjBlNjBhNmMwOTVhYjVmMGQ1ZmExYTI3MDBhMTY4MGFiYmJhNTAzZWRiMWI3ZGVhMjk1ZTcyODRlYzYxMWZlZTkzZDdkMDJjNzdiYWFlNjViZTlhOWRhMDU2YTkzZGM3Yzc0ZWI0NGQzZmE0ZDlhOTQ5Mjg3M2Q4OWYxZmU0NWE0YzE5MzBjNDk3NGI1NGNhNyJ9',
                'X-s-Common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0rhN0rjNsQh+aHCH0rhGArMGA+Y+/WFG9M1+/GAyBkly780+dr7qnb1qnEU4fuIJgp7qecE+/ZIPeZlPAPI+/rjNsQh+jHCP/qIP/P9PAcFPAH7PsIj2eqjwjQGnp4K8gSt2fbg8oppPMkMank6yLELznSPcFkCGp4D4p8HJo4yLFD9anEd2rSk49S8nrQ7LM4zyLRka0zYarMFGF4+4BcUpfSQyg4kGAQVJfQVnfl0JDEIG0HFyLRkagYQyg4kGF4B+nQownYycFD9anMyyDECn/+yJpQk/gkp2LMC//b+JpbhnSzp4MSCGA+wzMLI/nkm2rEx//QwPSk3nnMBybkTnfM+pFLU/dkVJLMCa/+wJpkT/D4z+bkxL/+wpMDU/dknyLELngSw2DMC/nkbPSSx…br3nSm7+FShPo+h4g4U+obFyFS3qd4QyaRAyMk0PFSe/BzQPFRSPopFJeQmzbkA/epSzb+tqM+c4MYQzg8Ayp8FaDRc4AYs4g4fLomD8pzrpFRQ2eznanSM+Skc49QtqgcIagYH2nR+cnpn4gzgag89qA8n4BQQyLMCanSiPd+f+d+/+9WMqSpOq98M4ezA//pSp7iFpDl6afp/p7poagYN8n8M4B+QynRAPop7p9QPynkc8omAa/+D8nSl4e+IpA4SPnq3PDSiyURQznTlaB4o8DDAL94Nn0WhanSC4LQn4MpQ4D4B+BL98nzj+np3pdzeagYmq98SP7PI8opyanWM8/+ryb+cqg4ranTOqA+sadP9L9pAygb7N7QDN9pr4g4xaL+Bz7kmJ9LIqg4V2f4NqAmc494Q40YYa/+L+gQl4F4T4gzSGASLNAWIP9pkc/4Sy7p7LrSb/7+gyjRSprzazsHVHdWEH0iTweZEP0DAwePhNsQhP/Zjw0HMwemR',
                'X-t': '1701363573000',
            }
            payload = {
                "image_scenes": "FD_PRV_WEBP,FD_WM_WEBP",
                "keyword": "口红",
                "note_type": 0,
                "page": 2,
                "page_size": 20,
                "search_id": "2cise94o8cky5wm6n7enw",
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
