# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

def get_cookie_dist():
    cookie_str = 'abRequestId=65f0cc8e-f23b-578b-b365-d2e53c63cada; xsecappid=xhs-pc-web; a1=18c15c3a584cmn563hjqkvc6q7qanqnrvo0muwp4950000133051; webId=41ba17d09438474ff276f3508f6df38c; websectiga=2845367ec3848418062e761c09db7caf0e8b79d132ccdd1a4f8e64a11d0cac0d; gid=yYSy2SqDyJhSyYSy2Sq02lEUY4S6I2KqxVAT84jhSKAWA6280IAIF7888yqq82y8dDS4jqf0; web_session=040069b0e8138e12dbecf9ba52374b516591b5; webBuild=3.18.1; unread={%22ub%22:%226560bdd3000000003203b79e%22%2C%22ue%22:%2265470788000000001e029272%22%2C%22uc%22:25}; cacheId=12b48636-ce30-4be2-942e-c0b7925370df; sec_poison_id=9aa4f3fe-beac-41e0-8c84-484bcef3e418'
    cookie_dist = {}
    for item in cookie_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        if '"' in value:
            value = value[1:-1]
        cookie_dist[key] = value
    print(cookie_dist)
    return cookie_dist

COOKIE_DIST = get_cookie_dist()

class XiaohongshuSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class XiaohongshuDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIE_DIST
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
