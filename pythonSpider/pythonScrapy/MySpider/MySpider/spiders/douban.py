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
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            movieItem = MovieItem()
            movieItem['title'] = list_item.css('span.title::text').extract_first()
            movieItem['rank'] = list_item.css('span.rating_num::text').extract_first()
            movieItem['subject'] = list_item.css('span.inq::text').extract_first()
            yield movieItem

        # hrefs_list = sel.css('div.paginator > a::attr(href)')
        # for href in hrefs_list:
        #     url = response.urljoin(href.extract())
        #     yield Request(url=url)
