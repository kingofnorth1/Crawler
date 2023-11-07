import scrapy
from scrapy import Selector

from ..items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('html.ua-windows.ua-ff11 body div#wrapper div#content div.grid-16-8.clearfix div.article ol.grid_view li')
        for list_item in list_items:
            movieItem = MovieItem()
            movieItem['title'] = list_item.css('span.title::text').extract_first()
            movieItem['rank'] = list_item.css('span.rating_num::text').extract_first()
            movieItem['subject'] = list_item.css('span.inq::text').extract_first()
            yield movieItem
