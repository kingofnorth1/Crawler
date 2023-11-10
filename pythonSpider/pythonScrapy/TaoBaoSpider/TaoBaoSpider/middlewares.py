# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
def get_cookie_dist():
    cookie_str = 'cna=XznLHSv5dCICAXZxgbyHpeab; isg=BHZ2lRHjD4ylp_thW5HoMwR4xKx4l7rRVHwTc-BfmNk6Ixe9SCYV4USVO39PkLLp; l=fBrT6MjrPYSuQEkaBO5IPurza77TXIR48kPzaNbMiIEGa6QO6QUTbNCTOLEXJdtfgTf09etrVskUfdEv-yzLRx90MWpDRs5mpxv9-etzRy1..; _m_h5_tk=4ee3c8c9283b20bf983d8d88dc8a318c_1699590094704; _m_h5_tk_enc=14f85a8fe32e463a4e82ee6e2d8c6dbc; miid=234995322061210715; lLtC1_=1; t=cbf25e580a89d66943517a6b23c3cd75; mt=ci=-1_0; sgcookie=E100lOvJaerJH%2B%2BIU7oQ46ViV8wUdRl0A0kDjmNX2whoQRVa2%2Bg0sfKQI%2FssTo83OXqmZnwGWt2XEeyyXlb96%2BfnLhV0k…zSU80EW6dedixskcJ%2Bc8J0R27pVpwR009bxUw3pJYMDEOjj9VTZncJdZFFzzCuQZlwE8TjCTVe%2BanRW2AFxgsM6jBL562pbhAHbZabkC2bRcGFXwX4Mi4l%2Bq8pz7SxIFTOQpkzKvgWrCuSGlqcjoaSlpx5OsiDqtPyET1k%2BD2hiNHLe8D%2BHVPzwkewj%2Fs0YYE%2B96Lt1Jdzdp7Fw7x1VhFDBz1%2F4TE9XjOJyk%2BdaNqT5UIKMBrOnMazUum%2BrsondoEeMB0mLlJoi8KNMMg3ghzYIymekDtj4aTW61ObJO8Hp2mG4kQGMgmG24JZ3zLvqM%2FR6ciTHW1%2BpckUBUs60xc9dXPhvBR%2Fd0Hb5zZuVXXyjA2ozMONWsA3; cookie2=26af96eab909eb81c94c316f45e8250c; _tb_token_=f8733a337beee; uc1=cookie14=Uoe9ZL2a8cdd6A%3D%3D; thw=cn'
    cookie_dist = {}
    for item in cookie_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        if '"' in value:
            value = value[1:-1]
        cookie_dist[key] = value
    # print(cookie_dist)
    return cookie_dist


COOKIE_ITEM = get_cookie_dist()


class TaobaospiderSpiderMiddleware:
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


class TaobaospiderDownloaderMiddleware:
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
        request.cookies = COOKIE_ITEM
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
