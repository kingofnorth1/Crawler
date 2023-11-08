import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from ..items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    # start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=',
                          callback=self.parse)
            # , meta = {'proxy': 'sock5://127.0.0.1:7980'}

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            detail_url = list_item.css('div.info > div.hd > a::attr(href)').extract_first()
            movieItem = MovieItem()
            movieItem['title'] = list_item.css('span.title::text').extract_first()
            movieItem['rank'] = list_item.css('span.rating_num::text').extract_first()
            movieItem['subject'] = list_item.css('span.inq::text').extract_first()
            yield Request(url=detail_url, callback=self.parse_detail,
                          cb_kwargs={'item': movieItem})

        # hrefs_list = sel.css('div.paginator > a::attr(href)')
        # for href in hrefs_list:
        #     url = response.urljoin(href.extract())
        #     yield Request(url=url)

    def parse_detail(self, response, **kwargs):
        movieItem = kwargs['item']
        sel = Selector(response)
        movieItem['duration'] = sel.css('span[property="v:runtime"]::attr(content)').extract_first()
        movieItem['intro'] = sel.css('span[property="v:summary"]::text').extract_first()
        yield movieItem
