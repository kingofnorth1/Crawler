import scrapy
from scrapy import Selector, Request
from scrapy.http import Response, HtmlResponse


class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["textlink.simba.taobao.com"]

    def start_requests(self):
        for i in range(1):
            url = "https://textlink.simba.taobao.com/lk?pid=419780_1007&layouttid=375605&number=10&callback=jsonp2los9ufx5"
            yield Request(url=url, encoding='utf-8')

    def parse(self, response, **kwargs):
        # sel = Selector(response)
        # title = sel.css("html").extract_first()
        temp = response.text
        print(temp[temp.find('['):])
        # print(title)
        yield None
